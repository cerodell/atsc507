# %% [markdown]

# # Homework 4
# ## ATSC 507
# ### Christopher Rodell


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
# &T^{*}=T_{n}+\frac{\Delta t}{2} \ f\left(T_{n}, t_{n}, \cdots\right)\\
# &T_{n+1}=T_{n}+\Delta t \ f\left(T^{*}, t_{n}+\frac{\Delta t}{2} \ , \ldots .\right)
# \end{aligned}
# $$
# $$
# \\
# $$
#
# - c\) Runge–Kutta 3rd order
# $$
# \begin{array}{l}
# {T^{*}=T_{n}+\frac{\Delta t}{3} \ f(T_{n} \ , t_{n} \ , x_{n})} \\
# {T^{* *}=T_{n}+\frac{\Delta t}{2} \ f\left(T^{*}, t_{n}+\frac{\Delta t}{3}\right)} \\
# {T_{n+1}=T_{n}+\Delta t\left(T^{**}, \quad t_{n} + \frac{\Delta t}{2}, \cdots\right)}
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
# {k_{2}=f\left(T_{n}+\frac{1}{2} \Delta t \ k_{1}, \ x_{n} \ , \ t_{n}+\frac{1}{2} \Delta t\right)} \\
# {k_{3}=f\left(T_{n}+\frac{1}{2} \Delta t \ k_{2}, \ x_{n} \ , \ t_{n}+\frac{1}{2} \Delta t\right)} \\
# {k_{4}=f\left(T_{n} + \Delta t \ k_{3} \ , \ x_{n} \ , \ t_{n}+\Delta t\right)} \\
# {T_{n+1}=T_{n}+\frac{\Delta t}{6} \ \left(k_{1}+2 k_{2}+2 k_{3}+k_{4}\right)}
# \end{array}
# $$
# $$
# \\
# $$
# - e\) Which one gave an answer closest to the actual analytical answer
#  as given by the function above?   (Note: do NOT use the 1-D model 
# from the previous HW for this.)
# $$
# \\
# $$
# **Runge–Kutta 3rd order gave the best approximation and was closest to the analytical solution.**
# %%
import context
import numpy as np
from collections import namedtuple 


class Approximator:

    def __init__(self, valueDict):
        self.__dict__.update(valueDict)

    def solution(self):
        T = self.A * ((self.c * self.m * self.dt) \
             + self.Tref - self.Tn) * (self.Tn - (self.c * self.m * self.dt))
        return T


    # function slope
    def TempFun(self):
        f = 1.5 * ( 2 - 1.5 * self.t - (self.Tn / (2 - (1.5 * self.t))))
        return f

    ## Euler forward
    def eulerf(self):
        T = self.TempFun() * self.dt + self.Tn
        return T

    ## Runge–Kutta 2nd order (mid-point)
    def rk2(self): 
        Tn = self.Tn
        t = self.t

        T_str = Tn + (self.dt/2) * self.TempFun()

        self.Tn = T_str
        self.t  = (t + (self.dt/2))
        T  = Tn + self.dt * self.TempFun()

        self.Tn = Tn
        self.t  = t
        return round(T, 4)

    ## Runge–Kutta 3rd order 
    def rk3(self): 
        Tn = self.Tn
        t = self.t

        T_str = self.Tn + (self.dt/3) * self.TempFun()

        self.Tn = T_str
        self.t  = (t + (self.dt/3))
        T_str_str  = Tn + (self.dt/2) * self.TempFun()

        self.Tn = T_str_str
        self.t  = (t + (self.dt/2))
        T  = Tn + self.dt * self.TempFun()

        self.Tn = Tn
        self.t  = t
        return round(T, 4)


    ## Runge–Kutta 4th order 
    def rk4(self): 
        Tn = self.Tn
        t = self.t

        k1 = self.TempFun()

        self.Tn = (Tn + (self.dt/2)*k1)
        self.t  = (t + (self.dt/2))
        k2 = self.TempFun()

        self.Tn = (Tn + (self.dt/2)*k2)
        self.t  = (t + (self.dt/2))
        k3 = self.TempFun()

        self.Tn = (Tn + self.dt*k3)
        self.t  = (t + (self.dt))
        k4 = self.TempFun()

        T = Tn + (self.dt/6) * (k1 + (2 * k2) + (2 * k3) + k4)

        self.Tn = Tn
        self.t  = t
        return round(T, 4)




# %%

initialVals={'Tn': 2. , 't':0. , 'm':1. ,'dt':1. , 'A': 1. , 'Tref': 3. , 'c': 1.5 }
intVals= Approximator(initialVals)

T_dict = {}

T_dict.update({"Analytic Solution": intVals.solution()})
T_dict.update({"Euler Forward": intVals.eulerf()})
T_dict.update({"Runge–Kutta 2nd order": intVals.rk2()})
T_dict.update({"Runge–Kutta 3rd order": intVals.rk3()})
T_dict.update({"Runge–Kutta 4th order": intVals.rk4()})


print(T_dict)


