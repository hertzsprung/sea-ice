#!/usr/bin/env python

from pyhdf import SD
import matplotlib.pyplot as plt
import numpy as np
import datetime

#File names
amsr_name = 'AMSR_E_L2A_BrightnessTemperatures_V10_201012141724_D.hdf'
callid1_name = 'CAL_LID_L1-ValStage1-V3-01.2010-12-14T17-23-02ZN.hdf'
callid2_name = 'CAL_LID_L2_333mCLay-ValStage1-V3-01.2010-12-14T17-23-02ZN.hdf'

amsr = SD.SD(amsr_name)
l1 = SD.SD(callid1_name)
l2 = SD.SD(callid2_name)


#Reading Calipso level 1 data

l1utc = l1.select('Profile_UTC_Time')
l1tab532 = l1.select('Total_Attenuated_Backscatter_532')
l1pab532 = l1.select('Perpendicular_Attenuated_Backscatter_532')
l1lon = l1.select('Longitude')
l1lat = l1.select('Latitude')

#Reading Calipso level 2 data
# Infrared Radiometer (IIR) Data

l2utc = l2.select('Profile_UTC_Time')
l2lse = l2.select('Lidar_Surface_Elevation')

# Calipso Analysis
# focus on UTC: 17.4-17.5 UTC

l2time = (l2utc[:] - l2utc[:].astype(int))*24.0	#UTC time in hours
l2time_index = [i for i, x in enumerate(l1time) if x > 17.4 and x < 17.5]
l2time_min = min(l2time_index)
l2time_max = max(l2time_index)

# Select 17.4-17.5 UTC data
l2time_r = l2time[l2time_min:l2time_max]
l2lse_r = l2lse[l2time_min:l2time_max]

l1tab532_r = l1tab532[l2time_min:l2time_max]
l1pab532_r = l1pab532[l2time_min:l2time_max]
l1lon_r = l1lon[l2time_min:l2time_max]
l1lat_r = l1lat[l2time_min:l2time_max]


# time_utc_l2 = (time_prof_l2-long(time_prof_l2))*24.0 ; time in UTC (hours)
#     z = where( abs(time_utc_l2-17.45) le 0.5, n1)
#     if (n1 gt 0) then surf_elv = surf_elv(*,z)

