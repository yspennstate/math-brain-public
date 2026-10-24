#!/usr/bin/env python3
"""Exact checks for B16 central-Hardy frequency-localization lemmas.

This checks only the new finite algebra. It does not run the FEI
read-once certificate or any prior exhaustive Boolean-function sweep.
"""
from fractions import Fraction
from math import comb
import random

def hard_coeff(r, s):
    return (
        Fraction(16, 1)
        * Fraction(1, 2 ** (r + s + 3))
        / ((r + 2) * (s + 2) * (r + s + 3))
    )

# Lemma 4.1: exact avoidance sum.
avoidance_cases = 0
for n in range(2, 31):
    N = n - 1
    for r in range(0, n):
        lhs = Fraction(0)
        for k in range(1, N - r + 1):
            lhs += Fraction(k + 1, 1) * Fraction(comb(N - r, k), comb(N, k))
        rhs = Fraction((N - r) * (N + r + 3), (r + 1) * (r + 2))
        assert lhs == rhs, (n, r, lhs, rhs)
        avoidance_cases += 1

# Theorem 1.1: compare direct polynomial integration to the Gram formula.
rng = random.Random(20260921)
synthetic_cases = 0
levels = (1, 3, 5, 7)
for _ in range(100):
    a = {r: Fraction(rng.randint(0, 7), 32) for r in levels}
    kappa = {r: Fraction(rng.randint(-8, 8), 5) for r in levels}

    # R A(t) = sum_e coeff[e] t^e.
    coeff = {
        r + 1: -4 * a[r] * kappa[r] / (r + 2)
        for r in levels
    }
    direct = Fraction(0)
    for e, ce in coeff.items():
        for f, cf in coeff.items():
            direct += ce * cf * Fraction(1, (e + f + 1) * 2 ** (e + f + 1))

    gram = Fraction(0)
    for r in levels:
        for s in levels:
            gram += a[r] * a[s] * kappa[r] * kappa[s] * hard_coeff(r, s)

    assert direct == gram, (direct, gram)
    synthetic_cases += 1

# Sharp coefficient constants through a broad exact odd grid.
max_bounded = Fraction(0)
arg_bounded = None
max_hardy = Fraction(0)
arg_hardy = None
coefficient_cases = 0
for r in range(1, 32, 2):
    for s in range(1, 32, 2):
        k = hard_coeff(r, s)
        if k > max_bounded:
            max_bounded = k
            arg_bounded = (r, s)

        scaled = k * (r + 2) * (s + 2) * 2 ** (r - 1) * 2 ** (s - 1)
        if scaled > max_hardy:
            max_hardy = scaled
            arg_hardy = (r, s)
        coefficient_cases += 1

assert max_bounded == Fraction(1, 90)
assert arg_bounded == (1, 1)
assert max_hardy == Fraction(1, 10)
assert arg_hardy == (1, 1)

print("PASS")
print("avoidance_identity_cases", avoidance_cases)
print("synthetic_gram_cases", synthetic_cases)
print("coefficient_grid_cases", coefficient_cases)
print("max_bounded", f"{max_bounded.numerator}/{max_bounded.denominator}", arg_bounded)
print("max_hardy_scaled", f"{max_hardy.numerator}/{max_hardy.denominator}", arg_hardy)
