#!/usr/bin/env python3
"""Exact finite check for R03/F0002 switching-normalized richness.

No floating point is used.  Determinants and adjugates are evaluated by the
Leibniz formula over Python integers.  For an invertible symmetric 0/1 core C
of size d=m-1, the normalized sign matrix

    B = [[1, 1^T], [1, J-2C]]

satisfies

    N(B) = 2 * #{z in {0,1}^d : z^T C^{-1} z in {0,1}}.

The script enumerates all normalized cores through d=5 (equivalently m<=6)
and reports the exact richness distributions and exact means.
"""

from collections import Counter
from fractions import Fraction
from itertools import permutations, product

_PERMS = {}


def signed_permutations(n):
    if n not in _PERMS:
        out = []
        for p in permutations(range(n)):
            inv = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
            out.append((p, -1 if inv & 1 else 1))
        _PERMS[n] = out
    return _PERMS[n]


def det_exact(A):
    n = len(A)
    if n == 0:
        return 1
    total = 0
    for p, sgn in signed_permutations(n):
        term = 1
        for i in range(n):
            term *= A[i][p[i]]
        total += sgn * term
    return total


def adjugate_exact(A):
    n = len(A)
    if n == 0:
        return []
    adj = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            minor = [
                [A[r][c] for c in range(n) if c != j]
                for r in range(n) if r != i
            ]
            cof = det_exact(minor)
            if (i + j) & 1:
                cof = -cof
            adj[j][i] = cof
    return adj


def quad_numerator(z, adj):
    return sum(
        z[i] * adj[i][j] * z[j]
        for i in range(len(z))
        for j in range(len(z))
    )


def symmetric_zero_one_from_bits(d, bits):
    C = [[0] * d for _ in range(d)]
    t = 0
    for i in range(d):
        for j in range(i, d):
            v = (bits >> t) & 1
            C[i][j] = C[j][i] = v
            t += 1
    return C


def distribution(m):
    d = m - 1
    total = 1 << (d * (d + 1) // 2)
    inv = 0
    hist = Counter()
    for bits in range(total):
        C = symmetric_zero_one_from_bits(d, bits)
        determinant = det_exact(C)
        if determinant == 0:
            continue
        inv += 1
        adj = adjugate_exact(C)
        good = 0
        for z in product((0, 1), repeat=d):
            qnum = quad_numerator(z, adj)
            # q = qnum/determinant lies in {0,1} exactly iff qnum is 0 or det.
            if qnum == 0 or qnum == determinant:
                good += 1
        hist[2 * good] += 1
    sum_n = sum(N * count for N, count in hist.items())
    return total, inv, hist, Fraction(sum_n, total), Fraction(sum_n, inv)


def main():
    expected_m4 = {8: 8, 12: 24}
    expected_m5 = {10: 31, 12: 60, 16: 20, 18: 225, 20: 192}
    expected_m6 = {
        12: 401, 14: 120, 16: 900, 18: 360, 20: 570, 22: 720,
        24: 3870, 26: 1080, 28: 405, 30: 480, 32: 540, 34: 1440,
        36: 2790, 38: 3600, 40: 1260, 48: 60,
    }

    rows = {}
    for m in range(1, 7):
        total, inv, hist, mean_all, mean_inv = distribution(m)
        rows[m] = (total, inv, dict(sorted(hist.items())), mean_all, mean_inv)
        print(
            f"m={m} normalized_cores={total} invertible={inv} "
            f"distribution={dict(sorted(hist.items()))} "
            f"E_N={mean_all} E_N_given_invertible={mean_inv}"
        )

    assert rows[1][2] == {2: 1}
    assert rows[2][2] == {4: 1}
    assert rows[3][2] == {6: 4}
    assert rows[4][2] == expected_m4
    assert rows[5][2] == expected_m5
    assert rows[6][2] == expected_m6
    assert rows[4][3] == Fraction(11, 2)
    assert rows[5][3] == Fraction(1155, 128)
    assert rows[6][3] == Fraction(69759, 4096)

    # The m=4 normalized counts lift by the exact fiber size 2^m to the
    # previous full-sign enumeration: 8*16=128 and 24*16=384.
    assert rows[4][2][8] * (1 << 4) == 128
    assert rows[4][2][12] * (1 << 4) == 384

    print("EXACT_CHECK_PASS")


if __name__ == "__main__":
    main()
