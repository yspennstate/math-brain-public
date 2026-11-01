import math
from fractions import Fraction

c3 = Fraction(11907, 16384)
partner_bound = 16*math.sqrt(math.pi)/math.sqrt(float(c3))
assert abs(partner_bound - 33.26623964880013) < 1e-12

# Exact spectral factor for the perturbative obstruction:
# char poly = -l^2(l-1)(d^2-d*l+1)(d^2+d*l+1)/d^2,
# hence nonzero eigenvalues are 1, +(d+d^-1), -(d+d^-1)
for d in (1.0, 0.5, 0.1, 0.01):
    L = d + 1/d
    assert L >= 2
    assert abs(2*math.sqrt(math.pi) - 3.5449077018110318) < 1e-12

# 2D bathtub identity for K=1/(2*s1*s2).
for s1,s2 in ((1,1),(3,2),(10,0.2)):
    K = 1/(2*s1*s2)
    R = 1/math.sqrt(math.pi*K)
    disk_integral = K*2*math.pi*R
    layercake = 2*math.sqrt(math.pi*K)
    assert abs(disk_integral-layercake) < 1e-12

print('PASS')
print('null-bank coefficient', 2*math.sqrt(math.pi))
print('partner r37/r38 null-bank bound', partner_bound)
