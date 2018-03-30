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
from numpy import array, linspace, abs, pi, sin, sqrt
from numpy.linalg import norm
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
        x = linspace(-1, 1, num)
    else:
        x = sin(linspace(-pi/2, pi/2, num))
    bounds = [(-1, 1) for cont in range(num)]
    opt_fun = lambda x: -abs(vander_det(x))
    res = minimize(opt_fun, x, method='SLSQP', bounds=bounds,
               tol=tol)
    return res.x


if __name__ == "__main__":
    x = gauss_lobatto(5)
    x_exact = array([-1, -sqrt(3/7), 0, sqrt(3/7), 1])
    print("Relative error: {:g}".format(norm(x - x_exact)/norm(x_exact)))
