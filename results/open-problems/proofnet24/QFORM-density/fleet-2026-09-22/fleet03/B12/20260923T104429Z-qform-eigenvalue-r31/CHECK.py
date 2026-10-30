import json, math
import numpy as np

SEED = 20260923104429
rng = np.random.default_rng(SEED)

def orth(n):
    Q, R = np.linalg.qr(rng.normal(size=(n, n)))
    d = np.sign(np.diag(R)); d[d == 0] = 1
    return Q * d

N1 = 10000
min_count = 10**9
min_margin = float('inf')
max_comp_err = 0.0
for _ in range(N1):
    m = int(rng.integers(7, 18))
    e = int(rng.integers(3, m))
    mu = float(rng.uniform(0.5, 3.0))
    delta = float(rng.uniform(0, 0.9 * mu))
    Q = orth(m); E = Q[:, :e]
    Qe = orth(e)
    vals = rng.normal(scale=.4, size=e)
    vals[:3] = rng.choice([-1, 1], 3) * (mu + rng.random(3) * 3)
    B0 = Qe @ np.diag(vals) @ Qe.T
    Qc = orth(e)
    cvals = rng.uniform(-delta, delta, size=e)
    C = Qc @ np.diag(cvals) @ Qc.T
    X = (10 ** rng.uniform(-2, 4)) * rng.normal(size=(e, m-e))
    Qf = orth(m-e)
    fvals = (10 ** rng.uniform(-2, 4)) * rng.normal(size=m-e)
    D = Qf @ np.diag(fvals) @ Qf.T
    Ab = np.block([[B0 + C, X], [X.T, D]])
    A = Q @ Ab @ Q.T
    ev = np.linalg.eigvalsh(A)
    threshold = mu - delta
    count = int(np.sum(np.abs(ev) >= threshold - 1e-9))
    if count < 3:
        raise AssertionError((count, mu, delta))
    min_count = min(min_count, count)
    third = np.sort(np.abs(ev))[::-1][2]
    min_margin = min(min_margin, float(third - threshold))
    comp = E.T @ A @ E
    max_comp_err = max(max_comp_err, float(np.linalg.norm(comp - B0, 2)))

N2 = 10000
min_partner_count = 10**9
min_partner_margin = float('inf')
for _ in range(N2):
    s = int(rng.integers(1, 7)); d = int(rng.integers(3, 10))
    mu = float(rng.uniform(.5, 3))
    Qd = orth(d)
    dvals = rng.normal(scale=.3, size=d)
    dvals[:3] = rng.choice([-1, 1], 3) * (mu + rng.random(3) * 3)
    D = Qd @ np.diag(dvals) @ Qd.T
    C = rng.normal(size=(s, s)); C = (C + C.T) / 2
    Cross = (10 ** rng.uniform(-2, 4)) * rng.normal(size=(s, d))
    U = orth(s)
    theta_vals = (10 ** rng.uniform(-2, 4)) * rng.normal(size=s)
    Theta = U @ np.diag(theta_vals) @ U.T
    H = np.block([[C + Theta, Cross], [Cross.T, D]])
    ev = np.linalg.eigvalsh(H)
    count = int(np.sum(np.abs(ev) >= mu - 1e-9))
    if count < 3:
        raise AssertionError((count, mu))
    min_partner_count = min(min_partner_count, count)
    third = np.sort(np.abs(ev))[::-1][2]
    min_partner_margin = min(min_partner_margin, float(third - mu))

mu = 2.0; delta = 0.3
sharp = np.diag([mu-delta] * 3)
sharp_third = float(np.sort(np.abs(np.linalg.eigvalsh(sharp)))[::-1][2])
assert abs(sharp_third - (mu-delta)) < 1e-12

out = {
    'seed': SEED,
    'general_compression_tests': N1,
    'general_violations': 0,
    'minimum_large_mode_count_at_threshold': int(min_count),
    'minimum_third_abs_eigenvalue_minus_threshold': min_margin,
    'max_observed_compression_error_norm': max_comp_err,
    'partner_style_tests': N2,
    'partner_style_violations': 0,
    'minimum_partner_large_mode_count_at_mu': int(min_partner_count),
    'minimum_partner_third_abs_eigenvalue_minus_mu': min_partner_margin,
    'sharp_example_mu': mu,
    'sharp_example_delta': delta,
    'sharp_example_third_abs_eigenvalue': sharp_third,
    'sharp_threshold': mu-delta,
    'volume_q1_coefficient_3e': 3*math.e,
    'volume_branch_if_s3_ge_g_over_2_coefficient_6e': 6*math.e,
    'finite_core_m14_if_gap_g_over_2_coefficient_over_g': 4*math.sqrt(6*math.pi*14),
}
print(json.dumps(out, indent=2, sort_keys=True))
