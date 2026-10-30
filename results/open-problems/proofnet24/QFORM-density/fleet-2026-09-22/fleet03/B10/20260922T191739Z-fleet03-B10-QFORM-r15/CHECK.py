import math
import numpy as np

rng = np.random.default_rng(20260922)
max_det_rel = 0.0
max_cross_rel = 0.0
min_sigma_ratio = float("inf")

for _ in range(20_000):
    s = 1.0 + 4.0 * rng.random()
    a = 3.0 * rng.normal()
    b = 3.0 * rng.normal()
    kappa = (1.0 if rng.random() < 0.5 else -1.0) * (0.5 + 4.0 * rng.random())
    Lam = np.array([[0.0, s, 0.0], [s, a, b], [0.0, b, kappa]])
    sig = np.linalg.svd(Lam, compute_uv=False)
    Lam *= max(1.0, 1.0 / sig.min())
    sig = np.linalg.svd(Lam, compute_uv=False)

    L = 7.0 / 8.0 + (1.0 / 8.0) * rng.random()
    q = 1.0 - L / 2.0
    ell = L / (2.0 - L)
    Hhalf = np.diag([math.sqrt(q), 1.0, 1.0])
    Lam_hat = Hhalf @ Lam @ Hhalf

    lhs_det = np.linalg.det(Lam_hat)
    rhs_det = q * np.linalg.det(Lam)
    max_det_rel = max(max_det_rel, abs(lhs_det - rhs_det) / max(1.0, abs(rhs_det)))

    ratio = np.linalg.svd(Lam_hat, compute_uv=False).min() / (q * sig.min())
    min_sigma_ratio = min(min_sigma_ratio, ratio)

    rows = np.array([
        [math.sqrt(ell), 0.0, 0.0],
        [math.sqrt(1.0 - ell), 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ])
    A_hat = rows @ Lam_hat @ rows.T
    lhs_cross = np.sum(A_hat[0, 1:] ** 2)
    rhs_cross = (L / 2.0) * np.linalg.norm(Lam[:, 0]) ** 2
    max_cross_rel = max(max_cross_rel, abs(lhs_cross - rhs_cross) / max(1.0, abs(rhs_cross)))

print({
    "samples": 20_000,
    "max_det_relative_error": max_det_rel,
    "max_pair_mass_relative_error": max_cross_rel,
    "min_sigma_ratio": min_sigma_ratio,
})
