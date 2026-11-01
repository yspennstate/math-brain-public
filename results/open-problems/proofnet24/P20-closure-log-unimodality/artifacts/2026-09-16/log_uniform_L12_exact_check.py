#!/usr/bin/env python3
"""Exact finite-arithmetic checks for P20 I0081 log-uniform counterexample.

This script does NOT certify the analytic branch or curvature derivation; those are
proved symbolically in the run report.  It certifies the finite rational
inequalities used to turn that derivation into the explicit L=12 sign.
"""

from fractions import Fraction

# e > 1+1+1/2+1/6+1/24 = 65/24 > 27/10.
e_partial = Fraction(65, 24)
assert e_partial > Fraction(27, 10)

# Hence e^12 > (27/10)^12 > 100000, so a=e^{-12}<10^{-5}.
pow27 = 27**12
assert pow27 > 10**17

# Classical rational upper bound pi < 22/7 implies pi^2 < 10.
pi2_upper = Fraction(22, 7) ** 2
assert pi2_upper < 10

# With a<10^-5, P_a(phi)>=(1-a)/(1+a), so for L=12
# A = 12*csc(t)^2*P_a(phi)-1 > this exact rational lower bound.
a_upper = Fraction(1, 100000)
A_lower = 12 * (1 - a_upper) / (1 + a_upper) - 1
assert A_lower == Fraction(1099987, 100001)
assert A_lower > 0

# Curvature correction coefficient
#   C_12 = a(1-a^2)(144+pi^2)^2/[12(1-a)^4]
# is bounded using a<10^-5, pi^2<10, 1-a^2<1, and 1-a>1/2.
C_upper = a_upper * (144 + 10) ** 2 * Fraction(16, 12)
assert C_upper == Fraction(5929, 18750)
assert C_upper < 1

print("P20 I0081 exact finite check: PASS")
print(f"65/24 = {e_partial} > 27/10")
print(f"27^12 = {pow27} > 10^17")
print(f"(22/7)^2 = {pi2_upper} < 10")
print(f"A_lower = {A_lower} > 0")
print(f"C_12_upper = {C_upper} < 1")
