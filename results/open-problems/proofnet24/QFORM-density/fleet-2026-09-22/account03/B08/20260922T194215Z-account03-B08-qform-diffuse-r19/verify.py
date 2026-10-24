from fractions import Fraction
from math import e, sqrt

# Exact parameters used in QFORM-SYMMETRIC-RIDGE-OR-BICOLOOP-v1.
theta_min = Fraction(256, 129)
p = Fraction(99, 100)
theta0 = Fraction(201, 100)
q_hi = Fraction(2, 1)
s_hi = Fraction(399, 200)

assert theta_min > 2*p
beta0 = theta0/(2*q_hi)
beta_s = beta0*s_hi
assert beta_s == Fraction(80199, 80000) > 1
ratio = beta_s/(beta_s-1)
assert ratio == Fraction(80199, 199)

# Intersection exterior-volume reserve in the two-sided near-coloop branch.
F0 = 2*p*(theta0-1) - (theta0*theta0-p*p)/2
assert F0 == Fraction(2349, 5000)

# One-sided actual-H row/column exterior-volume reserve.
row_norm = p*(theta_min-1)
assert row_norm == Fraction(4191, 4300)
actual_coeff = row_norm/Fraction(16**4, 1)
assert actual_coeff == Fraction(4191, 281804800)

# High-effective-dimension q=2 + L^p + physical-square constant.
C_hi = (400**(200/399)+1) * e**0.25 * sqrt(8*float(ratio))
assert C_hi < 1543

# Previous 99-percent one-sided diffuse constant, re-used symmetrically.
C_99 = (1000**(500/999)+1) * sqrt((189440/3)*sqrt(e/99))
assert C_99 < 3349

# Compatible account04/B18 application when theta>=5 at g=gamma/16.
C_partner_theta5 = 4*sqrt(10)*e**0.25
assert C_partner_theta5 < 16.25

print('theta_min =', float(theta_min))
print('beta_s_min =', beta_s, '=', float(beta_s))
print('tail_ratio =', ratio, '=', float(ratio))
print('two_sided_intersection_reserve =', F0, '=', float(F0))
print('one_sided_normalized_reserve =', row_norm, '=', float(row_norm))
print('actual_H_gamma4_coefficient =', actual_coeff, '=', float(actual_coeff))
print('C_hi =', C_hi)
print('C_99 =', C_99)
print('C_partner_theta_ge_5 =', C_partner_theta5)
print('QFORM_SYMMETRIC_RIDGE_BICOLOOP_CHECK_PASS')
