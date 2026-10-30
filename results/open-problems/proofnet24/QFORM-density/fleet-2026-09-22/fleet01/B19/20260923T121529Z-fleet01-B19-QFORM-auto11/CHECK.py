from fractions import Fraction
from math import sqrt, e

c0 = Fraction(65025, 262144)
delta = Fraction(1, 64)
rank1_floor = Fraction(63,64) - 3*delta
rank2_floor = 1-delta
z3_den = 64*64*(64*225)
C_tail = 36*sqrt(3)*e/sqrt(float(c0))
C_Dprime = 9*sqrt(3*e)*(z3_den**(1/6))/sqrt(float(c0))

assert rank1_floor == Fraction(15,16)
assert rank2_floor == Fraction(63,64)
assert z3_den == 58982400
assert 3*z3_den == 176947200

print('c0 =', float(c0))
print('rank1 top singular fraction >', rank1_floor)
print('rank2 top-two fraction >', rank2_floor)
print('Z3 lower denominator =', z3_den)
print('tail-theorem universal bound =', C_tail)
print('Dprime universal bound =', C_Dprime)
print('joint anchored volume denominator =', 3*z3_den)
print('QFORM_B19_STAR_TAIL_CLASSIFICATION_CHECK_PASS')
