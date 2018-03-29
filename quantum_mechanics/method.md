% **Description of the method**

We describe the solution of the Schrödinger equation using Ritz method
and Hermite functions basis.

## Description
We want to solve the variational equation

$$\delta \Pi[\psi] = 0\, ,$$

with

$$\Pi[\psi] = \frac{1}{2} \langle \nabla \psi, \nabla\psi\rangle +
              \langle \psi, V(x) \psi\rangle -
               E\langle \psi, \psi\rangle \, ,$$

being $\psi$ the wave function, $V(x)$ the potential and $E$ the energy.
This variational formulation is equivalent to the time-independent
Schrödinger equation, and $E$ works as a Lagrange multiplier to enforce
that the probability over the whole domain is 1.

We can expand the wave function in an orthonormal basis, namely

$$\psi = \sum_{n=0}^N c_n u_n(x)\, ,$$

where $u_n(x) \equiv \mu_n H_n(x) e^{-x^2/2}$ is a normalized
Hermite function, $\mu_n$ is the inverse of magnitude of the $n$th
Hermite polynomial

$$\mu_n = \frac{1}{\sqrt{\pi^{1/2} n! 2^n}}\, ,$$

and $c_n$ are the coefficients of the expansion. This representation
is exact in the limit $N \rightarrow \infty$.

If we replace the expansion in the functiona, we obtain

$$\Pi_N = \sum_{m=0}^N\sum_{n=0}^N c_m c_n\left[
          \frac{1}{2} \langle \nabla u_m, \nabla u_n\rangle +
          \langle u_m, V(x) u_n\rangle -
          E^N \delta_{mn}\right]\, .$$

The integral involving the two derivatives reads

\begin{align*}
u_m' u_n' =& \left[2m \frac{\mu_{m-1}}{\mu_m}u_{m-1} - x u_m\right]
            \left[2n \frac{\mu_{n-1}}{\mu_n}u_{n-1} - x u_n\right]\\
          =& 4mn\frac{\mu_{m-1} \mu_{n-1}}{\mu_m \mu_n} u_{n-1} u_{m-1}
           - 2m\frac{\mu_{m-1}}{\mu_{m}}x u_{m-1} u_n\\
           &- 2n\frac{\mu_{n-1}}{\mu_{n}}x u_{n-1} u_m + x^2 u_m u_n
\end{align*}

Thus, the kinetic energy term reads

\begin{align*}
\langle \nabla u_m, \nabla u_n \rangle =&
    4mn\frac{\mu_{m-1} \mu_{n-1}}{\mu_m \mu_n} \langle u_{n-1}, u_{m-1}\rangle
    - 2m\frac{\mu_{m-1}}{\mu_{m}} \langle u_{m-1}, x u_n\rangle\\
    &- 2n\frac{\mu_{n-1}}{\mu_{n}} \langle u_{m}, x u_{n - 1}\rangle
     + \langle u_m, x^2 u_n\rangle\\
    =& 4mn \frac{\mu_{m-1}^2}{\mu_m^2}\delta_{mn} -
      2m \frac{\mu_{m-1}}{\mu_m} \alpha_{m-1, n} -
      2n \frac{\mu_{n-1}}{\mu_n} \alpha_{m, n-1} + \beta_{mn} \, ,
\end{align*}

with

$$\alpha_{m,n} \equiv \langle u_{m}, x u_n\rangle = \begin{cases}
\sqrt{\frac{n + 1}{2}} & m=n +1\\
\sqrt{\frac{n}{2}} & m=n - 1\\
0 & \text{otherwise}\end{cases}\, ,$$

and

$$\beta_{m,n} \equiv \langle u_{m}, x^2 u_n\rangle = \begin{cases}
\frac{\sqrt{n(n-1)}}{2} & m = n - 2\\
\frac{2n + 1}{2} & m = n \\
\frac{\sqrt{(n+1)(n+1)}}{2} & m = n + 2 \\
0 & \text{otherwise}\end{cases}\, .$$

The functional is rewritten as
\begin{align}
\Pi_N =& \sum_{m=0}^N \sum_{n=0}^N c_m c_n
  \left[2mn \frac{\mu^2_{m-1}}{\mu^2_m}\delta_{mn}
  - m\frac{\mu_{m-1}}{\mu_m}\alpha_{m - 1, n}
  - n\frac{\mu_{n-1}}{\mu_n}\delta_{m, n-1} \right.\nonumber \\
  &\left. - \frac{1}{2}\beta_{mn} + \langle u_m, V(x) u_n\rangle
  - E^N \delta_{mn}\right] \, .
\end{align}

Taking the variation

$$\delta \Pi_N = 0\, ,$$

that in this case is equivalent to

$$\frac{\partial \Pi_N}{\partial c_i} = 0\quad \forall i=0, 1, \cdots N\, ,$$

yields to

$$[H]\lbrace c\rbrace = E^N\lbrace c\rbrace \, ,$$

with

$$H_{mn} = 2mn \frac{\mu^2_{m-1}}{\mu^2_m}\delta_{mn}
  - m\frac{\mu_{m-1}}{\mu_m}\alpha_{m - 1, n}
  - n\frac{\mu_{n-1}}{\mu_n}\delta_{m, n-1}
  - \frac{1}{2}\beta_{mn} + \langle u_m, V(x) u_n\rangle\, .$$

The last integral is computed using Gauss-Hermite quadrature.

