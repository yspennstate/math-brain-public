from fractions import Fraction
from math import e, sqrt

S0 = Fraction(1,12800) - Fraction(1,65536)
assert S0 == Fraction(103,1638400)
assert S0/4 == Fraction(103,6553600)
assert S0/2 == Fraction(103,3276800)
D = S0/2 - Fraction(1,65536)
assert D == Fraction(53,3276800)
M = Fraction(67,512)
kappa = D/M
assert kappa == Fraction(53,428800)
E1 = Fraction(3969,16384)
top4 = Fraction(63,64)*E1
assert top4 == Fraction(250047,1048576)
rank2 = top4 - Fraction(1,32)
assert rank2 == Fraction(217279,1048576)
gamma2 = Fraction(1,384)
assert gamma2/2 == Fraction(1,768)
ridge = 36*sqrt(3*e)
assert ridge < 102.805
partner = 3*e*(4**(Fraction(1,3)))
assert partner < 12.946
print('S0=', S0, float(S0))
print('arm=', S0/4, float(S0/4))
print('det_lb=', D, float(D))
print('kappa_lb=', kappa, float(kappa))
print('top4=', top4, float(top4))
print('rank2=', rank2, float(rank2))
print('ridge_row_energy=', gamma2/2, float(gamma2/2))
print('ridge_density=', ridge)
print('partner_density=', float(partner))
print('STATUS=PASS')
