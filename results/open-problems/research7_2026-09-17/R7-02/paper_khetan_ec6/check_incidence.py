#!/usr/bin/env python3
"""Exact finite check for the six-edge two-direction incidence classification.

Enumerate all simple bipartite incidence matrices with 6 edges, 2 or 3
nonempty line-sections on each side, and minimum degree at least 2.
The proof predicts only K_{2,3}/K_{3,2}, or 3x3 complements of a
permutation matrix (C6).
"""
from itertools import combinations
from collections import Counter

cases = []
for r in (2, 3):
    for c in (2, 3):
        cells = list(range(r*c))
        if len(cells) < 6:
            continue
        for comb in combinations(cells, 6):
            M = [[0]*c for _ in range(r)]
            for k in comb:
                i, j = divmod(k, c)
                M[i][j] = 1
            rs = tuple(sum(row) for row in M)
            cs = tuple(sum(M[i][j] for i in range(r)) for j in range(c))
            if min(rs) >= 2 and min(cs) >= 2:
                cases.append((r, c, rs, cs, tuple(tuple(row) for row in M)))

sig = Counter((r, c, rs, cs) for r, c, rs, cs, _ in cases)
print("admissible labelled matrices:", len(cases))
for key in sorted(sig):
    print(key, "count=", sig[key])

assert len(cases) == 8
assert sig[(2, 3, (3, 3), (2, 2, 2))] == 1
assert sig[(3, 2, (2, 2, 2), (3, 3))] == 1
assert sig[(3, 3, (2, 2, 2), (2, 2, 2))] == 6

# Every 3x3 admissible matrix has exactly one zero in each row and column,
# hence is the complement of a permutation matrix and its incidence graph is C6.
for r, c, rs, cs, M in cases:
    if (r, c) == (3, 3):
        assert all(row.count(0) == 1 for row in M)
        assert all(sum(1 for i in range(3) if M[i][j] == 0) == 1 for j in range(3))

print("VERIFIED: only K_2,3 / K_3,2 and C6 incidence types occur.")
