from fractions import Fraction
from math import e, pi, sqrt

# Exact family parameters for the named-partner application.
m = 16
eps = Fraction(1, 64)
mu = Fraction(1, m)
r = 3
alpha = (1.0 - sqrt(r * float(mu))) / 2.0
sigma = alpha - float(eps)
kappa = (sqrt(float(mu) / alpha) + sqrt(6.0) * float(eps) / sigma) ** 2
partner_bound = (9.0 / 2.0) * sqrt(3.0 * e) / sigma

# Two-coordinate definite principal block in G_1 for A_eps.
local_det = eps * (eps + Fraction(2, 1) * (1 - eps) / m)
local_bound = pi / sqrt(float(local_det))

# Universal obstruction constant for the previous approximate-block criterion.
cross_fraction = sqrt(2.0) / 3.0
rho_fraction_upper = 0.5 - cross_fraction
ridge_term_lower = sqrt(6.0) * cross_fraction / rho_fraction_upper
ridge_square_lower = ridge_term_lower ** 2

assert mu == Fraction(1, 16)
assert local_det == Fraction(71, 32768)
assert sigma > 0
assert kappa < 0.5
assert 18.0 / 7.0 > 2.0
assert partner_bound < 48.0
assert ridge_square_lower > 0.5

print(f"m={m}")
print(f"selected_row_leverage={float(mu):.15f}")
print(f"epsilon={float(eps):.15f}")
print(f"alpha={alpha:.15f}")
print(f"sigma={sigma:.15f}")
print(f"kappa={kappa:.15f}")
print(f"partner_density_bound={partner_bound:.15f}")
print(f"local_principal_det={local_det.numerator}/{local_det.denominator}")
print(f"local_principal_bound={local_bound:.15f}")
print(f"cross_fraction_lower={cross_fraction:.15f}")
print(f"rho_fraction_upper={rho_fraction_upper:.15f}")
print(f"ridge_term_lower={ridge_term_lower:.15f}")
print(f"ridge_square_lower={ridge_square_lower:.15f}")
print("QFORM_B08_EXTRACTION_NOGO_CHECK_PASS")
