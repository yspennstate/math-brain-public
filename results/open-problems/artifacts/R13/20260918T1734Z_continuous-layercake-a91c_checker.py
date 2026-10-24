from fractions import Fraction

# Exact-arithmetic self-check for the R13 continuous layer-cake sharpening.
# The analytic proof is in the accompanying immutable report.  This script
# checks only the finite rational comparisons used at n=86.

n = 86
D = 133
h = Fraction(148709, 20000)          # 7.43545
old_floor = Fraction(7507, 1000)     # previous R13 row-pruning floor

# Classical rational upper bound pi < 355/113.
pi_up = Fraction(355, 113)

# Rational upper bounds for sqrt(2*pi) and sqrt(133).
s_up = Fraction(250663, 100000)      # 2.50663
r_up = Fraction(57663, 5000)         # 11.5326
assert s_up * s_up > 2 * pi_up
assert r_up * r_up > D

# Strict active-row count: d < n^2/h^2, so d <= ceil(n^2/h^2)-1.
ratio = Fraction(n * n, 1) / (h * h)
assert Fraction(133, 1) < ratio < Fraction(134, 1)
active_dimension_bound = 133

# For Y=S^{-1}, S~chi^2_3, the report proves for t>=1
#   P(X_D >= t) >= [alpha/(1+alpha)] t^{-3/2},
# alpha=(2-1/D)/(3*sqrt(2*pi)*sqrt(D)).
# Replacing both square roots in the denominator by rational upper bounds
# gives a rigorous lower bound alpha0 <= alpha.
alpha0 = (Fraction(2, 1) - Fraction(1, D)) / (3 * s_up * r_up)
beta0 = alpha0 / (2 * (1 + alpha0))

# Hence C_D=3*sqrt(2*pi)*(1-beta_D) is at most this rational quantity.
c_up = 3 * s_up * (1 - beta0)
assert c_up < h
assert h < old_floor

print('R13_CONTINUOUS_LAYERCAKE_EXACT_PASS')
print('n =', n)
print('h =', float(h), h)
print('n^2/h^2 =', float(ratio), ratio)
print('active_dimension_bound =', active_dimension_bound)
print('sqrt(2pi)_upper =', float(s_up), s_up)
print('sqrt(133)_upper =', float(r_up), r_up)
print('alpha_lower =', float(alpha0), alpha0)
print('beta_lower =', float(beta0), beta0)
print('finite_D_constant_upper =', float(c_up), c_up)
print('new_B86_upper =', float(h), h)
print('old_R13_B86_envelope_floor =', float(old_floor), old_floor)
print('strict_bound_improvement_at_86 =', float(old_floor-h), old_floor-h)
