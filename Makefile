.phony: all

all: amsre.dat
	gnuplot -p -e 'load "seaice.plt"'

amsre.dat: seaice.py *.hdf
	./seaice.py > amsre.dat

irradiance: irradiance.f90
	gfortran -o irradiance irradiance.f90
