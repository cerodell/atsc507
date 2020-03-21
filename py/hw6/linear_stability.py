import context
import numpy as np
import matplotlib.pyplot as plt
from cr507.utils import plt_set

########################################################
######################### A.2 #########################
########################################################

mm = np.arange(0.1,1,0.0001)
cr = 6 / (8 * np.sin(2 * np.pi / mm) - np.sin( 4 * np.pi / mm))
l = np.full_like(mm, 0.729)

# print(cr)
fig, ax = plt.subplots(1,1, figsize=(12,6))
fig.suptitle('Linear Stability HW6(A.2)', fontsize= plt_set.title_size, fontweight="bold")
ax.plot(mm,cr)
ax.plot(mm,l, label = "CR = 0.729")
ax.set_xlabel('m', fontsize = plt_set.label)
ax.set_ylabel('cr', fontsize = plt_set.label)
ax.set_ylim(-6,6)
ax.xaxis.grid(color='gray', linestyle='dashed')
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.legend()

plt.show()



########################################################
######################### B.3 #########################
########################################################
m = [2.0,2.5,3,4,5,10,20]
cr =  np.arange(0.,3.5,0.5)

A_list = []
for c in cr:
    mm = np.arange(1,20,0.01)
    p2m = (np.pi * 2 / mm)
    A = (1/24)*((-3 * (c**2) * np.sin(p2m)) - ((c**3) * np.sin(3 * p2m)) + (6 * (c**2) * np.sin( p2m)) - (6 * (c**2)) - (24 * (c**2) * np.sin(p2m)) + 24 )
    A_list.append(A)

AA = np.array(A_list)
# l = np.full_like(m, 0.729)

# # print(cr)
# fig, ax = plt.subplots(1,1, figsize=(12,6))
# fig.suptitle('Linear Stability HW6(B.5)', fontsize= plt_set.title_size, fontweight="bold")
# ax.plot(A_list,cr)
# # ax.plot(mm,l, label = "CFL")
# ax.set_xlabel('A', fontsize = plt_set.label)
# ax.set_ylabel('cr', fontsize = plt_set.label)
# # ax.set_ylim(-6,6)
# # ax.legend()

# plt.show()


fig, ax = plt.subplots(1,1, figsize=(12,6))
fig.suptitle('Linear Stability HW6(B.5)', fontsize= plt_set.title_size, fontweight="bold")
for i in range(len(AA[:,0])):
    ax.plot(mm,AA[i], label = ("CR = " + str(cr[i])))
# ax.plot(mm,l, label = "CFL")
ax.set_xlabel('m', fontsize = plt_set.label)
ax.set_ylabel('A(k)', fontsize = plt_set.label)
ax.xaxis.grid(color='gray', linestyle='dashed')
ax.yaxis.grid(color='gray', linestyle='dashed')
# ax.set_ylim(-6,6)
ax.legend()

plt.show()


