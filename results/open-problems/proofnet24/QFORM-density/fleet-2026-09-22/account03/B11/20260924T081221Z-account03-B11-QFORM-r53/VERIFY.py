#!/usr/bin/env python3
import math
import numpy as np

rng = np.random.default_rng(20260924)
max_partner_rel = 0.0
max_area_rel = 0.0
tested = 0

for _ in range(20000):
    n = int(rng.integers(4, 11))
    G = rng.normal(size=(n, 3))
    R, _ = np.linalg.qr(G)
    lam = np.array([
        rng.uniform(1.0, 5.0),
        rng.uniform(1.0, 5.0),
        -rng.uniform(1.0, 5.0),
    ])
    if rng.random() < 0.5:
        lam = -lam
    M = np.diag(lam)
    A = R @ M @ R.T

    h = int(rng.integers(n))
    alpha = float(A[h, h])
    if abs(alpha) < 1e-5:
        continue

    idx = np.array([j for j in range(n) if j != h])
    c = A[idx, h]
    B = A[np.ix_(idx, idx)]
    S = B - np.outer(c, c) / alpha

    svals = np.linalg.svd(S, compute_uv=False)
    delta2 = float(svals[0] * svals[1])
    q = float(np.dot(R[h], R[h]))
    D = abs(float(np.prod(lam)))
    partner_rhs = q * D / abs(alpha)
    max_partner_rel = max(
        max_partner_rel,
        abs(delta2 - partner_rhs) / max(1.0, abs(partner_rhs)),
    )

    U, _, _ = np.linalg.svd(S)
    E = U[:, :2]
    L = E.T @ S
    area = math.sqrt(max(float(np.linalg.det(L @ L.T)), 0.0))
    max_area_rel = max(
        max_area_rel,
        abs(area - delta2) / max(1.0, abs(delta2)),
    )
    tested += 1

# Exact collar constants used in the report.
s = 1.0
q = 63.0 / 64.0
alpha = s / 64.0
D = s**3
partner_floor = q * D / alpha
cap_ceiling = 2.0 / partner_floor
reciprocal_ceiling = 2.0 * math.sqrt(2.0 * math.pi / partner_floor)

assert abs(partner_floor - 63.0) < 1e-14
assert abs(cap_ceiling - 2.0 / 63.0) < 1e-14
assert abs(reciprocal_ceiling - 2.0 * math.sqrt(2.0 * math.pi / 63.0)) < 1e-14
assert max_partner_rel < 1e-10
assert max_area_rel < 1e-10

print(f"tested={tested}")
print(f"max_partner_relative_error={max_partner_rel:.17g}")
print(f"max_area_relative_error={max_area_rel:.17g}")
print(f"collar_Delta2_floor={partner_floor:.17g}")
print(f"collar_density_cap_constant={cap_ceiling:.17g}")
print(f"collar_reciprocal_constant={reciprocal_ceiling:.17g}")
print("QFORM_B11_R53_SCHUR_DIFFERENCE_CHECK_PASS")
