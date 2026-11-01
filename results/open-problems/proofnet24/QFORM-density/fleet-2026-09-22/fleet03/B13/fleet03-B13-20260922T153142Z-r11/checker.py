from fractions import Fraction
from math import isclose

# Exact rational model in REPORT.md, Section 8.
c = Fraction(3, 5)
h = Fraction(3, 5)
B = 1 - h
rho2 = Fraction(0, 1)
beta = rho2 + h * (1 - c)
alpha = c * B
theta = Fraction(0, 1)
dstar = Fraction(1, 4)

lower_M = alpha * beta * (1 - theta - 3 * dstar)
actual_M = 12 * Fraction(3, 50) ** 2
bank_product_lower = lower_M / 16

assert alpha == Fraction(6, 25)
assert beta == Fraction(6, 25)
assert lower_M == Fraction(9, 625)
assert actual_M == Fraction(27, 625)
assert actual_M >= lower_M
assert bank_product_lower == Fraction(9, 10000)

# Explicit collar in REPORT.md: eta=1/8, epsilon=1/2.
eta = Fraction(1, 8)
epsilon = Fraction(1, 2)
min_M = (eta * eta / 4) * epsilon
assert min_M == Fraction(1, 512)
assert min_M / 16 == Fraction(1, 8192)

C_model = 6.0 * float(bank_product_lower) ** (-1.0 / 6.0)
C_collar = 6.0 * 8192.0 ** (1.0 / 6.0)
C_formula = 12.0 * float(eta) ** (-1.0 / 3.0) * float(epsilon) ** (-1.0 / 6.0)
assert isclose(C_model, 19.309787692112593, rel_tol=0, abs_tol=1e-12)
assert isclose(C_collar, 26.939089159424945, rel_tol=0, abs_tol=1e-12)
assert isclose(C_collar, C_formula, rel_tol=0, abs_tol=1e-12)

print('QFORM_PROFILE_OVERLAP_CHECK_PASS')
print('alpha=', alpha)
print('beta=', beta)
print('lower_M=', lower_M)
print('actual_M=', actual_M)
print('bank_product_lower=', bank_product_lower)
print('model_density_constant=', format(C_model, '.15f'))
print('collar_density_constant=', format(C_collar, '.15f'))
