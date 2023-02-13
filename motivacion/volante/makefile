simple:
	pdflatex -interaction=nonstopmode verdades_empiricas.tex

final: verdades_empiricas.png

../../aux/static/.git:
	git submodule update --init ../../aux/static/

verdades_empiricas.png: verdades_empiricas.pdf
	convert -density 300 verdades_empiricas.pdf -resize 100% png/verdades_empiricas.png

verdades_empiricas.pdf: ../../aux/static/.git
	pdflatex -interaction=nonstopmode verdades_empiricas.tex

