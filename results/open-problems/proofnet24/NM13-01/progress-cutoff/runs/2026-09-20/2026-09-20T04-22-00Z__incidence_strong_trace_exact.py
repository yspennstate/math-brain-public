from fractions import Fraction
import math


def parameters(d):
    e = 2 * (d - 1)                     # degree of L(G)
    D = d + e + d * e                   # degree of G boxtimes L(G)
    aG = Fraction(d * (e + 1), D)       # marginal base jump rate
    aL = Fraction(e * (d + 1), D)       # marginal line jump rate
    b = Fraction(d, 2 * (d - 1))        # visible line/base time factor
    base_center = Fraction(d, d - 2)
    line_center = Fraction(2 * (d - 1), d - 2)
    output_center = line_center / aL
    predicted = Fraction(D, (d - 2) * (d + 1))
    assert output_center == predicted
    # At the output cutoff time the base marginal is macroscopically past
    # its own entropic center.
    assert aG * output_center > base_center
    # Tensorized Dirichlet lower bound.
    gap_coeff = Fraction(d, D)
    assert Fraction(e, D) * b == gap_coeff
    return d, e, D, aG, aL, b, base_center, line_center, output_center, gap_coeff


print("GENERAL_PARAMETER_CHECKS")
for d in range(3, 10):
    vals = parameters(d)
    print(
        "d=%d e=%d D=%d aG=%s aL=%s b=%s base=%s line=%s output=%s gapcoef=%s"
        % vals
    )

# The explicit obstruction calculation uses d=6, hence e=10 and D=76.
d = 6
e = 2 * (d - 1)
D = d + e + d * e
assert (e, D) == (10, 76)

# Visible line-graph eigenvalues are mu=(3 lambda+2)/5. Their average is
# 2/5 because the normalized base adjacency has trace zero. Since mu<=1,
# at least 1/25 of the visible eigenvalues satisfy mu>=3/8.
avg_mu = Fraction(2, 5)
mu_threshold = Fraction(3, 8)
mass_fraction = (avg_mu - mu_threshold) / (1 - mu_threshold)
assert mass_fraction == Fraction(1, 25)

# Pairing the constant base eigenvector with such a line eigenvector in the
# strong product gives theta >= (6+70*(3/8))/76 = 129/304.
theta0 = Fraction(d + e * (d + 1) * mu_threshold, D)
assert theta0 == Fraction(129, 304)

# For a 76-regular graph the NBRW polynomial recurrence has characteristic
# roots z^2 -(76/75) theta z + 1/75=0. At theta0,
# z_+=(129+sqrt(11841))/600 > 79/200 because sqrt(11841)>108.
disc = Fraction(D * D) * theta0 * theta0 - 4 * (D - 1)
assert disc == Fraction(11841, 16)
assert 11841 > 108 ** 2
z_lower = Fraction(79, 200)

# The lower root bound is strong enough to beat the square-root state-count
# penalty at the entropic radius: 75*z_lower^4 > 1 is exact.
cert = Fraction(75) * z_lower ** 4
assert cert == Fraction(116850243, 64000000)
assert cert > 1

kappa = 0.5 + 2 * math.log(float(z_lower), 75)
assert kappa > 0

print("\nD6_TRACE_OBSTRUCTION")
print("e=", e)
print("D=", D)
print("mass_fraction_mu_ge_3/8=", mass_fraction)
print("theta0=", theta0, float(theta0))
print("discriminant_at_theta0=", disc, float(disc))
print("zplus_lower_bound=", z_lower, float(z_lower))
print("75*zlower^4=", cert, float(cert))
print("polynomial_trace_exponent_kappa=", "%.15f" % kappa)
print("ALL_EXACT_ALGEBRA_CHECKS_PASS")
