from devito import Grid, Function, Eq, solve, dimensions
from sympy.abc import a
# Initialize `u` for space order 2

nx = 50
ny = 50
nz = 50

i, j, k = dimensions('i/2 j/2 k/2')

grid = Grid(shape=(nx, ny, nz), extent=(2., 2., 2.))
T = Function(name='T', grid=grid, space_order=2, staggered = dimensions('x/2 y/2 z/2'))
S = Function(name='S', grid=grid, space_order=2)

# Create an equation with second-order derivatives
eq = Eq(T.dx2 + T.dy2 + T.dz2)
stencil = solve(eq, T)
eq_stencil = Eq(T, stencil)
print(eq_stencil)