#!/usr/bin/env python3
"""Exact self-check for HARD7-02: W=1 scalar-Rademacher fresh-closure obstruction.

Han's scalar transfer at W=1, z=0, with b=1/sqrt(3), has
    A_i^(1) = b C_i,
    C_i = [[0, p_i], [-m_i, -o_i]],
where (m_i,o_i,p_i) are the Rademacher signs at offsets -1,0,+1.
Also A_i^(0)=b p_i and A_i^(2)=b m_i.

Choose the deterministic exterior family
    B^(0)=b^{-2}=3,
    B^(1)=diag(b^{-2},0)=diag(3,0),
    B^(2)=0.
Then M_B=3 and, for two fresh rows,
    Z_B = tr(B0 Q0) - tr(B1 Q1) + tr(B2 Q2)
is an integer-valued expression after the b^2 factors cancel.
This script exhausts all 2^6 sign assignments using integer arithmetic only.
"""

from itertools import product
from fractions import Fraction


def matmul2(A, B):
    return tuple(
        tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def closure(row1, row2):
    m1, o1, p1 = row1
    m2, o2, p2 = row2
    C1 = ((0, p1), (-m1, -o1))
    C2 = ((0, p2), (-m2, -o2))
    C21 = matmul2(C2, C1)

    # B^(0) Q^(0) = p2*p1; B^(1)Q^(1) contributes (C2 C1)_{11}.
    Z = p2 * p1 - C21[0][0]
    expected = p2 * (p1 + m1)
    assert Z == expected
    return Z


counts = {0: 0, 2: 0, -2: 0}
for signs in product((-1, 1), repeat=6):
    z = closure(signs[:3], signs[3:])
    assert z in counts
    counts[z] += 1

assert sum(counts.values()) == 64
assert counts[0] == 32
assert counts[2] == 16
assert counts[-2] == 16
assert Fraction(counts[0], 64) == Fraction(1, 2)
M_B = 3
assert M_B > 0

print("HARD7-02 exact W=1 scalar-Rademacher fresh-closure self-check")
print("assignments = 64")
print(f"Z=0 count = {counts[0]}")
print(f"Z=+2 count = {counts[2]}")
print(f"Z=-2 count = {counts[-2]}")
print("P(Z_B=0) = 1/2")
print("M_B = 3")
print("factorization: Z_B = p2*(p1+m1)")
print("ALL_EXACT_CHECKS_PASS = True")
