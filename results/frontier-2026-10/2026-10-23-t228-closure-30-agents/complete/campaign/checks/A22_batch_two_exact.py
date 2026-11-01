"""Exact rational certificates for the A22 batch-two T228 author proof.

No floating point integration or simulation is used. The probability
arguments and the identities involving the exponential distribution are
proved in campaign/proofs/T228_BATCH_TWO.md.
"""

from fractions import Fraction as F
from math import factorial


delta = F(1, 1000)
eta_min = F(11, 10)
eta_max = F(6, 5)
mixed_label = 3 + 2 * delta
perturbation = 4 * delta + 3 * delta**2 + 2 * delta * mixed_label
series = sum(((F(5, 6) ** k) / factorial(k) for k in range(5)), F(0))
series_margin = series - F(25, 11)
derivative_lower = -1 + 2 * F(1, 3) * F(11, 6)
h1_upper = 1 - eta_max + 2 * eta_max * F(11, 25)
q2 = h1_upper + eta_max * perturbation
margin = 1 - q2
h2_minimum = 1 - 2 * eta_min + 2 * eta_min**2
sd_min_squared = eta_min**2 / 2
sd_max_squared = 2 * eta_max**2 * (1 + delta) ** 2
mean_coefficient = 4 * eta_max

assert mixed_label == F(1501, 500)
assert perturbation == F(10007, 10**6)
assert series == F(71449, 31104)
assert series_margin == F(8339, 342144) > 0
assert derivative_lower == F(2, 9) > 0
assert h1_upper == F(107, 125) < 1
assert q2 == F(2170021, 2500000) < F(87, 100) < 1
assert margin == F(329979, 2500000) > 0
assert h2_minimum == F(61, 50) > 1
assert sd_min_squared == F(121, 200)
assert sd_max_squared == F(9018009, 3125000)
assert mean_coefficient == F(24, 5)

certificates = {
    "mixed_label_bound": mixed_label,
    "derivative_perturbation": perturbation,
    "exp_5_over_6_taylor_lower": series,
    "taylor_margin_above_25_over_11": series_margin,
    "h1_eta_derivative_strict_lower": derivative_lower,
    "uniform_h1_strict_upper": h1_upper,
    "uniform_contraction_q2": q2,
    "contraction_margin": margin,
    "minimum_h2": h2_minimum,
    "minorization_sd_min_squared": sd_min_squared,
    "minorization_sd_max_squared": sd_max_squared,
    "minorization_mean_coefficient": mean_coefficient,
}

for name, value in certificates.items():
    print(f"{name}: {value}")
print("PASS: all exact rational certificate checks.")
