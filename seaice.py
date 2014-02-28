#!/usr/bin/env python

from pyhdf import SD

#File names
amsr_name = 'AMSR_E_L2A_BrightnessTemperatures_V10_201012141724_D.hdf'
callid1_name = 'CAL_LID_L1-ValStage1-V3-01.2010-12-14T17-23-02ZN.hdf'
callid2_name = 'CAL_LID_L2_333mCLay-ValStage1-V3-01.2010-12-14T17-23-02ZN.hdf'

amsr = SD.SD(amsr_name)
l1 = SD.SD(callid1_name)
l2 = SD.SD(callid2_name)


#Read AMSR-E
t_b_18_7v_grid = amsr.select("18.7V_Res.1_TB").get()
t_b_18_7h_grid = amsr.select("18.7H_Res.1_TB").get()
t_b_36_5v_grid = amsr.select("36.5V_Res.1_TB").get()

print '#x, y, 18_7v, 36_5v, 18_5h'

for x, t_b_18_7v_list in enumerate(t_b_18_7v_grid):
	for y, t_b_18_7v in enumerate(t_b_18_7v_list):
		print x, y, t_b_18_7v, t_b_36_5v_grid[x][y], t_b_18_7h_grid[x][y]

#Reading Calipso level 1 data

tab532 = l1.select('Total_Attenuated_Backscatter_532')
pab532 = l1.select('Perpendicular_Attenuated_Backscatter_532')
l1lon = l1.select('Longitude')
l1lat = l1.select('Latitude')
