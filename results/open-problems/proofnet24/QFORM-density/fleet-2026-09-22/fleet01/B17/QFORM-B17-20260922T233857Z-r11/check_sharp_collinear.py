#!/usr/bin/env python3
from fractions import Fraction
import math

q = Fraction(52933, 76545)
gap = Fraction(1, 2) - q*q
assert gap > 0
assert float(q) < 1/math.sqrt(2)

# Case-I constant cancellation in the Hölder+sinc argument.
holder_bound = (12*math.pi)**0.25 * (2*math.sqrt(3*math.pi))**0.5
assert abs(holder_bound - math.sqrt(12*math.pi)) < 1e-12
F_ceiling = holder_bound / math.sqrt(24*math.pi)
assert abs(F_ceiling - 1/math.sqrt(2)) < 1e-12
C_ceiling = 6*F_ceiling
assert abs(C_ceiling - 3*math.sqrt(2)) < 1e-12

# Partner fleet02/B17 r19 endpoint for delta=1.
partner_delta1 = 3*math.sqrt(2)/math.sqrt(1+1)
assert abs(partner_delta1 - 3.0) < 1e-12

print('PASS')
print('heavy_upper =', f'{q.numerator}/{q.denominator}', '=', float(q))
print('1/sqrt(2) =', 1/math.sqrt(2))
print('exact_square_gap =', f'{gap.numerator}/{gap.denominator}')
print('F_ceiling =', F_ceiling)
print('C_ceiling =', C_ceiling)
print('partner_delta1_endpoint =', partner_delta1)
