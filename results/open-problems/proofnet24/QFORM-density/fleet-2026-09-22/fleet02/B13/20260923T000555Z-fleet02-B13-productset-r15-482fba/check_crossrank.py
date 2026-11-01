import itertools
import math
import numpy as np

np.random.seed(230923)


def find_pq(A, r, tol=1e-10):
    n = A.shape[0]
    for P in itertools.combinations(range(n), r):
        rem = [i for i in range(n) if i not in P]
        for Q in itertools.combinations(rem, r):
            if abs(np.linalg.det(A[np.ix_(P, Q)])) > tol:
                return list(P), list(Q)
    raise RuntimeError("no maximal disjoint pivot found")


def reconstruct(A, r):
    n = A.shape[0]
    if r == 0:
        return np.diag(np.diag(A)), np.zeros_like(A)
    P, Q = find_pq(A, r)
    S = P + Q
    K = [i for i in range(n) if i not in S]
    B = A[np.ix_(P, Q)]
    H = np.block([[np.zeros((r, r)), 2 * B],
                  [2 * B.T, np.zeros((r, r))]])
    C = A[np.ix_(S, K)]
    R1 = np.zeros_like(A)
    R1[np.ix_(S, S)] = H
    R1[np.ix_(S, K)] = C
    R1[np.ix_(K, S)] = C.T
    R1[np.ix_(K, K)] = C.T @ np.linalg.inv(H) @ C
    diff = A[np.ix_(S, S)] - H
    np.fill_diagonal(diff, 0.0)
    R2 = np.zeros_like(A)
    R2[np.ix_(S, S)] = diff
    R = R1 + R2
    D = np.diag(np.diag(A - R))
    return D, R


max_error = 0.0
max_rank_ratio = 0.0
trials = 0
for n in [7, 8, 9, 10]:
    for r in [1, 2, 3]:
        if 2 * r > n:
            continue
        for _ in range(20):
            U = np.random.randn(n, r)
            A = np.diag(np.random.randn(n)) + U @ U.T
            D, R = reconstruct(A, r)
            err = np.max(np.abs(A - D - R))
            rank = np.linalg.matrix_rank(R, tol=1e-8)
            assert err < 1e-7
            assert rank <= 4 * r
            max_error = max(max_error, err)
            max_rank_ratio = max(max_rank_ratio, rank / (4 * r))
            trials += 1

C3 = 9 * math.sqrt(3 * math.e)
C5 = 5 * math.sqrt(2 * math.e)
print("QFORM_B13_R15_CHECK_PASS")
print("trials", trials)
print("max_reconstruction_error", f"{max_error:.3e}")
print("max_rank_over_4r", f"{max_rank_ratio:.6f}")
print("C3", f"{C3:.15f}")
print("C5", f"{C5:.15f}")
print("C5_over_C3", f"{C5/C3:.15f}")
