# Preservation priority queue

## Purpose

This queue ranks external evidence by **risk of irreversible historical loss**, not by fame.

A source should move upward when:

- it is the only known evidence for a fact;
- it lives on an aging/small/personal site;
- it already disappeared once;
- it contains IDs/metadata not reproduced elsewhere;
- a later summary depends on it but does not reproduce enough provenance to reconstruct it;
- it contains participant testimony that cannot be regenerated if the page/account disappears.

For each high-priority cluster, the desired end state is:

`source pack + stable IDs + Wayback snapshot + manifest entry + alternate locator/mirror where possible`

---

# P0 — preserve first

## P0-01 — RonFez.net restored File Library, Gallery and plain-text forum archive

Why:
- primary/near-primary community archive;
- already survived one major restoration;
- has gone offline after restoration;
- contains unique file IDs, photo IDs, filenames, breadcrumbs, comments and uploader metadata.

Existing pack:
- `source-packs/rfnet-restoration-and-archive.md`

Still needed:
- complete inventory of cited RFNet URLs;
- per-record source packs for especially important event/photo/file pages;
- category-page snapshots;
- direct image/media filename mapping where permitted;
- old `displaymedia.cfm` URL inventory.

---

## P0-02 — JustJon's 2023 archive/source-code testimony

Source:
- Reddit `Looking for dot-com era photos`

Why:
- establishes private archive existence;
- establishes original ColdFusion + PHP source-code custody;
- establishes why application/database restoration matters;
- identifies corruption of a second remembered backup.

Existing pack:
- `source-packs/rfnet-restoration-and-archive.md`

Desired future:
- authorized preservation/export conversation with rights holder if feasible;
- checksummed inventory if an export is ever made available.

---

## P0-03 — externally copied historical RFNet `displaymedia.cfm` links

Known source:
- Friends of Tom January 2007 thread

Why:
- external pages may be the only surviving index of dead RFNet numeric media IDs;
- each copied link can reconnect a lost item title/description to an original record number.

Known IDs currently include:
- 2989
- 3004
- 3018

Needed:
- source pack for each external deep-link cluster;
- Wayback snapshot of external page;
- search for additional copied IDs across old boards/blogs.

---

## P0-04 — early physical-community gallery records

Priority cases:
- Christmas Party 2002;
- first RFNet X-Mas party group photos;
- `cp##` packet candidates;
- `dd##` / Double D's candidates;
- Big ASS Night of Fights `nof##` control packet;
- Big Ass Night of Fright;
- New York Forever / bar-crawl material.

Why:
- image bytes alone are insufficient; captions/comments/breadcrumbs often carry the only roster/date/provenance evidence.

Needed per photo:
- photo ID;
- original filename;
- dimensions/filesizes;
- category;
- uploader;
- source/photographer credit;
- displayed migration date;
- historical event date separately;
- comments identifying people.

---

## P0-05 — unique participant memorial/testimony pages

### GVac memorial / Doctor Steve
Why:
- firsthand accounts from many early RFNet participants;
- identity bridge for Greg Petraitis/GVac;
- early-event and board memories;
- FoundryMusicJeff identity/governance testimony.

Source:
- https://www.doctorsteve.com/gvac-memorial/

### Real Radio Ron & Ron/Nature Boy recollection
Why:
- unique memory of smoke/production ritual around Fez's Nature Boy;
- first-person influence testimony from another Florida radio host.

Source:
- https://realradio.iheart.com/featured/as-heard-on-the-monsters/content/2023-04-17-ron-bennington-a-heartfelt-tribute-from-a-grateful-talk-show-host/

Existing Nature Boy pack:
- `source-packs/nature-boy.md`

---

# P1 — highly vulnerable / highly informative

## P1-01 — 2001–03 plain-text RFNet forum archive specimens

Why:
- direct contemporaneous handles/timestamps/signatures/outbound links;
- lets us reconstruct culture without relying on later memory.

Examples already used:
- `t-600.html` — Iris / early culture;
- `t-5402.html` — entertainment/social-board evidence;
- additional event and moderation threads.

Needed:
- thread-level manifest with title, date, forum breadcrumb, key handles and old links.

---

## P1-02 — CDI/H / early outside-board material

Why:
- contemporary 2002 cross-board culture;
- FoundryMusicJeff governance/software statement;
- moderation philosophy;
- evidence that board identities/culture wars predate Board Gossip.

Risk:
- small legacy forum domain.

Needed:
- dedicated source pack;
- Wayback copies;
- thread IDs and exact post timestamps.

---

## P1-03 — Paltalk Big ASS Room page

Why:
- direct platform record;
- room name;
- fan-created description;
- French Bread Pizza ownership;
- `NO BASHING` governance clue.

Risk:
- platform pages can change/disappear independently of historical content.

Needed:
- source pack;
- screenshot/metadata where redistribution rules allow;
- group/room numeric ID;
- current Wayback locator.

---

## P1-04 — old rival-board infrastructure

Includes:
- Wackbag archive snapshots;
- Full Blown Aids references;
- ronfezv3.com traces;
- STI / 3rd Tier / Postwhores leads.

