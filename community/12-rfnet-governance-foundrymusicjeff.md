# RonFez.net governance — FoundryMusicJeff, board software, and the early admin layer

## Summary

One of the archive's longest-running open questions has been:

> **Who actually ran RonFez.net in its earliest years?**

A contemporary October 11, 2002 cross-board post materially improves the answer.

Posting as **FoundryMusicJeff**, Jeff says:

- **“how I run things at Ronfez.Net”**;
- refers to RonFez.net as **“my board”**;
- describes moderation rules as something he personally enforced;
- says software being used on OpieAnthony.com was **“my board software”**;
- says he had wanted that software removed from OA.com and had been threatened with legal action if he tried to take it back.

Source:
- https://www.cdih.net/cdih/showthread.php?pid=363247&tid=3733

Evidence grade: **D/A-adjacent contemporary first-person post by the participant.**

This is substantially stronger evidence of operational/technical authority than later fan recollections that somebody “ran the board.”

---

## Identity: FoundryMusicJeff = Jeff Shain

A 2016 memorial entry for GVac is visibly signed:

> **FoundryMusicJeff Shain**

The writer says he and GVac were part of the **early days of RonFez.Net**, which he describes as the first message board for the radio show.

Source:
- https://www.doctorsteve.com/gvac-memorial/

This provides strong participant-level identity linkage:

> **FoundryMusicJeff = Jeff Shain**

Evidence grade: **C/B**.

Do not extend this identity into unrelated modern people named Jeff Shain without participant/source continuity.

---

# What the October 2002 post establishes

## 1. Jeff exercised governance authority

The phrase:

> “how I run things at Ronfez.Net”

is direct evidence that Jeff understood himself as someone **running** the site, not merely a famous poster or moderator.

He contrasts RFNet's moderation philosophy with the much rougher OpieAnthony.com culture and argues that rules were necessary to stop communities from becoming cruel or unusable.

That gives us a period description of RFNet's moderation philosophy from a person exercising authority.

---

## 2. Jeff calls RonFez.net “my board”

This wording strengthens the operational-authority interpretation.

It does **not yet prove**:

- sole legal ownership of the domain;
- sole founding credit;
- that no other founder/technical partner existed;
- that he controlled every decision throughout RFNet's entire life.

The safe conclusion is narrower:

> **By October 2002, FoundryMusicJeff/Jeff Shain was a principal operator of RonFez.net with enough authority to describe it as his board.**

---

## 3. Jeff claims authorship/ownership of board software used at OA.com

The same post says:

> he did not want Froy to use **“my board software”** on OA.com.

That is a major technical-history clue.

It suggests Jeff was not merely enforcing forum rules; he had a **software-development or software-ownership role** in the underlying message-board infrastructure used in the adjacent O&A web ecosystem.

This may explain why early RFNet and neighboring boards shared structural/technical similarities.

### Research questions

- Did Jeff write the forum software from scratch?
- Was it a customized package built on another platform?
- Did the same code power RFNet itself?
- What was the software called?
- Was OA.com licensed, informally sharing it, or using a fork?
- Who hosted RFNet's servers/database?

---

## 4. FoundryMusic independently used the same `displaymedia.cfm` media-route family

A September 2026 external-link recovery pass found multiple contemporary or near-contemporary pages preserving dead **FoundryMusic** media URLs.

Examples include:

- a March 23, 2007 wrestling-news item linking Mick Foley's Opie & Anthony appearance as:
  - `foundrymusic.com/media/displaymedia.cfm/id/14411/page/show_video_number_14411.html`
- other surviving third-party references use section-prefixed FoundryMusic routes such as:
  - `/opieanthony/displaymedia.cfm/...`
  - `/braincandy/displaymedia.cfm/...`

Representative source:
- https://www.wrestlezone.com/news/220697-wwe-notes-on-orton-wm23-lesnarmma-more

This matters because historical RFNet media links independently survive in the closely related form:

- `ronfez.net/displaymedia.cfm/id/<number>`

See:
- `../reference/10-rfnet-media-url-reconstruction.md`

### What can safely be inferred

Taken together with Jeff's explicit 2002 statement about **“my board software”**, the matching ColdFusion-style media-route convention materially strengthens a working hypothesis that RFNet and FoundryMusic belonged to a **shared Jeff-era software/code ecosystem** rather than being technically unrelated fan sites.

The evidence is consistent with possibilities such as:

1. shared custom application code;
2. a common Jeff-developed software family deployed separately;
3. one site's code being forked or adapted for another;
4. shared conventions layered on a broader ColdFusion application stack.

### What this does **not** prove

The matching route does **not** establish that:

- RFNet and FoundryMusic used the same database;
- media IDs were globally unique across both domains;
- an RFNet item with ID `3004` was the same record as a FoundryMusic item with ID `3004`;
- FoundryMusic mirrored every RFNet media item;
- Jeff personally wrote every part of the media subsystem.

A direct September 2026 search for FoundryMusic records matching known historical RFNet IDs **2989, 3004, and 3018** produced no indexed title/record matches. That is not proof the IDs never existed on FoundryMusic, but it provides no support for a shared global ID namespace.

**Current technical classification:**

> **shared/related software lineage: plausible and increasingly well-supported; shared media database or ID namespace: unproven.**

