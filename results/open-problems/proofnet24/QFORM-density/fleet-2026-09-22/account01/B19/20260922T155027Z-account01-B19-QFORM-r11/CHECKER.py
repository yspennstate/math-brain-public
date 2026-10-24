from fractions import Fraction
import math

# Exact constants inherited from the source-pinned Schur splice.
delta0 = Fraction(9, 280)
sigma0 = Fraction(3, 8) * delta0
m = Fraction(7, 8)
assert sigma0 == Fraction(27, 2240)

# Bathtub calculation: for density cap K0 and alpha <= 1/(2K0),
# integral min(1,alpha/|x|) g(x) dx <= 2K0 alpha(1+log(1/(2K0 alpha))).
# Here K0=sqrt(e), alpha=2sqrt(e)r/sigma, hence r0=sigma/(4e).
r0 = float(sigma0) / (4.0 * math.e)

# Quarter-moment bound uses sqrt(1+u) <= 1+sqrt(u):
# int_0^infty exp(-u/4) du = 4,
# int_0^infty exp(-u/4) sqrt(u) du = 4 sqrt(pi).
J_bound = 4.0 + 4.0 * math.sqrt(math.pi)
quarter_factor = 1.0 + J_bound / 4.0
assert abs(quarter_factor - (2.0 + math.sqrt(math.pi))) < 1e-14

# Final one-effective contaminated branch constant.
C = 2.0 * (2.0 + math.sqrt(math.pi)) * (
    (4.0 * math.e) / (float(m) ** 3 * float(sigma0))
) ** 0.25
assert C < 46.0

# Elementary inequality used in the integral estimate.
for j in range(100001):
    u = j / 1000.0
    assert math.sqrt(1.0 + u) <= 1.0 + math.sqrt(u) + 1e-15

print('QFORM_CROSSBANK_SPLICE_CHECK_PASS')
print('delta0 =', delta0, float(delta0))
print('sigma0 =', sigma0, float(sigma0))
print('m =', m, float(m))
print('r0 =', repr(r0))
print('quarter_factor =', repr(quarter_factor))
print('final_constant =', repr(C))
