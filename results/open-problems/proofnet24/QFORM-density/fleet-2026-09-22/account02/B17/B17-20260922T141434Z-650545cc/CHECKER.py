from fractions import Fraction
import math

c_pos_edge = Fraction(57, 640)
c_neg_edge = Fraction(3, 80)
assert 2*c_pos_edge + c_neg_edge == Fraction(69, 320)

Ez2_pos = Fraction(1, 4)
Ez2_neg = Fraction(1, 2)
trans_pos = 6*(Ez2_pos-1)
trans_neg = 6*(Ez2_neg-1)
assert trans_pos == Fraction(-9, 2)
assert trans_neg == Fraction(-3, 1)

spec_pos = Fraction(-3, 8)
spec_neg = Fraction(-1, 4)
assert spec_pos < 0 and spec_neg < 0

gauss_subclass = math.pi/math.sqrt(2)
diffuse_floor = 3*math.sqrt(2)
assert gauss_subclass < math.pi < diffuse_floor

print('PASS')
print('equal_bank_relative_1_over_m =', Fraction(69,320))
print('translation_relative_terms =', trans_pos, trans_pos, trans_neg)
print('spectral_relative_terms =', spec_pos, spec_pos, spec_neg)
print('gaussian_input_sharp =', repr(gauss_subclass))
print('diffuse_lower_floor =', repr(diffuse_floor))
