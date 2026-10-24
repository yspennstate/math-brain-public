#!/usr/bin/env python3
"""Exact arithmetic stress-test for P26 audit of R19-I0084-C002.

This checker does not replace the Huang--Wang analytic argument. It verifies
only the elementary finite inequalities used in P26's independent parameterized
gap-point audit and the retained sparse-weight/moment estimates.
"""
from fractions import Fraction

W_upper = Fraction(1, 8) + Fraction(1, 992)
assert W_upper == Fraction(125, 992)
assert W_upper < Fraction(1, 4)

# R19 midpoint theta=1/2.
q12 = Fraction(1, 1)
C12 = Fraction(9, 1)
assert q12 == 1
assert C12 == 9

# P26 alternate point theta=1/3.
# q(theta)=3/(4 theta)-1/(4(1-theta));
# C(theta)=2/theta^2+1/(4(1-theta)^2).
q13 = Fraction(15, 8)
C13 = Fraction(297, 16)
K2 = C13 * C13 / (q13 * q13 * q13)
assert K2 == Fraction(6534, 125)
margin = Fraction(29, 4) ** 2 - K2
assert margin == Fraction(581, 2000)
assert margin > 0

# Doubly-exponential geometry and a finite exact sanity core.
for n in range(2, 9):
    A = 2 ** (2 ** n)
    Aprev = 2 ** (2 ** (n - 1))
    assert Aprev * Aprev == A
    if n >= 3:
        # This is stronger than the theta=1/3 requirement Aprev <= A/6.
        assert 6 * Aprev <= A
    w = Fraction(1, (2 ** n) * (A ** n))
    assert w <= Fraction(1, 32 ** n)

# Critical 5/2-moment tail exponent bound used by the sparse law.
for n in range(3, 20):
    exponent = Fraction(-n, 1) + (Fraction(5, 2) - n) * (2 ** n)
    rhs = Fraction(-n - 2 ** (n - 1), 1)
    assert exponent <= rhs

print("W_upper=125/992 < 1/4 = True")
print("theta=1/2: q=1 C=9 threshold_K=9")
print("theta=1/3: q=15/8 C=297/16")
print("K_squared=6534/125")
print("(29/4)^2-K_squared=581/2000 > 0")
print("A_n=A_{n-1}^2 exact for n=2..8")
print("sqrt(A_n)<=A_n/6 exact for n=3..8")
print("w_n<=32^{-n} exact for n=2..8")
print("5/2-moment tail exponent inequality exact for n=3..19")
print("ALL_EXACT_CHECKS_PASS")
