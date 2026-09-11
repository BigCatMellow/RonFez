# Source preservation

## Purpose

This directory exists because the Ron & Fez historical record is unusually vulnerable to **link rot**.

The project currently depends on material spread across:

- RonFez.net's restored forum, gallery and file library;
- Internet Archive collections;
- YouTube and Dailymotion uploads;
- Reddit and surviving message boards;
- personal blogs and memorial pages;
- publisher episode listings;
- old event pages and photo galleries;
- news sites;
- Paltalk and other aging platforms;
- pages that already survive only because somebody else archived or restored them.

The preservation assumption is deliberately pessimistic:

> **Any external source we can read today may be unavailable tomorrow.**

Research files therefore should not depend on a bare URL as the only surviving evidence.

---

## Preservation layers

### Layer 1 — canonical research record

Every source should be represented in the repository with enough context to answer:

- what was the URL?
- what claim did it support?
- when did we inspect it?
- what type of source was it?
- was it direct, contemporary, retrospective or merely a lead?

This is the minimum layer and remains useful even if the source disappears.

### Layer 2 — automated source manifest

`scripts/preserve_sources.py` scans the repository for external URLs and produces:

- `preservation/source-manifest.csv`

For each discovered URL the manifest can record:

- files in this repository that cite it;
- live HTTP status;
- final redirected URL;
- content type and length when available;
- a SHA-256 content fingerprint when a reasonably small text response can be fetched completely;
- latest Wayback snapshot returned by the Internet Archive availability service;
- whether a fresh Save Page Now request was attempted;
- timestamp of the preservation check.

A hash is **not a copy**, but it can later prove whether a recovered page is the same version we inspected.

### Layer 3 — independent web archive copy

The preservation workflow asks the Internet Archive's Wayback Machine to save high-risk public web pages when no reasonably recent snapshot is available.

That creates an independently hosted copy without republishing entire third-party pages inside this public GitHub repository.

This is the preferred strategy for ordinary copyrighted web pages, forum pages and articles.

### Layer 4 — topic source packs

Historically important subjects should also receive a curated source pack under:

- `preservation/source-packs/`

A source pack preserves:

- exact source identity;
- publication/date information;
- the narrow fact it establishes;
- a short evidentiary excerpt when useful;
- archive/snapshot locations;
- unresolved questions;
- replacement/recovery leads.

The source pack should remain useful if the original page disappears.

### Layer 5 — permitted full copies

A full local copy may be retained when the material is:

- authored/owned by this project;
- explicitly licensed for redistribution;
- public domain;
- otherwise clearly permitted to be mirrored.

For ordinary third-party copyrighted articles, books, audio and video, the repository should **not** silently mirror the entire work merely because it is historically useful.

Instead preserve:

- metadata;
- source URL;
- archive URL;
- identifiers;
- checksums where obtainable;
- short evidentiary excerpts;
- timestamps/timecodes;
- enough description to know exactly what was lost.

---

## Media preservation policy

### Radio/audio

For a surviving R&F recording, preserve as much of the following as possible:

- broadcast date;
- segment title;
- full-show filename;
- Internet Archive item identifier;
- Fourble/index position when applicable;
- YouTube/Dailymotion video ID when applicable;
- duration;
- file size;
- known timestamps;
- uploader/archive attribution;
- checksum if a legitimately accessible copy can be processed;
- alternate mirrors.

Do not depend on a single YouTube URL.

### Images

Preserve:

- gallery photo ID;
- original filename (`nof25`, `cp26`, `dd16`, etc.);
- event/category breadcrumb;
- displayed migration/upload date;
- original event date separately;
- image dimensions;
- uploader/curator;
- photographer/source credit;
- comments identifying subjects;
- Wayback snapshot where available.

The filename and record ID can remain historically useful even when the image bytes disappear.

### Forums

Preserve:

- thread ID;
- thread title;
- forum breadcrumb;
- usernames/handles relevant to the evidence;
- exact post timestamps;
- quoted fragment needed for the historical claim;
- embedded/outbound historical URLs;
- Wayback copy.

Private/deleted material should not be reconstructed from unrelated personal information.

---

## What *not* to do

Do not:

- assume Internet Archive will always retain a page because it is there today;
- treat a Google/Bing snippet as a permanent archive;
- copy entire copyrighted articles into GitHub without permission;
- upload complete copyrighted radio/audio/video merely because the original host may disappear;
- collapse restoration date and historical event date;
- remove a dead URL from the record merely because it no longer resolves;
- overwrite an old source URL with a modern replacement without preserving the original locator.

A dead URL is still evidence about provenance.

---

## Automation

Workflow:

- `.github/workflows/preserve-sources.yml`

Script:

- `scripts/preserve_sources.py`

The workflow runs on a schedule and can also be run manually. It:

1. scans repository text files for external URLs;
2. refreshes the source manifest;
3. checks live status and Wayback availability;
4. asks Wayback to save a bounded number of high-risk sources lacking a recent snapshot;
5. commits the refreshed manifest back to the repository.

The Save Page Now requests are intentionally rate-limited and bounded. Preservation should not become abusive crawling.

---

## Priority order

Highest preservation priority:

1. **RonFez.net original/restored pages** — primary community archive and already the product of one rescue;
2. **unique participant testimony** — personal blogs, memorial pages, old forums, posts by staff/fans;
3. **pages preserving dead historical RFNet links or IDs**;
4. **event/photo pages with original metadata**;
5. **episode indexes and full-show locator pages**;
6. **third-party contemporary discussion**;
7. **later retrospective fan memory**;
8. easily replaced general-reference pages.

---

## Long-term goal

The ideal future state is that every historically material claim can be traced through a chain like:

`claim`

→ `repository evidence note`

→ `original URL + source identity`

→ `independent archived snapshot`

→ `content fingerprint / stable identifier`

→ `alternate source or mirror where available`

That will not make the archive indestructible, but it substantially reduces the chance that one dead website erases part of the story.