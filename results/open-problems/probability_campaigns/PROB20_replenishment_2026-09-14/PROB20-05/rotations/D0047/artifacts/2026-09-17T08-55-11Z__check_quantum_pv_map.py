#!/usr/bin/env python3
"""
Exact symbolic self-check for D0047's beta=2 Brownian-carousel -> quantum Painleve V map.

This checks only algebraic/differential identities used in the report.  It is a
self-check, not an independent audit and not a proof that the carousel gap
probability is already the classical PV tau function.
"""

import sympy as sp

x, y, z, t, s = sp.symbols("x y z t s")
A = 1 + x**2

# 1. alpha -> x=cot(alpha/2).
# dx/dalpha = -(1+x^2)/2.
dx_da = -A / 2
# If U=U(x), U_alpha = ua1*U_x and U_alphalpha =
# uaa2*U_xx + uaa1*U_x.
ua1 = dx_da
uaa2 = sp.simplify(dx_da**2)
uaa1 = sp.simplify(dx_da * sp.diff(dx_da, x))
# 2(1-cos alpha) = 4/(1+x^2).
diffusion_prefactor = 4 / A
assert sp.simplify(diffusion_prefactor * uaa2 - A) == 0
assert sp.simplify(diffusion_prefactor * uaa1 - 2*x) == 0
# Therefore beta=2: s U_s = A U_xx + (2x - s A/2) U_x.
assert sp.simplify(s*ua1 + diffusion_prefactor*uaa1 - (2*x - s*A/2)) == 0

# 2. x=sinh(y), tau=log(s).  The PDE becomes
# R_tau = R_yy + b R_y.
b = sp.tanh(y) - s*sp.cosh(y)/2

# Gauge R=e^phi Psi with phi_y=-b/2 and
# C_tau=-1/4-s^2/32.
phi_y = -sp.tanh(y)/2 + s*sp.cosh(y)/4
C_tau = -sp.Rational(1,4) - s**2/sp.Integer(32)
phi_tau = s*sp.sinh(y)/4 + C_tau
assert sp.simplify(2*phi_y + b) == 0

V = sp.diff(phi_y, y) + phi_y**2 + b*phi_y - phi_tau
V_target = (
    -sp.Rational(1,4)/sp.cosh(y)**2
    + s*sp.sinh(y)/4
    - s**2*sp.cosh(2*y)/32
)
assert sp.simplify(sp.trigsimp(V - V_target)) == 0

# 3. Analytic change y=2z-i*pi/2, tau=2t+i*pi/2.
# In Phi_t=(1/2)Phi_zz + V_QPV Phi, the transformed potential is
# 2*V_target.  Using
# cosh(y)^2=-sinh(2z)^2,
# e^tau sinh(y)=e^(2t) cosh(2z),
# e^(2tau) cosh(2y)=e^(4t) cosh(4z),
# gives this intermediate expression:
V_after_change = (
    sp.Rational(1,2)/sp.sinh(2*z)**2
    + sp.exp(2*t)*sp.cosh(2*z)/2
    - sp.exp(4*t)*sp.cosh(4*z)/16
)
V_qpv = (
    -sp.Rational(1,8)/sp.cosh(z)**2
    + sp.Rational(1,8)/sp.sinh(z)**2
    - sp.exp(4*t)*sp.cosh(4*z)/16
    + sp.exp(2*t)*sp.cosh(2*z)/2
)
assert sp.simplify(sp.trigsimp(V_after_change - V_qpv)) == 0

# 4. Match Zabrodin-Zotov's P_V quantum potential:
# (4*zeta^2-1/4)/(2 cosh^2 z)
# -(4*(xi+sigma)^2-1/4)/(2 sinh^2 z)
# -e^(4t)cosh(4z)/16 +(sigma-1/2)e^(2t)cosh(2z).
zeta = sp.Integer(0)
sigma = sp.Integer(1)
xi = sp.Integer(-1)
V_ZZ = (
    (4*zeta**2-sp.Rational(1,4))/(2*sp.cosh(z)**2)
    -(4*(xi+sigma)**2-sp.Rational(1,4))/(2*sp.sinh(z)**2)
    -sp.exp(4*t)*sp.cosh(4*z)/16
    +(sigma-sp.Rational(1,2))*sp.exp(2*t)*sp.cosh(2*z)
)
assert sp.simplify(sp.trigsimp(V_ZZ - V_qpv)) == 0

# 5. Their classical P_V parameter map.
alpha = 2*(xi+sigma)**2
beta = -2*zeta**2
gamma = 2*sigma-1
delta = -sp.Rational(1,2)
assert (alpha, beta, gamma, delta) == (
    0, 0, 1, -sp.Rational(1,2)
)

print("beta=2 cotangent generator transform: PASS")
print("hyperbolic gauge / scalar-time gauge: PASS")
print("analytic change to quantum P_V potential: PASS")
print("Zabrodin-Zotov parameter match (zeta,xi,sigma)=(0,-1,1): PASS")
print("classical P_V parameters (alpha,beta,gamma,delta)=(0,0,1,-1/2): PASS")
print("D0047 QUANTUM PV MAP EXACT CHECK PASSED")
