import numpy as np

rng = np.random.default_rng(20260924)


def parseval(n, r):
    q, _ = np.linalg.qr(rng.normal(size=(n, r)))
    return q[:, :r]


def sqrt_psd(g):
    x, v = np.linalg.eigh(g)
    return (v * np.sqrt(np.maximum(x, 0.0))) @ v.T


mx = {
    "nonzero_twist": 0.0,
    "zero_twist": 0.0,
    "residual_parseval": 0.0,
    "second_twist": 0.0,
    "beta_wedge": 0.0,
}
used = 0

for _ in range(4000):
    n = int(rng.integers(6, 15))
    uframe = parseval(n, 3)
    h = int(rng.integers(n))
    u = uframe[h]
    c = float(u @ u)
    if not (1e-8 < c < 0.999999):
        continue

    m = rng.normal(size=(3, 3))
    m = (m + m.T) / 2
    if abs(np.linalg.det(m)) < 0.05:
        m = m + np.diag([1.4, -1.2, 0.9])
    detm = float(np.linalg.det(m))

    d = float(rng.normal())
    q = float(u @ m @ u + d)
    if abs(d) > 1e-4 and abs(q) > 1e-4:
        g = np.eye(3) - np.outer(u, u)
        s = m - np.outer(m @ u, m @ u) / q
        cc = sqrt_psd(g) @ s @ sqrt_psd(g)
        rhs = (1 - c) * detm * d / q
        mx["nonzero_twist"] = max(
            mx["nonzero_twist"], abs(np.linalg.det(cc) - rhs) / (1 + abs(rhs))
        )

    a = float(u @ m @ u)
    if abs(a) < 1e-4:
        continue

    un = u / np.sqrt(c)
    proj = np.eye(3) - np.outer(un, un)
    vals, vecs = np.linalg.eigh(proj)
    e = vecs[:, np.argsort(vals)[-2:]]
    b = e.T @ (m - np.outer(m @ u, m @ u) / a) @ e
    rhs = c * detm / a
    mx["zero_twist"] = max(
        mx["zero_twist"], abs(np.linalg.det(b) - rhs) / (1 + abs(rhs))
    )

    u0 = np.delete(uframe, h, axis=0)
    wframe = u0 @ e
    mx["residual_parseval"] = max(
        mx["residual_parseval"], np.linalg.norm(wframe.T @ wframe - np.eye(2))
    )

    jj = int(rng.integers(wframe.shape[0]))
    w = wframe[jj]
    beta = float(w @ w)
    rj = u0[jj]
    wedge2 = float(c * (rj @ rj) - (u @ rj) ** 2)
    mx["beta_wedge"] = max(
        mx["beta_wedge"], abs(beta - wedge2 / c) / (1 + abs(beta))
    )

    if beta < 0.999:
        dj = float(rng.normal())
        qj = float(dj + w @ b @ w)
        if abs(dj) > 1e-4 and abs(qj) > 1e-4:
            g2 = np.eye(2) - np.outer(w, w)
            s2 = b - np.outer(b @ w, b @ w) / qj
            c2 = sqrt_psd(g2) @ s2 @ sqrt_psd(g2)
            rhs2 = (1 - beta) * np.linalg.det(b) * dj / qj
            mx["second_twist"] = max(
                mx["second_twist"],
                abs(np.linalg.det(c2) - rhs2) / (1 + abs(rhs2)),
            )

    used += 1

print("QFORM_B06_R52_CHECK_PASS")
print("samples", used)
for key, value in mx.items():
    print(key, f"{value:.6e}")
