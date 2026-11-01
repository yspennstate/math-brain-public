from fractions import Fraction
from math import sqrt, e

tau = Fraction(1, 2**20)
rho_star = Fraction(63, 16384) * (1 - tau)**2
Delta = Fraction(3, 8) * rho_star
kappa0 = sqrt(Fraction(1288, 3))
theta = Fraction(1, 64)
Z = float(Delta**3 * theta) / kappa0
D3 = 6 * sqrt(e) * Z**(-1/6)
Dp = 9 * sqrt(3) * e / 2 * Z**(-1/6)

print(f"rho_star={float(rho_star):.18g}")
print(f"Delta_star={float(Delta):.18g}")
print(f"kappa0={kappa0:.18g}")
print(f"Z_right_min={Z:.18g}")
print(f"D3_bound={D3:.18g}")
print(f"Dprime_partner_bound={Dp:.18g}")
print(f"half_Z={Z/2:.18g}")
print(f"two_thirds_Z={2*Z/3:.18g}")
print(f"common_plane_N2_product_min={(1-float(theta))*float(Delta):.18g}")
print(f"projection_F_distance_max={sqrt(2*float(theta)):.18g}")

assert D3 < 863.481
assert Dp < 1849.361
assert Z > 2.2608e-12
assert (1-float(theta))*float(Delta) > 0.0014194
print("QFORM_B19_RIGHTPLANE_CHECK_PASS")
