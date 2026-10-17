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
- [x] **Mar 2026 — 2026 Hollomon Health Innovation Challenge keynote.** Done
      (`43d870d`): closing remarks, not a lecture; now under Panels as "Judge and
      closing remarks".
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
- [x] May/Jun 2025 — **ASMS 2025**. Answered: a **poster**, not an oral, which
      matches the only ASMS 2025 deck in the archive (`20250603_asms_calcurves`,
      an unfinished calibration-curves poster). Nothing to add to the lectures.
      Posters stay `\hide{}`-wrapped, so nothing prints either.
- [x] Jun 2025 — **Entrepreneurship in Mass Spectrometry workshop, ASMS 2025**.
      Answered, and then widened considerably by a Drive sweep of
      `workshop_entrepreneurship/`. This is not one workshop but a **four-run
      series** co-chaired with **Paula Burton** (co-founder/CEO, Mass Dynamics),
      and only one run was anywhere in the CV. All four are now in Teaching under
      Entrepreneurship and Science Communication Workshops:

      | Run | Where | Title |
      | --- | --- | --- |
      | Jun 2025 | ASMS, Baltimore | Non-traditional Ways to Progress Your Science |
      | Nov 2025 | HUPO, Toronto | *not recovered* |
      | Jun 1 2026 | ASMS, San Diego | Navigating the Commercial Realities of MS/Proteomics Startups |
      | Oct 2026 | HUPO, Singapore | Entrepreneurship in Proteomics: Scaling Science into Sustainable Companies |

      Each run is its own row rather than a year range, since the titles and the
      host societies differ. Three things to check:

      1. ~~Role wording.~~ Settled 2026-10-16: the workshops and the ASMS DIA
         Interest Group are **Co-coordinator**; *Co-chair* is reserved for the
         ISMB CompMS COSI. The four rows were changed to match, so the ASMS 2026
         invitation letter's "Co-chaired by Lindsay Pino ... and Paula Burton"
         is not the wording the CV follows here.
      2. **The Toronto title.** No proposal doc for that run is in the folder.
         The row carries the series name as a stand-in. The sign-up form
         (`Entrepreneurship in MS and Proteomics (Responses)`) is what proves the
         run happened at all, by offering "HUPO (Toronto, 2025)" as an option.
      3. **The Singapore month.** Taken from the blog post's creation date
         (2026-10-07) plus "day zero of HUPO in Singapore", not from a program.

      Counting note, in case a fifth run turns up: the ASMS 2026 logistics email
      calls that run "our third time", and the Singapore post calls itself "the
      fourth time". Both are consistent with exactly these four.
- [x] Jul 2025 — **Cascadia Proteomics Symposium**, Seattle. Answered: **Andrea
      Gutierrez** presented (*High-Throughput Quantification of Chromatin-Associated
      Proteins to Advance Neuroblastoma Therapeutic Discovery*), not you. Nothing
      to add to your lectures.
- [x] Jul 22 2025 — **"Bringing ASMS 2025 to Seattle"**, Bruker event. Added:
      *Proteomics for Chromatin-Bound Protein Drug Discovery That Doesn't Fall
      Apart at Scale*. The title slide carries only the date, so the event name
      comes from the filename.
- [ ] Sep 2025 — **An unnamed panel**, early Pacific hours so likely
      European-hosted or virtual. Still open; no deck. Checked 2026-10-16: the
      calendar has nothing on Sep 5. The provenance does not survive in the repo
      either — both files were gitignored until `e854073`, so there is no history
      behind them, and `RECALL.md` only ever said "Sep — a panel, early Pacific
      hours" with no day. The "Sep 5" here is sharper than its own source. Day
      dropped from the heading above to stop it hardening further. Treat the
      whole entry as unverified; if nothing turns up, delete it rather than
      printing it.
- [x] Oct 2025 — **Forbeck Forum**, Lake Geneva, WI. Answered from the forum
      *program*, not the deck: *Measuring the Regulome to Translate Chromatin
      Biology into Cancer Therapeutics*. The program prints the abstract and the
      Talus Bio CTO/co-founder affiliation, so it confirms this was a titled
      lecture rather than a discussion slot, and it corroborates the venue that
      the Q4 platform deck's trip report had been the only source for. Now listed
      under Invited Research Lectures, unhidden.
