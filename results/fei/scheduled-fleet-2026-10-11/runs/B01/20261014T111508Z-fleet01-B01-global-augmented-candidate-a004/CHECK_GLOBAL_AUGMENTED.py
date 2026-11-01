#!/usr/bin/env python3
"""Targeted test of M+2U+2Phi <= (29/2+2/ln2) I.

Walsh coefficients and influence are exact Fractions. Entropic quantities are
evaluated in binary64 only for discovery; a positive margin is not certified
by this script.
"""
from fractions import Fraction
from math import log, log2
from random import Random
from time import monotonic


def xr(x, y):
    return 0.0 if x == 0 else float(x) * log2(float(y / x))


def T(a, b):
    return xr(a, a + b) + xr(b, a + b)


def fwht(v):
    a = [Fraction(x) for x in v]
    h = 1
    while h < len(a):
        for j in range(0, len(a), 2 * h):
            for k in range(j, j + h):
                x, y = a[k], a[k + h]
                a[k], a[k + h] = x + y, x - y
        h *= 2
    return [x / len(a) for x in a]


def caps(p):
    a = list(p)
    n = len(a).bit_length() - 1
    for i in range(n):
        bit = 1 << i
        for s in range(len(a)):
            if not s & bit:
                a[s] += a[s | bit]
    return a


def restrict(v, i, bit):
    n = len(v).bit_length() - 1
    out = []
    for z in range(1 << (n - 1)):
        lo = z & ((1 << i) - 1)
        hi = z >> i
        out.append(v[lo | (bit << i) | (hi << (i + 1))])
    return tuple(out)


def basic(v):
    h = fwht(v)
    p = [x * x for x in h]
    pi = caps(p)
    U = sum(xr(x, y) for x, y in zip(p, pi))
    I = sum(s.bit_count() * x for s, x in enumerate(p))
    B = 0.0
    n = len(v).bit_length() - 1
    for i in range(n):
        bit = 1 << i
        for s in range(len(p)):
            if not s & bit:
                B += T(p[s], p[s | bit])
    return U, I, B, p


def q(t):
    return 0.0 if t == 0 else t * log2(1 / t) + 2 * t / log(2)


def stats(v):
    U, I, B, p = basic(v)
    n = len(v).bit_length() - 1
    G = n * U
    for i in range(n):
        G -= 0.5 * basic(restrict(v, i, 0))[0]
        G -= 0.5 * basic(restrict(v, i, 1))[0]
    M = G - B
    Phi = sum(q(float(p[1 << i])) for i in range(n))
    c = Fraction(29, 2)
    c_float = float(c) + 2 / log(2)
    raw = M + 2 * U + 2 * Phi
    residual = raw - c_float * float(I)
    ratio = raw / float(I) if I else 0.0
    return dict(U=U, I=I, B=B, G=G, M=M, Phi=Phi,
                raw=raw, residual=residual, ratio=ratio)


def truth_from_mask(n, mask):
    return tuple(-1 if (mask >> x) & 1 else 1 for x in range(1 << n))


def point_defect(n):
    return tuple(-1 if x == 0 else 1 for x in range(1 << n))


def parity(n, subset=None):
    if subset is None:
        subset = (1 << n) - 1
    return tuple(-1 if (x & subset).bit_count() & 1 else 1
                 for x in range(1 << n))


def report(tag, n, ident, s):
    return (s["residual"], tag, n, ident, s["ratio"], s["G"],
            float(s["I"]), s["U"], s["M"], s["Phi"])


start = monotonic()
best = (-1e100,)
best_nonconstant = (-1e100,)
counts = {}

for n in range(1, 5):
    # Complement invariance fixes truth[2^n-1]=+1, hence 2^(2^n-1) masks.
    total = 1 << ((1 << n) - 1)
    for mask in range(total):
        v = truth_from_mask(n, mask)
        s = stats(v)
        r = report("exhaustive", n, mask, s)
        if r > best:
            best = r
        if s["I"] and r > best_nonconstant:
            best_nonconstant = r
    counts[f"exhaustive_n{n}"] = total

rng = Random(20261014111508)
for n in range(5, 10):
    total = 200 if n <= 7 else 50
    for k in range(total):
        v = tuple(1 if rng.getrandbits(1) else -1 for _ in range(1 << n))
        s = stats(v)
        r = report("random", n, k, s)
        if r > best:
            best = r
        if s["I"] and r > best_nonconstant:
            best_nonconstant = r
    counts[f"random_n{n}"] = total

for n in range(1, 13):
    for tag, v in (("point_defect", point_defect(n)),
                   ("full_parity", parity(n)),
                   ("dictator", parity(n, 1))):
        s = stats(v)
        r = report(tag, n, None, s)
        if r > best:
            best = r
        if s["I"] and r > best_nonconstant:
            best_nonconstant = r
    counts[f"structured_n{n}"] = 3

print("candidate=M+2U+2Phi<=(29/2+2/ln2)I")
print("constant=", 29 / 2 + 2 / log(2))
print("counts=", counts)
print("best=(residual,tag,n,id,ratio,G,I,U,M,Phi)=", best)
print("best_nonconstant=", best_nonconstant)
print("status=", "FAIL_DISCOVERY" if best[0] > 1e-9 else "NO_COUNTEREXAMPLE")
print("elapsed_seconds=", monotonic() - start)
