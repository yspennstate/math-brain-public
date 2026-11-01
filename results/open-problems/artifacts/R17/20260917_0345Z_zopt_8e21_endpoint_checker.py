#!/usr/bin/env python3
"""
R17-C022 exact endpoint compiler.

Dependency: the exact all-state h=8 cone certificate produced by the companion
C++ checker at
    z = 3208963 / 10000000
with
    lambda =
      28820304203953213132874757
      / 84313600646000000000000000.

This file uses Fraction arithmetic only for theorem checks.  Decimal is used
only to display already-certified rationals.
"""
from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec = 100

z = Fraction(3208963, 10_000_000)
a = 2*z
lam = Fraction(
    28820304203953213132874757,
    84313600646000000000000000,
)
U_old = Fraction(82627917856021403631, 10**20)
U_new = Fraction(826279178542431497521, 10**21)
L = Fraction(99083249, 125_000_000)

assert 0 < a < 1
assert 0 < lam < 1
assert U_new < U_old

def neglog_bounds(x: Fraction, terms: int):
    """
    u=(1-x)/(1+x).  For 0<x<1,
      -log x = 2 sum_{k>=0} u^(2k+1)/(2k+1).
    The omitted positive tail is at most
      2*u^(2m+1)/((2m+1)*(1-u^2)).
    """
    u = (1-x)/(1+x)
    s = Fraction(0)
    power = u
    for k in range(terms):
        s += power / (2*k+1)
        power *= u*u
    lo = 2*s
    hi = lo + 2*power / ((2*terms+1)*(1-u*u))
    return lo, hi

A_lo, A_hi = neglog_bounds(a, 80)
Lam_lo, Lam_hi = neglog_bounds(lam, 160)

# Lueker gives gamma_2 <= 2*(-log(2z))/(-log(lambda)).
B_lo = 2*A_lo/Lam_hi
B_hi = 2*A_hi/Lam_lo

# Exact endpoint certificate.
assert B_lo < B_hi < U_new

improvement = U_old - U_new
width = U_new - L

def dec(x):
    return Decimal(x.numerator) / Decimal(x.denominator)

print("R17-C022 exact logarithmic endpoint compiler")
print("z =", z)
print("lambda =", lam)
print("EXACT_LOG_INTERVAL_PASS")
print("continuous_bound_lower_decimal =", dec(B_lo))
print("continuous_bound_upper_decimal =", dec(B_hi))
print("CERTIFIED_NEW_UPPER =", U_new)
print("CERTIFIED_NEW_UPPER_DECIMAL =", dec(U_new))
print("PREVIOUS_UPPER =", U_old)
print("UPPER_DECREASE =", improvement)
print("UPPER_DECREASE_DECIMAL =", dec(improvement))
print("CERTIFIED_NEW_WIDTH =", width)
print("CERTIFIED_NEW_WIDTH_DECIMAL =", dec(width))
print("ALL_EXACT_CHECKS_PASS")
