.phony: all

all: amsre.dat
	gnuplot -p -e 'load "seaice.plt"'

amsre.dat: seaice.py
	./seaice.py > amsre.dat

