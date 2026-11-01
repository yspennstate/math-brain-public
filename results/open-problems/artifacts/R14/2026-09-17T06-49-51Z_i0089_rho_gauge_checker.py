#!/usr/bin/env python3
"""Exact symbolic bookkeeping for R14/I0089 background-gauge obstruction.

This checker only verifies the finite algebraic cancellation obtained by combining
Lewin's Jellium energy (50) with the outside potential in (82). It does not
formalize the source semantics of 'a similar definition using Theorem 28'.
"""
import sympy as sp

rho, J, c, mu = sp.symbols("rho J c mu")
phiY, crossY, pairY, IY = sp.symbols("phiY crossY pairY IY")
phiX, crossX, pairX, IX = sp.symbols("phiX crossX pairX IX")
n, N = sp.symbols("n N", integer=True)

# For a trial configuration Y in D:
#   sum_Y Phi_{D^c} = phiY - crossY + rho*IY
# and by source eq. (50)
#   E_s(Y,D,rho) = pairY - rho*IY + rho^2*J/2.
# The same bookkeeping applies to the incumbent X_D, with regularized self terms.
LY = phiY - crossY + rho*IY + pairY - rho*IY + rho**2*J/2
LX = phiX - crossX + rho*IX + pairX - rho*IX + rho**2*J/2

LYs = sp.simplify(LY)
LXs = sp.simplify(LX)
delta = sp.simplify(LY - LX)

print("R14/I0089 exact rho-gauge bookkeeping")
print("LY simplified =", LYs)
print("LX simplified =", LXs)
print("DLR comparison difference =", delta)
print("d/drho of comparison difference =", sp.diff(delta, rho))
assert sp.diff(delta, rho) == 0

# Source also says Phi is only defined up to an additive constant, at the
# expense of shifting mu. Verify the exact sign convention for (82):
#   LY >= LX + mu*(n-N).
# If Phi -> Phi+c then LY -> LY+c*n and LX -> LX+c*N, so mu -> mu+c.
mu2 = mu + c
shifted_residual = sp.expand((LY + c*n) - (LX + c*N) - mu2*(n-N))
original_residual = sp.expand(LY - LX - mu*(n-N))
print("Phi/mu gauge residual difference =", sp.simplify(shifted_residual-original_residual))
assert sp.simplify(shifted_residual-original_residual) == 0

print("ALL_SYMBOLIC_CHECKS_PASS")
