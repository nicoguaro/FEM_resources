from __future__ import division
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh
import matplotlib.pyplot as plt

L = 100
N = 501
x = np.linspace(-L/2, L/2, N)
dx = x[1] - x[0]

T = -0.5*diags([-2., 1., 1.], [0,-1, 1], shape=(N, N))/dx**2
U_vec = 0.5*np.sin(x)**2 * x**2
U = diags([U_vec], [0])

H = T + U

vals, vecs = eigsh(H, which='SM')

print(np.round(vals, 6))
for k in range(4):
    vec = vecs[:, k]
    mag = np.sqrt(np.dot(vecs[:, k],vecs[:, k]))
    vec = vec/mag
    plt.plot(x, vec, label=r"$n=%i$"%k)

plt.xlim(-10, 10) 
plt.legend()
plt.show()