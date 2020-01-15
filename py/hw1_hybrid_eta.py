# %%
import context
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors 
from cr507.utils import plt_set
from mpl_toolkits.axes_grid1 import make_axes_locatable


## COnstants
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
z_surf = np.where((250 < x) & (x < 750), z_si, 0 )


## Solve for temperature across domain 
T_trop = (40 - 0.08 * xx) - 6.5*zz  ## Within hypotehtical troposphere
T_iso = (40 - 0.08 * xx) - 6.5*12   ## Above hypotehtical troposphere (isothermal)

## Apply condition to set temps above "tropopause" to be isothermal
T = np.where(zz < 12, T_trop, T_iso)
## Convert to Kelvin for later calcualtions
T = T + 273.15

## Solve for pressure across the surface (x) of the domain (ie z = 0)
P_slp = 95 + 0.01 * x

## Solve for presure at hieght applying the hypsometric equation
P = []
T_avg = np.cumsum(T, axis=0)
# P_2 = P_1 * np.exp((dz)/a*T_avg)

T_test = [sum(T[i::1,0]) for i in range(len(T))]


# def avg(x):
#     x = [i for i in x if i is not None]
#     return sum(x, 0.0) / len(x)

# filt = imap(avg, izip_longest(*T))









# %%
# %matplotlib

fig, ax = plt.subplots(1,1, figsize=(10,5))
fig.suptitle('Eta something...', fontsize= plt_set.title_size, fontweight="bold")


v = np.linspace(np.min(T),np.max(T),41)
Cnorm = colors.Normalize(vmin= np.min(T), vmax =np.max(T))

ax.fill_between(x,0, z_surf, color = 'brown', zorder = 10)

divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.05)
C = ax.contourf(xx, zz, T, cmap = 'coolwarm', norm = Cnorm, levels = v)
clb = plt.colorbar(C,cax=cax)
# clb.set_label('Relative Humidity Gradient \n(%)', fontsize =ylabel)
# clb.ax.tick_params(labelsize=tick_size) 
# clb.set_alpha(.95)
# clb.draw_all()

#ax.set_xlabel("Wind Speed $(ms^-1)$", fontsize= plt_set.label)
#ax.set_ylabel("Height Above Ground Level  \n (AGL)", fontsize= plt_set.label)
#ax.tick_params(axis='both', which='major', labelsize= plt_set.tick_size)
#ax.xaxis.grid(color='gray', linestyle='dashed')
#ax.yaxis.grid(color='gray', linestyle='dashed')
#ax.set_facecolor('lightgrey')
#ax.legend(loc='best')
   

# %%
