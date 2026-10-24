#!/usr/bin/env python3
"""Exact arithmetic checks for the B17 AND-slack transport report.

This script checks only the finite rational arithmetic in Sections 3--4.
It consumes the peer-certified strict witness deficit |D| > 0.0176114 as
an input and does not attempt to re-certify the 18-variable Walsh transform.
"""
from fractions import Fraction


def T(x: Fraction) -> Fraction:
    y = 2 * x
    return y if y <= Fraction(1, 2) else 1 - y


def c(x: Fraction) -> Fraction:
    return x * (1 - 2 * x) / 2


y0 = Fraction(57, 1081)
seen = {}
orbit = []
x = y0
while x not in seen:
    seen[x] = len(orbit)
    orbit.append(x)
    x = T(x)

assert x == y0
assert len(orbit) == 253

U_num = sum(Fraction(1, 2**j) * c(y) for j, y in enumerate(orbit))
U = U_num / (1 - Fraction(1, 2**253))

Ua = Fraction(5, 64)
w = Fraction(57, 256)
x = Fraction(1081, 2048)
q = Fraction(1024, 1081)
assert x * q == Fraction(1, 2)
M = x * q * (1 - x) * (1 - q)
assert M == Fraction(55119, 4427776)

kappa = w * Ua + (M + x * U) / q
assert kappa < Fraction(69645, 10**6)

# Account03/B12 rigorously certifies |D| > 0.0176114 for this witness.
deficit_lower = Fraction(176114, 10**7)
Kmin = deficit_lower / kappa
assert Kmin > Fraction(2528769, 10**7)

# Rigorous read-once certificate uses coefficient 0.01; v1 uses 0.268204856.
A = Fraction(268204856, 10**9) - Fraction(1, 100)
assert A == Fraction(32275607, 125000000)
assert Kmin / A > Fraction(9793, 10000)
assert A - Kmin < Fraction(533, 100000)

print("PASS")
print("tent_period =", len(orbit))
print("U_upper = %.17f" % float(U))
print("kappa = %.17f" % float(kappa))
print("kappa_lt = 0.069645")
print("K_required_gt = %.16f" % float(Kmin))
print("guaranteed_AND_bank = %.9f" % float(A))
print("required_bank_fraction_gt = %.9f" % float(Kmin / A))
print("guaranteed_bank_reserve_lt = %.9f" % float(A - Kmin))
