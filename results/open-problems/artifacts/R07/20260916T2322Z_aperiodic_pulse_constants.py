from fractions import Fraction

# Exact-arithmetic self-check for the canonical aperiodic asymmetric pulse example.
# The analytic inputs used on the proof page are pi^2 > 9 and exp(-1/8) > 7/8.

eps = Fraction(1, 10)
gap_lo = Fraction(1) - 2 * eps
gap_hi = Fraction(1) + 2 * eps
tau = Fraction(2, 5)
rho = 1 / gap_hi

ell_star = Fraction(-1, 4)
u_star = Fraction(1, 2)
d = u_star - ell_star

pi_sq_lower = Fraction(9, 1)
exp_lower = Fraction(7, 8)
lambda_lower = pi_sq_lower * exp_lower / (2 * d * d)
kappa_lower = rho * tau * lambda_lower

assert gap_lo == Fraction(4, 5)
assert gap_hi == Fraction(6, 5)
assert tau < gap_lo
assert rho == Fraction(5, 6)
assert d == Fraction(3, 4)
assert lambda_lower == 7
assert kappa_lower == Fraction(7, 3)
assert kappa_lower > 1

print('PASS')
print(f'gap_lo={gap_lo}')
print(f'gap_hi={gap_hi}')
print(f'tau={tau}')
print(f'rho={rho}')
print(f'd={d}')
print(f'lambda_lower={lambda_lower}')
print(f'kappa_lower={kappa_lower}')
