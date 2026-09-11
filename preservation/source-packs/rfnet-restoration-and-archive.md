# Source pack — RonFez.net restoration, backups, and archive survival

## Why this pack exists

RonFez.net is both a historical source **and a preservation warning**.

Parts of its media were already lost or broken during earlier platform/forum changes. The site was later restored as a memorial archive, went offline again for a period, and came back. A large fraction of this project's early-community evidence currently depends on that restored copy.

Therefore:

> **RonFez.net must be treated as a rescued collection that could require rescuing again.**

Primary forensic reconstruction:
- `../../community/02-ronfez-net-history-and-structure.md`
- `../../reference/10-rfnet-media-url-reconstruction.md`
- `../../reference/11-rfnet-gallery-packet-reconstruction.md`

---

## RFN-P01 — July 2022 warning that old image material had already broken/disappeared

**URL**
- https://www.reddit.com/r/ronandfez/comments/wbl57p

**Thread**
- `Is there a picture gallery out there of the WNEW days?`

**What participants remember**

A user says a great deal of old photo material was lost/broken when RonFez.net changed forums or underwent a platform change. Another user reports using Archive.org/Wayback to reach a large amount of 2005-era imagery.

**What this establishes**
- archive loss/broken media was already a known community problem before the 2023 restoration;
- Wayback had already functioned as an auxiliary copy for some historical photos.

**Evidence type**
- C/E community recollection; useful preservation history rather than proof of the exact technical failure.

---

## RFN-P02 — January 8, 2023: JustJon says he has an RFNet archive

**URL**
- https://www.reddit.com/r/ronandfez/comments/106pdfx

**Thread**
- `Looking for dot-com era photos`

This is one of the most important preservation sources in the project.

A participant identifying as **JustJon** says, in substance:

- he has an **archive of RonFez.Net** that he needs to go through;
- he believes the pictures are present;
- they are not organized in a way that is easy to inspect without bringing the site back up;
- Mikeyboy had told him that Mikeyboy's own hard-drive backup was corrupted.

Later in the same discussion JustJon publicly states that:

- he had owned RonFez.Net for roughly twenty years;
- he was the forum administrator;
- he owns the **original source code**, both the **ColdFusion** version and the **PHP** version;
- the site would stay up as a memorial archive.

**Why this matters technically**

This gives the project a direct explanation for why restoring RFNet as an application could reveal relationships that are not visible in a loose directory of files:

- database IDs;
- gallery records;
- original filenames;
- category relationships;
- old media-address conventions;
- migration mappings.

It also establishes that at least one historically important backup existed outside the public web in 2023.

**Evidence type**
- C/A-adjacent participant first-person statement about his own archive/ownership.

**Preservation priority:** critical.

---

## RFN-P03 — January 16, 2023 memorial archive relaunch

**URL**
- https://www.reddit.com/r/ronandfez/comments/10drznn/the_fez_marie_whatley_memorial_ronfeznet_media/

**Thread title**
- `The Fez Marie Whatley Memorial RonFez.Net Media Archives`

The relaunch announcement says that RonFez.net was brought back as the **Fez Marie Whatley Memorial RonFez.Net Media Archives**, specifically restoring the **File Library and Gallery** for public browsing.

Comments immediately reveal two archival limits:

- the forums themselves were not restored for ordinary reading/login;
- some media links still pointed toward dead/defunct FoundryMusic locations.

**What it establishes**
- exact restoration framing and purpose;
- File Library + Gallery were deliberate preservation targets;
- restoration was incomplete at the level of every original link/resource.

---

## RFN-P04 — January 2023 first-Christmas-party material proves restoration recovered otherwise opaque social history

**URL**
- https://www.reddit.com/r/ronandfez/comments/10dvfb9

**Thread**
- `First RF.NET X-Mas party`

An apparent participant says the photograph was labeled, identifies the year as **2002**, and thanks JustJon for bringing the archive back. The discussion identifies old civilian-community figures and remembers additional group photographs.

**Preservation significance**

This is a concrete example of the restoration doing more than serving nostalgia:

`restored image → old participants recognize themselves/others → lost event chronology and civilian roster become recoverable`

If the restored image and the discussion both disappeared, a substantial part of the first RFNet Christmas-party reconstruction would disappear with them.

---

## RFN-P05 — February 2024: site down again

**URL**
- https://www.reddit.com/r/ronandfez/comments/1al797d

**Thread**
- `Who owns RonFez.net?`

A user reports that RonFez.net is down and specifically regrets not saving more of the historical photographs while the restored site was available. Other participants identify JustJon as the owner and remember that the site had been turned on for FezCon.

**Preservation significance**

This is direct community evidence that the 2023 restoration was **not continuously available afterward**.

It validates the project's pessimistic preservation assumption:

> a restored source can disappear again.

---

## RFN-P06 — surviving gallery-scale statistics

Representative surviving gallery pages expose the restored archive's site statistics. Example:

- https://www.ronfez.net/gallery/showphoto.php/photo/2030/ppuser/35895

Visible current/restored statistics include approximately:

- **38,387 users**;
- **4,932 photos**;
- **881 comments**;
- hundreds of megabytes of gallery storage;
- very large accumulated view counters.

Another representative gallery page:
- https://www.ronfez.net/gallery/showphoto.php/photo/4497/ppuser/34794

**Preservation use**

These statistics provide a rough inventory benchmark. If a future restored copy contains dramatically fewer than ~4,932 gallery records, that is evidence that the surviving collection has changed or become incomplete.

Do not treat view counters as historical audience measurements.

---

## RFN-P07 — original/migrated gallery metadata is itself historical evidence

