"""A cleaner estimate of the symmetric two-sided decay exponent, over the range where the sampler's
1e15 ceiling cannot bite (N <= 1e12), against the candidate (1-c)^2."""
import numpy as np, sys
from h0024_fast import trial
trials = int(sys.argv[1]) if len(sys.argv) > 1 else 40000
rng = np.random.default_rng(23)
E = (3, 6, 9, 12)
print(f"{'c':>5} " + " ".join(f"{10**e:>8.0e}" for e in E) + f" {'exponent':>9} {'(1-c)^2':>8} {'ratio':>6}")
for c in (0.4, 0.5, 0.6, 0.7, 0.8, 0.9):
    p = [sum(1 for _ in range(trials) if trial(c, True, 10**e, rng) >= 10**e) / trials for e in E]
    x = np.array([e*np.log(10) for e in E[1:]]); y = np.log(np.maximum(p[1:], 1e-12))
    sl = -np.polyfit(x, y, 1)[0]
    print(f"{c:>5.2f} " + " ".join(f"{v:>8.4f}" for v in p) + f" {sl:>9.4f} {(1-c)**2:>8.4f} {sl/(1-c)**2:>6.2f}")
