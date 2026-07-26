"""Audit the CV's publication list against the OpenAlex-derived record.

Retrieval already lives in lindsaypino/MyPublications (fetch_papers.py: OpenAlex
works API, filtered by ORCID 0000-0003-1857-7222, with curation for junk types
and duplicate preprints). Rather than duplicate that logic here, this script
consumes the curated papers.json that repo produces and reports the differences.

Nothing is written. The .tex files stay the source of truth for wording,
author-list formatting, and which section a paper belongs in -- those are
judgement calls no bibliographic API can make.

Usage
-----
    python audit_pubs.py                        # fetch papers.json from GitHub
    python audit_pubs.py ..\\MyPublications\\papers.json   # or use a local copy

Exit status is 1 if there are unexplained differences, so this can be wired into
a CI check later; 0 when the CV and the record agree.

For fresher data, re-run fetch_papers.py in MyPublications first.

Known limitation
----------------
OpenAlex is filtered by ORCID, so it only sees works where the ORCID was
actually recorded on the metadata. That is not everything. A worked example: the
2026 bioRxiv preprint "CpG island density predicts CBP/p300 dependency across 3D
chromatin clusters" (10.64898/2026.05.04.722036) is indexed in PubMed under
"Pino LK" but is absent from the ORCID-filtered OpenAlex results, so this audit
cannot see it either. Treat a clean run as "nothing new in the ORCID record",
not "the CV is provably complete", and cross-check PubMed occasionally:

    https://pubmed.ncbi.nlm.nih.gov/?term=Pino+LK%5BAuthor%5D
"""
import json
import re
import sys
import urllib.request

PAPERS_URL = ("https://raw.githubusercontent.com/lindsaypino/"
              "MyPublications/main/papers.json")

CV_TEX = "pino_cv.tex"
STYLE = "cvstyle.sty"

# Works that are in the publication record but deliberately not in the CV's
# Peer-Reviewed Publications list. Keep the reason -- it is the whole point of
# the list, and it stops the audit from re-reporting settled decisions.
EXCLUDE = {
    "10.1039/d2mo90036j":
        "Editorial for the Molecular Omics special issue; listed under "
        "Professional Service > Editorial Boards instead.",
    "10.1039/d2mo90026b":
        "Introduction to the US HUPO 2021 themed collection; an editorial, "
        "listed under Professional Service instead.",
    "10.1016/j.bpj.2021.11.1145":
        "Biophysical Society meeting abstract; OpenAlex mistypes it as an "
        "article.",
    "10.1016/j.euprot.2019.07.009":
        "Team COUNCIL OF RICKS / EuPA YPIC 2017 submission. Left off the CV on "
        "purpose (2026-07-26); the 2018 YPIC Challenge paper is listed instead.",
    "10.1101/345686":
        "bioRxiv preprint of the 2020 Cell Reports paper "
        "(10.1016/j.celrep.2020.01.096). MyPublications' fuzzy dedupe misses "
        "it because the titles were rewritten (similarity 0.33 < 0.90).",
}


def norm_doi(d):
    if not d:
        return ""
    d = d.strip().lower().rstrip(".")
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", d)


def strip_tags(t):
    return re.sub(r"<[^>]+>", "", t or "").strip()


def load_record(source):
    if source:
        with open(source, encoding="utf-8") as f:
            return json.load(f), source
    req = urllib.request.Request(
        PAPERS_URL, headers={"User-Agent": "cv-audit (lindsay.pino@gmail.com)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r), PAPERS_URL


def cv_sections(tex):
    """Map section title -> list of {doi, first_author, raw} for each \\item."""
    out = {}
    parts = re.split(r"\\mysection\{([^}]*)\}", tex)
    for i in range(1, len(parts), 2):
        name, body = parts[i], parts[i + 1]
        if not re.search(r"Publication|Preprint", name):
            continue
        items = re.findall(r"\\item\s(.*?)(?=\n\s*\\item|\Z)", body, re.S)
        entries = []
        for it in items:
            flat = " ".join(it.split())
            m = re.search(r"doi\.org/(10\.[^\s,;]+)", flat)
            entries.append({
                "doi": norm_doi(m.group(1)) if m else "",
                # Her own name bolded at the very start means first author.
                "first_author": bool(re.match(r"\\textbf\{Pino L", flat)),
                "raw": flat,
            })
        out[name] = entries
    return out


def macro(style, name):
    m = re.search(r"\\newcommand\{\\" + name + r"\}\{(\d+)\}", style)
    return int(m.group(1)) if m else None


def main():
    source = sys.argv[1] if len(sys.argv) > 1 else None
    try:
        record, origin = load_record(source)
    except Exception as e:                      # network down, bad path, etc.
        print("could not load the publication record: %s" % e)
        return 2

    tex = open(CV_TEX, encoding="utf-8").read()
    style = open(STYLE, encoding="utf-8").read()

    sections = cv_sections(tex)
    cv_dois = {e["doi"]: s for s, es in sections.items() for e in es if e["doi"]}

    print("record : %s" % origin)
    print("         %d works" % len(record))
    print("CV     : %s -- %d entries with a DOI" % (CV_TEX, len(cv_dois)))
    print()

    missing, excluded = [], []
    for p in record:
        d = norm_doi(p.get("doi"))
        if not d or d in cv_dois:
            continue
        (excluded if d in EXCLUDE else missing).append((d, p))

    print("=" * 72)
    print("IN THE RECORD, NOT IN THE CV -- %d needing a decision" % len(missing))
    print("=" * 72)
    if not missing:
        print("  nothing outstanding")
    for d, p in sorted(missing, key=lambda x: (x[1].get("type") or "",
                                               -(x[1].get("year") or 0))):
        authors = [a for a in (p.get("authors") or []) if a]
        first = " FIRST AUTHOR" if authors and "pino" in authors[0].lower() else ""
        print("  [%s %s]%s" % (p.get("type"), p.get("year"), first))
        print("    %s" % strip_tags(p.get("title"))[:78])
        print("    %-34s %s" % (d, (p.get("venue") or "")[:34]))
    print()

    if excluded:
        print("Known exclusions, still matching the record (no action needed):")
        for d, p in excluded:
            print("  %-30s %s" % (d, EXCLUDE[d].split(". ")[0]))
        print()

    orphans = [d for d in cv_dois if not any(
        norm_doi(p.get("doi")) == d for p in record)]
    print("IN THE CV, NOT IN THE RECORD -- %d" % len(orphans))
    if orphans:
        print("  (worth checking: a typo'd DOI, or a venue OpenAlex has not "
              "indexed under your ORCID)")
        for d in orphans:
            print("    %-46s [%s]" % (d, cv_dois[d]))
    else:
        print("  none -- every DOI in the CV is corroborated")
    print()

    # Purely local consistency check; needs no network.
    peer = sections.get("Peer-Reviewed Publications", [])
    counted, declared = len(peer), macro(style, "pubtotal")
    fa_counted = sum(1 for e in peer if e["first_author"])
    fa_declared = macro(style, "pubfirstauthor")
    print("COUNT CHECK (cvstyle.sty vs what is actually listed)")
    for label, dec, act in (("pubtotal", declared, counted),
                            ("pubfirstauthor", fa_declared, fa_counted)):
        mark = "ok" if dec == act else "MISMATCH"
        print("  \\%-16s declared %-4s actual %-4s %s" % (label, dec, act, mark))

    stale = declared != counted or fa_declared != fa_counted
    return 1 if (missing or orphans or stale) else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
