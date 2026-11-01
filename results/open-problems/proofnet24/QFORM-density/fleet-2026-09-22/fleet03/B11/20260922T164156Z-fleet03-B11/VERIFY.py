from fractions import Fraction as F
from itertools import combinations


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))]
            for i in range(len(A))]


def tr(A):
    return [list(x) for x in zip(*A)]


def det3(M):
    a, b, c = M[0]
    d, e, f = M[1]
    g, h, i = M[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


R = [
    [F(1, 2), F(1, 2), F(1, 2)],
    [F(1, 2), F(-1, 2), F(-1, 2)],
    [F(-1, 2), F(1, 2), F(-1, 2)],
    [F(-1, 2), F(-1, 2), F(1, 2)],
]
J = [[F(1), F(0), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(-1)]]
I3 = [[F(int(i == j)) for j in range(3)] for i in range(3)]

assert mm(tr(R), R) == I3
A = mm(mm(R, J), tr(R))
P = mm(R, tr(R))
assert mm(A, A) == P
assert mm(mm(A, A), A) == A
assert sum(A[i][i] for i in range(4)) == 1

dets = []
for T in combinations(range(4), 3):
    M = [R[i] for i in T]
    d = abs(det3(M))
    assert d == F(1, 2)
    dets.append(d)

assert sum(d * d for d in dets) == 1

expected = [
    [F(1, 4), F(1, 4), F(1, 4), F(-3, 4)],
    [F(1, 4), F(1, 4), F(-3, 4), F(1, 4)],
    [F(1, 4), F(-3, 4), F(1, 4), F(1, 4)],
    [F(-3, 4), F(1, 4), F(1, 4), F(1, 4)],
]
assert A == expected

print("QFORM_B11_PLUCKER_TETRA_CHECK_PASS")
print("all four |det R_T| = 1/2; sum of squared minors = 1")
print("A^2=RR^T, A^3=A, rank(R)=3 and trace(A)=1, hence spectrum {1,1,-1,0}")
