#!/usr/bin/env python3
"""Exact checks for fleet04/B09 MOC4 r02.

Standard library only.  This is a finite verifier/sanity check for the exact
certificates in REPORT.md; the polynomial arguments themselves are in the report.
"""
from fractions import Fraction as F
from itertools import combinations, permutations


def prod(xs):
    z = F(1)
    for x in xs:
        z *= x
    return z


def det2(M, rows, cols):
    i, j = rows
    k, l = cols
    return M[i][k] * M[j][l] - M[i][l] * M[j][k]


def det3(M):
    return (
        M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
        - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
        + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
    )


def matmul(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def complement(S):
    S = set(S)
    return tuple(i for i in range(4) if i not in S)


U = [
    [F(492, 625), F(-31, 625), F(-48, 125), F(12, 25)],
    [F(-9, 25), F(12, 25), F(-4, 5), F(0)],
    [F(-36, 125), F(48, 125), F(9, 25), F(4, 5)],
    [F(-256, 625), F(-492, 625), F(-36, 125), F(9, 25)],
]

I4 = [[F(int(i == j)) for j in range(4)] for i in range(4)]
UTU = [[sum(U[k][i] * U[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
assert UTU == I4

P = [[x * x for x in row] for row in U]
pairs = list(combinations(range(4), 2))
q = {(S, T): det2(U, S, T) ** 2 for S in pairs for T in pairs}

# Exact mixed-minor difference identity for every two-row/two-column block.
for S in pairs:
    for T in pairs:
        lhs = q[S, T] - q[S, complement(T)]
        rhs = sum(P[i][j] for i in S for j in T) - 1
        assert lhs == rhs

orient = [(0, 1), (0, 2), (0, 3)]
R = [[F(0) for _ in range(3)] for _ in range(3)]
for a, S in enumerate(orient):
    for b, T in enumerate(orient):
        R[a][b] = q[S, T] + q[S, complement(T)]
assert all(sum(row) == 1 for row in R)
assert all(sum(R[a][b] for a in range(3)) == 1 for b in range(3))


def induced_R(sigma):
    out = [[0 for _ in range(3)] for _ in range(3)]
    classes = [frozenset(x) for x in orient]
    universe = set(range(4))
    for a, S in enumerate(classes):
        image = frozenset(sigma[i] for i in S)
        for b, T in enumerate(classes):
            if image == T or image == frozenset(universe - set(T)):
                out[a][b] = 1
                break
        else:
            raise AssertionError("no induced complement-pair class")
    return out


def permutation_P(sigma):
    out = [[0 for _ in range(4)] for _ in range(4)]
    for i, j in enumerate(sigma):
        out[i][j] = 1
    return out


def pr_separator(P0, R0):
    # 1-based REPORT.md equation (3):
    # P12+P14+2P24+P31+P34-P41-P42-R23+R31.
    return (
        P0[0][1] + P0[0][3] + 2 * P0[1][3] + P0[2][0] + P0[2][3]
        - P0[3][0] - P0[3][1] - R0[1][2] + R0[2][0]
    )


vertex_values = []
for sigma in permutations(range(4)):
    val = pr_separator(permutation_P(sigma), induced_R(sigma))
    vertex_values.append(val)
    assert val >= 0
assert set(vertex_values) == {0, 2, 4}

unitary_violation = pr_separator(P, R)
assert unitary_violation == F(-448, 15625)


def vandermonde(x):
    return prod(x[i] - x[j] for i in range(4) for j in range(i + 1, 4))


def reduced_G(a, b):
    # Convenient complex-coefficient gauge from REPORT.md equation (6).
    # Exact rational inputs suffice for these algebraic checks.
    Am, Bm = [], []
    for S in orient:
        Sc = complement(S)
        Am.append(a[Sc[0]] * a[Sc[1]] - a[S[0]] * a[S[1]])
        Bm.append(b[Sc[0]] * b[Sc[1]] - b[S[0]] * b[S[1]])
    u = [sum(Am), Am[0], Am[1], Am[2]]
    v = [sum(Bm), Bm[0], Bm[1], Bm[2]]
    ac = [prod(a[k] for k in range(4) if k != i) for i in range(4)]
    bc = [prod(b[k] for k in range(4) if k != j) for j in range(4)]
    G = [
        [ac[i] * b[j] + a[i] * bc[j] + F(1, 2) * u[i] * v[j] for j in range(4)]
        for i in range(4)
    ]
    return [
        [G[i][j] - G[i][3] - G[3][j] + G[3][3] for j in range(3)]
        for i in range(3)
    ]


def inverse_formula(a, b):
    inv = [[F(0) for _ in range(3)] for _ in range(3)]
    for j in range(3):
        for i in range(3):
            da = prod(a[i] - a[k] for k in range(4) if k != i)
            db = prod(b[j] - b[k] for k in range(4) if k != j)
            inv[j][i] = -(a[i] - b[j]) ** 2 / (da * db)
    return inv


def check_structured_identity(a0, b0):
    a = [F(x) for x in a0]
    b = [F(x) for x in b0]
    G = reduced_G(a, b)
    lhs = det3(G)
    rhs = -F(1, 2) * vandermonde(a) * vandermonde(b)
    assert lhs == rhs
    assert lhs != 0
    inv = inverse_formula(a, b)
    assert matmul(G, inv) == [[F(int(i == j)) for j in range(3)] for i in range(3)]
    assert matmul(inv, G) == [[F(int(i == j)) for j in range(3)] for i in range(3)]
    return lhs


checks = [
    check_structured_identity((0, 1, 2, 3), (4, 5, 6, 7)),
    check_structured_identity((-3, 1, 4, 6), (-5, -1, 2, 8)),
    check_structured_identity((-4, -2, 3, 9), (-7, 0, 5, 11)),
]
assert checks[0] == -72

print("PASS")
print("PR vertex values =", sorted(set(vertex_values)))
print("unitary PR separator =", unitary_violation)
print("structured determinant checks =", checks)
