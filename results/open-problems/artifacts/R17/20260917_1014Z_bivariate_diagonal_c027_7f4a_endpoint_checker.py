#!/usr/bin/env python3
"""
R17-C027 exact endpoint compiler for the bivariate h=8 LCS cone certificate.

Dependency:
    x = 256701/800000,
    y = 256733/800000,
    A_{x,y} V <= lambda V componentwise on all 6,419,109 states,
where lambda is the exact maximum row ratio printed by the companion C++ checker.

The bivariate generating-function theorem proved in the R17 report gives
    gamma_2 <= log(4*x*y)/log(lambda).
All theorem comparisons below use Fraction arithmetic only.
"""
from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 110

x = Fraction(256701, 800000)
y = Fraction(256733, 800000)
lam = Fraction(
    31107964074938160190818541484674602978918848418821294684671225334220461,
    91006168618543357645705413918720000000000000000000000000000000000000000,
)
A = 4*x*y
L = Fraction(99083249, 125000000)
U_old = Fraction(826279178542397825380217, 10**24)
U_new = Fraction(826279177784605624, 10**18)

assert 0 < A < 1
assert 0 < lam < 1
assert U_new < U_old

def neglog_bounds(q: Fraction, terms: int):
    """Exact rational enclosure of -log(q), 0<q<1."""
    u = (1-q)/(1+q)
    s = Fraction(0)
    power = u
    for k in range(terms):
        s += power/(2*k+1)
        power *= u*u
    lo = 2*s
    hi = lo + 2*power/((2*terms+1)*(1-u*u))
    return lo, hi

A_lo, A_hi = neglog_bounds(A, 100)
L_lo, L_hi = neglog_bounds(lam, 160)

# log(A)/log(lam) = (-log A)/(-log lam), both positive.
B_lo = A_lo/L_hi
B_hi = A_hi/L_lo
assert B_lo < B_hi < U_new < U_old

improvement = U_old - U_new
width = U_new - L

def dec(q):
    return Decimal(q.numerator)/Decimal(q.denominator)

print("R17-C027 exact bivariate endpoint compiler")
print("x =", x)
print("y =", y)
print("4xy =", A)
print("lambda_num =", lam.numerator)
print("lambda_den =", lam.denominator)
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
