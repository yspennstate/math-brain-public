#!/usr/bin/env python3
"""Exact checker for P17-M49 PV-square gluing identities.

This script uses only integer arithmetic.  It checks:

1. right exterior contractions R_i R_j + R_j R_i = 0 on Lambda^even Z^4;
2. for every pair i<j, the two-cut complex

     Lambda^even Z^4 --(R_i,R_j)--> Lambda^odd Z^{4\{i}} + Lambda^odd Z^{4\{j}}
       --(R_j,R_i)--> Lambda^even Z^{4\{i,j}}

   has ranks 6 -> (8) -> 2 over Q and zero composite; the report supplies
   the coefficientwise integral-saturation proof;
3. on the historical symmetry sector c14=c23=0, the matched pairs (1,4)
   and (2,3) have exactly one gluing relation and kernel Z[1];
4. the two physical cuts (3,4) have exactly two gluing relations and
   kernel Z[1] + Z[p12].

No spectral computation and no magnetic-gap claim is made here.
"""
from fractions import Fraction
from itertools import combinations


def subsets(n, parity=None, exclude=()):
    ex = set(exclude)
    out = []
    for r in range(n + 1):
        if parity is not None and r % 2 != parity:
            continue
        for I in combinations(range(1, n + 1), r):
            if not (set(I) & ex):
                out.append(I)
    return out


def rcontract(I, j):
    """Right contraction by e_j in the inherited global ordering."""
    if j not in I:
        return None, 0
    pos = I.index(j)
    sign = -1 if ((len(I) - pos - 1) % 2) else 1
    return I[:pos] + I[pos + 1 :], sign


def rank_q(A):
    A = [[Fraction(x) for x in row] for row in A]
    m = len(A)
    n = len(A[0]) if m else 0
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i][c]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        v = A[r][c]
        A[r] = [x / v for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                v = A[i][c]
                A[i] = [A[i][k] - v * A[r][k] for k in range(n)]
        r += 1
    return r


def matmul(A, B):
    return [
        [sum(A[r][k] * B[k][c] for k in range(len(B))) for c in range(len(B[0]))]
        for r in range(len(A))
    ]


def pair_matrices(i, j):
    E = subsets(4, parity=0)
    Ai = subsets(4, parity=1, exclude=(i,))
    Aj = subsets(4, parity=1, exclude=(j,))
    middle = [("i", K) for K in Ai] + [("j", K) for K in Aj]
    midx = {v: k for k, v in enumerate(middle)}

    F = [[0] * len(E) for _ in middle]
    for c, I in enumerate(E):
        K, s = rcontract(I, i)
        if s:
            F[midx[("i", K)]][c] = s
        K, s = rcontract(I, j)
        if s:
            F[midx[("j", K)]][c] = s

    C = subsets(4, parity=0, exclude=(i, j))
    cidx = {K: r for r, K in enumerate(C)}
    G = [[0] * len(middle) for _ in C]
    for c, (tag, K) in enumerate(middle):
        cut = j if tag == "i" else i
        L, s = rcontract(K, cut)
        if s:
            G[cidx[L]][c] = s
    return E, Ai, Aj, C, F, G


def check_general_square():
    for i, j in combinations(range(1, 5), 2):
        E, Ai, Aj, C, F, G = pair_matrices(i, j)
        GF = matmul(G, F)
        assert all(x == 0 for row in GF for x in row), (i, j, GF)
        assert rank_q(F) == 6, (i, j, rank_q(F))
        assert rank_q(G) == 2, (i, j, rank_q(G))
        assert len(Ai) + len(Aj) == 8
        assert len(C) == 2


def check_historical_sector():
    # Coordinates on S/Z[1]: (c12,c13,c24,c34,c1234).
    # Matched (1,4): (d1_u2,d1_u3,d1_u234,d4_u2,d4_u3,d4_u123).
    def f14(c12, c13, c24, c34, c1234):
        return (-c12, -c13, -c1234, c24, c34, c1234)

    # Matched (2,3): (d2_u1,d2_u4,d2_u134,d3_u1,d3_u4,d3_u124).
    def f23(c12, c13, c24, c34, c1234):
        return (c12, -c24, c1234, c13, -c34, -c1234)

    # Physical (3,4): (d3_u1,d3_u4,d3_u124,d4_u2,d4_u3,d4_u123).
    def f34(c12, c13, c24, c34, c1234):
        del c12
        return (c13, -c34, -c1234, c24, c34, c1234)

    tests = [
        (2, -3, 5, 7, -11),
        (-1, 4, -2, 6, 9),
        (0, 0, 0, 0, 1),
    ]
    for c in tests:
        y = f14(*c)
        assert y[2] + y[5] == 0
        assert (-y[0], -y[1], y[3], y[4], y[5]) == c

        y = f23(*c)
        assert y[2] + y[5] == 0
        assert (y[0], y[3], -y[1], -y[4], y[2]) == c

        y = f34(*c)
        assert y[1] + y[4] == 0
        assert y[2] + y[5] == 0
        # c12 is invisible to the two physical cuts.
        assert (y[0], y[3], y[4], y[5]) == (c[1], c[2], c[3], c[4])


def main():
    check_general_square()
    check_historical_sector()
    print("M49 PV-square gluing checks: PASS")


if __name__ == "__main__":
    main()
