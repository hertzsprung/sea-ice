#!/usr/bin/env python

from pyhdf import SD
import matplotlib.pyplot as plt
import numpy as np
import datetime
import os

def gr(t_b_37v, t_b_19v):
	if (t_b_37v + t_b_19v == 0):
		return 0.0
	else:
		return (t_b_37v - t_b_19v)/(t_b_37v + t_b_19v)

def pr(t_b_19v, t_b_19h):
	if (t_b_19h + t_b_19v == 0):
		return 0.0
	else:
		return (t_b_19v - t_b_19h)/(t_b_19v + t_b_19h)

def gr_low(pr):
	return 0.75 * pr - 0.1175

def gr_high(pr):
	return 0.35 * pr - 0.0175

def ice(pr, gr):
	F_0 = 2782.3
	F_1 = -20044
	F_2 = 19935
	F_3 = 41660
	M_0 = -690.38
	M_1 = 14990
	M_2 = -27579
	M_3 = -43260
	D_0 = 1648.2
	D_1 = 7735.6
	D_2 = -4112.2
	D_3 = -10200
	D=D_0+D_1*pr + D_2*gr + D_3*pr*gr
	C_FY = (F_0 + F_1 * pr + F_2 * gr + F_3 * pr * gr) / D
	C_MY = (M_0 + M_1 * pr + M_2 * gr + M_3 * pr * gr) / D
	if (C_FY < 0 or C_FY > 1):
		C_FY = 'NA'
	if (C_MY < 0 or C_MY > 1):
		C_MY = 'NA'
	return (C_FY, C_MY)

def parse(filename):
	amsr = SD.SD(filename)
	t_b_18_7v_grid = amsr.select("18.7V_Res.1_TB").get()
	t_b_18_7h_grid = amsr.select("18.7H_Res.1_TB").get()
	t_b_36_5v_grid = amsr.select("36.5V_Res.1_TB").get()
	latitude_grid = amsr.select("Latitude").get()
	longitude_grid = amsr.select("Longitude").get()

	for x, t_b_18_7v_list in enumerate(t_b_18_7v_grid):
		for y, t_b_18_7v in enumerate(t_b_18_7v_list):
			t_b_19v_rescaled = 0.01 * float(t_b_18_7v) + 327.68
			t_b_19h_rescaled = 0.01 * float(t_b_18_7h_grid[x][y]) + 327.68
			t_b_37v_rescaled = 0.01 * float(t_b_36_5v_grid[x][y]) + 327.68
			gr_value = gr(t_b_37v_rescaled, t_b_19v_rescaled)
			pr_value = pr(t_b_19v_rescaled, t_b_19h_rescaled)
			fy, my = ice(pr_value, gr_value)
			print latitude_grid[x][y], longitude_grid[x][y], fy, my

print '#lat long ice_extent ice_age'
for f in os.listdir("."):
    if f.startswith("AMSR") and f.endswith(".hdf"):
	print '#', f
        parse(f)