Representative page:
- https://www.ronfez.net/gallery/showphoto.php/photo/3412/ppuser/mobiquo/tapatalkdetect.js

This surviving Christmas Party 2007 page preserves several layers simultaneously:

- event breadcrumb;
- image title;
- Mikeyboy as uploader/curator;
- original-source credit (`Picture courtesy of FleaMan`);
- displayed upload/gallery date;
- image dimensions/filesizes;
- participant identities.

This is why preserving only image bytes would be insufficient.

For RFNet photographs, **page metadata and comments can be as historically important as the photograph itself**.

---

# External copies / alternate media archives

These are not substitutes for primary RFNet metadata, but they reduce single-point failure.

## RFN-M01 — Internet Archive / whole-show collections

The repository's whole-show map documents Internet Archive-backed full-show collections and Fourble indexing:
- `../../reference/07-whole-show-archive-map.md`

Internet Archive remains a major independent copy surface for broadcast audio.

Risk: Internet Archive itself can be temporarily unavailable and should not be treated as the only copy.

---

## RFN-M02 — 2024 community Google Drive copy of R&F/O&A/other radio audio

**URL / discussion**
- https://www.reddit.com/r/ronandfez/comments/1f59uie

A community member says they copied available Ron & Fez material from Internet Archive into Google Drive for faster/easier access.

**Preservation value**
- independent storage copy of material already circulating in public fan archives;
- potentially useful during Internet Archive outages.

**Limit**
- commenters note gaps in some folders;
- the collection appears substantially derived from Internet Archive rather than containing a major independent pre-2001 corpus.

Do not treat it as complete.

---

## RFN-M03 — 2025 updated Google Drive archive

**Discussion**
- https://www.reddit.com/r/ronandfez/comments/1iv9w1n

The poster says they downloaded all Ron & Fez shows available on Internet Archive and put them into Google Drive. The publicly posted folder locator is:

- `1Q8nNxWec1iFIjJPaSVfMBThhJ4Qd0Ag3`

The stable Google Drive folder ID should be preserved independently of the full share URL because share parameters can change.

Comments again note temporary/missing folders, reinforcing that mirrors must be **inventoried**, not assumed complete.

---

## RFN-M04 — October 2024 alternate Drive during Internet Archive outage

**Discussion**
- https://www.reddit.com/r/ronandfez/comments/1g0guxu

During an Internet Archive outage, users shared another Google Drive folder:

- stable folder ID: `14t3nhNbTf7v5iI8_4RFut9YJWj8hN_oy`

Comments note that several R&F folders were empty.

**Preservation lesson**

Redundancy is useful, but a mirror without an inventory/checksum can create a false sense of completeness.

---

## RFN-M05 — April 2026 claim of additional WNEW-era recordings

**URL**
- https://www.reddit.com/r/ronandfez/comments/1sts0n5

A participant says they possess approximately **three years of O&A and Ron & Fez from the WNEW days** and offers to post/share it if people are interested.

This is a **lead**, not yet a preserved collection.

Because pre-2001/early-WNEW material is among the largest gaps in the public corpus, this person/source is a high-value future preservation contact if their material is actually made public.

Do not claim the tapes are unique until compared against existing archive holdings.

---

# Historical URL architecture that must be preserved

Old externally copied RFNet media links prove the historical format:

`http://www.ronfez.net/displaymedia.cfm/id/<number>`

The restored File Library uses:

`https://www.ronfez.net/forums/downloads.php?do=file&id=<number>`

Known old externally preserved IDs include:

- `2989`
- `3004`
- `3018`

Known restored direct-file anchors include:

- `1986`
- `2038`
- `2243`

See:
- `../../reference/10-rfnet-media-url-reconstruction.md`

Even when a URL dies, **the numeric ID must remain in the historical record**.

---

# Gallery packet filenames that must be retained

The restored gallery demonstrates that legacy packet filenames can survive migration.

Known/research-useful examples include:

- `nof25` — directly tied to Big ASS Night of Fights II;
- `cp26` — candidate Christmas Party 2002 packet member;
- `dd16` — candidate Double D's packet member.

See:
- `../../reference/11-rfnet-gallery-packet-reconstruction.md`

These terse names can become reconstruction keys if categories or captions disappear.

---

# Preservation actions for RFNet

## Automated

The repository-wide preservation workflow should:

- enumerate every cited RonFez.net URL;
- check live status;
- store final URL/content type/size;
- hash eligible text responses;
- record Wayback availability;
- request fresh Wayback copies when appropriate.

## Manual / forensic

For especially important gallery/file/forum records, create a source pack containing:

- URL;
- numeric ID;
- title;
- breadcrumb/category;
- displayed dates;
- original dates where separately known;
- uploader;
- photographer/source credit;
- dimensions/filesize;
- historically useful comments;
- relationship to unresolved cases.

## Desired future backup

If the owner/rights holder ever makes an authorized export available, the ideal institutional preservation package would include:

- ColdFusion source tree;
- PHP source tree;
- database dump/schema;
- gallery image files;
- file-library media files for which redistribution is permitted;
- original filename/path mapping;
- forum archive/database where privacy and rights allow;
- migration notes;
- checksums/manifests.

That would make future restoration possible without depending on the current live server.

---

# Core conclusion

RonFez.net is not simply another citation source.

It is itself a historical artifact that has already passed through:

`original live community → broken/migrated material → private backup → memorial restoration → later outage → renewed availability`

That lifecycle is precisely why this project should preserve **provenance, identifiers, metadata, independent snapshots and redundant locators now**, while the material remains reachable.