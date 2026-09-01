# CV completion checklist

Working list for turning `pino_cv.tex` into the complete record. Delete items as
they land. See README for the `\hide{}` / `\showall` convention.

## 1. ~~Talks that need real titles~~ — DONE

All resolved. Titles came from the slide-deck archive; the Hollomon "keynote"
turned out to be five minutes of closing remarks with no slides, so it moved to
Panels, Moderation, and Judging as "Judge and closing remarks" rather than being
listed as a lecture. No `% TITLE?` placeholders remain.

<details><summary>Original list</summary>

### Talks in the CV that need real titles

Seven of the eight placeholders are resolved, recovered from the slide-deck
archive in Google Drive (`presentations/`, root plus the year subfolders). The
talk log built from that sweep lives in `talks.xlsx`.

```bash
grep -n 'TITLE?' pino_cv.tex
```

Any that cannot be recovered get wrapped in `\hide{}` rather than printed with a
placeholder, since "Invited talk." reads worse than no entry at all.

- [x] Jul 2026 — Seattle University Summer Accelerator → *Accidental
      Entrepreneur: Founding a Biotech Startup Company*
- [x] May 2026 — Stanford Proteomics Users Group (PUG) → *Scaling Proteomics to
      Unlock Transcription Factors for Drug Discovery*
- [x] Apr 2026 — Life Science Innovation NorthWest, AI session → *Unlocking the
      regulo.me for drug discovery using a high-throughput proteomics platform*
- [x] Apr 2026 — Bioscience Careers Seminar Series, UW PhD Ambassadors → *From
      PhD to Platform: Founding a Biotech Startup Company*
- [x] Apr 2026 — Discovery Continuum Seminar, SCIEX → *SCIEX ZenoTOF 8600 system
      in chemoproteomics drug discovery applications*
- [x] Mar 2026 — ACS Division of Medicinal Chemistry → *Unlocking the regulo.me
      for drug discovery using a high-throughput proteomics platform*
- [ ] **Mar 2026 — 2026 Hollomon Health Innovation Challenge keynote.** Still
      open. No deck for this anywhere in the archive, so it has to come from
      memory, the event page, or your calendar.
- [x] Feb 2026 — Sciex Lunch Seminar, US HUPO 2026 → *Chromatogram-based
      chemoproteomics with ZenoTOF 8600 and Skyline*

~~Caveat on the LSINW and ACS pair: they now carry the *same* title~~ — resolved.
The LSINW deck was a copy of the ACS deck whose title slide was never updated, so
the extracted title was wrong. The real one is *Unlocking the regulo.me for drug
discovery with Strategian, a functional proteomics recommender system*. The two
entries are now distinct.

Two of the new 2026 talks already have titles and need nothing: the ASMS selected
oral (DNA damage / DNA repair-directed therapeutics) and the ASMS Sciex breakfast
seminar (ZenoTOF 8600 + Skyline).

The Aug 2026 Protein Society (Thailand) talk has also been added, title as
supplied — that deck and the Stanford one are both 82 MB and return no
extractable text through Drive, so neither title was read off a slide.

</details>

## 2. Missing venues

- [x] Stanford PUG (May 2026) — confirmed in person, on the Stanford University
      campus. Entry now reads "Stanford University, Stanford, CA".
- [x] SCIEX Discovery Continuum (Apr 2026) — Seattle, WA, inferred from the deck
      filename `20260402_sciex_pharma-seattle.pptx`. Worth confirming it was not
      a webinar.

ASMS 2026 (San Diego, CA) and US HUPO 2026 (St. Louis, MO) are filled in.

Two older entries are in the CV `\hide{}`-wrapped with a `% VENUE?` tag because
the venue could not be recovered: the Feb 2022 spatiotemporal-DIA talk (filename
says US HUPO, title slide names nothing and dates it Mar 01) and the Jun 2021
"TF conf" talk (no venue, date, or organizer anywhere in the deck).

One date conflict surfaced and is tagged `% DATE?` in `pino_cv.tex`: the BCPM
Simon Fraser talk is listed as Jan 2024 here and in `RECALL.md`, but the deck
`20240221_sfu-vancouver_keynote.pptx` prints "February 21, 2024".

## 3. The 2025 gap

Mostly closed. The deck archive supplied five 2025 talks; four are now printed
and two are `\hide{}`-wrapped as non-lectures.

- [x] Feb 2025 — **US HUPO 2025**, Philadelphia. You spoke: *Drug Discovery
      Screening for Transcription Factors from Low-Input, High-Throughput,
      Cell-Based Proteomics*, Session 9 "Down in the Dumps: Treasure from
      Troubleshooting". Separately you ran an **Evening Workshop**, *The Business
      of Starting a Lab Business* — added but `\hide{}`-wrapped, since it may sit
      better under Teaching.
