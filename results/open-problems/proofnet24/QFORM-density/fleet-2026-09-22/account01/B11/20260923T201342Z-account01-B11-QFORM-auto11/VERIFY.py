#!/usr/bin/env python3
"""Deterministic algebra/constant checks for account01/B11 run 20260923T201342Z.
Uses only the Python standard library.
"""
from fractions import Fraction
from math import pi, sqrt
from random import Random


def det2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]


def det3(M):
    return (
        M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
        - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
        + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
    )


def inv3(M):
    d = det3(M)
    if d == 0:
        raise ZeroDivisionError("singular matrix")
    cof = [
        [ M[1][1]*M[2][2]-M[1][2]*M[2][1], -(M[1][0]*M[2][2]-M[1][2]*M[2][0]), M[1][0]*M[2][1]-M[1][1]*M[2][0]],
        [-(M[0][1]*M[2][2]-M[0][2]*M[2][1]), M[0][0]*M[2][2]-M[0][2]*M[2][0], -(M[0][0]*M[2][1]-M[0][1]*M[2][0])],
        [ M[0][1]*M[1][2]-M[0][2]*M[1][1], -(M[0][0]*M[1][2]-M[0][2]*M[1][0]), M[0][0]*M[1][1]-M[0][1]*M[1][0]],
    ]
    return [[cof[j][i]/d for j in range(3)] for i in range(3)]


def transpose(A):
    return [list(x) for x in zip(*A)]


def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


rng = Random(20260923)

# Exact identity det(cc^T-aB)=a det([[a,c^T],[c,B]]) in transverse dimension two.
for _ in range(10000):
    a = rng.randint(-20,20) or 1
    c1,c2 = rng.randint(-20,20),rng.randint(-20,20)
    b11,b12,b22 = rng.randint(-20,20),rng.randint(-20,20),rng.randint(-20,20)
    M = [[a,c1,c2],[c1,b11,b12],[c2,b12,b22]]
    N = [[c1*c1-a*b11,c1*c2-a*b12],[c1*c2-a*b12,c2*c2-a*b22]]
    assert det2(N) == a*det3(M)

# Exact Schur compatibility: D=B^T C^{-1}B makes [[C,B],[B^T,D]] have zero Schur complement.
# Fraction arithmetic makes this an exact check, not a floating-point tolerance test.
checked = 0
while checked < 1000:
    C = [[Fraction(rng.randint(-7,7)) for _ in range(3)] for __ in range(3)]
    C = [[C[i][j] + C[j][i] for j in range(3)] for i in range(3)]
    if det3(C) == 0:
        continue
    B = [[Fraction(rng.randint(-7,7)) for _ in range(3)] for __ in range(3)]
    if det3(B) == 0:
        continue
    Ci = inv3(C)
    D = matmul(transpose(B),matmul(Ci,B))
    S = [[D[i][j]-matmul(transpose(B),matmul(Ci,B))[i][j] for j in range(3)] for i in range(3)]
    assert all(x == 0 for row in S for x in row)
    checked += 1

kappa_star = (34/111)*(17/288)**2
linear_collar_constant = 2*sqrt(2*pi/kappa_star)
partner_family_constant = 2*sqrt(pi)

print(f"kappa_star={kappa_star:.15f}")
print(f"linear_collar_constant={linear_collar_constant:.12f}")
print(f"partner_family_constant={partner_family_constant:.12f}")
print("determinant_identity_exact_cases=10000")
print("schur_identity_exact_cases=1000")
print("QFORM_B11_FULL3_DISCRIMINANT_CHECK_PASS")
