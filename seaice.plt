set term postscript eps enhanced color size 6,4

set datafile missing 'NA'

unset key
set autoscale
set view map

set output "ice.eps"
plot 'amsre.dat' using 2:1:3 with points palette pointtype 0, \
 'world.dat' with lines lt 3
