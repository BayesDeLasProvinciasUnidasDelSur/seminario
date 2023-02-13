all: main-es.pdf main-en.pdf

main-es.pdf:
	sed -i 's/\\entrue/\\estrue/g' main-simple.tex
	pdflatex main-simple.tex
	mv main-simple.pdf BayesPlurinacional.pdf

main-en.pdf:
	sed -i 's/\\estrue/\\entrue/g' main-simple.tex
	pdflatex main-simple.tex
	mv main-simple.pdf PlurinationalBayes.pdf
