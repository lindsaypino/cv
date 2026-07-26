# cv

LaTeX sources for Lindsay K. Pino's CV, short CV, and resume.

| Source | Output | Purpose |
| --- | --- | --- |
| `pino_cv.tex` | `pino_cv.pdf` | Full CV — all publications, talks, posters, service, teaching |
| `pino_cv-short.tex` | `pino_cv-short.pdf` | Condensed CV — selected publications and talks |
| `pino_resume.tex` | `pino_resume.pdf` | Industry resume — employment first, heavily trimmed |

Every build also drops a dated duplicate beside each output —
`pino_cv_YYYYMMDD.pdf` — so a PDF still shows its vintage after it has been
emailed. The date in the filename always matches the "Updated" line inside the
document. The undated copy is the one that gets committed and linked.

All three share a single preamble in `cvstyle.sty`, which defines the page
layout, fonts, colors, the `\mysection`/`\mysubsection` headings, the `V`
two-column table format, and the `\cvheader` name-and-contact block. Style
changes belong there, not in the individual documents.

The running header reads "Curriculum Vitae" by default; `pino_resume.tex`
overrides it with `\renewcommand{\cvdoctitle}{Resume}`.

Publication tallies live in `cvstyle.sty` too, as `\pubtotal` and
`\pubfirstauthor`, rendered by `\pubcount`. Update those two numbers when a paper
lands and all three documents follow; nothing else needs touching.

## Building

Built locally with [MiKTeX](https://miktex.org/). Dependencies are deliberately
minimal — everything except `etaremune` (94 KB, reverse-numbered lists) comes
with a Basic MiKTeX install, so there is no large font package to fetch.

On Windows, `make` is not available; use the bundled script, which runs MiKTeX's
`texify` (it repeats passes until cross-references and the reverse-numbered
lists settle):

```powershell
.\build.ps1
```

```powershell
.\build.ps1 -Clean
```

A single document, if you prefer to drive it by hand — note this produces only
the undated PDF; the dated duplicate comes from `build.ps1` or `make`:

```powershell
texify --pdf pino_cv.tex
```

The `makefile` does the same thing on Linux or macOS via `make`.

## The published PDF

The undated full CV is committed as the published record, and GitHub Pages serves
it, so the URL is both permanent and opens in the browser:

```
https://lindsaypino.github.io/cv/pino_cv.pdf
```

That is what <https://lindsaykpino.com> links to. Rebuild, commit `pino_cv.pdf`,
and the site serves the new version without the menu ever being touched.
`https://lindsaypino.github.io/cv/` redirects there too, via `index.html`.

Pages is what makes it open inline rather than download. The alternatives both
fall short: `raw.githubusercontent.com` sends `application/octet-stream`, so
browsers save the file instead of rendering it, and jsDelivr sends the right
`application/pdf` but with `max-age=604800`, so a visitor's browser would hold a
stale CV for a week after an update. Pages sends `application/pdf` with a short
cache.

`.nojekyll` stops Pages running the LaTeX sources through Jekyll. The short CV
and resume are gitignored; add a negation to `.gitignore` if you want to publish
those too.

Dated duplicates are deliberately *not* committed — they exist so an emailed PDF
carries its vintage, and committing them would mean a new file in the repository
on every build.

Worth knowing when committing PDFs:

- pdfTeX stamps every PDF with a creation timestamp and a random ID, so a rebuild
  produces different bytes even when no source changed. Commit the regenerated
  PDF when you are actually publishing; otherwise check it out again.
- Old dated PDFs are not removed automatically. `.\build.ps1 -Clean` clears them
  locally.

## Auditing the publication list

`audit_pubs.py` compares the DOIs in `pino_cv.tex` against the publication record
built by [MyPublications](https://github.com/lindsaypino/MyPublications), which
fetches from OpenAlex by ORCID and curates out junk types and duplicate
preprints. It reports what is in the record but missing from the CV (and the
reverse), and checks `\pubtotal`/`\pubfirstauthor` against what is actually
listed.

```powershell
python audit_pubs.py
```

It writes nothing — the `.tex` files stay authoritative, since deciding a paper's
section, author-list formatting, and whether an editorial counts are judgement
calls no API can make. Deliberate omissions live in the `EXCLUDE` dict at the top
of the script, each with its reason, so settled decisions are not re-reported.
Exit status is 1 when something needs a decision.

For fresher data, re-run `fetch_papers.py` in MyPublications first. Note the
audit only sees works whose metadata carries the ORCID, so a clean run means
"nothing new in the ORCID record" rather than "provably complete" — the script's
docstring documents a real example it misses, and PubMed is a useful cross-check.

## Credit

Originally adapted from [Will Fondrie's CV template](https://github.com/wfondrie/cv).
