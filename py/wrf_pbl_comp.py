"""
Created on Sat Jan 31st 2020 

@author: rodell
"""
import context
import numpy as np
import xarray as xr
from datetime import datetime
from pathlib import Path
from context import data_dir
from netCDF4 import Dataset

import matplotlib.pyplot as plt
from cr507.utils.read_wrf import readwrf
from matplotlib.dates import DateFormatter

from wrf import (to_np, getvar, g_uvmet, ll_to_xy)

""" ####################################################################### """
""" ###################### Grab WRF Variables ####################### """


wrf_base = str(data_dir) + str('/wrf_data/wrf_base/')

wrf_ysu  = str(data_dir) + str('/wrf_data/wrf_ysu/')

ds_base = readwrf(wrf_base)
ds_ysu  = readwrf(wrf_ysu)




""" ####################################################################### """
""" ############ Mathematical Constants and Usefull Arrays ################ """
# ######Math Constants
# e = math.e
# ln_ = np.log
# length = len(temp)  ##nice for looping below

# e_full    = np.full(shape,e, dtype=float)
# zero_full = np.zeros(shape, dtype=float)

# ######Initial FFMC Values
# F_o      = 85.0   #Previous day's F becomes F_o
# F_o_full = np.full(shape,F_o, dtype=float)


# "############################# Make Plots #############################"

# fig, ax = plt.subplots(4,1, figsize=(14,10))
# fig.suptitle('Baldy \n Fire Lookout Tower', fontsize=16)
# fig.subplots_adjust(hspace=0.18)

# ax[0].plot(utc,ffmc, color = 'black')
# ax[0].set_ylim(74,101)  
# #ax[0].set_xlabel("Datetime (PDT)", fontsize = ylabel)
# ax[0].set_ylabel("FFMC", fontsize = label)
# ax[0].xaxis.grid(color='gray', linestyle='dashed')
# ax[0].yaxis.grid(color='gray', linestyle='dashed')
# ax[0].tick_params(axis='both', which='major', labelsize=tick_size)
# ax[0].set_facecolor('lightgrey')
# ax[0].set_xticklabels([])


# ax[1].plot(utc, temp, color = 'red')
# ax[1].set_ylim(0,30)  
# #ax[0].set_xlabel("Datetime (PDT)", fontsize = ylabel)
# ax[1].set_ylabel("Temp (\N{DEGREE SIGN}C)", fontsize = label)
# ax[1].xaxis.grid(color='gray', linestyle='dashed')
# ax[1].yaxis.grid(color='gray', linestyle='dashed')
# ax[1].tick_params(axis='both', which='major', labelsize=tick_size)
# ax[1].set_facecolor('lightgrey')
# ax[1].set_xticklabels([])
# #chartBox = ax[0].get_position()
# #ax[0].legend(loc='upper center', bbox_to_anchor=(1.06,0.95), shadow=True, ncol=1)


# ax[2].plot(utc, rh, color = 'green')  
# ax[2].set_ylim(0,100)
# #ax[2].set_xlabel("Datetime (UTC)", fontsize = label)
# ax[2].set_ylabel("RH (%)", fontsize = label)
# ax[2].xaxis.grid(color='gray', linestyle='dashed')
# ax[2].yaxis.grid(color='gray', linestyle='dashed')
# ax[2].tick_params(axis='both', which='major', labelsize=tick_size)
# ax[2].set_facecolor('lightgrey')
# ax[2].set_xticklabels([])


# ax[3].plot(utc, wsp, color = 'blue')
# ax[3].set_ylim(0,40)  
# ax[3].set_xlabels_top = False
# ax[3].set_xlabel("Datetime (PDT)", fontsize = label)
# ax[3].set_ylabel("Wsp (km/hr)", fontsize = label)
# ax[3].xaxis.grid(color='gray', linestyle='dashed')
# ax[3].yaxis.grid(color='gray', linestyle='dashed')
# ax[3].tick_params(axis='both', which='major', labelsize=tick_size)
# ax[3].set_facecolor('lightgrey') 
# ax[3].set_xticklabels([])
# ax[3].tick_params(axis='x', rotation=30)
# xfmt = DateFormatter('%m-%d %H:%M')
# ax[3].xaxis.set_major_formatter(xfmt)
 
#ax[4].plot(utc, wdir, color ="blue")  
#ax[4].set_ylim(0,360)
#ax[4].set_xlabel("Datetime (UTC)", fontsize = label)
#ax[4].set_ylabel("Wdir", fontsize = label)
#ax[4].xaxis.grid(color='gray', linestyle='dashed')
#ax[4].yaxis.grid(color='gray', linestyle='dashed')
#ax[4].tick_params(axis='both', which='major', labelsize=tick_size)
#ax[4].set_facecolor('lightgrey')
#xfmt = DateFormatter('%m-%d %H:%M')
#ax[4].tick_params(axis='x', rotation=30)
#ax[4].xaxis.set_major_formatter(xfmt)

#fig.legend(loc = (0.5, 0), ncol=5 )  
#fig.savefig(save + 'Station_vs_HOBO_Pre_Corrected')
##label = date[4:6]+"/"+date[6:8] + '/' + date[2:4] +'  ' + radar +'   ' 

#fig.savefig(save + 'Baldy_Tower')  
    
    
    
    







