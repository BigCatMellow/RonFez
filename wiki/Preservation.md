# Preserving the Ron & Fez Record

This project assumes a simple problem:

> **Anything on the public web can disappear.**

That matters more than usual for Ron & Fez because much of the history survives outside conventional institutional archives. Important evidence currently lives on old fan forums, restored RonFez.net pages, personal blogs, Reddit posts, Paltalk pages, YouTube uploads, Dailymotion, old event galleries and community-maintained audio indexes.

Some of this material has already disappeared once and only exists because somebody restored or mirrored it.

The archive therefore treats **preservation as part of research**, not as something to do after the history is finished.

---

## What we preserve for every important source

Whenever possible, the repository records:

- original URL;
- source/site identity;
- page/thread/media title;
- publication or post date;
- what historical claim the source actually establishes;
- evidence grade;
- stable IDs such as thread IDs, gallery photo IDs, video IDs and Internet Archive item names;
- live HTTP status;
- redirect target;
- content type/size when recoverable;
- SHA-256 fingerprint for reasonably small text pages;
- Internet Archive / Wayback snapshot;
- repository files that rely on the source;
- alternate copies or mirrors.

A URL by itself is no longer considered enough.

---

## Automatic preservation

The repository now contains an automated preservation system:

- [`scripts/preserve_sources.py`](https://github.com/BigCatMellow/RonFez/blob/main/scripts/preserve_sources.py)
- [`.github/workflows/preserve-sources.yml`](https://github.com/BigCatMellow/RonFez/blob/main/.github/workflows/preserve-sources.yml)

It scans the research archive for external URLs and builds:

- [`preservation/source-manifest.csv`](https://github.com/BigCatMellow/RonFez/blob/main/preservation/source-manifest.csv)

The workflow also checks for a Wayback Machine snapshot and makes a **bounded, rate-limited Save Page Now request** for high-risk public sources when a reasonably recent snapshot is missing.

This runs on a schedule and can be triggered manually.

---

## Why we do not simply copy every webpage into GitHub

Preservation is not permission to republish somebody else's complete copyrighted article, book, radio show or video.

For most third-party material the project instead preserves:

1. source metadata;
2. a narrow evidentiary description;
3. short excerpts only when necessary;
4. stable identifiers;
5. checksums/fingerprints;
6. independent Internet Archive snapshots;
7. alternate locators.

Full local copies are appropriate when the project owns the material, redistribution is licensed/permitted, or the material is public domain.

This approach preserves the **historical evidence chain** without turning the repository into an unauthorized mirror of entire third-party collections.

---

# Media requires special treatment

## Radio/audio

A recording should ideally retain:

- exact broadcast date;
- full-show filename;
- archive item identifier;
- segment title;
- timestamp;
- duration/file size;
- uploader/archive attribution;
- checksum where legitimately obtainable;
- alternate mirrors.

The long-term goal is that losing one YouTube upload does not make a segment unidentified.

## Photographs

For RFNet photographs we preserve, where available:

- gallery photo ID;
- original packet filename such as `nof25`, `cp26`, or `dd16`;
- gallery breadcrumb/category;
- image dimensions;
- migration/upload date;
- original event date separately;
- uploader/curator;
- original photographer/source;
- comments identifying people;
- archived page location.

This is particularly important because restored RFNet pages often have **2007 migration dates attached to photographs of much earlier events**.

## Forum posts

For important forum evidence we preserve:

- thread ID and title;
- forum breadcrumb;
- username/handle;
- exact post date/time;
- minimum relevant text;
- embedded historical URLs;
- Wayback copy.

An old thread can disappear while a copied link or quoted fragment becomes the only surviving evidence of an event.

---

# Topic source packs

Major subjects also receive curated preservation packets under:

[`preservation/source-packs/`](https://github.com/BigCatMellow/RonFez/tree/main/preservation/source-packs)

The first is:

- [Fez Whatley's Nature Boy](https://github.com/BigCatMellow/RonFez/blob/main/preservation/source-packs/nature-boy.md)

These packs are meant to answer a future researcher's worst-case question:

> **The original page is gone. What exactly did it say that mattered, where did it come from, and how might I recover it?**

---

# Highest-risk material

The archive gives highest preservation priority to:

1. **RonFez.net** — already the product of a rescue/restoration;
2. unique first-person testimony from staff, fans and participants;
3. pages containing dead historical RFNet links or numeric media IDs;
4. event/photo pages with original metadata;
5. obscure audio/video uploads with no known duplicate;
6. contemporary fan discussions documenting what listeners knew at the time;
7. personal blogs and small forums with uncertain longevity.

General facts available from many institutional sources are lower risk.

---

# The preservation rule

For an important claim, the ideal chain is:

`historical claim`

→ `research note explaining the evidence`

→ `original URL + stable ID`

→ `Wayback/independent snapshot`

→ `content fingerprint`

→ `alternate source or copy`

The project will never capture everything. But if the current web slowly disappears, this structure should leave enough provenance behind to **reconstruct rather than start over**.

For the full technical policy, see:

- [Source preservation README](https://github.com/BigCatMellow/RonFez/blob/main/preservation/README.md)