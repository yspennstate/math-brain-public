from math import sqrt, pi, e
from fractions import Fraction

sigma2 = Fraction(1, 12)
ceiling = 1.0 / (2.0 * sqrt(2.0) * float(sigma2))
assert abs(ceiling - 3.0 * sqrt(2.0)) < 1e-14

same_sign = 1.0 / (sqrt(2.0 * pi * e) * float(sigma2))
assert same_sign < ceiling

partner_c = Fraction(5295, 21952)
assert partner_c > 0

# Algebraic check of the mixed-sign upper bound reduction.
# For alpha >= beta > 0, gamma > 0:
# A-b = 1/(2 alpha)+1/(2 gamma), and
# 2 alpha beta gamma (A-b) = beta(alpha+gamma).
def mixed_bound(alpha, beta, gamma):
    assert alpha >= beta > 0 and gamma > 0
    A_minus_b = 1.0/(2.0*alpha) + 1.0/(2.0*gamma)
    left = 2.0*alpha*beta*gamma*A_minus_b
    right = beta*(alpha+gamma)
    assert abs(left-right) <= 1e-12*max(1.0, abs(right))
    return 1.0/(2.0*sqrt(right))

for triple in [(1.0,1.0,1.0),(2.0,1.0,1.0),(10.0,1.0,1.0),(3.0,2.0,4.0)]:
    a,b,g = triple
    assert mixed_bound(a,b,g) <= 1.0/(2.0*sqrt(2.0)) + 1e-15

print('gaussian_ceiling_sigma2_1_12 =', ceiling)
print('same_sign_ceiling_sigma2_1_12 =', same_sign)
print('partner_first_correction =', float(partner_c))
print('PASS')
