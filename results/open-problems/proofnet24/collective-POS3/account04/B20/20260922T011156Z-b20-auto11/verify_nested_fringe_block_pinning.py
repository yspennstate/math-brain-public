#!/usr/bin/env python3
"""Exact regressions for the POS3 nested-fringe and block-pinning lemmas.

The first check exhausts nested integer intervals and common truncation windows.
The second uses the 15-element module-prime witness published by account02/B19.
It validates only exact event/counting identities on that witness; because that
poset has balanced pairs, it is not a test of the no-balanced-pair hypothesis.
"""
from fractions import Fraction


def count_order(A, B, forward=True):
    if forward:
        return sum(1 for x in A for y in B if x <= y)
    return sum(1 for x in A for y in B if y <= x)


nested_cases = 0
for m in range(9):
    for a0 in range(m + 1):
        for b0 in range(a0, m + 1):
            for c0 in range(a0, b0 + 1):
                for d0 in range(c0, b0 + 1):
                    # [c0,d0] is nested in [a0,b0].
                    for L in range(m + 1):
                        for U in range(L, m + 1):
                            a, b = max(a0, L), min(b0, U)
                            c, d = max(c0, L), min(d0, U)
                            if a > b or c > d:
                                continue
                            A = range(a, b + 1)
                            B = range(c, d + 1)
                            lower_fringe = c - a
                            upper_fringe = b - d
                            expected = len(B) * (lower_fringe - upper_fringe)
                            observed = count_order(A, B, True) - count_order(A, B, False)
                            assert observed == expected
                            nested_cases += 1

print("nested_interval_window_cases", nested_cases)
print("nested_closed_form", "PASS")

N = 15
COVERS = [
    (0,1),(0,5),(1,2),(2,3),(2,12),(3,4),(3,9),(5,6),(5,11),
    (6,2),(6,7),(7,4),(7,8),(8,9),(9,14),(10,1),(10,11),(11,12),
    (12,8),(12,13),(13,4),(13,14),
]
CHAINS = [list(range(0,5)), list(range(5,10)), list(range(10,15))]
LSTAR = (0,10,5,6,1,11,2,7,12,3,13,8,9,4,14)

lt = [[False] * N for _ in range(N)]
for a, b in COVERS:
    lt[a][b] = True
for k in range(N):
    for i in range(N):
        if lt[i][k]:
            for j in range(N):
                if lt[k][j]:
                    lt[i][j] = True

pred = []
for j in range(N):
    mask = 0
    for i in range(N):
        if lt[i][j]:
            mask |= 1 << i
    pred.append(mask)

extensions = []
def enumerate_extensions(mask, seq):
    if len(seq) == N:
        extensions.append(tuple(seq))
        return
    for v in range(N):
        if (mask >> v) & 1:
            continue
        if pred[v] & ~mask == 0:
            enumerate_extensions(mask | (1 << v), seq + [v])

enumerate_extensions(0, [])
assert len(extensions) == 6294

chain_of = {}
for ci, chain in enumerate(CHAINS):
    for v in chain:
        chain_of[v] = ci

blocks = []
i = 0
while i < N:
    ci = chain_of[LSTAR[i]]
    j = i
    xs = []
    while j < N and chain_of[LSTAR[j]] == ci:
        xs.append(LSTAR[j])
        j += 1
    blocks.append((ci, tuple(xs), i, j))
    i = j

star_pos = {v: i for i, v in enumerate(LSTAR)}
rows = []
for ci, xs, left_index, right_index in blocks:
    for cj, chain in enumerate(CHAINS):
        if ci == cj:
            continue
        g = sum(star_pos[y] < left_index for y in chain)
        good = bad_left = bad_right = bad_union = 0
        for ext in extensions:
            pos = {v: i for i, v in enumerate(ext)}
            J = [sum(pos[y] < pos[x] for y in chain) for x in xs]
            assert all(J[k] <= J[k + 1] for k in range(len(J) - 1))
            left_bad = J[0] < g
            right_bad = J[-1] > g
            pinned = all(t == g for t in J)
            assert pinned == (not (left_bad or right_bad))
            good += int(pinned)
            bad_left += int(left_bad)
            bad_right += int(right_bad)
            bad_union += int(left_bad or right_bad)
        assert good + bad_union == len(extensions)
        assert bad_union <= bad_left + bad_right
        rows.append((xs, cj, g, good, bad_left, bad_right, bad_union))

minimum = min(rows, key=lambda row: row[3])
xs, cj, g, good, bad_left, bad_right, bad_union = minimum
print("extensions", len(extensions))
print("block_other_chain_cases", len(rows))
print("all_complement_identities", "PASS")
print("all_union_bounds", "PASS")
print("minimum_observed_pinned", xs, "other_chain", cj, "gap", g,
      "count", good, "fraction", Fraction(good, len(extensions)))
print("corresponding_bad_counts", bad_left, bad_right, bad_union)
print("POS3_NESTED_FRINGE_AND_BLOCK_PINNING_REGRESSION_PASS")