- [ ] May/Jun 2025 — **ASMS 2025**. Still open. The only ASMS 2025 deck in the
      archive is an unfinished calibration-curves *poster* (`20250603_asms_calcurves`,
      full of CARTOON/TODO placeholders), not a talk. If you gave an oral, its
      deck is not in the folder.
- [ ] Jun 2025 — **Entrepreneurship in Mass Spectrometry workshop, ASMS 2025**.
      Still open; no deck found. Belongs in Teaching or Professional Service.
- [x] Jul 2025 — **Cascadia Proteomics Symposium**, Seattle. Answered: **Andrea
      Gutierrez** presented (*High-Throughput Quantification of Chromatin-Associated
      Proteins to Advance Neuroblastoma Therapeutic Discovery*), not you. Nothing
      to add to your lectures.
- [x] Jul 22 2025 — **"Bringing ASMS 2025 to Seattle"**, Bruker event. Added:
      *Proteomics for Chromatin-Bound Protein Drug Discovery That Doesn't Fall
      Apart at Scale*. The title slide carries only the date, so the event name
      comes from the filename.
- [ ] Sep 5 2025 — **An unnamed panel**, early Pacific hours so likely
      European-hosted or virtual. Still open; no deck.
- [ ] Oct 2025 — **Forbeck Forum**, Lake Geneva, WI. Deck found
      (`20251006_forbeck`) but it is three content slides with no title slide, and
      the venue is only confirmed via the Q4 platform deck's trip report. Needs a
      title before it can be listed.
- [ ] Nov 2025 — **ASMS Fall Workshop, "Fundamentals of Instrumentation"**. Your
      post reads like attendee rather than instructor — confirm which.

Also added from the archive, not previously on this list: the **Nov 2025 Bruker
Lunch Seminar at HUPO Toronto** (*From regulome maps to first-in-class targets
through functional proteomics at scale*), and the **Mar 2025 Bruker User Meeting,
Los Angeles**, which is `\hide{}`-wrapped as the third stop on the same ABPP
roadshow as Sep 2024 San Francisco and Nov 2024 San Diego.

## 4. Other sections to sweep

- [ ] **Awards** — GeekWire Health Innovation of the Year *finalist* (Mar 2025).
      That is a Talus award rather than a personal one; decide whether it goes
      under Awards, Entrepreneurship, or not at all.
- [ ] **Posters** — all six are currently `\hide{}`-wrapped. Also decide about the
      ASMS 2025 posters MP224/225 (Canzani and Robbins presenting) — were you a
      co-author?
- [x] **Research Support** — done. Every application with Pino as PI or Co-I is
      now listed, with the unfunded ones `\hide{}`-wrapped: six awarded, eleven
      hidden. The NIH rows were pulled from the eRA Commons Status module rather
      than from the Drive summary, which had two of them wrong (`R43AG084786` was
      administratively withdrawn, not "scored 46"), and missed the NHGRI
      resubmission chain and four pre-Talus fellowship applications entirely.
      The Sep 2025 MNP grant is *not* here on purpose — the NIEHS microplastics
      application lists Pino in personnel at zero effort with Federation as PI, so
      by the same rule that keeps Deep Learning and SEPL out, it does not belong.
      Two loose ends: `1R43HG014987-01` is the only row with no dollar figure
      (eCommons Status does not expose requested budgets, and the Drive summary
      never had one), and the Co-I grants cannot be checked against eCommons at
      all, since the Status module only shows applications where you are PD/PI.
- [ ] **Teaching** — was there a Skyline Online 2026? The entry currently reads
      `2020--25`.
- [ ] **Publications** — run `python audit_pubs.py` against the ORCID record once
      the rest settles.

## 5. Record types the CV does not capture at all

Everything above is a gap *inside* a section. These are categories with no home
in `pino_cv.tex` — `grep` finds nothing for most of them. Ordered by what is
worth closing first. All of these can land `\hide{}`-wrapped; the point is that
the record exists somewhere, not that it prints.

- [x] **Patents and IP** — done. A `Patents` section now sits between Additional
      Publications and Invited Research Lectures, `\hide{}`-wrapped whole so the
      curated build does not print an empty heading. Three families, all assigned
      to Talus Bioscience, all with Pino as an inventor: the May 2022
      reactive-cysteine method (WO 2023/225568, US 2025/0306032, plus EP, AU and
      CA national phase), and two filed the same day in Feb 2023 —
      lectin-assisted nuclei isolation (WO 2024/163960, EP 4658665) and
      volatile-salt extraction of chromatin-bound proteins (WO 2024/163959,
      US 2026/0226097). Each row carries title, inventors, assignee, application
      and publication numbers, priority date, and status.
      The set came from the Google Patents inventor index, cross-checked entry by
      entry against Espacenet — *not* from counsel or the IP docket. Three
      caveats follow. Nothing is granted, so every row reads `Pending`. The
      lectin family shows no US publication, which may mean the US case has not
      laid open rather than that it does not exist. And an unpublished filing — a
      live provisional, or a national phase still inside the 18-month window — is
      invisible to both indexes. Worth one pass against the docket to confirm the
      set is complete.
