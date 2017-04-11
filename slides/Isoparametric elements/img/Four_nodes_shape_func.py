# -*- coding: utf-8 -*-
"""
Plot the interpolation functions for a 4-node isoparametric
element.

@author: Nicolas Guarin-Zapata
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 14

def make_plot(x, y, N):
    x_cords = [-1, 1, 1, -1]
    y_cords = [-1, -1, 1, 1]
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot([-1, 1, 1, -1, -1], [-1, -1, 1, 1, -1], "-ko", zorder=-10)
    ax.plot([x_cords[cont-1], x_cords[cont-1]],
            [y_cords[cont-1], y_cords[cont-1]], [0, 1], "--k", zorder=-10)
    ax.plot_surface(x, y, N, cstride=1, rstride=1, cmap="YlGnBu_r",
                alpha=0.6, lw=0.5, zorder=3)
    ax.view_init(azim=-60, elev=30)
    ax.set_xlabel(r"$x$", fontsize=18)
    ax.set_ylabel(r"$y$", fontsize=18)
    ax.set_zlabel(r"$N^%i(x, y)$"%cont, fontsize=18)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(0, 1)
    plt.savefig("shape_func-4-nodes-%i.svg"%cont,
                bbox_inches="tight", pad_inches=0.1, transparent=True)


x, y = np.mgrid[-1:1:21j, -1:1:21j]
N1 = 0.25*(1 - x)*(1 - y)
N2 = 0.25*(1 + x)*(1 - y)
N3 = 0.25*(1 + x)*(1 + y)
N4 = 0.25*(1 - x)*(1 + y)
cont = 0
for N in [N1, N2, N3, N4]:
    cont = cont + 1
    make_plot(x, y, N)    

plt.show()