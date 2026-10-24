"""Check the count-splitting DP against brute force over all binary trees (n = 4, 5, 6)."""
import time
import numpy as np
import wlib as W, countsplit as CS, csdp
from exhaustive_small import all_trees
W.set_polite()
rng = np.random.default_rng(5)
worst = 0.0
for n, reps in ((4, 30), (5, 12), (6, 3)):
    trees = list(all_trees(range(n)))
    for r in range(reps):
        tt = rng.choice(np.array([-1, 1], dtype=np.int8), size=1 << n)
        if r % 2:
            tt = np.where(rng.uniform(size=1 << n) < 0.15, -1, 1).astype(np.int8)
        p = W.spectrum(tt)
        bf = min(CS.cs_cost(p, n, t) for t in trees)
        dp, t = csdp.cs_opt(p, n)
        worst = max(worst, abs(bf - dp))
    print(f"n={n}: trees={len(trees)} max|bruteforce - dp| = {worst:.3e}", flush=True)
t0 = time.time(); p = W.spectrum(W.fam_majority(13)); v, t = csdp.cs_opt(p, 13)
print(f"maj13 CSopt={v:.6f} H={W.H_of(p):.6f}  [{time.time()-t0:.1f}s]")
