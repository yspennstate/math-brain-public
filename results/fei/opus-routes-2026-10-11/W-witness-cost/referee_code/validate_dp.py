"""Validate the convolution DP of check_TDL_large.rare_rank_dp against brute force over all owner gates."""
import random, math
import numpy as np
from check_TDL_large import rare_rank_dp, rare_rank_brute
rng = random.Random(4)
worst = 0.0; cases = 0
for trial in range(300):
    m = rng.randint(2, 6)
    widths = [rng.randint(1, 4) for _ in range(m)]
    j = rng.randint(1, m)
    wj = widths[j] if j < m else 0
    Sks = {}; Mk = np.zeros(j, dtype=np.int64)
    for k in range(j):
        if rng.random() < 0.5:
            w = widths[k]
            pos = sorted(rng.sample(range(1, w + 1), rng.randint(1, w)))
            Sks[k] = np.array(pos); Mk[k] = max(pos)
    if not Sks:
        continue
    s = sum(len(p) for p in Sks.values()) + rng.randint(1, 4)
    a1, b1 = rare_rank_dp(widths, j, Sks, Mk, wj, s)
    a2, b2 = rare_rank_brute(widths, j, Sks, Mk, wj, s)
    for v in Sks:
        worst = max(worst, float(np.max(np.abs(a1[v] - a2[v]))), float(np.max(np.abs(b1[v] - b2[v]))))
    cases += 1
print(f'{cases} random configurations: max |DP - brute force| = {worst:.3e}')
