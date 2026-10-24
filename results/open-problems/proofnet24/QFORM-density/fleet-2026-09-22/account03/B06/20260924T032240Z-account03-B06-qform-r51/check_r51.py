"""Finite sanity checks for account03/B06 r51.

These tests do not prove the theorem.  They numerically verify the finite-dimensional
algebraic identities used in REPORT.md on fixed-seed random matrices.
"""
from itertools import combinations
import math
import numpy as np

RNG = np.random.default_rng(51)


def one_case(n: int):
    R = RNG.normal(size=(3, n))
    while np.linalg.matrix_rank(R) < 3:
        R = RNG.normal(size=(3, n))

    M = RNG.normal(size=(3, 3))
    M = (M + M.T) / 2
    while abs(np.linalg.det(M)) < 0.2:
        M = RNG.normal(size=(3, 3))
        M = (M + M.T) / 2

    triples = list(combinations(range(n), 3))
    weights = np.array([np.linalg.det(R[:, I]) ** 2 for I in triples])
    T_R = np.linalg.det(R @ R.T)
    mu = weights / T_R
    plucker_sum_error = abs(mu.sum() - 1.0)

    Omega = 0.0
    for a, I in enumerate(triples):
        sI = set(I)
        for b, J in enumerate(triples):
            if sI.isdisjoint(J):
                Omega += mu[a] * mu[b]

    best = -1.0
    best_split = None
    for mask in range(1 << n):
        S = [i for i in range(n) if (mask >> i) & 1]
        T = [i for i in range(n) if not ((mask >> i) & 1)]
        if len(S) < 3 or len(T) < 3:
            continue
        V_S = np.linalg.det(R[:, S] @ R[:, S].T)
        V_T = np.linalg.det(R[:, T] @ R[:, T].T)
        value = V_S * V_T
        if value > best:
            best = value
            best_split = (S, T)

    expected_cut_product = T_R**2 * Omega / 64.0
    assert best + 1e-10 >= expected_cut_product

    S, T = best_split
    N = R[:, S].T @ M @ R[:, T]
    singular_values = np.linalg.svd(N, compute_uv=False)
    Delta = np.prod(singular_values[:3])
    exact = abs(np.linalg.det(M)) * math.sqrt(
        np.linalg.det(R[:, S] @ R[:, S].T)
        * np.linalg.det(R[:, T] @ R[:, T].T)
    )
    cross_rel_error = abs(Delta - exact) / (1.0 + abs(exact))

    avg_delta = 0.0
    for a, H in enumerate(triples):
        C = [i for i in range(n) if i not in H]
        if len(C) >= 3:
            delta_H = np.linalg.det(R[:, C] @ R[:, C].T) / T_R
        else:
            delta_H = 0.0
        avg_delta += mu[a] * delta_H
    complement_error = abs(avg_delta - Omega)

    return {
        "n": n,
        "Omega3": Omega,
        "best_cut_product": best,
        "expected_cut_product": expected_cut_product,
        "plucker_sum_error": plucker_sum_error,
        "cross_rel_error": cross_rel_error,
        "complement_error": complement_error,
    }


if __name__ == "__main__":
    rows = [one_case(n) for n in (6, 7, 9)]
    for row in rows:
        print(row)
    assert max(r["plucker_sum_error"] for r in rows) < 1e-10
    assert max(r["cross_rel_error"] for r in rows) < 1e-10
    assert max(r["complement_error"] for r in rows) < 1e-10
    print("QFORM_B06_R51_CHECK_PASS")
