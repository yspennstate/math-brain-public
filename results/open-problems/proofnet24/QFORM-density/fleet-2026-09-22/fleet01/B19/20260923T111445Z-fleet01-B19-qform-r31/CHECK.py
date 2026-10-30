from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 60

tau = Fraction(1,256)
M0 = tau + tau*tau
S0 = Fraction(123,4096)
beta0 = (S0-M0)/2
c0 = (1-tau)**2/4
eta = Fraction(1,64)
delta5 = eta**4 * c0**5 / 120
capture = (1-eta)*c0
ratio = c0/M0

D = lambda q: Decimal(q.numerator)/Decimal(q.denominator)
E = Decimal(1).exp()
C5 = Decimal(5) * (Decimal(2)*E).sqrt() * (D(delta5) ** (Decimal(-1)/Decimal(10)))

assert M0 == Fraction(257,65536)
assert beta0 == Fraction(1711,131072)
assert c0 == Fraction(65025,262144)
assert ratio > 63
assert C5 < Decimal('199.413')
assert capture == Fraction(63,64)*c0

print('M0 =', M0, D(M0))
print('beta0 =', beta0, D(beta0))
print('c0 =', c0, D(c0))
print('c0/M0 =', D(ratio))
print('delta5 =', D(delta5))
print('C5 =', C5)
print('capture_lower =', D(capture))
print('QFORM_N3_STAR_BALANCED_LEAFCROSS_CHECK_PASS')
