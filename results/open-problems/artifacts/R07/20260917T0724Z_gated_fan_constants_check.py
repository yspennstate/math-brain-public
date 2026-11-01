#!/usr/bin/env python3
"""Exact-arithmetic self-check for R07 I0077 gated disconnected fan constants.

This certifies only the finite/rational inequalities used in the explicit example.
The probabilistic/analytic theorem is proved in the immutable run report.
"""
from fractions import Fraction

eta = Fraction(1, 16)
a = Fraction(1, 4)
c = a + 2 * eta
tau = Fraction(1, 2)
period = Fraction(1, 1)

# For c=3/8,
# lambda_c >= (8*pi^2/9) exp(-9/128).
# Use pi^2 > 9 and exp(-x) > 1-x for x>0.
x = Fraction(9, 128)
exp_lb = 1 - x
lambda_lb = Fraction(8, 9) * 9 * exp_lb
kappa_lb = tau * lambda_lb / period

# Explicit subcritical reference interval (0,3): with f(x)=x(3-x),
# Q(f)<1 follows once I0=int_0^3 exp(-x^2/2)dx > 12/11.
# Taylor's formula gives exp(-z) >= 1-z+z^2/2-z^3/6 for z>=0.
# Integrate with z=x^2/2 on [0,8/5].
r = Fraction(8, 5)
I_lb = r - r**3 / 6 + r**5 / 40 - r**7 / 336
I_gap = I_lb - Fraction(12, 11)

outer_total = Fraction(1, 4)
transition_total = Fraction(1, 4)
gate_total = Fraction(1, 2)

assert c == Fraction(3, 8)
assert exp_lb == Fraction(119, 128)
assert lambda_lb == Fraction(119, 16)
assert kappa_lb == Fraction(119, 32)
assert kappa_lb > 1
assert outer_total + transition_total + gate_total == 1
assert I_lb == Fraction(601336, 546875)
assert I_gap == Fraction(52196, 6015625)
assert I_gap > 0

print("PASS")
print("eta =", eta)
print("a =", a)
print("twice_padded_gate_radius_c =", c)
print("exp_lower = 1-9/128 =", exp_lb)
print("lambda_c_lower >", lambda_lb)
print("kappa_lower >", kappa_lb)
print("phase_lengths outer/transitions/gate =", outer_total, transition_total, gate_total)
print("I0_trial_lower =", I_lb)
print("I0_trial_lower - 12/11 =", I_gap)
