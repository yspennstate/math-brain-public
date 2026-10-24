from fractions import Fraction
from math import sqrt

c0 = Fraction(2349, 5000)
p = Fraction(99, 100)
tau2 = Fraction(1, 100)
theta_hi = Fraction(201, 100)

arm2 = p - tau2
core2 = theta_hi - 2*p + tau2
err2 = tau2 + core2
star_bank_norm = sqrt(float(arm2))**2 - 0  # display aid only
star_bank_lower = Fraction(24, 25)
star_bank_sq = star_bank_lower * star_bank_lower
sigma2_lower = sqrt(float(arm2)) - sqrt(float(err2))

theta_m4 = 4 * Fraction(256, 257)

assert arm2 == Fraction(49, 50)
assert core2 == Fraction(1, 25)
assert err2 == Fraction(1, 20)
assert star_bank_sq == Fraction(576, 625)
assert star_bank_sq > c0
assert theta_m4 > theta_hi
assert sigma2_lower > 0

print('c0 =', c0, float(c0))
print('sqrt(c0) =', sqrt(float(c0)))
print('arm_energy_lower =', arm2, float(arm2))
print('core_energy_upper =', core2, float(core2))
print('star_error_energy_upper =', err2, float(err2))
print('sigma2_star_perturbation_lower =', sigma2_lower)
print('star_bank_norm_lower =', star_bank_lower, float(star_bank_lower))
print('star_bank_squared_lower =', star_bank_sq, float(star_bank_sq))
print('theta_m4_lower =', theta_m4, float(theta_m4))
print('theta_threshold =', theta_hi, float(theta_hi))
print('selected_frame_leverage_m8 =', Fraction(3, 16), float(Fraction(3, 16)))
print('QFORM_B08_BICOLOOP_SCHUR_STAR_CHECK_PASS')
