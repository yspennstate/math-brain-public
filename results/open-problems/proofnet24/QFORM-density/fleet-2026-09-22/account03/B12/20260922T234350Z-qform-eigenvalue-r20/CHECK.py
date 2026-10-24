import json
import math
import numpy as np

rng = np.random.default_rng(20260922)
violations = 0
min_margin = float("inf")

for _ in range(5000):
    Q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    vals = 1.0 + 3.0 * rng.random(3)
    vals *= rng.choice([-1.0, 1.0], 3)
    B = Q @ np.diag(vals) @ Q.T

    H = rng.normal(size=(3, 3))
    H = (H + H.T) / 2.0
    op = np.linalg.norm(H, 2)
    if op > 0:
        H *= 0.4 / op

    s0 = np.linalg.svd(B, compute_uv=False)[-1]
    s1 = np.linalg.svd(B + H, compute_uv=False)[-1]
    margin = s1 - (s0 - np.linalg.norm(H, 2))
    min_margin = min(min_margin, float(margin))
    if margin < -1e-10:
        violations += 1

out = {
    "seed": 20260922,
    "trials": 5000,
    "weyl_violations": violations,
    "minimum_numerical_margin": min_margin,
    "C_half": 6.0 * math.sqrt(math.e),
    "C_two_thirds": 9.0 * math.sqrt(3.0 * math.e),
    "C_two_thirds_half_gap": 18.0 * math.sqrt(3.0 * math.e),
    "principal_half_gap": 40.0,
}
print(json.dumps(out, indent=2, sort_keys=True))
