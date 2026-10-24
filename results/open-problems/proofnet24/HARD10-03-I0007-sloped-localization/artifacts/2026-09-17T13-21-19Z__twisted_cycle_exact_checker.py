#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

# Exact finite self-check for the C4 winding-sector diagnostic used in the
# I0007 terminal handoff report. No floating point arithmetic is used.
#
# Model: oriented 4-cycle, integer edge increments n_1,...,n_4 with
# sum n_i = 2, discrete-Gaussian weight q^(sum n_i^2), q=1/100.
# Observable: h_2=n_1+n_2 with h_0 pinned to zero.

q = Fraction(1, 100)

# Balanced ground states in the winding-2 sector: exactly two 1s and two 0s.
ground = [ns for ns in product(range(2), repeat=4) if sum(ns) == 2]
assert len(ground) == 6
extreme = [ns for ns in ground if (ns[0] + ns[1] - 1) ** 2 == 1]
assert len(extreme) == 2

# From coefficient domination at t=q^{-1}:
# Z_2 <= 16 q^2/(1-q^2)^4, while the variance numerator is >=2q^2.
variance_lower_bound = (1 - q*q) ** 4 / 8

# Rigorous upper bound on the untwisted van-Engelenburg--Lis constant
# C_beta = sup_theta |U''(theta)| for
# w(theta)=sum_n q^(n^2)e^{in theta}, U=-log w.
# We use q^(n^2)<=q^n for n>=1.
w_lower = (1 - 3*q) / (1 - q)
S1 = q / (1 - q) ** 2
S2 = q * (1 + q) / (1 - q) ** 3
C_beta_upper_bound = 2*S2/w_lower + 4*S1*S1/(w_lower*w_lower)
assert w_lower > 0
assert variance_lower_bound > C_beta_upper_bound

# Opposite-vertex effective resistance of the unit-conductance C4 is 1:
# two length-2 paths in parallel.
effective_resistance = Fraction(1, 1)
assert variance_lower_bound > C_beta_upper_bound * effective_resistance

print('q =', q)
print('ground_count =', len(ground))
print('variance_contributing_ground_states =', len(extreme))
print('variance_lower_bound =', variance_lower_bound)
print('C_beta_upper_bound =', C_beta_upper_bound)
print('effective_resistance_C4_opposite =', effective_resistance)
print('gap_lower_minus_Cupper =', variance_lower_bound - C_beta_upper_bound)
print('ratio_lower_over_Cupper =', variance_lower_bound / C_beta_upper_bound)
print('ALL_EXACT_CHECKS_PASS')
