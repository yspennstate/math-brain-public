import numpy as np
import math

rng = np.random.default_rng(20260923)

rank_tests = 0
rank_min_gap = float("inf")
for m in range(4, 11):
    for r in range(1, m - 2):
        for _ in range(200):
            M = rng.normal(size=(m, m)); M = (M + M.T) / 2
            U = rng.normal(size=(m, r))
            C = rng.normal(size=(r, r)); C = (C + C.T) / 2
            R = U @ C @ U.T
            sm = np.linalg.svd(M, compute_uv=False)
            sn = np.linalg.svd(M + R, compute_uv=False)
            gap = sn[2] - sm[2 + r]
            rank_min_gap = min(rank_min_gap, float(gap))
            assert gap >= -1e-9
            rank_tests += 1

threshold_tests = 0
threshold_min_margin = 999
for m in range(3, 10):
    for _ in range(1000):
        B0 = rng.normal(size=(m, m)); B0 = (B0 + B0.T) / 2
        T = rng.normal(size=(m, m)); T = (T + T.T) / 2
        op = np.linalg.norm(T, 2); delta = rng.uniform(0, 0.5)
        if op:
            T = T * (delta / op)
        E = rng.normal(size=(m, m)); E = (E + E.T) / 2
        L = rng.uniform(0.1, 1.5)
        p0 = int((np.linalg.eigvalsh(B0) >= L + delta - 1e-10).sum())
        hostile = int((np.linalg.eigvalsh(E) < -1e-10).sum())
        actual = int((np.linalg.eigvalsh(B0 + T + E) >= L - 1e-10).sum())
        margin = actual - (p0 - hostile)
        threshold_min_margin = min(threshold_min_margin, margin)
        assert margin >= 0
        threshold_tests += 1

print(f"rank_tests={rank_tests}")
print(f"rank_min_gap={rank_min_gap:.16g}")
print(f"threshold_tests={threshold_tests}")
print(f"threshold_min_integer_margin={threshold_min_margin}")
print(f"rank1_m4_density_constant={4*math.sqrt(6*math.pi):.15f}")
print(f"helpful_m3_density_constant={6*math.sqrt(math.pi):.15f}")
print("PASS")
