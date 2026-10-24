#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt

# HARD7-05 exact self-check: degree-7 polynomial quasimode for the killed OU
# operator, exact conditional-moment recurrences, sixth-trace spectral separation,
# Kato-Temple top-eigenvalue enclosure, and persistence-exponent conversion.
# Every theorem-deciding comparison below is exact integer/rational arithmetic.
DROOT = 10**20
NATAN = 24
DEG = 7
MAXM = 2 * DEG


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


def neglog_bounds(x, N=44):
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


# Same source-valid Slepian grid and inherited exact sixth-trace certificate.
r = F(287831, 500000)
R = r * r
s2 = 1 - R
TRACE6_UPPER = F(15014436, 100000000)

sI = sqrt_point_bounds(s2)
gI = sqrt_point_bounds(1 + R)
sqrt2piI = sqrt_interval((2 * PI[0], 2 * PI[1]))
tI = (1 / sqrt2piI[1], 1 / sqrt2piI[0])
t2I = imul(tI, tI)
t3I = imul(t2I, tI)

asinr = asin_point(r)
asinR = asin_point(R)
atanr = atan_point(r)
P = iadd(C(F(1, 4)), iscale(F(1, 2), idiv(asinr, PI)))
aI = idiv(C(r), sI)

# Powers of s = sqrt(1-r^2), enclosed rationally.
sPow = [C(1)]
for _ in range(1, MAXM + 2):
    sPow.append(imul(sPow[-1], sI))

# Positive-half Gaussian moments G_m = int_0^inf x^m phi(x) dx.
Gmom = [None] * (MAXM + 1)
Gmom[0] = C(F(1, 2))
Gmom[1] = tI
for m in range(2, MAXM + 1):
    Gmom[m] = iscale(m - 1, Gmom[m - 2])
G = [[Gmom[i + j] for j in range(DEG + 1)] for i in range(DEG + 1)]

# One-step scalar families:
# A_m = int y^m phi(y) Phi((r/s)y) dy,
# B_m = int y^m phi(y) phi((r/s)y) dy.
B = [None] * (MAXM + 1)
B[0] = iscale(F(1, 2), imul(sI, tI))
B[1] = iscale(s2, t2I)
for m in range(2, MAXM + 1):
    B[m] = iscale((m - 1) * s2, B[m - 2])

A = [None] * (MAXM + 1)
A[0] = P
A[1] = iadd(iscale(F(1, 2), tI), imul(aI, B[0]))
for m in range(2, MAXM + 1):
    A[m] = iadd(iscale(m - 1, A[m - 2]), imul(aI, B[m - 1]))


def poly_add(P1, P2):
    out = dict(P1)
    for k, v in P2.items():
        out[k] = iadd(out.get(k, C(0)), v)
    return out


def poly_scale(P1, c):
    return {k: iscale(c, v) for k, v in P1.items()}


def poly_y_scale(P1, c):
    return {k + 1: iscale(c, v) for k, v in P1.items()}


# J_n(y) = E[X^n 1_{X>0} | Y=y] = q(y) Q_n(y) + p(y) P_n(y).
# The truncated-normal integration-by-parts recurrence is
# J_n = r y J_{n-1} + (n-1) s^2 J_{n-2}.
Jq = [{0: C(1)}, {1: C(r)}]
Jp = [{}, {0: sI}]
for n in range(2, DEG + 1):
    Jq.append(poly_add(poly_y_scale(Jq[n - 1], r),
                       poly_scale(Jq[n - 2], (n - 1) * s2)))
    Jp.append(poly_add(poly_y_scale(Jp[n - 1], r),
                       poly_scale(Jp[n - 2], (n - 1) * s2)))


def int_poly(poly, shift, seq):
    z = C(0)
    for p, coeff in poly.items():
        z = iadd(z, imul(coeff, seq[p + shift]))
    return z


# M_ij = <x^i, K x^j>.
M = [[iadd(int_poly(Jq[j], i, A), int_poly(Jp[j], i, B))
      for j in range(DEG + 1)] for i in range(DEG + 1)]

# Symmetry sanity: independent conditional evaluations must overlap.
for i in range(DEG + 1):
    for j in range(DEG + 1):
        assert max(M[i][j][0], M[j][i][0]) <= min(M[i][j][1], M[j][i][1])

# Middle-point scalar families for K^2:
# V_m = s^(m+1) t Q_m(r), with Q_m = int z^m phi(z) Phi(rz) dz.
H = [None] * MAXM
H[0] = iscale(F(1, 2), idiv(tI, gI))
H[1] = idiv(t2I, C(1 + R))
for m in range(2, MAXM):
    H[m] = iscale(m - 1, idiv(H[m - 2], C(1 + R)))

Q = [None] * MAXM
Q[0] = iadd(C(F(1, 4)), iscale(F(1, 2), idiv(atanr, PI)))
Q[1] = iadd(iscale(F(1, 2), tI), iscale(r, H[0]))
for m in range(2, MAXM):
    Q[m] = iadd(iscale(m - 1, Q[m - 2]), iscale(r, H[m - 1]))

