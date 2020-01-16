# %% [markdown]


# %%
import context
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors 
from cr507.utils import plt_set
from mpl_toolkits.axes_grid1 import make_axes_locatable

# %%

## Constants
a = 0.0293 ## 0.0293 km/K


## Set delta x and z
dx, dz = (20., 1.)

## Set range in x and z
x = np.arange(0, 1000, dx)
z = np.arange(0, 30, dz)

## create 2D array (domain) of x and z
xx, zz = np.meshgrid(x, z)

## create mnt range on surface of domain
z_si = 1 + np.cos(2.*(3.14159)*(x-500.) / 500.)
## apply condtion for mnt location
z_ground = np.where((250 < x) & (x < 750), z_si, 0 )

# %% [markdown]



# %%

## Solve for temperature across domain 
T_trop = (40 - 0.08 * xx) - 6.5*zz  ## Within hypotehtical troposphere
T_iso = (40 - 0.08 * xx) - 6.5*12   ## Above hypotehtical troposphere (isothermal)

## Apply condition to set temps above "tropopause" to be isothermal
T = np.where(zz < 12, T_trop, T_iso)
## Convert to Kelvin for later calcualtions
T = T + 273.15
T = np.vstack((T, T[-1,:]))



# %% [markdown]



# %%
## Solve for pressure across the surface (x) of the domain (ie z = 0)
P_1 = 95 + 0.01 * x

def pressure(P_1,T):
    P_2 = P_1 * np.exp((-dz)/(a*T))
    return P_2

P_list, T_avg = [], []
for i in range(len(z)):
    P_list.append(P_1)
    T_avg_i = (T[i,:]+T[i+1,:])/2.
    T_avg.append(T_avg_i)
    # zz = np.vstack((zz,zz[-1,:]))
    P_2 = pressure(P_1,T_avg_i)
    P_1 = P_2




T_avg = np.stack(T_avg)
P_final = np.stack(P_list)

# %% [markdown]


# %%
%matplotlib



## Set up Figure for plotting multiple variable on one graph
fig, ax = plt.subplots(1,1, figsize=(10,5))
fig.suptitle('Eta something...', fontsize= plt_set.title_size, fontweight="bold")
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.05)

def confil(var):
    """ 
    This funstion set up the extent for you color bar
    """
    v = np.linspace(0,105,56)
    Cnorm = colors.Normalize(vmin= np.min(var), vmax =np.max(var))
    return v, Cnorm

## Plot mnt
ax.fill_between(x,0, z_ground, color = 'saddlebrown', zorder = 4)

## Plot isobars
v_line = [2,5,10,20,30,40,50,60,70,80,90,100]
CS = ax.contour(xx, zz, P_final, levels = v_line, colors = 'black', zorder = 10)
ax.clabel(CS, fmt = '%2.1d', colors = 'k', fontsize=14) #contour line labels

## contour pressure feild
v, Cnorm = confil(P_final)
C = ax.contourf(xx, zz, P_final, cmap = 'coolwarm', norm = Cnorm, levels = v, zorder = 1)
clb = plt.colorbar(C,cax=cax, extend='both')
clb.set_label('Pressure kPa', fontsize = plt_set.label)
clb.ax.tick_params(labelsize= plt_set.tick_size) 
clb.set_alpha(.95)
clb.draw_all()



# divider = make_axes_locatable(ax)
# cax = divider.append_axes("right", size="5%", pad=0.05)
# C = ax.contourf(xx, zz, T, cmap = 'coolwarm', norm = Cnorm, levels = v)
# clb = plt.colorbar(C,cax=cax, extend='both')
# clb.set_label('Pressure kPa', fontsize = plt_set.label)
# clb.ax.tick_params(labelsize= plt_set.tick_size) 
# clb.set_alpha(.95)
# clb.draw_all()

#ax.set_xlabel("Wind Speed $(ms^-1)$", fontsize= plt_set.label)
#ax.set_ylabel("Height Above Ground Level  \n (AGL)", fontsize= plt_set.label)
#ax.tick_params(axis='both', which='major', labelsize= plt_set.tick_size)
#ax.xaxis.grid(color='gray', linestyle='dashed')
#ax.yaxis.grid(color='gray', linestyle='dashed')
#ax.set_facecolor('lightgrey')
#ax.legend(loc='best')
   


# %% [markdown]

# Solve for Surface Pressure at gorund level


# %%



P_2 = P_final[0,:] * np.exp((zz[0,:]-z_ground)/(a*T_avg[0,:]))

values = {'x(km)': x, 'Zground(km)': z_ground, 'Psfc(kPa)':P_2}

pd = pd.DataFrame(values, columns = ['x(km)', 'Zground(km)', 'Psfc(kPa)'])

pd

# %% [markdown]

# Solve for Eta using the equations from WRFv4 Tech Notes





# %%

# P_d = B(eta)(P_surf-P_top) + (eta-B(eta))8(P_0 - P-top) + P_top










