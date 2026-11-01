"""Deterministic numerical regression for QFORM-RANK3-OVERLAP1-INTEGRATED-FOURIER-v1.

This is not a proof. It checks the exact exterior-mass identities on random Parseval frames
and prints the two analytic constants used in REPORT.md.
"""
import itertools
import math
import numpy as np

rng = np.random.default_rng(20260922)
max_overlap_error = 0.0
max_pair_error = 0.0

for _ in range(50):
    x = rng.normal(size=(7, 3))
    r, _ = np.linalg.qr(x)
    triples = list(itertools.combinations(range(7), 3))
    w = {I: float(np.linalg.det(r[list(I), :]) ** 2) for I in triples}

    d1 = sum(
        w[I] * w[J]
        for I in triples
        for J in triples
        if len(set(I).intersection(J)) == 1
    )

    rhs = 0.0
    for i in range(7):
        c = float(r[i] @ r[i])
        if c <= 1e-14:
            continue
        e = r[i] / math.sqrt(c)
        _, _, vh = np.linalg.svd(e.reshape(1, 3))
        W = vh[1:].T
        pairw = {}
        others = [j for j in range(7) if j != i]
        for j, k in itertools.combinations(others, 2):
            sj = W.T @ r[j]
            sk = W.T @ r[k]
            pairw[(j, k)] = float(np.linalg.det(np.column_stack([sj, sk])) ** 2)
            I = tuple(sorted((i, j, k)))
            max_pair_error = max(max_pair_error, abs(pairw[(j, k)] - w[I] / c))

        di = sum(
            pairw[P] * pairw[Q]
            for P in pairw
            for Q in pairw
            if set(P).isdisjoint(Q)
        )
        rhs += c * c * di

    max_overlap_error = max(max_overlap_error, abs(d1 - rhs))

print(f"max pair factorization error = {max_pair_error:.3e}")
print(f"max D1 identity error       = {max_overlap_error:.3e}")
print(f"C_one_pivot = {4 * 3**0.25 * math.sqrt(math.pi):.12f}")
print(f"C_E1        = {4 * math.sqrt(3 * math.pi):.12f}")
assert max_pair_error < 1e-12
assert max_overlap_error < 1e-12
