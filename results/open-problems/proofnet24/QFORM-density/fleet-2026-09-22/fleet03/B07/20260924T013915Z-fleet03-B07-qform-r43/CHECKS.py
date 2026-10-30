import itertools
import math
import numpy as np

rng = np.random.default_rng(20260924)
ETA = 2.0**-30
ZETA = 2.0**-12

def elementary(vals, k):
    ans = 0.0
    for I in itertools.combinations(range(len(vals)), k):
        p = 1.0
        for i in I:
            p *= vals[i]
        ans += p
    return ans

def e23(M):
    vals = np.linalg.eigvalsh((M + M.T) / 2.0)
    vals = np.maximum(vals, 0.0)
    return elementary(vals, 2), elementary(vals, 3), vals

max_newton_rel = 0.0
max_update_violation = 0.0
max_loewner_violation = 0.0
heavy_max = 0
trials = 0

for _ in range(800):
    m = int(rng.integers(3, 9))
    n = int(rng.integers(2, 9))
    p = int(rng.integers(1, 5))
    K = rng.normal(size=(m, n))
    U = rng.normal(size=(m, p))
    B = K @ K.T
    Z, E3, _ = e23(B)
    if Z < 1e-9:
        continue
    H2 = B @ B - np.trace(B) * B + Z * np.eye(m)
    x, W = np.linalg.eigh(B)
    x = np.maximum(x, 0.0)
    alpha = x * (x.sum() - x) / Z
    h_formula = Z * (1.0 - alpha)
    h_eval = np.diag(W.T @ H2 @ W)
    max_newton_rel = max(
        max_newton_rel,
        float(np.max(np.abs(h_eval - h_formula)) / (1.0 + np.max(np.abs(h_formula)))),
    )
    heavy = alpha > 2.0 / 3.0 + 1e-12
    heavy_max = max(heavy_max, int(heavy.sum()))
    P = W[:, heavy] @ W[:, heavy].T if heavy.any() else np.zeros((m, m))
    min_eig = np.linalg.eigvalsh(H2 - (Z / 3.0) * (np.eye(m) - P)).min()
    max_loewner_violation = max(max_loewner_violation, max(0.0, float(-min_eig)))
    _, E3_aug, _ = e23(B + U @ U.T)
    one_U = float(np.trace(U.T @ H2 @ U))
    max_update_violation = max(
        max_update_violation, max(0.0, one_U - (E3_aug - E3))
    )
    trials += 1

sync_trials = 0
max_sync_ratio = 0.0
for _ in range(500):
    m = n = 6
    p = 5
    x = np.array([
        1.0,
        3.0e-4,
        10.0 ** rng.uniform(-12, -9),
        10.0 ** rng.uniform(-12, -9),
        0.0,
        0.0,
    ])
    Ql, _ = np.linalg.qr(rng.normal(size=(m, m)))
    Qr, _ = np.linalg.qr(rng.normal(size=(n, n)))
    K = Ql @ np.diag(np.sqrt(x)) @ Qr.T
    B = K @ K.T
    Z, E3, _ = e23(B)
    if not (Z >= ZETA and E3 < ETA):
        continue
    lam, W = np.linalg.eigh(B)
    lam = np.maximum(lam, 0.0)
    alpha = lam * (lam.sum() - lam) / Z
    heavy = alpha > 2.0 / 3.0 + 1e-12
    P = W[:, heavy] @ W[:, heavy].T if heavy.any() else np.zeros((m, m))
    U0 = P @ rng.normal(size=(m, p))
    R = (np.eye(m) - P) @ rng.normal(size=(m, p))
    scale = 1e-5
    U = U0 + scale * R
    _, E3_aug, _ = e23(B + U @ U.T)
    while E3_aug >= ETA and scale > 1e-12:
        scale *= 0.3
        U = U0 + scale * R
        _, E3_aug, _ = e23(B + U @ U.T)
    if E3_aug >= ETA:
        continue
    tail2 = np.linalg.norm((np.eye(m) - P) @ U, "fro") ** 2
    limit = 3.0 * (ETA - E3) / Z
    max_sync_ratio = max(max_sync_ratio, tail2 / limit)
    sync_trials += 1

C3 = 3.0 * 2.0 ** (4.0 / 3.0) * math.e ** (1.0 / 3.0)
paid_bound = 32.0 * C3
plane_radius = math.sqrt(3.0 * ETA / ZETA)
skeleton_radius = math.sqrt(12.0 * ETA / ZETA)
d = 1.0 / 64.0
eps = 1.0 / 768.0
gamma = d - 3.0 * eps
partner_bound = 2.0 * math.sqrt(18.0 * math.pi) / gamma

assert heavy_max <= 2
assert max_newton_rel < 1e-11
assert max_update_violation < 1e-8
assert max_loewner_violation < 1e-10
assert sync_trials > 100
assert max_sync_ratio <= 1.0 + 1e-8
assert abs(plane_radius - math.sqrt(3.0) / 512.0) < 1e-15
assert abs(skeleton_radius - math.sqrt(12.0) / 512.0) < 1e-15
assert abs(gamma - 3.0 / 256.0) < 1e-15

print(f"general_trials={trials}")
print(f"heavy_max={heavy_max}")
print(f"max_newton_relative_error={max_newton_rel:.3e}")
print(f"max_extension_inequality_violation={max_update_violation:.3e}")
print(f"max_loewner_violation={max_loewner_violation:.3e}")
print(f"synchronization_trials={sync_trials}")
print(f"max_sync_tail_to_bound_ratio={max_sync_ratio:.6g}")
print(f"C3={C3:.15f}")
print(f"paid_E3_bound={paid_bound:.15f}")
print(f"one_side_plane_radius={plane_radius:.15f}")
print(f"rank12_skeleton_radius={skeleton_radius:.15f}")
print(f"partner_s3_lower_bound={gamma:.15f}")
print(f"partner_density_bound={partner_bound:.15f}")
print("STATUS=PASS")
