from fractions import Fraction
import math

theta = Fraction(3, 4)
th = float(theta)
K = th**(-th) * (1-th)**(-(1-th))
C = 4 * math.sqrt(math.e * (3*th/(3*th-2))) * K**(-1/(8*th))
m = Fraction(3501,8000)
g = 1/(8*math.sqrt(2))
xi = Fraction(1,64)
application = C * float(m)**(-0.5) * (g*float(xi))**(-0.25)
anchored = g*g*float(xi)**2/3

assert abs(K - 4/(3**0.75)) < 1e-14
assert abs(C - 18.014628561278105) < 1e-12
assert application < 141.261
assert abs(anchored - 1/1572864) < 1e-20
assert Fraction(3,4) > Fraction(2,3)
assert Fraction(2,3) == 1/(2*theta)
print('QFORM_B01_AUTO12_CONSTANTS_PASS')
print('K_3/4=', repr(K))
print('C_2,3/4=', repr(C))
print('balanced_application=', repr(application))
print('anchored_mass=', repr(anchored))
