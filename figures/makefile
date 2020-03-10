######################
## R requirements   ##
## /usr/bin/Rscript ##
######################

all:
	/usr/bin/Rscript main.R
	rm Rplots.pdf
	for i in *.tex; do pdflatex $i;done

python:
	/usr/bin/python3 linearRegression.py
	/usr/bin/python3 model_selection.py

