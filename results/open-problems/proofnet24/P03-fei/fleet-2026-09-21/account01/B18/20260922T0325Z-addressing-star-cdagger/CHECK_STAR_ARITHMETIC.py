"""Arithmetic transfer for B18's source-candidate star lemma.

This does NOT independently re-read or interval-certify the h96 npz array.
It checks the deductions from deliberately weakened source-output premises:
  wobble_min > 2.22,
  G(2) > 17.8,
  each relevant consecutive node drop > -0.056,
and the h96 near-center mesh 1/2048.
"""
from decimal import Decimal, getcontext
getcontext().prec = 60

D = Decimal
C0 = D('6.4548')
Cdag = D('6.521851214')
a = D(4) * (Cdag - C0)
alpha = D(2) * (C0 - D(4))
wobble_floor = D('2.22')
G2_floor = D('17.8')
step_loss = D('0.056')

# x0 is reported here using Decimal logs only for diagnostics; the proof only
# needs an upper bound of 55 mesh steps. Python Decimal has no log2 on all
# supported versions, so use float for this non-critical diagnostic.
import math
x0 = float((D(2)*C0 - a/D(4) - wobble_floor) / alpha)
s0 = 2.0 ** (-x0)
steps = math.ceil(2048.0*(0.25-s0))
near_bracket = G2_floor - D(steps)*step_loss - D(2)*C0 + a/D(4)
far_at_x0 = alpha*D(str(x0)) + wobble_floor - D(2)*C0 + a/D(4)

assert a == D('0.268204856')
assert steps == 55
assert near_bracket == D('1.877451214')
assert near_bracket > 0
assert far_at_x0 > D('-1e-13')

print('PASS')
print('C0', C0)
print('Cdag', Cdag)
print('a_dagger', a)
print('alpha', alpha)
print('x0', format(x0, '.16f'))
print('s0', format(s0, '.16f'))
print('mesh_steps', steps)
print('near_star_bracket_lower', near_bracket)
print('far_boundary_roundoff_check', far_at_x0)
