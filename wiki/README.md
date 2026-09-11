# Canonical GitHub Wiki Source

This directory is the **version-controlled source of truth for the reader-facing Ron & Fez wiki**.

GitHub stores a repository's visible Wiki in a separate Git repository named:

`BigCatMellow/RonFez.wiki.git`

The normal GitHub Contents API used for the main repository does not directly manage those Wiki pages. Keeping the source here solves two problems:

1. every wiki change is reviewed and preserved alongside the forensic archive;
2. the public GitHub Wiki can be regenerated from these files instead of becoming a separate, drifting history.

## Pages

- `Home.md` — main reader entry point
- `_Sidebar.md` — Wiki navigation
- `Living-Story-of-Ron-and-Fez.md` — continuously maintained compiled oral history
- `Timeline.md` — chronological map
- `People-and-Cast.md` — cast genealogy and biographies
- `The-Secondary-Universe.md` — RFNet, Paltalk, boards, community and distribution infrastructure
- `Live-Events.md` — physical-event history
- `Comedy-Bits-and-Formats.md` — comedy mechanisms and recurring formats
- `Music-and-Sonic-Identity.md` — music, production and sonic vocabulary
- `Work-Shoot-and-What-We-Know.md` — work/shoot analysis and evidence boundaries
- `Archives-Sources-and-Evidence.md` — source/evidence methodology and archive recovery

## Editing rule

The forensic repository remains authoritative for detailed claims.

When new evidence changes the history:

1. update the relevant chronology/community/person/event/forensics/reference file;
2. update the reader-facing wiki page if the synthesis materially changes;
3. sync `wiki/` to the GitHub Wiki;
4. preserve uncertainty rather than making the public narrative cleaner than the evidence.

## Sync to the visible GitHub Wiki

From a local clone of this repository on Windows:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync-wiki.ps1
```

The script:

1. clones `BigCatMellow/RonFez.wiki.git` into a temporary directory;
2. copies the canonical Markdown pages from `wiki/`;
3. does **not** publish this `README.md` as a Wiki page;
4. commits only when the Wiki content changed;
5. pushes the Wiki repository.

It uses the Git credentials already configured for `git` on the machine. It does not store a token or password in this repository.

## Why the Living Story is separate from the forensic chronology

The chronology files are designed to retain evidence, qualifications and research questions by era.

The Living Story has a different purpose: it should read coherently from beginning to end and braid together voices from the archive—broadcast history, participant recollections, contemporary community records, later fan memory and unresolved lore—without pretending to be a verbatim transcript.

The two layers should correct one another:

`forensic evidence → living narrative → new evidence → corrected forensic record → updated narrative`

That loop is intentional.