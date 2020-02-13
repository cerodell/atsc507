# %% [markdown]

# # Homework 3
# ## ATSC 507
# ### Christopher Rodel

# %%
import context
import numpy as np
import pandas as pd
from context import data_dir
import matplotlib.pyplot as plt
import matplotlib.colors as colors 
from labellines import labelLine, labelLines
from cr507.utils import plt_set

## Set path to data
filein = str(data_dir) + '/n_hem.csv'

## Read data
df = pd.read_csv(filein)

## Make 1D arrays of lat and lon
lat = np.array(df['lat_degr'])
lon = np.array(df['lon_degr'])




# %% [markdown]
# - 1\) Then everyone use these files to create two maps, similar to the maps
# in the solved example on page 748 Stull 2017 Practical Meteorology.  
# Namely, one map is a plot of the coastlines on a lat/lon grid, and the
# other is a plot of the coastlines on a polar stereographic grid using 
# 60°N as the reference latitude.
# $$
# \\
# $$
# *We will make use of the following equation to apply the cordinate transform.*
# $$
# \\
# $$
# $$
# x=r \cdot \cos (\lambda) \quad, \quad y=r \cdot \sin (\lambda)
# $$
# $$
# \\
# $$
# $$
# r=L \cdot \tan \left[0.5 \cdot\left(90^{\circ}-\phi\right)\right], L=R_{o} \cdot\left[1+\sin \left(\phi_{\mathrm{o}}\right)\right]
# $$
# %%
""" ####################################################################### """
""" ############################# Make Plots ############################## """
%matplotlib

## Set up Figure for plotting multiple variable on one graph
fig, ax = plt.subplots(1,1, figsize=(12,6))
fig.suptitle('North America Mercador?', fontsize= plt_set.title_size, fontweight="bold")
ax.plot(lon, lat)





# %%

## define constants
Ro = 6371   # Units: km
phio = 60   # Units: deg

## convert deg to rad
DtoR = (np.pi/180)

## APply cordinate stransform to Polar Stereographic
L = Ro * (1 + np.sin(phio * DtoR)) 
r = L * np.tan(0.5*((90 - lat) * DtoR)) 

x = r * np.cos(lon * DtoR)
y = r * np.sin(lon * DtoR)

## Make plot of Polar Stereographic projection
fig, ax = plt.subplots(1,1, figsize=(10,10))
fig.suptitle('North America Polar Stereographic', fontsize= plt_set.title_size, fontweight="bold")
ax.plot(x, y)
ax.set_xlabel('x km', fontsize = plt_set.label)
ax.set_ylabel('y km', fontsize = plt_set.label)





# %% [markdown]

# - 2\) On page 748 Stull 2017 Practical Meteorology, 
# in the INFO box, is eq. (F20.2), which gives an 
# expression for "r".  This looks different than the 
# expression I gave in class.  Start with the eq for "r" 
# that Stull wrote on the blackboard during class, and 
# show how you can manipulate that equation to get eq (F20.2). 

# %%
