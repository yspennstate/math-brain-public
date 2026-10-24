import math
import numpy as np


def stats(V):
    n = V.shape[0]
    lev = np.sum(V * V, axis=1)
    qsum = 0.0
    q2 = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            d = V[i, 0] * V[j, 1] - V[i, 1] * V[j, 0]
            q = d * d
            qsum += q
            q2 += q * q
    S2 = float(np.sum(lev * lev))
    theta = np.arctan2(V[:, 1], V[:, 0])
    A = np.sum((lev * lev) * np.exp(2j * theta))
    B = np.sum((lev * lev) * np.exp(4j * theta))
    q2_formula = 3.0 / 16.0 * S2 * S2 - 0.25 * abs(A) ** 2 + 1.0 / 16.0 * abs(B) ** 2
    delta = 1.0 - S2 + q2
    return lev, qsum, q2, q2_formula, delta


# Sharp equality frame: four rows of leverage 1/2 at angles 0, pi/4, pi/2, 3pi/4.
angles = np.arange(4) * math.pi / 4.0
V = math.sqrt(0.5) * np.c_[np.cos(angles), np.sin(angles)]
lev, qsum, q2, q2_formula, delta = stats(V)
assert np.linalg.norm(V.T @ V - np.eye(2)) < 1e-12
assert max(abs(lev - 0.5)) < 1e-12
assert abs(qsum - 1.0) < 1e-12
assert abs(q2 - q2_formula) < 1e-12
assert abs(delta - 3.0 / 16.0) < 1e-12

# Random sanity checks of the exact Fourier-moment identity and the proved floor.
rng = np.random.default_rng(20260923)
checked = 0
minimum = 1.0
max_formula_error = 0.0
for _ in range(10000):
    n = int(rng.integers(4, 61))
    Z = rng.normal(size=(n, 2))
    Q, _ = np.linalg.qr(Z)
    V = Q[:, :2]
    lev, qsum, q2, q2_formula, delta = stats(V)
    max_formula_error = max(max_formula_error, abs(q2 - q2_formula))
    if np.max(lev) <= 0.5 + 1e-12:
        checked += 1
        minimum = min(minimum, delta)
        assert delta >= 3.0 / 16.0 - 1e-10

C_T = 759375.0 / 2.0
H0sq = 1536.0 * math.e ** 2
M = 8.0 * C_T / H0sq
assert abs(8.0 * C_T - 3037500.0) < 1e-9
assert abs(M - 267.630809134903) < 1e-12
assert abs((2.0 / 3.0) ** 2 * (3.0 / 16.0) - 1.0 / 12.0) < 1e-15

print('QFORM_B13_R38_SHARP_DPP_CHECK_PASS')
print('random_frames_checked', checked)
print('minimum_random_delta', repr(minimum))
print('max_q2_formula_error', repr(max_formula_error))
print('sharp_delta_floor', 3.0 / 16.0)
print('W_floor', 1.0 / 12.0)
print('improved_mu_constant', 8.0 * C_T)
print('nonrank1_mu_mean_constant', repr(M))
print('R2_center_size', 48)
print('R2_star_mass_floor', 1.0 / 96.0)
print('light_bank_area_floor', 1.0 / math.sqrt(24.0))
print('light_transverse_row_marginal_cap', 0.5)
