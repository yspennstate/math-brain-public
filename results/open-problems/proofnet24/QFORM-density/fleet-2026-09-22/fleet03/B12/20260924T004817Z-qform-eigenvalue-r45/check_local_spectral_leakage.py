import math
import numpy as np

rng = np.random.default_rng(2026092401)

n, m, q, h = 14, 8, 2, 0.01
viol_a = 0
max_tail = 0.0
min_slack = float("inf")
for _ in range(5000):
    idx = [0, 1] + list(range(m, n))
    z = rng.normal(size=(len(idx), len(idx)))
    qmat, _ = np.linalg.qr(z)
    eigvecs = []
    for col in range(len(idx)):
        v = np.zeros(n)
        v[idx] = qmat[:, col]
        eigvecs.append(v)
    eigvecs += [np.eye(n)[:, i] for i in range(2, m)]
    V = np.column_stack(eigvecs)
    huge = (10 ** rng.uniform(-1, 5, size=len(idx))) * rng.choice([-1, 1], size=len(idx))
    small = rng.uniform(-h, h, size=m - 2)
    theta = np.r_[huge, small]
    T = V @ np.diag(theta) @ V.T
    svals = np.linalg.svd(T[:m, :], compute_uv=False)
    tail = svals[q]
    max_tail = max(max_tail, tail)
    min_slack = min(min_slack, h - tail)
    if tail > h + 1e-10:
        viol_a += 1

viol_b = 0
min_margin = float("inf")
max_tau_error = 0.0
for _ in range(5000):
    M0 = rng.normal(size=(m, n))
    qs = [int(rng.integers(0, 3)), int(rng.integers(0, 3))]
    qsum = sum(qs)
    k = int(rng.integers(1, m - qsum + 1))
    M = M0.copy()
    tail_sum = 0.0
    for q_i in qs:
        z = rng.normal(size=(n, n))
        T = (z + z.T) / 2
        Y = T[:m, :]
        M += Y
        svals = np.linalg.svd(Y, compute_uv=False)
        tail_sum += svals[q_i]
        evals = np.linalg.eigvalsh((T @ T)[:m, :m])[::-1]
        tau = math.sqrt(max(evals[q_i], 0.0))
        max_tau_error = max(max_tau_error, abs(tau - svals[q_i]))
    s0 = np.linalg.svd(M0, compute_uv=False)
    sf = np.linalg.svd(M, compute_uv=False)
    rhs = s0[k + qsum - 1] - tail_sum
    margin = sf[k - 1] - rhs
    min_margin = min(min_margin, margin)
    if margin < -1e-9:
        viol_b += 1

print({
    "seed": 2026092401,
    "threshold_trials": 5000,
    "threshold_violations": viol_a,
    "max_observed_s_qplus1": max_tail,
    "h": h,
    "min_threshold_slack": min_slack,
    "reserve_trials": 5000,
    "reserve_violations": viol_b,
    "min_reserve_margin": min_margin,
    "max_tau_identity_error": max_tau_error,
})
