import math
import numpy as np

rng = np.random.default_rng(20260923)
max_rel = 0.0
cases = 0
for m in [2, 3, 5, 10, 30]:
    for _ in range(500):
        M = rng.normal(size=(2, m))
        lhs = float(np.linalg.det(M @ M.T))
        rhs = 0.0
        for i in range(m):
            for j in range(i + 1, m):
                rhs += float(np.linalg.det(M[:, [i, j]]) ** 2)
        rel = abs(lhs - rhs) / max(1.0, abs(lhs), abs(rhs))
        max_rel = max(max_rel, rel)
        cases += 1

print(f"cases={cases}")
print(f"max_relative_cauchy_binet_error={max_rel:.17g}")
print(f"pi_e={math.pi * math.e:.15f}")
print(f"two_pi={2 * math.pi:.15f}")
print(f"ratio_pi_e_to_two_pi={(math.e / 2):.15f}")
print("STATUS=PASS" if max_rel < 1e-12 else "STATUS=FAIL")
