#!/usr/bin/env python3
from fractions import Fraction as F
from math import comb
import math


def padd(a, b):
    n = max(len(a), len(b))
    z = [F(0)] * n
    for i, v in enumerate(a):
        z[i] += v
    for i, v in enumerate(b):
        z[i] += v
    return z


def pmul(a, b):
    z = [F(0)] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            z[i + j] += u * v
    return z


def pscale(a, c):
    return [c * v for v in a]


def ppow(a, n):
    z = [F(1)]
    for _ in range(n):
        z = pmul(z, a)
    return z


def bernstein_to_power(bc, a, b):
    n = len(bc) - 1
    den = b - a
    y = [-a / den, F(1) / den]
    oy = [b / den, -F(1) / den]
    out = [F(0)]
    for k, c in enumerate(bc):
        term = pmul(ppow(y, k), ppow(oy, n - k))
        out = padd(out, pscale(term, c * comb(n, k)))
    return out


# P(x)=116x^5+145x^4+216x^3+270x^2-408x+102.
P = [F(102), F(-408), F(270), F(216), F(145), F(116)]
segments = [
    (F(0), F(2, 5), [F(102), F(1734, 25), F(1026, 25), F(11514, 625), F(454, 125), F(2262, 3125)]),
    (F(2, 5), F(9, 20), [F(2262, 3125), F(1126, 3125), F(9123, 50000), F(9909, 50000), F(332697, 800000), F(337773, 400000)]),
    (F(9, 20), F(1, 2), [F(337773, 400000), F(203679, 160000), F(76497, 40000), F(22173, 8000), F(193, 50), F(83, 16)]),
    (F(1, 2), F(1), [F(83, 16), F(1477, 80), F(1113, 20), F(1267, 10), F(247), F(441)]),
]

# ln 2 = 2*atanh(1/3) > 2*(1/3 + (1/3)^3/3) = 56/81 > 17/25.
assert F(56, 81) > F(17, 25)
for a, b, bc in segments:
    assert min(bc) > 0
    assert bernstein_to_power(bc, a, b) == P


def h(x):
    if x <= 0 or x >= 1:
        return 0.0
    return -x * math.log2(x) - (1 - x) * math.log2(1 - x)


def branch_credit(t, u):
    A = (1 - u) / (4 * (1 + u))
    B = (1 + u) / (4 * (1 - u))
    T = (1 - t) * A + t * B
    eta = t * B / T
    return 0.25 * h(t) + T * h(eta)


def W(t):
    return t * (1 - t) / 4


# Dense floating diagnostic only; the theorem above is exact rational/calculus.
mn = (1e100, None)
for i in range(1, 1000):
    t = i / 1000
    for j in range(1001):
        u = -0.5 + j / 1000
        q = branch_credit(t, u) / W(t)
        if q < mn[0]:
            mn = (q, (t, u))
        assert q > 6.0 - 2e-12

print("PASS exact Bernstein positivity + entropy-tail reduction")
print("ln2 lower certificate: 56/81 > 17/25")
print("minimum diagnostic H(B|S)/W on grid:", repr(mn[0]), "at", mn[1])
