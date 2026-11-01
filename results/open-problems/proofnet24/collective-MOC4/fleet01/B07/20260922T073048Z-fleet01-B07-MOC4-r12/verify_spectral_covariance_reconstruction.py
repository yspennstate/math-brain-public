from fractions import Fraction as F


def inv(A):
    n = len(A)
    M = [[F(x) for x in row] + [F(i == j) for j in range(n)] for i, row in enumerate(A)]
    for j in range(n):
        k = next(k for k in range(j, n) if M[k][j])
        M[j], M[k] = M[k], M[j]
        p = M[j][j]
        M[j] = [x / p for x in M[j]]
        for k in range(n):
            if k == j:
                continue
            c = M[k][j]
            M[k] = [M[k][l] - c * M[j][l] for l in range(2 * n)]
    return [row[n:] for row in M]


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def tr(A):
    return [list(r) for r in zip(*A)]


def det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def det3(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
            - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def cmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def conj(z):
    return (z[0], -z[1])


def csub(z, w):
    return (z[0] - w[0], z[1] - w[1])


def re3(a, b, c):
    return cmul(cmul(a, b), c)[0]


def im_z_conj_w(z, w):
    return cmul(z, conj(w))[1]


def abs2(z):
    return z[0] * z[0] + z[1] * z[1]


eta = (1, 1)
z1, z2 = (2, 1), (-1, 3)
q = [(1, 2), (-2, 1), (3, -1)]
C = [[F(re3(eta, z, qb)) for qb in q] for z in (z1, z2)]
P = [[F(i == j) - F(1, 3) for j in range(3)] for i in range(3)]
S = mm(mm(C, P), tr(C))
L = [[F(1)] * 3, C[0], C[1]]
area_q = im_z_conj_w(csub(q[0], q[2]), csub(q[1], q[2]))
area_formula = (F(abs2(eta) ** 2, 3)
                * F(im_z_conj_w(z1, z2) ** 2)
                * F(area_q ** 2))
assert det2(S) == area_formula == F(det3(L) ** 2, 3)

W1 = (F(1, 2), F(-2, 3))
W2 = (F(3, 5), F(1, 7))
Li = inv(L)
V = []
for beta in range(3):
    V.append((Li[beta][1] * W1[0] + Li[beta][2] * W2[0],
              Li[beta][1] * W1[1] + Li[beta][2] * W2[1]))
inner = lambda u, v: u[0] * v[0] + u[1] * v[1]
E = sum(inner(v, v) for v in V)
G = inv(S)
E_reconstructed = (G[0][0] * inner(W1, W1)
                   + 2 * G[0][1] * inner(W1, W2)
                   + G[1][1] * inner(W2, W2))
assert E == E_reconstructed

# A rational edge-budget check with sqrt(Q) = 1, 2, 3.
Q12, Q13, Q23 = F(1), F(4), F(9)
lam1, lam2, lam3 = F(2), F(3), F(5, 2)
u12_1, u12_2 = F(1, 2), F(3, 2)
u13_1, u13_3 = F(1), F(3)
u23_2, u23_3 = F(2), F(4)
assert u12_1 + u12_2 == 2
assert u13_1 + u13_3 == 4
assert u23_2 + u23_3 == 6
lhs = (lam1 * (u12_1 ** 2 + u13_1 ** 2)
       + lam2 * (u12_2 ** 2 + u23_2 ** 2)
       + lam3 * (u13_3 ** 2 + u23_3 ** 2))
rhs = 4 * (Q12 * max(lam1, lam2)
           + Q13 * max(lam1, lam3)
           + Q23 * max(lam2, lam3))
assert lhs <= rhs

print("PASS exact covariance determinant =", det2(S))
print("PASS det(L)^2/3 =", F(det3(L) ** 2, 3))
print("PASS exact reconstruction E =", E)
print("PASS edge-budget sample lhs =", lhs)
print("PASS edge-budget sample rhs =", rhs)
