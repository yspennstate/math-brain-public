#!/usr/bin/env python3
"""
R17 exact checker for C021.

Starting from the fully archived R17-C020 h=8 cone certificate at
z=3209/10000, replace the previous giant-integer endpoint power comparison by
an exact rational enclosure of logarithms.  This converts essentially all of
the C020 continuous cone margin into a deterministic rational endpoint.

No floating-point or Monte Carlo arithmetic is used in any theorem check.
"""
from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 100

LAM = Fraction(
    1205756908493739750118272911119587569742420049311,
    3527335053202052628125000000000000000000000000000,
)
A_BASE = Fraction(3209, 5000)  # 2z
U_OLD = Fraction(287817, 348329)
U_NEW = Fraction(82627917856021403631, 10**20)
L = Fraction(99083249, 125000000)

assert 0 < LAM < 1
assert 0 < A_BASE < 1
assert U_NEW < U_OLD

def neglog_bounds(x: Fraction, terms: int):
    """
    For 0<x<1, u=(1-x)/(1+x) lies in (0,1) and
      -log(x)=2*sum_{k>=0} u^(2k+1)/(2k+1).
    Return exact rational lower/upper bounds after `terms` summands.
    """
    u = (1 - x) / (1 + x)
    s = Fraction(0)
    power = u
    for k in range(terms):
        j = 2*k + 1
        s += power / j
        power *= u*u
    lower = 2*s
    first_omitted = 2*terms + 1
    tail_upper = 2*power / (first_omitted * (1-u*u))
    return lower, lower + tail_upper, tail_upper

A_lo, A_hi, A_tail = neglog_bounds(A_BASE, 50)
L_lo, L_hi, L_tail = neglog_bounds(LAM, 110)

# C020 gives gamma_2 <= 2*(-log A_BASE)/(-log LAM).
# For U_NEW=p/q, exact sufficient condition is 2 q A_hi < p L_lo.
p, q = U_NEW.numerator, U_NEW.denominator
margin = p*L_lo - 2*q*A_hi
assert margin > 0

B_lo = 2*A_lo/L_hi
B_hi = 2*A_hi/L_lo
assert B_lo < B_hi < U_NEW < U_OLD

improvement = U_OLD - U_NEW
width = U_NEW - L

def dec(x: Fraction):
    return Decimal(x.numerator) / Decimal(x.denominator)

print("R17-C021 exact logarithmic endpoint compiler")
print("DEPENDENCY=R17-C020 exact all-state cone certificate")
print("A_BASE=3209/5000")
print("lambda_num=", LAM.numerator, sep="")
print("lambda_den=", LAM.denominator, sep="")
print("ATANH_TERMS_A=50")
print("ATANH_TERMS_LAMBDA=110")
print("A_tail_upper_decimal=", dec(A_tail), sep="")
print("lambda_tail_upper_decimal=", dec(L_tail), sep="")
print("EXACT_LOG_MARGIN_POSITIVE=PASS")
print("margin_decimal=", dec(margin), sep="")
print("continuous_bound_lower_decimal=", dec(B_lo), sep="")
print("continuous_bound_upper_decimal=", dec(B_hi), sep="")
print("CERTIFIED_NEW_UPPER=", U_NEW, sep="")
print("CERTIFIED_NEW_UPPER_DECIMAL=", dec(U_NEW), sep="")
print("PREVIOUS_UPPER=", U_OLD, sep="")
print("UPPER_DECREASE=", improvement, sep="")
print("UPPER_DECREASE_DECIMAL=", dec(improvement), sep="")
print("CERTIFIED_NEW_WIDTH=", width, sep="")
print("CERTIFIED_NEW_WIDTH_DECIMAL=", dec(width), sep="")
print("ALL_EXACT_CHECKS_PASS")
