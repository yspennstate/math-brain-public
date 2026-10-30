"""Candidate limit for phi = n * angle at depth s = l/n: d phi = -phi^2/(3 pi) ds + sigma phi dB (Ito), started from the
deterministic 3 pi / s0 at s0 = 0.005. Prints quantiles at s = 0.25, 0.5, 1, 2 for sigma^2 values, to set beside
two_input_run1.txt. usage: python -X utf8 sde_check.py sig2a,sig2b"""
import sys
import numpy as np
rng = np.random.default_rng(7); N = 40000; ds = 2e-4
for s2 in [float(v) for v in sys.argv[1].split(",")]:
    s = 0.005; lp = np.full(N, np.log(3 * np.pi / s)); marks = [0.25, 0.5, 1.0, 2.0]; k = 0
    while k < len(marks):
        p = np.exp(lp)
        lp += (-p / (3 * np.pi) - s2 / 2) * ds + np.sqrt(s2 * ds) * rng.standard_normal(N)   # Ito for log phi
        s += ds
        if s >= marks[k] - 1e-12:
            v = np.exp(lp); q = np.quantile(v, [0.1, 0.25, 0.5, 0.75, 0.9])
            print("sig2 %.2f s %.2f | quantiles %s | mean %.3f | mean log %.3f sd log %.3f"
                  % (s2, marks[k], " ".join("%.3f" % x for x in q), v.mean(), lp.mean(), lp.std()), flush=True)
            k += 1
