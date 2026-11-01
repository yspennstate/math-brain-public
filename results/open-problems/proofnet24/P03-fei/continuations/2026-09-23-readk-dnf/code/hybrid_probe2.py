"""More one-parameter limits for the hybrid reference (eps -> 1e-12): i.i.d. thresholds at extreme bias, lexicographic
(geometric) weights with frozen coordinates, frozen predecessors + active successors, multi-scale frozen successors."""
import numpy as np, math
from hybrid import analyse
fams = []
for n in (5, 7):
    for t in range(1, n + 1):
        fams.append((f"thr {t}/{n} p=eps", lambda e, n=n, t=t: (np.ones(n), 2 * t - n - 1.0, np.full(n, -(1 - 2 * e)))))
        fams.append((f"thr {t}/{n} p=1-eps", lambda e, n=n, t=t: (np.ones(n), 2 * t - n - 1.0, np.full(n, 1 - 2 * e))))
fams.append(("lex 6, frozen 2nd", lambda e: (2.0 ** -np.arange(6), 0.3, np.array([0, 1 - 2 * e, 0, 0, 0, 0.0]))))
fams.append(("lex 6, frozen 1st,3rd", lambda e: (2.0 ** -np.arange(6), 0.3, np.array([1 - 2 * e, 0, -(1 - 2 * e), 0, 0, 0.0]))))
fams.append(("frozen preds + active succ", lambda e: (np.array([5.0, 4.0, 1, 1, 1, 1]), 3.5, np.array([1 - 2 * e, 1 - 2 * e, 0, 0, 0, 0.0]))))
fams.append(("multiscale frozen succ", lambda e: (np.array([4.0, 2, 2, 1, 1]), 3.9, np.array([0, 1 - 2 * e, 1 - 2 * e ** 2, 0, 0.0]))))
fams.append(("majority 7, one frozen", lambda e: (np.ones(7), 0.0, np.array([1 - 2 * e, 0, 0, 0, 0, 0, 0.0]))))
fams.append(("heavy active + light frozen", lambda e: (np.array([6.0, 1, 1, 1, 1, 1]), 0.5, np.array([0, 1 - 2 * e, 1 - 2 * e, -(1 - 2 * e), 0, 0.0]))))
worst = []
for tag, gen in fams:
    vals = []
    for e in (1e-3, 1e-6, 1e-9, 1e-12):
        w, th, mu = gen(e)
        r = analyse(np.asarray(w, float), th, np.asarray(mu, float))
        vals.append(r['ratio'] if r else float('nan'))
    growth = vals[-1] - vals[0] if not any(math.isnan(v) for v in vals) else float('nan')
    worst.append((growth, tag, vals))
    print(f"{tag:30s} Bd/J at eps 1e-3..1e-12: " + " ".join(f"{v:6.2f}" for v in vals), flush=True)
worst = [w for w in worst if not math.isnan(w[0])]
worst.sort(key=lambda z: -z[0])
print("largest growth:", worst[:3])
