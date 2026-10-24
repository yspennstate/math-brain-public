from fractions import Fraction
from math import e, sqrt

# Section 5 constant.
C_two = 4.0 * sqrt((9.0 / 2.0) * sqrt(3.0 * e))
assert C_two < 14.34

# Section 6 diffuse residual parameters.
mu = Fraction(1, 32)
alpha = Fraction(3, 8)
eta = Fraction(1, 64)
sigma = alpha - eta
assert sigma == Fraction(23, 64)
assert mu / alpha == Fraction(1, 12)

# Rational certificates for the ridge-leverage perturbation.
assert sqrt(1.0 / 12.0) < 29.0 / 100.0
assert sqrt(6.0) / 23.0 < 107.0 / 1000.0
ridge_sqrt_cap = Fraction(29, 100) + Fraction(107, 1000)
assert ridge_sqrt_cap == Fraction(397, 1000)
assert ridge_sqrt_cap * ridge_sqrt_cap < Fraction(1, 2)

# Numerical actual bound at |a|=1/312, sigma=23/64.
a = 1.0 / 312.0
sig = 23.0 / 64.0
actual_bound = C_two / sqrt(a * sig)
assert actual_bound < 423.0

# Safe coarse rational bound using e<3:
# C_two^2 = 72 sqrt(3e) < 216.
coarse_sq = Fraction(216 * 19968, 23)
assert coarse_sq < 434 * 434

# Account04/B18 application constant in (6.10).
C_partner = 3.0 * sqrt(2.0) * (3.0 * e) ** 0.25
assert C_partner < 7.17

# Optimizer c=1/sqrt(6) of f(c)=c(1-2c^2) on (0,1/sqrt(2)).
c = 1.0 / sqrt(6.0)
derivative = 1.0 - 6.0 * c * c
second_derivative = -12.0 * c
assert abs(derivative) < 1e-14
assert second_derivative < 0

print(f"C_two={C_two:.15f}")
print(f"sigma={float(sigma):.15f}")
print(f"ridge_sqrt_cap={float(ridge_sqrt_cap):.15f}")
print(f"ridge_cap={float(ridge_sqrt_cap * ridge_sqrt_cap):.15f}")
print(f"actual_bound_at_a_1over312={actual_bound:.15f}")
print(f"coarse_bound={sqrt(float(coarse_sq)):.15f}")
print(f"account04_partner_constant={C_partner:.15f}")
print(f"optimizer_c={c:.15f}")
print("ALL_CHECKS_PASS")
