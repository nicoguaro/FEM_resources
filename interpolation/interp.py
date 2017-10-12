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
    power = np.array(range(2*n))
    for row in range(n):
        if x[row] == 0:
            conf_van[row, 0] = 1
            conf_van[row + n, 1] = 1
        else:
            conf_van[row, :] = x[row]**power
            conf_van[row + n, :] = power*x[row]**(power - 1)
    return conf_van


def inter_coef(x, inter_type="lagrange"):
    """Compute the coefficients for interpolation

    The desired interpolation is for the points x
    """
    if inter_type == "lagrange":
        vand_mat = vander_mat(x)
    elif inter_type == "hermite":
        vand_mat = conf_vander_mat(x)
    coef = np.linalg.solve(vand_mat, np.eye(vand_mat.shape[0]))
    return coef


def compute_interp(x, f, x_eval, df=None):
    """
    Compute the interpolation for points x_eval given by
    points x.

    If derivatives are given (df) it computes the
    Hermite interpolation for x_eval.
    """
    n = len(x)
    if df is None:
        coef = inter_coef(x, inter_type="lagrange")
    else:
        coef = inter_coef(x, inter_type="hermite")
    f_eval = np.zeros_like(x_eval)
    nmat = coef.shape[0]
    for row in range(nmat):
        for col in range(nmat):
            if col < n or nmat == n:
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
    interp_f = compute_interp(x, f, x_eval, df=df)
    plt.plot(x_eval, 1/(1 + 25*x_eval**2))
    plt.plot(x_eval, interp_f)
    plt.plot(x, f, '.')
    plt.ylim(0, 2)
    plt.show()