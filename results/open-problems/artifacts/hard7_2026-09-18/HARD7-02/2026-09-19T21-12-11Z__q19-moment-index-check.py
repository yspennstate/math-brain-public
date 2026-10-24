"""Exact symbolic self-check for HARD7-02 Q1.9 moment-index dichotomy.

This checks only the finite algebra used in the analytic argument.  It is a
self-check, not an independent audit and not a proof of the measure-theoretic
layer-cake step.
"""
import sympy as sp

t, r, alpha = sp.symbols("t r alpha", positive=True)

# For t >= r > 0, the analytic proof uses
#     1/t <= t^(alpha-1)/r^alpha.
# The difference has the exact factorization below, whose numerator is
# nonnegative under t >= r.
lhs_difference = sp.simplify(
    t ** (alpha - 1) / r ** alpha - 1 / t
)
expected_factor = (t ** alpha - r ** alpha) / (r ** alpha * t)
assert sp.simplify(lhs_difference - expected_factor) == 0

# Exact axis-family scale at p=1/4 from the earlier axis classification:
# k_{alpha,p}^alpha = 2(2p-1)/log(p/(1-p)).
p = sp.Rational(1, 4)
k_alpha_power = sp.simplify(2 * (2 * p - 1) / sp.log(p / (1 - p)))
assert sp.simplify(k_alpha_power - 1 / sp.log(3)) == 0

print("HARD7-02 Q1.9 moment-index exact algebra self-check")
print("tail_integrand_difference =", lhs_difference)
print("expected_factor =", expected_factor)
print("factor_identity =", sp.simplify(lhs_difference - expected_factor) == 0)
print("axis_p_1_4_k_alpha_power =", k_alpha_power)
print("axis_scale_identity =", sp.simplify(k_alpha_power - 1 / sp.log(3)) == 0)
print("ALL_EXACT_CHECKS_PASS = True")
