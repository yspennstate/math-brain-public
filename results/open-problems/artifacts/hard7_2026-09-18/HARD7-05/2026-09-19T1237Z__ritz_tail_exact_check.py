#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt

# HARD7-05 exact self-check, 2026-09-19.
# Three-dimensional even-polynomial Ritz compression for the killed AR(1)
# operator, followed by exact spectral-tail subtraction from the inherited
# six-cycle trace certificate. All theorem-deciding comparisons below are
# exact integer/rational comparisons; printed decimals are diagnostics only.

DROOT = 10**10
NATAN = 10


def sqrt_interval(x):
    assert x > 0
    m = isqrt((DROOT * DROOT * x.numerator) // x.denominator)
    lo, hi = F(m, DROOT), F(m + 1, DROOT)
    assert lo * lo <= x < hi * hi
    return lo, hi


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


# Machin's identity gives a rigorous rational enclosure of pi.
a5 = atan_series_bounds(F(1, 5), 18)
a239 = atan_series_bounds(F(1, 239), 5)
pi_lo = 16 * a5[0] - 4 * a239[1]
pi_hi = 16 * a5[1] - 4 * a239[0]
assert pi_lo < pi_hi


def atan_point_interval(t):
    if t < 0:
        lo, hi = atan_point_interval(-t)
        return -hi, -lo
    if t <= F(1, 2):
        return atan_series_bounds(t)
    if t <= 2:
        u = (t - 1) / (t + 1)
        lo, hi = atan_series_bounds(u)
        return pi_lo / 4 + lo, pi_hi / 4 + hi
    lo, hi = atan_series_bounds(1 / t)
    return pi_lo / 2 - hi, pi_hi / 2 - lo


def asin_point_interval(x):
    assert 0 <= x < 1
    slo, shi = sqrt_interval(1 - x * x)
    tlo, thi = x / shi, x / slo
    lo, _ = atan_point_interval(tlo)
    _, hi = atan_point_interval(thi)
    return lo, hi


# Basic outward interval arithmetic over exact rationals.
def iadd(x, y):
    return x[0] + y[0], x[1] + y[1]


def isub(x, y):
    return x[0] - y[1], x[1] - y[0]


def imul(x, y):
    vals = (x[0] * y[0], x[0] * y[1], x[1] * y[0], x[1] * y[1])
    return min(vals), max(vals)


def iscale(c, x):
    return (c * x[0], c * x[1]) if c >= 0 else (c * x[1], c * x[0])


def det2(A):
    return isub(imul(A[0][0], A[1][1]), imul(A[0][1], A[1][0]))


def det3(A):
    a, b, c = A[0]
    d, e, f = A[1]
    g, h, i = A[2]
    t1 = imul(a, isub(imul(e, i), imul(f, h)))
    t2 = imul(b, isub(imul(d, i), imul(f, g)))
    t3 = imul(c, isub(imul(d, h), imul(e, g)))
    return iadd(isub(t1, t2), t3)


# Same source-valid Slepian grid as the preceding HARD7-05 trace proof.
r = F(287831, 500000)
R = r * r
slo, shi = sqrt_interval(1 - R)
aslo, ashi = asin_point_interval(r)

# For (X,Y) standard bivariate normal with corr(X,Y)=r, set
# P=P(X>0,Y>0), h=r*sqrt(1-r^2)/(2*pi).
P = (F(1, 4) + aslo / (2 * pi_hi), F(1, 4) + ashi / (2 * pi_lo))
h = (r * slo / (2 * pi_hi), r * shi / (2 * pi_lo))


def lin(ap, ah):
    return iadd(iscale(ap, P), iscale(ah, h))


# M_ij=<x^(2i), K x^(2j)> on x>0, i,j=0,1,2.
# Repeated one-dimensional Gaussian integration by parts gives these exact
# bivariate truncated-moment identities.
M = [
    [lin(1, 0), lin(1, 1), lin(3, 5 - 2 * R)],
    [lin(1, 1), lin(1 + 2 * R, 3), lin(3 + 12 * R, 13 + 2 * R)],
    [lin(3, 5 - 2 * R), lin(3 + 12 * R, 13 + 2 * R),
     lin(9 + 72 * R + 24 * R * R, 55 + 50 * R)],
]

# G_ij=<x^(2i),x^(2j)>_{L2(gamma; x>0)}.
G = [
    [F(1, 2), F(1, 2), F(3, 2)],
    [F(1, 2), F(3, 2), F(15, 2)],
    [F(3, 2), F(15, 2), F(105, 2)],
]


def shift(q):
    return [[(M[i][j][0] - q * G[i][j], M[i][j][1] - q * G[i][j])
             for j in range(3)] for i in range(3)]


# Inertia certificate for the second generalized Ritz value.
a = F(7, 25)
A = shift(a)
A00_lo = A[0][0][0]
detA = det3(A)
assert A00_lo > 0
assert detA[1] < 0

# Sylvester certificate for the third generalized Ritz value.
b = F(21, 200)
B = shift(b)
B00_lo = B[0][0][0]
detB2 = det2(B)
detB3 = det3(B)
assert B00_lo > 0
assert detB2[0] > 0
assert detB3[0] > 0

# By min-max, lambda_2>=a and lambda_3>=b. Subtract their sixth powers
# from the inherited exact upper bound tr(K^6)<15014436/10^8.
trace6_coarse = F(15014436, 100000000)
tail_floor = a ** 6 + b ** 6
lambda1_6_hi = trace6_coarse - tail_floor
assert lambda1_6_hi > 0

# Certify theta >= 14331/100000. Since Delta=4 log(1/r), it suffices that
# lambda1^6 < r^(24*theta); after clearing the rational exponent this is
# the exact integer comparison below.
target = F(14331, 100000)
assert 24 * target == F(42993, 12500)
power_certificate = lambda1_6_hi ** 12500 < r ** 42993
assert power_certificate

width = F(1, 4) - target
old_width = F(53467, 500000)
improvement = old_width - width
assert width == F(10669, 100000)
assert improvement == F(61, 250000)

print('P interval =', float(P[0]), float(P[1]))
print('h interval =', float(h[0]), float(h[1]))
print('nu2 inertia: A00_lo =', float(A00_lo), 'detA_hi =', float(detA[1]))
print('nu3 Sylvester: B00_lo =', float(B00_lo),
      'detB2_lo =', float(detB2[0]), 'detB3_lo =', float(detB3[0]))
print('tail_floor =', tail_floor, '=', float(tail_floor))
print('lambda1^6 upper =', lambda1_6_hi, '=', float(lambda1_6_hi))
print('power_certificate =', power_certificate)
print('certified theta lower =', target, '=', float(target))
print('new bracket width =', width, '=', float(width))
print('width improvement =', improvement, '=', float(improvement))
print('ALL_EXACT_CHECKS_PASS = True')
