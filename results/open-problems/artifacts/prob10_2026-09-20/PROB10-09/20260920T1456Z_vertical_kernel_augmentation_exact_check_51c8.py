#!/usr/bin/env python3
"""Exact/core arithmetic and falsification checks for the matching PROB10-09
vertical-kernel augmentation report.  This checks arithmetic and theorem-side
inequalities only; it is not independent source validation.
"""
from fractions import Fraction
import math


def beta(D, a):
    q = D - 1
    if a <= 2 * math.sqrt(q):
        return math.sqrt(q)
    return (a + math.sqrt(a * a - 4 * q)) / 2

# Frozen g=4, m=6 graph.  D=22, adjacency norm <=14.
# A fully rational NB test at p=81/1000 avoids relying on decimal radicals.
p = Fraction(81, 1000)
z = 1 / p
q = 21
z2_minus_q = z*z - q
char_slack = z + Fraction(q,1)/z - 14
assert z2_minus_q > 0
assert char_slack > 0
print("SCALAR_Z2_MINUS_Q", z2_minus_q)
print("SCALAR_CHAR_SLACK", char_slack)

# The free rank-seven marked subset gives p_c <=1/13.
gap = p - Fraction(1, 13)
assert gap == Fraction(53, 13000)
assert gap > Fraction(1,250)
print("RATIONAL_GAP", gap)
print("RATIONAL_GAP_MINUS_1_250", gap-Fraction(1,250))

# Stronger closed-form floor: beta_22(14)=7+2sqrt(7), so
# 1/beta=(7-2sqrt(7))/21 and exact gap is (70-26sqrt(7))/273.
# To prove this exceeds 1/250, reduce to 17227 > 6500 sqrt(7).
radical_square_margin = 17227**2 - (6500**2)*7
assert radical_square_margin > 0
print("RADICAL_SQUARE_MARGIN", radical_square_margin)

# Exact vertical-budget negation test at genus four.
# m=6: beta_22(14)=7+2sqrt(7)<13 because sqrt(7)<3.
assert 9 > 7
print("M6_PASS_SQUARE_MARGIN", 9-7)
# m=7: beta_23(15)=(15+sqrt(137))/2>13 because sqrt(137)>11.
assert 137 > 121
print("M7_FAIL_SQUARE_MARGIN", 137-121)

# Alternate two-type horizontal/vertical resolvent certificate.
# Horizontal data: D0=16, r_Q<=8, q0=15; m=6.
p_alt = Fraction(39,500)
den = 1 - 8*p_alt + 15*p_alt*p_alt
f = 1 - 14*p_alt + 15*p_alt*p_alt + 6*p_alt**3
feedback = 6*p_alt*(1-p_alt*p_alt)/den
assert den > 0
assert f > 0
assert feedback < 1
print("TWO_TYPE_DEN", den)
print("TWO_TYPE_F", f)
print("TWO_TYPE_FEEDBACK_LT1_SLACK", 1-feedback)
print("TWO_TYPE_GAP_OVER_1_13", p_alt-Fraction(1,13))

# Cheeger-only route cannot certify the frozen m=6 graph with the available
# Mohar/Dodziuk quotient bound: beta=7+2sqrt(7)>143/15.
# This follows from sqrt(7)>19/15.
cheeger_fail_margin = Fraction(7) - Fraction(19,15)**2
assert cheeger_fail_margin > 0
print("CHEEGER_FAIL_RADICAL_SQUARE_MARGIN", cheeger_fail_margin)

# Crude all-walk adjacency-resolvent route also fails: 1/14 < 1/13.
assert Fraction(1,14) < Fraction(1,13)
print("ALL_WALK_FAIL_GAP", Fraction(1,13)-Fraction(1,14))

# Falsification scan of the closed-form surface vertical-budget threshold.
# Proposed equivalence:
# beta_{4g+m}(4sqrt(g)+m)<4g-3 iff
# m < M_g=[4g^2-5g+2-(4g-3)sqrt(g)]/(g-1).
# Numerical scan is auxiliary only; the report contains the algebraic proof.
mismatches=[]
cases=0
for g in range(2,101):
    M=(4*g*g-5*g+2-(4*g-3)*math.sqrt(g))/(g-1)
    upper=min(100,max(0,int(math.ceil(M))+3))
    for m in range(upper):
        cases += 1
        lhs = beta(4*g+m, 4*math.sqrt(g)+m) < 4*g-3
        rhs = m < M
        if lhs != rhs:
            mismatches.append((g,m,M,lhs,rhs))
assert not mismatches
print("THRESHOLD_SCAN_CASES", cases)
print("THRESHOLD_SCAN_MISMATCHES", len(mismatches))
print("ALL_EXACT_CORE_CHECKS_PASS")
