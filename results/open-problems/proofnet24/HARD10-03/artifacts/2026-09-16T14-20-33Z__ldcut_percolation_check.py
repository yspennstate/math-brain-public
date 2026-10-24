from fractions import Fraction
import math

q = Fraction(37, 50)
# n=500 r, m=370 r, s=185 r.
# Exact one-r block factor after the type-class lower bound and Chernoff step:
A = Fraction(2**500, 1) * q**370 * (1-q)**130 * Fraction(25, 74)**185
# To certify exponent epsilon=203/500, compare A with 2^{-203}.
R = A * 2**203
r0 = 2326

def holds(r: int) -> bool:
    return (500*r + 1) * pow(R.numerator, r) <= pow(R.denominator, r)

assert R < 1
assert not holds(r0 - 1)
assert holds(r0)
# f_r=(500r+1)R^r is decreasing for every r>=r0 once this exact ratio is <1.
step_ratio = R * Fraction(500*r0 + 501, 500*r0 + 1)
assert step_ratio < 1

# Explicit 2-dependent Peierls gate constants: Delta_*=26, M=27.
Delta_star = 26
M = 27
assert 8 * Delta_star**2 == 5408
q0 = Fraction(1, 5408**27)
peierls_lower = Fraction(1,1) - q0 - Fraction(8,49)
assert peierls_lower > 0

print('ALL_EXACT_CHECKS_PASS')
print('q = 37/50')
print('n = 500 r, m = 370 r, s = 185 r')
print('R = 2^203 * A < 1:', R < 1)
print('r0_minus_1_fails:', not holds(r0-1))
print('r0_holds:', holds(r0))
print('r0:', r0)
print('n0:', 500*r0)
print('step_ratio_at_r0_lt_1:', step_ratio < 1)
print('certified_polynomial_exponent:', '203/500')
print('asymptotic_rate_approx:', format(-math.log2(float(A))/500, '.15f'))
print('Delta_star:', Delta_star)
print('dependence_color_count_M:', M)
print('q0 = 5408^-27')
print('percolation_lower_bound_positive:', peierls_lower > 0)
print('percolation_lower_bound_approx:', format(float(peierls_lower), '.15f'))
