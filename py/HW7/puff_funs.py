import context
import numpy as np
from cr507.utils import plt_set
import matplotlib.pyplot as plt
from collections import namedtuple 


class Approximator:

    #############################################
    # initialize condtions
    #############################################
    def __init__(self, valueDict):
        self.__dict__.update(valueDict)



    #############################################
    # spatial discretization methods
    #############################################
    # def centdif(self):

    #     Pj = np.zeros_like(self.Pj)
        
    #     P = np.pad(self.Pj,(1,1),'edge')
    #     print(P[50],"centdif P")
    #     for j in range(len(self.xx)):
    #         Pj[j] = (-self.u0 * (P[j+1] - P[j-1]) / (2 * self.dx))
    #         # Pjn.append(Pj)
    #     # Pjn = np.array(Pjn)
    #     # self.Pj = Pj
    #     return Pj

    def centdif(self):
        # print(self.Pj[50],"centdif start")
        Pj = (-self.u0 * (np.roll(self.Pj,-1) - np.roll(self.Pj,1)) / (2 * self.dx))
        
        # print(Pj[50],"centdif end")
        return Pj
    
    #############################################
    # time discretization methods
    #############################################
    def rk3(self):
        Pjn_1 = []

        for n in range(len(self.nsteps)):
            
            Pj = self.Pj
            # print(Pj[50], "Pj var")
            P_str = Pj + (self.dt/3) * self.centdif()
            # print(P_str[50], 'P_str')

            self.Pj = P_str
            # print(self.Pj[50], 'self Pj should be Pjstr')

            P_str_str  = Pj + (self.dt/2) * self.centdif()
            # print(P_str_str[50], 'P_str_str')

            self.Pj = P_str_str
            # print(self.Pj[50], 'self Pj should be Pj_str_str')

            Pn  = Pj + self.dt * self.centdif()
            Pn = np.array(Pn)
            # print(Pn[50], "Pn pre append")
            Pjn_1.append(Pn)

            self.Pj = Pn
            # print(self.Pj[50], "self Pj or Pn")

        Pjn_1 = np.array(Pjn_1)
        return Pjn_1

    def plot_functions(self, method):
        if method == 'Initial':
            fig, ax = plt.subplots(1,1, figsize=(12,4))
            fig.suptitle('Puff HW7', fontsize= plt_set.title_size, fontweight="bold")
            ax.plot(self.xx, self.Pj, color = 'blue', label = "Initial concentration", zorder = 9)
            # ax.plot(self.xx,self.cideal, color = 'red', label = "Final Ideal", zorder = 8)
            # Prk3 = self.rk3()
            # ax.plot(self.xx,Prk3.T[:,-1], color = 'green', label = "RK3", zorder = 10)
            # ax.plot(initialVals['xx'],pnew, color = 'green', label = "RK3", zorder = 10)

            ax.set_xlabel('Grid Index (i)', fontsize = plt_set.label)
            ax.set_ylabel('Quantity', fontsize = plt_set.label)
            ax.xaxis.grid(color='gray', linestyle='dashed')
            ax.yaxis.grid(color='gray', linestyle='dashed')
            ax.set_ylim(-10,15)
            ax.legend()
            plt.show()

        elif method == 'Final':
            fig, ax = plt.subplots(1,1, figsize=(12,4))
            fig.suptitle('Puff HW7', fontsize= plt_set.title_size, fontweight="bold")
            ax.plot(self.xx, self.Pj, color = 'blue', label = "Initial concentration", zorder = 9)
            ax.plot(self.xx,self.cideal, color = 'red', label = "Final Ideal", zorder = 8)
            # Prk3 = self.rk3()
            # ax.plot(self.xx,Prk3.T[:,-1], color = 'green', label = "RK3", zorder = 10)
            # ax.plot(initialVals['xx'],pnew, color = 'green', label = "RK3", zorder = 10)

            ax.set_xlabel('Grid Index (i)', fontsize = plt_set.label)
            ax.set_ylabel('Quantity', fontsize = plt_set.label)
            ax.xaxis.grid(color='gray', linestyle='dashed')
            ax.yaxis.grid(color='gray', linestyle='dashed')
            ax.set_ylim(-10,15)
            ax.legend()
            plt.show()

        elif method == 'RK3':
            fig, ax = plt.subplots(1,1, figsize=(12,4))
            fig.suptitle("Runge-Kutta 3rd order Centred in Space  CR: 0.5", fontsize= plt_set.title_size, fontweight="bold")
            ax.plot(self.xx, self.Pj, color = 'blue', label = "Initial concentration", zorder = 9)
            ax.plot(self.xx,self.cideal, color = 'red', label = "Final Ideal", zorder = 8)
            Prk3 = self.rk3()
            ax.plot(self.xx,Prk3.T[:,-1], color = 'green', label = "RK3", zorder = 10)
            ax.set_xlabel('Grid Index (i)', fontsize = plt_set.label)
            ax.set_ylabel('Quantity', fontsize = plt_set.label)
            ax.xaxis.grid(color='gray', linestyle='dashed')
            ax.yaxis.grid(color='gray', linestyle='dashed')
            ax.set_ylim(-10,15)
            ax.legend()
            plt.show()
        else:
            pass

        
        return







