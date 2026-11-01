"""Decay exponent of P(size >= N) for the one-sided and symmetric two-sided firework, c < 1.
Two candidate laws: exponent 1-c (the one-sided answer, and what a decoupling of the two ends
would predict for the two-sided one up to a constant 2) and (1-c)^2 (the memo's earlier reading)."""
import numpy as np, sys
from h0024_fast import trial

trials = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
rng = np.random.default_rng(11)
E = (3, 5, 7, 9, 11)
print(f"{'c':>5} {'side':>4} " + " ".join(f"{10**e:>8.0e}" for e in E) + f" {'slope':>8} {'1-c':>6} {'(1-c)^2':>8}")
for c in (0.4, 0.5, 0.6, 0.75):
    for two in (False, True):
        p = []
        for e in E:
            n = 10 ** e
            p.append(sum(1 for _ in range(trials) if trial(c, two, n, rng) >= n) / trials)
        x = np.array([e * np.log(10) for e in E]); y = np.log(np.maximum(p, 1e-12))
        sl = -np.polyfit(x[1:], y[1:], 1)[0]
        print(f"{c:>5.2f} {'two' if two else 'one':>4} " + " ".join(f"{v:>8.4f}" for v in p)
              + f" {sl:>8.4f} {1-c:>6.3f} {(1-c)**2:>8.3f}")
