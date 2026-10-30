from fractions import Fraction
from math import gamma, log, pi, sqrt

# Exact Young constants for the limiting wedge.
L = log(7/5)
P = L**4 + 4*L**3 + 12*L**2 + 24*L + 24
h43 = sqrt(6/pi) * gamma(1/3)**(3/4) / (8**(1/4))
C_wedge = P**(1/4) * h43
C_cross_limit = 24**(1/4) * h43
C_target = 3*sqrt(2)

# Exact rational certification used in the report.
x = Fraction(337,1000)
P_rat = x**4 + 4*x**3 + 12*x**2 + 24*x + 24
margin4 = Fraction(324,1) - P_rat * Fraction(9,2) * Fraction(11,4)**3 / Fraction(157,50)**2

# Gamma(1/3)<11/4 appendix arithmetic.
first = Fraction(8042117,3319680)
tail = Fraction(46,125) - Fraction(37,900)
gamma_upper = first + tail

assert C_cross_limit < C_wedge < C_target
assert margin4 > 0
assert gamma_upper < Fraction(11,4)
assert P_rat == Fraction(33616816929761,10**12)
assert margin4 == Fraction(6201481198392981,1262028800000000)

# Finite cross theorem algebra: 24^(1/4) * 3^(3/4) * 2^(-1/4) = 3 sqrt(2).
finite_cross = 24**0.25 * 3**0.75 * 2**(-0.25)
assert abs(finite_cross-C_target) < 1e-12

print(f"C_cross_limit={C_cross_limit:.15f}")
print(f"C_wedge={C_wedge:.15f}")
print(f"3sqrt2={C_target:.15f}")
print(f"wedge_gap={C_target-C_wedge:.15f}")
print(f"fourth_power_rational_margin={margin4}")
print(f"gamma_elementary_upper={float(gamma_upper):.15f}")
print("PASS QFORM-SATURATED-CROSS-FINITE-GLOBAL-v1 QFORM-SATURATED-CROSS-WEDGE-GLOBAL-v1")
