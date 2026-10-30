import math

Csq = 1 + 4*math.sqrt(2) + 8*(math.log(3/2) + 0.5*math.log(3))
partner_const = Csq / math.sqrt(2*math.pi)
c = 1e-4
lhs_lower = 1/(2*c)
partner_rhs = partner_const * c**(-0.5)
assert lhs_lower > partner_rhs

square_L43 = 3**(3/4) / math.sqrt(2)
ordinary_L2 = square_L43**2
assert abs(ordinary_L2 - 3**1.5/2) < 1e-12
ordinary_L2_sq = ordinary_L2**2
assert abs(ordinary_L2_sq - 27/4) < 1e-12

A43_sq = 2 / 3**(3/4)
sharp_L2 = A43_sq * ordinary_L2
assert abs(sharp_L2 - 3**(3/4)) < 1e-12
sharp_L2_sq = sharp_L2**2
assert abs(sharp_L2_sq - 3*math.sqrt(3)) < 1e-12
collision_const = 2*sharp_L2_sq
assert abs(collision_const - 6*math.sqrt(3)) < 1e-12

# r=3 member of the L^r ladder.
r = 3
Cr = (r+1)**((r+1)/r) * 2**(-2/r)
assert abs(Cr - 4) < 1e-12
third_square_L32 = 2
three_square_Linf = Cr * third_square_L32
assert abs(three_square_Linf - 8) < 1e-12

print('QFORM_B03_R19_CHECK_PASS')
print(f'Csq={Csq:.15f}')
print(f'partner_const={partner_const:.15f}')
print(f'counterexample_l2_lower={lhs_lower:.12f}')
print(f'partner_claimed_rhs={partner_rhs:.12f}')
print(f'sharp_L2_norm_constant={sharp_L2:.15f}')
print(f'sharp_L2_squared_constant={sharp_L2_sq:.15f}')
print(f'collision_constant={collision_const:.15f}')
print(f'r3_two_square_constant={Cr:.15f}')
print(f'three_square_Linf_constant={three_square_Linf:.15f}')
