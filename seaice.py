#!/usr/bin/env python

from pyhdf import SD
import matplotlib.pyplot as plt
import numpy as np
import datetime

#File names
amsr_name = 'AMSR_E_L2A_BrightnessTemperatures_V10_201012141724_D.hdf'

amsr = SD.SD(amsr_name)

#Read AMSR-E
t_b_18_7v_grid = amsr.select("18.7V_Res.1_TB").get()
t_b_18_7h_grid = amsr.select("18.7H_Res.1_TB").get()
t_b_36_5v_grid = amsr.select("36.5V_Res.1_TB").get()
latitude_grid = amsr.select("Latitude").get()
longitude_grid = amsr.select("Longitude").get()

print '#x, y, 18_7v, 36_5v, 18_7h, lat, long'

for x, t_b_18_7v_list in enumerate(t_b_18_7v_grid):
	for y, t_b_18_7v in enumerate(t_b_18_7v_list):
		print x, y, t_b_18_7v, t_b_36_5v_grid[x][y], t_b_18_7h_grid[x][y], latitude_grid[x][y], longitude_grid[x][y]
