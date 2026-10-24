import math
import numpy as np

rng = np.random.default_rng(2026092403)

# Check Lemma 2.1 on dense random symmetric matrices.
dense_cases = 0
max_violation = 0.0
min_margin = float('inf')
for n in range(5, 16):
    for _ in range(300):
        G0 = rng.normal(size=(n, n))
        A = (G0 + G0.T) / 2
        vals, vecs = np.linalg.eigh(A)
        order = np.argsort(np.abs(vals))[::-1]
        vals = vals[order]
        vecs = vecs[:, order]
        ss = np.abs(vals)
        L = ss[2]
        s4 = ss[3]
        U = vecs[:, :3]
        for i in rng.choice(n, size=min(3, n), replace=False):
            p = float(U[i] @ U[i])
            C = np.delete(np.delete(A, i, axis=0), i, axis=1)
            s3c = float(np.linalg.svd(C, compute_uv=False)[2])
            rhs = (1 - p) * L - s4
            margin = s3c - rhs
            min_margin = min(min_margin, margin)
            max_violation = max(max_violation, max(0.0, -margin))
            dense_cases += 1

# Exact-rank-three stress: check s3(child) >= (1-p)L.
exact_cases = 0
min_exact_margin = float('inf')
for n in range(4, 20):
    for _ in range(200):
        H = rng.normal(size=(n, 3))
        U, _ = np.linalg.qr(H)
        lam = (1 + 4 * rng.random(3)) * rng.choice([-1, 1], size=3)
        A0 = U @ np.diag(lam) @ U.T
        L = float(np.min(np.abs(lam)))
        for i in rng.choice(n, size=min(3, n), replace=False):
            p = float(U[i] @ U[i])
            C = np.delete(np.delete(A0, i, axis=0), i, axis=1)
            s3c = float(np.linalg.svd(C, compute_uv=False)[2])
            min_exact_margin = min(min_exact_margin, s3c - (1 - p) * L)
            exact_cases += 1

mu = 1 / 48
theta = 1 / 64
delta = 1 - mu - theta
CR = 288 * math.sqrt(3 * math.e) / 13

assert max_violation < 1e-10
assert dense_cases == 9900
assert exact_cases == 9600
assert abs(delta - 185 / 192) < 1e-15

print('QFORM_B08_R49_RANK4_SPILL_CHECK_PASS')
print('dense_cases', dense_cases)
print('dense_max_violation', max_violation)
print('dense_min_margin', min_margin)
print('exact_rank3_cases', exact_cases)
print('exact_rank3_min_margin', min_exact_margin)
print('delta', delta)
print('CR', CR)
print('global_payment_constant', CR / delta)
print('partner_payment_constant', 64 / theta)
print('child_witness', theta / 512)
print('global_witness', delta / 512)