### Highest-value technical proof still missing

Recover one of the following:

- identical media title/content on both domains with independently preserved URLs;
- source/footer/software credit naming the media application;
- archived RFNet/Foundry HTML showing identical generated markup or database keys beyond generic ColdFusion syntax;
- Jeff or another operator explicitly describing the relationship between the two codebases;
- an old redirect or cross-domain link that maps one media record directly to the other.

Until then, keep **software lineage** and **database identity** as separate questions.

---

# The OA.com dispute as evidence of board ecology

The October 2002 post appears during the collapse/crisis of an O&A board.

Jeff criticizes the other site's governance and says that RFNet deliberately prevented the level of personal abuse he had seen there.

This matters because it proves several aspects of the web ecosystem **four years before Board Gossip**:

- board operators knew one another;
- software crossed between communities;
- users crossed between communities;
- admins argued publicly about moderation philosophy;
- sites developed reputations for being permissive, hostile or “candy coated”;
- technical and personal relationships among admins could affect entire fan populations.

Board Gossip later converted this existing ecology into radio entertainment; it did not create it.

---

# Corroborating October 2002 culture

A separate October 21, 2002 outside-board discussion contains an RFNet user introducing herself as coming from the:

> **“shiney happy ronfez.net board”**

Other posters call RFNet “candy coated.” The RFNet user discusses warning emails and says moderators moved an offending thread into the **staff room**.

Source:
- https://www.cdih.net/cdih/showthread.php?pid=153124&tid=3870

This independently supports Jeff's claim that RFNet had a consciously more controlled moderation culture.

It also shows that the culture was visible enough for **outsiders to stereotype the entire board**.

---

# Jeff's later continuity

Jeff did not disappear from the R&F-adjacent media world.

Doctor Steve's *Weird Medicine* archive documents **Foundry Music Jeff** appearing as a recurring contributor/correspondent in the XM/Sirius era, including:

- helping with the October 25, 2008 program;
- later appearing to discuss health-care reform.

Sources:
- https://www.doctorsteve.com/2008/10/26/
- https://www.doctorsteve.com/tags/ron-and-fez/

This produces another long continuity line:

`early RFNet operator → R&F civilian identity → XM202/Weird Medicine contributor → later community memorial witness`

---

# Governance map — revised

The evidence now supports a more differentiated early governance model:

| Person | Evidence-backed role | Confidence |
|---|---|---:|
| **FoundryMusicJeff / Jeff Shain** | principal early operator; says he ran RFNet/calls it his board; software authority | High for 2002 operational role |
| **JustJon** | founding-era member, uploader, later front-page/event organizer | High for functions; formal title unresolved |
| **Mikeyboy** | later former admin; major photo/archive custodian | High |
| **thepaulo** | visible Forum Moderator | High |
| **sailor** | later front-page/community-news poster | Medium-high |
| **MojoPin** | persistent early internal reference | unresolved |
| **Matty** | early prominent community figure | no admin role established |

This table should continue to separate:

- **founding/ownership**;
- **technical operation**;
- **administration/moderation**;
- **content/news/event leadership**;
- **archive/media custody**.

Those roles may have overlapped but should not be treated as synonymous.

---

# Does this prove Jeff founded RonFez.net?

**Not yet.**

The evidence is strong enough to say that Jeff was a principal early operator and likely technical architect/owner of relevant board software by 2002.

It is not yet sufficient to state:

> “Jeff Shain was the sole founder of RonFez.net on February 5, 2001.”

To establish that, recover one or more of:

- first-day/launch announcement;
- domain registration history;
- archived About/Staff page;
- direct Jeff/JustJon/MojoPin account of founding;
- original source-code/footer credits;
- server/hosting history.

This distinction matters because community sites are often created by several people whose roles later collapse in memory into “the guy who ran it.”

---

# Research targets

1. Earliest Wayback capture of RFNet.
2. Original About/Staff page.
3. WHOIS/domain history where publicly archived historically.
4. Exact board-software name/code lineage.
5. FoundryMusic.com/RFNet relationship.
6. Jeff's exact title/ownership share.
7. Relationship between Jeff, JustJon, MojoPin and later Mikeyboy administration.
8. OA.com software dispute details.
9. Whether RFNet's rules/moderation policy was written by Jeff.
10. Exact date Jeff ceased daily governance.
11. Board migration/version changes and whether software ownership changed.
12. Whether FoundryMusic and RFNet used one media application codebase or sibling deployments.
13. Whether any media record can be cross-mapped between domains by title, ID, generated markup or redirect.

## Core conclusion

The early RFNet administration is no longer a blank.

A contemporary 2002 record places **FoundryMusicJeff / Jeff Shain directly in the site's governing and technical layer**. He describes himself as running RFNet, calls it his board, and claims ownership of board software used elsewhere in the radio-fan web ecosystem.

The later discovery that FoundryMusic also used the same `displaymedia.cfm` media-route family strengthens the case for a shared software lineage, but it does **not** establish a shared database or common numeric-ID namespace.

The remaining question is no longer **“Did Jeff run RFNet?”**

The better questions are:

> **Exactly what combination of founder, owner, software architect and administrator was Jeff—and how much code and infrastructure did RFNet share with FoundryMusic and the neighboring O&A web ecosystem?**