V = [imul(imul(sPow[m + 1], tI), Q[m]) for m in range(MAXM)]

# W_m = int y^m phi(y) p(y)^2 dy.
tau = idiv(sI, gI)
tau2 = imul(tau, tau)
W = [None] * (MAXM - 1)
W[0] = iscale(F(1, 2), imul(tau, t2I))
W[1] = imul(tau2, t3I)
for m in range(2, MAXM - 1):
    W[m] = iscale(m - 1, imul(tau2, W[m - 2]))

# U_m = int y^m phi(y) q(y)^2 dy.
U = [None] * (MAXM + 1)
U[0] = iadd(
    C(F(1, 8)),
    iscale(F(1, 4), idiv(iadd(iscale(2, asinr), asinR), PI)),
)
U[1] = iadd(iscale(F(1, 4), tI), iscale(2, imul(aI, V[0])))
for m in range(2, MAXM + 1):
    U[m] = iadd(iscale(m - 1, U[m - 2]), iscale(2, imul(aI, V[m - 1]))


def Nij(i, j):
    z = C(0)
    for p, c in Jq[i].items():
        for q, d in Jq[j].items():
            z = iadd(z, imul(imul(c, d), U[p + q]))
    for p, c in Jq[i].items():
        for q, d in Jp[j].items():
            z = iadd(z, imul(imul(c, d), V[p + q]))
    for p, c in Jp[i].items():
        for q, d in Jq[j].items():
            z = iadd(z, imul(imul(c, d), V[p + q]))
    for p, c in Jp[i].items():
        for q, d in Jp[j].items():
            z = iadd(z, imul(imul(c, d), W[p + q]))
    return z


N = [[Nij(i, j) for j in range(DEG + 1)] for i in range(DEG + 1)]
for i in range(DEG + 1):
    for j in range(DEG + 1):
        assert max(N[i][j][0], N[j][i][0]) <= min(N[i][j][1], N[j][i][1])

# Rational degree-seven quasimode chosen before this checker.
c = [F(x) for x in (
    100000000, 66277120, 7826678, -3196811,
    -506238, 417141, -75196, 4570,
)]


def quad_interval(A0):
    z = C(0)
    for i in range(DEG + 1):
        for j in range(DEG + 1):
            z = iadd(z, iscale(c[i] * c[j], A0[i][j]))
    return z


qI = quad_interval(G)
mI = quad_interval(M)
nrawI = quad_interval(N)
assert qI[0] > 0 and mI[0] > 0 and nrawI[0] > 0

muI = idiv(mI, qI)
nI = idiv(nrawI, qI)

# epsilon^2 = <f,K^2f>/<f,f> - mu^2.
eps2_lo = nI[0] - muI[1] ** 2
eps2_hi = nI[1] - muI[0] ** 2
assert 0 < eps2_lo <= eps2_hi
assert eps2_hi < F(38, 10**12)  # < 3.8e-11

# Spend at least mu^6 of the inherited sixth-trace budget on lambda_1.
# Then lambda_2^6 <= tr(K^6)-mu^6.  Use the exact coarse cap beta=0.302.
beta = F(151, 500)
spectral_remainder = TRACE6_UPPER - muI[0] ** 6
assert spectral_remainder < beta ** 6
assert muI[0] > beta

# Kato-Temple: lambda_1 <= mu + epsilon^2/(mu-beta).
lambda1_upper = muI[1] + eps2_hi / (muI[0] - beta)
LAMBDA_RATIONAL_CAP = F(72843224, 100000000)  # 0.72843224
assert lambda1_upper < LAMBDA_RATIONAL_CAP

# Persistence conversion inherited from the source-valid Slepian comparison:
# theta >= -log(lambda_1) / (4 * -log r).
target = F(14344477, 100000000)  # 0.14344477
neglog_cap = neglog_bounds(LAMBDA_RATIONAL_CAP, 36)
neglog_r = neglog_bounds(r, 44)
log_margin = neglog_cap[0] - 4 * target * neglog_r[1]
assert log_margin > 0

old_lower = F(286879, 2000000)       # 0.1434395
old_width = F(213121, 2000000)       # 0.1065605
new_width = F(1, 4) - target
improvement = target - old_lower

assert new_width == F(10655523, 100000000)
assert improvement == F(527, 100000000)
assert old_width - new_width == improvement

print("degree =", DEG)
print("mu interval =", float(muI[0]), float(muI[1]))
print("normalized K2 interval =", float(nI[0]), float(nI[1]))
print("residual^2 interval =", float(eps2_lo), float(eps2_hi))
print("spectral remainder upper =", float(spectral_remainder))
print("beta^6 =", float(beta ** 6))
print("lambda2 cap =", float(beta))
print("Kato lambda1 upper =", float(lambda1_upper))
print("rational lambda1 cap =", float(LAMBDA_RATIONAL_CAP))
print("log comparison margin =", float(log_margin))
print("certified theta lower =", float(target))
print("new bracket width =", float(new_width))
print("width improvement =", float(improvement))
print("ALL_EXACT_CHECKS_PASS = True")
