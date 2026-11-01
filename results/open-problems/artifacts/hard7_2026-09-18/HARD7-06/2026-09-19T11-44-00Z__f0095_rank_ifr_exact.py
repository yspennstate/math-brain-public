#!/usr/bin/env python3
"""
Exact finite checker for HARD7-06:
rank-layer evidence for the 3-colourability complex.

For n=4,...,7, enumerate every unlabeled graph in NetworkX's graph atlas,
retain the 3-colourable ones, and convert each isomorphism class to its exact
number n!/|Aut(G)| of labeled graphs. For n<=6, independently enumerate all
2^(n choose 2) labeled graphs and cross-check the layer counts.

Then verify with integer arithmetic that the normalized layer probabilities
    p_m = a_m / binom(N,m)
are log-concave:
    p_m^2 >= p_{m-1} p_{m+1}.
This is finite evidence only; it is NOT a proof for all n.
"""
from math import comb, factorial
from fractions import Fraction
from itertools import combinations
import networkx as nx


def is_3colorable_edges(n, edges):
    adj = [0] * n
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    order = sorted(range(n), key=lambda v: adj[v].bit_count(), reverse=True)
    color = [-1] * n

    def dfs(i):
        if i == n:
            return True
        v = order[i]
        used = 0
        av = adj[v]
        for u in range(n):
            if ((av >> u) & 1) and color[u] >= 0:
                used |= 1 << color[u]
        for c in range(3):
            if not ((used >> c) & 1):
                color[v] = c
                if dfs(i + 1):
                    return True
                color[v] = -1
        return False

    return dfs(0)


def is_3colorable_graph(G):
    return is_3colorable_edges(G.number_of_nodes(), list(G.edges()))


def aut_size(G):
    return sum(
        1
        for _ in nx.algorithms.isomorphism.GraphMatcher(G, G).isomorphisms_iter()
    )


def atlas_counts(n):
    N = comb(n, 2)
    counts = [0] * (N + 1)
    unlabeled_good = 0
    for G in nx.graph_atlas_g():
        if G.number_of_nodes() != n:
            continue
        if not is_3colorable_graph(G):
            continue
        a = aut_size(G)
        assert factorial(n) % a == 0
        counts[G.number_of_edges()] += factorial(n) // a
        unlabeled_good += 1
    return counts, unlabeled_good


def direct_labeled_counts(n):
    pairs = list(combinations(range(n), 2))
    N = len(pairs)
    counts = [0] * (N + 1)
    for mask in range(1 << N):
        m = mask.bit_count()
        edges = [pairs[i] for i in range(N) if (mask >> i) & 1]
        if is_3colorable_edges(n, edges):
            counts[m] += 1
    return counts


# OEIS A076315, used only as an independent total-unlabeled count check.
expected_unlabeled = {4: 10, 5: 29, 6: 119, 7: 667}
all_counts = {}

for n in range(4, 8):
    N = comb(n, 2)
    counts, ugood = atlas_counts(n)
    assert ugood == expected_unlabeled[n]
    if n <= 6:
        assert counts == direct_labeled_counts(n)

    for m in range(1, N):
        # Exact normalized log-concavity after clearing denominators.
        lhs = counts[m] * counts[m] * comb(N, m - 1) * comb(N, m + 1)
        rhs = counts[m - 1] * counts[m + 1] * comb(N, m) * comb(N, m)
        assert lhs >= rhs, (n, m, lhs, rhs)

    p = [Fraction(counts[m], comb(N, m)) for m in range(N + 1)]
    ET = sum(p[1:], Fraction(0))
    theta_mean = Fraction(2, n) * ET
    all_counts[n] = counts

    print(f"n={n}")
    print("labeled_layer_counts =", counts)
    print("unlabeled_3colorable =", ugood)
    print("normalized_layer_log_concavity = PASS")
    print("E_T =", ET)
    print("2E_T/n =", theta_mean)
    print()

assert all_counts[4] == [1, 6, 15, 20, 15, 6, 0]
assert all_counts[5] == [1, 10, 45, 120, 210, 252, 205, 100, 15, 0, 0]
assert all_counts[6] == [
    1, 15, 105, 455, 1365, 3003, 4990, 6300,
    5895, 3805, 1365, 240, 15, 0, 0, 0,
]
assert all_counts[7] == [
    1, 21, 210, 1330, 5985, 20349, 54229, 115755,
    199815, 278215, 306831, 256746, 147665, 55125,
    12915, 1750, 105, 0, 0, 0, 0, 0,
]

print("ALL_EXACT_CHECKS_PASS = True")
print("SCOPE = finite n<=7 evidence only; no asymptotic inference")
