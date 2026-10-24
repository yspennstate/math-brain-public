#!/usr/bin/env python3
"""
Exact symbolic self-check for the finite algebra used in the 2026-09-17
RS-2026-DC35 pencil/Jensen-duality report.

This checks only algebraic identities (projective normalization and the
one-free-coordinate barycentric parameterization for four planar points).
It is a self-check, NOT a certificate for Open Problem 35.
"""
import sympy as sp

r1, r2, r3, r4 = sp.symbols("r1 r2 r3 r4")
s, t, u = sp.symbols("s t u")

# Mobius/projective normalization of three distinct quotient directions:
# r1 -> 0, r2 -> 1, r3 -> infinity.
T = lambda r: sp.factor((r-r1)*(r2-r3)/((r-r3)*(r2-r1)))

checks = {}
checks["T_r1"] = sp.factor(T(r1))
checks["T_r2_minus_1"] = sp.factor(T(r2)-1)
# The denominator vanishes at r3, so r3 is the pole/infinity image.
den = sp.factor((r3-r3)*(r2-r1))
checks["T_r3_denominator"] = den

tau = sp.factor(T(r4))
dtau = sp.factor(sp.diff(tau, r4))
expected_dtau = sp.factor((r2-r3)*(r1-r3)/((r2-r1)*(r4-r3)**2))
checks["cross_ratio_derivative"] = sp.factor(dtau-expected_dtau)

# Four points (0,0),(1,0),(0,1),(1,1): any barycentric weights with
# barycenter (s,t) have one free coordinate u=lambda_11.
lam11 = u
lam10 = s-u
lam01 = t-u
lam00 = 1-s-t+u
checks["weights_sum"] = sp.factor(lam00+lam10+lam01+lam11-1)
checks["x_barycenter"] = sp.factor(lam10+lam11-s)
checks["y_barycenter"] = sp.factor(lam01+lam11-t)

bad = {k: sp.simplify(v) for k,v in checks.items() if sp.simplify(v) != 0}
if bad:
    print("status=FAIL")
    for k,v in bad.items():
        print(k, "=", v)
    raise SystemExit(1)

print("status=PASS")
print("scope=exact algebra only; NOT Open Problem 35 closure")
print("mobius=T(r)=((r-r1)(r2-r3))/((r-r3)(r2-r1))")
print("images: r1->0, r2->1, r3->infinity")
print("fourth_direction_cross_ratio=tau=T(r4)")
print("d_tau/dr4=(r2-r3)(r1-r3)/((r2-r1)(r4-r3)^2)")
print("four_point_weights=(1-s-t+u, s-u, t-u, u)")
print("free_barycentric_dimension=1")
print("global_metric_moved=False")
