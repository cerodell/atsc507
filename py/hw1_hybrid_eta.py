# %%
import context
import numpy as np
import matplotlib.pyplot as plt

## COnstants
a = 0.0293 ## 0.0293 km/K


## Set delta x and z
dx, dz = (20, 1)

## Set range in x and z
x = np.arange(0, 1000, dx)
z = np.arange(0, 30, dz)

## create 2D array (domain) of x and z
xx, zz = np.meshgrid(x, z)

## Solve for temperature across domain 
T_trop = (40 - 0.08 * xx) - 6.5*zz  ## Within hypotehtical troposphere
T_iso = (40 - 0.08 * xx) - 6.5*12   ## Above hypotehtical troposphere (isothermal)

## Apply condition to set temps above "tropopause" to be isothermal
T = np.where(zz < 12, T_trop, T_iso)
## COnvert to Kelvin for later calcualtions
T = T + 273.15

## Solve for pressure across  x on surface of domain (z = 0)
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
