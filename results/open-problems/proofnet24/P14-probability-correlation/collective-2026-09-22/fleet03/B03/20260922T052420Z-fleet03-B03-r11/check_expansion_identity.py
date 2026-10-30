#!/usr/bin/env python3
"""Exact standard-library check for FOREST-EXPANSION-SCOPE-v4.

Enumerates ALL acyclic edge subsets, including empty and disconnected forests.
Checks one exact simple expansion implementing q=2/(2^2-1)=2/3.
"""
from fractions import Fraction
from itertools import combinations


def is_forest(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        parent[rv] = ru
    return True


def counts(n, edges, e_idx, f_idx, weights):
    Z = Ze = Zf = Zef = Fraction(0)
    m = len(edges)
    for mask in range(1 << m):
        chosen = [edges[i] for i in range(m) if (mask >> i) & 1]
        if not is_forest(n, chosen):
            continue
        w = Fraction(1)
        for i in range(m):
            if (mask >> i) & 1:
                w *= weights[i]
        Z += w
        if (mask >> e_idx) & 1:
            Ze += w
        if (mask >> f_idx) & 1:
            Zf += w
        if ((mask >> e_idx) & 1) and ((mask >> f_idx) & 1):
            Zef += w
    return Z, Ze, Zf, Zef, Ze * Zf - Z * Zef


# Host K4, marked e=01 and f=02; g=23 has activity q=2/3.
host = list(combinations(range(4), 2))
host_weights = [Fraction(1)] * len(host)
g_idx = host.index((2, 3))
host_weights[g_idx] = Fraction(2, 3)
h = counts(4, host, host.index((0, 1)), host.index((0, 2)), host_weights)

# Replace g=23 by k=2 internally-disjoint paths of length a=2.
# New internal vertices are 4 and 5.  This graph is simple.
expanded = [
    (0, 1), (0, 2), (0, 3), (1, 2), (1, 3),
    (2, 4), (4, 3), (2, 5), (5, 3),
]
x = counts(6, expanded, 0, 1, [Fraction(1)] * len(expanded))

D = (2**2 - 1)**2  # (2^a-1)^k = 9
assert x[:4] == tuple(D * z for z in h[:4])
assert x[4] == D * D * h[4]

print("host weighted (Z,Ze,Zf,Zef,Delta) =", h)
print("expanded unit (Z,Ze,Zf,Zef,Delta) =", x)
print("D =", D)
print("Delta_expanded / Delta_host =", x[4] / h[4])
print("PASS exact expansion identity")
