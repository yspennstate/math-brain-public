#!/usr/bin/env python3
"""Exact finite regression for the covariance-inverse FOREST squeeze.

Enumerates every nonempty labelled simple graph on 2..5 vertices, then all
forests of each graph.  Uses exact integer covariance numerators and Fraction
Gauss-Jordan inversion.  This is regression evidence only, not a universal
proof of FOREST.
"""
from fractions import Fraction
from itertools import combinations

def is_forest(n, edges, mask):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for j, (u, v) in enumerate(edges):
        if (mask >> j) & 1:
            ru, rv = find(u), find(v)
            if ru == rv:
                return False
            parent[ru] = rv
    return True

def rank_graph(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
    return n - len({find(v) for v in range(n)})

def inverse_fraction(A):
    n = len(A)
    M = [
        [Fraction(A[i][j]) for j in range(n)]
        + [Fraction(int(i == j)) for j in range(n)]
        for i in range(n)
    ]
    for col in range(n):
        pivot = next((r for r in range(col, n) if M[r][col]), None)
        if pivot is None:
            raise AssertionError("singular covariance matrix")
        M[col], M[pivot] = M[pivot], M[col]
        z = M[col][col]
        M[col] = [x / z for x in M[col]]
        for r in range(n):
            if r != col and M[r][col]:
                z = M[r][col]
                M[r] = [M[r][j] - z * M[col][j] for j in range(2*n)]
    return [row[n:] for row in M]

def covariance_numerator(n, edges):
    m = len(edges)
    forests = [s for s in range(1 << m) if is_forest(n, edges, s)]
    Z = len(forests)
    one = [sum((s >> i) & 1 for s in forests) for i in range(m)]
    pair = [[0] * m for _ in range(m)]
    for i in range(m):
        pair[i][i] = one[i]
        for j in range(i + 1, m):
            z = sum(bool((s >> i) & 1) and bool((s >> j) & 1) for s in forests)
            pair[i][j] = pair[j][i] = z
    C = [[Z * pair[i][j] - one[i] * one[j] for j in range(m)] for i in range(m)]
    return C

graphs = 0
cyclic = 0
violations = 0
min_cyclic_excess = None
min_cyclic_meta = None

for n in range(2, 6):
    complete = list(combinations(range(n), 2))
    for gmask in range(1, 1 << len(complete)):
        edges = [complete[i] for i in range(len(complete)) if (gmask >> i) & 1]
        m = len(edges)
        C = covariance_numerator(n, edges)
        graphs += 1

        # Exact n<=5 target regression: off-diagonal covariances are nonpositive.
        if any(C[i][j] > 0 for i in range(m) for j in range(m) if i != j):
            violations += 1
            continue

        Cinv = inverse_fraction(C)

        # Stieltjes inverse positivity.
        if any(Cinv[i][j] < 0 for i in range(m) for j in range(m)):
            violations += 1

        diag_terms = [Fraction(C[i][i]) * Cinv[i][i] for i in range(m)]
        if any(t < 1 for t in diag_terms):
            violations += 1

        kappa = sum(diag_terms, Fraction(0))
        rank = rank_graph(n, edges)
        if m > rank:
            cyclic += 1
            excess = kappa - m
            if excess <= 0:
                violations += 1
            if min_cyclic_excess is None or excess < min_cyclic_excess:
                min_cyclic_excess = excess
                min_cyclic_meta = (n, m, rank, kappa)

print(f"graphs_checked={graphs}")
print(f"cyclic_graphs_checked={cyclic}")
print(f"violations={violations}")
print(f"minimum_cyclic_kappa_minus_m={min_cyclic_excess}")
n0, m0, r0, k0 = min_cyclic_meta
print(f"minimum_cyclic_meta_n_m_rank_kappa=({n0}, {m0}, {r0}, {k0})")
print("STATUS=PASS" if violations == 0 else "STATUS=FAIL")
