from fractions import Fraction
from math import factorial

partial = sum(Fraction(1, factorial(n)) for n in range(6))
assert partial == Fraction(163, 60)
assert partial**6 > 400
pi2_rational_upper = Fraction(22, 7)**2
assert pi2_rational_upper == Fraction(484, 49)
assert pi2_rational_upper < 10

a_upper = Fraction(1, 400)
phase_lower = 6 * Fraction(399, 401) - 1
assert phase_lower == Fraction(1993, 401) > 0

C6_upper = a_upper * Fraction(46**2, 6) * Fraction(400**4, 399**4)
assert C6_upper == Fraction(67712000000, 76034875203)
assert C6_upper < 1

derivative_upper = -1 + Fraction(3, 6)
assert derivative_upper == Fraction(-1, 2) < 0

print('P20 I0081 L>=6 exact family check v2: PASS')
print('e lower partial =', partial)
print('(163/60)^6 - 400 =', partial**6 - 400, '> 0')
print('(22/7)^2 =', pi2_rational_upper, '< 10')
print('phase derivative lower bound =', phase_lower, '> 0')
print('C6_upper =', C6_upper, '< 1')
print('log-derivative upper bound for monotonic envelope =', derivative_upper, '< 0')
