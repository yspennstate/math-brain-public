"""Rerun of Toeplitz m_10 (paper 7 says 415) with fresh seeds; first run gave 415.052 +- 0.014."""
import numpy as np, time
from p8_moment_mc import pairings, vol
if __name__ == "__main__":
    t0 = time.time()
    for seed in (91, 92):
        rng = np.random.default_rng(seed)
        tot = var = 0.0
        for pr in pairings(list(range(1, 11))):
            q, s = vol(pr, 10, "T", 2_000_000, rng); tot += q; var += s * s
        print(f"seed {seed}: T m_10 = {tot:.4f} +- {var**0.5:.4f}  ({time.time()-t0:.0f} s)", flush=True)
