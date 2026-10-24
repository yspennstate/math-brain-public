import itertools
import math
import numpy as np

SEED = 20260915232246
rng = np.random.default_rng(SEED)


def opnorm(M):
    return np.linalg.svd(M, compute_uv=False)[0]


def rand_psd(d, scale=1.0):
    Z = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    H = Z @ Z.conj().T
    H /= opnorm(H)
    return scale * H


def aligned_pair(d=5):
    # One dominant common scalar direction; a noncommuting lower block remains.
    A0 = 3.0
    B0 = 2.5
    Al = rand_psd(d - 1, scale=0.7)
    Bl = rand_psd(d - 1, scale=0.8)
    A = np.zeros((d, d), dtype=complex)
    B = np.zeros((d, d), dtype=complex)
    A[0, 0] = A0
    B[0, 0] = B0
    A[1:, 1:] = Al
    B[1:, 1:] = Bl
    return A, B


def check_pair(A, B, tol=5e-11):
    T = A @ B
    p = opnorm(T)
    K = A @ B @ B @ A
    vals, vecs = np.linalg.eigh(K)
    v = vecs[:, -1]
    a = np.vdot(v, A @ v).real
    residual = np.linalg.norm(A @ v - a * v)
    x = opnorm(A @ A @ B @ B)
    y = opnorm(A @ B @ A @ B)
    prod_ratio = x * y / (p ** 4)
    sum_ratio = (x + y) / (2 * p * p)
    assert residual < tol, residual
    assert prod_ratio >= 1 - tol, prod_ratio
    assert sum_ratio >= 1 - tol, sum_ratio
    return residual, prod_ratio, sum_ratio


mins = [float("inf"), float("inf")]
max_residual = 0.0
for d in (3, 4, 6, 9):
    for _ in range(100):
        A, B = aligned_pair(d)
        residual, pr, sr = check_pair(A, B)
        max_residual = max(max_residual, residual)
        mins[0] = min(mins[0], pr)
        mins[1] = min(mins[1], sr)


def aligned_quadruple(d=5):
    # All four matrices share a dominant scalar direction, while their lower
    # PSD blocks are independently random and generally noncommuting.
    mats = []
    for i in range(4):
        M = np.zeros((d, d), dtype=complex)
        M[0, 0] = 3.0 + 0.2 * i
        M[1:, 1:] = rand_psd(d - 1, scale=0.45 + 0.05 * i)
        mats.append(M)
    return mats


def word_norm(mats, inds):
    W = np.eye(mats[0].shape[0], dtype=complex)
    for i in inds:
        W = W @ mats[i]
    return opnorm(W)


def occupancy_stats(mats):
    S = sum(word_norm(mats, perm) for perm in itertools.permutations(range(4)))
    R = sum(word_norm(mats, inds) for inds in itertools.product(range(4), repeat=4))
    P = sum(
        opnorm(mats[i] @ mats[j]) ** 2
        for i in range(4)
        for j in range(i + 1, 4)
    )
    Q22 = 0.0
    for inds in itertools.product(range(4), repeat=4):
        counts = sorted(
            [inds.count(i) for i in range(4) if inds.count(i)], reverse=True
        )
        if counts == [2, 2]:
            Q22 += word_norm(mats, inds)
    return S, R, P, Q22


bound_RS = 13 / 2 + 3 / (6 ** (1 / 3))
bound_norm = 3 * bound_RS / 32
min_q22_ratio = float("inf")
min_RS_ratio = float("inf")
for d in (3, 5, 7):
    for _ in range(20):
        mats = aligned_quadruple(d)
        S, R, P, Q22 = occupancy_stats(mats)
        min_q22_ratio = min(min_q22_ratio, Q22 / (6 * P))
        min_RS_ratio = min(min_RS_ratio, (R / S) / bound_RS)
        assert Q22 >= 6 * P * (1 - 2e-10)
        assert R / S >= bound_RS * (1 - 2e-10)

print(f"seed={SEED}")
print(f"max alignment residual={max_residual:.3e}")
print(f"min pair product ratio xy/p^4={mins[0]:.15f}")
print(f"min pair sum ratio (x+y)/(2p^2)={mins[1]:.15f}")
print(f"min quadruple Q22/(6P)={min_q22_ratio:.15f}")
print(f"proved class bound R/S={bound_RS:.15f}")
print(f"proved normalized factor={bound_norm:.15f}")
print(f"min sampled (R/S)/bound={min_RS_ratio:.15f}")
