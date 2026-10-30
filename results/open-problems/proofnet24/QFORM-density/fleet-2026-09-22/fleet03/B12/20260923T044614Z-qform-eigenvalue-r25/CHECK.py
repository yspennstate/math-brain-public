from fractions import Fraction
from math import e, pi, sqrt

# Exact split constant for b=9/8.
b = Fraction(9, 8)
split = Fraction(1, 2) + Fraction(1, 1) / (2-b) + Fraction(1, 1) / (b-1)
assert split == Fraction(135, 14)

# Large-shift crude bound is dominated by the displayed Holder constant.
assert 18 < Fraction(135, 7)

# Near-diffuse a-scale constants.
T_a = 8*e*pi*sqrt(3)/15
cap_a = 24*sqrt(3)*e/5
mod_a = 72*e*sqrt(3)/7
assert cap_a < 23

# Collective-tail G-scale constants.
T_G = e*pi*sqrt(3)/2
cap_G = 9*sqrt(3)*e/2
mod_G = 135*e*sqrt(3)/14

print('b=', float(b))
print('split=', split, float(split))
print('T_a coefficient=', T_a)
print('density coefficient / a=', cap_a)
print('translation coefficient / a=', mod_a)
print('T_G coefficient=', T_G)
print('tail density coefficient / G=', cap_G)
print('tail translation coefficient / G=', mod_G)
print('PASS')
