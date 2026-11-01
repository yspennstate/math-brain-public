from fractions import Fraction
from math import sqrt, e

eps = Fraction(1, 32)
tau = Fraction(1, 39)
delta = Fraction(7, 32)
sigma = delta - tau
assert sigma == Fraction(241, 1248)

# Strict ridge-leverage certificate using rational upper bounds.
assert Fraction(1, 7) < Fraction(19, 50) ** 2
assert 6 * 32**2 * 500**2 < (163**2) * (241**2)
ridge_upper = Fraction(19, 50) + Fraction(163, 500)
assert ridge_upper == Fraction(353, 500)
assert ridge_upper**2 < Fraction(1, 2)

# Heavy-window failure produces a physical original-coordinate row certificate.
energy_floor = Fraction(1, 32 * 39**2)
assert energy_floor == Fraction(1, 48672)
assert energy_floor == 2 * Fraction(1, 312)**2

ridge_exact = 1/sqrt(7) + 32*sqrt(6)/241
C = 9*sqrt(3*e)/(2*float(sigma))
a = 1/sqrt(2) - 1/sqrt(7)
tau_star = float(delta) * a/(sqrt(6)+a)
partner_pivot_C = 2*sqrt(C*312)

print('QFORM_B12_WINDOW_CHECK_PASS')
print(f'sigma={sigma}={float(sigma):.17g}')
print(f'ridge_sqrt_exact={ridge_exact:.17g}')
print(f'ridge_leverage_exact={ridge_exact**2:.17g}')
print(f'rational_ridge_upper={ridge_upper} square={float(ridge_upper**2):.17g}')
print(f'C_window={C:.17g}')
print(f'tau_star={tau_star:.17g} reciprocal={1/tau_star:.17g}')
print(f'cutoff_gain={(Fraction(1,39)/Fraction(1,64))}={64/39:.17g}')
print(f'heavy_row_energy_floor={energy_floor}={float(energy_floor):.17g}')
print(f'partner_pivot_corollary_C_if_abs_a_ge_1_over_312_and_L_1={partner_pivot_C:.17g}')
