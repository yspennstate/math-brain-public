from fractions import Fraction
from math import sqrt, pi, e

# Exact spectral-window constants.
eps = Fraction(1, 72)
eta = Fraction(1, 19)
delta = Fraction(23, 72)
sigma = delta - eta
assert sigma == Fraction(365, 1368)
assert eps / delta == Fraction(1, 23)

# Fully rational certificate for ridge leverage < 1/2.
# 1/sqrt(23) < 21/100 and sqrt(6) < 49/20.
upper = Fraction(21, 100) + Fraction(882, 1825)
assert upper == Fraction(5061, 7300)
assert 2 * 5061**2 < 7300**2

ridge = (1 / sqrt(23) + 72 * sqrt(6) / 365) ** 2
assert ridge < 0.5

C_window = 9 * sqrt(3 * e) / (2 * float(sigma))
L1_window = 2 * pi * C_window

# Strong physical hub threshold: if window leverage fails, one row piece exceeds 1/228.
assert Fraction(2, 228**2) == Fraction(1, 19**2 * 72)

# Live r45 full-cut constants.
kappa = Fraction(247, 576)
a0 = Fraction(1, 228)
delta0 = a0 / 2
zA = kappa * delta0**2
zB = zA / 64
assert zA == Fraction(247, 119771136)
assert zB == Fraction(247, 7665352704)

C3 = 10.345083232147514
density_A = C3 * float(zA) ** (-1 / 6)
density_B = C3 * float(zB) ** (-1 / 6)
L1_A = 2 * pi * density_A
L1_B = 2 * pi * density_B
carrier = float(a0) / sqrt(2)

# Designated fleet04/B02 L2 hybrid constant from the completed compiler.
hybrid_prefactor = 2 ** (8 / 3) * 3 ** (1 / 4) * e ** (1 / 4)
hybrid_A = hybrid_prefactor * float(zA) ** (-1 / 8)
hybrid_B = hybrid_prefactor * float(zB) ** (-1 / 8)

print({
    "sigma": float(sigma),
    "ridge_leverage_upper_actual": ridge,
    "ridge_leverage_upper_rational_certificate": float(upper**2),
    "window_density_constant": C_window,
    "window_L1_constant": L1_window,
    "physical_hub_threshold": float(a0),
    "zA": float(zA),
    "zB": float(zB),
    "density_A": density_A,
    "density_B": density_B,
    "L1_A": L1_A,
    "L1_B": L1_B,
    "carrier_aligned_threshold": carrier,
    "partner_hybrid_A_coefficient": hybrid_A,
    "partner_hybrid_B_coefficient": hybrid_B,
})
