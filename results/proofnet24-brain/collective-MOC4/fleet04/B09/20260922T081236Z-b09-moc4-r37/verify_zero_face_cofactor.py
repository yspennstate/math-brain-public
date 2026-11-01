from fractions import Fraction as F


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def transpose(A):
    return [list(r) for r in zip(*A)]


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def det3(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
            - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def adj3(A):
    cof = []
    for i in range(3):
        row = []
        for j in range(3):
            minor = [[A[r][c] for c in range(3) if c != j]
                     for r in range(3) if r != i]
            d = minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0]
            row.append((-1 if (i + j) % 2 else 1) * d)
        cof.append(row)
    return transpose(cof)


def rot12(c, s):
    return [[c, -s, F(0)], [s, c, F(0)], [F(0), F(0), F(1)]]


def rot23(c, s):
    return [[F(1), F(0), F(0)], [F(0), c, -s], [F(0), s, c]]


def diag(v):
    return [[v[i] if i == j else F(0) for j in range(3)] for i in range(3)]


# Rational orthogonal matrices.  The construction N=L diag(1,1,0) R^T,
# M=L diag(0,0,1) R^T is an exact model of the zero-face singular-value
# pattern proved in REPORT.md.  It is a consistency verifier, not the proof.
L = matmul(rot12(F(3, 5), F(4, 5)), rot23(F(5, 13), F(12, 13)))
R = matmul(rot23(F(7, 25), F(24, 25)), rot12(F(20, 29), F(21, 29)))
N = matmul(matmul(L, diag([F(1), F(1), F(0)])), transpose(R))
M = matmul(matmul(L, diag([F(0), F(0), F(1)])), transpose(R))
I = eye(3)
Z = [[F(0)] * 3 for _ in range(3)]

assert det3(L) == 1 and det3(R) == 1 and det3(N) == 0
assert add(matmul(M, transpose(M)), matmul(N, transpose(N))) == I
assert add(matmul(transpose(M), M), matmul(transpose(N), N)) == I
assert add(matmul(M, transpose(N)), matmul(N, transpose(M))) == Z
assert adj3(N) == transpose(M)

frobN = sum(x * x for row in N for x in row)
frobM = sum(x * x for row in M for x in row)
qN = [[x * x for x in row] for row in N]
qM = [[x * x for x in row] for row in M]
row_sums = [sum(row) for row in qN]
col_sums = [sum(qN[i][j] for i in range(3)) for j in range(3)]

assert frobN == 2 and frobM == 1
assert all(qM[i][j] == (1 - row_sums[i]) * (1 - col_sums[j])
           for i in range(3) for j in range(3))

print("detL detR detN:", det3(L), det3(R), det3(N))
print("orthogonality-left:", add(matmul(M, transpose(M)), matmul(N, transpose(N))) == I)
print("orthogonality-right:", add(matmul(transpose(M), M), matmul(transpose(N), N)) == I)
print("cross:", add(matmul(M, transpose(N)), matmul(N, transpose(M))) == Z)
print("adjN_eq_MT:", adj3(N) == transpose(M))
print("frob2_N frob2_M:", frobN, frobM)
print("row_sums_qN:", row_sums)
print("col_sums_qN:", col_sums)
print("cofactor_factorization:", all(qM[i][j] == (1 - row_sums[i]) * (1 - col_sums[j])
                                         for i in range(3) for j in range(3)))
