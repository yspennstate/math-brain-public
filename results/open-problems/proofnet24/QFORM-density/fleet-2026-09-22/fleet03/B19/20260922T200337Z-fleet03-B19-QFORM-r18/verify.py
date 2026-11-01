from fractions import Fraction
import math

theta0 = Fraction(256,129)
beta0 = (3*theta0-1)/8
gap = beta0-Fraction(1,2)
assert beta0 == Fraction(213,344)
assert gap == Fraction(41,344)
assert 1/gap == Fraction(344,41)

L1 = math.pi*math.e*math.sqrt(2)
half_const = (426/41)*(2**0.25)*math.sqrt(math.e)
gamma_const = 4*half_const
pair_gamma_const = 16*math.sqrt(2)*(math.e**0.25)*((10/7)**0.25)

assert float(beta0) > 0.5
assert gamma_const < 81.488
assert pair_gamma_const < 31.764

print('theta0 =', float(theta0))
print('beta0 =', beta0, float(beta0))
print('beta0-1/2 =', gap, float(gap))
print('L1 =', L1)
print('hybrid half-Riesz coefficient / sqrt(g) =', half_const)
print('hybrid density coefficient / sqrt(|a0| gamma) =', gamma_const)
print('two-row pair density coefficient / sqrt(|a0| gamma) =', pair_gamma_const)
print('QFORM_B19_R18_HYBRID_CHECK_PASS')
