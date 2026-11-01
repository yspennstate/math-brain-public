import math
import numpy as np

rng = np.random.default_rng(20260924)
max_rel = 0.0
min_delta = float("inf")
for _ in range(1000):
    m = int(rng.integers(3, 13))
    M = rng.normal(size=(3, m))
    gram = M @ M.T
    delta = math.sqrt(max(float(np.linalg.det(gram)), 0.0))
    s = np.linalg.svd(M, compute_uv=False)
    prod3 = float(np.prod(s[:3]))
    rel = abs(delta - prod3) / max(1.0, abs(delta), abs(prod3))
    max_rel = max(max_rel, rel)
    min_delta = min(min_delta, delta)

c_l1 = 6.0 * math.sqrt(2.0) * math.pi
c_density = 3.0 * math.sqrt(2.0)
c_hybrid = 2.0 ** (49.0 / 24.0) * 3.0 ** 0.25

assert max_rel < 1e-11
assert abs(c_l1 - 26.6572976289502) < 1e-12
assert abs(c_density - 4.242640687119286) < 1e-12
assert abs(c_hybrid - 5.418551700481505) < 1e-12

print("QFORM_B02_R42_THREE_LEAF_CHECK_PASS")
print(f"trials=1000")
print(f"max_relative_gram_svd_error={max_rel:.17g}")
print(f"min_sampled_delta={min_delta:.17g}")
print(f"l1_constant={c_l1:.15f}")
print(f"density_constant={c_density:.15f}")
print(f"partner_hybrid_constant={c_hybrid:.15f}")
