from fractions import Fraction as F
from itertools import permutations


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def tr(A):
    return [list(row) for row in zip(*A)]


def dg(v):
    n = len(v)
    return [[v[i] if i == j else F(0) for j in range(n)] for i in range(n)]


def plus(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]


def determinant(A):
    A = [r[:] for r in A]
    n = len(A)
    ans = F(1)
    for c in range(n):
        pivot = next((r for r in range(c, n) if A[r][c]), None)
        if pivot is None:
            return F(0)
        if pivot != c:
            A[c], A[pivot] = A[pivot], A[c]
            ans = -ans
        p = A[c][c]
        ans *= p
        for r in range(c + 1, n):
            q = A[r][c] / p
            for j in range(c + 1, n):
                A[r][j] -= q * A[c][j]
    return ans


U = [[F(s, 2) for s in row] for row in ((1, 1, 1, 1), (1, -1, 1, -1), (1, 1, -1, -1), (1, -1, -1, 1))]
x = list(map(F, (0, 1, 2, 3)))
b = list(map(F, (1, 2, 4, 5)))
alpha, beta, gamma, delta = map(F, (2, 1, 1, 3))
a = [(alpha*z + beta) / (gamma*z + delta) for z in x]
bp = [(beta + delta*z) / (alpha + gamma*z) for z in b]
C = F(1)
for z in b:
    C *= alpha + gamma*z
for z in x:
    C /= gamma*z + delta
B = mm(mm(U, dg(b)), tr(U))
Bp = mm(mm(U, dg(bp)), tr(U))
lhs = determinant(plus(dg(a), B))
rhs0 = determinant(plus(dg(x), Bp))
endpoint_matches = 0
for sigma in permutations(range(4)):
    old = F(1)
    new = F(1)
    for i, j in enumerate(sigma):
        old *= a[i] + b[j]
        new *= x[i] + bp[j]
    endpoint_matches += int(old == C*new)
print('orthogonal=' + str(mm(U, tr(U)) == dg([F(1)]*4)))
print('a=' + ','.join(map(str, a)))
print('b_prime=' + ','.join(map(str, bp)))
print('scale=' + str(C))
print('lhs=' + str(lhs))
print('transformed=' + str(rhs0))
print('scaled_transformed=' + str(C*rhs0))
print('determinant_identity=' + str(lhs == C*rhs0))
print('endpoint_matches=' + str(endpoint_matches) + '/24')
