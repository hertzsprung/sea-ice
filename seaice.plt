set terminal pngcairo size 1600,1200 enhanced

set datafile missing 'NA'

unset key
set autoscale
set view map

spatial_filter = "< awk '{ if ($2 > -110 && $2 < -80 && $1 > 75 && $1 < 80) print $1, $2, $3, $4 }' "

set palette defined ( 0 '#FFFFD9',\
    	    	      1 '#EDF8B1',\
		      2 '#C7E9B4',\
		      3 '#7FCDBB',\
		      4 '#41B6C4',\
		      5 '#1D91C0',\
		      6 '#225EA8',\
		      7 '#0C2C84' )
#set palette negative

set output "ice-fy.png"
set xrange [-180:180]
set yrange [-90:90]
#plot 'amsre.dat' using 2:1:3 with points palette pointtype 0, \
# 'world_10m.txt' with lines lt 3

#set output "ice-my.png"
#plot 'amsre.dat' using 2:1:4 with points palette pointtype 0, \
# 'world_10m.txt' with lines lt 3

set output "ice-total.png"
plot 'amsre.dat' using 2:1:($3+$4) with points palette pointtype 0, \
 'world_10m.txt' with lines lt 3

#set output "ice-extent-zoom.png"
#set xrange [-110:-80]
#set yrange [75:80]
#plot spatial_filter.'amsre.dat' using 2:1:3 with points palette pointtype 7 pointsize 3, \
# 'world_10m.txt' with lines lt 3

#set output "ice-my-zoom.png"
#set xrange [-110:-80]
#set yrange [75:80]
#plot spatial_filter.'amsre.dat' using 2:1:4 with points palette pointtype 7 pointsize 3, \
# 'world_10m.txt' with lines lt 3

set output "ice-total-zoom.png"
set xrange [-110:-80]
set yrange [75:80]
plot spatial_filter.'amsre.dat' using 2:1:($3+$4) with points palette pointtype 7 pointsize 3, \
 'world_10m.txt' with lines lt 3

#set output "ice-fy-zoom.png"
#set xrange [-110:-80]
#set yrange [75:80]
#plot spatial_filter.'amsre.dat' using 2:1:3 with points palette pointtype 7 pointsize 3, \
# 'world_10m.txt' with lines lt 3

set output "amsre.png"
set xrange [0:0.3]
plot 0.75 * x - 0.1175 with line, \
     0.35 * x - 0.0175 with line
