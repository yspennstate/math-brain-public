"""Annealing that tries to BREAK the lemmas of Theorem B: maximise max_i (P1 ratio), max_i (P2 ratio),
or Sigma/(L I) over LTFs (real weights, threshold).  Any value > 1 would refute the proof.
Usage: python adversarial_rank.py key seed restarts steps   (key in p1, p2, sig)"""
import sys, math
import numpy as np
from check_rank import analyse

key = sys.argv[1]; seed = int(sys.argv[2]); R = int(sys.argv[3]); ST = int(sys.argv[4])
rng = np.random.default_rng(seed)
best = (0, None)
for r in range(R):
    n = int(rng.integers(3, 13))
    lw = rng.normal(0, 1.0, n)
    th = rng.normal() * 1.0
    def val(lw, th):
        w = np.exp(lw)
        res = analyse(w, th * np.linalg.norm(w) + 1e-9)
        return -1 if res is None else res[key]
    cur = val(lw, th)
    T = 0.05
    for s in range(ST):
        lw2 = lw.copy(); th2 = th
        m = rng.integers(3)
        if m == 0:
            lw2[rng.integers(n)] += rng.normal(0, 0.5)
        elif m == 1:
            th2 = th + rng.normal(0, 0.2)
        else:
            j = rng.integers(n); k = rng.integers(n); lw2[j] = lw2[k] + rng.normal(0, 0.05)
        v = val(lw2, th2)
        if v > cur or rng.random() < math.exp((v - cur) / T):
            lw, th, cur = lw2, th2, v
        T *= 0.99
        if cur > best[0]:
            best = (cur, (np.round(np.exp(lw), 4).tolist(), round(th, 4)))
    print("restart %d n=%d %s=%.4f" % (r, n, key, cur), flush=True)
print("BEST %s = %.5f at %s" % (key, best[0], best[1]), flush=True)
