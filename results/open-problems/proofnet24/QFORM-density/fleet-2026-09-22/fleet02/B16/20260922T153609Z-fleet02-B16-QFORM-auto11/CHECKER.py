#!/usr/bin/env python3
"""Diagnostic arithmetic checks for QFORM-INDEFINITE-BINARY-FROSTMAN-v1.

This is not a proof certificate. It checks the scalar inequalities/constants used
in REPORT.md on deterministic grids.
"""
import math


def L_eps(R, eps=1.0):
    if R <= -eps:
        return 0.0
    lo = max(0.0, R-eps)
    hi = max(0.0, R+eps)
    return 2.0*(math.sqrt(hi)-math.sqrt(lo))


def psi(x):
    if x >= 1.0:
        return 1.0
    return x*(1.0+math.log(1.0/x))

# Root-length controls, eps=1 normalization.
mx = (0.0, None)
for i in range(300001):
    R = -1.0 + 31.0*i/300000.0
    L = L_eps(R)
    if L > mx[0]:
        mx = (L, R)
    assert L <= 2.0*math.sqrt(2.0) + 1e-12
    if R > 1.0:
        assert L <= 2.0/math.sqrt(R-1.0) + 1e-12

# Square-preimage interval estimate 2(sqrt(u+H)-sqrt(u)) <= 2sqrt(H).
for iu in range(1001):
    u = 100.0*iu/1000.0
    for j in range(1,301):
        H = 10.0**(-10.0 + 12.0*j/300.0)
        lhs = 2.0*(math.sqrt(u+H)-math.sqrt(u))
        assert lhs <= 2.0*math.sqrt(H) + 1e-12

# Psi(x) <= 3e^{-2/3} x^{2/3}.
c23 = 3.0*math.exp(-2.0/3.0)
for i in range(1,300001):
    x = math.exp(-18.0*i/300000.0)
    assert psi(x) <= c23*x**(2.0/3.0) + 1e-12

K_interval = 2.0*math.sqrt(5.0)
M_star = c23*K_interval**(2.0/3.0)
C_ind = 4.0*math.sqrt(2.0)*M_star**(3.0/4.0)
C_closed = 8.0*3.0**(3.0/4.0)*5.0**(1.0/4.0)/math.sqrt(math.e)
assert abs(C_ind-C_closed) < 1e-13

print("PASS")
print(f"max_L_eps1={mx[0]:.17g} at R={mx[1]:.17g}")
print(f"2sqrt2={2*math.sqrt(2):.17g}")
print(f"K_interval={K_interval:.17g}")
print(f"M_star={M_star:.17g}")
print(f"C_ind={C_ind:.17g}")
print(f"C_ind_closed={C_closed:.17g}")
