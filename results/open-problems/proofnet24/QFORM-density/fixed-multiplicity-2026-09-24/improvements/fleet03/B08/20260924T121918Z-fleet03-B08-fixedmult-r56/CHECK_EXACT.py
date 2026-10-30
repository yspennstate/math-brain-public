from fractions import Fraction
from math import sqrt, e

eta = Fraction(1,100)
eps = Fraction(1,16)
off = Fraction(1,7) + eps
beta = eta + 4*off
s12_lower = Fraction(15,16) - beta
delta4 = (Fraction(15,16)-eta) - 3*off
amin = delta4/2
detP = amin**4
cross_constant = 2*sqrt(e)*sqrt(700/109)

assert off == Fraction(23,112)
assert beta == Fraction(291,350)
assert s12_lower == Fraction(297,2800)
assert delta4 == Fraction(109,350)
assert amin == Fraction(109,700)
assert detP == Fraction(109,700)**4
assert cross_constant < 8.357

print('QFORM_B08_R56_EXACT_CHECK_PASS')
print('off=', off, float(off))
print('beta=', beta, float(beta))
print('s12_lower=', s12_lower, float(s12_lower))
print('delta4=', delta4, float(delta4))
print('amin=', amin, float(amin))
print('detP_lower=', detP, float(detP))
print('conditional_cross_constant=', cross_constant)
