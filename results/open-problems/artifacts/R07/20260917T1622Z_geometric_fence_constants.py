from fractions import Fraction

# R07 / I0077 / T25 exact rational scaffold.
# Canonical sampling period: P = log 4. Then the sampled OU chain has
# one-step coefficient r = exp(-P/2) = 1/2 and innovation variance 3/4.
# Canonical normalized aperture: a = 1/20, so the target interval has
# length 2a = 1/10.
#
# Analytic (non-finite) input proved on the report page:
# the Lebesgue density of N(mean, 3/4) is everywhere < 1, since its
# maximum is sqrt(2/(3*pi)) < 1. Therefore the one-step row survival
# probability q is < 2a = 1/10. Reversibility plus Schur's test then
# gives rho <= q. The exact rational comparison below verifies
# 1/10 < 1/4 = exp(-P), hence kappa_d = -log(rho)/P > 1.

a = Fraction(1, 20)
r = Fraction(1, 2)
sigma_sq = Fraction(1) - r * r
interval_length = 2 * a
row_survival_rational_upper = interval_length
critical_rho = Fraction(1, 4)

assert sigma_sq == Fraction(3, 4)
assert interval_length == Fraction(1, 10)
assert row_survival_rational_upper < critical_rho

print("R07 I0077 T25 exact rational self-check")
print(f"a={a}")
print(f"r={r}")
print(f"sigma_sq={sigma_sq}")
print(f"interval_length=2a={interval_length}")
print("analytic input: max density of N(mean,3/4) is sqrt(2/(3*pi)) < 1")
print(f"row_survival_q < {row_survival_rational_upper}")
print(f"critical_rho=e^(-P)=1/4={critical_rho} for P=log 4")
print(f"q_upper_lt_critical={row_survival_rational_upper < critical_rho}")
print("therefore rho <= q < e^(-P), so kappa_d > 1")
print("PASS")
