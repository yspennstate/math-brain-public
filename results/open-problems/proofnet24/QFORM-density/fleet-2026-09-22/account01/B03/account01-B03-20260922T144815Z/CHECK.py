import math
import numpy as np
from scipy.integrate import quad

rng = np.random.default_rng(92622)

# Bilinear determinant identity.
for r in range(2, 7):
    sigma = np.exp(rng.normal(size=r))
    delta = float(np.prod(sigma))
    M = np.diag(np.r_[2 * sigma, -2 * sigma])
    lhs = abs(np.linalg.det(M)) ** 0.5
    rhs = (2 ** r) * delta
    assert abs(lhs - rhs) <= 1e-12 * max(1.0, rhs)

# Exact weighted-integral constant in the theorem.
for r in (2, 3, 4, 5):
    delta = 1.7
    C0 = (2 * math.pi) ** (r / 2) * delta ** (-0.5)
    f = lambda t: t ** (-0.5) * min(1.0, C0 * t ** (-r / 2))
    numerical = 2 * quad(f, 0.0, math.inf, limit=500)[0]
    formula = (4 * r / (r - 1)) * math.sqrt(2 * math.pi) * delta ** (-1 / (2 * r))
    assert abs(numerical - formula) <= 2e-7 * formula

# account02/B03 coloop-bank family: balanced exact-rank-two cross block.
min_delta = 1.0
max_bound = 0.0
for m in range(2, 101):
    p = m // 2
    q = m - p
    delta = p * q / (m * m)
    min_delta = min(min_delta, delta)
    max_bound = max(max_bound, 8 * delta ** (-0.25))
assert min_delta >= 2 / 9 - 1e-15
assert abs(max_bound - 8 * (9 / 2) ** 0.25) < 1e-12

print("QFORM_B03_COPY_RECTANGULAR_CROSS_PASS")
print(f"min_partner_delta={min_delta:.16g}")
print(f"worst_partner_bound={max_bound:.12f}")
print(f"partner_special_bound_pi_sqrt2={math.pi * math.sqrt(2):.12f}")