- [x] Nov 2025 — **ASMS Fall Workshop, "Fundamentals of Instrumentation"**.
      Answered: **instructor**. Added to Teaching under the workshop instructor
      table. No city on the row yet.

Also added from the archive, not previously on this list: the **Nov 2025 Bruker
Lunch Seminar at HUPO Toronto** (*From regulome maps to first-in-class targets
through functional proteomics at scale*), and the **Mar 2025 Bruker User Meeting,
Los Angeles**, which is `\hide{}`-wrapped as the third stop on the same ABPP
roadshow as Sep 2024 San Francisco and Nov 2024 San Diego.

## 4. Other sections to sweep

- [x] **Awards** — GeekWire Health Innovation of the Year *finalist* (Mar 2025).
      Decided 2026-10-17: it goes under **Awards and Honors**, not
      Entrepreneurship. Because it is a company award rather than a personal
      one, the row says so outright — `Finalist; awarded to Talus Bio` — so it
      cannot be misread as an individual honor sitting beside the HUPO Rising
      Star and LSWI awards.
- [x] **Posters** — decided: they **stay `\hide{}`-wrapped**. The ASMS 2025
      MP224/225 co-authorship question (Canzani and Robbins presenting) is
      therefore moot for the printed CV; it would only matter if posters are ever
      unhidden.
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
- [x] **Teaching** — answered: **yes**, Skyline Online runs again the week of
      2026-10-19. The entry now reads `2020--26`.
- [x] **Publications** — run `python audit_pubs.py` against the ORCID record once
      the rest settles. Done 2026-10-05 (`233eb52`): audit exits 0 against the
      OpenAlex refresh of the same day.

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
      Partly answered 2026-10-16: it happened **once, around winter 2025--26**.
      The panel, the sponsor and the exact date still need a Gmail search for the
      invitation or the reviewer agreement before a row can be written.
- [x] **Dates and counts on the journal refereeing.** Done 2026-10-17 from the
      public ORCID peer-review record (`0000-0003-1857-7222`): **29 reviews,
      2019--2026**. Kept as prose with spans appended rather than broken into a
      table, so the line still costs two lines instead of ten.

      | Journal | n | Span |
      | --- | --- | --- |
      | Nature Communications | 13 | 2020--26 |
      | Journal of Proteome Research | 8 | 2020--26 |
      | Analytical Chemistry | 5 | 2019--24 |
      | Clinical Proteomics | 1 | 2021 |
      | J. Am. Soc. Mass Spectrometry | 1 | 2020 |
      | Scientific Data | 1 | 2022 |

      **Scientific Data** was in the ORCID record but missing from the CV list
      entirely, and is now added. Four journals keep no span —
      **Molecular \& Cellular Proteomics, Scientific Reports, Proteomics,
      Frontiers in Molecular Neuroscience** — because ORCID only holds reviews a
      publisher deposited, and the only depositors here are ACS and Springer
      Nature. A LaTeX comment above the line says so, so the gaps are not
      mistaken for an oversight and "fixed" with invented years. Dating those
      four needs memory or the journals' own reviewer records; counts are
      deliberately not printed.
