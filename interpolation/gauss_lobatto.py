# -*- coding: utf-8 -*-
"""
Computes the Legendre-Gauss-Lobatto nodes, weights and the LGL Vandermonde 
matrix. The LGL nodes are the zeros of (1-x**2)*P'_N(x). Useful for numerical
integration and spectral methods. 

Reference on LGL nodes and weights: 
  C. Canuto, M. Y. Hussaini, A. Quarteroni, T. A. Tang, "Spectral Methods
  in Fluid Dynamics," Section 2.3. Springer-Verlag 1987

  
Originally implemented in MATLAB by Greg von Winckel
http://www.mathworks.com/matlabcentral/fileexchange/4775-legende-gauss-lobatto-nodes-and-weights


@author: Nicolas Guarin-Zapata
"""
from __future__ import division, print_function
from numpy import pi, sin, zeros, amax, abs, square, array, linspace
from numpy.linalg import norm
import numpy as np


def gauss_lobatto(N, tol=1e-15):
    """
    Use Chebyshev nodes as first guess.
    
    Compute P_(N) using the recursion relation
    Compute its first and second derivatives and
    update x using the Newton-Raphson method.
    
    Chebyshev nodes are computed using the symmetric
    formula that involves sine as presented in:

      Nick Trefethen. Aproximation Theory and 
      Aproximation Practice, Chapter 2, exercise 2.
    
    """
    x = sin(linspace(-pi/2, pi/2, N))
    P = zeros((N, N))  # Vandermonde Matrix
    x_old = 2
    while amax(abs(x - x_old)) > tol:
        x_old = x
        P[:, 0] = 1
        P[:, 1] = x
        for k in range(2, N):
            P[:, k] = ((2 * k - 1) * x * P[:, k - 1] -
                       (k - 1) * P[:, k - 2]) / k
        x = x_old - (x * P[:, N - 1] - P[:, N - 2]) / (N * P[:, N - 1])

    w = 2.0 / ((N - 1) * N * square(P[:, N - 1]))

    return array(x), array(w)


if __name__ == "__main__":
    x, _ = gauss_lobatto(5)
    x_exact = array([-1, -np.sqrt(3/7), 0, np.sqrt(3/7), 1])
    print("Relative error: {:g}".format(norm(x - x_exact)/norm(x_exact)))
