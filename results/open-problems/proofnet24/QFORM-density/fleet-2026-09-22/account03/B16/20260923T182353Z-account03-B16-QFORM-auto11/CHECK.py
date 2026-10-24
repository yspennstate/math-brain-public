from fractions import Fraction
from math import sqrt, pi, e

# inherited near-coloop arithmetic
R2min = Fraction(4031,4096)
alpha2a_max = Fraction(1,63**2*64)
beta2min = R2min-alpha2a_max
assert beta2min > Fraction(31,32)
ratio_min = 1-alpha2a_max/R2min
k_min = Fraction(63,64)*ratio_min
assert k_min > Fraction(31,32)

# new exact-coloop density constant M=2, L=1, |beta^2 w|=|det Lambda|>=1
C_coloop = 3*2**(4/3)
assert C_coloop < 7.56

# designated partner threshold: c>63/64 and |alpha det Lambda|>=1/4096
C_partner = 4*sqrt(2*e)*sqrt(64/63)*8
assert C_partner < 76

print('beta2min=', beta2min, float(beta2min))
print('k_min=', k_min, float(k_min))
print('C_coloop=', C_coloop)
print('C_partner_threshold=', C_partner)
print('STATUS=PASS')
