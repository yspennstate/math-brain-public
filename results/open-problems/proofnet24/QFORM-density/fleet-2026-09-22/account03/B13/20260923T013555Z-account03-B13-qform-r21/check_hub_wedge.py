from fractions import Fraction
from itertools import combinations
import math

M = [
    [1, 2, 0, 1, -1],
    [0, 1, 1, 2, 1],
    [2, -1, 1, 0, 1],
    [1, 0, 2, -1, 2],
    [-1, 1, 0, 2, 1],
]
M = [[Fraction(x) for x in row] for row in M]


def det3(A):
    return (
        A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    )


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def z_total(M):
    z = Fraction(0)
    for S in combinations(range(len(M)), 3):
        for T in combinations(range(len(M[0])), 3):
            z += det3([[M[i][j] for j in T] for i in S]) ** 2
    return z


def z_h(M, h):
    z = Fraction(0)
    others = [i for i in range(len(M)) if i != h]
    for i, j in combinations(others, 2):
        for T in combinations(range(len(M[0])), 3):
            z += det3([[M[k][l] for l in T] for k in (h, i, j)]) ** 2
    return z


def contraction_rhs(M, h):
    a = M[h]
    aa = dot(a, a)
    if aa == 0:
        return Fraction(0)
    projected = []
    for i, row in enumerate(M):
        if i == h:
            continue
        coeff = dot(row, a) / aa
        projected.append([row[j] - coeff * a[j] for j in range(len(a))])
    e2 = Fraction(0)
    for u, v in combinations(projected, 2):
        e2 += dot(u, u) * dot(v, v) - dot(u, v) ** 2
    return aa * e2


Z = z_total(M)
Zhs = [z_h(M, h) for h in range(len(M))]
RHS = [contraction_rhs(M, h) for h in range(len(M))]
assert Z == 2129
assert Zhs == RHS
assert sum(Zhs, Fraction(0)) == 3 * Z

C0 = 2 ** (-0.5) * math.pi ** (3 / 4) * math.e ** (5 / 8)
C_E2 = 3 ** (4 / 3) * 2 ** (-4 / 9) * math.e ** (5 / 9)
C_paid = (6 * math.sqrt(math.e)) ** (2 / 3) * 32 ** (1 / 9)
C_hub = C_E2 * (192 / 31) ** (1 / 9)
assert abs(C0 - 3.1173205167723097) < 1e-14
assert abs(C_E2 - 5.541728894337633) < 1e-14
assert C_paid < 6.773
assert C_hub < 6.787
assert max(C_paid, C_hub) < 6.787

print('Z=', Z)
print('Z_h=', ','.join(str(x) for x in Zhs))
print('sum_h_Z_h_over_Z=', float(sum(Zhs, Fraction(0)) / Z))
print('C0=', C0)
print('C_E2=', C_E2)
print('C_paid=', C_paid)
print('C_hub=', C_hub)
print('QFORM_B13_R21_HUB_WEDGE_CHECK_PASS')
