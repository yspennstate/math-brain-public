from fractions import Fraction
from math import e, sqrt

c = Fraction(3969, 16384)
assert c == Fraction(63*63, 128*128)

# Distinct-draw D5 lower-bound constants.
assert 120 * 64**4 == 2013265920
C5 = 5*sqrt(2*e)*(120*64**4)**0.1/float(c)**0.5
Ctail = 36*sqrt(3)*e/float(c)**0.5
CD3 = 9*sqrt(3*e)*(58982400)**(1/6)/float(c)**0.5

assert C5 < 201.787
assert Ctail < 344.372
assert CD3 < 1030.245
assert abs(Ctail - (512/7)*sqrt(3)*e) < 1e-12

anchored = c**3 / 176947200
nested = anchored / 4
matching = nested / 36
assert nested == c**3 / 707788800
assert matching == c**3 / 25480396800

print('QFORM_B20_LEVERAGEFREE_CROSSCUT_CHECK_PASS')
print('c_star =', float(c), c)
print('D5 bound =', C5)
print('collective-tail bound =', Ctail)
print('Dprime bound =', CD3)
print('nested mass floor =', float(nested), nested)
print('matching-product floor =', float(matching), matching)
