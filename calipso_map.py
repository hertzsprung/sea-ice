#!/usr/bin/env python

from pyhdf import SD
import matplotlib.pyplot as plt
import numpy as np
import datetime
from mpl_toolkits.basemap import Basemap, cm

#----------------------
# Draw map

latmin = np.min(l1lat_r) - 0.02
latmax = np.max(l1lat_r) + 0.02
lonmin = np.min(l1lon_r) - 0.02
lonmax = np.max(l1lon_r) + 0.02
latts = (latmax + latmin)/2
#
m = Basemap(projection='npstere',boundinglat=50,lon_0=270,resolution='i')
#m = Basemap(resolution='c',projection='ortho',lat_0=60.,lon_0=-60.)
#m = Basemap(projection='merc',llcrnrlat=latmin,urcrnrlat=latmax,\
#             llcrnrlon=lonmin,urcrnrlon=lonmax,lat_ts=latts,resolution='i')

# create figure, add axes
fig1 = plt.figure(figsize=(8,10))
ax = fig1.add_axes([0.1,0.1,0.8,0.8])
# define parallels and meridians to draw.
parallels = np.arange(-80.,90,20.)
meridians = np.arange(0.,360.,20.)

x,y = m(l1lon_r,l1lat_r)
x2,y2 = m(l1lon[:],l1lat[:])

#m = Basemap(projection='merc',llcrnrlat=latmin,urcrnrlat=latmax,\
#             llcrnrlon=lonmin,urcrnrlon=lonmax,lat_ts=latts,resolution='i')

m.plot(x,y,linewidth = 1.5,color='r')
m.plot(x2,y2,linewidth = 1.5, color='b')
# draw coastlines, parallels, meridians.
m.drawcoastlines(linewidth=1)
m.drawmapboundary(fill_color='#ffffff')
m.drawparallels(parallels)
m.drawmeridians(meridians)
m.drawcoastlines()
plt.show()

