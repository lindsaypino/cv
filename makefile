DOCS  = pino_cv pino_cv-short pino_resume
STAMP = $(shell date +%Y%m%d)
# Outputs carry the build date: pino_cv_YYYYMMDD.pdf
PDFS  = $(foreach d,$(DOCS),$(d)_$(STAMP).pdf)

all: $(PDFS)

# Build <doc>.pdf from <doc>.tex, then rename to the dated form.
%_$(STAMP).pdf: %.tex cvstyle.sty
	pdflatex $*.tex
	if ( grep -q citation $*.aux ) ; then \
		bibtex $* ; \
		pdflatex $*.tex ; \
	fi
	pdflatex $*.tex
	mv $*.pdf $@

clean:
	rm -f $(addsuffix .aux,$(DOCS)) $(addsuffix .log,$(DOCS)) \
		$(addsuffix .out,$(DOCS)) $(addsuffix .bbl,$(DOCS)) \
		$(addsuffix .blg,$(DOCS))

distclean: clean
	rm -f $(addsuffix .pdf,$(DOCS)) $(foreach d,$(DOCS),$(d)_*.pdf)

.PHONY: all clean distclean
