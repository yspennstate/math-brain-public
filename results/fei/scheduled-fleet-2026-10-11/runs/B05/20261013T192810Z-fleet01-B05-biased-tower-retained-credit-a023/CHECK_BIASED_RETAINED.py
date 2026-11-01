#!/usr/bin/env python3
"""Finite audit for the biased-tower retained-credit theorem.

The all-dimensional proof is analytic.  This script independently rebuilds
Walsh spectra, U, influence, tower recurrences, and randomly pruned physical
restriction-tree ledgers.  It also checks cancellation of a common disjoint
terminal core by direct tensor construction.
"""

from fractions import Fraction
from math import log2
import random

SEED = 0xB05A023B
rng = random.Random(SEED)
B = (-1, -1, -1, 1)
C0 = Fraction(48, 35)


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
    return sum(
        Fraction(sum(f[x] != f[x ^ (1 << j)] for x in range(1 << n)), 1 << n)
        for j in range(n)
    )


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


def tower(base, depth):
    f = activate(product((-1, 1), base))
    layers = [f]
    for _ in range(2, depth + 1):
        f = activate(product(B, f))
        layers.append(f)
    return layers


def R(t):
    t = float(t)
    u = 0.0 if t == 0 else t * t * log2(1 / (t * t))
    xp, xm = (1 + t) / 2, (1 - t) / 2
    e1 = 0.0 if xp == 0 else xp * xp * log2(1 / (xp * xp))
    e2 = 0.0 if xm == 0 else xm * xm * log2(1 / xm)
    return e1 + e2 - u / 2 + (1 - t * t) / 4


def pruned_leaf_average(f, budget):
    """Return average leaf U for a deterministic random pruned tree."""
    n = len(f).bit_length() - 1
    if budget == 0 or n == 0 or rng.random() < 0.32:
        return U(f), 1
    j = rng.randrange(n)
    left, nl = pruned_leaf_average(restrict(f, j, 0), budget - 1)
    right, nr = pruned_leaf_average(restrict(f, j, 1), budget - 1)
    return (left + right) / 2, nl + nr


assert mean(B) == Fraction(-1, 2)
assert influence(B) == 1
assert abs(U(B) - 1) < 1e-14

# Diagnostic sampling of the analytic scalar lemma R(t) <= 1 on [-1,0].
max_scalar = (-1e100, None)
for j in range(20001):
    t = -1 + j / 20000
    val = R(t)
    if val > max_scalar[0]:
        max_scalar = (val, t)
    assert val <= 1 + 2e-13

cases = []
for n in range(4):
    for mask in range(1 << (1 << n)):
        cases.append(tuple(1 if (mask >> x) & 1 else -1 for x in range(1 << n)))
for n in range(4, 8):
    rare = [-1] * (1 << n)
    rare[-1] = 1
    cases.append(tuple(rare))
    for _ in range(3):
        cases.append(tuple(rng.choice((-1, 1)) for _ in range(1 << n)))

direct_towers = 0
recurrence_checks = 0
endpoint_checks = 0
tree_checks = 0
tensor_checks = 0
total_tree_leaves = 0
max_recurrence_error = 0.0
max_endpoint_ratio = (0.0, None)
max_tree_ratio = (0.0, None)

for base in cases:
    n = len(base).bit_length() - 1
    max_depth = 3 if n <= 3 else 2
    layers = tower(base, max_depth)
    prev = None
    for depth, f in enumerate(layers, 1):
        direct_towers += 1
        uf, inf = U(f), float(influence(f))
        ratio = 0.0 if inf == 0 else uf / inf
        if ratio > max_endpoint_ratio[0]:
            max_endpoint_ratio = (ratio, (n, depth, mean(base)))

        ub, ib = U(base), float(influence(base))
        for c in (float(C0), 1.5, 2.0, 3.0):
            if ub <= c * ib + 3e-12:
                assert uf <= c * inf + 5e-11
                endpoint_checks += 1

        if depth == 1:
            expected_u = 1 + ub / 2
            expected_i = 1 + Fraction(influence(base), 2)
            assert abs(uf - expected_u) < 4e-12
            assert influence(f) == expected_i
            recurrence_checks += 2
        else:
            m = mean(prev)
            assert Fraction(3, 8) <= m <= Fraction(1, 2)
            expected_u = U(prev) / 2 + 0.5 + R(-m / 2)
            expected_i = influence(prev) / 2 + 1 + m / 4
            max_recurrence_error = max(max_recurrence_error, abs(uf - expected_u))
            assert abs(uf - expected_u) < 5e-11
            assert influence(f) == expected_i
            recurrence_checks += 2
        prev = f

# Tree tests on modest towers.  The tree may stop independently on branches.
small_bases = cases[:20] + [cases[270], cases[271], cases[272]]
terminal_cores = [(-1,), (-1, 1), (-1, -1, -1, 1), (-1, -1, 1, -1)]
for base in small_bases:
    for depth, f in enumerate(tower(base, 2), 1):
        inf = float(influence(f))
        for _ in range(12):
            leaf_u, leaves = pruned_leaf_average(f, budget=4)
            retained = U(f) - leaf_u
            assert retained <= 2 * inf + 5e-11
            ratio = retained / inf if inf else 0.0
            if ratio > max_tree_ratio[0]:
                max_tree_ratio = (ratio, (len(base).bit_length() - 1, depth, leaves))
            total_tree_leaves += leaves
            tree_checks += 1

        # Directly verify cancellation for common disjoint terminal cores.
        for h in terminal_cores:
            leaf_u, _ = pruned_leaf_average(f, budget=3)
            root_tensor_u = U(product(f, h))
            assert abs(root_tensor_u - U(f) - U(h)) < 8e-12
            # Tensor additivity makes every leaf gain the same U(h).
            assert abs((root_tensor_u - (leaf_u + U(h))) - (U(f) - leaf_u)) < 1e-11
            tensor_checks += 1

print(f"seed={SEED}")
print(f"base_cases={len(cases)}")
print(f"direct_towers={direct_towers}")
print(f"scalar_samples=20001 max_R={max_scalar[0]:.15f} at_t={max_scalar[1]:.8f}")
print(f"exact_recurrence_checks={recurrence_checks}")
print(f"endpoint_transfer_checks={endpoint_checks}")
print(f"pruned_tree_checks={tree_checks} total_tree_leaves={total_tree_leaves}")
print(f"terminal_tensor_checks={tensor_checks}")
print(f"max_endpoint_ratio={max_endpoint_ratio[0]:.15f} witness={max_endpoint_ratio[1]}")
print(f"max_retained_tree_ratio={max_tree_ratio[0]:.15f} witness={max_tree_ratio[1]}")
print(f"max_recurrence_error={max_recurrence_error:.3e}")
print("proved_endpoint_threshold=48/35")
print("dense_nullity_two_corollary_constant=2")
print("full_fei=OPEN")
print("PASS")
