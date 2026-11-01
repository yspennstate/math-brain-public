import math
import numpy as np

rng = np.random.default_rng(20260923)
max_det_err = 0.0
max_lower_violation = 0.0
max_wedge_err = 0.0

for _ in range(20):
    nR, nL = 7, 5
    raw = rng.normal(size=(nR, 2))
    V, _ = np.linalg.qr(raw)
    v, q = V[:, 0], V[:, 1]
    beta = float(rng.normal())
    m = float(0.5 + 2.0 * rng.random())
    h = beta * v + m * q
    eta = v * v + q * q
    order = np.argsort(-eta)
    r = next(int(j) for j in order if abs(h[j]) > 1e-9)
    hr = h[r]

    u = rng.normal(size=nL)
    u /= np.linalg.norm(u)
    hL = rng.normal(size=nL)
    vm, qm, hm = np.delete(v, r), np.delete(q, r), np.delete(h, r)

    ell = np.concatenate([-(v[r] / hr) * hL,
                          vm - (v[r] / hr) * hm])
    uu = np.concatenate([u, np.zeros(nR - 1)])

    sigma = float(0.3 + 2.0 * rng.random())
    a = float((0.5 + 2.0 * rng.random()) * (1 if rng.random() < 0.5 else -1))
    c = a * sigma**2 * v[r]**2 / hr**2
    K = sigma * (np.outer(uu, ell) + np.outer(ell, uu)) - c * np.outer(uu, uu)

    ev = np.linalg.eigvalsh(K)
    nz = ev[np.abs(ev) > 1e-8]
    pdet = abs(float(np.prod(nz)))
    perp = ell - uu * np.dot(uu, ell)
    b = np.linalg.norm(perp)

    det_expected = sigma**2 * b**2
    lower = sigma**2 * m**2 * eta[r] / hr**2
    wedge = np.linalg.norm(q[r] * vm - v[r] * qm)**2

    max_det_err = max(max_det_err, abs(pdet - det_expected))
    max_lower_violation = max(max_lower_violation, max(0.0, lower - pdet))
    max_wedge_err = max(max_wedge_err, abs(wedge - eta[r]))

print(f"max_det_identity_abs_error={max_det_err:.3e}")
print(f"max_lower_bound_violation={max_lower_violation:.3e}")
print(f"max_wedge_identity_abs_error={max_wedge_err:.3e}")
print(f"C_rank2={16*math.sqrt(30):.15f}")
print(f"C_target={16*math.sqrt(60):.15f}")
print(f"C_time={16*math.sqrt(60*math.pi):.15f}")
print(f"C_theta_1_8={16*math.sqrt(480):.15f}")
