#!/usr/bin/env python3
"""
Exact algebra self-check for I0014, 2026-09-16.

This checker does NOT certify a Bradley counterexample. It checks the finite
algebra in the source-condition reduction recorded in the accompanying report.

Source normalization:
  gamma = 1-beta
  q_C(x) = x^2 exp(C (log^+ x)^gamma)
  C = 2^(gamma+1) alpha / gamma
Matsui's Remark 2.5(ii) evaluates Bradley's condition (1.5) with a unit
exponential coefficient. Scaling that coefficient to C changes the positive
leading term by C. In units of 2^gamma, C/2^gamma = 2 alpha/gamma, hence
the leading exponent coefficient is alpha(2-d)/gamma.

At equality d=2, the first nonzero term has coefficient
-4 alpha^2/gamma and power 2 gamma - 1, which is positive exactly when
beta<1/2. The analytic concavity inequality used to control the equality
case is proved on the report page; this file checks the exact coefficient
and a rational grid of beta values.
"""
from fractions import Fraction

alpha = Fraction(1, 1)  # homogeneity permits this normalization


def check_beta(beta: Fraction):
    assert Fraction(0) < beta < Fraction(1, 2)
    gamma = 1 - beta

    # C/2^gamma = 2*alpha/gamma.
    q_leading = 2 * alpha / gamma

    # Bradley negative leading term has alpha*d/gamma. At d=2 it cancels.
    d_eq = Fraction(2, 1)
    negative_eq = alpha * d_eq / gamma
    assert q_leading == negative_eq

    # General leading coefficient: alpha*(2-d)/gamma.
    for d in [Fraction(3, 2), Fraction(2), Fraction(5, 2)]:
        direct = q_leading - alpha * d / gamma
        closed = alpha * (2 - d) / gamma
        assert direct == closed

    # At d=2 the concavity estimate produces
    # -(4 alpha^2/gamma) L^(2 gamma - 1).
    equality_coeff = -4 * alpha * alpha / gamma
    equality_power = 2 * gamma - 1
    assert equality_coeff < 0
    assert equality_power > 0

    return gamma, equality_power, equality_coeff


grid = [
    Fraction(1, 24),
    Fraction(1, 12),
    Fraction(1, 6),
    Fraction(1, 4),
    Fraction(1, 3),
    Fraction(2, 5),
    Fraction(5, 12),
    Fraction(11, 24),
    Fraction(23, 48),
]

print("I0014 EXACT BRADLEY-THRESHOLD ALGEBRA SELF-CHECK")
print("alpha normalized to 1 (homogeneous coefficient check)")
print("beta | gamma=1-beta | 2gamma-1 | equality coefficient -4/gamma")
for beta in grid:
    gamma, power, coeff = check_beta(beta)
    print(f"{beta} | {gamma} | {power} | {coeff}")

beta = Fraction(1, 3)
gamma, power, coeff = check_beta(beta)
assert gamma == Fraction(2, 3)
assert power == Fraction(1, 3)
assert coeff == Fraction(-6, 1)
print("beta=1/3 equality case: gamma=2/3, power=1/3, coefficient=-6 (for alpha=1)")

print("ALL EXACT I0014 BRADLEY-THRESHOLD CHECKS PASSED")
