#!/usr/bin/env python3
"""Finite audit for the singleton-potential GU' transfer theorem.

The all-dimensional statement is analytic in PROOF.md.  This checker verifies
the scalar inequalities, reconstructs U,G,I,Phi from Boolean truth tables, and
tests product/activation/restriction closure on small generated instances.
"""

from fractions import Fraction
from math import log, log2
import itertools
import random

SEED = 0xB01A003F
rng = random.Random(SEED)
TOL = 2e-9
LN2 = log(2.0)
L = 1.0 / LN2
M = 2.0 / LN2
RHO = (1.0 + LN2) / 4.0
LAM = 4.0 / (1.0 - LN2)
ADDED = LAM * M


def fwht(vals):
    a = [Fraction(v) for v in vals]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return [x / len(a) for x in a]


def caps(p):
    c = list(p)
    n = len(c).bit_length() - 1
    for j in range(n):
        bit = 1 << j
        for s in range(1 << n):
            if not s & bit:
                c[s] += c[s | bit]
    return c


def U(f):
    p = [x * x for x in fwht(f)]
    c = caps(p)
    return sum(float(x) * log2(float(y / x)) for x, y in zip(p, c) if x)


def restrict(f, j, b):
    n = len(f).bit_length() - 1
    out = []
    for z in range(1 << (n - 1)):
        lo = z & ((1 << j) - 1)
        hi = z >> j
        out.append(f[lo | (b << j) | (hi << (j + 1))])
    return tuple(out)


def influence(f):
    n = len(f).bit_length() - 1
    return sum(
        (Fraction(sum(f[x] != f[x ^ (1 << j)] for x in range(len(f))), len(f))
         for j in range(n)),
        Fraction(0),
    )


def G(f):
    root = U(f)
    n = len(f).bit_length() - 1
    return sum(root - (U(restrict(f, j, 0)) + U(restrict(f, j, 1))) / 2
               for j in range(n))


def phi(x):
    x = abs(float(x))
    if x == 0.0:
        return 0.0
    return 2.0 * x * x * (log2(1.0 / x) + L)


def Phi(f):
    hats = fwht(f)
    n = len(f).bit_length() - 1
    return sum(phi(hats[1 << j]) for j in range(n))


def mean(f):
    return Fraction(sum(f), len(f))


def product(f, g):
    return tuple(f[x] * g[y] for y in range(len(g)) for x in range(len(f)))


def activate(q):
    return tuple(q[x >> 1] if not (x & 1) else 1 for x in range(2 * len(q)))


def point_defect(r, sign=1):
    q = [sign] * (1 << r)
    q[-1] = -sign
    return tuple(q)


def zlog(x):
    return 0.0 if x == 0.0 else x * log2(1.0 / x)


def R(t):
    x = (1.0 + t) ** 2 / 4.0
    y = (1.0 - t) ** 2 / 4.0
    e = zlog(x) + (0.0 if y == 0.0 else y * log2(2.0 / (1.0 - t)))
    u = 0.0 if t == 0.0 else t * t * log2(1.0 / (t * t))
    return e - u / 2.0 + (1.0 - t * t) / 4.0


def R2(t):
    return 1.0 + (log(t * t / ((1.0 + t) * (1.0 - t) ** 0.5)) + 0.75) / LN2


def qstats(r):
    if r == 1:
        return 0.0, 0.0, 1.0, 0.0
    p = 2.0 ** (-r)
    beta = 1.0 - 2.0 * p
    uq = zlog(beta * beta) + 2.0 * r * p * beta
    iq = 2.0 * r * p
    if r == 2:
        gq = 2.0
    else:
        pp = 2.0 ** (-(r - 1))
        bp = 1.0 - 2.0 * pp
        up = zlog(bp * bp) + 2.0 * (r - 1) * pp * bp if bp else 0.0
        gq = r * (uq - up / 2.0)
    return beta, uq, iq, gq


# Scalar inequalities and point-defect budget.
scalar_checks = 0
worst_midpoint = (-1e9, None)
for j in range(1, 250000):
    t = -1.0 + 2.0 * j / 250000.0
    if t == 0.0:
        continue
    assert -R2(t) <= 2.0 * log2(1.0 / abs(t)) + 2e-11
    scalar_checks += 1

for j in range(1, 200001):
    x = j / 200001.0
    assert phi(x) <= M * x + 2e-12
    assert phi(x / 2.0) <= RHO * phi(x) + 2e-12
    scalar_checks += 2

