#!/usr/bin/env python3
"""Deterministic corroborative checks for PROB20-17 run 2026-09-16T103657Z.

Checks only. The analytic proofs are in the accompanying Markdown report.
No external packages beyond numpy are required.
"""

import itertools
import math
import numpy as np

SEED = 20260916103657
rng = np.random.default_rng(SEED)


def hp_directed_sum(X):
    n = X.shape[0]
    total = 0.0
    for p in itertools.permutations(range(n)):
        z = 1.0
        for r in range(n - 1):
            z *= X[p[r], p[r + 1]]
        total += z
    return total


def edge_sum(X):
    n = X.shape[0]
    return sum(X[i, j] for i in range(n) for j in range(i + 1, n))


def random_symmetric_edges_5():
    X = np.zeros((5, 5), dtype=float)
    vals = rng.random(10)
    for value, (i, j) in zip(vals, itertools.combinations(range(5), 2)):
        X[i, j] = X[j, i] = value
    return X


def cycle_5(weight):
    X = np.zeros((5, 5), dtype=float)
    for i in range(5):
        j = (i + 1) % 5
        X[i, j] = X[j, i] = weight
    return X


def random_absolute_gram_5(dim):
    U = rng.normal(size=(5, dim)) + 1j * rng.normal(size=(5, dim))
    U /= np.linalg.norm(U, axis=1, keepdims=True)
    G = np.abs(U @ U.conj().T)
    np.fill_diagonal(G, 1.0)
    return G


def transfer_R5(G):
    one = np.ones(5)
    return float(one @ np.linalg.matrix_power(G, 4) @ one) / (5 ** 5)


# Exact equality family for the sharp K5 path bound.
Xeq = cycle_5(0.2)
Weq = edge_sum(Xeq)
Deq = hp_directed_sum(Xeq)
assert abs(Weq - 1.0) < 1e-14
assert abs(Deq - 2.0 / 125.0) < 1e-14
assert abs(Deq - 2 * Weq**4 / 125) < 1e-14

# First reproduce the report's 1000 weighted-K5 sample.
min_path_bound_ratio = math.inf
min_low_margin_first1000 = math.inf
min_high_margin_first1000 = math.inf
low_first1000 = 0
high_first1000 = 0
for _ in range(1000):
    X = random_symmetric_edges_5()
    W = edge_sum(X)
    D = hp_directed_sum(X)
    bound = 2.0 * W**4 / 125.0
    assert D <= bound + 2e-11
    if D > 0:
        min_path_bound_ratio = min(min_path_bound_ratio, bound / D)

    H = D / math.factorial(5)
    gbar = W / 10.0
    mu = (1.0 + 4.0 * gbar) / 5.0
    if gbar <= 18.0 / 25.0:
        upper = (4.0 / 3.0) * gbar**4
        assert H <= upper + 1e-12
        assert upper <= mu**4 + 1e-12
        min_low_margin_first1000 = min(min_low_margin_first1000, mu**4 - upper)
        low_first1000 += 1
    else:
        T = 10.0 * (1.0 - gbar)
        upper = 1.0 - 2.0 * T / 5.0 + 3.0 * T**2 / 50.0
        assert H <= upper + 1e-12
        assert upper <= mu**4 + 1e-12
        min_high_margin_first1000 = min(min_high_margin_first1000, mu**4 - upper)
        high_first1000 += 1

# Then reproduce the report's 500 random complex rank-one sample.
min_owner_ratio = math.inf
min_bl_ratio = math.inf
for _ in range(500):
    dim = int(rng.integers(2, 8))
    G = random_absolute_gram_5(dim)
    H = hp_directed_sum(G) / math.factorial(5)
    R = transfer_R5(G)
    W = edge_sum(G)
    gbar = W / 10.0
    mu = (1.0 + 4.0 * gbar) / 5.0
    bl = mu**4
    assert R + 2e-12 >= bl
    assert R + 2e-12 >= H
    if H > 0:
        min_owner_ratio = min(min_owner_ratio, R / H)
    if bl > 0:
        min_bl_ratio = min(min_bl_ratio, R / bl)

# Additional scalar degree-lemma corroboration.
max_scalar = 0.0
for _ in range(20000):
    while True:
        y = 2.0 * rng.dirichlet(np.ones(5))
        if np.max(y) <= 1.0:
            break
    val = np.sum(y * (1.0 - y) ** 3)
    max_scalar = max(max_scalar, float(val))
    assert val <= 54.0 / 125.0 + 1e-12

# Boundary all-ones equality.
G = np.ones((5, 5), dtype=float)
H = hp_directed_sum(G) / math.factorial(5)
R = transfer_R5(G)
assert abs(H - 1.0) < 1e-14
assert abs(R - 1.0) < 1e-14

print(f"seed={SEED}")
print(f"cycle_equality_D={Deq:.16g}")
print(f"min_path_bound_ratio={min_path_bound_ratio:.16g}")
print(f"first1000_low_cases={low_first1000} min_low_margin={min_low_margin_first1000:.16g}")
print(f"first1000_high_cases={high_first1000} min_high_margin={min_high_margin_first1000:.16g}")
print(f"min_owner_ratio={min_owner_ratio:.16g}")
print(f"min_actual_R_over_BlakleyRoy={min_bl_ratio:.16g}")
print(f"max_scalar_random={max_scalar:.16g}")
print(f"scalar_sharp={54/125:.16g}")
print("all checks passed")
