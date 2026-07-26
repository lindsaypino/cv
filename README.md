# cv

LaTeX sources for Lindsay K. Pino's CV, short CV, and resume.

| Source | Output | Purpose |
| --- | --- | --- |
| `pino_cv.tex` | `pino_cv.pdf` | Full CV — all publications, talks, posters, service, teaching |
| `pino_cv-short.tex` | `pino_cv-short.pdf` | Condensed CV — selected publications and talks |
| `pino_resume.tex` | `pino_resume.pdf` | Industry resume — employment first, heavily trimmed |

All three share a single preamble in `cvstyle.sty`, which defines the page
layout, fonts, colors, the `\mysection`/`\mysubsection` headings, the `\tdim`
two-column table format, and the `\cvheader` name-and-contact block. Style
changes belong there, not in the individual documents.

The running header reads "Curriculum Vitae" by default; `pino_resume.tex`
overrides it with `\renewcommand{\cvdoctitle}{Resume}`.

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

A single document, if you prefer to drive it by hand:

```powershell
texify --pdf pino_cv.tex
```

The `makefile` does the same thing on Linux or macOS via `make`.

Generated PDFs and LaTeX aux files are gitignored. To publish a built PDF
anyway, add it explicitly with `git add -f pino_cv.pdf`.

## Credit

Originally adapted from [Will Fondrie's CV template](https://github.com/wfondrie/cv).
