DOCS = pino_cv pino_cv-short pino_resume
PDFS = $(addsuffix .pdf,$(DOCS))

all: $(PDFS)

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
	rm -f $(PDFS)

.PHONY: all clean distclean
