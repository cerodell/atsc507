# from sympy import *
# init_printing()
# # x, x0, u = symbols('x, x_i, u')


# # Function for Taylor Series Expansion
# def taylor(function, x0, n):
#     """
#     Parameter "function" is our function which we want to approximate
#     "x0" is the point where to approximate
#     "n" is the order of approximation
#     """
#     return function.series(x,x0,n).removeO()


# f = Function('f')
# x, x0, u = symbols('x, x_i, u')
# f_x = f(x,u)

# test =  taylor(f_x, x0, 2)
# # print(test)
# print('f =', taylor(f_x, x0, 2))


# # x, x0, u = symbols('x, ((x_{i+0.5}+x_{i-0.5})*0.5), u')
# # f_x = f(x,u)
# # print('f =', taylor(f_x, x0, 2))



# from examples.cfd import plot_field, init_hat
import numpy as np
# %matplotlib inline


#NBVAL_IGNORE_OUTPUT
from devito import Grid, Function, TimeFunction, Operator, configuration, Eq, solve

nx = 50
ny = 50
nz = 50
nt  = 100


# Silence the runtime performance logging
configuration['log-level'] = 'ERROR'

# Now with Devito we will turn `p` into `TimeFunction` object 
# to make all the buffer switching implicit
grid = Grid(shape=(nx, ny), extent=(1., 2.))
p = Function(name='p', grid=grid, space_order=2)
pd = Function(name='pd', grid=grid, space_order=2)
p.data[:] = 0.
pd.data[:] = 0.

# Initialise the source term `b`
b = Function(name='b', grid=grid)
b.data[:] = 0.
b.data[int(nx / 4), int(ny / 4)]  = 100
b.data[int(3 * nx / 4), int(3 * ny / 4)] = -100

# Create Laplace equation base on `pd`
eq = Eq(pd.laplace, b, subdomain=grid.interior)
# Let SymPy solve for the central stencil point
stencil = solve(eq, pd)
# Now we let our stencil populate our second buffer `p`
eq_stencil = Eq(p, stencil)

# # Create boundary condition expressions
# x, y = grid.dimensions
# t = grid.stepping_dim
# bc = [Eq(p[x, 0], 0.)]
# bc += [Eq(p[x, ny-1], 0.)]
# bc += [Eq(p[0, y], 0.)]
# bc += [Eq(p[nx-1, y], 0.)]
          
# # Now we can build the operator that we need
# op = Operator([eq_stencil] + bc)

# # Run the outer loop explicitly in Python
# for i in range(nt):
#     # Determine buffer order
#     if i % 2 == 0:
#         _p = p
#         _pd = pd
#     else:
#         _p = pd
#         _pd = p

#     # Apply operator
#     op(p=_p, pd=_pd)
     
# plot_field(p.data, xmax=xmax, ymax=ymax, view=(30, 225))


# Silence the runtime performance logging
configuration['log-level'] = 'ERROR'

# Now with Devito we will turn `p` into `TimeFunction` object 
# to make all the buffer switching implicit
grid = Grid(shape=(nx, ny, nz))
p = Function(name='p', grid=grid, space_order=2)
pd = Function(name='pd', grid=grid, space_order=2)
p.data[:] = 0.
pd.data[:] = 0.

# Initialise the source term `b`
b = Function(name='b', grid=grid)
b.data[:] = 0.
b.data[int(nx / 4), int(ny / 4)]  = 100
b.data[int(3 * nx / 4), int(3 * ny / 4)] = -100

# Create Laplace equation base on `pd`
eq = Eq(pd.laplace, b, subdomain=grid.interior)
# Let SymPy solve for the central stencil point
stencil = solve(eq, pd)
# Now we let our stencil populate our second buffer `p`
eq_stencil = Eq(p, stencil)