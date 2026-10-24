#!/usr/bin/env python3
"""
D0047 exact symbolic self-check for the source-side beta=2 Brownian-carousel
normalization/Darboux bridge.

This is a self-check only. It verifies algebraic identities derived before code:
(1) the two gauged hyperbolic potentials from the carousel PDE and its
    normalized flux derivative;
(2) the analytically rotated quantum-PV potentials;
(3) the Zabrodin-Zotov parameter matches;
(4) the exact time-dependent Darboux intertwiner between the two
    quantum-PV Hamiltonians.

It does NOT prove the missing global Lax/monodromy identification.
"""
import sympy as sp

y, tau, z, t = sp.symbols("y tau z t")
E_tau = sp.exp(tau)
E = sp.exp(2*t)

# Source-side hyperbolic drift at beta=2 after x=sinh(y), tau=log(s).
b = sp.tanh(y) - E_tau*sp.cosh(y)/2

# Gauge already derived from the carousel generator.
phi = (
    -sp.log(sp.cosh(y))/2
    + E_tau*sp.sinh(y)/4
    - tau/4
    - sp.exp(2*tau)/64
)

# Survival wavefunction R=e^phi Psi.
V0_y_from_gauge = sp.simplify(
    sp.diff(phi, y, 2)
    + sp.diff(phi, y)**2
    + b*sp.diff(phi, y)
    - sp.diff(phi, tau)
)
V0_y = (
    -sp.Rational(1, 4)/sp.cosh(y)**2
    + E_tau*sp.sinh(y)/4
    - sp.exp(2*tau)*sp.cosh(2*y)/32
)
assert sp.simplify(sp.trigsimp(V0_y_from_gauge - V0_y)) == 0

# Flux derivative m=R_y has an extra b_y in its forward equation.
V1_y_from_gauge = sp.simplify(
    sp.diff(phi, y, 2)
    + sp.diff(phi, y)**2
    + b*sp.diff(phi, y)
    + sp.diff(b, y)
    - sp.diff(phi, tau)
)
V1_y = (
    sp.Rational(3, 4)/sp.cosh(y)**2
    - E_tau*sp.sinh(y)/4
    - sp.exp(2*tau)*sp.cosh(2*y)/32
)
assert sp.simplify(sp.trigsimp(V1_y_from_gauge - V1_y)) == 0

# After y=2z-i*pi/2 and tau=2t+i*pi/2, the two x-dependent potentials are:
V0 = (
    -sp.Rational(1, 8)/sp.cosh(z)**2
    + sp.Rational(1, 8)/sp.sinh(z)**2
    - E**2*sp.cosh(4*z)/16
    + E*sp.cosh(2*z)/2
)
V1 = (
    sp.Rational(3, 8)/sp.cosh(z)**2
    - sp.Rational(3, 8)/sp.sinh(z)**2
    - E**2*sp.cosh(4*z)/16
    - E*sp.cosh(2*z)/2
)

# Zabrodin-Zotov quantum-PV potential, using eta=xi+sigma.
def V_ZZ(zeta, eta, sigma):
    return (
        (4*zeta**2 - sp.Rational(1, 4))/(2*sp.cosh(z)**2)
        - (4*eta**2 - sp.Rational(1, 4))/(2*sp.sinh(z)**2)
        - E**2*sp.cosh(4*z)/16
        + (sigma - sp.Rational(1, 2))*E*sp.cosh(2*z)
    )

# Survival equation: zeta=0, eta=0, sigma=1.
assert sp.simplify(sp.trigsimp(V0 - V_ZZ(0, 0, 1))) == 0

# Normalized flux partner: zeta=1/2, eta=1/2, sigma=0.
assert sp.simplify(
    sp.trigsimp(V1 - V_ZZ(sp.Rational(1, 2), sp.Rational(1, 2), 0))
) == 0

# Classical PV parameters from ZZ (7.18):
# alpha=2 eta^2, beta=-2 zeta^2, gamma=2 sigma-1, delta=-1/2.
params0 = (
    2*sp.Rational(0)**2,
    -2*sp.Rational(0)**2,
    2*sp.Rational(1)-1,
    -sp.Rational(1, 2),
)
params1 = (
    2*sp.Rational(1, 2)**2,
    -2*sp.Rational(1, 2)**2,
    2*sp.Rational(0)-1,
    -sp.Rational(1, 2),
)
assert params0 == (0, 0, 1, -sp.Rational(1, 2))
assert params1 == (
    sp.Rational(1, 2),
    -sp.Rational(1, 2),
    -1,
    -sp.Rational(1, 2),
)

# Exact first-order Darboux operator A = d_z + a(z,t).
a = -sp.coth(2*z) + E*sp.sinh(2*z)/2

# For H_j = 1/2 d_z^2 + V_j, the operator identity
#   (d_t-H1) A = A (d_t-H0)
# is equivalent to the two coefficient identities below.
coeff_dz = sp.simplify(sp.trigsimp(V1 - (V0 - sp.diff(a, z))))
coeff_0 = sp.simplify(
    sp.trigsimp(
        sp.diff(a, t)
        + sp.diff(V0, z)
        - sp.diff(a, z, 2)/2
        + a*sp.diff(a, z)
    )
)
assert coeff_dz == 0
assert coeff_0 == 0

# Source-side zero-drift boundary profile:
# U0(x)=1/2+atan(x)/pi, x=sinh(y), hence normalized y-density is sech(y)/pi.
rho0 = 1/(sp.pi*sp.cosh(y))
assert sp.simplify(
    sp.diff(sp.Rational(1, 2) + sp.atan(sp.sinh(y))/sp.pi, y) - rho0
) == 0
# Its total mass is exactly 1.
assert sp.integrate(rho0, (y, -sp.oo, sp.oo)) == 1

print("D0047 QUANTUM-PV NORMALIZATION/DARBOUX EXACT CHECK PASSED")
print("survival classical PV parameters =", params0)
print("flux-partner classical PV parameters =", params1)
print("intertwiner A = d_z - coth(2z) + exp(2t)/2*sinh(2z)")
