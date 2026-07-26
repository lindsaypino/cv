# cv

LaTeX sources for Lindsay K. Pino's CV, short CV, and resume.

| Source | Output | Purpose |
| --- | --- | --- |
| `pino_cv.tex` | `pino_cv_YYYYMMDD.pdf` | Full CV — all publications, talks, posters, service, teaching |
| `pino_cv-short.tex` | `pino_cv-short_YYYYMMDD.pdf` | Condensed CV — selected publications and talks |
| `pino_resume.tex` | `pino_resume_YYYYMMDD.pdf` | Industry resume — employment first, heavily trimmed |

Outputs are stamped with the build date, so a PDF still shows its vintage after
it has been emailed or uploaded. The date in the filename always matches the
"Updated" line inside the document.

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

A single document, if you prefer to drive it by hand — note this leaves the
undated `pino_cv.pdf`; only `build.ps1` and `make` apply the date stamp:

```powershell
texify --pdf pino_cv.tex
```

The `makefile` does the same thing on Linux or macOS via `make`.

## The published PDF

Dated builds of the full CV are committed as the published record, e.g.
`pino_cv_20260726.pdf`. The short CV and resume are gitignored; add a negation to
`.gitignore` if you want to publish those too.

Because the filename changes with each build, there is no fixed download URL —
link to the newest file, or to the repository itself. If you would rather have a
permanent link, commit an undated copy alongside the dated one and point at that.

Two things worth knowing when committing PDFs:

- pdfTeX stamps every PDF with a creation timestamp and a random ID, so a rebuild
  produces different bytes even when no source changed. Commit the regenerated
  PDF when you are actually publishing; otherwise delete it.
- Old dated PDFs are not removed automatically. `.\build.ps1 -Clean` clears them
  locally; `git rm` the ones you no longer want published.

## Credit

Originally adapted from [Will Fondrie's CV template](https://github.com/wfondrie/cv).
