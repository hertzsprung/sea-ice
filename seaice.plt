set term postscript eps enhanced color size 6,4

unset key
set autoscale
set view map
GR(t_b_18_7v, t_b_36_5v) = (t_b_36_5v - t_b_18_7v) / (t_b_36_5v + t_b_18_7v)
PR(t_b_18_7h, t_b_18_7v) = (t_b_18_7v - t_b_18_7h) / (t_b_18_7v + t_b_18_7h)

set output "gr.eps"
splot 'amsre.dat' using 1:2:(GR($3, $4)) with image

set output "pr.eps"
splot 'amsre.dat' using 1:2:(PR($5, $3)) with image
