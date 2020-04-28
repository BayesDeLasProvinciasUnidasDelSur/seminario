all: submodules pdf

pdf:

figs:
	make -C figures


submodules: 
	make -C aux


