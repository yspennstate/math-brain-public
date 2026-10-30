from fractions import Fraction
import math

eps = Fraction(1, 2**18)
C = 21.59066859519
assert 12 * math.sqrt(float(eps)) == 3/128
assert Fraction(1, 3*2**18) == Fraction(1, 786432)
assert Fraction(1, 12*2**18) == Fraction(1, 3145728)
print('epsilon', float(eps))
print('rank2_tube', 12*math.sqrt(float(eps)))
print('diffuse_density_bound', C*float(eps)**(-1/6))
print('nested_anchor_mass', Fraction(1, 3*2**18))
print('nested_four_bank_mass', Fraction(1, 12*2**18))
