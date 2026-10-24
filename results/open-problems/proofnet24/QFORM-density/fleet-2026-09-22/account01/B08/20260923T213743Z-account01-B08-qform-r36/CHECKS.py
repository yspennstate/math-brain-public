import math
import numpy as np

rng = np.random.default_rng(20260923)
violations = 0
tested = 0
min_slack = float('inf')

for n in (5, 7, 10, 15):
    for rep in range(500):
        G = rng.normal(size=(n, n))
        A = (G + G.T) / 2
        vals, vecs = np.linalg.eigh(A)
        idx = np.argsort(np.abs(vals))[::-1][:3]
        lam = vals[idx]
        R = vecs[:, idx]
        L = float(np.min(np.abs(lam)))
        i = int(rng.integers(n))
        p = float(np.sum(R[i, :] ** 2))
        keep = [j for j in range(n) if j != i]
        C = A[np.ix_(keep, keep)]
        b = A[keep, i]
        cv, cu = np.linalg.eigh(C)
        order = np.argsort(np.abs(cv))[::-1]
        U = cu[:, order[:2]]
        s3 = abs(cv[order[2]]) if len(cv) >= 3 else 0.0
        x = s3 / L
        if x < 1 - 1e-10 and p > 1e-12:
            r = b - U @ (U.T @ b)
            tau = float(np.linalg.norm(r))
            rhs = (1 - x) * math.sqrt((1 - p) / p) * L
            slack = tau - rhs
            tested += 1
            min_slack = min(min_slack, slack)
            if slack < -1e-8:
                violations += 1

sigma = math.sqrt(47 / 48)
tau0 = (129 / 130) * math.sqrt(47)
kappa0 = tau0 * sigma / (2 * math.sqrt(16 * tau0 * tau0 + sigma * sigma))
density_constant = 24 * math.sqrt(3) * math.e / (5 * kappa0)

print('QFORM_B08_R36_TRANSVERSE_AMPLIFICATION_CHECK')
print('tested', tested)
print('violations', violations)
print('min_slack', min_slack)
print('sigma', sigma)
print('tau0', tau0)
print('kappa0', kappa0)
print('kappa0_over_16', kappa0 / 16)
print('one_over_130', 1 / 130)
print('density_constant', density_constant)
assert violations == 0
assert 1 / 130 < kappa0 / 16
assert density_constant < 183
print('QFORM_B08_R36_CHECK_PASS')
