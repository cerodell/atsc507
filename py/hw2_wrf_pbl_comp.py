# %%
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
from cr507.utils import plt_set
from mpl_toolkits.axes_grid1 import make_axes_locatable

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

# %%
""" ####################################################################### """
""" ############################# Make Plots ############################## """
%matplotlib

for i in range(0,24,6):
    theTime = np.array2string(ds_base.Time[i])
    theTime = theTime[1:-14]
    print(theTime)

    fig2 = plt.figure(constrained_layout=True, figsize=[14,8])
    fig2.suptitle(theTime, x = 0.2)
    spec2 = gridspec.GridSpec(ncols=3, nrows=2, figure=fig2)
    f2_ax1 = fig2.add_subplot(spec2[0, 0], projection=cord)
    f2_ax2 = fig2.add_subplot(spec2[0, 1], projection=cord)
    f2_ax3 = fig2.add_subplot(spec2[0, 2], projection=cord)
    f2_ax4 = fig2.add_subplot(spec2[1, 0], projection=cord)
    f2_ax5 = fig2.add_subplot(spec2[1, 1], projection=cord)
    f2_ax6 = fig2.add_subplot(spec2[1, 2], projection=cord)

    cmap = cm.BrBG
    level = np.arange(0,100,1)
    # norm = mpl.colors.BoundaryNorm(bounds, cmap)

    f2_ax1.set_title('RH Base')
    f2_ax1.coastlines('50m')
    C1 = f2_ax1.contourf(to_np(lon), to_np(lat),ds_base.rh2[i], extend = 'both',
                    transform=crs.PlateCarree(), levels = level, cmap=cmap)

    clb = fig2.colorbar(C1, ax= f2_ax1, fraction=0.04, pad=0.02)
    clb.set_label("$RH$", fontsize = 8)
    clb.ax.tick_params(labelsize= 8) 

    f2_ax2.set_title('RH YSU')
    f2_ax2.coastlines('50m')
    C2= f2_ax2.contourf(to_np(lon), to_np(lat),ds_ysu.rh2[i], extend = 'both',
                    transform=crs.PlateCarree(), levels = level, cmap=cmap)

    clb = fig2.colorbar(C2, ax = f2_ax2, fraction=0.04, pad=0.02)
    clb.set_label("$RH$", fontsize = 8)
    clb.ax.tick_params(labelsize= 8) 
    # clb.set_alpha(.95)
    # clb.draw_all()

    cmap = cm.coolwarm
    level = np.arange(-20,20,1)

    f2_ax3.set_title('RH Diff(YSU- Base)')
    f2_ax3.coastlines('50m')
    C3 = f2_ax3.contourf(to_np(lon), to_np(lat),ds_ysu.rh2[i]- ds_base.rh2[i], extend = 'both',
                    transform=crs.PlateCarree(), levels = level, cmap=cmap)
    clb = fig2.colorbar(C3, ax= f2_ax3, fraction=0.04, pad=0.02)
    clb.set_label("$\Delta RH$", fontsize = 8)
    clb.ax.tick_params(labelsize= 8) 
    # clb.set_alpha(.95)
    # clb.draw_all()

    cmap = cm.RdYlBu_r
    level = np.arange(-30,30,1)


    f2_ax4.set_title('Temp Base')
    f2_ax4.coastlines('50m')
    C4 = f2_ax4.contourf(to_np(lon), to_np(lat),ds_base.T2[i]-273.15, extend = 'both',
                    transform=crs.PlateCarree(), levels = level, cmap=cmap)

    clb = fig2.colorbar(C4, ax= f2_ax4, fraction=0.04, pad=0.02)
    clb.set_label("$Temp Deg C$", fontsize = 8)
    clb.ax.tick_params(labelsize= 8) 

    f2_ax5.set_title('Temp YSU')
    f2_ax5.coastlines('50m')
    C5 = f2_ax5.contourf(to_np(lon), to_np(lat),ds_ysu.T2[i]-273.15, extend = 'both',
                    transform=crs.PlateCarree(), levels = level, cmap=cmap)

    clb = fig2.colorbar(C5, ax = f2_ax5, fraction=0.04, pad=0.02)
    clb.set_label("$Temp C$", fontsize = 8)
    clb.ax.tick_params(labelsize= 8) 
    # clb.set_alpha(.95)
    # clb.draw_all()

    cmap = cm.coolwarm
    level = np.arange(-5,5,0.1)
    f2_ax6.set_title('Temp Diff(YSU-Base)')
    f2_ax6.coastlines('50m')
    C6 = f2_ax6.contourf(to_np(lon), to_np(lat), ds_ysu.T2[i] - ds_base.T2[i], extend = 'both',
                    transform=crs.PlateCarree(), levels = level, cmap=cmap)

    # divider = make_axes_locatable(f2_ax6)
    # cax = divider.append_axes("right", size="5%", pad=0.05)
    clb = fig2.colorbar(C6, ax = f2_ax6, fraction=0.04, pad=0.02)
    clb.set_label("$\Delta T$", fontsize = 8)
    clb.ax.tick_params(labelsize= 8) 
    # clb.set_alpha(.95)
    # clb.draw_all()
    # fig2.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    fig2.savefig('/Users/crodell/atsc507/py/Images/fig_rh_temp_'+str(theTime))



