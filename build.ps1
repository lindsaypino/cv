<#
.SYNOPSIS
    Build the CV, short CV, and resume PDFs with MiKTeX.

.DESCRIPTION
    Uses MiKTeX's texify, which reruns pdflatex until cross-references and the
    reverse-numbered (etaremune) lists stop changing. Windows has no `make`, so
    this stands in for the makefile; the makefile still works on Linux/macOS.

.PARAMETER Clean
    Delete LaTeX auxiliary files and the generated PDFs instead of building.

.PARAMETER Quiet
    Suppress texify's per-pass chatter; only report pass/fail per document.
#>
[CmdletBinding()]
param(
    [switch]$Clean,
    [switch]$Quiet
)

$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot

$docs = @('pino_cv', 'pino_cv-short', 'pino_resume')
$auxExt = @('aux', 'log', 'out', 'bbl', 'blg', 'toc', 'fls', 'fdb_latexmk')

# Build date, stamped into each output filename (pino_cv_YYYYMMDD.pdf) so a PDF
# carries its own vintage once it has been emailed or uploaded somewhere.
$stamp = Get-Date -Format 'yyyyMMdd'

if ($Clean) {
    foreach ($d in $docs) {
        foreach ($e in $auxExt + @('pdf')) {
            $p = "$d.$e"
            if (Test-Path $p) { Remove-Item $p -Force; "removed $p" }
        }
        # Dated outputs from this and any earlier build.
        Get-ChildItem -File -Filter "${d}_*.pdf" -ErrorAction SilentlyContinue |
            ForEach-Object { Remove-Item $_.FullName -Force; "removed $($_.Name)" }
    }
    return
}

# texify is not on PATH by default for a per-user MiKTeX install.
$texify = (Get-Command texify -ErrorAction SilentlyContinue).Source
if (-not $texify) {
    $candidates = @(
        "$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64\texify.exe",
        "$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\texify.exe",
        "$env:ProgramFiles\MiKTeX\miktex\bin\x64\texify.exe"
    )
    $texify = $candidates | Where-Object { Test-Path $_ } | Select-Object -First 1
}
if (-not $texify) {
    throw "texify not found. Install MiKTeX (winget install MiKTeX.MiKTeX) or add it to PATH."
}

$failed = @()
foreach ($d in $docs) {
    $args = @('--pdf')
    if ($Quiet) { $args += '--quiet' }
    & $texify @args "$d.tex"
    if ($LASTEXITCODE -ne 0) {
        $failed += $d
        Write-Warning "$d failed (exit $LASTEXITCODE) - see $d.log"
    }
    else {
        # Surface anything worth looking at; ignore routine font-shape notices.
        $warn = Select-String -Path "$d.log" -Pattern 'Overfull|Underfull|LaTeX Warning' -ErrorAction SilentlyContinue |
            Where-Object { $_.Line -notmatch 'Font shape|\(Font\)' }
        $suffix = if ($warn) { "$($warn.Count) warning(s)" } else { 'clean' }

        # pdflatex names its output after the .tex file; rename to the dated form.
        $dated = "${d}_$stamp.pdf"
        if (Test-Path $dated) { Remove-Item $dated -Force }
        Move-Item -LiteralPath "$d.pdf" -Destination $dated
        "built $dated - $suffix"
    }
}

foreach ($d in $docs) {
    foreach ($e in $auxExt) {
        if (Test-Path "$d.$e") { Remove-Item "$d.$e" -Force }
    }
}

if ($failed.Count) { throw "failed: $($failed -join ', ')" }
"all documents built"
