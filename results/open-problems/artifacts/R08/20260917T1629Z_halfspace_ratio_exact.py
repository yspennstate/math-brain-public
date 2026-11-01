#!/usr/bin/env python3
"""Exact symbolic self-check for R08 F0083 half-space boundary asymptotics.

This checks only the finite algebraic core used in the accompanying proof:
(1) the negative and positive corner integrals;
(2) the homogeneous ratio equation and its factorization;
(3) strict monotonicity/sign data implying one root in (0,1).
It does not certify the infinite-dimensional stable-allocation theorem.
"""
import sympy as sp

S, d, D, lam = sp.symbols("S d D lam", positive=True)
mid = (D + d) / 2

negative = sp.integrate(2 * (S - d) * (S**2 / 2), (S, 0, d))
positive = (
    sp.integrate((S - d) * (S**2 / 2), (S, d, mid))
    + sp.integrate((D - S) * (S**2 / 2), (S, mid, D))
)
positive_closed = (D - d)**2 * (7*D**2 + 10*D*d + 7*d**2) / sp.Integer(192)

assert sp.simplify(negative + d**4 / 12) == 0
assert sp.simplify(positive - positive_closed) == 0

ratio_eq = sp.expand((1-lam)**2 * (7 + 10*lam + 7*lam**2) - 16*lam**4)
factor_target = sp.expand(-(lam + 1) * (9*lam**3 - 5*lam**2 + 11*lam - 7))
assert sp.expand(ratio_eq - factor_target) == 0

P = 9*lam**3 - 5*lam**2 + 11*lam - 7
Pprime = sp.diff(P, lam)
disc = sp.discriminant(Pprime, lam)
assert disc == -1088
assert P.subs(lam, 0) == -7
assert P.subs(lam, 1) == 8
# P' has positive leading coefficient and negative discriminant, hence P'>0 on R.
assert sp.LC(sp.Poly(Pprime, lam)) > 0

roots = sp.nroots(P, n=30, maxsteps=100)
real_root = [r for r in roots if abs(sp.im(r)) < sp.Float("1e-25")]
assert len(real_root) == 1
root = sp.re(real_root[0])
assert 0 < root < 1

print("PASS exact symbolic checks")
print("negative_corner_integral =", sp.factor(negative))
print("positive_corner_integral =", sp.factor(positive))
print("ratio_factorization =", sp.factor(ratio_eq))
print("Pprime_discriminant =", disc)
print("P(0) =", P.subs(lam, 0), "P(1) =", P.subs(lam, 1))
print("lambda_star ~=", sp.N(root, 16))
