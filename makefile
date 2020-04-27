all: submodules

submodules: biblio/.git

biblio/.git:
	git submodule update --init biblio/


