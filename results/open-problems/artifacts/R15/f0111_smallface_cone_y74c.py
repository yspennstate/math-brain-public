from fractions import Fraction
from math import factorial

# Exact arithmetic supporting the analytic cone proof in the matching R15 report.
# No floating-point calculation is used.

x = Fraction(25, 36)
exp_trunc5 = sum((x ** k) / factorial(k) for k in range(6))
assert exp_trunc5 > 2
# Since exp is increasing, exp(25/36) > 2 implies log 2 < 25/36.

alpha_lower = Fraction(2, 3) - Fraction(4, 9) * x
assert alpha_lower == Fraction(29, 81)
assert alpha_lower > Fraction(179, 500)

beta_star = Fraction(13, 45)
assert beta_star > Fraction(36, 125)

alpha0 = Fraction(179, 500)
beta0 = Fraction(36, 125)
discriminant = (1 - alpha0) ** 2 - 4 * alpha0 * beta0
assert discriminant == Fraction(-63, 250000)
assert discriminant < 0

print("PASS R15 F0111 universal small-face cone exact arithmetic")
print(f"exp_25_36_trunc5={exp_trunc5} > 2")
print(f"alpha_star > {alpha_lower} > {alpha0}")
print(f"beta_star={beta_star} > {beta0}")
print(f"cone_discriminant={discriminant} < 0")
