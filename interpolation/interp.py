#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auxiliary functions for interpolation

@author: Nicolas Guarin-Zapata
"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
from gauss_lobatto import gauss_lobatto


def vander_mat(x):
    """Vandermonde matrix for points in x"""
    n = len(x)
    van = np.zeros((n, n))
    for row in range(n):
        for col in range(n):
            van[row, col] = x[row]**col
    return van


def conf_vander_mat(x):
    """Confluent Vandermonde matrix for points in x
    
        
    References
    ----------
    .. [1] Walter Gautschi (1962). On inverses of Vandermonde
        and confluent Vandermonde matrices. Numerische Mathematik, 4
        117-123.
    """
    
    n = len(x)
    conf_van = np.zeros((2*n, 2*n))
    for row in range(n):
        if x[row] == 0:
            conf_van[row, 0] = 1
            conf_van[row + n, 1] = 1
        else:
            for col in range(2*n):
                conf_van[row, col] = x[row]**col
                conf_van[row + n, col] = col*x[row]**(col - 1)
    return conf_van


def hermite_coef(x):
    """Compute the coefficients for Hermite interpolation
    
    The desired interpolation is for the points x
    """
    n = len(x)
    conf_vand = conf_vander_mat(x)
    coef = np.linalg.solve(conf_vand, np.eye(2*n))
    return coef


def compute_interp(x, f, df, x_eval):
    """
    Compute the interpolation for points x_eval given by
    points x
    """
    coef = hermite_coef(x)
    n = len(x)
    f_eval = np.zeros_like(x_eval) 
    for row in range(2*n):
        for col in range(2*n):
            if col < n:
                f_eval += coef[row, col]*x_eval**row*f[col]
            else:
                f_eval += coef[row, col]*x_eval**row*df[col - n]
    return f_eval
    

if __name__ == "__main__":
    equispaced = False
    n = 11
    if equispaced:
        x = np.linspace(-1, 1, n)
    else:
        x, _ = gauss_lobatto(n)
    f = 1/(1 + 25*x**2)
    df = -50*x/(1 + 25*x**2)**2
    x_eval = np.linspace(-1, 1, 500)
    interp_f = compute_interp(x, f, df, x_eval)
    plt.plot(x_eval, 1/(1 + 25*x_eval**2))
    plt.plot(x_eval, interp_f)
    plt.plot(x, f, '.')
    plt.ylim(0, 2)
    plt.show()