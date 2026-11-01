import math
import numpy as np

# Regression only; the proof is analytic in REPORT.md.
rng = np.random.default_rng(20260923)
violations = 0
checked = 0
worst_ratio = float('inf')
worst = None
for _ in range(300000):
    mags = np.exp(rng.uniform(0.0, math.log(30.0), 3))
    signs = np.array([1.0, 1.0, -1.0])
    rng.shuffle(signs)
    eig = mags * signs
    O, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    Lam = O @ np.diag(eig) @ O.T
    e = rng.normal(size=3)
    e /= np.linalg.norm(e)
    alpha = float(e @ Lam @ e)
    if abs(alpha) >= 1/16:
        continue
    u = rng.normal(size=3)
    u /= np.linalg.norm(u)
    u *= rng.random() ** (1/3)
    x = float(e @ u)
    y = u - x * e
    h = float(y @ y)
    if h < 1/4:
        continue
    checked += 1
    b = float(e @ Lam @ u)
    q = float(u @ Lam @ u)
    ratio = max(abs(b)/(1/32), abs(q)/(1/128))
    if ratio < worst_ratio:
        worst_ratio = ratio
        worst = (alpha, h, b, q, eig.tolist())
    if abs(b) < 1/32 and abs(q) < 1/128:
        violations += 1
        break

scalar_bound = 128 * 512 ** 0.25
pair_bound = 64 * 2 ** 0.75
print('checked_near_null_transverse_rows', checked)
print('violations', violations)
print('minimum_threshold_ratio_seen', worst_ratio)
print('worst_fixture', worst)
print('scalar_branch_bound', scalar_bound)
print('pair_branch_bound', pair_bound)
print('diffuse_c_le_7_8', 6*math.e)
print('delete_diffuse_c_le_7_8', 12*math.e)
