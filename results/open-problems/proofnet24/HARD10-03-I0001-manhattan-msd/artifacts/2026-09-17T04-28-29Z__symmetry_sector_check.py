#!/usr/bin/env python3
"""Exact standard-library self-check for the finite symmetry boundary case in NEW-I0001-L3.

This checks only finite matrix algebra. It is NOT an audit of the infinite-dimensional
Manhattan-lattice theorem.
"""


def mm(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def is_zero(A):
    return all(x == 0 for row in A for x in row)


# Basis: (h_0, h_2, v_0, v_2).
# The h-sector has character (-,+); the v-sector has character (+,-).
U1 = [
    [-1, 0, 0, 0],
    [0, -1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]
U2 = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, -1, 0],
    [0, 0, 0, -1],
]
# Coordinate swap h_k <-> v_k.
J = [
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
]

# Symmetry-compatible positive operator with genuine intra-sector mode mixing.
T = [
    [2, 1, 0, 0],
    [1, 2, 0, 0],
    [0, 0, 2, 1],
    [0, 0, 1, 2],
]

assert is_zero(sub(mm(T, U1), mm(U1, T)))
assert is_zero(sub(mm(T, U2), mm(U2, T)))
assert is_zero(sub(mm(T, J), mm(J, T)))

# Each 2x2 block K=[[2,1],[1,2]] is positive definite by Sylvester:
# first leading principal minor 2>0 and determinant 4-1=3>0.
assert T[0][0] == 2
assert T[0][0] * T[1][1] - T[0][1] * T[1][0] == 3
assert T[0][1] == 1  # genuine h_0 <-> h_2 mixing survives all displayed symmetries

# Generic 2x2 species compression M=[[a,b],[c,d]]:
# commuting with diag(-1,+1) forces b=c=0; commuting with swap J2 then forces a=d.
# Thus the species commutant is exactly span{I_2}.
print("SPECIES_COMMUTANT: b=c=0 from reflection; a=d from axis swap => span{I_2}")
print("TOY_COMMUTES_WITH_U1=PASS")
print("TOY_COMMUTES_WITH_U2=PASS")
print("TOY_COMMUTES_WITH_AXIS_SWAP=PASS")
print("TOY_POSITIVE_DEFINITE_BLOCKS=PASS")
print("INTRASECTOR_MODE_MIXING_ENTRY=1")
print("COUNTEREXAMPLE_TO_SYMMETRY_IMPLIES_MODE_DIAGONALITY=PASS")
print("ALL_EXACT_CHECKS_PASS")
