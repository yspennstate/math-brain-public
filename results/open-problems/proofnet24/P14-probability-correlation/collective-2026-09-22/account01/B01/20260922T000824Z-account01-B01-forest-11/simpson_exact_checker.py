#!/usr/bin/env python3
"""Exact sanity checks for FOREST-UNIVERSAL-SIMPSON-20260922.

Enumerates every labelled simple graph on 2,3,4,5 vertices, every unordered
triple of present edges, and each of the three choices of a conditioned edge.
All arithmetic is exact Fraction arithmetic.  This checks the binary
law-of-total-covariance identity used in the proof report; it is only a
sanity check, not evidence beyond the inherited finite source baseline.
"""
from fractions import Fraction
from itertools import combinations


def forests(n, edges):
    out = []
    m = len(edges)
    for mask in range(1 << m):
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        ok = True
        for i, (u, v) in enumerate(edges):
            if (mask >> i) & 1:
                ru, rv = find(u), find(v)
                if ru == rv:
                    ok = False
                    break
                parent[ru] = rv
        if ok:
            out.append(mask)
    return out


def mean(fs, i):
    return Fraction(sum((x >> i) & 1 for x in fs), len(fs))


def cov(fs, i, j):
    z = len(fs)
    pi = Fraction(sum((x >> i) & 1 for x in fs), z)
    pj = Fraction(sum((x >> j) & 1 for x in fs), z)
    pij = Fraction(sum(((x >> i) & 1) * ((x >> j) & 1) for x in fs), z)
    return pij - pi * pj


graphs = 0
marked_conditionings = 0
identity_failures = 0
positive_pair_instances = 0

for n in range(2, 6):
    universe = list(combinations(range(n), 2))
    for graph_mask in range(1 << len(universe)):
        edges = [
            universe[i]
            for i in range(len(universe))
            if (graph_mask >> i) & 1
        ]
        graphs += 1
        if len(edges) < 3:
            continue
        fs = forests(n, edges)
        z = len(fs)
        for e, f, g in combinations(range(len(edges)), 3):
            for a, b, c in ((e, f, g), (e, g, f), (f, g, e)):
                marked_conditionings += 1
                cab = cov(fs, a, b)
                pc = mean(fs, c)
                vc = pc * (1 - pc)
                cac = cov(fs, a, c)
                cbc = cov(fs, b, c)

                fs0 = [x for x in fs if ((x >> c) & 1) == 0]
                fs1 = [x for x in fs if ((x >> c) & 1) == 1]
                c0 = cov(fs0, a, b)
                c1 = cov(fs1, a, b)
                rhs = (
                    Fraction(len(fs0), z) * c0
                    + Fraction(len(fs1), z) * c1
                    + cac * cbc / vc
                )
                if rhs != cab:
                    identity_failures += 1
                if cab > 0:
                    positive_pair_instances += 1

print(f"graphs_checked={graphs}")
print(f"marked_conditionings_checked={marked_conditionings}")
print(f"law_total_covariance_failures={identity_failures}")
print(f"positive_pair_instances_n_le_5={positive_pair_instances}")
assert graphs == 1098
assert marked_conditionings == 46563
assert identity_failures == 0
assert positive_pair_instances == 0
print("ALL_EXACT_CHECKS_PASSED")
