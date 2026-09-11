#!/usr/bin/env python3
"""Build and refresh the RonFez external-source preservation manifest.

The script intentionally preserves *metadata and independent archive locators*, not
full third-party copyrighted pages. It can optionally ask the Wayback Machine to
save a bounded number of public pages that lack a recent snapshot.

Stdlib only; designed for GitHub Actions and local use.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "preservation" / "source-manifest.csv"
TEXT_EXTENSIONS = {".md", ".txt", ".yml", ".yaml", ".json", ".csv"}
URL_RE = re.compile(r"https?://[^\s<>\"'`]+", re.IGNORECASE)
USER_AGENT = "RonFez-History-Preservation/1.0 (+https://github.com/BigCatMellow/RonFez)"
MAX_HASH_BYTES = 2 * 1024 * 1024
TIMEOUT = 12

SKIP_PATH_PARTS = {
    ".git",
    ".venv",
    "node_modules",
}

LOW_RISK_ARCHIVE_HOSTS = {
    "archive.org",
    "www.archive.org",
    "web.archive.org",
    "fourble.co.uk",
}

HIGH_PRIORITY_HOST_PARTS = (
    "ronfez.net",
    "reddit.com",
    "paltalk.com",
    "friendsoftom.com",
    "cdih.net",
    "doctorsteve.com",
    "thesmartmarks.com",
    "interrobang.com",
    "profilesarchive.com",
    "scotthudson.blogspot.com",
    "podscan.fm",
    "libsyn.com",
    "dailymotion.com",
    "youtube.com",
    "youtu.be",
)

TRAILING_PUNCT = ".,;:!?)]}"


@dataclass
class SourceRow:
    source_url: str
    cited_in: str
    live_status: str = ""
    final_url: str = ""
    content_type: str = ""
    content_length: str = ""
    sha256: str = ""
    hash_scope: str = ""
    wayback_snapshot: str = ""
    wayback_timestamp: str = ""
    save_attempted: str = "no"
    save_result: str = ""
    checked_at_utc: str = ""


def clean_url(raw: str) -> str:
    u = raw.strip().rstrip(TRAILING_PUNCT)
    # Markdown links occasionally leave a terminal quote encoded by punctuation.
    while u.endswith("%29") and raw.endswith(")"):
        break
    return u


def is_internal_project_url(url: str) -> bool:
    p = urlparse(url)
    host = p.netloc.lower()
    path = p.path.lower()
    if host in {"github.com", "www.github.com", "raw.githubusercontent.com"}:
        return "/bigcatmellow/ronfez" in path
    return False


def iter_text_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        if any(part in SKIP_PATH_PARTS for part in path.parts):
            continue
        # Do not let the generated manifest cite itself.
        if path.resolve() == DEFAULT_OUT.resolve():
            continue
        yield path


def collect_urls(root: Path) -> dict[str, set[str]]:
    found: dict[str, set[str]] = {}
    for path in iter_text_files(root):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        rel = path.relative_to(root).as_posix()
        for match in URL_RE.findall(text):
            url = clean_url(match)
            if not url.startswith(("http://", "https://")):
                continue
            if is_internal_project_url(url):
                continue
            found.setdefault(url, set()).add(rel)
    return found


def priority(url: str) -> tuple[int, str]:
    host = urlparse(url).netloc.lower()
    if any(part in host for part in HIGH_PRIORITY_HOST_PARTS):
        return (0, url)
    if host in LOW_RISK_ARCHIVE_HOSTS or host.endswith("archive.org"):
        return (3, url)
    if host.endswith("wikipedia.org"):
        return (2, url)
    return (1, url)


def fetch_url_metadata(url: str) -> tuple[str, str, str, str, str, str]:
    """Return status, final_url, content_type, length, sha256, hash_scope."""
    headers = {"User-Agent": USER_AGENT, "Accept": "text/html,application/json,text/plain,*/*;q=0.2"}
    req = Request(url, headers=headers, method="GET")
    try:
        with urlopen(req, timeout=TIMEOUT) as resp:
            status = str(getattr(resp, "status", 200))
            final_url = resp.geturl()
            ctype = (resp.headers.get("Content-Type") or "").split(";", 1)[0].strip().lower()
            declared = resp.headers.get("Content-Length") or ""
            length_num = int(declared) if declared.isdigit() else None
            digest = ""
            scope = ""
            textual = ctype.startswith("text/") or ctype in {"application/json", "application/xml", "application/xhtml+xml"}
            if textual and (length_num is None or length_num <= MAX_HASH_BYTES):
                body = resp.read(MAX_HASH_BYTES + 1)
                if len(body) <= MAX_HASH_BYTES:
                    digest = hashlib.sha256(body).hexdigest()
                    scope = "full-response"
                    if not declared:
                        declared = str(len(body))
                else:
                    scope = "too-large"
            return status, final_url, ctype, declared, digest, scope
    except HTTPError as exc:
        return str(exc.code), getattr(exc, "url", url), "", "", "", ""
    except (URLError, TimeoutError, OSError) as exc:
        return f"ERR:{type(exc).__name__}", url, "", "", "", ""


def wayback_available(url: str) -> tuple[str, str]:
    api = "https://archive.org/wayback/available?url=" + quote(url, safe="")
    req = Request(api, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    try:
        with urlopen(req, timeout=TIMEOUT) as resp:
            data = json.loads(resp.read().decode("utf-8", errors="replace"))
        closest = (data.get("archived_snapshots") or {}).get("closest") or {}
        if closest.get("available"):
            snap = closest.get("url") or ""
            ts = closest.get("timestamp") or ""
            return snap, ts
    except Exception:
        pass
    return "", ""


def snapshot_is_recent(timestamp: str, days: int) -> bool:
    if not timestamp or len(timestamp) < 8:
        return False
    try:
        snap = datetime.strptime(timestamp[:8], "%Y%m%d").replace(tzinfo=timezone.utc)
        age = datetime.now(timezone.utc) - snap
        return age.days <= days
    except ValueError:
        return False


def request_wayback_save(url: str) -> str:
    # Anonymous Save Page Now. Failures are recorded rather than treated as fatal.
    save = "https://web.archive.org/save/" + url
    req = Request(save, headers={"User-Agent": USER_AGENT, "Accept": "text/html,*/*;q=0.8"})
    try:
        with urlopen(req, timeout=45) as resp:
            location = resp.headers.get("Content-Location") or resp.geturl()
            status = getattr(resp, "status", 200)
            return f"HTTP {status} {location}"
    except HTTPError as exc:
        return f"HTTP {exc.code}"
    except (URLError, TimeoutError, OSError) as exc:
        return f"ERR:{type(exc).__name__}"


def check_one(url: str, cited_in: set[str]) -> SourceRow:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    status, final_url, ctype, length, digest, scope = fetch_url_metadata(url)
    snapshot, snap_ts = wayback_available(url)
    return SourceRow(
        source_url=url,
        cited_in=" | ".join(sorted(cited_in)),
        live_status=status,
        final_url=final_url,
        content_type=ctype,
        content_length=length,
        sha256=digest,
        hash_scope=scope,
        wayback_snapshot=snapshot,
        wayback_timestamp=snap_ts,
        checked_at_utc=now,
    )


def write_csv(rows: list[SourceRow], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    fields = list(asdict(SourceRow("", "")).keys())
    with out.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--max-checks", type=int, default=0, help="0 = check every discovered URL")
    parser.add_argument("--save-wayback", action="store_true")
    parser.add_argument("--max-saves", type=int, default=30)
    parser.add_argument("--recent-days", type=int, default=180)
    parser.add_argument("--save-delay", type=float, default=2.0)
    args = parser.parse_args()

    sources = collect_urls(args.root)
    ordered = sorted(sources, key=priority)
    if args.max_checks > 0:
        checked_urls = set(ordered[: args.max_checks])
    else:
        checked_urls = set(ordered)

    rows_by_url: dict[str, SourceRow] = {
        url: SourceRow(source_url=url, cited_in=" | ".join(sorted(paths)))
        for url, paths in sources.items()
    }

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = {
            pool.submit(check_one, url, sources[url]): url
            for url in checked_urls
        }
        for fut in as_completed(futures):
            url = futures[fut]
            try:
                rows_by_url[url] = fut.result()
            except Exception as exc:
                row = rows_by_url[url]
                row.live_status = f"ERR:{type(exc).__name__}"
                row.checked_at_utc = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    rows = [rows_by_url[url] for url in ordered]

    if args.save_wayback:
        saves = 0
        for row in rows:
            if saves >= args.max_saves:
                break
            host = urlparse(row.source_url).netloc.lower()
            if host in LOW_RISK_ARCHIVE_HOSTS or host.endswith("archive.org"):
                continue
            if row.live_status and not row.live_status.startswith(("2", "3")):
                # A dead page may still be archivable historically, but Save Page Now
                # cannot rescue content that no longer resolves.
                continue
            if snapshot_is_recent(row.wayback_timestamp, args.recent_days):
                continue
            row.save_attempted = "yes"
            row.save_result = request_wayback_save(row.source_url)
            saves += 1
            time.sleep(max(0.0, args.save_delay))
            # Refresh availability after a successful-ish request when practical.
            if row.save_result.startswith("HTTP 2") or row.save_result.startswith("HTTP 3"):
                snap, ts = wayback_available(row.source_url)
                if snap:
                    row.wayback_snapshot = snap
                    row.wayback_timestamp = ts

    write_csv(rows, args.output)
    print(f"Discovered {len(rows)} external URLs; checked {len(checked_urls)}; manifest: {args.output}")
    if args.save_wayback:
        attempted = sum(1 for r in rows if r.save_attempted == "yes")
        print(f"Wayback Save Page Now attempts: {attempted}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