Why:
- Board Gossip and the wider talk-radio web cannot be reconstructed from RFNet alone.

Needed:
- domain/URL table;
- active-date range;
- founders/admins where sourced;
- Wayback snapshots;
- important listening-thread IDs.

---

## P1-05 — 2007 Dave/Casey wedding source cluster

Includes:
- RFNet gallery pages;
- Mike the Teacher photo credits;
- Scott Hudson 2010 near-contemporary account;
- Bronx Johnny Sextravaganza image;
- Lilly Dating Game image.

Why:
- unusually dense example of private life becoming live-show infrastructure.

Needed:
- consolidated source pack with all photo IDs and credits.

---

## P1-06 — Board Gossip debut evidence

Includes:
- full shows 2006-11-06 through 11-10;
- later compilation metadata;
- Fourble/Internet Archive locators;
- 2007 contemporary fan references.

Why:
- central mechanism connecting off-air internet society to the broadcast.

Needed:
- exact full-show filenames;
- timestamps;
- hashes if files can be legitimately processed;
- independent audio locators.

---

## P1-07 — Fez/Nature Boy archive

Existing pack:
- `source-packs/nature-boy.md`

Still needed:
- complete April 10, 2015 2h36m retrospective locator;
- original `Marge Schott` clip year;
- earliest WNEW appearance;
- first XM timestamp;
- 2006 Fezbird full-show locator/timecode;
- 2009/2010 RFNet direct item IDs if recoverable.

---

# P2 — major secondary preservation surfaces

## P2-01 — Internet Archive / Fourble whole-show maps

Why:
- enormous amount of full broadcast audio survives here;
- filenames can establish date provenance even when segment pages disappear.

Risk:
- one institutional archive is still a single point of failure;
- availability outages have already caused users to seek mirrors.

Needed:
- item/filename inventory independent of Fourble UI;
- alternate mirror IDs;
- coverage/gap map by year/month/day.

---

## P2-02 — community Google Drive mirrors

Known public folder IDs/leads:
- `1Q8nNxWec1iFIjJPaSVfMBThhJ4Qd0Ag3`
- `14t3nhNbTf7v5iI8_4RFut9YJWj8hN_oy`

Why:
- independent redundancy during Archive.org outages.

Limit:
- gaps reported by users;
- collections largely derived from existing Internet Archive material;
- folder availability is not guaranteed.

Needed:
- non-invasive inventory of filenames/coverage when publicly accessible;
- compare against Internet Archive map;
- do not re-upload copyrighted recordings to this public repository without rights.

---

## P2-03 — YouTube/Dailymotion segment uploads

Why:
- many bits survive only as fan uploads;
- channels and individual videos are frequently removed.

Preserve for each important upload:
- platform;
- video ID;
- title;
- uploader/channel;
- duration;
- upload date;
- claimed broadcast date;
- actual broadcast date if separately verified;
- timestamps;
- alternate mirrors.

Never make the platform upload date stand in for broadcast date.

---

## P2-04 — modern oral-history podcasts

Examples:
- East Side Dave's *Tales From the Satellite*;
- FezCon interviews;
- modern participant podcasts.

Why:
- first-person recollection can disappear when podcast hosting changes.

Needed:
- RSS/feed identifiers;
- episode title/date/number;
- participant names;
- transcript/notes for claims used by this project;
- audio enclosure URL and checksum when legitimately accessible;
- Wayback snapshot of episode metadata.

---

# P3 — useful but replaceable

Lower priority includes:
- Wikipedia/reference pages for general dates;
- large institutional news pages where the same basic fact has many independent sources;
- generic wrestling results when multiple databases preserve the same event;
- modern articles that only summarize already-preserved primary evidence.

These should remain in the manifest but generally do not need immediate handcrafted source packs.

---

# Preservation backlog by artifact type

## Build next

- `source-packs/gvac-memorial.md`
- `source-packs/foundrymusicjeff-and-early-governance.md`
- `source-packs/christmas-party-2002.md`
- `source-packs/big-ass-night-of-fights-2002.md`
- `source-packs/board-gossip-debut.md`
- `source-packs/paltalk-big-ass-room.md`
- `source-packs/dave-casey-wedding.md`
- `source-packs/whole-show-audio-coverage.md`

## Recovery inventories next

- RFNet cited-page inventory;
- gallery photo-ID inventory;
- old `displaymedia.cfm` ID table;
- full-show audio date/filename coverage matrix;
- YouTube/Dailymotion stable-ID table;
- external forum thread-ID table.

---

# Completion rule

A source is **not considered preserved merely because it has a Wayback URL**.

For critical evidence, preservation means we can still answer these questions if the live page and Wayback UI both become difficult to use:

1. What was the source?
2. What exact historical claim did it support?
3. Who created it and when?
4. What stable identifiers did it contain?
5. Where else might a copy exist?
6. What evidence grade should the claim retain?
7. What would need to be recovered to improve it?

That is the standard this queue is intended to enforce.