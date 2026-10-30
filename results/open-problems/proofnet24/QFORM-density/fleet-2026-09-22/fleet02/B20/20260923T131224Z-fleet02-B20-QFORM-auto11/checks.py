from decimal import Decimal, getcontext
from fractions import Fraction
import math

getcontext().prec = 60

# Ridge-window constants.
epsilon = Decimal(1) / Decimal(56)
eta = Decimal(1) / Decimal(14)
delta = Decimal(1)/Decimal(2) - (Decimal(1)/Decimal(28)).sqrt() - Decimal(1)/Decimal(56)
sigma = delta - eta
gamma = Decimal(7)/Decimal(10) * sigma
ridge_sqrt = (epsilon/delta).sqrt() + eta/gamma
one_over_sqrt2 = (Decimal(1)/Decimal(2)).sqrt()
theta = Decimal(300)/Decimal(149)
ratio = theta/(theta-Decimal(2))
assert ridge_sqrt < one_over_sqrt2
assert theta > 2
assert ratio == 150

# Decimal e and final constant. Decimal.exp is available at this precision.
e = Decimal(1).exp()
density_constant = Decimal(150) * e.sqrt() / ((Decimal(2).sqrt()) * gamma)
assert density_constant < Decimal(1127)

# Exact star-energy constant.
star = Fraction(1,840) * Fraction(25,448)**2
assert star == Fraction(125,33718272)

# Stress family exact checks.
assert Fraction(3,256) < Fraction(1,64)
assert Fraction(1,8192) < Fraction(1,64)
assert Fraction(1,700) < Fraction(1,64)
for N in [5, 7, 16, 100, 10000]:
    assert Fraction(7,100*N) < Fraction(1,64)
    # hub-leaf square = 1/(10000 N), total N leaves = 1/10000
    assert N * Fraction(1,10000*N) == Fraction(1,10000)
assert Fraction(1,50) > Fraction(1,56)
assert Fraction(3,256) < Fraction(1,60)

print('delta=', delta)
print('sigma=', sigma)
print('gamma=', gamma)
print('sqrt(max ridge diag) upper=', ridge_sqrt)
print('1/sqrt(2)=', one_over_sqrt2)
print('theta lower=', theta)
print('theta/(theta-2) upper=', ratio)
print('density upper=', density_constant)
print('star exact=', star, 'decimal=', float(star))
print('stress large diagonal=', Fraction(3,256))
print('stress nonzero pair determinant=', Fraction(1,8192))
print('stress annular hub leverage=', Fraction(1,50))
print('stress total hub row energy=', Fraction(1,10000))
print('STATUS=PASS')
