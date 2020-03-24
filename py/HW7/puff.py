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
# P_{j, n+1}=P_{j, n} -u_{0} \frac{P_{j,n}-P_{j-1,n}}{2 \Delta x} \Delta t
# $$
# - (b) RK3 - Runga-Kutte 3rd order, and
# - (c) PPM - Piecewise Parabolic Method 
# where PPM is the scheme used to advect pollutants in the CMAQ model.


# %%

# # Create the grid and initial conditions
# gridx = 1000             # number of grid points in x-direction
# dx    = 100.             # horizontal grid spacing (m)
# dt    = 10.              # time increment (s)
# u     = 5.               # horizontal wind speed (m/s)
# xx    = np.arange(0,gridx,1)

initialVals={'gridx': 1000 , 'dx':100.  ,'dt':10. , 'u0': 5. , \
     'xx': np.arange(0,1000,1) , 'cmax': 10. }


# def finite_diff(xx, cons, cideal):
#     fig, ax = plt.subplots(1,1, figsize=(12,4))
#     fig.suptitle('Puff HW7', fontsize= plt_set.title_size, fontweight="bold")
#     ax.plot(xx,conc, color = 'blue', label = "Initial concentration")
#     ax.plot(xx,cideal, color = 'red', label = " Final Ideal")
#     ax.set_xlabel('Grid Index (i)', fontsize = plt_set.label)
#     ax.set_ylabel('Quantity', fontsize = plt_set.label)
#     ax.xaxis.grid(color='gray', linestyle='dashed')
#     ax.yaxis.grid(color='gray', linestyle='dashed')
#     ax.set_ylim(-10,15)
#     ax.legend()
#     plt.show()
#     return

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
cr = initialVals['u0'] * initialVals['dt']/initialVals['dx']
print("Courant number  ", cr)

# %% [markdown]
# - 2) (a) Create initial concentration anomaly distribution in the x-direction
# %%

conc = np.zeros(initialVals['gridx'])                          # initial concentration of background is zero
conc[100:151] = np.linspace(0.,initialVals['cmax'],51)         # insert left side of triangle
conc[150:201] = np.linspace(initialVals['cmax'], 0.,51)        # insert right side of triangle
conc[20:41] = np.linspace(0., -0.5*initialVals['cmax'], 21)    # insert left side of triangle
conc[40:61] = np.linspace(-0.5*initialVals['cmax'], 0., 21)    # insert right side of triangle
initialVals.update({'Pj': conc})

# %% [markdown]
# - (b) Plot (using blue colour) the initial concentration distribution on a graph.
# %%

# fig, ax = plt.subplots(1,1, figsize=(12,4))
# fig.suptitle('Puff HW7', fontsize= plt_set.title_size, fontweight="bold")
# ax.plot(initialVals['xx'],initialVals['Pj'], color = 'blue', label = "Initial concentration")
# ax.set_xlabel('Grid Index (i)', fontsize = plt_set.label)
# ax.set_ylabel('Quantity', fontsize = plt_set.label)
# ax.xaxis.grid(color='gray', linestyle='dashed')
# ax.yaxis.grid(color='gray', linestyle='dashed')
# ax.set_ylim(-10,15)
# ax.legend()
# plt.show()

# %% [markdown]
# 3) Also, on the same plot, show (in red) the ideal exact final solution,
# after the puff anomaly has been advected downwind, as given by
# %%
cideal = np.zeros(initialVals['gridx'])                             # initial concentration of ideal background is zero
cideal[800:851] = np.linspace(0., initialVals['cmax'],51)           # insert left side of triangle
cideal[850:901]  = np.linspace(initialVals['cmax'], 0., 51)         # insert right side of triangle
cideal[720:741]  = np.linspace(0., -0.5*initialVals['cmax'], 21)    # insert left side of triangle
cideal[740:761]  = np.linspace(-0.5*initialVals['cmax'], 0., 21)    # insert right side of triangle
initialVals.update({'cideal': cideal})

# fig, ax = plt.subplots(1,1, figsize=(12,4))
# fig.suptitle('Puff HW7', fontsize= plt_set.title_size, fontweight="bold")
# ax.plot(initialVals['xx'],initialVals['Pj'], color = 'blue', label = "Initial concentration", zorder = 10)
# ax.plot(initialVals['xx'],initialVals['cideal'], color = 'red', label = "Final Ideal", zorder = 8)
# ax.set_xlabel('Grid Index (i)', fontsize = plt_set.label)
# ax.set_ylabel('Quantity', fontsize = plt_set.label)
# ax.xaxis.grid(color='gray', linestyle='dashed')
# ax.yaxis.grid(color='gray', linestyle='dashed')
# ax.set_ylim(-10,15)
# ax.legend()
# plt.show()

# %% [markdown]
# 4) Advect the concentration puff anomaly for the following number of time steps
# and plot (in green) the resulting concentration on the same graph, using ...
# %%

nsteps = (initialVals['gridx'] - 300) / (initialVals['u0'] * initialVals['dt'] / initialVals['dx'])
nsteps = np.arange(0,nsteps)

# nsteps = np.pad(nsteps,(1,1), 'edge')
initialVals.update({'nsteps': nsteps})
# fun = np.stack(conc,nsteps)
# initialVals.update({'fun': fun})


# print(nsteps)


coeff = Approximator(initialVals)


pnew=coeff.rk3()
# print(pnew.T.shape)

# plt.plot(pnew.T[:,-1])

fig, ax = plt.subplots(1,1, figsize=(12,4))
fig.suptitle('Puff HW7', fontsize= plt_set.title_size, fontweight="bold")
ax.plot(initialVals['xx'],initialVals['Pj'], color = 'blue', label = "Initial concentration", zorder = 9)
ax.plot(initialVals['xx'],initialVals['cideal'], color = 'red', label = "Final Ideal", zorder = 8)
ax.plot(initialVals['xx'],pnew.T[:,-1], color = 'green', label = "RK3", zorder = 10)
ax.set_xlabel('Grid Index (i)', fontsize = plt_set.label)
ax.set_ylabel('Quantity', fontsize = plt_set.label)
ax.xaxis.grid(color='gray', linestyle='dashed')
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.set_ylim(-10,15)
ax.legend()
plt.show()


# # PF=[]
# P = coeff.Pj
# PF.append(coeff.Pj)
# for i in np.arange(1,nsteps):
#     pnew=coeff.rk3()
#     PF.append(pnew)
#     # ynew=midpointinter41(coeff,y,timeVec[i-1])
#     # ym.append(ynew)
#     # y=ynew





# %%
