"""Finite sanity checks for QFORM-RANK3-OVERLAP1-SCHUR-CUT-v1.

These checks are not part of the proof.  They verify the exact determinant
identities numerically on random exact-rank-three matrices and on the
A_m stress family.
"""

from itertools import combinations
import numpy as np


def e2_cross(N):
    r, c = N.shape
    out = 0.0
    for K in combinations(range(r), 2):
        for L in combinations(range(c), 2):
            out += np.linalg.det(N[np.ix_(K, L)]) ** 2
    return out


def overlap_energy(A, i):
    idx = [j for j in range(A.shape[0]) if j != i]
    out = 0.0
    for K in combinations(idx, 2):
        rest = [j for j in idx if j not in K]
        for L in combinations(rest, 2):
            I = (i,) + K
            J = (i,) + L
            out += np.linalg.det(A[np.ix_(I, J)]) ** 2
    return out


def schur_disjoint_energy(A, i):
    a = A[i, i]
    idx = [j for j in range(A.shape[0]) if j != i]
    r = A[idx, i]
    S = A[np.ix_(idx, idx)] - np.outer(r, r) / a
    out = 0.0
    for K in combinations(range(len(idx)), 2):
        rest = [j for j in range(len(idx)) if j not in K]
        for L in combinations(rest, 2):
            out += np.linalg.det(S[np.ix_(K, L)]) ** 2
    return S, out


def cut_average_e2(S):
    m = S.shape[0]
    vals = []
    for mask in range(1 << m):
        P = [j for j in range(m) if (mask >> j) & 1]
        Q = [j for j in range(m) if not ((mask >> j) & 1)]
        vals.append(e2_cross(S[np.ix_(P, Q)]))
    return float(np.mean(vals)), float(np.max(vals))


def random_rank_three_checks():
    rng = np.random.default_rng(20260922)
    for n in (6, 7, 8):
        for trial in range(4):
            U, _ = np.linalg.qr(rng.normal(size=(n, 3)))
            lam = np.array([1.0 + 0.2 * trial, -1.4 - 0.1 * trial, 2.0])
            A = U @ np.diag(lam) @ U.T
            for i in range(n):
                a = A[i, i]
                if abs(a) < 1e-7:
                    continue
                M = overlap_energy(A, i)
                S, E = schur_disjoint_energy(A, i)
                assert np.linalg.matrix_rank(S, tol=1e-9) == 2
                assert np.isclose(M, a * a * E, rtol=2e-9, atol=2e-10)
                avg, mx = cut_average_e2(S)
                assert np.isclose(avg, E / 16.0, rtol=2e-9, atol=2e-10)
                assert mx + 1e-12 >= avg


def stress_family_checks():
    for m in range(2, 8):
        J = np.ones((m, m)) / m
        A = np.zeros((1 + 2 * m, 1 + 2 * m))
        A[0, 0] = 1.0
        A[1:1 + m, 1:1 + m] = J
        A[1 + m:, 1 + m:] = -J
        eig = np.linalg.eigvalsh(A)
        nz = eig[np.abs(eig) > 1e-9]
        assert np.allclose(np.sort(nz), np.array([-1.0, 1.0, 1.0]))
        M = overlap_energy(A, 0)
        expected = ((m - 1) / m) ** 2
        assert np.isclose(M, expected, rtol=2e-10, atol=2e-10)
        S, E = schur_disjoint_energy(A, 0)
        assert np.isclose(E, expected, rtol=2e-10, atol=2e-10)
        r = m // 2
        P = list(range(r)) + list(range(m, m + r))
        Q = [j for j in range(2 * m) if j not in P]
        N = S[np.ix_(P, Q)]
        sv = np.linalg.svd(N, compute_uv=False)
        Delta = sv[0] * sv[1]
        expected_delta = (r * (m - r)) / (m * m)
        assert np.isclose(Delta, expected_delta, rtol=2e-10, atol=2e-10)


if __name__ == "__main__":
    random_rank_three_checks()
    stress_family_checks()
    print("PASS: overlap-one Schur identities, cut expectation, and A_m stress family")
