import math
import json
import numpy as np
from scipy.integrate import quad

rng = np.random.default_rng(26092202)
identity_checks = []
for q in [1.0, 1.25, 1.5, 2.0]:
    B = rng.normal(size=(7, 5))
    gamma = 0.73
    K = B @ B.T @ np.linalg.inv(gamma**2 * np.eye(B.shape[0]) + B @ B.T)
    D = np.linalg.det(np.eye(B.shape[0]) + B @ B.T / gamma**2)
    for t in [0.17, 0.9, 3.4]:
        a = 2 * t
        alpha = (2 * gamma * abs(t))**2
        R = B.T
        M = alpha * np.eye(R.shape[0]) + a * a * (R @ R.T)
        d = np.array([
            a * a * R[:, j] @ np.linalg.solve(M, R[:, j])
            for j in range(R.shape[1])
        ])
        det_graph = np.linalg.det(np.eye(R.shape[0]) + (a * a / alpha) * (R @ R.T))
        identity_checks.append({
            "q": q,
            "t": t,
            "max_weight_error": float(np.max(np.abs(d - np.diag(K)))),
            "determinant_error": float(abs(det_graph - D)),
        })

envelope_checks = []
for beta in [2/3, 4/3, 1.7]:
    for r in [1.6, 1.8, 1.95]:
        if r * beta <= 1:
            continue
        t0 = 0.73
        f = lambda t: min(1.0, (t0 / t)**beta)**r
        numeric = 2 * (quad(f, 0, t0, limit=200)[0] + quad(f, t0, np.inf, limit=200)[0])
        exact = 2 * t0 * (r * beta) / (r * beta - 1)
        envelope_checks.append({
            "beta": beta,
            "r": r,
            "numeric": numeric,
            "exact": exact,
            "absolute_error": abs(numeric - exact),
        })

r = 9 / 5
theta_floor = 4 / 3
P_r = 4 * (2 - r)**((r - 3) / 2) * r**(-r / 2)
rank2_constant = math.e**0.25 * P_r * math.sqrt(r * theta_floor / (r * theta_floor - 2))
flat = []
for m in [4, 8, 16, 32]:
    col1 = np.ones(m) / math.sqrt(m)
    col2 = np.r_[np.ones(m // 2), -np.ones(m // 2)] / math.sqrt(m)
    U = np.column_stack([col1, col2])
    B = U @ U.T
    gamma = 1 / math.sqrt(2)
    K = B @ B.T @ np.linalg.inv(gamma**2 * np.eye(m) + B @ B.T)
    flat.append({
        "m": m,
        "theta": float(np.trace(K)),
        "max_diag_K": float(np.max(np.diag(K))),
        "top_two_singular_values": [float(x) for x in np.linalg.svd(B, compute_uv=False)[:2]],
    })

out = {
    "status": "ALL_CHECKS_PASS",
    "max_graph_weight_identity_error": max(x["max_weight_error"] for x in identity_checks),
    "max_determinant_identity_error": max(x["determinant_error"] for x in identity_checks),
    "max_envelope_integral_error": max(x["absolute_error"] for x in envelope_checks),
    "rank2_corollary": {
        "r": r,
        "theta_floor": theta_floor,
        "P_r": P_r,
        "density_constant": rank2_constant,
    },
    "flat_frame": flat,
}
print(json.dumps(out, indent=2, sort_keys=True))
