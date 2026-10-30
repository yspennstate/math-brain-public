"""Two inputs through a critical (He, weight variance 2/n, no bias) fully connected ReLU net of width n, depth L = t n.

Exact reduction: given the layer-l outputs h1, h2 (only their norms and angle matter), the next preactivations are n iid
pairs (z1, z2) = (a1 g, a2 (cos th g + sin th g')), g, g' iid N(0, 2/n); h' = relu(z). The angle is computed as
2 atan2(|u1 - u2|, |u1 + u2|) on unit vectors, which keeps full precision at angles of order 1/n.
Deterministic (infinite-width) recursion: th_l ~ 3 pi / l. Prediction: at L = t n the rescaled angle n th_L has a
nondegenerate random limit (the count of units whose sign differs between the inputs is O(1) per layer).
Prints, for each n and t: quantiles of n th_L, its mean against 3 pi / t, the mean number of sign-disagreeing units per
layer over the last tenth of the layers, and the correlation of log(n th_L) with log of the first input's norm.
usage: python -X utf8 two_input.py n1,n2 t1,t2 reps th0"""
import sys
import numpy as np

try:
    import psutil
    psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

ns = [int(v) for v in sys.argv[1].split(",")]; ts = [float(v) for v in sys.argv[2].split(",")]
reps = int(sys.argv[3]); th0 = float(sys.argv[4])
rng = np.random.default_rng(262)
for n in ns:
    Lmax = int(round(max(ts) * n)); marks = {int(round(t * n)): t for t in ts}
    out, flips, lognorm = {}, {}, {}
    a1 = np.ones(reps); a2 = np.ones(reps); th = np.full(reps, th0); ln1 = np.zeros(reps); fl = []
    for l in range(1, Lmax + 1):
        g = rng.standard_normal((reps, n)) * np.sqrt(2.0 / n); gp = rng.standard_normal((reps, n)) * np.sqrt(2.0 / n)
        z1 = a1[:, None] * g; z2 = a2[:, None] * (np.cos(th)[:, None] * g + np.sin(th)[:, None] * gp)
        fl.append(np.count_nonzero((z1 > 0) != (z2 > 0), axis=1))
        h1 = np.maximum(z1, 0); h2 = np.maximum(z2, 0)
        n1 = np.linalg.norm(h1, axis=1); n2 = np.linalg.norm(h2, axis=1)
        u1 = h1 / np.where(n1 > 0, n1, 1)[:, None]; u2 = h2 / np.where(n2 > 0, n2, 1)[:, None]
        th = 2 * np.arctan2(np.linalg.norm(u1 - u2, axis=1), np.linalg.norm(u1 + u2, axis=1))
        ln1 = ln1 + np.log(np.where(n1 > 0, n1, np.nan) / a1); a1, a2 = n1, n2
        if l in marks:
            t = marks[l]; out[t] = n * th; lognorm[t] = ln1.copy()
            flips[t] = np.mean(np.array(fl[-max(1, l // 10):]), axis=0)
    for t in ts:
        ok = np.isfinite(out[t]) & np.isfinite(lognorm[t]) & (out[t] > 0)
        v = out[t][ok]; q = np.quantile(v, [0.1, 0.25, 0.5, 0.75, 0.9])
        c = np.corrcoef(np.log(v), lognorm[t][ok])[0, 1]
        print("n %5d t %.2f L %5d reps %d | n*th quantiles 10/25/50/75/90: %s | mean %.3f (3pi/t %.3f) | mean log %.3f sd log %.3f | "
              "flips/layer %.3f (n th/pi at end %.3f) | corr(log n th, log|h1|) %+.2f"
              % (n, t, int(round(t * n)), len(v), " ".join("%.3f" % x for x in q), v.mean(), 3 * np.pi / t,
                 np.log(v).mean(), np.log(v).std(), np.mean(flips[t][ok]), v.mean() / np.pi, c), flush=True)
print("DONE", flush=True)
