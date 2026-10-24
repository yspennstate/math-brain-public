from fractions import Fraction
from math import e, sqrt, exp, gamma, pi

# 8-sample linear-intersection stability constants.
a = Fraction(63, 64) ** 2
upper_eighth_moment = a ** 4 + (Fraction(5, 4) - a) ** 4
threshold = Fraction(57, 64)  # 1 - 28/256
margin = threshold - upper_eighth_moment
assert margin > 0

# Collision-payment constants.
cross_cut_constant = 6 * e * (768 ** (1/6))
pair_area_constant = 128 * sqrt(2) * sqrt(1152)
assert cross_cut_constant < 50
assert abs(pair_area_constant - 6144) < 1e-10

# True-near-coloop transverse-bank constants.
# q<1/16, rho<1/64, ||b||>=sqrt(255)/16,
# sigma_2(W_B)>1/sqrt(32).
star_amp_lower = sqrt(255)/(64*sqrt(2)) - Fraction(1,128)
assert star_amp_lower > Fraction(1,6)
# Physical hub r_0=sqrt(c)e, c>63/64, hence each selected bank has
# sum_{j in B} A_{0j}^2 > c*(1/6)^2 > 7/256.
physical_star_energy_lower = Fraction(63,64) * Fraction(1,36)
assert physical_star_energy_lower == Fraction(7,256)

# If |q|>=1/100, the scalar-pivot theorem pays the true near-coloop.
scalar_pivot_constant = 128 * sqrt(Fraction(640,63))
assert scalar_pivot_constant < 408

# In the remaining |q|<1/100 branch, apply the completed two-bank
# row-energy/small-ball theorem with kappa=1/32 and c>63/64.
kappa = Fraction(1,32)
delta = Fraction(1,100)
c = Fraction(63,64)
rstar = sqrt(float(c)) * (sqrt(float(kappa))*sqrt(1-float(delta)**2)-float(delta))
smallball_constant = exp(0.5) * gamma(0.25) / sqrt(2*rstar)
assert rstar > 0.165
assert smallball_constant < 10.392

print('QFORM_B11_R36_COLLISION_NEARCOLOOP_CHECK_PASS')
print('eighth_moment_upper=', float(upper_eighth_moment))
print('57/64=', float(threshold))
print('strict_margin=', float(margin))
print('cross_cut_constant=', cross_cut_constant)
print('pair_area_constant=', pair_area_constant)
print('bank_star_amplitude_lower=', float(star_amp_lower))
print('physical_star_energy_lower=', float(physical_star_energy_lower))
print('scalar_pivot_constant=', scalar_pivot_constant)
print('two_bank_rstar=', rstar)
print('two_bank_sqrt_smallball_constant=', smallball_constant)
