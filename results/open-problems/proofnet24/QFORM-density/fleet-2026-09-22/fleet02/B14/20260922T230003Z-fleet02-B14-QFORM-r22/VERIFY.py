import math

# Deterministic regression checks for REPORT.md.  The proof itself is exact;
# these checks only guard constants/algebra used in the written argument.

for k in range(1, 101):
    eps = k / 100.0
    lam_plus = (1.0 + math.sqrt(1.0 + 4.0 * eps * eps)) / 2.0
    lam_minus = (1.0 - math.sqrt(1.0 + 4.0 * eps * eps)) / 2.0
    assert lam_plus >= 1.0
    assert lam_minus <= 0.0

    h075 = 0.75**2 - (2.0 - eps / 2.0) * 0.75
    h1 = 1.0 - (2.0 - eps / 2.0)
    assert max(h075, h1) <= -0.5 + 1e-12

# The two optimized pair-log formulas must meet continuously at theta=1.
D = 1.0
kappa = 1.0
H = 1.0 / 8.0
theta = 2.0 * math.sqrt(2.0 * D * H / kappa)
low = 6.0 * (H / (kappa * math.sqrt(D))) ** (1.0 / 3.0)
high = D ** (-0.5) * (3.0 + 2.0 * math.log(theta))
assert abs(theta - 1.0) < 1e-12
assert abs(low - 3.0) < 1e-12
assert abs(high - 3.0) < 1e-12

print('tv_lower_bound=', 1.0 / 128.0)
print('event_q_upper_bound=', -3.0 / 8.0)
print('boundary_theta=', theta)
print('boundary_pairlog_bound=', low)
print('QFORM_B14_R22_CHECK_PASS')
