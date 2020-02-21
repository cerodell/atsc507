# %% [markdown]

# # Homework 4
# ## ATSC 507
# ### Christopher Rodel


# %% [markdown]
# $$
# \\
# $$
# $$
# \mathrm{T}\left(^{\circ} \mathrm{C}\right)=\mathrm{A} \left(\mathrm{c} \ \mathrm{m} \ \Delta \mathrm{t}+\text { Tref }-\mathrm{Tref}_{-} \mathrm{o}\right) \left(\text { Tref }_{-} \mathrm{o}-\mathrm{c} \ \mathrm{m} \ \Delta \mathrm{t}\right)
# $$
# Given the above function with Tref_o = 2,  A = 1,  c = 1.5,  ∆t = 1,  and  t = m*∆t. 
# This was the basis for the worksheet that I handed out today in class 
# (the coloured curved lines in the fig below), where I used variable 
# Tref in the range of 2 to 6, and m in the range of 0 to 1. 
# Given the info above, the function that you should apply to the finite 
# difference methods (a) - (d) below is:
# $$
# \\
# $$
# $$
# \partial \mathrm{T} / \partial \mathrm{t}=\mathrm{f}(\mathrm{t}, \mathrm{T})=1.5 \ \{2-1.5 \ \mathrm{t}-[\mathrm{T} /(2-1.5 \ \mathrm{t})]\}
# $$
# $$
# \\
# $$
# *Hint: To get the eq above for f(t, T), I first solved the eq above for Tref(T, t). 
#  Then I  analytically found ∂T/∂t from the first equation above, and substituted in
#  the expression for Tref.  This takes advantage of the fact that Tref is constant 
# along any of the curves in the fig below.*


# %%
import context
import numpy as np
from collections import namedtuple 



## Initial condtions / function parameters 
Tref = 3        ## Referance temp
m = 0           ## ?
Tn = 2          ## Initial referance tmep
A = 1           ## Not sure, empirical constant?
c = 1.5         ## Not sure, empirical constant?
dt = 1     ## timestep 
# t = m*delta_t   ## time

## Analytic solution?
T_final = A * (1.5 * m * dt  + Tref - Tn) * (Tn - 1.5 *m * dt)



# # function slope
# def TempFun(m, dt, Tn):
#     """
#     Out put of slope of function at defined condtions
#     """
#     t = m * dt
#     f = 1.5 * ( 2 - 1.5 * t - (Tn / (2 - 1.5 * t)))
#     return f


# %% [markdown]
#
# Please start from initial condition of T = 2 degC as we did in class, but compute
#  the new T (degC) at 1 timestep (1∆t) ahead using:
# - a\) Euler forward
#$$
# T_{n+1}=f(T_{n}, \ t_{n}) * \Delta t + T_{n}
# $$
# $$
# \\
# $$
#
# - b\) Runge–Kutta 2nd order (mid-point)
# $$
# \begin{aligned}
# &T^{*}=T_{n}+\frac{\Delta t}{2} f\left(T_{n}, t_{n}, \cdots\right)\\
# &T_{n+1}=T_{n}+\Delta t f\left(T^{*}, t_{n}+\frac{\Delta t}{2} \ , \ldots .\right)
# \end{aligned}
# $$
# $$
# \\
# $$
#
# - c\) Runge–Kutta 3rd order
# $$
# \begin{array}{l}
# {T^{*}=T_{n}+\frac{\Delta t}{3} f(T_{n} \ , t_{n} \ , x_{n})} \\
# {T^{* *}=T_{n}+\frac{\Delta t}{2} f\left(T^{*}, t_{n}+\frac{\Delta t}{3}\right)} \\
# {T_{n+1}=T_{n}+\Delta t+\left(T^{**}, \quad t_{n} + \frac{\Delta t}{2}, \cdots\right)}
# \end{array}
# $$
# $$
# \\
# $$
#
# - d\) Runge–Kutta 4th order
# $$
# \begin{array}{l}
# {k_{1}=f(T_{n} \ , \ x_{n} \ , \ t_{n})} \\
# {k_{2}=f\left(T_{n}+\frac{1}{2} \Delta t k_{1}, \ x_{n} \ , \ t_{n}+\frac{1}{2} \Delta t\right)} \\
# {k_{3}=f\left(T_{n}+\frac{1}{2} \Delta t k_{2}, \ x_{n} \ , \ t_{n}+\frac{1}{2} \Delta t\right)} \\
# {k_{4}=f\left(T_{n} + \Delta t k_{3} \ , \ x_{n} \ , \ t_{n}+\Delta t\right)} \\
# {T_{n+1}=T_{n}+\frac{\Delta t}{6}\left(k_{1}+2 k_{2}+2 k_{3}+k_{4}\right)}
# \end{array}
# $$
# $$
# \\
# $$
# e) Which one gave an answer closest to the actual analytical answer
#  as given by the function above?   (Note: do NOT use the 1-D model 
# from the previous HW for this.)

# %%


initialVals={'Tn': 1. ,'t':0. ,'m':0. ,'dt':1.}
class Integrator:

    def __init__(self, Tn, t,m, dt):
        self.Tn = Tn
        self.t  = t
        self.m  = m
        self.dt = dt

    # function slope
    def TempFun(self, **theTime):
        """
        Out put of slope of function at defined condtions
        """
        t = self.m * self.dt
        f = 1.5 * ( 2 - 1.5 * t - (self.Tn / (2 - 1.5 * self.t)))
        return f

    ## Euler forward
    def eulerf(self):
        t = m * self.dt
        T = self.TempFun() * self.dt + self.Tn
        return T

    # ## Runge–Kutta 2nd order (mid-point)
    # def rk2(coeff): 
    #     T_str = Tn + (dt/2) * TempFun(m, dt, Tn)
    #     T  = TempFun(coeff.m, (coeff.dt + (coeff.dt/2)), coeff.Tn) * coeff.dt + coeff.Tn

    # T_dict.update({"Runge–Kutta 2nd order": rk2(coeff)})


# %%


intVals= Integrator(1. , 0. , 0. , 1.)
T_dict = {}

T_dict.update({"Euler Forward": intVals.eulerf()})


    # ## Initialize dictionary to compile dif approximation methods
    # T_dict = {}


# %%
