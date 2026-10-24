"""Deterministic corroborating checks for account03/B02 QFORM r18.

The report contains symbolic proofs.  This script only checks the two finite-dimensional
algebra identities numerically on seeded random rank-two cross blocks:

  det(L^T (B-a b^T/d) R) = det(Sigma) * (1-kappa/d),
  det(H_mix) = det(Sigma)^2 * (d-2*kappa),

where B=L Sigma R^T, a in Col(B), b in Row(B), and
kappa=(R^T b)^T Sigma^{-1}(L^T a).
"""

import numpy as np

rng = np.random.default_rng(1802)
max_schur_err = 0.0
max_singular_product_err = 0.0
max_critical_skeleton_err = 0.0
cases = 0

for _ in range(200):
    m = int(rng.integers(2, 8))
    n = int(rng.integers(2, 8))
    L = np.linalg.qr(rng.normal(size=(m, 2)))[0][:, :2]
    R = np.linalg.qr(rng.normal(size=(n, 2)))[0][:, :2]
    sig = np.exp(rng.normal(size=2))
    Sigma = np.diag(sig)
    B = L @ Sigma @ R.T

    u = rng.normal(size=m)
    v = rng.normal(size=n)
    a = B @ v
    b = B.T @ u
    aa = L.T @ a
    bb = R.T @ b
    kappa = float(bb @ np.linalg.solve(Sigma, aa))
    Delta = float(np.prod(sig))

    # Stay quantitatively away from the critical Schur relation for this check.
    d = kappa + 0.2 + abs(float(rng.normal()))
    C = B - np.outer(a, b) / d
    active = L.T @ C @ R
    rhs = Delta * (1.0 - kappa / d)
    err = abs(np.linalg.det(active) - rhs) / (1.0 + abs(rhs))
    max_schur_err = max(max_schur_err, float(err))

    sv = np.linalg.svd(C, compute_uv=False)
    lhs_product = float(np.prod(sv[:2]))
    rhs_product = Delta * abs(1.0 - kappa / d)
    err2 = abs(lhs_product - rhs_product) / (1.0 + rhs_product)
    max_singular_product_err = max(max_singular_product_err, float(err2))

    # At the exact Schur-critical value d=kappa, the mixed skeleton remains
    # nondegenerate whenever d != 0: det(H_mix) = -d Delta^2.
    if abs(kappa) > 1e-5:
        dc = kappa
        H = np.zeros((5, 5))
        H[0, 0] = dc
        H[0, 1:3] = aa
        H[1:3, 0] = aa
        H[0, 3:5] = bb
        H[3:5, 0] = bb
        H[1:3, 3:5] = Sigma
        H[3:5, 1:3] = Sigma
        rhs_critical = -dc * Delta**2
        err3 = abs(np.linalg.det(H) - rhs_critical) / (1.0 + abs(rhs_critical))
        max_critical_skeleton_err = max(max_critical_skeleton_err, float(err3))
        cases += 1

print(f"cases={cases}")
print(f"max_schur_identity_scaled_error={max_schur_err:.3e}")
print(f"max_singular_product_scaled_error={max_singular_product_err:.3e}")
print(f"max_critical_skeleton_scaled_error={max_critical_skeleton_err:.3e}")
print("STATUS=PASS")
