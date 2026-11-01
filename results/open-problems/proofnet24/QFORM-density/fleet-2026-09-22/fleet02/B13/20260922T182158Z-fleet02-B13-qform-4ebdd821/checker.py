import math
import numpy as np

SEED = 20260922182158
rng = np.random.default_rng(SEED)
tau = 0.3
max_sg_err = 0.0
max_e2_err = 0.0
branch_cases = 0
pair_fail = 0

for _ in range(10000):
    n = int(rng.integers(3, 61))
    raw = rng.normal(size=(n, 3))
    R, _ = np.linalg.qr(raw)
    R = R[:, :3]
    c = np.sum(R * R, axis=1)
    H = np.where(c > tau)[0]
    L = np.where(c <= tau)[0]
    S = R[L].T @ R[L] if len(L) else np.zeros((3, 3))
    G = R[H].T @ R[H] if len(H) else np.zeros((3, 3))
    max_sg_err = max(max_sg_err, float(np.max(np.abs(S + G - np.eye(3)))))
    eigS = np.linalg.eigvalsh(S)[::-1]
    eigG = np.linalg.eigvalsh(G)[::-1]
    e2 = eigG[0]*eigG[1] + eigG[0]*eigG[2] + eigG[1]*eigG[2]
    wedges = 0.0
    max_delta = 0.0
    for a in range(len(H)):
        ri = R[H[a]]
        for b in range(a + 1, len(H)):
            rj = R[H[b]]
            delta = float(np.dot(ri, ri)*np.dot(rj, rj) - np.dot(ri, rj)**2)
            wedges += delta
            max_delta = max(max_delta, delta)
    max_e2_err = max(max_e2_err, abs(e2 - wedges))
    if eigS[1] <= 0.6 + 1e-12:
        branch_cases += 1
        if max_delta + 1e-12 < 1/225:
            pair_fail += 1

maxentry_fail = 0
min_ratio = float('inf')
for _ in range(20000):
    vals = np.array([rng.choice([-1, 1])*(1 + 4*rng.random()) for _ in range(3)])
    z = rng.normal(size=(3, 3))
    O, _ = np.linalg.qr(z)
    Lam = O @ np.diag(vals) @ O.T
    ri = rng.normal(size=3)
    rj = rng.normal(size=3)
    ri = ri / max(1.0, np.linalg.norm(ri)) * math.sqrt(rng.random())
    rj = rj / max(1.0, np.linalg.norm(rj)) * math.sqrt(rng.random())
    delta = float(np.dot(ri, ri)*np.dot(rj, rj) - np.dot(ri, rj)**2)
    if delta < 1e-12:
        continue
    a = float(ri @ Lam @ ri)
    b = float(ri @ Lam @ rj)
    c = float(rj @ Lam @ rj)
    ratio = max(abs(a), abs(b), abs(c))/(delta/4)
    min_ratio = min(min_ratio, ratio)
    if ratio < 1 - 1e-10:
        maxentry_fail += 1

Cagg = 43.323633263897
print(f'SEED={SEED}')
print('PARSEVAL_FRAMES=10000')
print(f'S2_LE_3_OVER_5_CASES={branch_cases}')
print(f'MAX_S_PLUS_G_ERROR={max_sg_err:.17g}')
print(f'MAX_E2_CAUCHY_BINET_ERROR={max_e2_err:.17g}')
print(f'HEAVY_PAIR_DELTA_BOUND_FAILURES={pair_fail}')
print('MAXENTRY_TESTS=20000')
print(f'MAXENTRY_DELTA_OVER_4_FAILURES={maxentry_fail}')
print(f'MIN_OBSERVED_MAXENTRY_RATIO={min_ratio:.15g}')
print(f'DIFFUSE_CAP_5E={5*math.e:.15g}')
print(f'PIVOT_CAP={128*(6000**0.25):.15g}')
print(f'NEAR_NULL_CAP={Cagg*math.sqrt(2)*15:.15g}')
print(f'PARTNER_ZERO_PAIR_CAP_D_GE_1_OVER_225={2*math.sqrt(math.e)*math.sqrt(15):.15g}')
status = 'PASS' if pair_fail == 0 and maxentry_fail == 0 else 'FAIL'
print(f'STATUS={status}')
