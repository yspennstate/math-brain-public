#!/usr/bin/env python3
"""Exact checks for B17 true-stall / exception-ladder FEI constructions.

All Walsh coefficients and influences are computed with Fraction. Entropy
comparisons are numerical sanity checks only; the report contains the universal
analytic H<4J proof for the true-stall family.
"""
from fractions import Fraction
from math import log2

def bits(i, n):
    return tuple((i >> k) & 1 for k in range(n))

def fwht(vals):
    a = [Fraction(v) for v in vals]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [x / n for x in a]

def influence(vals, coord):
    n = len(vals)
    return Fraction(sum(vals[x] != vals[x ^ (1 << coord)] for x in range(n)), n)

def spectral_influence(hat, n):
    return sum((sum((s >> i) & 1 for i in range(n)) * a * a
                for s, a in enumerate(hat)), Fraction(0))

def entropy(hat):
    out = 0.0
    for a in hat:
        p = float(a*a)
        if p:
            out += p * log2(1.0/p)
    return out

def star(r, m):
    vals = []
    for idx in range(1 << (r+m)):
        x = bits(idx, r)
        y = tuple((idx >> (r+i)) & 1 for i in range(m))
        vals.append(-1 if (all(v == 0 for v in x) and (sum(y) & 1)) else 1)
    return vals

def true_stall(r, m):
    vals = []
    for idx in range(1 << (r+m)):
        x = bits(idx, r)
        y = tuple((idx >> (r+i)) & 1 for i in range(m))
        f = -1 if (all(v == 0 for v in x) and (sum(y) & 1)) else 1
        h = -1 if all(v == 1 for v in x) else 1
        vals.append(f*h)
    return vals

# Base star: every coordinate has influence q.
for r in range(1, 5):
    for m in range(1, 5):
        q = Fraction(1, 2**r)
        vals = star(r, m)
        infl = [influence(vals, i) for i in range(r+m)]
        assert infl == [q] * (r+m)
        hat = fwht(vals)
        assert spectral_influence(hat, r+m) == sum(infl)
        assert entropy(hat) < 4.0 * float(sum(infl))
print("STAR_WALSH_INFLUENCE_H_LT_4J_PASS")

# r=1, m>=2: certified y rows use Z={x} and pay exactly, but x is
# not C12-certified. For any codimension-one atom y_k=b, parity(y)=1
# differs on exactly half the y cube when m>=2.
for m in range(2, 9):
    vals = star(1, m)
    assert [influence(vals, i) for i in range(m+1)] == [Fraction(1,2)]*(m+1)
    for k in range(m):
        for b in (0,1):
            diff = Fraction(sum(
                ((sum(bits(y,m)) & 1) == 1) != (((y >> k) & 1) == b)
                for y in range(1 << m)), 1 << m)
            assert diff == Fraction(1,2)
print("CLOSED_KERNEL_FALSE_POSITIVE_DIRECT_PAID_ROWS_PASS")

# True-stall family: pivots have influence q; controls have 3q. The exact
# nonzero Fourier magnitudes have counts predicted in the report.
for r in range(3, 5):
    for m in range(2, 5):
        q = Fraction(1, 2**r)
        vals = true_stall(r, m)
        infl = [influence(vals, i) for i in range(r+m)]
        assert infl[:r] == [3*q]*r
        assert infl[r:] == [q]*m
        hat = fwht(vals)
        counts = {}
        for a in hat:
            counts[abs(a)] = counts.get(abs(a), 0) + 1
        assert counts[1-3*q] == 1
        assert counts[q] == 3 * 2**(r-1)
        assert counts[3*q] == 2**(r-1)-1
        assert spectral_influence(hat, r+m) == q*(3*r+m)
        assert entropy(hat) < 4.0 * float(q*(3*r+m))
print("TRUE_STALL_SPECTRUM_AND_H_LT_4J_PASS")
