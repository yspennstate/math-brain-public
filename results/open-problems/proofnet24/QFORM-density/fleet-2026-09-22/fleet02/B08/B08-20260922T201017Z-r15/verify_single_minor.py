from fractions import Fraction

rho = Fraction(256, 257)
theta = 2*rho
bank = rho*rho

assert rho > Fraction(99,100)
assert theta < Fraction(201,100)
assert theta > Fraction(256,129)
assert bank > Fraction(576,625)

print('rho =', rho, float(rho))
print('theta =', theta, float(theta))
print('partner_theta_lower =', Fraction(256,129), float(Fraction(256,129)))
print('partner_theta_upper =', Fraction(201,100), float(Fraction(201,100)))
print('normalized_bank =', bank, float(bank))
print('single_normalized_minor_at_dimension_d = rho/d')
print('single_physical_minor_at_dimension_d = gamma^2/d')
print('QFORM_B08_SINGLE_MINOR_NOGO_CHECK_PASS')
