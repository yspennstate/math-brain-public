#!/usr/bin/env python3
"""Exact B24 census for F0011 sign-Gram support fibers, r=2..6.

A sign class [x]={x,-x} is represented canonically by x_1=+1.  For each
r-subset S of the 2^(r-1) sign classes, the Gram sum K(S)=sum_{[x] in S}xx^T
has diagonal r, so it is keyed exactly by its off-diagonal entries.  The
script counts all support fibers, finds the global maximum, and verifies that
a global-max fiber has a positive-definite witness.  Bareiss elimination is
used for exact integer determinants; no floating point arithmetic occurs.
"""
from itertools import product, combinations
from collections import defaultdict


def bareiss_det(A):
    A = [row[:] for row in A]
    n = len(A)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        piv = k
        while piv < n and A[piv][k] == 0:
            piv += 1
        if piv == n:
            return 0
        if piv != k:
            A[k], A[piv] = A[piv], A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * pivot - A[i][k] * A[k][j]) // prev
        for i in range(k + 1, n):
            A[i][k] = 0
        prev = pivot
    return sign * A[n - 1][n - 1]


def data_for_r(r):
    reps = [(1,) + tail for tail in product((-1, 1), repeat=r - 1)]
    pairs = [(i, j) for i in range(r) for j in range(i + 1, r)]
    feats = [tuple(x[i] * x[j] for i, j in pairs) for x in reps]

    counts = defaultdict(int)
    total = 0
    for inds in combinations(range(len(reps)), r):
        s = [0] * len(pairs)
        for idx in inds:
            f = feats[idx]
            for a, value in enumerate(f):
                s[a] += value
        counts[tuple(s)] += 1
        total += 1

    max_mult = max(counts.values())
    max_keys = {key for key, value in counts.items() if value == max_mult}

    positive = None
    for inds in combinations(range(len(reps)), r):
        s = [0] * len(pairs)
        for idx in inds:
            f = feats[idx]
            for a, value in enumerate(f):
                s[a] += value
        key = tuple(s)
        if key not in max_keys:
            continue

        K = [[r if i == j else 0 for j in range(r)] for i in range(r)]
        q = 0
        for i in range(r):
            for j in range(i + 1, r):
                K[i][j] = K[j][i] = key[q]
                q += 1
        detK = bareiss_det(K)
        if detK > 0:
            positive = (key, inds, detK, K)
            break

    assert positive is not None, (r, max_mult, len(max_keys))
    key, inds, detK, K = positive

    # Independent exact consistency check by rebuilding C C^T.
    C = [[reps[j][i] for j in inds] for i in range(r)]
    K2 = [
        [sum(C[i][a] * C[j][a] for a in range(r)) for j in range(r)]
        for i in range(r)
    ]
    assert K2 == K
    assert bareiss_det(K) > 0

    return reps, total, len(counts), max_mult, len(max_keys), key, inds, detK, K


print("F0011 exact sign-Gram support-fiber census")
print("canonical sign classes use first coordinate +1; fibers count r-subsets S with sum_{[x] in S} xx^T = K")
for r in range(2, 7):
    reps, total, nkeys, mult, nmax, key, inds, detK, K = data_for_r(r)
    print(
        f"r={r} classes={len(reps)} supports={total} distinct_K={nkeys} "
        f"global_max_support_fiber={mult} number_of_global_max_K={nmax}"
    )
    print(f"  positive_definite_max_witness_indices={inds} detK={detK}")
    print(f"  offdiag_key={key}")
    print("  columns=" + ";".join("".join("+" if a == 1 else "-" for a in reps[j]) for j in inds))
    print("  K=" + ";".join(",".join(str(v) for v in row) for row in K))
print("ALL_EXACT_ASSERTIONS_PASS")
