from fractions import Fraction
from math import pi, sqrt

# Exact model from REPORT.md Section 7.
c = Fraction(3, 5)
h = Fraction(3, 5)
rho2 = Fraction(0, 1)
dmax = Fraction(1, 4)
Delta = (1-c)*(1-h) - rho2
lower_D0 = c*h*Delta*(1-3*dmax)
exact_D0 = (2*c*(1-c))**2 * (1-4*Fraction(1,4)**2)

assert Delta == Fraction(4,25)
assert lower_D0 == Fraction(9,625)
assert exact_D0 == Fraction(108,625)
assert exact_D0 >= lower_D0

C3 = 2*pi + 3*sqrt(3)
branch1 = 24*C3
branch2 = 12*(128**(1/6))
assert branch1 < 275.505
assert branch2 < 26.940

# The local-triple singular-value resource in the exact model.
kappa_resource = c*h*dmax
assert kappa_resource == Fraction(9,100)

print('QFORM_NESTED_HEAVY_CHECK_PASS')
print('Delta=', float(Delta))
print('lower_D0=', float(lower_D0))
print('exact_D0=', float(exact_D0))
print('kappa_resource=', float(kappa_resource))
print('C3=', C3)
print('branch_dmax_ge_1_over_6=', branch1)
print('branch_dmax_lt_1_over_6_Delta_ge_1_over_16=', branch2)
