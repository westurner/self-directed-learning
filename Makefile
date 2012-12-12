# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = _build

SLIDES_BUILDDIR = $(BUILDDIR)/slides
SLIDES_FILE		 = slides.rst
SLIDES_TMP		 = $(SLIDES_BUILDDIR)/$(SLIDES_FILE)_
SLIDES_OUTP		 = $(SLIDES_BUILDDIR)/index.html

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man changes linkcheck doctest gettext

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  dirhtml    to make HTML files named index.html in directories"
	@echo "  singlehtml to make a single large HTML file"
	@echo "  pickle     to make pickle files"
	@echo "  json       to make JSON files"
	@echo "  htmlhelp   to make HTML files and a HTML help project"
	@echo "  qthelp     to make HTML files and a qthelp project"
	@echo "  devhelp    to make HTML files and a Devhelp project"
	@echo "  epub       to make an epub"
	@echo "  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
	@echo "  text       to make text files"
	@echo "  man        to make manual pages"
	@echo "  texinfo    to make Texinfo files"
	@echo "  info       to make Texinfo files and run them through makeinfo"
	@echo "  gettext    to make PO message catalogs"
	@echo "  changes    to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  doctest    to run all doctests embedded in the documentation (if enabled)"
	@echo ""
	@echo "  setup_ubuntu               to setup ubuntu dependencies"
	@echo "  sphinx_deps_ubuntu         to install sphinx build dependencies"
	@echo "  latex_build_deps_ubuntu    to install LaTeX build dependencies"
	@echo "  rst2pdf_build_deps_ubuntu  to install rst2pdf build dependencies"
	@echo ""
	@echo "  rst2pdf           to make a PDF with rst2pdf"
	@echo "  rst2pdf_open      to open rst2pdf PDF"
	@echo "  rst2pdf_preview   to make a PDF with rdt2pdf and open it"
	@echo ""
	@echo "  html_open         to browse to _build/html/index.html"
	@echo "  html_preview      to make HTML files and browse to index.html"
	@echo ""
	@echo "  latexpdf_open     to open _build/latex"
	@echo "  latexpdf_preview  to make a PDF with pdflatex and open it"
	@echo ""
	@echo "  s5                to make S5 slides with rst2s5.py"
	@echo "  s5_open           to browse to _build/slides/index.html"
	@echo "  s5_preview        to make S5 slides with rst2s5.py and open them"
	@echo ""
	@echo "  auto_setup  to install pyinotify and autocompile.py"
	@echo "              NOTE: remember to refresh the browser"
	@echo "  auto_html   to rebuild HTML when files change"
	@echo "  auto_s5     to build S5 slides when files change"
	@echo "  auto_shtml  to rebuild singlehtml when files change"


clean:
	-rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

dirhtml:
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."

singlehtml:
	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/singlehtml
	@echo
	@echo "Build finished. The HTML page is in $(BUILDDIR)/singlehtml."

pickle:
	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) $(BUILDDIR)/pickle
	@echo
	@echo "Build finished; now you can process the pickle files."

json:
	$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) $(BUILDDIR)/json
	@echo
	@echo "Build finished; now you can process the JSON files."

htmlhelp:
	$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) $(BUILDDIR)/htmlhelp
	@echo
	@echo "Build finished; now you can run HTML Help Workshop with the" \
	      ".hhp project file in $(BUILDDIR)/htmlhelp."

qthelp:
	$(SPHINXBUILD) -b qthelp $(ALLSPHINXOPTS) $(BUILDDIR)/qthelp
	@echo
	@echo "Build finished; now you can run "qcollectiongenerator" with the" \
	      ".qhcp project file in $(BUILDDIR)/qthelp, like this:"
	@echo "# qcollectiongenerator $(BUILDDIR)/qthelp/TechWPaper.qhcp"
	@echo "To view the help file:"
	@echo "# assistant -collectionFile $(BUILDDIR)/qthelp/TechWPaper.qhc"

devhelp:
	$(SPHINXBUILD) -b devhelp $(ALLSPHINXOPTS) $(BUILDDIR)/devhelp
	@echo
	@echo "Build finished."
	@echo "To view the help file:"
	@echo "# mkdir -p $$HOME/.local/share/devhelp/TechWPaper"
	@echo "# ln -s $(BUILDDIR)/devhelp $$HOME/.local/share/devhelp/TechWPaper"
	@echo "# devhelp"

epub:
	$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $(BUILDDIR)/epub
	@echo
	@echo "Build finished. The epub file is in $(BUILDDIR)/epub."

latex:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo
	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."
	@echo "Run \`make' in that directory to run these through (pdf)latex" \
	      "(use \`make latexpdf' here to do that automatically)."

latexpdf:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through pdflatex..."
	$(MAKE) -C $(BUILDDIR)/latex all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

