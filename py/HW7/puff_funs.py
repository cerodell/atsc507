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
    def centered(self):
        ff = []
        Pj = np.pad(self.Pj,(1,1),'edge')
        for j in range(len(self.Pj)):
            f = (Pj[j+1] - Pj[j-1])/ self.dx
            ff.append(f)
        ff = ff[1:-1]
        return ff

    # ## Euler forward
    # def eulerf(self):
    #     T = self.TempFun() * self.dt + self.Tn
    #     return T

    # ## Runge–Kutta 2nd order (mid-point)
    # def rk2(self): 
    #     Tn = self.Tn
    #     t = self.t

    #     T_str = Tn + (self.dt/2) * self.TempFun()

    #     self.Tn = T_str
    #     self.t  = (t + (self.dt/2))
    #     T  = Tn + self.dt * self.TempFun()

    #     self.Tn = Tn
    #     self.t  = t
    #     return round(T, 4)

    #############################################
    # time discretization methods
    #############################################
    ## Runge–Kutta 3rd order 
    # def rk3(self):
    #     # Pn = self.Pj
    #     # t = self.t
    #     PF = []
    #     for i in range(len(self.t)):
    #         Pj = self.Pj
    #         t = self.t[i]
    #         P_str = self.Pj + (self.dt/3) * self.centered()

    #         self.Pj = P_str
    #         # self.t  = (t + (self.dt/3))
    #         P_str_str  = Pj + (self.dt/2) * self.centered()

    #         self.Pj = P_str_str
    #         # self.t  = (t + (self.dt/2))
    #         P  = Pj + self.dt * self.centered()
    #         PF.append(P)
    #     # self.Pn = Pn
    #     # self.t  = t

    #     return PF

    def rk3(self):
        Pj = self.Pj
        P_str = self.Pj + (self.dt/3) * self.centered()

        self.Pj = P_str
        P_str_str  = Pj + (self.dt/2) * self.centered()

        self.Pj = P_str_str
        P  = Pj + self.dt * self.centered()
        return P


    # ## Runge–Kutta 4th order 
    # def rk4(self): 
    #     Tn = self.Tn
    #     t = self.t

    #     k1 = self.TempFun()

    #     self.Tn = (Tn + (self.dt/2)*k1)
    #     self.t  = (t + (self.dt/2))
    #     k2 = self.TempFun()

    #     self.Tn = (Tn + (self.dt/2)*k2)
    #     self.t  = (t + (self.dt/2))
    #     k3 = self.TempFun()

    #     self.Tn = (Tn + self.dt*k3)
    #     self.t  = (t + (self.dt))
    #     k4 = self.TempFun()

    #     T = Tn + (self.dt/6) * (k1 + (2 * k2) + (2 * k3) + k4)

    #     self.Tn = Tn
    #     self.t  = t
    #     return round(T, 4)






