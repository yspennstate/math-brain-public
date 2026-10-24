#!/usr/bin/env python3
"""Arithmetic checker for the C*=6.5218512 fixed-core threat-corridor theorem.

The analytic ingredients (shared-core cocycle, strong concavity, maximizer
bracket, and integer-depth forcing ceiling) are proved in the cited peer
reports.  This script checks only the exact constant propagation used by B16.
"""
from decimal import Decimal, getcontext
getcontext().prec = 90
D = Decimal

C = D('6.5218512')
Mplus = D('6.52185121301287772365150440023918196647146413881')
Tint_upper = D('6.521851180069836')
ell = D('0.002713295')
u = D('0.002713296')
alpha = D(9)/D(256)
d0 = D(133)/D(128)

# Exact ratios simplify to d0/alpha = 266/9 and (128/9)d0 = 133/9.
assert d0/alpha == D(266)/D(9)
assert (D(128)/D(9))*d0 == D(133)/D(9)

gap = Mplus-C
assert D('1.3012877723651504e-8') < gap < D('1.301287772365151e-8')

deficit_cap = (d0/alpha)*gap
assert deficit_cap < D('3.8460283050e-7')
assert deficit_cap > D('3.8460283049e-7')

# K'' <= -9/64 implies K(b) <= K(b*)-(9/128)(b-b*)^2.
# Using only K(b*)/d0 < Mplus and b* in (ell,u), any point with T(b)>C
# must lie within this radius of [ell,u].
radius = ((D(133)/D(9))*gap).sqrt()
assert radius < D('0.000438521853')
assert radius > D('0.000438521852')
left = ell-radius
right = u+radius
assert left > D('0.002274773147')
assert right < D('0.003151817853')

# The entire adaptive integer one-branch family has T(b)<=Tint_upper<C.
integer_gap = C-Tint_upper
integer_defect_floor = d0*integer_gap
assert integer_gap == D('1.9930164e-8')
assert integer_defect_floor == D('2.070868603125e-8')

print('PASS')
print('C_star=', C)
print('Mplus_minus_C=', gap)
print('universal_input_deficit_cap=', deficit_cap)
print('threat_radius=', radius)
print('threat_interval_outer=', left, right)
print('integer_forcing_gap=', integer_gap)
print('integer_output_defect_floor_for_safe_input=', integer_defect_floor)
print('full_FEI=OPEN_NOT_PROVED')
