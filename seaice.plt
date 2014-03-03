set term postscript eps enhanced color size 6,4

unset key
set autoscale
set view map
GR(t_b_18_7v, t_b_36_5v) = (t_b_36_5v - t_b_18_7v) / (t_b_36_5v + t_b_18_7v)
PR(t_b_18_7h, t_b_18_7v) = (t_b_18_7v - t_b_18_7h) / (t_b_18_7v + t_b_18_7h)

set output "pr.eps"
plot 'amsre.dat' using 7:6:(PR($5, $3)) with points palette pointtype 0, \
 'world.dat' with lines lt 3

set output "gr.eps"
plot 'amsre.dat' using 7:6:(GR($4, $3)) with points palette pointtype 0, \
 'world.dat' with lines lt 3
