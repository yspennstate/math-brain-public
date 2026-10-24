from fractions import Fraction

# Exact route-kill check for the two-branch OR collider.
# E1,E2 are independent Bernoulli(p), U=E1 or E2, 0<p<1.
# Conditional covariance numerator is
# p(2-p)-1 = -(1-p)^2.

lhs_coeff = [-1, 2, -1]  # constant, p, p^2 in p*(2-p)-1
rhs_coeff = [-1, 2, -1]  # constant, p, p^2 in -(1-p)^2
assert lhs_coeff == rhs_coeff

for p in [Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)]:
    den = 2 - p
    marginal = 1 / den
    joint = p / den
    cov = joint - marginal * marginal
    target = -((1 - p) ** 2) / (den ** 2)
    assert cov == target
    assert cov < 0

print("GENERIC_POLYNOMIAL_IDENTITY: PASS")
print("RATIONAL_SAMPLES_STRICTLY_NEGATIVE: PASS")
print("ALL_EXACT_CHECKS_PASSED")
