# %% [markdown]
# # Homework 10 Spectral
# ### ATSC 507 
# ##### Christopher Rodell 


# - 1\) Given the polynomial 
# $$
# y = 0.5*x + x*sin(\frac{2* \pi *x}{10}) \hspace{16mm} \text{for: } 0 ≤ x ≤ 20
# $$
#   - (a) plot this function
# %%
import context
import numpy as np 
import matplotlib.pyplot as plt
from cr507.utils import plt_set


x = np.arange(0.,20,0.1)
y = 0.5 * x + x * np.sin((2 *np.pi * x)/ 10)


fig, ax = plt.subplots(1,1, figsize=(10,8))
fig.suptitle('Polynomial', fontsize= plt_set.title_size, fontweight="bold")
ax.plot(x,y)
ax.set_xlabel('x', fontsize = plt_set.label)
ax.set_ylabel('y', fontsize = plt_set.label)
ax.xaxis.grid(color='gray', linestyle='dashed')
ax.yaxis.grid(color='gray', linestyle='dashed')
# ax.legend()

plt.show()

# %% [markdown]
#   - (b) analytically integrate it, to find the exact solution.
# $$
# f(x)=\int_{0}^{20} \frac{x}{2} d x+\int_{0}^{20} x \sin \left(\frac{\pi x}{5}\right) d x
# $$
# $$
# \\
# $$
# Let:
# $$
# \begin{array}{l}u=x \quad v=\frac{5}{\pi} \cos \left(\frac{\pi x}{5}\right) \\ d u=1 \quad d v=\sin \left(\frac{\pi x}{5}\right)\end{array}
# $$
# $$
# \\
# $$
# $$
# f(x)=\biggr|_{0} ^{20} \frac{x^{2}}{4}-x \frac{5}{\pi} \cos \biggr(\frac{\pi x}{5}\biggr)-\biggr(-\frac{5}{\pi}\biggr) \int_{0}^{20} \cos \biggr(\frac{\pi x}{5}\biggr) d x
# $$


# $$
# f(x)=\biggr|_{0} ^{20} \frac{x^{2}}{4}- \frac{5x}{\pi} \cos \biggr(\frac{\pi x}{5}\biggr)+ \frac{25}{\pi^{2}} \sin \biggr(\frac{\pi x}{5}\biggr)
# $$
# $$
# \\
# $$
# $$
# \\
# $$
# $$
# f(x)= f(20) - f(0)
# $$
# $$
# \begin{aligned}f(x)=\biggr[\frac{20^{2}}{4}- \frac{5*20}{\pi} \cos \biggr(\frac{\pi *20}{5}\biggr)+ \frac{25}{\pi^{2}} \sin \biggr(\frac{\pi *20}{5}\biggr)\biggr] \\ - \biggr[\frac{0^{2}}{4}- \frac{5*0}{\pi} \cos \biggr(\frac{\pi *0}{5}\biggr)+ \frac{25}{\pi^{2}} \sin \biggr(\frac{\pi *0}{5}\biggr)\biggr]\end{aligned}
# $$
#
# $$
# \boxed{f(x) = 68.169}
# $$
# %% [markdown]
# - (c) Use Gauss quadrature to numerically integrate it (using the eqs and tables in the handout,
#  not any built-in integration function) for the following number of key points (m or n=): 
#  (i) 2 ,  (ii) 4 , (iii) 6 , (iv) 8 , and discuss how Gaussian quadrature converges to the
#  exact solution.  Show your work on your spreadsheet, or matlab, or your computer program.
# I 
# $$
# \text {Use Gauss-Legendre quadrature:}
# $$
# $$
# \bar{I}=\frac{b-a}{2} \sum_{k=1}^{m} w_{k} f\left(x_{k}\right) \hspace{4mm} \text {to evaluate integral:} \hspace{4mm} I=\int_{a}^{b} f(x) d x
# $$

# $$
# \text {First transform}
# $$

# $$
# \mathrm{-1}\leqslant \xi \leqslant \mathbf{1} \hspace{4mm}\text {onto}\hspace{4mm} \mathrm{a} \leqslant x \leqslant \mathrm{b}
# $$

# $$
# \text {by}
# $$
# $$
# x=\frac{b+a}{2}+\frac{b-a}{2} \xi
# $$

# $$
# \text {Use Table A-1 Zeros and Weights for Gauss-Legendre Quadrature }
# $$

# $$
# \begin{array}{|c|c|c|}\hline m & \pm \xi_{k} & w_{k} \\ \hline 2 & 0.5773502692
#  & 1.0000000000 \\ \hline 4 & 0.3399810436 & 0.6521451549 \\ & 0.8611363116 
# & 0.3478548451 \\ \hline 6 & 0.2386191861 & 0.4679139346 \\ & 0.6612093865 
# & 0.3607615730 \\ & 0.9324695142 & 0.1713244924 \\ \hline & 0.1834346425 
# & 0.3626837834 \\ 8 & 0.5255324099 & 0.3137066459 \\ & 0.7966664774 
# & 0.2223810345 \\ & 0.9602898565 & 0.1012285363 \\ \hline\end{array}
# $$

# %%

def guass(table):
    t = table
    a, b = 0, 20
    I_bar = []
    for i in range(len(t["Xi"])):
        x = (b + a)/2 + ((b - a)/2)*t["Xi"][i]
        fx = (0.5 * x) + x * np.sin((2 *np.pi * x)/ 10)
        I = (b - a)/2 * fx * t["w"][i]
        I_bar.append(I)
    I_bar = np.array(I_bar)
    print(I_bar)
    I_bar = np.sum(I_bar)
    return I_bar

m = ["m2", "m4", "m6", "m8"]
table = {"m2": {"Xi": [0.5773502692], 
            "w": [1.0000000000]},
        "m4": {"Xi": [0.3399810436, 0.8611363116], 
            "w": [0.6521451549, 0.3478548451]},
        "m6": {"Xi": [0.2386191861, 0.6612093865, 0.9324695142], 
            "w": [0.4679139346, 0.3607615730, 0.1713244924]},
         "m8": {"Xi": [0.1834346425, 0.5255324099, 0.7966664774, 0.9602898565],  
            "w": [0.3626837834, 0.3137066459, 0.2223810345, 0.1012285363]}}

I_bar_all = {}
for i in range(len(m)):
    I_bar = guass(table[m[i]])
    I_bar_all.update({m[i]: I_bar})

print("Gauss quadrature:  ", I_bar_all)
# %%
