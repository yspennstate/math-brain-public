"""Does the symmetric two-sided firework die for every c < 1, or does the mutual help (a site near one
end whose reach crosses the whole interval) push the threshold below 1?  Follow P(size >= N) out to
N = 10^15: a positive limit means survival, a slow power decay means extinction."""
import numpy as np, sys
from h0024_fast import trial

trials = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
rng = np.random.default_rng(7)
E = (3, 6, 9, 12, 15, 18)
print(f"{'c':>5} " + " ".join(f"{10**e:>8.0e}" for e in E) + f" {'tail slope':>10} {'(1-c)^2':>8}")
for c in (0.6, 0.7, 0.8, 0.9, 0.95):
    p = []
    for e in E:
        n = 10 ** e
        p.append(sum(1 for _ in range(trials) if trial(c, True, n, rng) >= n) / trials)
    x = np.array([e * np.log(10) for e in E[-3:]]); y = np.log(np.maximum(p[-3:], 1e-12))
    sl = -np.polyfit(x, y, 1)[0]
    print(f"{c:>5.2f} " + " ".join(f"{v:>8.4f}" for v in p) + f" {sl:>10.4f} {(1-c)**2:>8.4f}")
