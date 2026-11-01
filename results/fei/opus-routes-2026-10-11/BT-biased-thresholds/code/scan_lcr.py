"""Search for violations of (LCR): excess = sum_k W_k ln(1/W_k) - sum_k sum_i W_k pi_i^(k) ln^+(4 pi_i^(k)/sigma_i^2), divided by I.
Random weighted thresholds n <= 10, random/extreme biases, local maximization of excess/I. Evidence only."""
import numpy as np, math, sys, time, warnings
from scipy.optimize import minimize
from biased import ltf_table, g_transform, sigma2_vector, popcount_vector
warnings.filterwarnings('ignore')
rng = np.random.default_rng(int(sys.argv[1])); TLIM = float(sys.argv[2])
MEM = {}
def lcr(T, q):
    n = len(q); g = g_transform(T, q); s2 = sigma2_vector(q); k = popcount_vector(n); P = s2 * g * g
    sig = 4 * q * (1 - q); I = (k * P).sum()
    if I < 1e-300: return 0.0
    if n not in MEM:
        idx = np.arange(2 ** n); MEM[n] = ((idx[:, None] >> np.arange(n)) & 1).astype(float)
    M = MEM[n]; tot = 0.0
    for kk in range(1, n + 1):
        sel = (k == kk); Wk = P[sel].sum()
        if Wk <= 1e-300: continue
        pik = (P[sel] @ M[sel]) / Wk
        cred = np.sum(Wk * pik * np.maximum(0.0, np.log(np.maximum(4 * pik / sig, 1e-300))))
        tot += Wk * math.log(1 / Wk) - cred
    return tot / I
def neg(x, T): return -lcr(T, 1 / (1 + np.exp(-np.clip(x, -12, 12))))
t0 = time.time(); best = (-1e9, None); cnt = 0
while time.time() - t0 < TLIM:
    n = int(rng.integers(2, 11)); kind = rng.integers(0, 3)
    w = (rng.integers(1, 6, n) if kind == 0 else np.exp(rng.normal(0, 1.4, n)) if kind == 1 else np.where(rng.random(n) < 0.3, rng.integers(2, 7), 1)).astype(float)
    th = rng.random() * w.sum(); T = ltf_table(w, th)
    if T.min() == T.max(): continue
    x = rng.normal(0, 3.5, n); v = lcr(T, 1 / (1 + np.exp(-x))); cnt += 1
    if v > best[0] - 0.5:
        r = minimize(neg, x, args=(T,), method='Nelder-Mead', options=dict(maxiter=120 * n))
        if -r.fun > best[0]:
            best = (-r.fun, (n, np.round(w, 3).tolist(), round(th, 3), np.round(1 / (1 + np.exp(-np.clip(r.x, -12, 12))), 6).tolist()))
print('configs', cnt, 'max LCR excess / I =', best)
# T_s family
for s in (4, 8, 12):
    x = 1.0 / s; p = x / 50; a2 = p ** s; ph = a2 * (1 - x) / (x + a2 * (1 - x))
    print('T_s s=%d LCR excess/I = %.4f' % (s, lcr(ltf_table([s] + [1] * s, s), np.array([ph] + [p] * s))))
