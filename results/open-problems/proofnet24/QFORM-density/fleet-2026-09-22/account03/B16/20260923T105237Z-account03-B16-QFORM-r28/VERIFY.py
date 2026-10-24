from fractions import Fraction
from math import sqrt, e

alpha_bound = Fraction(95, 4032)
u_bound = ((1 + 1/sqrt(31))/8)**2
cstar = Fraction(643, 7936)
score_floor = Fraction(63, 32) * sqrt(float(cstar) / 64)
constant = 3 * e * score_floor**(-1/3)
partner = 12 * 64**(1/6)

print('alpha_bound =', float(alpha_bound))
print('u01_bound =', u_bound)
print('score_floor =', score_floor)
print('density_constant =', constant)
print('partner_threshold =', partner)

assert alpha_bound < Fraction(1, 40)
assert u_bound < 1/32
assert constant < 19.8
assert abs(partner - 24.0) < 1e-12
print('STATUS=PASS')
