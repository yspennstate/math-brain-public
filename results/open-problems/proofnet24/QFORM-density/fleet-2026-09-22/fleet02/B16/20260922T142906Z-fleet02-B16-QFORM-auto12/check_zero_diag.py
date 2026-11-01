#!/usr/bin/env python3
"""Diagnostic checks for QFORM-ZERODIAG-TRIPLE-PRODUCT-TRACE-v1.

This script is not a proof. It verifies the quoted constants, algebraic identities,
and monotonicity numerically on a wide log grid.
"""

import math
import random


def F(eta: float) -> float:
    return math.log1p(eta) + eta * math.log1p(1.0 / eta)


def edge_bound(a: float, b: float, c: float) -> float:
    return (2.0 / abs(a)) * F(2.0 * abs(a) / math.sqrt(abs(b * c)))


F2 = F(2.0)
C_off = (2.0 ** (4.0 / 3.0)) * F2
assert abs(F2 - 1.9095425048844383) < 1e-15
assert abs(C_off - 4.8117455951457755) < 1e-15

# Check det([[0,a,b],[a,0,c],[b,c,0]]) = 2abc numerically.
for _ in range(1000):
    a, b, c = [random.uniform(-10.0, 10.0) for _ in range(3)]
    if min(abs(a), abs(b), abs(c)) < 1e-6:
        continue
    det = 2.0 * a * b * c
    # Direct 3x3 determinant expansion for the zero-diagonal matrix.
    direct = a * c * b + b * a * c
    assert abs(det - direct) <= 1e-12 * max(1.0, abs(det))

# For product-normalized edge magnitudes abc=1, the minimum of the three
# edge bounds times g should never exceed its symmetric value 2 F(2).
# The proof in REPORT.md is analytic; this is only a broad diagnostic.
max_seen = 0.0
argmax = None
for i in range(-160, 161):
    for j in range(-160, 161):
        a = math.exp(i / 20.0)
        b = math.exp(j / 20.0)
        c = 1.0 / (a * b)
        val = min(edge_bound(a, b, c), edge_bound(b, a, c), edge_bound(c, a, b))
        if val > max_seen:
            max_seen = val
            argmax = (a, b, c)
        assert val <= 2.0 * F2 + 2e-12

# Verify the derivative-sign formula for x>=1 on a log grid.
for k in range(0, 2001):
    x = math.exp(k / 200.0)
    eta = 2.0 * x ** 1.5
    sign_numerator = -math.log1p(eta) + 0.5 * eta * math.log1p(1.0 / eta)
    assert sign_numerator < 0.0

print("PASS")
print(f"F(2)={F2:.16f}")
print(f"C_off={C_off:.16f}")
print(f"max_grid_det_normalized_bound={max_seen:.16f}")
print(f"argmax_grid={argmax}")
