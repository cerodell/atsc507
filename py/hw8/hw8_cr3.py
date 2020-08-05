# %% [markdown]
# ## Homework 8  Finite Volume
# ### ATSC 507
# #### Christopher Rodell 

# %% [markdown]
# ### Question 1
# $$
# \begin{array}{l}\text {(/5) Show that } T_{i} \text { (i.e. } T(x) \text { at the centroid of control-volume } \mathrm{CV}_{i} \text { ) and } \bar{T}_{i} \text { (i.e. the control- } \\ \text { volume averaged value of } T(x) \text { in } \mathrm{CV}_{i} \text { ) are the same only to second-order accuracy. } \\ \text { Hint } 1: \text { Try expanding } \bar{T}_{i} \text { at } x=x_{i} \\ \text { Hint } 2: x_{i}=\frac{x_{i+\frac{1}{2}}+x_{i-\frac{1}{2}}}{2}\end{array}
# $$
# $$
# \\
# $$
# $$
# \begin{aligned}
# T_{i} &= \frac{1}{\Delta x} \int_{i-1 / 2}^{i+1 / 2} T d x  \\  &= \frac{1}{\Delta x} \int_{i-1 / 2}^{i+1 / 2}\left[T_{i}+\left.\frac{d T}{d x}\right|_{i}\left(x-x_{i}\right)\right.\\
# &+\left.\frac{d^{2} T}{d x^{2}}\right|_{i} \frac{\left(x-x_{i}\right)^{2}}{2 !}+\left.\frac{d^{3} T}{d x^{3}}\right|_{i} \frac{\left(x-x_{i}\right)^{3}}{3 !} \biggr] d x
# \end{aligned}
# $$
# $$
# \frac{1}{\Delta x}\left\{\underbrace{\int_{i-1 / 2}^{i+1 / 2} T_{i} d x}_{1}+ \underbrace{\left.\int_{i-1 / 2}^{i+1 / 2} \frac{d T}{d x}_{1}\right|_{i}\left(x-x_{i}\right)d x}_{2} +  \underbrace{\left.\int_{i-1/2}^{i+1 / 2} \frac{d^{2} T}{dx^{2}}\right|_{i} \frac{\left(x-x_{i}\right)^{2}}{2 !} d x}_{3}+\ldots .\right\}
# $$
# ##### Integrate portions of parts 1-3 using sympy 
# %%
import context
import numpy as np
from sympy import *
from sympy.abc import x, h
from sympy import symbols, IndexedBase, Idx


expr = integrate(x, x/2)

# %% [markdown]






# %%
