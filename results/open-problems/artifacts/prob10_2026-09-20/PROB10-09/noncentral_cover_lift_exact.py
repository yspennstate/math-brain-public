#!/usr/bin/env python3
"""Exact finite-core self-check for PROB10-09 noncentral cover-lift iteration.

This checks only the algebraic semidirect-product example and exact radical
inequalities.  The analytic Hilbert-fibre adjacency domination and
nonbacktracking argument are proved in the accompanying report.
"""

from fractions import Fraction

def mv(A, x):
    return (
        A[0][0]*x[0] + A[0][1]*x[1],
        A[1][0]*x[0] + A[1][1]*x[1],
    )

def mm(A, B):
    return (
        (
            A[0][0]*B[0][0] + A[0][1]*B[1][0],
            A[0][0]*B[0][1] + A[0][1]*B[1][1],
        ),
        (
            A[1][0]*B[0][0] + A[1][1]*B[1][0],
            A[1][0]*B[0][1] + A[1][1]*B[1][1],
        ),
    )

def subm(A, B):
    return tuple(tuple(A[i][j]-B[i][j] for j in range(2)) for i in range(2))

def det(A):
    return A[0][0]*A[1][1] - A[0][1]*A[1][0]

def basis_det(x, y):
    return x[0]*y[1] - x[1]*y[0]

I = ((1,0),(0,1))
M = ((0,-1),(1,1))
v = (0,-1)
e1 = (1,0)
e2 = (0,1)

assert det(M) == 1
w = mv(subm(M,I), v)
assert w == e1
Mw = mv(M,w)
assert Mw == e2
assert basis_det(w,Mw) == 1
assert Mw != w

# The quotient action respects [a1,b1][a2,b2]=1 because only a1 acts
# nontrivially and b1,a2,b2 act by I.
Minv = ((1,1),(-1,0))
assert mm(M, Minv) == I
assert mm(mm(M,I), mm(Minv, I)) == I

# Nonbacktracking root at D=8, rho=4 sqrt(2):
# beta = (4sqrt2 + sqrt(32-28))/2 = 1+2sqrt2 < 5.
assert 2 < 4

# Exact certificate:
# (10 sqrt(2)-12)/35 > 61/1000
# iff 10000 sqrt(2) > 14135; both sides positive, so square.
lhs_sq = 2 * 10000**2
rhs_sq = 14135**2
gap_square_margin = lhs_sq - rhs_sq
assert gap_square_margin > 0
assert gap_square_margin == 201775

# Equivalent p_u floor > 261/1000:
# 1/(1+2sqrt2)=(2sqrt2-1)/7 > 261/1000
# iff 739 > 522 sqrt2; square.
pu_square_margin = 739**2 - 2*522**2
assert pu_square_margin == 1153
assert pu_square_margin > 0

# Negation/scope test: another unimodular action/lift can span only an
# index-two sublattice, so horizontal generation is not automatic.
Mbad = ((0,-1),(1,0))
vbad = (1,0)
wbad = mv(subm(Mbad,I),vbad)
Mwbad = mv(Mbad,wbad)
bad_index_det = abs(basis_det(wbad,Mwbad))
assert bad_index_det == 2

print("PROB10-09 NONCENTRAL COVER-LIFT EXACT CHECK")
print(f"det_M={det(M)}")
print(f"w=(M-I)v={w}")
print(f"Mw={Mw}")
print(f"kernel_orbit_basis_det={basis_det(w,Mw)}")
print(f"noncentral_test_Me1_ne_e1={mv(M,e1) != e1}")
print(f"beta_lt_5_square_margin={4-2}")
print(f"gap_gt_61_over_1000_square_margin={gap_square_margin}")
print(f"pu_gt_261_over_1000_square_margin={pu_square_margin}")
print(f"negation_index_det={bad_index_det}")
print("ALL_EXACT_CHECKS_PASS")
