import context
import numpy as np
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
    def centdif(self):

        Pj = np.zeros_like(self.Pj)
        
        P = np.pad(self.Pj,(1,1),'edge')
        for j in range(len(self.xx)):
            Pj[j] = (-self.u0 * (P[j+1] - P[j-1]) / (2 * self.dx))
            # Pjn.append(Pj)
        # Pjn = np.array(Pjn)
        # self.Pj = Pj
        return Pj
    
    #############################################
    # time discretization methods
    #############################################
    def rk3(self):
        Pjn_1 = []

        for n in range(len(self.nsteps)):
            
            Pj = self.Pj

            P_str = Pj + (self.dt/3) * self.centdif()

            self.Pj = P_str
            P_str_str  = Pj + (self.dt/2) * self.centdif()

            self.Pj = P_str_str
            Pn  = Pj + self.dt * self.centdif()
            Pn = np.array(Pn)
            Pjn_1.append(Pn)

            self.Pj = Pn
        Pjn_1 = np.array(Pjn_1)
        return Pjn_1








