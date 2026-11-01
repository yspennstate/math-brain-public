from fractions import Fraction
import math

# Exact rational checks for QFORM-SPECTRAL-WINDOW-LEVERAGE-1OVER22-v1.
assert 11*3317**2 - 11000**2 == 27379 > 0
assert 5451**2*1683 - 500*10000**2 == 7653883 > 0
margin = Fraction(27,50) - (Fraction(5451,10000)+Fraction(625,3297))**2
assert margin == Fraction(288569529191,1087020900000000) > 0

# Numerical display of the exact theorem parameters.
delta = 5/11 - 1/math.sqrt(11)
sigma = delta - 1/64
gamma = (3/5)*sigma
q = 27/25
theta0 = 75/34
ridge_sqrt = math.sqrt((1/22)/delta) + (1/64)/gamma
C22 = 15625*math.sqrt(math.e)/(117*math.sqrt(6)*sigma)

print('delta', repr(delta))
print('sigma', repr(sigma))
print('gamma', repr(gamma))
print('ridge_sqrt_bound', repr(ridge_sqrt))
print('ridge_diag_bound', repr(ridge_sqrt**2))
print('q_over_2', repr(q/2))
print('theta_lower', repr(theta0))
print('two_q', repr(2*q))
print('C22', repr(C22))
assert ridge_sqrt**2 < q/2
assert theta0 > 2*q
assert C22 < 655
print('QFORM_B08_WINDOW_1OVER22_CHECK_PASS')
