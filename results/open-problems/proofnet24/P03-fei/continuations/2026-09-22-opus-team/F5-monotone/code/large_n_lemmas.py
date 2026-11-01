"""Lemmas of Theorem 1 on structured LTFs with n = 16..22 (value/bound ratios; each must be <= 1)."""
import numpy as np, math, time
from check_rank import analyse
fib = [1.0, 1.0]
while len(fib) < 22: fib.append(fib[-1] + fib[-2])
fams = [
 ("majority n=21", np.ones(21), 0.0),
 ("AND n=20", np.ones(20), 19.0 - 1e-9 + 0.5),
 ("threshold k=3 of n=20 (<3 of the -1s)", np.ones(20), 20 - 2*3 + 1.0),
 ("chain 2^-j n=18, mid", 2.0 ** -np.arange(18), 1e-7),
 ("chain 2^-j n=18, rare", 2.0 ** -np.arange(18), 2.0 - 2.0**-15 - 1e-9),
 ("power law j^-0.5 n=20 theta=0", np.arange(1, 21) ** -0.5, 1e-7),
 ("power law j^-0.5 n=20 theta=2 sigma", np.arange(1, 21) ** -0.5, 2 * np.linalg.norm(np.arange(1, 21) ** -0.5)),
 ("heavy 3 x 5 + 17 x 1, theta=0", np.array([5.0] * 3 + [1.0] * 17), 1e-7),
 ("heavy 3 x 5 + 17 x 1, theta=7", np.array([5.0] * 3 + [1.0] * 17), 7.0 + 1e-7),
 ("Fibonacci n=20, theta=0.4 sum", np.array(fib[:20]), 0.4 * sum(fib[:20]) + 1e-7),
 ("weights 1..20, theta=60.5", np.arange(1.0, 21.0), 60.5),
 ("gaussian n=22", np.abs(np.random.default_rng(0).standard_normal(22)), 1.3),
]
for name, w, th in fams:
    t = time.time()
    r = analyse(w, th)
    print("%-42s H/I=%.4f  L2=%.3f L3=%.3f L4=%.3f L5=%.3f L6=%.3f Thm=%.3f  (%.0fs)" % (
        name, r['ratio'], r['p1'], r['p2'], r['sig'], r['lev'], r['cond'], r['tot'], time.time() - t), flush=True)
