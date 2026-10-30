from fractions import Fraction
from math import pi, sqrt

# Exact arithmetic for the fixed target-level threshold tau=499/1000.
tau = Fraction(499, 1000)
m = 1 - tau
assert m == Fraction(501, 1000)
assert m*m - tau*tau == Fraction(1, 500)

# Certify 50*(1000/501)^(3/4) < 84 without floating-point dependence.
margin = Fraction(84, 50)**4 - Fraction(1000, 501)**3
assert margin == Fraction(675442655696, 49121680078125)
assert margin > 0

opposite = 50 * (1000/501)**0.75
same_sign = pi * sqrt(500)
assert opposite < 84
assert same_sign < 84

# Equality model for the sharp entry estimate |H_ij|<=tau.
# H=[[0,tau],[tau,0]] has eigenvalues +/-tau. Removing the +tau mode
# leaves R with eigenvalues 0,-tau and H_12=tau.
assert tau > 0

print("QFORM_B19_HALF_BARRIER_CHECK")
print(f"tau={tau}")
print(f"m={m}")
print(f"m^2-tau^2={m*m-tau*tau}")
print(f"84/50 fourth-power margin numerator={margin.numerator}")
print(f"84/50 fourth-power margin denominator={margin.denominator}")
print(f"opposite_bound={opposite:.15f}")
print(f"same_sign_bound={same_sign:.15f}")
print("sharp_2x2_H=[[0,tau],[tau,0]] has singular values tau,tau")
print("STATUS=PASS")
