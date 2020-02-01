"""
Created on Sat Jan 31st 2020 

@author: rodell
"""
import context
import numpy as np
import xarray as xr
from pathlib import Path
import cartopy.crs as crs
from netCDF4 import Dataset
from context import data_dir
from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm

from cr507.utils.read_wrf import readwrf
from matplotlib.dates import DateFormatter
import matplotlib.gridspec as gridspec


from wrf import (to_np, getvar, g_uvmet, ll_to_xy, get_cartopy, latlon_coords)

""" ####################################################################### """
""" ###################### Grab WRF Variables ####################### """


wrf_base = str(data_dir) + str('/wrf_data/wrf_base/')

wrf_ysu  = str(data_dir) + str('/wrf_data/wrf_ysu/')

ds_base = readwrf(wrf_base)
ds_ysu  = readwrf(wrf_ysu)

cord = get_cartopy(ds_base.rh2)
lat, lon = latlon_coords(ds_base.rh2)


""" ####################################################################### """
""" ############################# Make Plots ############################## """

fig2 = plt.figure(constrained_layout=True)
spec2 = gridspec.GridSpec(ncols=3, nrows=2, figure=fig2)
f2_ax1 = fig2.add_subplot(spec2[0, 0], projection=cord)
f2_ax2 = fig2.add_subplot(spec2[0, 1], projection=cord)
f2_ax3 = fig2.add_subplot(spec2[0, 2], projection=cord)
f2_ax4 = fig2.add_subplot(spec2[1, 0], projection=cord)
f2_ax5 = fig2.add_subplot(spec2[1, 1], projection=cord)
f2_ax6 = fig2.add_subplot(spec2[1, 2], projection=cord)

cmap = cm.BrBG
level = np.arange(0,100,10)
# norm = mpl.colors.BoundaryNorm(bounds, cmap)

f2_ax1.set_title('RH Base')
f2_ax1.coastlines('50m')
f2_ax1.contourf(to_np(lon), to_np(lat),ds_base.rh2[0], extend = 'both',
                 transform=crs.PlateCarree(), levels = level, cmap=cmap)

f2_ax2.set_title('RH YSU')
f2_ax2.coastlines('50m')
f2_ax2.contourf(to_np(lon), to_np(lat),ds_ysu.rh2[0], extend = 'both',
                 transform=crs.PlateCarree(), levels = level, cmap=cmap)

cmap = cm.coolwarm
level = np.arange(-10,10,1)

f2_ax3.set_title('RH Base-YSU')
f2_ax3.coastlines('50m')
f2_ax3.contourf(to_np(lon), to_np(lat),ds_base.rh2[0]- ds_ysu.rh2[0], extend = 'both',
                 transform=crs.PlateCarree(), levels = level, cmap=cmap)


cmap = cm.RdYlBu_r
level = np.arange(-20,20,1)


f2_ax4.set_title('Temp Base')
f2_ax4.coastlines('50m')
f2_ax4.contourf(to_np(lon), to_np(lat),ds_base.T2[0]-273.15, extend = 'both',
                 transform=crs.PlateCarree(), levels = level, cmap=cmap)

f2_ax5.set_title('Temp YSU')
f2_ax5.coastlines('50m')
f2_ax5.contourf(to_np(lon), to_np(lat),ds_ysu.T2[0]-273.15, extend = 'both',
                 transform=crs.PlateCarree(), levels = level, cmap=cmap)

cmap = cm.coolwarm
level = np.arange(-2,2,0.1)
f2_ax6.set_title('Temp Base-YSU')
f2_ax6.coastlines('50m')
f2_ax6.contourf(to_np(lon), to_np(lat),ds_base.T2[0]- ds_ysu.T2[0], extend = 'both',
                 transform=crs.PlateCarree(), levels = level, cmap=cmap)


plt.show()
