from fractions import Fraction
import math

D = Fraction(53,3276800)
kappa = Fraction(53,428800)
pair = 3*(400**(1/3))*float(D)**(-1/3)*float(kappa)**(-1/6)

E1 = Fraction(3969,16384)
Z5 = Fraction(1,64)**4 * E1**5 / 120
d5 = 5*math.sqrt(2*math.e)*float(Z5)**(-1/10)

A0 = Fraction(103,6553600)
B0 = Fraction(217279,1048576)
Z_rank2 = Fraction(3,64)*B0*B0*A0
rank2 = 9*math.sqrt(3*math.e)*float(Z_rank2)**(-1/6)

Z_ridge = A0/Fraction(16384,1)
ridge = 9*math.sqrt(3*math.e)*float(Z_ridge)**(-1/6)

print('pair_bound=',repr(pair))
print('D5_bound=',repr(d5))
print('A0=',float(A0),'B0=',float(B0))
print('Z_rank2=',float(Z_rank2),'rank2_Dprime_bound=',repr(rank2))
print('Z_ridge=',float(Z_ridge),'ridge_Dprime_bound=',repr(ridge))
assert pair < 3917
assert d5 < 201.787
assert rank2 < 457.013
assert ridge < 819
print('STATUS=PASS')
