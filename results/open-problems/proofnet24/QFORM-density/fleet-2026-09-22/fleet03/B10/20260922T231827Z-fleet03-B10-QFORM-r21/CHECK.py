import numpy as np

rng = np.random.default_rng(20260922)

packet_err = 0.0
for _ in range(1000):
    O, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    e1, e2, n = O[:, 0], O[:, 1], O[:, 2]
    nb = int(rng.integers(2, 8))
    coeff = rng.normal(size=(nb, 2))
    rows_b = coeff[:, 0, None] * e1 + coeff[:, 1, None] * e2
    h = float(np.linalg.det(coeff.T @ coeff))

    r = rng.normal(size=3)
    r /= np.linalg.norm(r)
    nc = int(rng.integers(1, 7))
    alpha = rng.normal(size=nc)
    rows_c = alpha[:, None] * r
    m = float(alpha @ alpha)
    delta = float((r @ n) ** 2)

    T = 0.0
    for i in range(nb):
        for j in range(i + 1, nb):
            for k in range(nc):
                T += float(np.linalg.det(np.stack([rows_b[i], rows_b[j], rows_c[k]])) ** 2)
    packet_err = max(packet_err, abs(T - m * h * delta))

active_det_err = 0.0
for _ in range(500):
    O, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    e1, e2, n = O[:, 0], O[:, 1], O[:, 2]
    r = rng.normal(size=3)
    r /= np.linalg.norm(r)

    V, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    vals = np.array([1.2, -1.7, 2.3])
    M = V @ np.diag(vals) @ V.T
    F = np.column_stack([r, e1, e2])
    delta = float((r @ n) ** 2)
    lhs = abs(float(np.linalg.det(F.T @ M @ F)))
    rhs = abs(float(np.linalg.det(M))) * delta
    active_det_err = max(active_det_err, abs(lhs - rhs))

print(f"packet_identity_max_abs_error={packet_err:.17g}")
print(f"active_det_identity_max_abs_error={active_det_err:.17g}")
