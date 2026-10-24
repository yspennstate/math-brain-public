from fractions import Fraction
from math import sqrt, e

# Exact algebra behind 1/sqrt(7)+sqrt(3)/6 < 2/3.
# Squaring the equivalent positive inequality 4-sqrt(3) > 6/sqrt(7)
# reduces after one more isolation/square to 97^2 > 3*56^2.
assert 97 * 97 == 9409
assert 3 * 56 * 56 == 9408
assert 97 * 97 > 3 * 56 * 56

eta = Fraction(1, 64)
sigma = Fraction(3, 32)  # worst case delta=1/2
gamma = float(sigma) / sqrt(3.0)
lev = (1.0 / sqrt(7.0) + float(eta) / gamma) ** 2
assert lev < 4.0 / 9.0 < 0.5

theta = Fraction(9, 4)
assert theta > 2
assert theta / (theta - 2) == 9

C = 96.0 * sqrt(3.0 * e / 2.0)
assert C < 194.0

print('QFORM_CONDITIONED_SPECTRAL_WINDOW_CONSTANTS_PASS')
print('ridge_diag_upper=', repr(lev))
print('theta_lower=', str(theta))
print('density_constant_upper=', repr(C))
