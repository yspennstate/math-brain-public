from fractions import Fraction as F
from math import sqrt

# standardized Uniform[-sqrt(3),sqrt(3)] fourth cumulant
mu2 = F(1,1)
mu4 = F(9,5)
kappa4 = mu4 - 3*mu2*mu2
assert kappa4 == F(-6,5)
assert kappa4/F(24,1) == F(-1,20)

# Cone moment calculation.  For s=a^2+b^2, t=c^2,
# E_mu (v.Z)^2 = s/4+t/2,
# E_mu (v.Z)^4 = 9s^2/32+9st/4+3t^2/4.
def ecoeff(s,t):
    return (F(9,32)*s*s + F(9,4)*s*t + F(3,4)*t*t
            - 6*(s+t)*(F(1,4)*s+F(1,2)*t)
            + 3*(s+t)*(s+t))

# coefficients of s^2, st, t^2 recovered by basis evaluations
A = ecoeff(F(1),F(0))
C = ecoeff(F(0),F(1))
B = ecoeff(F(1),F(1)) - A - C
assert A == F(57,32)
assert B == F(15,4)
assert C == F(3,4)

# block pattern
E_block = 2*A + C
assert E_block == F(69,16)
assert E_block/F(20) == F(69,320)

# Hadamard four-row pattern: each v=(+/-1,+/-1,+/-1)/2
s = F(1,2)
t = F(1,4)
E_one_had = ecoeff(s,t)
E_had = 4*E_one_had
assert E_one_had == F(123,128)
assert E_had == F(123,32)
assert E_had/F(20) == F(123,640)

# orientation lower bound: e/h^2 is concave in x=t/h, so min is endpoint min=3/4.
assert min(A,C) == F(3,4)

print('PASS')
print('kappa4=', kappa4)
print('cone_coefficients=', A, B, C)
print('block_E=', E_block, 'relative_correction=', E_block/F(20))
print('hadamard_E=', E_had, 'relative_correction_per_m=', E_had/F(20))
print('universal_pattern_lower_bound=sum E >= 27/(4r)')
print('relative_deficit >= 27/(80 r m) = 27/(80 n) at first order')
print('3sqrt2=', 3*sqrt(2))
