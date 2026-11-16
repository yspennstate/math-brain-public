"""Brute-force check for Grimmett-Holmes Open Problem 3.8 (K(P)={1} for a.e. P).

Claim: if a grand coupling mu of P has k(mu) >= 2, then supp(mu) is contained in End(H) for a
nonempty k-uniform family H of k-subsets (k >= 2), where End(H) = maps sending every member of H
onto a member of H. So P lies in conv{M_f : f in End(H)}. The claim to check: for every such H
this polytope has affine dimension < n(n-1), the dimension of the set of stochastic matrices.
We also check the core equation: with e an idempotent of minimal rank in End(H), image W, every
f in End(H) has e o f bijective on W.

Usage: python check_dims.py N   (N = 3, 4 or 5; seconds)
"""
import itertools, sys
import numpy as np

n = int(sys.argv[1]) if len(sys.argv) > 1 else 4
S = range(n)
maps = list(itertools.product(S, repeat=n))
full = n * (n - 1)
worst = 0
count = 0
for k in range(2, n + 1):
    ksets = [frozenset(c) for c in itertools.combinations(S, k)]
    for mask in range(1, 2 ** len(ksets)):
        H = [ksets[i] for i in range(len(ksets)) if mask >> i & 1]
        Hs = set(H)
        End = [f for f in maps if all(frozenset(f[x] for x in A) in Hs for A in H)]
        # affine dimension of {M_f}: rank of differences of the vectors M_f
        V = np.zeros((len(End), n * n))
        for r, f in enumerate(End):
            for x in S:
                V[r, x * n + f[x]] = 1
        d = np.linalg.matrix_rank(V[1:] - V[0]) if len(End) > 1 else 0
        worst = max(worst, d)
        count += 1
        assert d < full, (k, H, d)
        # core equation
        rmin = min(len(set(f)) for f in End)
        e = next(f for f in End if len(set(f)) == rmin and all(f[f[x]] == f[x] for x in S))
        W = sorted(set(e))
        for f in End:
            assert len({e[f[x]] for x in W}) == len(W)
print(f"n={n}: {count} families checked, largest affine dimension {worst} < {full}; core equation holds")
