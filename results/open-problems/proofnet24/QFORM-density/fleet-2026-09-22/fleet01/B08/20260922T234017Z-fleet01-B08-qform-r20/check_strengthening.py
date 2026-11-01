from fractions import Fraction
import math

m=1/16
kappa=1/81
b=1/2
alpha=(1-math.sqrt(3*m))/2
rho=alpha*b-kappa
gate=(math.sqrt(m/alpha)+math.sqrt(6)*kappa/rho)**2
C=9*math.sqrt(3*math.e)/(2*rho)
Cr=(14580/419)*math.sqrt(3*math.e)

print('alpha =',repr(alpha))
print('rho =',repr(rho))
print('gate =',repr(gate))
print('exact_boundary_constant =',repr(C))
print('rational_report_constant =',repr(Cr))

assert alpha > 17/60
assert rho > 419/3240
assert Fraction(15,68) < Fraction(64,289)
s=Fraction(8,17)+Fraction(98,419)
print('rational_gate_sum =',s, float(s))
print('rational_gate_square =',s*s,float(s*s))
print('half_minus_gate_square =',Fraction(1,2)-s*s)
assert s*s < Fraction(1,2)
assert gate < 1/2
assert Cr < 100
print('QFORM_B08_R20_STRENGTHENING_CHECK_PASS')
