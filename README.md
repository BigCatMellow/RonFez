# Ron & Fez — Living History, Archive, and Forensic Reference

This repository is a long-form historical reconstruction of **The Ron & Fez Show** and the unusually large social world that formed around it.

It now has two deliberately different layers:

1. **the reader-facing living history** in [`wiki/`](wiki/), including a compiled oral-history-style story of the show;
2. **the forensic archive** in `chronology/`, `community/`, `people/`, `events/`, `themes/`, `forensics/`, and `reference/`, where claims, sources, contradictions, unresolved lore, archive recovery and corrections are preserved in detail.

The goal is not merely to summarize the program. It is to reconstruct **how the system worked**: hosts, staff, callers, fictional characters, RonFez.net, Paltalk, rival boards, live events, music, fan creators, archivists, friends of the show, work/shoot ambiguity, physical community and the post-show preservation network.

## Start here

### [`wiki/Home.md`](wiki/Home.md)
The reader-facing entrance to the project.

### [`wiki/Living-Story-of-Ron-and-Fez.md`](wiki/Living-Story-of-Ron-and-Fez.md)
The main continuously maintained narrative. It reads as a **compiled oral history** rather than an encyclopedia entry, braiding surviving broadcasts, contemporary records, participant testimony, fan memory and unresolved lore without fabricating a transcript.

### Reader guides

- [`wiki/Timeline.md`](wiki/Timeline.md) — full era map from *Ron & Ron* through the 2026 archive/reconstruction period
- [`wiki/People-and-Cast.md`](wiki/People-and-Cast.md) — hosts, staff, fictional callers, civilians, creators and cast pathways
- [`wiki/The-Secondary-Universe.md`](wiki/The-Secondary-Universe.md) — RonFez.net, Paltalk, boards, fan streaming, community hierarchy and afterlife
- [`wiki/Live-Events.md`](wiki/Live-Events.md) — fights, bar culture, weddings, parties, simulcasts and memorial events
- [`wiki/Comedy-Bits-and-Formats.md`](wiki/Comedy-Bits-and-Formats.md) — Comedy Pyramid through Cakehorn/Steakgate and failure-as-format
- [`wiki/Music-and-Sonic-Identity.md`](wiki/Music-and-Sonic-Identity.md) — deep tracks, rejoiners, openers, production and ritual music
- [`wiki/Work-Shoot-and-What-We-Know.md`](wiki/Work-Shoot-and-What-We-Know.md) — reality ambiguity and current forensic conclusions
- [`wiki/Archives-Sources-and-Evidence.md`](wiki/Archives-Sources-and-Evidence.md) — evidence grades, surviving archives, media-ID recovery and correction method

## GitHub Wiki publishing

GitHub stores the visible Wiki in a separate Git repository (`BigCatMellow/RonFez.wiki.git`), while the standard repository Contents API manages this main repository.

To prevent the public Wiki and the forensic project from drifting apart, [`wiki/`](wiki/) is now the **canonical version-controlled source**.