# %%

for i in range(0,24,6):
# i = 0
    theTime = np.array2string(ds_base.Time[i])
    theTime = theTime[1:-14]
    print(theTime)

    fig2 = plt.figure(constrained_layout=True, figsize=[14,8])
    fig2.suptitle(theTime, x = 0.2)
    spec2 = gridspec.GridSpec(ncols=3, nrows=2, figure=fig2)
    f2_ax1 = fig2.add_subplot(spec2[0, 0], projection=cord)
    f2_ax2 = fig2.add_subplot(spec2[0, 1], projection=cord)
    f2_ax3 = fig2.add_subplot(spec2[0, 2], projection=cord)
    f2_ax4 = fig2.add_subplot(spec2[1, 0], projection=cord)
    f2_ax5 = fig2.add_subplot(spec2[1, 1], projection=cord)
    f2_ax6 = fig2.add_subplot(spec2[1, 2], projection=cord)

    cmap = cm.BrBG
    level = np.arange(960,1050,0.5)
    v_line = np.arange(960,1050,5)

    f2_ax1.set_title('MSLP Base')
    f2_ax1.coastlines('50m')
    C = f2_ax1.contourf(to_np(lon), to_np(lat),(ds_base.slp[i]), extend = 'both',
                    transform=crs.PlateCarree(), levels = level, cmap=cmap)
    CS = f2_ax1.contour(to_np(lon), to_np(lat),(ds_base.slp[i]),
                    transform=crs.PlateCarree(), levels = v_line, colors = 'k', linewidths = 0.5)
    f2_ax1.clabel(CS, fmt = '%2.2d', colors = 'k', fontsize=4) #contour line labels

    clb = fig2.colorbar(C, ax= f2_ax1, fraction=0.04, pad=0.02)
    clb.set_label("$Pressure hPa$", fontsize = 8)
    clb.ax.tick_params(labelsize= 8) 

    f2_ax2.set_title('MSLP YSU')
    f2_ax2.coastlines('50m')
    C= f2_ax2.contourf(to_np(lon), to_np(lat),(ds_ysu.slp[i]), extend = 'both',
                    transform=crs.PlateCarree(), levels = level, cmap=cmap)
    CS = f2_ax2.contour(to_np(lon), to_np(lat),(ds_ysu.slp[i]),
                    transform=crs.PlateCarree(), levels = v_line, colors = 'k', linewidths = 0.5)
    f2_ax2.clabel(CS, fmt = '%2.2d', colors = 'k', fontsize=4) #contour line labels

    clb = fig2.colorbar(C, ax = f2_ax2, fraction=0.04, pad=0.02)
    clb.set_label("$Pressure hPa$", fontsize = 8)
    clb.ax.tick_params(labelsize= 8) 

    cmap = cm.coolwarm
    level = np.arange(-3,3,0.1)
    v_line = np.arange(-3,3,0.8)
    f2_ax3.set_title('MSLP Diff(YSU-Base)')
    f2_ax3.coastlines('50m')
    C = f2_ax3.contourf(to_np(lon), to_np(lat),((ds_ysu.slp[i]- ds_base.slp[i])), extend = 'both',
                    transform=crs.PlateCarree(), levels = level, cmap=cmap)
    CS = f2_ax3.contour(to_np(lon), to_np(lat),((ds_ysu.slp[i]- ds_base.slp[i])),
                    transform=crs.PlateCarree(), levels = v_line, colors = 'k', linewidths = 0.5)
    f2_ax3.clabel(CS, fmt = '%1.1d', colors = 'k', fontsize=4) #contour line labels

    clb = fig2.colorbar(C, ax= f2_ax3, fraction=0.04, pad=0.02)
    clb.set_label("$\Delta hPa $", fontsize = 8)
    clb.ax.tick_params(labelsize= 8) 


    cmap = cm.jet
    level = np.arange(0,30,1)

    base_u = ds_base.uvmet10_wspd_wdir[i][0]* np.cos(np.deg2rad(ds_base.uvmet10_wspd_wdir[i][1]))
    base_v = ds_base.uvmet10_wspd_wdir[i][0]* np.sin(np.deg2rad(ds_base.uvmet10_wspd_wdir[i][1]))

    ysu_u = ds_ysu.uvmet10_wspd_wdir[i][0]* np.cos(np.deg2rad(ds_ysu.uvmet10_wspd_wdir[i][1]))
    ysu_v = ds_ysu.uvmet10_wspd_wdir[i][0]* np.sin(np.deg2rad(ds_ysu.uvmet10_wspd_wdir[i][1]))




    f2_ax4.set_title('Hourly Wind Speed Base')
    f2_ax4.coastlines('50m')
    C4 = f2_ax4.contourf(to_np(lon), to_np(lat),ds_base.uvmet10_wspd_wdir[i][0], extend = 'both',
                    transform=crs.PlateCarree(), levels = level, cmap=cmap)

    f2_ax4.quiver(np.array(lon[0::4,0::4]), np.array(lat[0::4,0::4]), np.array(base_u[0::4,0::4]),\
        np.array(base_v[0::4,0::4]), pivot='middle', transform=crs.PlateCarree(), lw = 0.5)

    clb = fig2.colorbar(C4, ax= f2_ax4, fraction=0.04, pad=0.02)
    clb.set_label("$Wind Speed (ms^-1)$", fontsize = 8)
    clb.ax.tick_params(labelsize= 8) 

    f2_ax5.set_title('Hourly Wind Speed YSU')
    f2_ax5.coastlines('50m')
    C5 = f2_ax5.contourf(to_np(lon), to_np(lat),ds_ysu.uvmet10_wspd_wdir[i][0], extend = 'both',
                    transform=crs.PlateCarree(), levels = level, cmap=cmap)

    f2_ax5.quiver(np.array(lon[0::4,0::4]), np.array(lat[0::4,0::4]), np.array(ysu_u[0::4,0::4]),\
        np.array(ysu_v[0::4,0::4]), pivot='middle', transform=crs.PlateCarree(), lw = 0.5)

    clb = fig2.colorbar(C5, ax = f2_ax5, fraction=0.04, pad=0.02)
    clb.set_label("$Wind Speed (ms^-1)$", fontsize = 8)
    clb.ax.tick_params(labelsize= 8) 


    cmap = cm.coolwarm
    level = np.arange(-5,5,0.1)
    f2_ax6.set_title('Wind Speed Diff(YSU-Base)')
    f2_ax6.coastlines('50m')
    C6 = f2_ax6.contourf(to_np(lon), to_np(lat),ds_ysu.uvmet10_wspd_wdir[i][0]-ds_base.uvmet10_wspd_wdir[i][0], extend = 'both',
                    transform=crs.PlateCarree(), levels = level, cmap=cmap)

    clb = fig2.colorbar(C6, ax = f2_ax6, fraction=0.04, pad=0.02)
    clb.set_label("$\Delta Wind Speed (ms^-1)$", fontsize = 8)
    clb.ax.tick_params(labelsize= 8) 
    fig2.savefig('/Users/crodell/atsc507/py/Images/fig_wspd_pressure_'+str(theTime))



# %%
