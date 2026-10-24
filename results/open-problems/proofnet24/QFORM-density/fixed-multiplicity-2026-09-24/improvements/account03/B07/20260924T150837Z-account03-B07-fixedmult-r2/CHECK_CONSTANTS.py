from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec = 50

eta = Fraction(1, 100)
a2 = eta + eta*eta
minor_abs_max = 2*a2
minor_sq_max = minor_abs_max**2
assert a2 == Fraction(101, 10000)
assert minor_abs_max == Fraction(101, 5000)
assert minor_sq_max == Fraction(10201, 25000000)

# Coarse exact lower bound used in the proof:
# sqrt(2)<3/2 and sqrt(202)<15 imply delta_*>6779/8000>4/5.
delta_lower = Fraction(6779, 8000)
assert delta_lower > Fraction(4, 5)
g_lower = Fraction(1, 2) * Fraction(4, 5)**2
assert g_lower == Fraction(8, 25)
assert g_lower / 3 > minor_sq_max

# Main no-pivot third-volume bound: kappa=1/6400,
# random cut loses 4^3=64 and C3<15.
kappa = Fraction(1, 6400)
# (kappa^3 / 64)^(-1/6) = 160 exactly.
assert Fraction(1,1) / (kappa**3 / 64) == 160**6
assert 15 * 160 == 2400

print('minor_sq_max =', float(minor_sq_max))
print('g_lower/3 =', float(g_lower/3))
print('ratio =', float((g_lower/3)/minor_sq_max))
print('third-volume safe constant = 2400')
print('STATUS=PASS')
