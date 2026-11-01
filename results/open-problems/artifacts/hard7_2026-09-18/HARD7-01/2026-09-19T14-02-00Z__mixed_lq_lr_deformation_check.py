from fractions import Fraction as F

# Exact arithmetic self-check for HARD7-01 mixed l_q^2 + eps l_r^2 deformation.
# This verifies only the finite/rational calibration in the accompanying proof note.

n, q, r = 3, 4, 6
eps = F(1, 12)

# Rigorous rational envelopes used in the proof:
# M = 3^(1/3) < 3/2 because 3 < (3/2)^3.
M_up = F(3, 2)
assert F(3, 1) < M_up**3

# delta_0 = 3^(-1/6) > 4/5 because (4/5)^6 < 1/3.
delta_lo = F(4, 5)
assert delta_lo**6 < F(1, 3)

# Cone-measure density distortion squared at eps <= 1/12.
R2_up = ((F(1) + eps) / (F(1) + eps * delta_lo))**n
assert R2_up == F(65, 64)**3

# Hessian upper-comparison factor and gradient-share factor.
Afac_up = F(1) + eps * (r - 1) * M_up
gfac_up = F(1) + eps * M_up
assert Afac_up == F(13, 8)
assert gfac_up == F(9, 8)

# Sufficient condition for the source-required variance ratio:
# R^2 * [1 + eps(r-1)M] * [1 + eps M] <= q/2.
criterion_lhs = R2_up * Afac_up * gfac_up
criterion_rhs = F(q, 2)
assert criterion_lhs == F(32131125, 16777216)
assert criterion_lhs < criterion_rhs
criterion_slack = criterion_rhs - criterion_lhs
assert criterion_slack == F(1423307, 16777216)

# Previous exact l_q cone gap: lambda_q = n q / (2(q-1)).
lambda_q = F(n * q, 2 * (q - 1))
assert lambda_q == F(2, 1)

# Comparison lower bound for the deformed full-even spectral gap.
lambda_lo = lambda_q / (R2_up * Afac_up)
assert lambda_lo == F(4194304, 3570125)

# Pointwise deformed energy coefficient c_eps.
c_up = F(2, q - 1) * gfac_up
assert c_up == F(3, 4)

# Resulting variance ratio upper bound c/(lambda+c).
ratio_up = c_up / (lambda_lo + c_up)
assert ratio_up == F(10710375, 27487591)

target = F(2, n + 2)
assert target == F(2, 5)
assert ratio_up < target
ratio_slack = target - ratio_up
assert ratio_slack == F(1423307, 137437955)

# Quantitative covariance coefficient from
# Cov >= n/2 * [1 - (n+2)/2 * ratio_up] * m(1-m).
covariance_coefficient = F(n, 2) * (F(1) - F(n + 2, 2) * ratio_up)
assert covariance_coefficient == F(4269921, 109950364)
assert covariance_coefficient > 0

print(f"n_q_r = {n}_{q}_{r}")
print(f"eps_max = {eps}")
print(f"M_upper = {M_up}")
print(f"delta0_lower = {delta_lo}")
print(f"R2_upper = {R2_up}")
print(f"A_factor_upper = {Afac_up}")
print(f"gradient_factor_upper = {gfac_up}")
print(f"criterion_lhs = {criterion_lhs}")
print(f"criterion_rhs = {criterion_rhs}")
print(f"criterion_slack = {criterion_slack}")
print(f"lambda_q = {lambda_q}")
print(f"lambda_lower = {lambda_lo}")
print(f"c_upper = {c_up}")
print(f"variance_ratio_upper = {ratio_up}")
print(f"variance_ratio_target = {target}")
print(f"variance_ratio_slack = {ratio_slack}")
print(f"covariance_coefficient_lower = {covariance_coefficient}")
print("ALL_EXACT_CHECKS_PASS = True")
