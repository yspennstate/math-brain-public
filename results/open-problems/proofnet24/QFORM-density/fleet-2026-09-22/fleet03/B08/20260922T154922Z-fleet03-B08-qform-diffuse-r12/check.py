from fractions import Fraction
from math import sqrt, e

mu = Fraction(169, 1875)
alpha = Fraction(6, 25)
eta = Fraction(1, 64)
sigma = alpha - eta
ell = mu / alpha
q = Fraction(5, 4)

assert sigma == Fraction(359, 1600)
assert ell == Fraction(169, 450)

# Exact algebra: sqrt(3*mu)=13/25 and hence alpha=(1-13/25)/2=6/25.
assert 3 * mu == Fraction(169, 625)

# kappa = 169/450 + 3750/128881 + 130 sqrt(3)/1077.
# Rigorous upper bound sqrt(3)<7/4.
kappa_upper = Fraction(169, 450) + Fraction(3750, 128881) + Fraction(455, 2154)
assert kappa_upper == Fraction(17859632, 28998225)
assert Fraction(5, 8) - kappa_upper == Fraction(2114069, 231985800)
assert kappa_upper < q / 2

# Effective dimension at gamma=sigma/sqrt(6).
theta_lower = Fraction(18, 7)
assert theta_lower > 2 * q

# q=1 obstruction at the same worst-case corner:
# 13/30 + 25/359 = 1/2 + 16/5385 > 1/2.
assert Fraction(13, 30) + Fraction(25, 359) - Fraction(1, 2) == Fraction(16, 5385)

C = (57600 / 359) * sqrt(12 * e / 5)
print('mu=', float(mu))
print('alpha=', float(alpha))
print('sigma=', float(sigma))
print('ell=', float(ell))
print('kappa_upper=', float(kappa_upper))
print('q/2=', float(q/2))
print('theta_lower=', float(theta_lower))
print('2q=', float(2*q))
print('C=', C)
assert C < 410
print('QFORM_FRACTIONAL_RIDGE_DIFFUSE_CHECK_PASS')
