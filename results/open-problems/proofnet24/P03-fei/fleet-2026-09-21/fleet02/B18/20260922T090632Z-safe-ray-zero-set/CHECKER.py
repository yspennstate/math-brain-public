from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec=70

def F(m):
    return 1-m**4-Fraction(1,36)*(1-m*m)**2

def eta(u):
    return F(1-2*u)/8

u38=Fraction(3,8)
ur=Fraction(967,2048)
uh=Fraction(1,2)
beta=Fraction(23156036957147,44712962557360)
gamma=Fraction(465,256)-beta
scale=Fraction(34877,250000)

assert eta(u38)==Fraction(995,8192)
assert eta(uh)==Fraction(35,288)
assert eta(ur)==Fraction(38489330046971,316659348799488)

P=Fraction(57,256)*eta(u38)+Fraction(465,256)*eta(uh)-eta(ur)
assert P==Fraction(39974940944389,316659348799488)

B=-(Fraction(57,256)*eta(u38)-eta(ur)+beta*eta(uh))
assert B==Fraction(5586911653540898590992293,176984720078868840129232896)
assert B>0
assert P+B==gamma*eta(uh)

scaledP=scale*P
scaledB=scale*B
scaledCenter=scale*eta(uh)
assert scaledCenter==Fraction(244139,14400000)
assert scaledP>Fraction(17611420,10**9)

def dec(x):
    return Decimal(x.numerator)/Decimal(x.denominator)

print('eta_3_8=',dec(eta(u38)))
print('eta_half=',dec(eta(uh)))
print('eta_r=',dec(eta(ur)))
print('prime_increment_per_unit=',dec(P))
print('aggregate_AND_increment_per_unit=',dec(B))
print('gamma=',dec(gamma))
print('dual_identity=',P+B==gamma*eta(uh))
print('scaled_prime_increment=',dec(scaledP))
print('scaled_AND_increment=',dec(scaledB))
print('scaled_center_increment=',dec(scaledCenter))
print('repair_gap_vs_0.017611420=',dec(scaledP-Fraction(17611420,10**9)))
print('PASS')