text:
	$(SPHINXBUILD) -b text $(ALLSPHINXOPTS) $(BUILDDIR)/text
	@echo
	@echo "Build finished. The text files are in $(BUILDDIR)/text."

man:
	$(SPHINXBUILD) -b man $(ALLSPHINXOPTS) $(BUILDDIR)/man
	@echo
	@echo "Build finished. The manual pages are in $(BUILDDIR)/man."

texinfo:
	$(SPHINXBUILD) -b texinfo $(ALLSPHINXOPTS) $(BUILDDIR)/texinfo
	@echo
	@echo "Build finished. The Texinfo files are in $(BUILDDIR)/texinfo."
	@echo "Run \`make' in that directory to run these through makeinfo" \
	      "(use \`make info' here to do that automatically)."

info:
	$(SPHINXBUILD) -b texinfo $(ALLSPHINXOPTS) $(BUILDDIR)/texinfo
	@echo "Running Texinfo files through makeinfo..."
	make -C $(BUILDDIR)/texinfo info
	@echo "makeinfo finished; the Info files are in $(BUILDDIR)/texinfo."

gettext:
	$(SPHINXBUILD) -b gettext $(I18NSPHINXOPTS) $(BUILDDIR)/locale
	@echo
	@echo "Build finished. The message catalogs are in $(BUILDDIR)/locale."

changes:
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

doctest:
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in $(BUILDDIR)/doctest/output.txt."

latex_build_deps_ubuntu:
	sudo apt-get install -y texlive-latex-base \
							texlive-latex-extra \
							texlive-latex-recommended \
							texlive-fonts-recommended

rst2pdf_build_deps_ubuntu:
	sudo apt-get install -y rst2pdf

sphinx_deps_ubuntu:
	sudo apt-get install -y \
								--install-suggests \
								   python-sphinx \
									python-sphinxcontrib.issuetracer \
									python-sphinxcontrib.spelling
								  #python3-sphinx

setup_ubuntu: rst2pdf_build_deps_ubuntu latex_build_deps_ubuntu sphinx_deps_ubuntu auto_setup
	

rst2pdf:
	mkdir -p pdfrst
	rst2pdf --break-level=1 \
			--stylesheets=_static/pdf.styles \
			--repeat-table-rows \
			report.rst -o _build/pdfrst/report.pdf

rst2pdf_open:
	evince _build/pdf-rst/report.pdf

rst2pdf_preview: rst2pdf rst2pdf_open


html_open:
	sensible-browser ./_build/html/index.html

html_preview: html html_open


latex_debug:
	cd _build/latex/
	gvim -p _build/latex/*.tex \
				_build/latex/*.aux \
				_build/latex/*.toc \
				_build/latex/*.out \
				_build/latex/*.log \
				_build/latex/*.idx

latexpdf_open:
	evince _build/latex/TechWPaper.pdf

latexpdf_preview: latexpdf latexpdf_open


s5: 
	[ -d $(SLIDES_BUILDDIR) ] || rm -rf $(SLIDES_BUILDDIR)
	mkdir -p $(SLIDES_BUILDDIR)
	cp $(SLIDES_FILE) $(SLIDES_TMP)
	sed -i 's/:term:`\(.*\)`/**\1**/g' $(SLIDES_TMP)
	sed -i 's/:ref:`\(.*\)`/**\1**/g' $(SLIDES_TMP)
	sed -i 's/:pypi:`\(.*\)/**\1**/g' $(SLIDES_TMP)
	# TODO
	rst2s5.py \
		--section-numbering \
		--title='' \
		--date \
		--time \
		--strip-elements-with-class notes \
		--current-slide \
		--compact-lists \
		--embed-stylesheet \
		--attribution=parentheses \
		--table-style=borderless \
		--cloak-email-addresses \
		--view-mode=outline \
		--theme=small-white \
		 $(SLIDES_TMP) \
		 $(SLIDES_OUTP)

s5_open:
	sensible-browser $(SLIDES_OUTP)

s5_preview: s5 s5_open



auto_setup:
	pip install pyinotify
	wget https://raw.github.com/seb-m/pyinotify/master/python2/examples/autocompile.py

auto_html: html_preview
	python ./autocompile.py . '.rst,Makefile,conf.py,theme.conf' "make html"

auto_s5: s5_preview
	python ./autocompile.py . '.rst,Makefile' "make s5"

GLOSSARY_TERMS=_glossary_undefined.rst

glossary_terms: clean
	make html 2>&1 \
		| grep 'term not in glossary' \
		| awk '{ path = print $$7,$$8,$$9,$$10  }' \
	    | tee $(GLOSSARY_TERMS)

glossary_terms_uniq: check_glossary_terms
	cat $(GLOSSARY_TERMS) \
		| sort \
	   	| uniq -c \
		| sort -n -r
