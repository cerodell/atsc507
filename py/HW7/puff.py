# %% [markdown]
# # HW 7
# ## ATSC 707
# ##### Christopher Rodell 




# %%
import context
import numpy as np
from cr507.utils import plt_set
import matplotlib.pyplot as plt
from collections import namedtuple 
from puff_funs import Approximator




# %% [markdown]
# A 1-D pollutant puff "anomaly" is being advected in
# the x-direction by a constant wind u. The "anomaly" includes positive
# and negative concentration deviations about a mean concentration.
# $$
# \\
# $$
# $$
# \frac{\partial P}{\partial t}= -u_{0} \frac{\partial P}{\partial x}
# $$
# $$
# \\
# $$
#  The 3 finite-difference schemes you will compare are
# - (a) FTBS - Forward in time, Backward in space;
# $$
# P_{j, n+1}=P_{j, n} -u_{0} \frac{P_{j,n}-P_{j-1,n}}{ \Delta x} \Delta t
# $$
# - (b) RK3 - Runga-Kutte 3rd order, and
# - (c) PPM - Piecewise Parabolic Method 
# where PPM is the scheme used to advect pollutants in the CMAQ model.


# %%

## Create the grid and initial conditions
initialVals={'gridx': 1000 , 'dx':100.  ,'dt':10. , 'u0': 5. , \
     'xx': np.arange(0,1000,1) , 'cmax': 10. }

## Call on approximator class
coeff = Approximator(initialVals)



# %% [markdown]
# - 1) Calculate and display the Courant number.  You can display it in the
# graph in the question (3) if you would like.
# $$
# \\
# $$
# $$
# C=\frac{u \Delta t}{\Delta x} \leq C_{\max }
# $$
# %%
print("Courant number  ", coeff.cr)

# %% [markdown]
# - 2) (a) Create initial concentration anomaly distribution in the x-direction
#    *See def__init__() in Approximator class*
# $$ 
# \\
# $$
# - (b) Plot (using blue colour) the initial concentration distribution on a graph.
# %%

## Plot With initial concentration in blue
# plot = coeff.plot_functions('Initial')


# %% [markdown]
# 3) Also, on the same plot, show (in red) the ideal exact final solution,
# after the puff anomaly has been advected downwind, as given by
#    *See def__init__() in Approximator class*

# %%
## Plot With final concentration in red
# plot = coeff.plot_functions('Final')


# %% [markdown]
# 4) Advect the concentration puff anomaly for the following number of time steps
# and plot (in green) the resulting concentration on the same graph, using
# $$
# \\
# $$
# - RK3 centered in space
# $$
# P_{i,n}^{*}=P_{i, n}+\frac{\Delta t}{3}\left[-u_{0} \frac{P_{i+1, n}-P_{i-1, n}}{2\Delta x}\right]
# $$
# $$
# P_{i,n}^{**}=P_{i, n}+\frac{\Delta t}{2}\left[-u_{0} \frac{P_{i+1, n}^{*}-P_{i-1, n}^{*}}{2\Delta x}\right]
# $$
# $$
# P_{i,n+1}=P_{i, n}+\Delta t\left[-u_{0} \frac{P_{i+1, n}^{**}-P_{i-1, n}^{**}}{2\Delta x}\right]
# $$

# %%

## Plot RK3 centered in space solution
plot = coeff.plot_functions('FTBS')

# %%

## Plot RK3 centered in space solution
plot = coeff.plot_functions('RK3')



# %%
