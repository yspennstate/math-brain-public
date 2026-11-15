"""Paper 7 Thm exactmoments: independent Monte Carlo of T m10, H m10, H m12, and p_T(12123434) = 9/20."""
import numpy as np, time
from p8_moment_mc import pairings, vol
rng = np.random.default_rng(2026)
t0 = time.time()
p, se = vol([(1, 3), (2, 4), (5, 7), (6, 8)], 8, "T", 4_000_000, rng)
print(f"12123434: {p:.4f} +- {se:.4f} (9/20 = 0.45)", flush=True)
for k, kind, N, target in ((5, "H", 1_000_000, 2717/36), (6, "H", 500_000, 1052/3), (5, "T", 1_000_000, 415.0)):
    tot = var = 0.0
    for pr in pairings(list(range(1, 2 * k + 1))):
        q, s = vol(pr, 2 * k, kind, N, rng); tot += q; var += s * s
    print(f"{kind} m_{2*k} = {tot:.3f} +- {var**0.5:.3f}  paper {target:.3f}  ({time.time()-t0:.0f} s)", flush=True)
