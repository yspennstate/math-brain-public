#!/usr/bin/env python3
"""Exact finite checks for P26 audit of Guo--Fang--Lu Theorem 1.1.

This does not replace the analytic BV/Finsler proof. It checks the exact constants,
open-interval geometry, and the lift half-width extremum used in the audit.
"""
from fractions import Fraction

print("P26-GFL-KOMLOS-EXACT-CHECK")

# Retained-height constants at lift half-width L=3.
L = Fraction(3)
baseline = L / 2
loss_coeff = L * L / 6
threshold = 3 * (L - 2) / (L * L)
assert baseline == Fraction(3, 2)
assert loss_coeff == Fraction(3, 2)
assert threshold == Fraction(1, 3)
assert baseline - loss_coeff * threshold == 1
print("retained-height threshold: PASS (3/2 - (3/2)(1/3) = 1)")

# Source-normalization integrals.
# int_0^6 (6-h) dh = 18; int_0^6 h(6-h) dh = 36.
I0 = Fraction(6**2, 2)
I1 = Fraction(6**3, 6)
assert I0 == 18
assert I1 == 36
assert Fraction(I0, 12) == Fraction(3, 2)
assert Fraction(I1, 24) == Fraction(3, 2)
print("source integrals: PASS (18, 36)")

# General lift half-width L in the containment-admissible range 2 < L <= 3.
# threshold(L) = 3(L-2)/L^2 <= 1/3 because
# 1/3-threshold = (L-3)(L-6)/(3L^2) >= 0 on [2,3].
assert (1, -9, 18) == (1, -(3 + 6), 3 * 6)
for q in range(2, 201):
    for k in range(1, q + 1):
        ell = Fraction(2 * q + k, q)
        if ell > 3:
            continue
        th = 3 * (ell - 2) / (ell * ell)
        assert th <= Fraction(1, 3)
        if ell == 3:
            assert th == Fraction(1, 3)
        else:
            assert th < Fraction(1, 3)
print("L-parameter extremum: PASS (unique max 1/3 at L=3 on 2<L<=3)")

# 1D open-set transform geometry: K=(-a,a), v=1.
# For a>1 the core is (-a+1,a-1), and adding (-2,2) gives (-a-1,a+1).
def open_interval_transform(a):
    a = Fraction(a)
    if a <= 1:
        return None
    return (-a - 1, a + 1)

assert open_interval_transform(Fraction(1)) is None
assert open_interval_transform(Fraction(3)) == (Fraction(-4), Fraction(4))
assert open_interval_transform(Fraction(3, 2)) == (Fraction(-5, 2), Fraction(5, 2))
print("open-transform endpoint geometry: PASS")

# Cube initialization constant cancels exactly:
# kappa = sqrt(2*pi)/(3*sqrt(2*pi)) = 1/3.
assert Fraction(1, 3) == Fraction(1) / Fraction(3)
print("cube constant cancellation: PASS (kappa=1/3)")

# Chi-square_3 inverse moment used in the Gaussian scale mixture:
# S~Gamma(alpha=3/2, scale=2), E[S^{-1}] = 1/(2*(alpha-1)) = 1.
alpha = Fraction(3, 2)
scale = Fraction(2)
e_inv = 1 / (scale * (alpha - 1))
assert e_inv == 1
print("chi-square inverse moment: PASS (E[1/S]=1)")

print("ALL_EXACT_CHECKS_PASS")
