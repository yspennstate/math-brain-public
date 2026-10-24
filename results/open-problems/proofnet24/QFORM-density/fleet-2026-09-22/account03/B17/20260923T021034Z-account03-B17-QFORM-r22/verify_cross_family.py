#!/usr/bin/env python3
"""Deterministic arithmetic checks for account03/B17 r22.

This verifies only algebraic/numerical constants used by REPORT.md; the analytic
weak-L^{3/2}, bathtub, and local-limit arguments are proved in the report.
"""
from math import gamma, pi, sqrt


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


g54 = gamma(1.25)
D = (2 ** (13 / 4)) * g54 / ((3 * pi) ** (3 / 4))
C = 3 * D ** (2 / 3)
sharp = 3 * sqrt(2)
coarse = (2 ** (11 / 6)) * sqrt(3) * pi ** (-1 / 3)

u = [0.5, 0.5, 1 / sqrt(2)]
assert abs(sum(x*x for x in u) - 1) < 1e-14
B = [[(1.0 if i == j else 0.0) - 2*u[i]*u[j] for j in range(3)]
     for i in range(3)]
B2 = matmul(B, B)
err = max(abs(B2[i][j] - (1.0 if i == j else 0.0))
          for i in range(3) for j in range(3))
assert err < 1e-14

assert C < sharp
assert coarse < sharp
assert 16 < 3 * sqrt(3) * pi
assert abs(C - 4.109270566451296) < 5e-14

print("PASS QFORM-TWO-HEAVY-SHARED-BANK-GAUSSIAN-NOESCAPE-v1")
print(f"Gamma(5/4) = {g54:.17g}")
print(f"D = {D:.17g}")
print(f"C_cross = {C:.17g}")
print(f"3sqrt2 = {sharp:.17g}")
print(f"gap = {sharp-C:.17g}")
print(f"coarse_upper = {coarse:.17g}")
print(f"coarse_gap = {sharp-coarse:.17g}")
print(f"max |B^2-I| = {err:.17g}")
