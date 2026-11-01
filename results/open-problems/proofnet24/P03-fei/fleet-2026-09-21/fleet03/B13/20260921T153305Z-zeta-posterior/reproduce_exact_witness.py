#!/usr/bin/env python3
"""Reproduce the exact 4-bit Boolean obstruction in REPORT.md.

Standard library only. Exact Fourier-square probabilities use Fraction; floating
point is used only for displayed logarithmic values. The decisive inequality
G_zeta > 3*delta is certified by an integer comparison.
"""
from fractions import Fraction
from math import log2, log
from collections import Counter, defaultdict

M = 4
N = 1 << M
MASK0 = 0x8116
MASK1 = 0x8117


def values(mask):
    return [(-1 if ((mask >> i) & 1) else 1) for i in range(N)]


def fwht_int(a):
    a = list(map(int, a))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def spectrum(mask):
    nums = fwht_int(values(mask))
    p = [Fraction(z * z, N * N) for z in nums]
    assert sum(p) == 1
    return nums, p


def upper(p):
    u = list(p)
    for bit in range(M):
        for A in range(N):
            if not ((A >> bit) & 1):
                u[A] += u[A | (1 << bit)]
    return u


def bcan_float(p):
    u = upper(p)
    return sum(float(x) * log2(float(uu / x)) for x, uu in zip(p, u) if x)


def factor(n):
    out = defaultdict(int)
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] += 1
            n //= d
        d += 1
    if n > 1:
        out[n] += 1
    return dict(out)


def log2_rational_factors(q):
    out = defaultdict(int)
    for p, e in factor(q.numerator).items():
        out[p] += e
    for p, e in factor(q.denominator).items():
        out[p] -= e
    return out


def bcan_symbolic(p):
    u = upper(p)
    coeff = defaultdict(Fraction)
    for x, uu in zip(p, u):
        if not x:
            continue
        for prime, exponent in log2_rational_factors(uu / x).items():
            coeff[prime] += x * exponent
    return dict(coeff)


def subtract_symbols(a, b, scale=Fraction(1, 1)):
    out = defaultdict(Fraction)
    for k, v in a.items():
        out[k] += v
    for k, v in b.items():
        out[k] -= scale * v
    return dict(out)


def eval_symbolic(coeff):
    return sum(float(c) * log2(p) for p, c in coeff.items())


v0, v1 = values(MASK0), values(MASK1)
assert sum(a != b for a, b in zip(v0, v1)) == 1
delta = Fraction(1, N)

w0, p0 = spectrum(MASK0)
w1, p1 = spectrum(MASK1)
assert Counter(map(abs, w0)) == Counter({2: 10, 6: 6})
assert Counter(map(abs, w1)) == Counter({4: 16})  # bent endpoint

mix = [(a + b) / 2 for a, b in zip(p0, p1)]
B0 = bcan_float(p0)
B1 = bcan_float(p1)
BM = bcan_float(mix)
G = BM - (B0 + B1) / 2

s0 = bcan_symbolic(p0)
s1 = bcan_symbolic(p1)
sm = bcan_symbolic(mix)
gap = defaultdict(Fraction)
for k, v in sm.items():
    gap[k] += v
for k, v in s0.items():
    gap[k] -= v / 2
for k, v in s1.items():
    gap[k] -= v / 2
gap = dict(gap)

expected_gap = {
    2: Fraction(21, 128),
    13: Fraction(-13, 128),
    3: Fraction(29, 64),
    5: Fraction(-27, 64),
    11: Fraction(15, 64),
    7: Fraction(-3, 64),
}
assert gap == expected_gap
assert abs(eval_symbolic(gap) - G) < 1e-13

# Exact certificate for G > 3/16 = 3*delta.
# From the symbolic expression, 128*(G-3/16) is
# log2(3^58*11^30 / (2^3*13^13*5^54*7^6)).
lhs = 3**58 * 11**30
rhs = 2**3 * 13**13 * 5**54 * 7**6
assert lhs > rhs

# Also 2/ln(2) < 3 because ln(2) > 2/3. The latter follows from
# d/dx [ln x - 2(x-1)/(x+1)] = (x-1)^2/[x(x+1)^2] > 0 on (1,2].
assert log(2.0) > 2.0 / 3.0

print("masks:", hex(MASK0), hex(MASK1))
print("truth-table Hamming disagreement =", delta)
print("Walsh |numerator| counts endpoint 0:", dict(Counter(map(abs, w0))))
print("Walsh |numerator| counts endpoint 1:", dict(Counter(map(abs, w1))))
print("B_can(P0) =", format(B0, ".17g"))
print("B_can(P1) =", format(B1, ".17g"))
print("B_can(M)  =", format(BM, ".17g"))
print("G_zeta    =", format(G, ".17g"))
print("G_zeta/delta =", format(G / float(delta), ".17g"))
print("2/ln(2)      =", format(2.0 / log(2.0), ".17g"))
print("exact integer certificate lhs > rhs:", lhs > rhs)
print("lhs =", lhs)
print("rhs =", rhs)
