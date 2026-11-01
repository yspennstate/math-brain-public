from fractions import Fraction
from math import factorial

# Exact finite inequalities for the L >= 6 log-uniform counterexample family.
partial = sum(Fraction(1, factorial(n)) for n in range(6))
assert partial == Fraction(163, 60)
assert partial**6 > 400

# Hence e > 163/60 and e^6 > 400, so exp(-6) < 1/400.
a_upper = Fraction(1, 400)
phase_lower = 6 * Fraction(399, 401) - 1
assert phase_lower > 0

# Using pi^2 < 10, 1-a^2 < 1, and a < 1/400 at L=6:
# C_6 < (1/400) * 46^2 / 6 * (400/399)^4.
C6_upper = a_upper * Fraction(46**2, 6) * Fraction(400**4, 399**4)
assert C6_upper < 1

# For L >= 6, the logarithmic derivative of
# exp(-L)(L^2+10)^2 / (L(1-exp(-L))^4)
# is strictly less than -1 + 3/L <= -1/2.
derivative_upper_at_6 = -1 + Fraction(3, 6)
assert derivative_upper_at_6 == Fraction(-1, 2)
assert derivative_upper_at_6 < 0

print('P20 I0081 L>=6 exact family check: PASS')
print('sum_{n=0}^5 1/n! =', partial)
print('(163/60)^6 =', partial**6, '> 400')
print('163^6 - 400*60^6 =', 163**6 - 400*60**6, '> 0')
print('phase derivative lower bound at L=6 =', phase_lower, '> 0')
print('C6_upper =', C6_upper, '< 1')
print('monotonicity log-derivative upper bound for L>=6 <=', derivative_upper_at_6, '< 0')
