#!/usr/bin/env python3
"""Exact finite checks for the A052 tensor-purity package.

The analytic all-dimension proof is in CRITICAL_SOURCE_STRUCTURE.tex.  This
script checks Walsh/product/restriction identities on genuine Boolean tables,
the exact one-point-defect formulas, and the near-tensor nonfactorization
witnesses.  Decimal entropy output is diagnostic, not an interval certificate.
"""

from fractions import Fraction
from math import log2


def fwht(vals):
    a = list(map(int, vals))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def spectrum(vals):
    n = (len(vals)).bit_length() - 1
    den = 1 << (2 * n)
    return [Fraction(x * x, den) for x in fwht(vals)]


def influence_from_spectrum(vals):
    return sum(p * mask.bit_count() for mask, p in enumerate(spectrum(vals)))


def influence_from_edges(vals):
    n = len(vals).bit_length() - 1
    boundary = 0
    for x in range(1 << n):
        for i in range(n):
            if x < (x ^ (1 << i)) and vals[x] != vals[x ^ (1 << i)]:
                boundary += 1
    return Fraction(boundary, 1 << (n - 1))


def entropy(vals):
    return sum(-float(p) * log2(float(p)) for p in spectrum(vals) if p)


def tensor(f, g):
    return [f[x] * g[y] for y in range(len(g)) for x in range(len(f))]


def row(vals, nx, y):
    return vals[y * (1 << nx):(y + 1) * (1 << nx)]


checks = 0


def check(cond):
    global checks
    assert cond
    checks += 1


# Genuine Boolean tensor identities: OR2-sign table and parity3.
f = [1, -1, -1, -1]
g = [1 if x.bit_count() % 2 == 0 else -1 for x in range(8)]
F = tensor(f, g)
pf, pg, pF = spectrum(f), spectrum(g), spectrum(F)
check(sum(pf) == sum(pg) == sum(pF) == 1)
check(influence_from_spectrum(f) == influence_from_edges(f))
check(influence_from_spectrum(g) == influence_from_edges(g))
check(influence_from_spectrum(F) == influence_from_edges(F))
check(influence_from_spectrum(F) == influence_from_spectrum(f) + influence_from_spectrum(g))
check(abs(entropy(F) - entropy(f) - entropy(g)) < 1e-12)

# Weighted-average algebra over exact rational surrogate H/I data.
Hs = [Fraction(7, 3), Fraction(11, 5), Fraction(13, 7)]
Is = [Fraction(2, 3), Fraction(5, 4), Fraction(9, 5)]
r = sum(Hs) / sum(Is)
check(r == sum((I / sum(Is)) * (H / I) for H, I in zip(Hs, Is)))

# Exact point-defect spectrum and influence for N=2,...,9.
ratios = []
for n in range(2, 10):
    q = [1] * (1 << n)
    q[0] = -1
    p = spectrum(q)
    delta = Fraction(1, 1 << n)
    check(p[0] == (1 - 2 * delta) ** 2)
    check(all(x == 4 * delta * delta for x in p[1:]))
    check(influence_from_spectrum(q) == 2 * n * delta)
    check(influence_from_spectrum(q) == influence_from_edges(q))
    ratios.append(entropy(q) / float(influence_from_spectrum(q)))

# One-point surgery of an arbitrary core: not rank one across old/new blocks.
core = [1, 1, 1, -1]  # nonconstant two-bit core
for n in range(2, 8):
    lifted = core * (1 << n)
    surg = list(lifted)
    surg[0] *= -1
    d = 2 + n
    check(row(surg, 2, 0) != core and row(surg, 2, 0) != [-z for z in core])
    check(row(surg, 2, 1) == core)
    check(abs(influence_from_spectrum(surg) - influence_from_spectrum(core)) <= Fraction(d, 1 << (d - 1)))

print(f"PASS: {checks} exact/algebraic assertions")
print("point-defect H/I for N=2..9:", " ".join(f"{x:.12f}" for x in ratios))
print("scope: finite identity checks only; all-dimension theorem is analytic")