- [x] **Software, datasets, and accessions.** Closed 2026-10-17: **decided
      against a section.** Every repository and dataset below is already cited
      through the paper it belongs to, or will be once that paper lands, so a
      separate section would restate the publication list rather than add to
      it. The item's own premise — that this output is "visible only as a
      citation" — is the answer, not the problem.

      The sweep is kept below as reference. It is the only place this material
      is collected, and it answers the question quickly if a funder or a
      nomination packet ever asks for software and data products directly.

      **Repositories, verified on GitHub:**

      | Repo | Stars | Tied to |
      | --- | --- | --- |
      | `TalusBio/nf-encyclopedia` | 8 | the 2023 JPR paper |
      | `TalusBio/timsbuktoolkit` | 6 | authorship unverified |
      | `LJonesGroup/coADAPTr` | 1 | the 2024 JASMS paper; Jones lab owns it |
      | `TalusBio/msspeculator` | 1 | authorship unverified |
      | `lindsaypino/matrix-matched_calcurves` | 3 | the 2020 calibration-curves paper |
      | `lindsaypino/2024_abrf_sprg` | 2 | ABRF sPRG hybrid proteome standard |

      Also under `lindsaypino`, unstarred and probably not CV material:
      `randoMS`, `histone_ptms`, `parkinsons_proteomics` (Alonge's intern
      project), `silac-dia`, `als_ptms`, `MSstats-patch`.

      **Accessions recovered from open-access full texts:**

      | Paper | Accession |
      | --- | --- |
      | Chromatogram libraries (2018) | MassIVE `MSV000082805` |
      | Late-life mitochondrial restoration (2020) | MassIVE `MSV000084961`, `MSV000085329` |
      | *Dictyostelium* epigenetics (2021) | PRIDE `PXD024225`, GEO `GSE137604` |

      **This list is a floor, not the full set.** Four independent reasons:

      1. ORCID holds **no software or dataset works at all** — 34 articles and
         one preprint, nothing else. So the upstream record is as thin as the CV,
         and nothing here can be recovered from ORCID later.
      2. Europe PMC has **zero cross-references indexed** for any of the 31
         papers it has, so the usual paper-to-repository link is empty.
      3. PRIDE's keyword search for "Pino" returns a *different* researcher
         (Juan Borrero del Pino). None of these datasets were submitted under
         LKP's name, so submitter search cannot find them.
      4. Only **7 of 31** papers are open access with a PMCID, so 24 could not
         be scanned at all. Those need checking by hand.

      **Worth knowing separately:** the 2025 regulome preprint has *no*
      accession. Its data availability statement reads "Raw mass spectrometry
      data will be made public in PRIDE upon acceptance", with processed
      matrices and analysis code "available upon request". So the flagship
      dataset is not deposited yet, and cannot be cited until it is.
- [x] **Affiliations that are not employment.** Answered 2026-10-16: **none** —
      no adjunct, visiting or honorary positions, no SAB seats, no unpaid
      advisory roles. Nothing to add, so the section stays as it is. Re-check if
      a Common Forms submission ever needs it, since the net is wide: Worth capturing specifically
      because NIH retired the Biosketch and Other Support format pages on
      **May 8, 2026** (NOT-OD-26-079, read off the eRA Commons banner in Aug
      2026) in favor of the Common Forms, now in force. Those want *all*
      appointments, foreign and unpaid included, plus in-kind support — a wider
      net than Employment and Professional Appointments currently casts.
- [x] **Print press.** The structural half of this was already solved before
      the item was written: a `Media Coverage` section exists (`777333b`), so
      print has had somewhere to go since then. Filled out 2026-10-17 with five
      more, oldest first:

      | Year | Outlet | Piece |
      | --- | --- | --- |
      | 2022 | GeekWire | Inspired by scientist CEOs ... lands $9.75M |
      | 2023 | GeekWire | Talus Bioscience lands $4.3M in grant funding |
      | 2023 | PharmaVoice | A biotech tackles drug discovery with transcription factor know-how (*Biotech Spotlight*) |
      | 2024 | GeekWire | Seattle biotech startup secures $11.2M ... "undruggable" targets |
      | 2024 | FierceBiotech | Talus Bio tacks on $11M ... |

      **Four of those five are now `\hide{}`-wrapped** (decided 2026-10-17):
      every one whose headline states a funding figure. Hiding the
      `Company Financing` block alone did not keep the numbers off the page —
      the press headlines were still printing $11.2M, $11M, $4.3M and $9.75M on
      the last page. Only the PharmaVoice *Biotech Spotlight* prints, since it
      is a feature rather than a raise. Verified against the built PDF: no
      funding figure appears anywhere in it.

      Each new URL is one long hyphenated run, so each carries the same local
      `\UrlBreaks` override the Drug Discovery & Development entry already used.
      Checked once the build was unblocked: all three documents compile with
      zero overfull boxes, so every line stays inside the margin. The Fierce
      URL does split after `https:`, which is cosmetic only; `\UrlBigBreaks`
      does not suppress it.

      Two of the four outlets named in the original item produced nothing:

      - **Endpoints News** — no Talus coverage found at all.
      - **Timmerman Report** — one piece only, "Seattle's AI-Biotech Leaders See
        Hype, Hope, and Hard Problems" (Nov 2025), where Talus is one of several
        companies giving a fast pitch. Too thin to list as coverage; say if you
        want it anyway.
      - **Life Science WA** — carries the Fierce story rather than its own
        reporting, so the Fierce original is listed instead.

      Left out deliberately: GeekWire's 2025 awards listicle ("Health Innovation
      of the Year field is dominated by finalists battling cancer"). It is
      neither funding coverage nor a feature, and the award itself is already an
      Awards row. Add it if you want the finalist claim to carry a citation.
