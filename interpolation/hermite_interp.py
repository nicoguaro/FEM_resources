# -*- coding: utf-8 -*-
"""
Hermite interpolation from Numerical Analysis (Burden and Faires)

@author: Nicolas Guarin-Zapata
@date: June 6, 2017
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from gauss_lobatto import gauss_lobatto


def hermite_coeff(x, f, df):
    """Compute coefficients for Hermite interpolation"""
    n = len(x)
    Q = np.zeros((2*n, 2*n))
    z = np.zeros((2*n))
    z[::2] = x
    z[1::2] = x
    Q[::2, 0] = f
    Q[1::2, 0] = f
    Q[1::2, 1] = df
    Q[2::2, 1] = (Q[2::2, 0] - Q[1:-1:2, 0])/(z[2::2] - z[1:-1:2])
    for i in range(2, 2*n):
        for j in range(2, i + 1):
            numer = Q[i, j - 1] - Q[i - 1, j - 1]
            denom = z[i] - z[i - j]
            Q[i, j] = numer/denom
    return np.diagonal(Q)


def eval_hermite(x, x_int, Q):
    """
    Evaluate the interpolation using the coefficients Q
    given the points x_int
    """
    n = len(Q)
    z = np.zeros((n))
    z[::2] = x
    z[1::2] = x
    acum = np.zeros_like(x_int)
    for k in range(n):
        prod = np.ones_like(x_int)
        for i in range(k):
            prod *= (x_int - z[i])
        acum += Q[k]*prod
    return acum
        

if __name__ == "__main__":
    equispaced = False
    n = 21
    if equispaced:
        x = np.linspace(-1, 1, n)
    else:
        x, _ = gauss_lobatto(n)
    f = 1/(1 + 25*x**2)
    df = -50*x/(1 + 25*x**2)**2
    z = np.linspace(-1, 1, 500)
    Q = hermite_coeff(x, f, df)
    interp_f = eval_hermite(x, z, Q)
    plt.plot(z, 1/(1 + 25*z**2))
    plt.plot(z, interp_f)
    plt.plot(x, f, '.')
    plt.ylim(0, 2)
    plt.show()