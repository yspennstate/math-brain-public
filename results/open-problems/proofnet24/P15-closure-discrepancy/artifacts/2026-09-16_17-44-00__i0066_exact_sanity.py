from fractions import Fraction


def matmul(A, B):
    return [[sum(A[i][t] * B[t][j] for t in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def matadd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def matsub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def smul(c, A):
    return [[c * x for x in row] for row in A]


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


# Standard so(3) generators.  They do not commute, but the quadratic Casimir
# is scalar in the defining representation.
L1 = [[0, 0, 0], [0, 0, -1], [0, 1, 0]]
L2 = [[0, 0, 1], [0, 0, 0], [-1, 0, 0]]
L3 = [[0, -1, 0], [1, 0, 0], [0, 0, 0]]

comm12 = matsub(matmul(L1, L2), matmul(L2, L1))
sum_squares = matadd(matadd(matmul(L1, L1), matmul(L2, L2)), matmul(L3, L3))

print('COMM_L1_L2', comm12)
print('L3', L3)
print('COMMUTATOR_OK', comm12 == L3)
print('SUM_SQUARES', sum_squares)
print('CASIMIR_OK', sum_squares == smul(-2, eye(3)))

# Exact p-th radial drift coefficient for dX=-a X dt +(s I+k J)X dW
# in R^2: p[-a +(k^2 +(p-1)s^2)/2].
def radial_drift(p, a, s, k):
    p = Fraction(p)
    a = Fraction(a)
    s = Fraction(s)
    k = Fraction(k)
    return p * (-a + (k*k + (p-1)*s*s) / 2)

for p in (2, 4, 6):
    print('RADIAL_p', p, 'DRIFT', radial_drift(p, 1, 1, 0))
for p in (2, 4, 6):
    print('SKEW_p', p, 'DRIFT', radial_drift(p, 1, 0, 1))

assert comm12 == L3
assert sum_squares == smul(-2, eye(3))
assert radial_drift(2, 1, 1, 0) == -1
assert radial_drift(4, 1, 1, 0) == 2
assert radial_drift(6, 1, 1, 0) == 9
assert radial_drift(2, 1, 0, 1) == -1
assert radial_drift(4, 1, 0, 1) == -2
assert radial_drift(6, 1, 0, 1) == -3
print('ALL_EXACT_CHECKS_PASSED')
