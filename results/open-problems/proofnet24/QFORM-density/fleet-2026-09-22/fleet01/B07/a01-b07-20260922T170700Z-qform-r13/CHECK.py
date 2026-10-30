from fractions import Fraction as F
from itertools import combinations


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def tr(A):
    return [list(x) for x in zip(*A)]


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def add(A, B, sign=1):
    return [[A[i][j] + sign * B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def sub(A, rows, cols=None):
    if cols is None:
        cols = rows
    return [[A[i][j] for j in cols] for i in rows]


def det(A):
    A = [[F(x) for x in row] for row in A]
    n = len(A)
    out = F(1)
    for i in range(n):
        p = next((r for r in range(i, n) if A[r][i]), None)
        if p is None:
            return F(0)
        if p != i:
            A[i], A[p] = A[p], A[i]
            out = -out
        piv = A[i][i]
        out *= piv
        for j in range(i + 1, n):
            A[i][j] /= piv
        for r in range(i + 1, n):
            q = A[r][i]
            if q:
                for j in range(i + 1, n):
                    A[r][j] -= q * A[i][j]
    return out


def inv(A):
    A = [[F(x) for x in row] for row in A]
    n = len(A)
    M = [A[i] + eye(n)[i] for i in range(n)]
    for i in range(n):
        p = next(r for r in range(i, n) if M[r][i])
        M[i], M[p] = M[p], M[i]
        q = M[i][i]
        M[i] = [x / q for x in M[i]]
        for r in range(n):
            if r == i:
                continue
            q = M[r][i]
            if q:
                M[r] = [M[r][j] - q * M[i][j] for j in range(2 * n)]
    return [row[n:] for row in M]


def principal_sum(L, fixed, free):
    ans = F(0)
    for r in range(len(free) + 1):
        for R in combinations(free, r):
            S = sorted(list(fixed) + list(R))
            ans += F(1) if not S else det(sub(L, S))
    return ans


# Ridge set deletion and fixed-pattern factorization.
B = [[F(x) for x in row] for row in [
    [1, 2, 0, 1],
    [0, 1, 1, 2],
    [2, 0, 1, 1],
    [1, 1, 2, 0],
    [2, 1, 0, 1],
]]
L = mm(B, tr(B))
D = det(add(eye(5), L))
K = mm(L, inv(add(eye(5), L)))
H = [0, 2]
C = [1, 3, 4]
assert D == 1455
assert det(add(eye(3), sub(L, C))) / D == F(208, 1455)
assert det(add(eye(2), sub(K, H), sign=-1)) == F(208, 1455)
weights = {
    (): principal_sum(L, [], C),
    (0,): principal_sum(L, [0], C),
    (2,): principal_sum(L, [2], C),
    (0, 2): principal_sum(L, [0, 2], C),
}
assert weights == {(): F(208), (0,): F(376), (2,): F(376), (0, 2): F(495)}
assert sum(weights.values()) == D
T = [0, 2]
LT = sub(L, T)
M = add(sub(L, C), mm(mm(sub(L, C, T), inv(LT)), sub(L, T, C)), sign=-1)
assert det(LT) == 27
assert det(add(eye(3), M)) == F(55, 3)
assert det(LT) * det(add(eye(3), M)) == weights[(0, 2)]
BT = sub(B, T, list(range(4)))
BC = sub(B, C, list(range(4)))
Pperp = add(eye(4), mm(mm(tr(BT), inv(mm(BT, tr(BT)))), BT), sign=-1)
assert M == mm(mm(BC, Pperp), tr(BC))

# Division-free bordered-minor identity.
A = [[F(x) for x in row] for row in [
    [3, 1, 2, 0, 1],
    [1, 2, 1, 1, 0],
    [2, 1, 4, 2, 1],
    [0, 1, 2, 3, 1],
    [1, 0, 1, 1, 2],
]]
S = [0, 1]
C = [2, 3, 4]
H0 = sub(A, S)
adjH = [[H0[1][1], -H0[0][1]], [-H0[1][0], H0[0][0]]]
bordered = [[det(sub(A, S + [i], S + [j])) for j in C] for i in C]
rhs = add([[det(H0) * x for x in row] for row in sub(A, C)],
          mm(mm(sub(A, C, S), adjH), sub(A, S, C)), sign=-1)
assert bordered == rhs == [[F(13), F(9), F(2)], [F(9), F(12), F(6)], [F(2), F(6), F(8)]]

# Cancellation stress fixture A=I_4-J_4/3.
A4 = [[F(int(i == j)) - F(1, 3) for j in range(4)] for i in range(4)]
S = [0, 1]
C = [2, 3]
stress = [[det(sub(A4, S + [i], S + [j])) for j in C] for i in C]
assert stress == [[F(0), F(-1, 3)], [F(-1, 3), F(0)]]

print("D=1455")
print("set_deletion_ratio=208/1455")
print("pattern_weights=208,376,376,495")
print("T02_factor=27*(55/3)=495")
print("bordered_identity=[[13,9,2],[9,12,6],[2,6,8]]")
print("stress_bordered=[[0,-1/3],[-1/3,0]]")
print("QFORM_B07_R13_EXACT_CHECK_PASS")
