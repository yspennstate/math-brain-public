import math
import numpy as np

rng = np.random.default_rng(20260924)
max_mixed = 0.0
max_det = 0.0
max_balance_rel = 0.0

for _ in range(10000):
    ang = rng.uniform(-math.pi, math.pi)
    v = np.array([math.cos(ang), math.sin(ang)])
    w = np.array([-math.sin(ang), math.cos(ang)])
    theta = rng.normal()
    if abs(theta) < 0.1:
        theta += 0.2 if theta >= 0 else -0.2

    P = theta * np.outer(v, v)
    c = rng.normal(size=2)
    khh = rng.normal()
    K = np.block([[P, c[:, None]], [c[None, :], np.array([[khh]])]])

    m = 5
    M = rng.normal(size=(2, m))
    t = rng.normal(size=m)

    R = []
    Rpred = []
    for p in range(m):
        block = np.block([
            [P, M[:, p, None]],
            [c[None, :], np.array([[t[p]]])],
        ])
        R.append(np.linalg.det(block))
        Rpred.append(-theta * np.dot(c, w) * np.dot(w, M[:, p]))

    R = np.asarray(R)
    Rpred = np.asarray(Rpred)
    max_mixed = max(max_mixed, float(np.max(np.abs(R - Rpred))))

    det_pred = -theta * np.dot(c, w) ** 2
    max_det = max(max_det, abs(float(np.linalg.det(K) - det_pred)))

    rho = float(np.linalg.norm(R))
    d = abs(float(np.linalg.det(K)))
    q = math.sqrt(float(np.dot(c, w) ** 2 + np.linalg.norm(M.T @ w) ** 2))
    lhs = (abs(theta) * q) ** 2
    if rho > 1e-10 and d > 1e-10:
        rhs = abs(theta) * (d + rho * rho / d)
        max_balance_rel = max(max_balance_rel, abs(lhs - rhs) / max(1.0, abs(lhs), abs(rhs)))

print({
    "trials": 10000,
    "max_mixed_factorization_abs_error": max_mixed,
    "max_hub_determinant_abs_error": max_det,
    "max_balance_relative_error": max_balance_rel,
})
