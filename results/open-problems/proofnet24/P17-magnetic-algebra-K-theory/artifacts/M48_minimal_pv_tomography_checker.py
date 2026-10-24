#!/usr/bin/env python3
"""
Exact integer checker for ProofNet24 P17 M48.

Purpose
-------
Verify the K_0 tomography statements for the historical Example 4.3.3
magnetic noncommutative 4-torus at

    theta_1 = 97/153, theta_2 = 87/148, b = 1/153.

The ordered K_0 basis is
    (1, p12, p13, p14, p23, p24, p34, p1234).

PV boundary maps use the retained right-exterior-contraction orientation.
The M46 fixed-flux real-structure sector is c14 = c23 = 0.

This script performs exact rational/integer linear algebra only.
It performs no spectral computation and certifies no magnetic gap.
"""

from fractions import Fraction
from itertools import combinations

BASIS = ("1", "p12", "p13", "p14", "p23", "p24", "p34", "p1234")
S_COLS = (0, 1, 2, 5, 6, 7)  # impose c14=c23=0

# Each D[j] is the matrix of the even-to-odd PV boundary ∂_j.
# Rows are in the natural odd exterior basis of the three remaining generators.
D = {
    1: (
        (0,-1,0,0,0,0,0,0),  # -c12 [u2]
        (0,0,-1,0,0,0,0,0),  # -c13 [u3]
        (0,0,0,-1,0,0,0,0),  # -c14 [u4]
        (0,0,0,0,0,0,0,-1),  # -c1234 [u234]
    ),
    2: (
        (0,1,0,0,0,0,0,0),   # +c12 [u1]
        (0,0,0,0,-1,0,0,0),  # -c23 [u3]
        (0,0,0,0,0,-1,0,0),  # -c24 [u4]
        (0,0,0,0,0,0,0,1),   # +c1234 [u134]
    ),
    3: (
        (0,0,1,0,0,0,0,0),   # +c13 [u1]
        (0,0,0,0,1,0,0,0),   # +c23 [u2]
        (0,0,0,0,0,0,-1,0),  # -c34 [u4]
        (0,0,0,0,0,0,0,-1),  # -c1234 [u124]
    ),
    4: (
        (0,0,0,1,0,0,0,0),   # +c14 [u1]
        (0,0,0,0,0,1,0,0),   # +c24 [u2]
        (0,0,0,0,0,0,1,0),   # +c34 [u3]
        (0,0,0,0,0,0,0,1),   # +c1234 [u123]
    ),
}

# Rational fiber rank = 22644 * tau_* at the target.
RANK_ROW = (22644, 0, 14356, 0, 0, 13311, 148, 8439)

EXPECTED_UNMATCHED_KERNELS = {
    (1, 2): (-1, 0, 0, 0, 0, 0, 153, 0),       # 153 p34 - 1
    (1, 3): (-87, 0, 0, 0, 0, 148, 0, 0),      # 148 p24 - 87*1
    (2, 4): (-97, 0, 153, 0, 0, 0, 0, 0),      # 153 p13 - 97*1
    (3, 4): (0, 1, 0, 0, 0, 0, 0, 0),          # p12
}

MATCHED_PAIRS = {(1, 4), (2, 3)}

def matvec(M, v):
    return tuple(sum(a*b for a, b in zip(row, v)) for row in M)

def restrict_cols(M, cols):
    return [tuple(row[c] for c in cols) for row in M]

def rational_rank(M):
    A = [[Fraction(x) for x in row] for row in M]
    if not A:
        return 0
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i][c] != 0), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        p = A[r][c]
        A[r] = [x/p for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f*A[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r

def combined_matrix(pair):
    return list(D[pair[0]]) + list(D[pair[1]]) + [RANK_ROW]

# 1. Exact rank dichotomy on the M46 symmetry sector.
for pair in combinations((1,2,3,4), 2):
    M = restrict_cols(combined_matrix(pair), S_COLS)
    rank = rational_rank(M)
    if pair in MATCHED_PAIRS:
        assert rank == 6, (pair, rank)
    else:
        assert rank == 5, (pair, rank)

# 2. Explicit nonzero integral kernels for every unmatched pair.
for pair, v in EXPECTED_UNMATCHED_KERNELS.items():
    assert v != (0,)*8
    assert v[3] == 0 and v[4] == 0  # lies in c14=c23=0 sector
    assert matvec(D[pair[0]], v) == (0,0,0,0)
    assert matvec(D[pair[1]], v) == (0,0,0,0)
    assert sum(a*b for a,b in zip(RANK_ROW, v)) == 0

# 3. Explicit reconstruction for the matched pair (∂1, ∂4, rank).
def reconstruct_14(d1, d4, rank_value):
    # d1=(-c12,-c13,-c14,-c1234), d4=(c14,c24,c34,c1234)
    assert d1[2] == 0 and d4[0] == 0
    assert d4[3] == -d1[3]
    c12 = -d1[0]
    c13 = -d1[1]
    c14 = 0
    c23 = 0
    c24 = d4[1]
    c34 = d4[2]
    c1234 = d4[3]
    numer = rank_value - (
        14356*c13 + 13311*c24 + 148*c34 + 8439*c1234
    )
    assert numer % 22644 == 0
    c0 = numer // 22644
    return (c0,c12,c13,c14,c23,c24,c34,c1234)

tests = (
    (2, -3, 5, 0, 0, 7, -11, 13),
    (-17, 19, -23, 0, 0, 29, 31, -37),
    (0, 1, 0, 0, 0, 0, 0, 0),
)
for x in tests:
    d1 = matvec(D[1], x)
    d4 = matvec(D[4], x)
    R = sum(a*b for a,b in zip(RANK_ROW, x))
    assert reconstruct_14(d1, d4, R) == x

# 4. Explicit reconstruction for the matched pair (∂2, ∂3, rank).
def reconstruct_23(d2, d3, rank_value):
    # d2=(c12,-c23,-c24,c1234), d3=(c13,c23,-c34,-c1234)
    assert d2[1] == 0 and d3[1] == 0
    assert d2[3] == -d3[3]
    c12 = d2[0]
    c13 = d3[0]
    c14 = 0
    c23 = 0
    c24 = -d2[2]
    c34 = -d3[2]
    c1234 = d2[3]
    numer = rank_value - (
        14356*c13 + 13311*c24 + 148*c34 + 8439*c1234
    )
    assert numer % 22644 == 0
    c0 = numer // 22644
    return (c0,c12,c13,c14,c23,c24,c34,c1234)

for x in tests:
    d2 = matvec(D[2], x)
    d3 = matvec(D[3], x)
    R = sum(a*b for a,b in zip(RANK_ROW, x))
    assert reconstruct_23(d2, d3, R) == x

print("PASS")
print("matched pairs:", sorted(MATCHED_PAIRS))
for pair in sorted(EXPECTED_UNMATCHED_KERNELS):
    print("unmatched kernel", pair, EXPECTED_UNMATCHED_KERNELS[pair])
print("rank row:", RANK_ROW)
