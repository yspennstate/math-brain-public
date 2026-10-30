from fractions import Fraction
import math

eps=Fraction(1,100)
l1,l2,l3=Fraction(2),Fraction(3),Fraction(5)
V21=eps/Fraction(4)
V3=(1-eps)/Fraction(4)
P=V21*V3
S2=(l1*l2)**2/Fraction(16)
Z1=l3*l3*eps*(1-eps)
lhs=S2*Z1
rhs=(l1*l2*l3)**2*P
alpha1=(eps/Fraction(8))/V21
alpha2=(eps/Fraction(8))/V21
C=3*2**(7/6)
partner=Fraction(320,3)

print('eps =', eps)
print('V21 =', V21)
print('V3 =', V3)
print('P =', P)
print('S_B^2 =', S2)
print('Z1 =', Z1)
print('lhs =', lhs)
print('rhs =', rhs)
print('identity =', lhs == rhs)
print('alpha =', alpha1, alpha2)
print('grouped_constant =', f'{C:.12f}')
print('partner_gate_constant =', float(partner))
print('barrier P<=eps =', P <= eps)
assert lhs == rhs
assert alpha1 == alpha2 == Fraction(1,2)
assert P <= eps
assert C < 6.735
assert partner < Fraction(106667,1000)
print('STATUS=PASS')
