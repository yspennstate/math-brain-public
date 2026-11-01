from fractions import Fraction
from math import sqrt, pi

mu = Fraction(1,48)
alpha = (1 - sqrt(3*float(mu)))/2
assert abs(alpha - 3/8) < 1e-15
rho = sqrt(alpha/(1-alpha))
assert abs(rho - sqrt(3/5)) < 1e-15
c = rho/2
beta = alpha*c
assert c > 0.38729 and c < 0.38730
assert beta > 0.14523 and beta < 0.14524
Cstar = 2*pi + 3*sqrt(3) + sqrt((2*pi+3*sqrt(3))**2 + 3*pi*pi)
terminal = Cstar/c
assert terminal < 62.441
print('alpha =', alpha)
print('rho =', rho)
print('c/L =', c)
print('cross/L =', beta)
print('Cstar =', Cstar)
print('terminal constant =', terminal)
print('QFORM_B08_R24_CONSTANTS_PASS')
