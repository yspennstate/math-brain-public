#!/usr/bin/env python3
"""Exact Prüfer-sequence checker for HARD7-04 P0157 four-hub core trees.

For k=4 marked hub labels and t labeled bulk branch labels, enumerate every
labeled tree via its Prüfer word and count those in which every bulk branch
vertex has tree degree exactly 3.  The t=3 count is included to certify the
degree-sum cutoff.
"""
from itertools import product

def count_core_trees(k: int, t: int) -> int:
    n = k + t
    branches = range(k, n)
    total = 0
    for word in product(range(n), repeat=n - 2):
        deg = [1] * n
        for x in word:
            deg[x] += 1
        if all(deg[b] == 3 for b in branches):
            total += 1
    return total

counts = [count_core_trees(4, t) for t in range(4)]
expected = [16, 12, 6, 0]
for t, c in enumerate(counts):
    print(f"k=4 t={t} labeled_core_trees={c}")
assert counts == expected, (counts, expected)
print("ALL_EXACT_CHECKS_PASS = True")