- [ ] **Trainee outcomes.** `Mentoring` lists five names. Partly answered
      2026-10-17, and the pass turned up a bigger problem than the missing
      outcomes: **two rows overstated the role.** Witek and Gilbert carried no
      qualifier, so they read as primary supervision when the role was
      collaborator rather than mentor of record. Decided: **both rows are now
      `\hide{}`-wrapped**, so neither prints. They stay in the file because the
      collaborations did happen, each tagged `collaborator, not a mentor of
      record`. Alonge, a real mentorship, keeps her row and now reads
      `(undergraduate internship mentor)`. Worth re-reading the rest of the CV
      with the same eye.

      That leaves **three printed rows**: Kohler (thesis committee), Shetty
      (WE Lead), Alonge (undergraduate internship). Outcomes: Kohler, Witek and
      Gilbert all defended, marked on their rows. Still open for the printed
      three — *where each of them landed*, which is the part that carries weight
      in a nomination packet:

      | Trainee | Prints? | Defended? | Current position |
      | --- | --- | --- | --- |
      | Devon Kohler | yes | yes | unknown |
      | Nina Shetty | yes | n/a (undergrad) | unknown |
      | Adetola Alonge | yes | n/a (undergrad) | unknown |
      | Gabriela Witek | no, hidden | yes | unknown |
      | Michael Gilbert | no, hidden | yes | unknown |

      Gilbert is first author on the 2025 *Cell* ant paper, which would date a
      position, but a paper affiliation is not a current position and was not
      used. No defense *years* are printed either — the span end implies them,
      and inventing exact dates was not worth it.
- [x] **Company financing milestones.** Done 2026-10-17. The item's own premise
      was half wrong — **there is no Series A** (confirmed by LKP) — and the
      first attempt at this entry was wrong in a worse way, so both were
      rewritten 2026-10-17 after LKP supplied the real round history.

      **The mistake, recorded so it is not repeated.** The first draft treated
      **$9.75M as a tracker's bad reporting of the 2024 round**. It is not. It
      is the figure *Talus Bio's own June 2022 release* carried for the 2022
      seed, and GeekWire ran it the same week. Two separate events, two years
      apart, were collapsed into one, and a real announcement was dismissed as
      an outlier. The spread of "totals" in the trackers — $16M, $19.7M, $21.7M,
      ~$27M — was likewise written off as unusable when those are just different
      cuts of the same history taken at different dates.

      **What a press figure actually is.** A line of the form "has raised $X in
      seed funding" is a *running total*, and it can fold in the pre-seed and
      awarded grants. So the announced number for a round and the size of that
      round are different quantities, and must not be used interchangeably. The
      rows now say "as announced" for exactly this reason, and no cumulative
      total is printed.

      Two rows, both public announcements: the **Jun 2022 seed** ($9.75M as
      announced; NFX and Y Combinator named) and the **Aug 2024 Seed+** ($11.2M,
      led by Two Bear Capital with WRF Capital, NFX, YC Continuity Fund,
      FundersClub and BoxOne Ventures). They sit under Entrepreneurship as a
      `Company Financing` subsection that is **commented out**, not
      `\hide{}`-wrapped, so it stays invisible even under `\showalltrue` — the
      same treatment the CTO role bullets got in `e950458`.

      **Public figures only, deliberately.** This repo is public, so only what
      the company has itself announced goes in these files. Internal round
      history was used to check the public numbers and is not written down here.
      Non-dilutive funding is also left out, since Research Support already
      itemises the NIH awards and a grant total would double-count them.

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

**Blocker, found 2026-10-16.** The build does not run on this machine:
`cvstyle.sty` line 73 does `\RequirePackage{needspace}` and MiKTeX has no
`needspace.sty` installed. A plain `pdflatex` or `build.ps1` run does not fail —
it *hangs*, because MiKTeX stops at an interactive installer prompt that no one
is there to answer. Install it once and both go back to working:

```powershell
mpm --install=needspace
```

Until that runs, every edit since `e950458` is unbuilt, and `pino_cv.pdf` in the
repo is older than `pino_cv.tex`.
