#!/usr/bin/env python3
"""Exact integer self-check for P01-P67 mixed K1 class.

This script does NOT prove the operator-K-theory theorem. It checks only the
finite Z^2 bookkeeping after Pooya's published theorem identifies the source
and target bases and the assembly matrix with I_2.
"""

A = ((1, 0), (0, 1))
x = (1, -1)  # [v_1]-[v_2]

y = (
    A[0][0] * x[0] + A[0][1] * x[1],
    A[1][0] * x[0] + A[1][1] * x[1],
)

det = A[0][0] * A[1][1] - A[0][1] * A[1][0]

assert y == (1, -1)
assert y != (0, 0)
assert det == 1

print("assembly_matrix =", A)
print("source_vector =", x)
print("target_vector =", y)
print("determinant =", det)
print("mixed_class_nonzero = True")
print("All assertions passed.")
