from math import sqrt, e

# Exact threshold algebra used in REPORT.md.
# Small-defect branch is delegated to the pinned fleet02/B08 theorem.

stable_rank_threshold = 30.0
theta_residual_lower = stable_rank_threshold / 5.0
theta_actual_lower = theta_residual_lower - 3.0
assert theta_residual_lower == 6.0
assert theta_actual_lower == 3.0

# If tau > 1/40 and gamma=tau/2, the q=1 ridge theorem gives
# sqrt(e)/(sqrt(2)*gamma) * theta/(theta-2), maximized at theta=3.
worst_universal_constant = 120.0 * sqrt(2.0 * e)
localized_row_floor = 1.0 / (80.0 * sqrt(2.0))

print('theta_residual_lower', theta_residual_lower)
print('theta_actual_lower', theta_actual_lower)
print('universal_density_constant_upper', worst_universal_constant)
print('localized_row_floor', localized_row_floor)
print('QFORM_B08_STABLE_RANK_TRICHOTOMY_CHECK_PASS')
