#!/usr/bin/env python3
"""Exact finite core for HARD7-06 run 5.

This checks the scalar unweighted hard-field density-evolution surrogate
for unsigned 3-uniform hypergraph 2-coloring.

For x in [0,1], let
  A = 1 - x^2/4,  B = 1 - x^2/2,
and
  F_d(x)=2(A^(d-1)-B^(d-1))/(2 A^(d-1)-B^(d-1)).

At d=6 we certify F_6(x)<x for every x in (0,1] by writing
  x(2A^5-B^5)-2(A^5-B^5) = x(2-x) H(x)/512
and certifying H>0 on [0,1] from a degree-25 Bernstein expansion with
strictly positive rational coefficients.

At d=7 exact rational sign evaluations certify at least two nonzero
fixed points by IVT.
"""
from fractions import Fraction
from math import comb


def padd(a, b):
    n = max(len(a), len(b))
    out = [Fraction(0) for _ in range(n)]
    for i, v in enumerate(a):
        out[i] += v
    for i, v in enumerate(b):
        out[i] += v
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def pscale(a, c):
    return [v * c for v in a]


def pmul(a, b):
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[i + j] += u * v
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def ppow(a, n):
    out = [Fraction(1)]
    for _ in range(n):
        out = pmul(out, a)
    return out


def fmt(q):
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


A = [Fraction(1), Fraction(0), Fraction(-1, 4)]
B = [Fraction(1), Fraction(0), Fraction(-1, 2)]
A5 = ppow(A, 5)
B5 = ppow(B, 5)
D = padd(pscale(A5, 2), pscale(B5, -1))
N = padd(pscale(A5, 2), pscale(B5, -2))
P = padd([Fraction(0)] + D, pscale(N, -1))

# H coefficients, low to high.
H = [
    Fraction(256), Fraction(-512), Fraction(-256), Fraction(832),
    Fraction(96), Fraction(-512), Fraction(-16), Fraction(142),
    Fraction(1), Fraction(-15),
]
rhs = pscale(pmul([Fraction(0), Fraction(2), Fraction(-1)], H), Fraction(1, 512))
assert P == rhs

bern = []
for k in range(26):
    s = Fraction(0)
    for j, aj in enumerate(H):
        if j <= k:
            s += aj * Fraction(comb(k, j), comb(25, j))
    bern.append(s)
assert all(c > 0 for c in bern)


def Ffrac(xx, d):
    AA = 1 - xx * xx / Fraction(4)
    BB = 1 - xx * xx / Fraction(2)
    AP = AA ** (d - 1)
    BP = BB ** (d - 1)
    return Fraction(2) * (AP - BP) / (Fraction(2) * AP - BP)


sign_points = [
    (Fraction(2, 5), -1),
    (Fraction(1, 2), +1),
    (Fraction(9, 10), +1),
    (Fraction(19, 20), -1),
]
sign_values = []
for q, sgn in sign_points:
    v = Ffrac(q, 7) - q
    assert (v > 0) - (v < 0) == sgn
    sign_values.append((q, v))

print("d=6 factorization identity: PASS")
print("H Bernstein degree 25 coefficients:")
print(", ".join(fmt(c) for c in bern))
print("all Bernstein coefficients strictly positive:", all(c > 0 for c in bern))
print("Therefore F_6(x) < x for every 0 < x <= 1.")
print("Since F_d(x) is increasing in d for fixed x in (0,1], the same holds for d<=6.")
print("d=7 exact sign values:")
for q, v in sign_values:
    print(f"F_7({fmt(q)})-{fmt(q)} = {fmt(v)}")
print("IVT intervals with nonzero fixed points: (2/5,1/2) and (9/10,19/20)")
print("ALL_EXACT_CHECKS_PASS")
