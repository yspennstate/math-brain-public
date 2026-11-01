#!/usr/bin/env python3
"""Arithmetic check for fleet03/B15 arity-5 uniform-bias tube theorem.

The proof inputs are source-bound theorems/diagnostics:
  * all 5-input Boolean gates at uniform bias satisfy D_{Gamma_.01} >= 0;
  * for the h96 base candidate, 0 <= Gamma_0 and
      G(x)-4.9096 x <= 8.62812, |G'(x)| < 31;
  * current scalar lift a = 0.268204856.
This script checks only the conservative scalar inequalities used in the proof.
"""
from math import e, log2, sqrt

EPS = 1e-7
A = 0.268204856
C_DAG = 6.521851214
CENTER_PEER_LIFT = 0.01

# Integer-lattice center reserve for every 5-bit nonconstant nondictator.
center_reserve = (A - CENTER_PEER_LIFT) / 1024.0

# If ||p-1/2||_inf <= EPS and the uniform output has m in {1,...,31},
# the smaller output bias is > 1/64, hence x=log2(1/u)<6.
Gmax = 4.9096 * 6.0 + 8.62812
Gdag_max = Gmax + A
Gdag_prime_max = 31.0 + A * 0.7 / 2.0  # ln2 < 0.7, u<=1/2
Gamma_lip = Gdag_max + 1.5 * Gdag_prime_max  # 1/ln2 < 3/2
assert Gamma_lip < 85.0
L = 85.0

# Input price A_i = Gamma(p_i)+h_2(V_{p_i}) stays below 8 in the tube.
assert C_DAG + L * EPS + 1.0 < 8.0
Amax = 8.0

# h_2(x) <= x log2(e/x).
xin = 4.0 * EPS * EPS
hin = xin * log2(e / xin)
assert hin < 2e-12

# Product-measure TV gives |alpha_i(p)-alpha_i(1/2)|<=4 EPS,
# |p_out(p)-p_out(1/2)|<=5 EPS.
price_weight_cost = 5.0 * (4.0 * EPS) * Amax
price_value_cost = 5.0 * (L * EPS + hin)
output_potential_cost = 5.0 * L * EPS

# Biased Fourier coefficient map is an orthogonal 5-fold rotation.
# ||w(p)-w(u)||_1 <= 40/sqrt(3) EPS, so TV <= 20/sqrt(3) EPS < 12 EPS.
tau = 12.0 * EPS
assert 20.0 / sqrt(3.0) * EPS < tau
# Fannes-Audenaert on 32 atoms, with log2 31 < 5.
entropy_cost = tau * (log2(e / tau) + 5.0)
assert entropy_cost < 3.2e-5

total_cost = price_weight_cost + price_value_cost + output_potential_cost + entropy_cost
slack = center_reserve - total_cost
assert total_cost < 1.324e-4
assert slack > 1.198e-4

# For positive denominator W, W <= (sum_i It_i)/4 <= 5/4.
margin_upper = A - slack / 1.25
assert margin_upper < 0.26811

print("PASS")
print("epsilon", EPS)
print("center_reserve", format(center_reserve, ".16g"))
print("Gmax_x_le_6", format(Gmax, ".16g"))
print("Gamma_lipschitz_bound_computed", format(Gamma_lip, ".16g"))
print("Gamma_lipschitz_used", L)
print("price_weight_cost", format(price_weight_cost, ".16g"))
print("price_value_cost", format(price_value_cost, ".16g"))
print("output_potential_cost", format(output_potential_cost, ".16g"))
print("spectral_entropy_cost", format(entropy_cost, ".16g"))
print("total_variation_cost", format(total_cost, ".16g"))
print("defect_lower_bound", format(slack, ".16g"))
print("cG_upper_if_denominator_positive", format(margin_upper, ".16g"))
print("conclusion", "all 5-input nonconstant nondictators in the l_inf bias tube satisfy D_Gamma_dagger>0; constants/dictators are exact base cases")
