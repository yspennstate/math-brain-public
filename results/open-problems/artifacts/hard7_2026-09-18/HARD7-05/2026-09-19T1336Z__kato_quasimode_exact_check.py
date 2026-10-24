#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt

# HARD7-05 exact self-check: degree-2 polynomial quasimode + Kato-Temple.
# All theorem-deciding comparisons use exact integers/rationals.
DROOT = 10**16
NATAN = 24


def sqrt_point_bounds(x):
    assert x > 0
    m = isqrt((DROOT * DROOT * x.numerator) // x.denominator)
    lo, hi = F(m, DROOT), F(m + 1, DROOT)
    assert lo * lo <= x < hi * hi
    return lo, hi


def sqrt_interval(I):
    return sqrt_point_bounds(I[0])[0], sqrt_point_bounds(I[1])[1]


def atan_series_bounds(x, m=NATAN):
    if x < 0:
        lo, hi = atan_series_bounds(-x, m)
        return -hi, -lo
    assert 0 <= x <= F(1, 2)
    s = F(0)
    for k in range(m + 1):
        s += F((-1) ** k, 2 * k + 1) * x ** (2 * k + 1)
    nxt = F((-1) ** (m + 1), 2 * (m + 1) + 1) * x ** (2 * (m + 1) + 1)
    return min(s, s + nxt), max(s, s + nxt)


a5 = atan_series_bounds(F(1, 5), 32)
a239 = atan_series_bounds(F(1, 239), 9)
PI = (16 * a5[0] - 4 * a239[1], 16 * a5[1] - 4 * a239[0])


def iadd(x, y):
    return x[0] + y[0], x[1] + y[1]


def imul(x, y):
    vals = (x[0] * y[0], x[0] * y[1], x[1] * y[0], x[1] * y[1])
    return min(vals), max(vals)


def iscale(c, x):
    return (c * x[0], c * x[1]) if c >= 0 else (c * x[1], c * x[0])


def idiv(x, y):
    assert y[0] > 0
    return imul(x, (1 / y[1], 1 / y[0]))


def C(x):
    return F(x), F(x)


def atan_point(t):
    if isinstance(t, tuple):
        lo, _ = atan_point(t[0])
        _, hi = atan_point(t[1])
        return lo, hi
    if t < 0:
        lo, hi = atan_point(-t)
        return -hi, -lo
    if t <= F(1, 2):
        return atan_series_bounds(t)
    if t <= 2:
        u = (t - 1) / (t + 1)
        lo, hi = atan_series_bounds(u)
        return PI[0] / 4 + lo, PI[1] / 4 + hi
    lo, hi = atan_series_bounds(1 / t)
    return PI[0] / 2 - hi, PI[1] / 2 - lo


def asin_point(x):
    s = sqrt_point_bounds(1 - x * x)
    return atan_point((x / s[1], x / s[0]))


def neglog_bounds(x, N=30):
    # -log x = 2 sum_{k>=0} z^(2k+1)/(2k+1), z=(1-x)/(1+x).
    assert 0 < x < 1
    z = (1 - x) / (1 + x)
    partial = F(0)
    for k in range(N + 1):
        partial += z ** (2 * k + 1) / F(2 * k + 1)
    lo = 2 * partial
    m = 2 * N + 3
    tail = 2 * z ** m / F(m) / (1 - z * z)
    return lo, lo + tail


# Same source-valid Slepian grid and inherited trace certificate.
r = F(287831, 500000)
R = r * r
s2 = 1 - R
TRACE6_UPPER = F(15014436, 100000000)

sI = sqrt_point_bounds(s2)
gI = sqrt_point_bounds(1 + R)
sqrt2piI = sqrt_interval((2 * PI[0], 2 * PI[1]))
tI = (1 / sqrt2piI[1], 1 / sqrt2piI[0])  # t=1/sqrt(2*pi)
t2I = imul(tI, tI)
t3I = imul(t2I, tI)
invpiI = (1 / PI[1], 1 / PI[0])

asinr = asin_point(r)
asinR = asin_point(R)
atanr = atan_point(r)
P = iadd(C(F(1, 4)), iscale(F(1, 2), idiv(asinr, PI)))
h = iscale(r / 2, imul(sI, invpiI))

# M_ij = <x^i, K x^j> on x>0, i,j=0,1,2.
M = [[None] * 3 for _ in range(3)]
M[0][0] = P
M[0][1] = M[1][0] = iscale((1 + r) / 2, tI)
M[0][2] = M[2][0] = iadd(P, h)
M[1][1] = iadd(iscale(r, P), iscale(F(1, 2), imul(sI, invpiI)))
M[1][2] = M[2][1] = iscale((1 + r) ** 2 / 2, tI)
M[2][2] = iadd(iscale(1 + 2 * R, P), iscale(3, h))

# G_ij = <x^i,x^j> on x>0.
G = [
    [C(F(1, 2)), tI, C(F(1, 2))],
    [tI, C(F(1, 2)), iscale(2, tI)],
    [C(F(1, 2)), iscale(2, tI), C(F(3, 2))],
]

# For N_ij=<x^i,K^2 x^j>, condition on the middle AR(1) site.
# Let q(y)=Phi(a y), p(y)=phi(a y), a=r/s.
# J0=q, J1=r y q+s p, J2=(r^2 y^2+s^2)q+r s y p.
# We need U_m=int y^m phi q^2, V_m=int y^m phi q p, W_m=int y^m phi p^2.

# V_m = s^(m+1) t Q_m(r), with Q_m=int z^m phi(z) Phi(r z) dz.
Q0 = iadd(C(F(1, 4)), iscale(F(1, 2), idiv(atanr, PI)))
H0 = iscale(F(1, 2), idiv(tI, gI))
Q1 = iadd(iscale(F(1, 2), tI), iscale(r, H0))
H1 = idiv(t2I, C(1 + R))
Q2 = iadd(Q0, iscale(r, H1))
g3I = imul(C(1 + R), gI)
H2 = iscale(F(1, 2), idiv(tI, g3I))
Q3 = iadd(iscale(2, Q1), iscale(r, H2))

s3I = imul(C(s2), sI)
s4I = C(s2 * s2)
V = [
    imul(imul(sI, tI), Q0),
    imul(imul(C(s2), tI), Q1),
    imul(imul(s3I, tI), Q2),
    imul(imul(s4I, tI), Q3),
]

# W_m is elementary after combining the three Gaussian densities.
tau = idiv(sI, gI)
tau2 = imul(tau, tau)
tau3 = imul(tau2, tau)
W = [
    iscale(F(1, 2), imul(tau, t2I)),
    imul(tau2, t3I),
    iscale(F(1, 2), imul(tau3, t2I)),
]

# Trivariate orthant base term and integration-by-parts recursion for U_m.
aI = idiv(C(r), sI)
U = [None] * 5
U[0] = iadd(
    C(F(1, 8)),
    iscale(F(1, 4), idiv(iadd(iscale(2, asinr), asinR), PI)),
)
U[1] = iadd(iscale(F(1, 4), tI), iscale(2, imul(aI, V[0])))
U[2] = iadd(U[0], iscale(2, imul(aI, V[1])))
U[3] = iadd(iscale(2, U[1]), iscale(2, imul(aI, V[2])))
U[4] = iadd(iscale(3, U[2]), iscale(2, imul(aI, V[3])))

N = [[None] * 3 for _ in range(3)]
N[0][0] = U[0]
N[0][1] = N[1][0] = iadd(iscale(r, U[1]), imul(sI, V[0]))
N[0][2] = N[2][0] = iadd(
    iadd(iscale(R, U[2]), iscale(s2, U[0])),
    iscale(r, imul(sI, V[1])),
)
N[1][1] = iadd(
    iadd(iscale(R, U[2]), iscale(2 * r, imul(sI, V[1]))),
    iscale(s2, W[0]),
)

x = C(0)
for term in (
    iscale(r ** 3, U[3]),
    iscale(r * s2, U[1]),
    iscale(2 * R, imul(sI, V[2])),
    imul(s3I, V[0]),
    iscale(r * s2, W[1]),
):
    x = iadd(x, term)
N[1][2] = N[2][1] = x

x = C(0)
for term in (
    iscale(R ** 2, U[4]),
    iscale(2 * R * s2, U[2]),
    iscale(s2 ** 2, U[0]),
    iscale(2 * r ** 3, imul(sI, V[3])),
    iscale(2 * r, imul(s3I, V[1])),
    iscale(R * s2, W[2]),
):
    x = iadd(x, term)
N[2][2] = x

# Rational quasimode f(x)=100000+75665 x-2316 x^2 on x>0.
c = [F(100000), F(75665), F(-2316)]


def quad_interval(A):
    ans = C(0)
    for i in range(3):
        for j in range(3):
            ans = iadd(ans, iscale(c[i] * c[j], A[i][j]))
    return ans


qI = quad_interval(G)
mI = quad_interval(M)
nrawI = quad_interval(N)
assert qI[0] > 0 and mI[0] > 0 and nrawI[0] > 0
muI = idiv(mI, qI)
nI = idiv(nrawI, qI)

# Residual epsilon^2 = <f,K^2 f>/<f,f> - mu^2.
eps2_hi = nI[1] - muI[0] ** 2
assert eps2_hi > 0

# Spectral-separation input for Kato-Temple:
# lambda_2^6 <= tr K^6 - lambda_1^6 <= TRACE6_UPPER - mu^6.
beta = F(31, 100)
assert TRACE6_UPPER - muI[0] ** 6 < beta ** 6
assert muI[0] > beta

# Kato-Temple upper bound on the top eigenvalue.
lambda1_upper = muI[1] + eps2_hi / (muI[0] - beta)
LAMBDA_RATIONAL_CAP = F(18211, 25000)  # 0.72844
assert lambda1_upper < LAMBDA_RATIONAL_CAP

# Convert the operator bound to a persistence exponent without floating logs.
target = F(286879, 2000000)  # 0.1434395
neglog_cap = neglog_bounds(LAMBDA_RATIONAL_CAP, 24)
neglog_r = neglog_bounds(r, 34)
assert neglog_cap[0] > 4 * target * neglog_r[1]

old_lower = F(14331, 100000)
old_width = F(10669, 100000)
new_width = F(1, 4) - target
improvement = target - old_lower
assert new_width == F(213121, 2000000)
assert improvement == F(259, 2000000)
assert old_width - new_width == improvement

print("mu interval =", float(muI[0]), float(muI[1]))
print("normalized K2 interval =", float(nI[0]), float(nI[1]))
print("residual^2 upper =", float(eps2_hi))
print("lambda2 cap =", float(beta))
print("Kato lambda1 upper =", float(lambda1_upper))
print("rational lambda1 cap =", float(LAMBDA_RATIONAL_CAP))
print("log comparison margin =", float(neglog_cap[0] - 4 * target * neglog_r[1]))
print("certified theta lower =", float(target))
print("new bracket width =", float(new_width))
print("width improvement =", float(improvement))
print("ALL_EXACT_CHECKS_PASS = True")
