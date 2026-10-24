#!/usr/bin/env python3
"""Finite diagnostics for B05 positive point-defect retained credit."""

from fractions import Fraction
from math import log, log2
import random

SEED = 0xB05A023C
rng = random.Random(SEED)
C = Fraction(8, 3)


def fwht(values):
    a = [Fraction(x) for x in values]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return [x / len(a) for x in a]


def upper_caps(p):
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
    cap = upper_caps(p)
    return sum(float(x) * log2(float(y / x)) for x, y in zip(p, cap) if x)


def influence(f):
    n = len(f).bit_length() - 1
    return sum(Fraction(sum(f[x] != f[x ^ (1 << j)] for x in range(1 << n)), 1 << n)
               for j in range(n))


def mean(f):
    return Fraction(sum(f), len(f))


def restrict(f, j, bit):
    n = len(f).bit_length() - 1
    out = []
    for z in range(1 << (n - 1)):
        lo = z & ((1 << j) - 1)
        hi = z >> j
        out.append(f[lo | (bit << j) | (hi << (j + 1))])
    return tuple(out)


def product(f, g):
    return tuple(f[x] * g[y] for y in range(len(g)) for x in range(len(f)))


def activate(q):
    return tuple(q[x >> 1] if not (x & 1) else 1 for x in range(2 * len(q)))


def Q(r):
    return tuple(-1 if x == 0 else 1 for x in range(1 << r))


def R(t):
    t = float(t)
    u = 0.0 if t == 0 else t * t * log2(1 / (t * t))
    xp, xm = (1 + t) / 2, (1 - t) / 2
    e1 = 0.0 if xp == 0 else xp * xp * log2(1 / (xp * xp))
    e2 = 0.0 if xm == 0 else xm * xm * log2(1 / xm)
    return e1 + e2 - u / 2 + (1 - t * t) / 4


def Rp(t):
    return ((1 + t) / 2 * log2(4 / (1 + t) ** 2)
            - (1 - t) / 2 * log2(2 / (1 - t))
            - t * log2(1 / t ** 2) - (1 - t) / (4 * log(2)) - t / 2)


def point_stats(r):
    p = 2.0 ** (-r)
    beta = 1 - 2 * p
    iq = 2 * r * p
    uq = beta * beta * log2(1 / (beta * beta)) + 2 * r * p * beta
    return beta, uq, iq


def tower(base, ranks):
    f = activate(product((-1, 1), base))
    layers = [f]
    for r in ranks:
        f = activate(product(Q(r), f))
        layers.append(f)
    return layers


def pruned_leaf_average(f, budget):
    n = len(f).bit_length() - 1
    if budget == 0 or n == 0 or rng.random() < 0.35:
        return U(f), 1
    j = rng.randrange(n)
    a, na = pruned_leaf_average(restrict(f, j, 0), budget - 1)
    b, nb = pruned_leaf_average(restrict(f, j, 1), budget - 1)
    return (a + b) / 2, na + nb


scalar_checks = 0
min_rp = (1e100, None)
max_secant = (-1e100, None)
for j in range(1, 200000):
    t = j / 200000
    rp = Rp(t)
    sec = R(t) / (1 - t)
    min_rp = min(min_rp, (rp, t))
    max_secant = max(max_secant, (sec, t))
    assert rp > -4 / 3 - 2e-12
    assert R(t) <= 4 * (1 - t) / 3 + 2e-12
    scalar_checks += 2

point_checks = 0
max_point_ratio = (0.0, None)
for r in range(2, 513):
    beta, uq, iq = point_stats(r)
    ratio = uq / iq
    if ratio > max_point_ratio[0]:
        max_point_ratio = (ratio, r)
    assert uq <= 2 * iq + 1e-13
    if r <= 10:
        q = Q(r)
        assert abs(U(q) - uq) < 2e-11
        assert abs(float(influence(q)) - iq) < 2e-14
    point_checks += 1

cases = []
for n in range(3):
    for mask in range(1 << (1 << n)):
        cases.append(tuple(1 if (mask >> x) & 1 else -1 for x in range(1 << n)))

rank_sequences = [(), (2,), (3,), (2, 2), (2, 3), (3, 2)]
direct_towers = recurrence_checks = endpoint_checks = 0
max_recurrence_error = 0.0
max_endpoint_ratio = (0.0, None)
small_towers = []
for base in cases:
    ub, ib = U(base), influence(base)
    for ranks in rank_sequences:
        layers = tower(base, ranks)
        prev = None
        for depth, f in enumerate(layers, 1):
            direct_towers += 1
            uf, inf = U(f), influence(f)
            if inf:
                max_endpoint_ratio = max(max_endpoint_ratio, (uf / float(inf), (len(base), ranks, depth)))
            if ub <= float(C * ib) + 2e-12:
                assert uf <= float(C * inf) + 5e-10
                endpoint_checks += 1
            if depth == 1:
                eu, ei = 1 + ub / 2, 1 + ib / 2
            else:
                r = ranks[depth - 2]
                beta, uq, iq = point_stats(r)
                t = beta * float(mean(prev))
                eu = U(prev) / 2 + uq / 2 + R(t)
                ei = influence(prev) / 2 + Fraction.from_float(iq / 2 + (1 - t) / 2)
            max_recurrence_error = max(max_recurrence_error, abs(uf - eu))
            assert abs(uf - eu) < 8e-10
            assert abs(float(inf) - float(ei)) < 8e-14
            recurrence_checks += 2
            prev = f
        if len(layers[-1]) <= 2048:
            small_towers.append(layers[-1])

# Long nonstationary state recurrences stress arbitrary rank and vanishing p.
state_checks = 0
for base in cases:
    u, i, m = 1 + U(base) / 2, 1 + float(influence(base)) / 2, 0.5
    assert u <= float(C) * i + 2e-12
    for _ in range(1000):
        r = rng.randint(2, 512)
        beta, uq, iq = point_stats(r)
        t = beta * m
        u = u / 2 + uq / 2 + R(t)
        i = i / 2 + iq / 2 + (1 - t) / 2
        m = (1 + t) / 2
        assert u <= float(C) * i + 2e-11
        state_checks += 1

tree_checks = terminal_checks = total_leaves = 0
cores = [(-1,), (-1, 1), (-1, -1, -1, 1)]
for f in small_towers[:90]:
    inf = float(influence(f))
    for _ in range(5):
        leaf_u, leaves = pruned_leaf_average(f, 4)
        assert U(f) - leaf_u <= float(C) * inf + 8e-10
        total_leaves += leaves
        tree_checks += 1
    for h in cores:
        leaf_u, _ = pruned_leaf_average(f, 3)
        root = U(product(f, h))
        assert abs(root - U(f) - U(h)) < 2e-10
        assert abs((root - leaf_u - U(h)) - (U(f) - leaf_u)) < 2e-10
        terminal_checks += 1

print(f"seed={SEED}")
print(f"scalar_checks={scalar_checks} min_Rp={min_rp}")
print(f"max_R_over_one_minus_t={max_secant}")
print(f"point_defect_checks={point_checks} max_point_ratio={max_point_ratio}")
print(f"direct_towers={direct_towers} recurrence_checks={recurrence_checks}")
print(f"endpoint_checks={endpoint_checks} max_endpoint_ratio={max_endpoint_ratio}")
print(f"long_state_checks={state_checks}")
print(f"tree_checks={tree_checks} total_leaves={total_leaves}")
print(f"terminal_tensor_checks={terminal_checks}")
print(f"max_recurrence_error={max_recurrence_error:.3e}")
print("proved_constant=8/3")
print("full_fei=OPEN")
print("PASS")
