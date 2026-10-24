import numpy as np

rng = np.random.default_rng(20260923)
max_block = 0.0
max_det = 0.0
max_gamma = 0.0
max_lev = 0.0

for _ in range(2000):
    n = 8
    R, _ = np.linalg.qr(rng.normal(size=(n, 3)))
    R = R[:, :3]
    u0 = R[0]
    h = float(u0 @ u0)
    if h < 1e-8:
        continue
    r = u0 / np.sqrt(h)

    z = rng.normal(size=3)
    z -= r * (r @ z)
    z /= np.linalg.norm(z)
    v = z
    q = np.cross(r, v)
    q /= np.linalg.norm(q)

    s = float(0.2 + 2 * rng.random())
    b = float(rng.normal())
    c = float(rng.normal())
    d = float((0.2 + 2 * rng.random()) * (1 if rng.random() < 0.5 else -1))

    P = np.stack([r, v, q], axis=1)
    M0 = np.array([[0.0, s, 0.0], [s, b, c], [0.0, c, d]])
    M = P @ M0 @ P.T

    leaves = R[1:]
    t = leaves @ r
    alpha = leaves @ v
    beta = leaves @ q
    g = np.sqrt(h) * s * alpha
    ell = (t + (b / (2 * s)) * alpha + (c / s) * beta) / np.sqrt(h)

    B = leaves @ M @ leaves.T
    B2 = np.outer(g, ell) + np.outer(ell, g) + d * np.outer(beta, beta)
    max_block = max(max_block, float(np.max(np.abs(B - B2))))
    max_det = max(max_det, abs(abs(np.linalg.det(M)) - s * s * abs(d)))
    max_gamma = max(max_gamma, abs(float(g @ g) - h * s * s))

    transverse = np.sum((leaves - (leaves @ r)[:, None] * r) ** 2, axis=1)
    max_lev = max(max_lev, float(np.max(np.abs(transverse - (alpha**2 + beta**2)))))

print(f"max_block_identity_error={max_block:.17g}")
print(f"max_det_identity_error={max_det:.17g}")
print(f"max_gamma_identity_error={max_gamma:.17g}")
print(f"max_augmented_leverage_identity_error={max_lev:.17g}")
