# -*- coding: utf-8 -*-
"""
Computes the Legendre-Gauss-Lobatto nodes.
The LGL nodes are the zeros of (1-x**2)*P'_N(x).

This routines are not intended to be optimized. Their
purpose is to illustrate that Lobatto nodes maximize
the Vandermonde matrix for the interval [-1, 1].

@author: Nicolas Guarin-Zapata
"""
from __future__ import division, print_function
import numpy as np
from scipy.optimize import minimize


def vander_det(x):
    """Vandermonde determinant for the points x"""
    prod = 1
    num = x.shape[0]
    for j in range(1, num):
        for i in range(0, j):
            prod *= x[j] - x[i]
    return prod


def gauss_lobatto(num, tol=1e-15, x0="chebyshev"):
    """
    Compute Lobatto nodes minimizing the Vandermonde
    determinant
    """
    if x0 == "equispaced":
        x = np.linspace(-1, 1, num)
    else:
        k = np.linspace(0, num + 1, num)
        x = np.cos(k[::-1]/(num +1)*np.pi)
    bounds = [(-1, 1) for k in range(num)]
    opt_fun = lambda x: -np.abs(vander_det(x))
    res = minimize(opt_fun, x, method='SLSQP', bounds=bounds,
               tol=tol)
    return res.x


if __name__ == "__main__":
    x = gauss_lobatto(5)
    x_exact = np.array([-1, -np.sqrt(3/7), 0, np.sqrt(3/7), 1])
    print(np.linalg.norm(x - x_exact)/np.linalg.norm(x_exact))
