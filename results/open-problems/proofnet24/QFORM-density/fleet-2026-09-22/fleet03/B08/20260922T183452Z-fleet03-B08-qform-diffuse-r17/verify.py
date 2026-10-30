from fractions import Fraction
from math import e, sqrt

tau = Fraction(1,16)
theta0 = Fraction(2,1) / (Fraction(1,1) + 2*tau*tau)
q = Fraction(99,50)
s = Fraction(999,500)
beta = theta0 / (2*q)
beta_s = beta*s
ratio = beta_s/(beta_s-1)
gate = q/2

assert theta0 == Fraction(256,129)
assert gate == Fraction(99,100)
assert beta == Fraction(6400,12771)
assert beta_s == Fraction(2368,2365)
assert beta_s > 1
assert ratio == Fraction(2368,3)

pair_reserve = gate * (theta0 - 1)
assert pair_reserve == Fraction(4191,4300)
actual_minor_coeff = pair_reserve * tau**4
assert actual_minor_coeff == Fraction(4191,281804800)

C99 = (1000**(500/999) + 1) * sqrt((189440/3) * sqrt(e/99))
assert C99 < 3349

assert Fraction(99,100) > Fraction(5,6)
assert tau < Fraction(1,4)

print('theta0 =', theta0, float(theta0))
print('q =', q, float(q))
print('row leverage gate q/2 =', gate, float(gate))
print('beta =', beta, float(beta))
print('s =', s, float(s))
print('beta*s =', beta_s, float(beta_s))
print('(beta*s)/(beta*s-1) =', ratio, float(ratio))
print('near-coloop pair reserve =', pair_reserve, float(pair_reserve))
print('actual two-row minor coefficient relative to gamma^4 =', actual_minor_coeff, float(actual_minor_coeff))
print('C99 =', C99)
print('QFORM_TUNABLE_RIDGE_99_CHECK_PASS')