On Windows, after pulling this repository, sync the canonical pages to the visible GitHub Wiki with:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync-wiki.ps1
```

The script clones the separate Wiki repository, copies all publishable Markdown pages, commits only when something changed, and pushes using the Git credentials already configured on the machine. It does not store credentials in this repository.

See [`wiki/README.md`](wiki/README.md).

---

# Governing rule

**No detail is too small.**

Obscure callers, forgotten board handles, one-off event details, deep-track music choices, rejoiners, production quirks, tiny phrases, contradictory recollections, fan-created songs, intern arcs, photo captions and uncertain lore all belong here when they can be sourced or clearly labeled as uncertain.

The intended direction is **more detail, not compression**.

The living-history layer makes that detail readable. It does not delete it.

---

# Central historical model

The repository increasingly supports a view of *Ron & Fez* as a **bidirectional social/media system**, not merely a talk show with hardcore fans.

At different times the audience functioned as:

- writers' room;
- caller pool;
- character pipeline;
- rumor network;
- town square;
- live audience room;
- physical social scene;
- fan-media production network;
- unofficial WJFK distribution system;
- archive;
- mutual-aid network;
- memorial community;
- historical research network.

The core loop was:

`SHOW ↔ COMMUNITY`

A show event could become a board argument. The board argument could become Board Gossip. The radio attention could change the board argument. A Friday bar incident could become Monday radio. A fan could make a song, photograph an event, run a Paltalk room or preserve audio, and that work could re-enter the program.

That is why the community is treated as part of the show's **production system**, not an appendix.

---

# Repository map

## [`chronology/`](chronology/)
Narrative history by era.

1. [`01-roots-ron-and-ron.md`](chronology/01-roots-ron-and-ron.md)
2. [`02-wnew-2000-2003.md`](chronology/02-wnew-2000-2003.md)
3. [`03-fairfax-wjfk-2003-2005.md`](chronology/03-fairfax-wjfk-2003-2005.md)
4. [`04-xm-2005-2007.md`](chronology/04-xm-2005-2007.md)
5. [`05-maximum-density-2007-2009.md`](chronology/05-maximum-density-2007-2009.md)
6. [`06-dave-fez-2009-2010.md`](chronology/06-dave-fez-2009-2010.md)
7. [`07-post-dave-coming-out-2010-2012.md`](chronology/07-post-dave-coming-out-2010-2012.md)
8. [`08-late-era-2012-2014.md`](chronology/08-late-era-2012-2014.md)
9. [`09-final-year-2014-2015.md`](chronology/09-final-year-2014-2015.md)
10. [`10-afterlife-2015-2026.md`](chronology/10-afterlife-2015-2026.md)

## [`community/`](community/)
The secondary universe and its production role.

Current deep branches include:

- RonFez.net institutional history and governance;
- Paltalk Big ASS Room;
- rival boards and Board Gossip;
- friends-of-show/civilian cast;
- off-air → on-air case traces;
- Friday Night Lights;
- Board Gossip episode ledger;
- RFNet decline, Most Post Wins and v3;
- WJFK fan streaming / Big ASS Antenna;
- early 2001–03 board culture;
- FoundryMusicJeff / RFNet software-governance history.

Start with [`community/README.md`](community/README.md).

## [`events/`](events/)
Individual live-event dossiers and physical artifacts.

The event layer now covers, among other things:

- New York Forever gatherings;
- both 2002 Big ASS Nights of Fights;
- 2002 celebrity-softball lead;
- Tuddle coffin/concrete stunt;
- first RFNet Christmas party (2002);
- WJFK tournaments and social events;
- Hurricane Isabel;
- Friday Night Lights via the community layer;
- BB King's XM kickoff;
- Big ASS Bash;
- Dave & Casey wedding;
- RF Softball;
- bar nights / BBQ / Rock-a-Hula / Winter Carnival;
- Night of a Hundred Podcasts;
- Tiger Woods and Oscars simulcasts;
- Fez's 2010 apartment party;
- Ronnie Spector's 2011 SiriusXM Christmas concert;
- unresolved early RFNet artifacts.

Start with [`events/README.md`](events/README.md).

## [`people/`](people/)
One-file-per-person biography and genealogy system.

The active biographies now include a large civilian layer in addition to staff, including GVac, Mikeyboy, JustJon, FoundryMusicJeff, French Bread Pizza, HTG, Irish Alkey, Sheepy, Perrynoid, Crazy Jen, Big A, Fleaman, Chuckwagon/Lenny McNab, Hottub, spoon, Matty Fridays, Don Stugots, Hard Rock Johnny, J-Dubs, Cigar Sid, Don the Hypnotist, Hosp/Gary Oransky, Death Metal Moe and Moshin.

Start with [`people/README.md`](people/README.md).

## [`themes/`](themes/)
Cross-era subjects that become distorted if left only inside chronology.

- [`01-comedy-formats.md`](themes/01-comedy-formats.md)
- [`02-events-and-live-culture.md`](themes/02-events-and-live-culture.md)
- [`03-music-and-sonic-identity.md`](themes/03-music-and-sonic-identity.md)

## [`forensics/`](forensics/)
Evidence-led reconstruction.

- [`00-methodology.md`](forensics/00-methodology.md)
- [`01-work-shoot-ledger.md`](forensics/01-work-shoot-ledger.md)
- [`02-cast-genealogy.md`](forensics/02-cast-genealogy.md)

## [`reference/`](reference/)
Research infrastructure, source matrices and open gates.

Important current files include:

- [`01-source-index.md`](reference/01-source-index.md)
- [`02-research-queue.md`](reference/02-research-queue.md)
- [`03-corrections-and-open-questions.md`](reference/03-corrections-and-open-questions.md)
- [`04-terminology.md`](reference/04-terminology.md)
- [`06-community-source-index.md`](reference/06-community-source-index.md)
- [`07-whole-show-archive-map.md`](reference/07-whole-show-archive-map.md)
- [`08-living-oral-history-watch.md`](reference/08-living-oral-history-watch.md)
- [`08-physical-community-source-index.md`](reference/08-physical-community-source-index.md)
- [`09-governance-staff-and-simulcast-source-index.md`](reference/09-governance-staff-and-simulcast-source-index.md)
- [`10-rfnet-media-url-reconstruction.md`](reference/10-rfnet-media-url-reconstruction.md)

## [`conversation/`](conversation/)
Project provenance and originating decisions.

---

# Evidence policy

- **A — Direct:** original broadcast, contemporary physical artifact, official documentation
- **B — Strong corroboration:** multiple independent contemporary sources or unusually strong corroboration
- **C — Participant recollection:** later account by somebody who was there; valuable, but memory can drift
- **D — Contemporary fan record:** board post, gallery, listening thread, fan archive from the period
- **E — Later fan consensus:** retrospective community memory; excellent lead, not proof by itself
- **U — Unresolved:** current evidence does not allow a responsible conclusion

The project explicitly preserves uncertainty rather than converting fan lore into fact.

---

# Work / shoot policy

The project does not force incidents into a false binary of “real” and “fake.”

Useful classifications include:

- WORK;
- SHOOT;
- WORK → SHOOT;
- SHOOT → WORK;
- WORK → SHOOT → WORK;
- genuine event with exaggerated radio framing;
- collaborative exaggeration;
- unresolved origin with deliberate escalation.

The current governing model for Ron is:

> **Ron orchestrated the frame more often than the underlying event.**

See [`wiki/Work-Shoot-and-What-We-Know.md`](wiki/Work-Shoot-and-What-We-Know.md).

---

# Important corrections already preserved

The project treats corrections as evidence rather than embarrassment.

Examples:

- **Iris** was initially discussed as possibly a real eccentric caller; the forensic pass corrected that she was a fictional recurring caller voiced by Ron.
- **Moshin** was initially overclassified from a later fan census; the stronger early anchor now comes from the first-RFNet-Christmas-party 2002 photo discussion.
- **Don the Hypnotist** publicly corrected his own remembered entry date after finding old material showing he was already appearing in 2004.

See [`reference/03-corrections-and-open-questions.md`](reference/03-corrections-and-open-questions.md).

---

# Current status — September 2026

The project is well beyond its initial structured import.

Major completed/active layers now include:

- complete era chronology through 2026;
- cross-era comedy, event and music histories;
- mature RFNet/Paltalk/board reconstruction;
- early RFNet governance evidence;
- civilian-cast biography system;
- extensive live-event dossiers;
- whole-show tape map;
- living participant oral-history ledger;
- work/shoot case ledger;
- physical-community source matrix;
- restored-media URL/ID reconstruction;
- reader-facing living-history wiki source;
- compiled oral-history narrative.

## Current highest-value open research gates

The reader-layer work temporarily superseded, but did not replace, the active forensic gate.

Next high-value research includes:

1. recover the direct records behind `Slumber Party Pics`, `A Night at Double D's`, `The Group Photo`, `RonFez.Net on WWF Smackdown!`, `CyberSoldier Holiday Party Pics 2002`, and `Moshin's Tattoo`;
2. reconstruct the three remembered group photographs from the first RFNet Christmas party in 2002;
3. establish CyberSoldier's role and test the `The Group Photo` Christmas-party hypothesis;
4. continue historical RFNet media-ID / `displaymedia.cfm` recovery;
5. index the complete Nov. 6–10, 2006 Board Gossip tapes;
6. index the May 29 / June 1, 2009 Chuckwagon tapes;
7. expand dedicated biographies for Ron, Fez, Dave, Chris, Earl, Billy and other core figures;
8. build the full music/rejoiner database;
9. build the essential-listening map;
10. continue capturing public living-participant history while cross-checking memory against surviving documents.

Nothing here should be treated as finished. The project is intended to become a detailed historical reference **and** a readable living history, with the evidence layer always capable of correcting the story layer.