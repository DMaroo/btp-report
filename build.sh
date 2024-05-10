#!/bin/sh

rm report.{aux,out}
pdflatex -halt-on-error -shell-escape report.tex &&
bibtex report &&
pdflatex -halt-on-error -shell-escape report.tex &&
pdflatex -halt-on-error -shell-escape report.tex

