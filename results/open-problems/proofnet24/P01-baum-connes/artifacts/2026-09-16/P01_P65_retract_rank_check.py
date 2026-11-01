#!/usr/bin/env python3
"""Exact integer self-check for P01-P65.

This does not prove the operator-algebraic input.  It checks the finite integer
certificate used after the analytic retraction has been proved: on the chosen
K_1 basis ([u_{s1}],[u_{s2}]) the composite quotient-after-section is I_2,
so the represented subgroup has rank exactly 2.
"""

J = ((1, 0), (0, 1))
Q = ((1, 0), (0, 1))

QJ = tuple(
    tuple(sum(Q[i][k] * J[k][j] for k in range(2)) for j in range(2))
    for i in range(2)
)
det = QJ[0][0] * QJ[1][1] - QJ[0][1] * QJ[1][0]
rank = 2 if det != 0 else (1 if any(QJ[i][j] for i in range(2) for j in range(2)) else 0)

print(f"J = {J}")
print(f"Q = {Q}")
print(f"QJ = {QJ}")
print(f"det(QJ) = {det}")
print(f"rank = {rank}")

assert QJ == ((1, 0), (0, 1))
assert det == 1
assert rank == 2
