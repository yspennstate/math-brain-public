import itertools
import math
import numpy as np

# Corroborative checker for the theorem proved in
# runs/2026-09-15/2026-09-15T215211Z__report.md.
# Randomized tests are not substitutes for the proof.

SEED = 20260915215211
rng = np.random.default_rng(SEED)


def opnorm(M):
    return np.linalg.svd(M, compute_uv=False)[0]


def rand_unitary(d):
    Z = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    Q, R = np.linalg.qr(Z)
    ph = np.diag(R)
    ph = np.where(np.abs(ph) > 0, ph / np.abs(ph), 1.0)
    return Q @ np.diag(np.conj(ph))


def rand_psd(d, cond_exp=10.0):
    U = rand_unitary(d)
    vals = np.exp(rng.uniform(-cond_exp, 0.0, size=d))
    return U @ np.diag(vals) @ U.conj().T


def rand_projection(d, r):
    U = rand_unitary(d)
    Q = U[:, :r]
    return Q @ Q.conj().T


def pair_projection_ratio(P, B):
    p = opnorm(P @ B)
    if p < 1e-14:
        return 1.0, 1.0
    x = opnorm(P @ B @ B)
    y = opnorm(P @ B @ P @ B)
    return x * y / (p**4), (x + y) / (2 * p * p)


# Theorem 3.1 diagnostics: arbitrary-rank complex projections versus
# arbitrary complex PSD matrices in several dimensions.
min_prod = float("inf")
min_sum = float("inf")
for d in [2, 3, 5, 8]:
    for _ in range(400):
        r = int(rng.integers(1, d + 1))
        P = rand_projection(d, r)
        B = rand_psd(d)
        rp, rs = pair_projection_ratio(P, B)
        min_prod = min(min_prod, rp)
        min_sum = min(min_sum, rs)
        assert rp >= 1 - 2e-10, (d, r, rp)
        assert rs >= 1 - 2e-10, (d, r, rs)


def word_norm(A, w):
    M = np.eye(A[0].shape[0], dtype=complex)
    for j in w:
        M = M @ A[j]
    return opnorm(M)


def occupancy(A):
    S = Q211 = Q22 = Q31 = Q4 = 0.0
    for w in itertools.product(range(4), repeat=4):
        counts = sorted([w.count(j) for j in set(w)], reverse=True)
        z = word_norm(A, w)
        if counts == [1, 1, 1, 1]:
            S += z
        elif counts == [2, 1, 1]:
            Q211 += z
        elif counts == [2, 2]:
            Q22 += z
        elif counts == [3, 1]:
            Q31 += z
        elif counts == [4]:
            Q4 += z
    return S, Q211, Q22, Q31, Q4


# Section 5 scalar constant and scaled-projection occupancy diagnostics.
bound_RS = 13 / 2 + 3 / (6 ** (1 / 3))
bound_norm = 3 * bound_RS / 32

min_q22 = float("inf")
min_final = float("inf")
for d in [3, 5]:
    for _ in range(80):
        A = []
        for _i in range(4):
            r = int(rng.integers(1, d + 1))
            c = float(np.exp(rng.uniform(-2, 2)))
            A.append(c * rand_projection(d, r))
        S, Q211, Q22, Q31, Q4 = occupancy(A)
        P = sum(
            opnorm(A[i] @ A[j]) ** 2
            for i in range(4)
            for j in range(i + 1, 4)
        )
        if P > 1e-14:
            min_q22 = min(min_q22, Q22 / (6 * P))
            assert Q22 >= 6 * P - 2e-9 * max(1, Q22, 6 * P)
        if S > 1e-14:
            R = S + Q211 + Q22 + Q31 + Q4
            ratio = R / S
            min_final = min(min_final, ratio / bound_RS)
            assert ratio >= bound_RS - 2e-9 * max(1, ratio, bound_RS)

print("seed", SEED)
print("projection pair min xy/p^4", min_prod)
print("projection pair min (x+y)/(2p^2)", min_sum)
print("scaled-projection min Q22/(6P)", min_q22)
print("scaled-projection min (R/S)/bound_RS", min_final)
print("bound R/S", bound_RS)
print("normalized bound", bound_norm)
print("all checks passed")
