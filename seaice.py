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

#Calipso Analysis



#------------------------------
#Reading AMSR-E data
