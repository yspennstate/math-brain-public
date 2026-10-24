#!/usr/bin/env python3
"""Exact-rational certificate for the QFORM s9 scalar-pivot constant."""

from fractions import Fraction as F
from math import factorial


def exp_lower(x, degree):
    return sum((x**k) / factorial(k) for k in range(degree + 1))


def exp_upper(x, degree):
    partial = exp_lower(x, degree)
    first = x ** (degree + 1) / factorial(degree + 1)
    ratio = x / (degree + 2)
    assert ratio < 1
    return partial + first / (1 - ratio)


def atan_upper(x, last_even):
    assert last_even % 2 == 0
    return sum((-1 if k % 2 else 1) * x ** (2*k+1) / (2*k+1)
               for k in range(last_even + 1))


def atan_lower(x, last_odd):
    assert last_odd % 2 == 1
    return sum((-1 if k % 2 else 1) * x ** (2*k+1) / (2*k+1)
               for k in range(last_odd + 1))


# Machin: pi/4 = 4 atan(1/5) - atan(1/239).
x5, x239 = F(1, 5), F(1, 239)
pi_lower = 4 * (4 * atan_lower(x5, 9) - atan_upper(x239, 0))
pi_upper = 4 * (4 * atan_upper(x5, 10) - atan_lower(x239, 1))
assert pi_lower > F(314159, 100000)
assert pi_upper < F(355, 113)

assert exp_lower(F(173287, 250000), 14) > 2
assert exp_lower(F(69271, 50000), 18) > F(399649, 100000)
assert exp_upper(F(1), 13) ** 3 < F(291, 200) ** 8

# Gamma(3/8): [0,1] alternating upper polynomial, [1,8]
# interval majorants, and a monotone tail bound.
gamma_upper = sum(F((-1)**k, factorial(k)) * F(8, 8*k+3)
                  for k in range(11))
den = 10**12
for j in range(128, 1024):
    a, b = F(j, 128), F(j+1, 128)
    lo, hi = 0, 4*den
    while lo < hi:
        mid = (lo + hi) // 2
        if F(mid, den) ** 8 * a ** 5 >= 1:
            hi = mid
        else:
            lo = mid + 1
    ua = F(lo, den)
    assert ua ** 8 * a ** 5 >= 1
    gamma_upper += ua * (1 / exp_lower(a, 45) - 1 / exp_upper(b, 45))

a = F(8)
lo, hi = 0, den
while lo < hi:
    mid = (lo + hi) // 2
    if F(mid, den) ** 8 * a ** 5 >= 1:
        hi = mid
    else:
        lo = mid + 1
u8 = F(lo, den)
gamma_upper += u8 / exp_lower(a, 45)
assert gamma_upper < F(2371, 1000)

assert F(15423, 10000) ** 8 > 32
assert F(75113, 100000) ** 4 * F(314159, 100000) > 1
cq_upper = (F(15423, 10000) * F(75113, 100000) *
            F(291, 200) * F(2371, 1000))
assert cq_upper < F(399649, 100000)

log2_upper = F(173287, 250000)
logcq_upper = F(69271, 50000)
llog_upper = 4 + 4 * logcq_upper
htr_upper = 10 * (F(355, 113) + 4*log2_upper + 2*llog_upper)
final_upper = 10 * (htr_upper + 1)
assert final_upper < 2510

print("gamma_upper", float(gamma_upper))
print("C_q_upper", float(cq_upper))
print("scalar_density_constant_upper", float(final_upper))
print("CERTIFIED: scalar-pivot branch < 2510")
