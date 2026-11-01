from fractions import Fraction
from math import sqrt

R2 = Fraction(4031,4096)
mu = Fraction(1,256) / R2
D = Fraction(15,4096)
kappa = Fraction(3,64)
pairC = 8*sqrt(5)*float(D*kappa)**(-0.25)
theta = Fraction(1,120)
upper = theta + mu
bank_ratio = mu/theta
bank_sigma = sqrt(float(R2*theta))

print('R2_lower=', float(R2))
print('mu=', float(mu), 'mu<1/251=', mu < Fraction(1,251))
print('pair_constant=', pairC, 'pair<157=', pairC < 157)
print('large_diagonal_constant=', 128/sqrt(1/64))
print('theta+mu=', float(upper), '<1/80=', upper < Fraction(1,80))
print('bank_atom_ratio=', float(bank_ratio), '<1/2=', bank_ratio < Fraction(1,2))
print('bank_sigma_lower=', bank_sigma)
assert R2 == Fraction(4031,4096)
assert mu == Fraction(16,4031)
assert mu < Fraction(1,251)
assert pairC < 157
assert upper < Fraction(1,80)
assert bank_ratio < Fraction(1,2)
assert bank_sigma > 0.09
print('STATUS=PASS')
