#!/usr/bin/env python3
"""Exact/diagnostic checks for B11 A053 critical near-tensor separation."""

from fractions import Fraction
from itertools import product
from math import log2


def walsh(values):
    n = (len(values)).bit_length() - 1
    out = []
    for mask in range(1 << n):
        total = 0
        for x, value in enumerate(values):
            parity = (mask & x).bit_count() & 1
            total += value * (-1 if parity else 1)
        out.append(Fraction(total, 1 << n))
    return out


def influence(values, i):
    n = (len(values)).bit_length() - 1
    return Fraction(sum(values[x] != values[x ^ (1 << i)] for x in range(1 << n)), 1 << n)


assertions = 0

# Six-bit one-point defect: -1 at zero, +1 elsewhere.
phi = [-1] + [1] * 63
hat = walsh(phi)
assert hat[0] == Fraction(31, 32); assertions += 1
for c in hat[1:]:
    assert abs(c) == Fraction(1, 32); assertions += 1
assert sum(c * c for c in hat) == 1; assertions += 1

infs = [influence(phi, i) for i in range(6)]
for x in infs:
    assert x == Fraction(1, 32); assertions += 1
assert sum(infs) == Fraction(3, 16); assertions += 1

# The analytic proof gives H(phi)<1449/2048 and 4I(phi)=1536/2048.
assert Fraction(3, 4) - Fraction(1449, 2048) == Fraction(87, 2048); assertions += 1
assert Fraction(66, 2048) < Fraction(87, 2048); assertions += 1

# Exact rational part of the explicit continuity budget.
for N in range(6, 257):
    eps = Fraction(1, (1 << 18) * N * N)
    t = Fraction(1, 256 * N)
    # Rational majorants used in the proof.
    entropy_modulus_majorant = Fraction(3, 128)
    linear_transport = (2 * N - 6) * t
    influence_transport = 48 * eps
    assert linear_transport <= Fraction(1, 128); assertions += 1
    assert influence_transport < Fraction(1, 1024); assertions += 1
    assert entropy_modulus_majorant + linear_transport + influence_transport < Fraction(87, 2048); assertions += 1

# One-point-surgery family: 2^{-N} lies inside the certified radius for N=6m, m>=5.
for m in range(5, 41):
    N = 6 * m
    assert Fraction(1, 1 << N) <= Fraction(1, (1 << 18) * N * N); assertions += 1

# Diagnostics only: direct entropy and first excluded family member.
H_phi = -(31/32)**2 * log2((31/32)**2) - 63 * (1/32)**2 * log2((1/32)**2)
R_phi = H_phi / (3/16)
assert H_phi < 1449/2048; assertions += 1
assert R_phi < 4; assertions += 1

print("PASS")
print(f"exact_assertions={assertions}")
print("arithmetic=Fraction for Walsh, influence, and certified margins")
print("random_seed=None")
print(f"H_phi_diagnostic={H_phi:.15f}")
print(f"R_phi_diagnostic={R_phi:.15f}")
print("certified_point_defect_gap_gt=87/2048")
print("certified_radius=1/(2^18*N^2)")
print("one_point_surgery_excluded_for=N=6m,m>=5")
