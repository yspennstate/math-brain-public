#!/usr/bin/env python3
from fractions import Fraction
import itertools, math

print('PROB10-09 HORIZONTAL-ONLY CENTRAL AMALGAM CHECK')

# Exact radical lower bound used for the frozen genus-two quantitative gap.
s2lo = Fraction(707,500)
margin_s2 = Fraction(2,1) - s2lo*s2lo
assert margin_s2 > 0
print('sqrt2_lower=707/500; 2-lower^2 =', margin_s2)

# Frozen r=1,g=2,e=+-1 graph:
# gap >= (10 sqrt(2)-12)/35 > the rationalized lower bound below.
gap_lo = (10*s2lo - 12)/35
assert gap_lo == Fraction(107,1750)
target = Fraction(61,1000)
assert gap_lo > target
print('frozen_gap_exact_radical=(10*sqrt(2)-12)/35')
print('frozen_gap_rational_lower=', gap_lo)
print('frozen_gap_minus_61_over_1000=', gap_lo-target)

# Algebraic positivity used for every genus g>=2:
# (4g-2)^2-(4sqrt(g))^2 = 4*(4(g-1)^2-3) > 0.
for g in range(2,1001):
    algebraic_square_margin = 4*(4*(g-1)*(g-1)-3)
    assert algebraic_square_margin > 0
print('delta_square_margin_check_g_2_to_1000=PASS')

# Finite falsification scan only; the report gives the all-parameter algebraic proof.
def beta(D,R):
    q = D-1
    edge = 2*math.sqrt(q)
    if R <= edge:
        return math.sqrt(q)
    return (R + math.sqrt(R*R-4*q))/2

count = 0
minimum = (float('inf'), None)
for r in range(1,6):
    for gs in itertools.product(range(2,9), repeat=r):
        G = sum(gs)
        H = sum(math.sqrt(g) for g in gs)
        D = 4*G
        q = D-1
        t = 4*G-2*r-1
        assert t*t > q
        b = beta(D,4*H)
        assert b < t
        count += 1
        if t-b < minimum[0]:
            minimum = (t-b, gs)
print('finite_negation_scan_cases=', count)
print('finite_negation_scan_min_t_minus_beta=', repr(minimum[0]), 'at', minimum[1])

# Exact lower bound for t^2-q at the smallest G=2r is positive for all r>=1:
# 36r^2-20r+2. Verify a broad range as a guardrail.
for r in range(1,10001):
    assert 36*r*r - 20*r + 2 > 0
print('t_squared_minus_q_min_formula_guardrail_r_1_to_10000=PASS')
print('ALL_EXACT_CHECKS_PASS')
