simple: BayesPlurinacional.pdf PlurinationalBayes.pdf

extensa: main-extensa-es.pdf main-extensa-en.pdf

BayesPlurinacional.pdf:
	sed -i 's/\\entrue/\\estrue/g' main-simple.tex
	pdflatex main-simple.tex
	mv main-simple.pdf BayesPlurinacional.pdf

PlurinationalBayes.pdf:
	sed -i 's/\\estrue/\\entrue/g' main-simple.tex
	pdflatex main-simple.tex
	mv main-simple.pdf PlurinationalBayes.pdf

main-extensa-es.pdf:
	sed -i 's/\\entrue/\\estrue/g' main-extensa.tex
	pdflatex main-extensa.tex
	mv main-extensa.pdf main-extensa-es.pdf

main-extensa-en.pdf:
	sed -i 's/\\estrue/\\entrue/g' main-extensa.tex
	pdflatex main-extensa.tex
	mv main-extensa.pdf main-extensa-en.pdf
