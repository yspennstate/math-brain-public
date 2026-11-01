#!/usr/bin/env python3
"""Deterministic arithmetic checks for the B01 Fejer report constants."""

from math import pi, sin, sqrt, log

s0 = (sin(0.5) / 0.5) ** 2
assert 0.91 < s0 < 0.93

# Integral_{-T}^T (1-|t|/T)^2 dt = 2T/3, checked at T=7.
T = 7.0
tri_sq = 2.0 * (T - T + T / 3.0)
assert abs(tri_sq - 2.0 * T / 3.0) < 1e-14

# The dyadic concentration-to-Fejer constant in the report's optional
# one-coordinate comparison is finite and scale-free.
fejer_sqrt_constant = (sqrt(2.0) + 8.0 / (1.0 - 2.0 ** (-1.5))) / pi
assert 4.38 < fejer_sqrt_constant < 4.40

# Partner-transfer formula (4.2) at a representative admissible scale.
a = 1.0
ell = 0.25
rhs = (1.0 / s0) * sqrt(
    ell / (3.0 * a) * (8.0 + 4.0 * pi * (1.0 + log(4.0 * a / ell)))
)
assert rhs > 0.0

print(f"s0={s0:.15f}")
print(f"triangular_L2_at_T7={tri_sq:.15f}")
print(f"fejer_sqrt_constant={fejer_sqrt_constant:.15f}")
print(f"partner_interval_rhs_a1_ell025={rhs:.15f}")
print("STATUS=PASS")
