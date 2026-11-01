from fractions import Fraction
import math

eps = Fraction(1, 2**18)
reviewed_diffuse_bound = 72*math.sqrt(3*math.e)
assert 12*math.sqrt(float(eps)) == 3/128
assert Fraction(1,3*2**18) == Fraction(1,786432)
assert Fraction(1,12*2**18) == Fraction(1,3145728)
print('epsilon', float(eps))
print('rank2_tube', 3/128)
print('reviewed_Dprime_density_bound', reviewed_diffuse_bound)
print('nested_anchor_mass', Fraction(1,786432))
print('nested_four_bank_mass', Fraction(1,3145728))
