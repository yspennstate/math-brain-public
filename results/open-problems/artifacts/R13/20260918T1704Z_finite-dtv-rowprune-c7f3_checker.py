#!/usr/bin/env python3
"""R13 exact arithmetic check for the finite-dimensional DTV row-pruning bound.

This is a self-check of the finite witness n=86.  It uses only Fraction arithmetic
plus the classical rational bounds 157/50 < pi < 355/113 and the elementary
inequality exp(-x) >= 1-x for x>=0.

It certifies:
  * h = 7507/1000 gives D_86 = ceil(86^2/h^2) = 132;
  * sqrt(2*pi) < 25067/10000 and sqrt(132) < 1149/100 under pi<355/113;
  * the analytic tail lower bound implies C_132 < 7508/1000;
  * h < 7508/1000 < 3*sqrt(2*pi), using pi>157/50.
Hence the new high-n branch is strictly below the old 3*sqrt(2*pi) branch at n=86.
"""
from fractions import Fraction

h = Fraction(7507, 1000)
n = 86
ratio = Fraction(n*n, 1) / (h*h)
D = (ratio.numerator + ratio.denominator - 1) // ratio.denominator
assert D == 132

# Classical rational enclosures for pi.
pi_lo = Fraction(157, 50)      # 3.14 < pi
pi_hi = Fraction(355, 113)     # pi < 355/113

# Rational upper bounds needed to lower-bound p_D.
q_sqrt_2pi = Fraction(25067, 10000)
q_sqrt_D = Fraction(1149, 100)
assert q_sqrt_2pi*q_sqrt_2pi > 2*pi_hi
assert q_sqrt_D*q_sqrt_D > D

# For L=9, p_D = 2 exp(-1/(18D)) / (81 sqrt(2*pi) D^(3/2)).
# Use exp(-x) >= 1-x and the rational upper bounds on the denominator.
x = Fraction(1, 18*D)
p_lower = Fraction(2, 1) * (1-x) / (
    Fraction(81, 1) * q_sqrt_2pi * D * q_sqrt_D
)

# P(max_i Y_i >= 9D) >= 1-(1-p_lower)^D.
P_lower = 1 - (1-p_lower)**D
# Identity 2(1-a_D)=E(sqrt(X)-1)^2 and X>=9 on this event give
# 1-a_D >= 2 P(event).
delta_lower = 2 * P_lower

# C_D = 3 sqrt(2*pi)(1-delta_D).  Upper-bound sqrt(2*pi) by q_sqrt_2pi.
C_upper = 3 * q_sqrt_2pi * (1-delta_lower)
target = Fraction(7508, 1000)
assert C_upper < target
assert h < target

# Old branch 3 sqrt(2*pi) is strictly above 7.508 from pi>3.14.
assert (target/Fraction(3, 1))**2 < 2*pi_lo

print("R13_FINITE_DTV_ROWPRUNE_EXACT_PASS")
print("h =", h)
print("D_86 =", D)
print("86^2/h^2 =", ratio)
print("p_lower ~=", float(p_lower))
print("P_event_lower ~=", float(P_lower))
print("delta_lower ~=", float(delta_lower))
print("C_132_upper ~=", float(C_upper))
print("certified: max(h,C_132) < 7.508 < 3*sqrt(2*pi)")
