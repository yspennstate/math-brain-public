from fractions import Fraction
from math import e, sqrt

c = Fraction(2349, 5000)
ratio = c / (1-c)
assert ratio == Fraction(2349, 2651)

K_half = 4*sqrt(2*e)
K_partner = 16*sqrt(2*e)*(Fraction(2651,2349))**0.25

assert K_half < 9.327
assert K_partner < 38.452

# Rank-two regularization implication:
# if z_i^2 > c and z_i^2 = s_i^2/(g^2+s_i^2), then
# s_i^2/g^2 > c/(1-c).
# Hence s1*s2 > ratio*g^2 and with g=gamma/16 the pivot bound is K_partner/sqrt(|a0| gamma).

print('c_star=', float(c))
print('c_over_1mc=', float(ratio))
print('K_half=', K_half)
print('K_partner=', K_partner)
print('QFORM_B08_RANK2_CROSS_HALF_RIESZ_CHECK_PASS')
