#!/usr/bin/env python3
"""Exact Walsh checks for the A067 Boolean degree/granularity refinement."""

from fractions import Fraction
from itertools import product
from math import log2


def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def entropy_from_walsh(w, n):
    den = 1 << (2 * n)
    ans = 0.0
    for z in w:
        if z:
            p = z * z / den
            ans += p * log2(1.0 / p)
    return ans


assertions = 0
failures = 0
tables = 0
nonconstant = 0
max_slack = 0.0

for n in range(1, 5):
    N = 1 << n
    for bits in range(1 << N):
        f = [1 if (bits >> x) & 1 else -1 for x in range(N)]
        w = fwht(f)
        tables += 1

        # Parseval in integer normalization.
        assertions += 1
        if sum(z * z for z in w) != N * N:
            failures += 1

        degree = max((s.bit_count() for s, z in enumerate(w) if z), default=0)
        if degree == 0:
            continue
        nonconstant += 1

        divisor = 1 << (n + 1 - degree)
        assertions += 1
        if any(z % divisor for z in w):
            failures += 1

        den = N * N
        v = Fraction(den - w[0] * w[0], den)
        infl = sum(Fraction(s.bit_count() * z * z, den) for s, z in enumerate(w))
        assertions += 1
        if v > infl:
            failures += 1

        H = entropy_from_walsh(w, n)
        empty_term = 0.0
        if w[0]:
            p0 = w[0] * w[0] / den
            empty_term = p0 * log2(1.0 / p0)
        sharp_bound = 2 * (degree - 1) * float(v) + empty_term
        fei_bound = (2 * (degree - 1) + log2(2.718281828459045)) * float(infl)
        assertions += 2
        if H > sharp_bound + 2e-12:
            failures += 1
        if H > fei_bound + 2e-12:
            failures += 1
        max_slack = max(max_slack, sharp_bound - H)


print("Arithmetic: integer FWHT + fractions.Fraction; floats only for log2 diagnostics")
print("Random seed: NONE")
print(f"Boolean truth tables exhausted: {tables}")
print(f"Nonconstant truth tables: {nonconstant}")
print("Maximum dimension: 4")
print(f"Assertions passed: {assertions - failures}")
print(f"Assertions failed: {failures}")

print("AND/point-defect controls:")
for d in range(2, 13):
    mu = 2.0 ** (-d)
    I = 2.0 * d * mu
    p0 = (1.0 - 2.0 * mu) ** 2
    q = 4.0 * mu * mu
    H = p0 * log2(1.0 / p0) + (2**d - 1) * q * log2(1.0 / q)
    old_support_coefficient = d / I
    new_coefficient = 2 * (d - 1) + log2(2.718281828459045)
    print(
        f"d={d:2d} H/I={H/I:.12f} old_support/I={old_support_coefficient:.6f} "
        f"new_Cd={new_coefficient:.6f}"
    )

print("Fixed-Renyi point-defect controls at alpha=3/4:")
alpha = 0.75
for d in (4, 8, 12, 16):
    mu = 2.0 ** (-d)
    I = 2.0 * d * mu
    Z = (1 - 2 * mu) ** (2 * alpha) + (2**d - 1) * (4 * mu * mu) ** alpha
    H_alpha = log2(Z) / (1 - alpha)
    print(f"d={d:2d} H_alpha/I={H_alpha/I:.12f}")

eps2 = 2.0 ** (-20)
near_boolean_ratio = (-(1-eps2)*log2(1-eps2)-eps2*log2(eps2))/eps2
print(f"Near-Boolean real degree-1 control H/I at epsilon^2=2^-20: {near_boolean_ratio:.12f}")

if failures:
    raise SystemExit(1)
print("ALL_A067_BOOLEAN_GRANULARITY_CHECKS_PASS")