for _ in range(300000):
    x = rng.uniform(-1.0, 1.0)
    y = rng.uniform(-1.0, 1.0)
    m = (x + y) / 2.0
    h = abs(x - y) / 2.0
    gap = R(m) - (R(x) + R(y)) / 2.0
    worst_midpoint = max(worst_midpoint, (gap - phi(h), (x, y, gap, phi(h))))
    assert gap <= phi(h) + 3e-11
    scalar_checks += 1

max_q_ratio = (-1.0, None)
for r in range(1, 257):
    _, _, iq, gq = qstats(r)
    ratio = gq / iq
    max_q_ratio = max(max_q_ratio, (ratio, r))
    assert gq <= 5.0 * iq + 2e-12
    scalar_checks += 1


# Exhaustive one-step product and activation identities for small bases.
bases = []
for n in range(4):
    for mask in range(1 << (1 << n)):
        bases.append(tuple(1 if (mask >> x) & 1 else -1 for x in range(1 << n)))

identity_checks = invariant_checks = restriction_checks = 0
max_identity_error = 0.0
max_gu_ratio = (-1.0, None)
for base in bases:
    ib = float(influence(base)); ub = U(base); gb = G(base); phib = Phi(base)
    assert phib <= M * ib + TOL
    for bcoef in (0.0, 0.37, 0.9):
        a = 0.0 if ib == 0.0 else max(0.0, (gb - bcoef * ub) / ib)
        A = max(a, 5.0) + ADDED
        assert gb + LAM * phib <= A * ib + bcoef * ub + TOL
        invariant_checks += 1

    for r, sign in ((1, 1), (1, -1), (2, 1), (2, -1)):
        bal = point_defect(r, sign)
        q = product(base, bal)
        f = activate(q)
        # Product additivity and exact activation identities.
        max_identity_error = max(
            max_identity_error,
            abs(U(q) - U(base) - U(bal)),
            abs(G(q) - G(base) - G(bal)),
            abs(float(influence(q)) - ib - float(influence(bal))),
            abs(U(f) - (0.5 * U(q) + R(float(mean(q))))),
        )
        identity_checks += 4
        bcoef = 0.37
        a = 0.0 if ib == 0.0 else max(0.0, (gb - bcoef * ub) / ib)
        A = max(a, 5.0) + ADDED
        assert G(f) + LAM * Phi(f) <= A * float(influence(f)) + bcoef * U(f) + 5e-8
        assert G(f) <= A * float(influence(f)) + bcoef * U(f) + 5e-8
        invariant_checks += 2
        if float(influence(f)):
            max_gu_ratio = max(max_gu_ratio, (G(f) / float(influence(f)), (len(f), r, sign)))

        # Every one-coordinate restriction stays under the same GU' constant.
        nf = len(f).bit_length() - 1
        for j in range(nf):
            for bit in (0, 1):
                h = restrict(f, j, bit)
                ih = float(influence(h))
                assert G(h) <= A * ih + bcoef * U(h) + 8e-8
                restriction_checks += 1


# Random deeper generated expressions, with direct truth-table reconstruction.
deep_cases = 0
sample_bases = bases[::19] + [bases[-1]]
for base in sample_bases:
    ib = float(influence(base)); ub = U(base); gb = G(base)
    bcoef = rng.choice((0.0, 0.25, 0.75))
    a = 0.0 if ib == 0.0 else max(0.0, (gb - bcoef * ub) / ib)
    A = max(a, 5.0) + ADDED
    f = base
    for _ in range(3):
        if len(f) >= 4096:
            break
        if rng.random() < 0.55:
            r = rng.choice((1, 2))
            sign = rng.choice((-1, 1))
            f = product(f, point_defect(r, sign))
        else:
            f = activate(f)
        assert G(f) + LAM * Phi(f) <= A * float(influence(f)) + bcoef * U(f) + 2e-7
        assert G(f) <= A * float(influence(f)) + bcoef * U(f) + 2e-7
        deep_cases += 1

assert max_identity_error < 2e-8
print(f"seed={SEED}")
print(f"scalar_checks={scalar_checks}")
print(f"truth_table_identity_checks={identity_checks}")
print(f"invariant_checks={invariant_checks}")
print(f"restriction_checks={restriction_checks}")
print(f"deep_generated_cases={deep_cases}")
print(f"rho={RHO:.15f}")
print(f"lambda={LAM:.15f}")
print(f"M={M:.15f}")
print(f"added_constant={ADDED:.15f}")
print(f"parity_class_GU_constant={5.0 + ADDED:.15f}")
print(f"max_point_defect_G_over_I={max_q_ratio}")
print(f"worst_sampled_midpoint_slack={worst_midpoint}")
print(f"max_identity_error={max_identity_error:.3e}")
print(f"max_sampled_G_over_I={max_gu_ratio}")
print("full_FEI=OPEN")
print("PASS")
