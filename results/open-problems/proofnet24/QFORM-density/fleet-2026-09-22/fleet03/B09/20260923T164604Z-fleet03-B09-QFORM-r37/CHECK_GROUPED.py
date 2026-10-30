import json
import math
import numpy as np

rng = np.random.default_rng(371)
max_w_error = 0.0
max_gamma_error = 0.0
for _ in range(100):
    h, t, s = 9, 8, 7
    P, _ = np.linalg.qr(rng.normal(size=(h, 2)))
    P = P[:, :2]
    B = rng.normal(size=(2, t))
    while np.linalg.matrix_rank(B) < 2:
        B = rng.normal(size=(2, t))
    D = rng.normal(size=(s, t))

    Delta = float(np.linalg.det(B @ B.T))
    Pi = B.T @ np.linalg.inv(B @ B.T) @ B
    E = D @ (np.eye(t) - Pi)
    W_projected = Delta * float(np.sum(E * E))
    W_cb = 0.0

    for k in range(s):
        coeff = np.vstack([B, D[k]])
        term = float(np.linalg.det(coeff @ coeff.T))
        W_cb += term

        full_cross = np.vstack([P @ B, D[k][None, :]])
        sing = np.linalg.svd(full_cross, compute_uv=False)
        gamma_sq = float(np.prod(sing[:3] ** 2))
        max_gamma_error = max(
            max_gamma_error,
            abs(gamma_sq - term) / max(1.0, abs(gamma_sq), abs(term)),
        )

    max_w_error = max(
        max_w_error,
        abs(W_projected - W_cb) / max(1.0, abs(W_projected), abs(W_cb)),
    )

out = {
    "trials": 100,
    "max_relative_W_identity_error": max_w_error,
    "max_relative_grouped_rank3_product_error": max_gamma_error,
    "grouped_diffuse_constant": 3 * 2 ** (7 / 6),
    "compiler_Gstar_constant": 4 * math.sqrt(6),
}
print(json.dumps(out, indent=2))