- [ ] **Grant and study-section review.** Eight NIH applications as PI and
      nothing recording service on the review side — SBIR study sections, Andy
      Hill CARE Fund panels, NSF panels, foundation review. Distinct from journal
      refereeing, and the version of peer review that reads as senior.
- [ ] **Dates and counts on the journal refereeing.** The `Journal Referee` line
      under Professional Service is nine journal names with no years and no
      volumes. `RECALL.md` already flags the list as unversioned. The ORCID peer
      review record can date most of these without relying on memory.
- [ ] **Software, datasets, and accessions.** Nothing points at a repository, a
      PRIDE or MassIVE accession, or a released tool, even though several of the
      papers *are* software papers — nf-encyclopedia, coADAPTr, the Skyline
      ecosystem work. For a computational proteomics CV that output is the work
      product, and right now it is visible only as a citation.
- [ ] **Affiliations that are not employment.** Adjunct, visiting, and honorary
      positions; SAB seats; unpaid advisory roles. Worth capturing specifically
      because NIH retired the Biosketch and Other Support format pages on
      **May 8, 2026** (NOT-OD-26-079, read off the eRA Commons banner in Aug
      2026) in favor of the Common Forms, now in force. Those want *all*
      appointments, foreign and unpaid included, plus in-kind support — a wider
      net than Employment and Professional Appointments currently casts.
- [ ] **Print press.** `Audio/Video Features` is AV only, so GeekWire, Endpoints,
      Timmerman, and Life Science WA coverage has nowhere to go.
- [ ] **Trainee outcomes.** `Mentoring` lists five names but not where any of
      them landed, which is the part that carries weight in a nomination packet.
- [ ] **Company financing milestones.** `Entrepreneurship > Accelerator Programs`
      carries YC but no rounds. Seed and Series A are CTO credentials.

Deliberately not on this list: talks declined, and any expansion of
`Conference Attendance` — it is already `\hide{}`-wrapped and low signal.

## 6. Filling the pre-2026 record

See `RECALL.md`. It walks year by year, listing what the CV already pins down so
memory has something to hang on, and asks a fixed set of questions of each year.

Worth checking alongside memory, since they are cheap:

- [ ] Your calendar — the most reliable source for talk titles and dates
- [ ] LinkedIn — login-gated, so it needs a manual export or copy-paste
- [ ] Old slide decks — filenames and title slides date themselves
- [ ] Conference programs, if any are still online

## 7. Last step

Once the record is complete, flip `\showalltrue` to `\showallfalse` in
`cvstyle.sty`, do a pass over what should be `\hide{}`-wrapped, rebuild, and
commit `pino_cv.pdf`.

## Research ops sweep, 2026-08-31

Recorded by the weekly sweep. One blocked check, and a partial result that stands
in for it until the blocker clears.

- [ ] **The ORCID publications audit cannot run on the Windows machine — its input
      repo is not cloned here.** `audit_pubs.py` is present in this repo, but
      `/d/MyPublications` does not exist, and neither `papers.json` nor
      `fetch_papers.py` is anywhere on `D:`. So the item under section 4,
      "run `python audit_pubs.py` against the ORCID record", is blocked on this
      machine rather than merely pending. Next command:

      ```
      gh repo clone lindsaypino/MyPublications D:/MyPublications
      cd /d/MyPublications && python -X utf8 fetch_papers.py
      cd /d/cv && python audit_pubs.py ../MyPublications/papers.json
      ```

      Confirm the repo name before cloning; the sweep verified only that no local
      copy exists, not what the remote is called.

- [x] **PubMed cross-check run instead, and it found no drift.** 23 records match
      `Pino LK[Author]`. Every one indexed since 2024 is already in `pino_cv.tex`.
      The only DOI absent is `10.1101/2024.11.07.622473`, the bioRxiv preprint of
      the *Cell* paper `10.1016/j.cell.2025.05.023` already listed at line 134 —
      correctly dropped by the rule that removes preprints a published version
      supersedes.

      This is **not** a substitute for the ORCID audit. PubMed indexes only
      biomedical literature, so anything outside that scope is invisible to it,
      and the ORCID record catches works PubMed never sees. Treat the CV's
      publication list as verified against PubMed only, until the audit above runs.
