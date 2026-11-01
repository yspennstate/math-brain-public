from fractions import Fraction
from math import e

# Exact rational bounds in QFORM-TWO-BANK-COCIRCUIT-FRESNEL-v1.
beta = Fraction(1, 63)
gamma = Fraction(189, 1984)
alpha_rest = (beta + gamma) / 2
Z_lower = Fraction(63, 2048)
C = 3 * e * float(Fraction(2048, 63)) ** (1/3)

print('beta_upper =', beta, float(beta))
print('gamma_upper =', gamma, float(gamma))
print('alpha_rest_upper =', alpha_rest, float(alpha_rest))
print('alpha_rest_lt_half =', alpha_rest < Fraction(1, 2))
print('Z_lower =', Z_lower, float(Z_lower))
print('C =', C)
print('C_lt_27 =', C < 27)

assert alpha_rest < Fraction(1, 2)
assert Z_lower > 0
assert C < 27
print('STATUS=PASS')
