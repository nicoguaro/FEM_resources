#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Weighted residual methods in 1D

@author: Nicolas Guarin-Zapata
"""
from __future__ import division, print_function
from sympy import zeros, symbols, S
from sympy import integrate, diff, linsolve
from sympy import sin, pi


def least_squares(lhs, rhs, basis, nterms, domain=(0, 1)):
    """
    Return matrices for least squares solution of differential 
    equations
    """
    x0, x1 = domain
    x = symbols("x")
    A_mat = zeros(nterms, nterms)
    b_vec = zeros(nterms, 1)
    for row in range(nterms):
        phi_i = basis(x, row)
        b_vec[row] = integrate(rhs(x)*lhs(phi_i, x), (x, x0, x1))
        for col in range(nterms):
            phi_j = basis(x, col)
            A_mat[row, col] = integrate(lhs(phi_i, x)*lhs(phi_j, x),
                                       (x, x0, x1))
    return A_mat, b_vec


def collocation(lhs, rhs, basis, nterms, domain=(0, 1), x_col=None):
    """
    Return matrices for least squares solution of differential 
    equations
    """
    x0, x1 = domain
    if x_col is None:
        dx = S(x1 - x0)/(nterms - 2)
        x_col = [dx + dx*cont for cont in range(nterms)]
    x = symbols("x")
    A_mat = zeros(nterms, nterms)
    b_vec = zeros(nterms, 1)
    for row in range(nterms):
        b_vec[row] = rhs(x_col[row])
        for col in range(nterms):
            phi_j = basis(x, col)
            A_mat[row, col] = lhs(phi_j, x).subs(x, x_col[row])
    return A_mat, b_vec


def galerkin(lhs, rhs, basis, nterms, domain=(0, 1)):
    """
    Return matrices for Galerkin solution of differential 
    equations
    """
    x0, x1 = domain
    x = symbols("x")
    A_mat = zeros(nterms, nterms)
    b_vec = zeros(nterms, 1)
    for row in range(nterms):
        phi_i = basis(x, row)
        b_vec[row] = integrate(rhs(x)*phi_i, (x, x0, x1))
        for col in range(nterms):
            phi_j = basis(x, col)
            A_mat[row, col] = integrate(lhs(phi_i, x)*phi_j, (x, x0, x1))
    return A_mat, b_vec



if __name__ == "__main__":
    basis = lambda x, k: x*(1 - x)*x**k
    lhs = lambda u, x: diff(u, x, 2) + u
    rhs = lambda x: -x
    x = symbols("x")
    u_e = sin(x)/sin(1) - x
    nterms = 10
    c = symbols('c0:%d' % nterms)
#    A, b = least_squares(lhs, rhs, basis, nterms)
#    A, b = collocation(lhs, rhs, basis, nterms)
    A, b =  galerkin(lhs, rhs, basis, nterms)
    sol = linsolve((A, b), c)
    subs = dict(zip(c, sol.args[0]))
    u = sum(c[cont]*basis(x, cont) for cont in range(nterms)).subs(subs)
    