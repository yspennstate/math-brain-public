#!/usr/bin/env python3
"""Deterministic corroborative checks for PROB20-17 run 2026-09-16T113641Z.

Checks:
  * D6 <= W^5/625 for random nonnegative weighted K6 arrays;
  * D6 <= W^5/648 for capped dense arrays with W >= 5/c0;
  * scalar constants c0, gamma0, gamma1, Tstar;
  * direct equal-scale rank-one L6/R6 enumeration on random complex vectors;
  * all-n-derived n=6 degree-sensitive deficit upper bound.

This file is numerical corroboration only. The Markdown report contains the proofs.
"""

import itertools
import math
import numpy as np

SEED = 20260916113641
rng = np.random.default_rng(SEED)
PERMS = np.array(list(itertools.permutations(range(6))), dtype=int)


def make_sym(vals):
    X = np.zeros((6, 6), dtype=float)
    k = 0
    for i in range(6):
        for j in range(i + 1, 6):
            X[i, j] = X[j, i] = float(vals[k])
            k += 1
    return X


def d6(X):
    vals = np.ones(len(PERMS), dtype=float)
    for r in range(5):
        vals *= X[PERMS[:, r], PERMS[:, r + 1]]
    return float(vals.sum())


def root_in_interval(coeffs, lo, hi):
    roots = np.roots(coeffs)
    good = [z.real for z in roots if abs(z.imag) < 1e-9 and lo < z.real < hi]
    assert len(good) == 1, roots
    return float(good[0])


c0 = root_in_interval([27, -90, 99, -32], 0, 1)
W0 = 5.0 / c0
gamma0 = 1.0 / (6.0 * (27.0 / 16.0) ** (1.0 / 5.0) - 5.0)
gamma1 = 1.0 / (6.0 * (625.0 / 384.0) ** (1.0 / 5.0) - 5.0)
Tstar = root_in_interval([5, -450, 16200, 128304, -524880], 3, 4)
high_threshold = 1.0 - Tstar / 15.0

# Exact displayed derivative factorization sanity check.
for x in np.linspace(0.0, 1.0, 1001):
    lhs = 81*x*x - 180*x + 99
    rhs = 9*(9*x - 11)*(x - 1)
    assert abs(lhs - rhs) < 1e-10

# Scalar K6 lemma by random feasible degree vectors.
f = lambda y: y * (1.0 - y) ** 4
max_scalar = 0.0
accepted = 0
for _ in range(100000):
    y = 2.0 * rng.dirichlet(np.ones(6))
    if np.max(y) > 1.0:
        continue
    accepted += 1
    s = float(np.sum(f(y)))
    max_scalar = max(max_scalar, s)
    assert s <= 256.0 / 625.0 + 1e-12
assert accepted > 1000

# Tangent-line bound on [0,c0].
grid = np.linspace(0.0, c0, 10001)
line = 32.0 / 243.0 - 16.0 * grid / 81.0
assert float(np.min(line - f(grid))) >= -1e-12

# Random arbitrary nonnegative weighted K6 tests.
min_global_ratio = float("inf")
for _ in range(300):
    vals = np.exp(rng.normal(size=15))
    X = make_sym(vals)
    W = float(np.sum(vals))
    exact = d6(X)
    bound = W**5 / 625.0
    assert exact <= bound * (1.0 + 1e-11)
    min_global_ratio = min(min_global_ratio, bound / max(exact, 1e-300))

# Random capped dense tests.
min_dense_ratio = float("inf")
dense_count = 0
for _ in range(300):
    vals = rng.uniform(0.55, 1.0, size=15)
    W = float(np.sum(vals))
    if W < W0:
        continue
    dense_count += 1
    X = make_sym(vals)
    exact = d6(X)
    bound = W**5 / 648.0
    assert exact <= bound * (1.0 + 1e-11)
    min_dense_ratio = min(min_dense_ratio, bound / max(exact, 1e-300))
assert dense_count > 0


def random_units(n, d):
    Z = rng.normal(size=(n, d)) + 1j * rng.normal(size=(n, d))
    Z /= np.linalg.norm(Z, axis=1, keepdims=True)
    return Z


def rankone_stats(U):
    G = np.abs(U @ U.conj().T)
    np.fill_diagonal(G, 1.0)
    L = d6(G) / math.factorial(6)
    one = np.ones(6)
    R = float((one @ np.linalg.matrix_power(G, 5) @ one).real) / 6**6
    gbar = float((np.sum(G) - 6.0) / 30.0)
    H = 1.0 - G
    np.fill_diagonal(H, 0.0)
    T = float(np.sum(np.triu(H, 1)))
    r = np.sum(H, axis=1)
    deficit_bound = 1.0 - T/3.0 + (2*T*T - float(r @ r)) / 30.0
    br_lower = (1.0 - T/18.0) ** 5
    return gbar, L, R, T, r, deficit_bound, br_lower

min_R_over_L = float("inf")
min_deficit_over_L = float("inf")
certified_samples = 0
for d in [2, 3, 5, 8]:
    for _ in range(60):
        stats = rankone_stats(random_units(6, d))
        gbar, L, R, T, r, deficit_bound, br_lower = stats
        assert L <= deficit_bound + 1e-10
        assert R + 1e-10 >= br_lower
        min_R_over_L = min(min_R_over_L, R / max(L, 1e-300))
        min_deficit_over_L = min(min_deficit_over_L,
                                 deficit_bound / max(L, 1e-300))
        if gbar <= gamma1 or gbar >= high_threshold:
            certified_samples += 1
            assert L <= br_lower + 1e-9

print("seed", SEED)
print("c0", c0)
print("W0", W0)
print("gamma0", gamma0)
print("gamma1", gamma1)
print("Tstar", Tstar)
print("high_threshold", high_threshold)
print("accepted_scalar_samples", accepted)
print("max_sampled_scalar_sum", max_scalar)
print("scalar_theorem_constant", 256.0/625.0)
print("min_global_bound_over_exact", min_global_ratio)
print("dense_count", dense_count)
print("min_dense_bound_over_exact", min_dense_ratio)
print("certified_rankone_samples", certified_samples)
print("min_direct_R_over_L", min_R_over_L)
print("min_deficit_bound_over_L", min_deficit_over_L)
