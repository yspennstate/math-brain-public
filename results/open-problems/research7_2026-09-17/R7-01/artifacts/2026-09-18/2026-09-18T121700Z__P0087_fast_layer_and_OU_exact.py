from fractions import Fraction as F
from itertools import permutations


def T(A):
    return [list(x) for x in zip(*A)]


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))


def rank3(A):
    A = [row[:] for row in A]
    r = 0
    for c in range(3):
        piv = next((i for i in range(r, 3) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        q = A[r][c]
        A[r] = [x/q for x in A[r]]
        for i in range(3):
            if i != r and A[i][c] != 0:
                q = A[i][c]
                A[i] = [A[i][j] - q*A[r][j] for j in range(3)]
        r += 1
    return r


def eye(n=3):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def scale(A, a):
    return [[a*x for x in row] for row in A]


def stationary_check(pi, Q):
    return [sum(pi[i]*Q[i][j] for i in range(3)) for j in range(3)] == pi


def lyap_check(Q, pi, C):
    I = eye()
    B = sub(I, Q)
    P = [[I[i][j] - pi[j] for j in range(3)] for i in range(3)]
    lhs = madd(mm(B, C), mm(C, T(B)))
    rhs = mm(P, T(P))
    support = [sum(C[i][j]*pi[j] for j in range(3)) for i in range(3)]
    return lhs == rhs and support == [F(0), F(0), F(0)], lhs, rhs


# Deliberately nonnormal / defective irreducible row-stochastic test.
Qd = [
    [F(1,2), F(1,2), F(0)],
    [F(0),   F(1,2), F(1,2)],
    [F(1,8), F(3,8), F(1,2)],
]
pid = [F(1,9), F(4,9), F(4,9)]
assert all(sum(row) == 1 for row in Qd)
assert stationary_check(pid, Qd)
assert det3(sub(Qd, eye())) == 0
assert det3(sub(Qd, scale(eye(), F(1,4)))) == 0
assert rank3(sub(Qd, scale(eye(), F(1,4)))) == 2
# Trace=3/2 and determinant=1/16, together with roots 1 and 1/4,
# certify characteristic polynomial (lambda-1)(lambda-1/4)^2.
assert sum(Qd[i][i] for i in range(3)) == F(3,2)
assert det3(Qd) == F(1,16)
kappa_d = sum(x*x for x in pid)
assert kappa_d == F(11,27)

# Normalized stationary covariance: C_y = y(1-y) C0.
C0d = [
    [ F(88,81), -F(8,81),   -F(14,81)],
    [-F(8,81),   F(22,81),  -F(20,81)],
    [-F(14,81), -F(20,81),   F(47,162)],
]
ok_d, lhs_d, rhs_d = lyap_check(Qd, pid, C0d)
assert ok_d


# Period-three irreducible row-stochastic stress test.
Qp = [
    [F(0), F(1), F(0)],
    [F(0), F(0), F(1)],
    [F(1), F(0), F(0)],
]
pip = [F(1,3), F(1,3), F(1,3)]
assert all(sum(row) == 1 for row in Qp)
assert stationary_check(pip, Qp)
assert mm(mm(Qp, Qp), Qp) == eye()
kappa_p = sum(x*x for x in pip)
assert kappa_p == F(1,3)
Pp = [[eye()[i][j] - pip[j] for j in range(3)] for i in range(3)]
C0p = scale(Pp, F(1,3))
ok_p, lhs_p, rhs_p = lyap_check(Qp, pip, C0p)
assert ok_p

print('Q_def stationary pi =', pid)
print('Q_def kappa =', kappa_d)
print('Q_def rank(Q-1/4 I) =', rank3(sub(Qd, scale(eye(), F(1,4)))))
print('Q_def det(Q) =', det3(Qd), 'trace(Q) =', sum(Qd[i][i] for i in range(3)))
print('Q_def C0 =', C0d)
print('Q_def exact Lyapunov certificate = PASS')
print('Q_periodic kappa =', kappa_p)
print('Q_periodic Q^3 = I =', mm(mm(Qp, Qp), Qp) == eye())
print('Q_periodic C0 =', C0p)
print('Q_periodic exact Lyapunov certificate = PASS')
print('ALL_EXACT_CHECKS_PASS')
