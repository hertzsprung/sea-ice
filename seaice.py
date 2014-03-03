#!/usr/bin/env python

from pyhdf import SD
import matplotlib.pyplot as plt
import numpy as np
import datetime

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
	return 0.35 * pr - 0.01175

def ice(pr, gr):
	if (pr < 0.05 or pr > 0.25):
		return 'NA'
	elif (gr >= gr_low(pr) and gr <= gr_high(pr)):
		return 1.0 - ((pr-0.05) * 5.0)
	else:
		return 'NA'

#File names
amsr_name = 'AMSR_E_L2A_BrightnessTemperatures_V10_201012141724_D.hdf'

amsr = SD.SD(amsr_name)

#Read AMSR-E
t_b_18_7v_grid = amsr.select("18.7V_Res.1_TB").get()
t_b_18_7h_grid = amsr.select("18.7H_Res.1_TB").get()
t_b_36_5v_grid = amsr.select("36.5V_Res.1_TB").get()
latitude_grid = amsr.select("Latitude").get()
longitude_grid = amsr.select("Longitude").get()

print '#lat long ice pr gr gr_low gr_high'

for x, t_b_18_7v_list in enumerate(t_b_18_7v_grid):
	for y, t_b_18_7v in enumerate(t_b_18_7v_list):
		t_b_19v_rescaled = 0.01 * float(t_b_18_7v) + 327.68
		t_b_19h_rescaled = 0.01 * float(t_b_18_7h_grid[x][y]) + 327.68
		t_b_37v_rescaled = 0.01 * float(t_b_36_5v_grid[x][y]) + 327.68
		gr_value = gr(t_b_37v_rescaled, t_b_19v_rescaled)
		pr_value = pr(t_b_19v_rescaled, t_b_19h_rescaled)
		print latitude_grid[x][y], longitude_grid[x][y], ice(pr_value, gr_value), pr_value, gr_value, gr_low(pr_value), gr_high(pr_value)
