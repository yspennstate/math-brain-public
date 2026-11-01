#!/usr/bin/env python3
"""Deterministic corroborative checks for PROB20-17 weighted Hamiltonian-path bounds.

Checks only. The proof is in the accompanying Markdown report.

Claims numerically checked:
1) Weighted Moran--Snir--Manber rooted bound:
   D_{n,v} <= (W/(n-1))^(n-1).
2) Global directed Hamiltonian path bound:
   D_n <= n (W/(n-1))^(n-1).
3) Degree-sensitive refinement:
   D_n <= sum_v d_v ((W-d_v)/(n-2))^(n-2), n>=3.
4) Rank-one n=5 two-cluster worked example and comparison with
   Blakley--Roy lower bound.
"""

import itertools
import math
import numpy as np

SEED = 20260916093724
rng = np.random.default_rng(SEED)


def directed_hamilton_sum(w):
    n = w.shape[0]
    total = 0.0
    for sigma in itertools.permutations(range(n)):
        term = 1.0
        for r in range(n - 1):
            term *= w[sigma[r], sigma[r + 1]]
        total += term
    return total


def rooted_hamilton_sum(w, start):
    n = w.shape[0]
    rest = [j for j in range(n) if j != start]
    total = 0.0
    for tail in itertools.permutations(rest):
        sigma = (start,) + tail
        term = 1.0
        for r in range(n - 1):
            term *= w[sigma[r], sigma[r + 1]]
        total += term
    return total


def path_bounds(w):
    n = w.shape[0]
    W = float(np.triu(w, 1).sum())
    global_bound = n * (W / (n - 1)) ** (n - 1)
    degrees = w.sum(axis=1)
    if n >= 3:
        degree_bound = sum(
            float(d) * ((W - float(d)) / (n - 2)) ** (n - 2)
            for d in degrees
        )
    else:
        degree_bound = global_bound
    return W, global_bound, degree_bound, degrees


min_global_ratio = float("inf")
min_degree_ratio = float("inf")
min_rooted_ratio = float("inf")
num_random = 0

for n in range(2, 8):
    trials = 30 if n <= 6 else 8
    for _ in range(trials):
        a = rng.random((n, n))
        w = np.triu(a, 1)
        w = w + w.T

        directed = directed_hamilton_sum(w)
        W, global_bound, degree_bound, degrees = path_bounds(w)

        assert directed <= global_bound + 1e-10
        if n >= 3:
            assert directed <= degree_bound + 1e-10

        if directed > 1e-15:
            min_global_ratio = min(min_global_ratio, global_bound / directed)
            if n >= 3:
                min_degree_ratio = min(min_degree_ratio, degree_bound / directed)

        for v in range(n):
            rooted = rooted_hamilton_sum(w, v)
            rooted_bound = (W / (n - 1)) ** (n - 1)
            assert rooted <= rooted_bound + 1e-10
            if rooted > 1e-15:
                min_rooted_ratio = min(min_rooted_ratio, rooted_bound / rooted)

        num_random += 1

# Equal-scale n=5 rank-one two-cluster kernel:
# clusters of sizes 2 and 3, within overlap 1, cross overlap c=1/3.
# This is realizable by duplicating one unit vector in each cluster and choosing
# the two directions to have absolute inner product 1/3.
n = 5
c = 1.0 / 3.0
g = np.ones((n, n))
for i in range(2):
    for j in range(2, 5):
        g[i, j] = g[j, i] = c

w = g - np.eye(n)
directed = directed_hamilton_sum(w)
H = directed / math.factorial(n)
W, global_bound, degree_bound, degrees = path_bounds(w)
path_upper = global_bound / math.factorial(n)
degree_upper = degree_bound / math.factorial(n)
bar_g = W / math.comb(n, 2)
mu = float(g.mean())
q = np.ones(n)
R = float(q @ np.linalg.matrix_power(g, n - 1) @ q) / n**n

C_path = (n / 2.0) ** (n - 1) / math.factorial(n - 1)
C_tree = 2.0 * n ** (n - 3) / math.factorial(n - 1)
tau_path = 1.0 / (n * C_path ** (1.0 / (n - 1)) - (n - 1))
tau_tree = 1.0 / (n * C_tree ** (1.0 / (n - 1)) - (n - 1))

assert abs(bar_g - 0.6) < 1e-14
assert tau_tree < bar_g < tau_path
assert H <= degree_upper <= path_upper <= mu ** (n - 1) <= R + 1e-14
assert max(g[np.triu_indices(n, 1)]) == 1.0
old_band_rhs = (1.0 + (n - 1) * c) / n
assert 1.0 > old_band_rhs

print(f"seed={SEED}")
print(f"random_graph_cases={num_random}")
print(f"min_global_bound_over_exact={min_global_ratio:.16g}")
print(f"min_degree_bound_over_exact={min_degree_ratio:.16g}")
print(f"min_rooted_bound_over_exact={min_rooted_ratio:.16g}")
print("path_thresholds_4_to_10=" + repr({
    k: 1.0 / (
        k * (((k / 2.0) ** (k - 1) / math.factorial(k - 1)) ** (1.0 / (k - 1)))
        - (k - 1)
    )
    for k in range(4, 11)
}))
print("n5_two_cluster=" + repr({
    "cross_overlap": c,
    "bar_g": bar_g,
    "degrees": degrees.tolist(),
    "H_5": H,
    "degree_upper": degree_upper,
    "path_upper": path_upper,
    "mu": mu,
    "mu^4": mu**4,
    "actual_R": R,
    "tree_threshold": tau_tree,
    "path_threshold": tau_path,
    "old_band_rhs_for_gplus": old_band_rhs,
}))
