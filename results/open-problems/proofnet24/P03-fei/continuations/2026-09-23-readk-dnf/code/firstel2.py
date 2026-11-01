"""Structured and larger adversarial checks of the first-element reference (see firstel.py):
families where the earlier global reference failed (frozen heavy + active light coordinates), OR/AND near the
extremes, majorities and thresholds with extreme i.i.d. or mixed biases, n up to 9."""
import math, sys, numpy as np
from firstel import analyse
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 5)
rows = []
def rec(tag, w, th, mu):
    r = analyse(np.asarray(w, float), th, np.asarray(mu, float))
    if r is None: return
    rows.append((r['ratio'], tag, r))
# frozen heavy + active light
for n in (5, 7, 9):
    for eps in (1e-2, 1e-4, 1e-6):
        for th_frac in (0.2, 0.5, 0.8):
            w = [10.0] + [1.0] * (n - 1)
            th = 10.0 * 0.0 + th_frac * (n - 1) - 10.0 + 0.5   # threshold region where the light part matters
            rec(f"frozenheavy n={n} eps={eps} t={th_frac}", w, th, [1 - eps] + [0.0] * (n - 1))
            rec(f"frozenheavy-neg n={n} eps={eps} t={th_frac}", w, -th, [-(1 - eps)] + [0.0] * (n - 1))
# OR / AND near the extremes, n up to 9
for n in (4, 6, 9):
    for eps in (1e-1, 1e-3, 1e-5):
        rec(f"OR n={n} q->1 eps={eps}", [1.0] * n, -(n - 1.0), [1 - eps] * n)
        rec(f"OR n={n} q->0 eps={eps}", [1.0] * n, -(n - 1.0), [-(1 - eps)] * n)
        rec(f"AND n={n} q->1 eps={eps}", [1.0] * n, n - 1.0, [1 - eps] * n)
# thresholds t-of-n with i.i.d. bias
for n in (5, 7, 9):
    for t in range(1, n + 1):
        for p in (1e-4, 1e-2, 0.1, 0.3, 0.5, 0.7, 0.9, 0.99, 0.9999):
            rec(f"thr {t}/{n} p={p}", [1.0] * n, 2 * t - n - 1.0, [2 * p - 1] * n)
# random weights, mixed extreme biases, n = 8, 9
for trial in range(int(sys.argv[2]) if len(sys.argv) > 2 else 60):
    n = int(rng.integers(8, 10))
    w = np.abs(rng.standard_normal(n)) * np.exp(rng.uniform(-2, 2, n))
    th = rng.uniform(-w.sum(), w.sum())
    mu = np.array([rng.choice([-1, 1]) * (1 - 10.0 ** (-rng.uniform(0.2, 5))) for _ in range(n)])
    rec(f"random n={n}", w, th, mu)
rows.sort(key=lambda z: -z[0])
for ratio, tag, r in rows[:15]:
    print(f"{ratio:7.2f}  {tag:40s} LHS/J {r['lhs']:5.2f}  T1 {r['T1']:6.2f} T2 {r['T2']:6.2f} T3 {r['T3']:6.2f}  (I-Var)/J {r['IV']:.2f}", flush=True)
print("cases:", len(rows))
