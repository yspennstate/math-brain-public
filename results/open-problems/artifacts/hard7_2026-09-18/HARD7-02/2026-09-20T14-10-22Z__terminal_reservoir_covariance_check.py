#!/usr/bin/env python3
"""
Exact self-check for HARD7-02 terminal-reservoir identities.

Checks, with exact integer/rational arithmetic:
  (1) Vandermonde factorization for the terminal residual count.
  (2) Conditional covariance of a uniform r-subset indicator:
        Cov(C-r/L*1) = [r(L-r)/(L(L-1))] (I-J/L).
  (3) Hypergeometric averaging conserves the covariance coefficient:
        E alpha(R) = d(n-d)/(n(n-1)), independent of L.
  (4) Exact endpoint probabilities and elementary product bounds.
  (5) Two deterministic rational examples of the block Gram determinant
      identity det([B C]^T[B C]) = det(B^T B) det(C^T P C).

This is a finite self-check, not an independent audit or a proof of the
asymptotic circular-law claim.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def zeros(m, n):
    return [[Fraction(0) for _ in range(n)] for _ in range(m)]


def outer(v, w):
    return [[v[i] * w[j] for j in range(len(w))] for i in range(len(v))]


def mat_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def transpose(A):
    return [list(r) for r in zip(*A)]


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))]
            for i in range(len(A))]


def matsub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def det_frac(A):
    A = [list(map(Fraction, row)) for row in A]
    n = len(A)
    if n == 0:
        return Fraction(1)
    sign = 1
    ans = Fraction(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if A[i][j] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            A[j], A[pivot] = A[pivot], A[j]
            sign *= -1
        p = A[j][j]
        ans *= p
        for i in range(j + 1, n):
            if A[i][j] != 0:
                f = A[i][j] / p
                for k in range(j, n):
                    A[i][k] -= f * A[j][k]
    return sign * ans


def inv_frac(A):
    A = [list(map(Fraction, row)) for row in A]
    n = len(A)
    M = [A[i] + [Fraction(int(i == j)) for j in range(n)]
         for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if M[i][j] != 0)
        if pivot != j:
            M[j], M[pivot] = M[pivot], M[j]
        p = M[j][j]
        M[j] = [x / p for x in M[j]]
        for i in range(n):
            if i != j and M[i][j] != 0:
                f = M[i][j]
                M[i] = [M[i][k] - f * M[j][k] for k in range(2 * n)]
    return [row[n:] for row in M]


def gram_col(A):
    return matmul(transpose(A), A)


def check_slice_case(n, d, L):
    lo = max(0, d - (n - L))
    hi = min(d, L)

    vandermonde = sum(comb(L, r) * comb(n - L, d - r)
                      for r in range(lo, hi + 1))
    assert vandermonde == comb(n, d)

    e_alpha = Fraction(0)
    for r in range(lo, hi + 1):
        pr = Fraction(comb(L, r) * comb(n - L, d - r), comb(n, d))
        alpha = Fraction(r * (L - r), L * (L - 1))
        e_alpha += pr * alpha

        subsets = list(combinations(range(L), r))
        q = Fraction(r, L)
        cov = zeros(L, L)
        for S in subsets:
            S = set(S)
            x = [Fraction(int(j in S)) - q for j in range(L)]
            cov = mat_add(cov, outer(x, x))
        cov = [[entry / len(subsets) for entry in row] for row in cov]

        H = [[Fraction(L - 1 if i == j else -1, L)
              for j in range(L)] for i in range(L)]
        target = [[alpha * H[i][j] for j in range(L)] for i in range(L)]
        assert cov == target

    expected = Fraction(d * (n - d), n * (n - 1))
    assert e_alpha == expected

    p0 = (Fraction(comb(n - L, d), comb(n, d))
          if d <= n - L else Fraction(0))
    pL = (Fraction(comb(n - L, d - L), comb(n, d))
          if d >= L else Fraction(0))

    assert p0 <= Fraction(n - L, n) ** d
    assert pL <= Fraction(d, n) ** L

    return p0, pL, expected


def check_block_gram(B, C):
    B = [[Fraction(x) for x in row] for row in B]
    C = [[Fraction(x) for x in row] for row in C]
    BtB = gram_col(B)
    BtB_inv = inv_frac(BtB)
    P = matsub(eye(len(B)), matmul(matmul(B, BtB_inv), transpose(B)))
    A = [B[i] + C[i] for i in range(len(B))]
    lhs = det_frac(gram_col(A))
    rhs = det_frac(BtB) * det_frac(matmul(matmul(transpose(C), P), C))
    assert lhs == rhs
    return lhs


def main():
    count = 0
    samples = []
    for n in range(4, 9):
        for d in range(1, n):
            for L in range(2, n):
                p0, pL, ea = check_slice_case(n, d, L)
                count += 1
                if (n, d, L) in {(4, 2, 2), (6, 2, 3), (8, 3, 4)}:
                    samples.append((n, d, L, p0, pL, ea))

    g1 = check_block_gram(
        [[1, 0], [0, 1], [1, 1]],
        [[1], [2], [0]],
    )
    g2 = check_block_gram(
        [[1, 0], [0, 1], [1, 1], [2, -1]],
        [[1, 0], [0, 1], [1, -1], [0, 2]],
    )

    print("HARD7-02 terminal-reservoir exact self-check")
    print("slice_cases_checked =", count)
    for row in samples:
        print("sample =", row)
    print("block_gram_example_1_det =", g1)
    print("block_gram_example_2_det =", g2)
    print("VANDERMONDE_FACTORISATION = PASS")
    print("CONDITIONAL_COVARIANCE = PASS")
    print("AVERAGED_ALPHA_CONSERVATION = PASS")
    print("ENDPOINT_PRODUCT_BOUNDS = PASS")
    print("BLOCK_GRAM_IDENTITY = PASS")
    print("ALL_EXACT_CHECKS_PASS = True")


if __name__ == "__main__":
    main()
