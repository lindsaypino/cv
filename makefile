DOCS  = pino_cv pino_cv-short pino_resume
STAMP = $(shell date +%Y%m%d)
# The undated PDF is the committed, permanently linkable copy; a dated duplicate
# (pino_cv_YYYYMMDD.pdf) sits beside it so an emailed PDF shows its vintage.
PDFS  = $(foreach d,$(DOCS),$(d).pdf)

all: $(PDFS)
	@for d in $(DOCS); do cp $$d.pdf $${d}_$(STAMP).pdf; done

%.pdf: %.tex cvstyle.sty
	pdflatex $*.tex
	if ( grep -q citation $*.aux ) ; then \
		bibtex $* ; \
		pdflatex $*.tex ; \
	fi
	pdflatex $*.tex

clean:
	rm -f $(addsuffix .aux,$(DOCS)) $(addsuffix .log,$(DOCS)) \
		$(addsuffix .out,$(DOCS)) $(addsuffix .bbl,$(DOCS)) \
		$(addsuffix .blg,$(DOCS))

distclean: clean
	rm -f $(addsuffix .pdf,$(DOCS)) $(foreach d,$(DOCS),$(d)_*.pdf)

.PHONY: all clean distclean
