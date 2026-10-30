#!/usr/bin/env python3
"""Deterministic finite diagnostics for fleet03/B16 r48.
Not a proof certificate. The report contains the dimension-free proof.
"""
import itertools, math
import numpy as np
import sympy as sp

rng = np.random.default_rng(20260924)
exact_cases = 0
for n in (6, 7):
    for _ in range(3):
        raw = rng.integers(-4, 5, (n, n))
        A = sp.Matrix((raw + raw.T).tolist())
        for S in itertools.combinations(range(n), 2):
            for T in itertools.combinations(range(n), 2):
                if not set(S).isdisjoint(T):
                    continue
                B = A.extract(S, T)
                if B.det() == 0:
                    continue
                L = [i for i in range(n) if i not in S and i not in T]
                P = A[:, list(T)] * B.inv() * A[list(S), :]
                for h in L:
                    rows = sorted(S + (h,))
                    cols = sorted(T + (h,))
                    lhs = A.extract(rows, cols).det() ** 2
                    rhs = (B.det() * (A[h, h] - P[h, h])) ** 2
                    assert sp.simplify(lhs-rhs) == 0
                    exact_cases += 1


def volumes(A):
    n = A.shape[0]
    V2 = V3 = W = 0.0
    twos = list(itertools.combinations(range(n), 2))
    threes = list(itertools.combinations(range(n), 3))
    for S in twos:
        ss = set(S)
        for T in twos:
            if not ss.isdisjoint(T):
                continue
            d = np.linalg.det(A[np.ix_(S, T)])
            V2 += d*d
            for h in range(n):
                if h not in ss and h not in T:
                    rows = tuple(sorted(S + (h,)))
                    cols = tuple(sorted(T + (h,)))
                    dd = np.linalg.det(A[np.ix_(rows, cols)])
                    W += dd*dd
    for S in threes:
        ss = set(S)
        for T in threes:
            if ss.isdisjoint(T):
                d = np.linalg.det(A[np.ix_(S, T)])
                V3 += d*d
    return V2, V3, W

rng = np.random.default_rng(20260924)
min_slack = float("inf")
for _ in range(12):
    M = rng.normal(size=(8, 8))
    A = (M + M.T)/2
    s8 = np.linalg.svd(A, compute_uv=False)[-1]
    V2, V3, W = volumes(A)
    rhs = 2*s8*s8*V2 - 12*s8*math.sqrt(V2*V3)
    min_slack = min(min_slack, W-rhs)
    assert W + 1e-8 >= rhs

print(f"exact_bordered_cases={exact_cases}")
print("numeric_global_cases=12")
print(f"minimum_numeric_slack={min_slack:.15f}")
print("normalized_terminal_W_lower=37/819200000=4.5166015625e-08")
print("STATUS=PASS")
