from fractions import Fraction as F
from itertools import product
import mpmath as mp

iv = mp.iv


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(x) for x in zip(*A)]


def diag(vals):
    n = len(vals)
    return [[vals[i] if i == j else F(0) for j in range(n)] for i in range(n)]


def assert_equal(A, B, name):
    assert A == B, (name, A, B)


# A genuinely overlapping variance-inversion example.  The first Givens
# rotation mixes variances 2 and 1, while the fresh variance 3 exceeds the
# conditional residual variance, so the earlier fresh-leaf theorem does not
# apply to the second rotation.
Q = [
    [F(3, 5), F(4, 5), F(0)],
    [F(-4, 13), F(3, 13), F(12, 13)],
    [F(48, 65), F(-36, 65), F(5, 13)],
]
I = diag([F(1), F(1), F(1)])
assert_equal(matmul(Q, transpose(Q)), I, "QQT")
assert_equal(matmul(transpose(Q), Q), I, "QTQ")

Lam = diag([F(2), F(1), F(3)])
C = matmul(matmul(Q, Lam), transpose(Q))
C_expected = [
    [F(34, 25), F(-12, 65), F(144, 325)],
    [F(-12, 65), F(473, 169), F(408, 845)],
    [F(144, 325), F(408, 845), F(7779, 4225)],
]
assert_equal(C, C_expected, "C")
assert sum(C[i][i] for i in range(3)) == F(6)


def ivf(q):
    return iv.mpf(q.numerator) / q.denominator


def orthant_first_second_moment(K):
    """E[U1^2 1_{U1,U2,U3>=0}] for U~N(0,K), using the closed formula."""
    k11, k22, k33 = K[0][0], K[1][1], K[2][2]
    a = K[0][1] / iv.sqrt(k11 * k22)
    b = K[0][2] / iv.sqrt(k11 * k33)
    c = K[1][2] / iv.sqrt(k22 * k33)

    # arcsin(x)=atan2(x,sqrt(1-x^2)) on [-1,1].  Keeping the computation
    # inside mpmath.iv gives outward interval enclosures throughout.
    asin = lambda x: iv.atan2(x, iv.sqrt(1 - x * x))
    P = iv.mpf(1) / 8 + (asin(a) + asin(b) + asin(c)) / (4 * iv.pi)
    correction = (
        a * iv.sqrt(1 - a * a)
        + b * iv.sqrt(1 - b * b)
        + (2 * a * b - c * (a * a + b * b)) / iv.sqrt(1 - c * c)
    )
    return k11 * (P + correction / (4 * iv.pi))


def cone_matrix(i, eps):
    """Map one minimum/sign cone to the positive orthant."""
    others = [j for j in range(3) if j != i]
    B = [[F(0) for _ in range(3)] for __ in range(3)]
    B[0][i] = F(eps[i])
    B[1][others[0]] = F(eps[others[0]])
    B[1][i] = -F(eps[i])
    B[2][others[1]] = F(eps[others[1]])
    B[2][i] = -F(eps[i])
    return B


def to_iv_matrix(A):
    return [[ivf(x) for x in row] for row in A]


def expected_min_square(Cq):
    # The 24 cones (3 choices of minimum coordinate x 8 sign patterns)
    # partition R^3 up to Gaussian-null boundaries.
    total = iv.mpf(0)
    for i in range(3):
        for eps in product([-1, 1], repeat=3):
            B = cone_matrix(i, eps)
            Kq = matmul(matmul(B, Cq), transpose(B))
            total += orthant_first_second_moment(to_iv_matrix(Kq))
    return total


Emin_rot = expected_min_square(C)
Emin_KL = expected_min_square(Lam)
gap = Emin_rot - Emin_KL

# For p=3,d=2, retained energy is trace minus the minimum square.  Hence the
# retained-energy excess is -gap and its normalized excess is -gap/trace.
normalized_retained_excess = -gap / 6

# Coarse rational enclosures deliberately leave a large margin relative to
# interval width.  They are the human-readable certificate quoted in the report.
assert gap > iv.mpf(49) / 1000
assert gap < iv.mpf(123) / 2500
assert normalized_retained_excess > -iv.mpf(41) / 5000
assert normalized_retained_excess < -iv.mpf(49) / 6000

print("PROB20-19 exact+interval self-check")
print("mpmath_version", mp.__version__)
print("Q_exact_orthogonality PASS")
print("C_exact", C)
print("trace_C", sum(C[i][i] for i in range(3)))
print("Emin_rot_interval", Emin_rot)
print("Emin_KL_interval", Emin_KL)
print("Emin_gap_interval", gap)
print("rational_gap_certificate 49/1000 < Emin_rot-Emin_KL < 123/2500")
print("normalized_retained_excess_interval", normalized_retained_excess)
print("rational_normalized_certificate -41/5000 < (F2_rot-F2_KL)/trace < -49/6000")
print("ALL_CHECKS_PASS")
