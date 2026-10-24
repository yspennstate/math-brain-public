#!/usr/bin/env python3
"""Independent exact audit of the B05 k=4 Boolean witness.

This reconstructs G,H from truth tables, performs an integer FWHT, and does
not use B05's four packet-multiplicity formulas.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
import platform


def fwht(values):
    out = list(values)
    h = 1
    while h < len(out):
        for i in range(0, len(out), 2 * h):
            for j in range(i, i + h):
                x, y = out[j], out[j + h]
                out[j], out[j + h] = x + y, x - y
        h *= 2
    return out


def bent(x, k):
    exponent = 0
    for i in range(0, k, 2):
        exponent ^= ((x >> i) & 1) & ((x >> (i + 1)) & 1)
    return -1 if exponent else 1


def children(k):
    r = 2 * k
    vals_g, vals_h = [], []
    for w in range(1 << (k + r)):
        x = w & ((1 << k) - 1)
        z = w >> k
        if z == 0:
            g = bent(x, k)
            h = -1 if x == 0 else g
        else:
            g = h = 1
        vals_g.append(g)
        vals_h.append(h)
    return vals_g, vals_h


def influence(values, coordinate):
    n = len(values).bit_length() - 1
    disagreements = sum(values[x] != values[x ^ (1 << coordinate)] for x in range(1 << n))
    return Fraction(disagreements, 1 << n)


getcontext().prec = 80
checks = 0


def check(condition):
    global checks
    assert condition
    checks += 1


k = 4
delta = Fraction(1, 1 << k)
d = Fraction(1, 1 << (3 * k))
g, h = children(k)
nres = 3 * k
N = 1 << nres
check(len(g) == N)
check(sum(x != y for x, y in zip(g, h)) == 1)

wg, wh = fwht(g), fwht(h)
sum_q = Fraction(0)
sum_e = Fraction(0)
second = Fraction(0)
max_theta = Fraction(0)
L = Decimal(0)
for A, B in zip(wg, wh):
    q = Fraction(A * A + B * B, 2 * N * N)
    e = Fraction((A - B) * (A - B), 4 * N * N)
    theta = e / q
    check(A - B == 2)
    check(q > 0)
    check(e == d * d)
    check(theta <= 4 * delta)
    sum_q += q
    sum_e += e
    second += q * theta * theta
    max_theta = max(max_theta, theta)
    td = Decimal(theta.numerator) / Decimal(theta.denominator)
    qd = Decimal(q.numerator) / Decimal(q.denominator)
    L += qd * (-(td * td.ln() + (Decimal(1) - td) * (Decimal(1) - td).ln()) / Decimal(2).ln())

check(sum_q == 1)
check(sum_e == d)
V = second - d * d
check(V <= 4 * delta * d)
check(max_theta <= 4 * delta)

diffs = []
for i in range(nres):
    ig = influence(g, i)
    ih = influence(h, i)
    check(ih - ig == 2 * d)
    diffs.append(ih - ig)
M = sum(x * x for x in diffs)
check(M == 12 * k * d * d)

lower = (1 - delta) * (k - 2) * d
lower_dec = Decimal(lower.numerator) / Decimal(lower.denominator)
check(L >= lower_dec)

print(f"Python: {platform.python_version()}")
print("Method: exact truth tables + integer FWHT + Fraction; Decimal(80) only for entropy")
print("Randomness: NONE")
print("Seed: NOT_APPLICABLE")
print(f"Residual dimension: {nres}")
print(f"Truth-table points: {N}")
print(f"Packets checked: {N}")
print(f"sum_q: {sum_q}")
print(f"sum_e: {sum_e}")
print(f"max_theta: {max_theta}")
print(f"V: {V}")
print(f"M: {M}")
print(f"L/d: {L / (Decimal(d.numerator) / Decimal(d.denominator))}")
print(f"lower/d: {lower / d}")
print(f"Assertions: {checks}")
print(f"Passed: {checks}")
print("Failed: 0")
print("STATUS=PASS")
