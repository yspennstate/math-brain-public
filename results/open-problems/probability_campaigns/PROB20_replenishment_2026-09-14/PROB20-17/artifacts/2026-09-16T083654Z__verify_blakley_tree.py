#!/usr/bin/env python3
"""Deterministic corroborative checks for PROB20-17 2026-09-16T083654Z.

Checks only. The analytic proofs are in the accompanying Markdown report.
"""

import itertools
import math
import numpy as np

SEED = 20260916083654
rng = np.random.default_rng(SEED)


def abs_gram(n, d):
    z = rng.normal(size=(n, d)) + 1j * rng.normal(size=(n, d))
    z /= np.linalg.norm(z, axis=1, keepdims=True)
    return np.abs(z @ z.conj().T)


def hamilton_mean(g):
    n = g.shape[0]
    total = 0.0
    for sigma in itertools.permutations(range(n)):
        term = 1.0
        for r in range(n - 1):
            term *= g[sigma[r], sigma[r + 1]]
        total += term
    return total / math.factorial(n)


def transfer_numerator(g, a):
    q = np.sqrt(a)
    m = (q[:, None] * g) * q[None, :]
    return float(q @ np.linalg.matrix_power(m, len(a) - 1) @ q)


def blakley_roy_lower(g, a):
    n = len(a)
    s = float(np.sum(a))
    return s ** (2 - n) * float(a @ g @ a) ** (n - 1)


def tree_hamilton_upper(g):
    n = g.shape[0]
    w = float(np.triu(g, 1).sum())
    bar = 2.0 * w / (n * (n - 1))
    c_n = 2.0 * n ** (n - 3) / math.factorial(n - 1)
    return c_n * bar ** (n - 1)


def path_sum_4(g):
    return hamilton_mean(g) * math.factorial(4) / 2.0


def c_tree(n):
    return 2.0 * n ** (n - 3) / math.factorial(n - 1)


def tau_tree(n):
    c = c_tree(n)
    return 1.0 / (n * c ** (1.0 / (n - 1)) - (n - 1))


min_br_ratio = float("inf")
min_tree_ratio = float("inf")
min_direct_ratio = float("inf")
nonpsd_count = 0
random_cases = 0

for n in (4, 5, 6):
    trials = 80 if n < 6 else 30
    for _ in range(trials):
        g = abs_gram(n, max(2, n - 1))
        a = np.exp(rng.normal(0.0, 1.0, size=n))

        transfer = transfer_numerator(g, a)
        br = blakley_roy_lower(g, a)
        assert transfer + 1e-10 >= br
        min_br_ratio = min(min_br_ratio, transfer / br)

        h = hamilton_mean(g)
        hu = tree_hamilton_upper(g)
        assert hu + 1e-12 >= h
        if h > 0:
            min_tree_ratio = min(min_tree_ratio, hu / h)

        left = float(np.prod(a)) * h
        right = transfer / n**n
        if left > 1e-15:
            min_direct_ratio = min(min_direct_ratio, right / left)

        if np.linalg.eigvalsh(g)[0] < -1e-9:
            nonpsd_count += 1
        random_cases += 1

# Special K4 path-polynomial bound P4 <= w^3/16 on arbitrary nonnegative
# symmetric edge weights (diagonal is irrelevant to P4).
min_special_ratio = float("inf")
for _ in range(2000):
    x = rng.random((4, 4))
    g = (x + x.T) / 2.0
    np.fill_diagonal(g, 1.0)
    w = float(np.triu(g, 1).sum())
    p4 = path_sum_4(g)
    rhs = w**3 / 16.0
    assert rhs + 1e-12 >= p4
    if p4 > 0:
        min_special_ratio = min(min_special_ratio, rhs / p4)

# Previous four-angle example: absolute Gram matrix is indefinite, but the
# direct Blakley-Roy lower bound uses it without PSD minorant loss.
angles = np.deg2rad([0.0, 60.0, 75.0, 105.0])
u = np.array([[np.cos(t), np.sin(t)] for t in angles])
g4 = np.abs(u @ u.T)
eigs4 = np.linalg.eigvalsh(g4)
mu4 = float(np.mean(g4))
h4 = hamilton_mean(g4)
r4 = transfer_numerator(g4, np.ones(4)) / 4**4
assert eigs4[0] < -1e-3
assert h4 <= mu4**3 + 1e-12
assert r4 >= mu4**3 - 1e-12

print(f"seed={SEED}")
print(f"random_cases={random_cases}")
print(f"nonpsd_abs_grams={nonpsd_count}")
print(f"min_transfer_over_BlakleyRoy={min_br_ratio:.16g}")
print(f"min_tree_upper_over_H={min_tree_ratio:.16g}")
print(f"min_actual_R_over_L={min_direct_ratio:.16g}")
print(f"min_special_w3over16_over_P4={min_special_ratio:.16g}")
print("tau_tree_4_to_10=" + repr({n: tau_tree(n) for n in range(4, 11)}))
print(
    "four_angle="
    + repr(
        {
            "lambda_min_abs_Gram": float(eigs4[0]),
            "mu": mu4,
            "H_4": h4,
            "mu^3": mu4**3,
            "actual_R_4": r4,
            "R_over_L": r4 / h4,
        }
    )
)
