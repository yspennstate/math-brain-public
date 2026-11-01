#!/usr/bin/env python3
from fractions import Fraction


def matmul(A, B):
    m, k, n = len(A), len(B), len(B[0])
    assert len(A[0]) == k
    return [[sum((A[i][t] * B[t][j] for t in range(k)), Fraction(0))
             for j in range(n)] for i in range(m)]


def transpose(A):
    return [list(row) for row in zip(*A)]


def diag(vals):
    n = len(vals)
    return [[Fraction(vals[i]) if i == j else Fraction(0) for j in range(n)]
            for i in range(n)]


def eye(n):
    return diag([1] * n)


for m in range(1, 9):
    n = m + 1
    lam = [4 ** i for i in range(n)]
    sqrt_lam = [2 ** i for i in range(n)]

    # C e_i=e_{i+1}, with the final basis vector wrapped to e_0.
    C = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in range(m):
        C[i + 1][i] = Fraction(1)
    C[0][m] = Fraction(1)

    CtC = matmul(transpose(C), C)
    assert CtC == eye(n)

    A = diag(lam)
    Ah = diag(sqrt_lam)
    AhCtCAh = matmul(matmul(Ah, CtC), Ah)
    candidate = [[2 * A[i][j] - AhCtCAh[i][j]
                  for j in range(n)] for i in range(n)]
    assert candidate == A  # uniform p=2 candidate margin delta=1

    Ah_inv = diag([Fraction(1, s) for s in sqrt_lam])
    D = matmul(matmul(Ah, C), Ah_inv)
    DtD = matmul(transpose(D), D)
    # D is a weighted cyclic permutation. Its squared operator norm is max diagonal.
    assert all(DtD[i][j] == 0 for i in range(n) for j in range(n) if i != j)
    norm_sq = max(DtD[i][i] for i in range(n))
    assert norm_sq == 4

    # Exact stationary second moments for du_i+lambda_i u_i dt =
    # sqrt(lambda_{i-1}) u_{i-1} dW, with additive unit noise at i=0
    # and the cyclic final-to-zero edge. Common block scale L cancels.
    v0 = Fraction(1, 1) / (Fraction(2, 1) - Fraction(1, 2 ** m))
    v = [v0]
    for i in range(1, n):
        v.append(v[-1] / 8)

    # Verify all stationary balance equations exactly.
    assert -2 * lam[0] * v[0] + lam[m] * v[m] + 1 == 0
    for i in range(1, n):
        assert -2 * lam[i] * v[i] + lam[i - 1] * v[i - 1] == 0

    top_w = Fraction(lam[m] ** 2) * v[m]
    amplification = top_w / v0
    assert amplification == 2 ** m

    print(
        f"m={m} candidate_margin_delta=1 "
        f"rel_conjugation_norm_sq={norm_sq} "
        f"stationary_v0={v0} stationary_top_w={top_w} "
        f"top_over_base={amplification}"
    )

print("ALL_EXACT_CHECKS_PASSED")
