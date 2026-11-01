#!/usr/bin/env python3
from fractions import Fraction

# Printed rigorous genus-3 Markov-operator upper bound from Nagnibeda,
# as quoted in Bartholdi's Theorem 1.3, relaxed upward by 8e-6.
nagnibeda_M3_printed = Fraction(69099, 125000)   # 0.552792
M3_relax = Fraction(691, 1250)                   # 0.5528

# Exact rational upper bound for sqrt(14).
sqrt14_upper = Fraction(187083, 50000)           # 3.74166

assert M3_relax > nagnibeda_M3_printed
assert sqrt14_upper**2 > 14

# Standard surface-group adjacency norms:
# ||A_3|| <= 12 M3_relax;
# BCCH gives ||A_4|| <= 2 sqrt(14)+1.
A3_upper = 12 * M3_relax
A4_upper_rational = 1 + 2 * sqrt14_upper
Rbar = A3_upper + A4_upper_rational

# X_{3,4} has degree D=28, so Q=D-1=27 in the NB recurrence.
D = 28
Q = D - 1

# Candidate rigorous lower floor for p_{2->2}, hence p_u.
pu_floor = Fraction(383213, 5_000_000)            # 0.0766426
z = 1 / pu_floor

# If z>sqrt(Q) and z^2-Rbar*z+Q>0, then z lies above the larger
# root beta_D(Rbar), so beta_D(Rbar)<z and p_{2->2}>1/z.
z2_minus_Q = z*z - Q
poly = z*z - Rbar*z + Q

# Predecessor exact p_c upper bound and prior frozen gap.
pc_upper = Fraction(4_540_551, 100_000_000)      # 0.04540551
old_gap = Fraction(2_649_449, 100_000_000)       # 0.02649449
gap = pu_floor - pc_upper
delta = gap - old_gap

assert z2_minus_Q > 0
assert poly > 0
assert gap > old_gap

print('PROB10-09 BCCH SURFACE SPECTRAL UPGRADE EXACT CORE')
print('nagnibeda_relax_margin:', M3_relax - nagnibeda_M3_printed)
print('sqrt14_square_margin:', sqrt14_upper**2 - 14)
print('A3_upper:', A3_upper)
print('A4_upper_rational:', A4_upper_rational)
print('Rbar:', Rbar)
print('z:', z)
print('z2_minus_Q:', z2_minus_Q)
print('poly_at_z:', poly)
print('pu_floor:', pu_floor)
print('pc_upper:', pc_upper)
print('new_gap:', gap)
print('old_gap:', old_gap)
print('gap_delta:', delta)
print('ALL_EXACT_CHECKS_PASS')
