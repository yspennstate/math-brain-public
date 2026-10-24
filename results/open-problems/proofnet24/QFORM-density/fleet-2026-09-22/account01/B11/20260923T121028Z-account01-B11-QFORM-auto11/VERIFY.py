import math
import numpy as np

rng = np.random.default_rng(20260923)
alpha = 0.5
threshold = alpha / 32.0
checked = 0

for _ in range(50):
    n = 600
    R, _ = np.linalg.qr(rng.normal(size=(n, 3)))
    O, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    ev = np.array([1.0 + rng.random(), 1.0 + rng.random(), -(1.0 + rng.random())])
    M = O @ np.diag(ev) @ O.T
    s = np.min(np.abs(ev))
    lev = np.sum(R * R, axis=1)
    D = np.flatnonzero(lev <= threshold)
    if len(D) < 3:
        continue
    G = R[D].T @ R[D]
    if np.min(np.linalg.eigvalsh(G)) < alpha:
        continue
    w, V = np.linalg.eigh(G)
    Ghalf = V @ np.diag(np.sqrt(w)) @ V.T
    MD = Ghalf @ M @ Ghalf
    assert np.min(np.abs(np.linalg.eigvalsh(MD))) >= alpha * s - 1e-10
    P = R[D] @ np.linalg.inv(G) @ R[D].T
    assert np.max(np.diag(P)) <= 1.0 / 32.0 + 1e-10
    checked += 1

assert checked > 0
Csw = 288 * math.sqrt(3 * math.e) / 13
partner = 24 * math.sqrt(math.pi) / (math.sqrt(17) - 1)
print('checked_diffuse_cases', checked)
print('C_sw', Csw)
print('alpha_half_bound', 2*Csw)
print('partner_bound', partner)
print('QFORM_B11_HEAVY_OR_DIFFUSE_CHECK_PASS')
