"""
Python script version of the IPython Notebook 
'Vibration modes of membranes with convex polygonal shape'.


Author: Nicolas Guarin Zapata
"""
from __future__ import division
from sympy import *
from sympy import symbols
from sympy.plotting import plot3d
from sympy.utilities.lambdify import lambdify
from time import time
import matplotlib.pyplot as plt
import numpy as np

x, y, r, s= symbols('x y r s')
k, m, n = symbols('k m n', integer=True)

t0 = time()

nsides = 4
poly = [[cos(2*k*pi/nsides), sin(2*k*pi/nsides)] for k in range(0,nsides)]
#poly = [[-1,-1],[1,-1],[1,1],[-1,1]]
npts = len(poly)
lines = [[k,0] if k==npts-1 else [k,k+1] for k in xrange(npts)]
centroid = [sum([poly[k][0] for k in xrange(npts)]), sum([poly[k][1] for k in xrange(npts)])]


# Polynomial defining the boundaries
def b(x,y,n):
    prod = 1
    for k in range(0, n):
        prod = prod * ((y - poly[lines[k][0]][1])*(poly[lines[k][0]][0] - poly[lines[k][1]][0]) - 
            (x - poly[lines[k][0]][0])*(poly[lines[k][0]][1] - poly[lines[k][1]][1]))
    return prod.expand()


def w_fun(x, y, m, n):
    """ Trial function. """
    var('c:%d' % (m*n)) # This is the way of define the coefficients c_i
    w = 0
    for i in xrange(0, m):
        for j in xrange(0, n):
            w = w + eval('c%d' % (m*j + i)) * x**i * y**j
    
    return w

def u_fun(x, y, m, n):
    """ Complete function. Contains the boundary and trial functions. """
    return (b(x, y, npts) * w_fun(x, y, m, n)).expand()

m = 4
n = 4
u = u_fun(x, y, m, n)
dudx = [diff(u, x), diff(u, y)]


dudx2 = expand(dudx[0]*dudx[0] + dudx[1]*dudx[1])
K = Matrix(m*n, m*n, lambda i,j: 0)
Kaux = Matrix(m*n, m*n, lambda ii, jj: diff(dudx2, eval('c%d' % ii), eval('c%d' % jj)))
M = Matrix(m*n, m*n, lambda i,j: 0)
Maux = Matrix(m*n, m*n, lambda ii, jj: diff(u**2, eval('c%d' % ii), eval('c%d' % jj)))
del dudx, u

t1 = time()
for j in xrange(len(lines)):
    A = [poly[lines[j][0]][0], poly[lines[j][0]][1]]
    B = [poly[lines[j][1]][0], poly[lines[j][1]][1]]
    C = [centroid[0], centroid[1]]
    J = Matrix([[B[0] - A[0], C[0] - A[0]],
                 [B[1] - A[1], C[1] - A[1]]])
    detJ = J.det()
    trans = J * Matrix([[r],[s]]) + Matrix(A)
    Kaux2 = Kaux.subs({x:trans[0], y:trans[1]})
    Maux2 = Maux.subs({x:trans[0], y:trans[1]})
    K = K + integrate(Kaux2*detJ, (r, 0, 1-s), (s, 0, 1))
    M = M + integrate(Maux2*detJ, (r, 0, 1-s), (s, 0, 1))
print "Elapsed time: ", time() - t0



Kn = np.array(K)
Mn = np.array(M)

import scipy.linalg as LA
vals, vecs = LA.eigh(Kn, Mn, eigvals=(0,8))

anal_vals = [pi**2/4*(i**2 + j**2) for i in xrange(1,4) for j in xrange(1,4)]
anal_valsN = np.sort(np.array(Matrix(anal_vals).T.evalf()).astype(dtype=float))

error = (anal_valsN - vals)/anal_valsN

print "Elapsed time: ", time() - t0


