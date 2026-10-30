from fractions import Fraction
from math import pow


def det(M):
    n = len(M)
    if n == 0:
        return Fraction(1)
    if n == 1:
        return M[0][0]
    ans = Fraction(0)
    for j in range(n):
        minor = [row[:j] + row[j+1:] for row in M[1:]]
        ans += ((-1) ** j) * M[0][j] * det(minor)
    return ans


def sub(A, rows, cols):
    return [[A[i][j] for j in cols] for i in rows]


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))]
            for i in range(len(A))]


def transpose(A):
    return [list(row) for row in zip(*A)]


def adj2(B):
    return [[B[1][1], -B[0][1]], [-B[1][0], B[0][0]]]


# Deterministic symmetric integer matrix.
n = 8
A = [[Fraction((i+1)**2 + (j+1)**2 + 3*(i+1)*(j+1) + ((i+2) if i == j else 0))
      for j in range(n)] for i in range(n)]

# q=1 bordered-minor matrix identity.
H = [0, 1]
R = [2, 3]
C = [4, 5]
B = sub(A, R, C)
Adj = adj2(B)
AHC = sub(A, H, C)
ARH = sub(A, R, H)
T = matmul(matmul(AHC, Adj), ARH)
for ii, h in enumerate(H):
    for jj, k in enumerate(H):
        lhs = det(sub(A, [h] + R, [k] + C))
        rhs = det(B) * A[h][k] - T[ii][jj]
        assert lhs == rhs, (h, k, lhs, rhs)

# q=2 polynomial identity a*N_{alpha,beta}=det K[alpha,beta].
H1 = [0, 1]
H2 = [2, 3]
r, c = 4, 5
HH = H1 + H2
idx = {h: i for i, h in enumerate(HH)}
a = A[r][c]
AHH = sub(A, HH, HH)
col = [[A[h][c]] for h in HH]
row = [[A[r][h] for h in HH]]
outer = matmul(col, row)
K = [[a * AHH[i][j] - outer[i][j] for j in range(len(HH))]
     for i in range(len(HH))]
for h1 in H1:
    for h2 in H2:
        for k1 in H1:
            for k2 in H2:
                N = det(sub(A, [h1, h2, r], [k1, k2, c]))
                rows = [idx[h1], idx[h2]]
                cols = [idx[k1], idx[k2]]
                rhs = det(sub(K, rows, cols))
                assert a * N == rhs, (h1, h2, k1, k2, a*N, rhs)

C3 = 6 ** (4/3)
tau = 1/16
p1 = 4/9375
p2 = 1/384
cq1 = 2*C3*(tau*p1) ** (-1/6)
cq2_direct = 2*C3*((tau/3)*p2) ** (-1/6)
p1prime = (tau/12)*p2
cq2_via_q1 = 2*C3*(tau*p1prime) ** (-1/6)

print('q1_identity_exact=PASS')
print('q2_identity_exact=PASS')
print('C3=', repr(C3))
print('C_q1=', repr(cq1))
print('C_q2_direct=', repr(cq2_direct))
print('P1prime_over_L6=', repr(p1prime))
print('C_q2_via_q1=', repr(cq2_via_q1))
