"""Biased FEI+ for linear threshold functions: adversarial search over biases (and weights).
ratio = H^mu[f^{>=1}] / (Inf^mu - Var^mu), H^mu = sum_{S != 0} Ft^2 log2(prod sigma^2 / Ft^2)."""
import math, numpy as np
from biased_feiplus import biased_coeffs
from feicore import popcounts, polite
polite()

def ltf_pm(w, theta, n):
    xs = np.arange(1 << n)
    x = 1 - 2 * ((xs[:, None] >> np.arange(n)[None, :]) & 1)     # bit 1 -> x_i = -1
    return np.where(x @ w - theta > 0, 1, -1)

def ratio_tt(F, mu, n, pc, xs):
    Ft = biased_coeffs(F, mu); P = Ft ** 2
    sig2 = 1 - np.asarray(mu) ** 2
    logsig = np.zeros(1 << n)
    for i in range(n): logsig += ((xs >> i) & 1) * math.log2(sig2[i])
    mask = (P > 1e-300) & (xs > 0)
    Hp = float((P[mask] * (logsig[mask] - np.log2(P[mask]))).sum())
    Inf = float((P * pc).sum()); Var = float(P[1:].sum())
    ex = Inf - Var
    return (Hp / ex if ex > 1e-13 else 0.0), Hp, ex

rng = np.random.default_rng(314)
best = (0, None)
for trial in range(60):
    n = int(rng.choice([5, 7, 9, 11]))
    xs = np.arange(1 << n); pc = popcounts(n)
    kind = trial % 3
    if kind == 0: w = np.ones(n); theta = 0.0                       # majority (n odd)
    elif kind == 1: w = rng.integers(1, 6, size=n).astype(float); theta = float(rng.integers(-3, 4)) + 0.5
    else: w = rng.exponential(size=n); theta = float(rng.uniform(-1, 1) * w.sum() * 0.5)
    F = ltf_pm(w, theta, n)
    if np.all(F == F[0]): continue
    z = rng.normal(size=n) * 1.5
    r, _, _ = ratio_tt(F, np.tanh(z), n, pc, xs)
    for it in range(250):
        z2 = z.copy(); j = rng.integers(n); z2[j] += rng.normal() * 1.5; z2 = np.clip(z2, -7, 7)
        r2, _, _ = ratio_tt(F, np.tanh(z2), n, pc, xs)
        if r2 > r: z, r = z2, r2
    if r > best[0]:
        best = (r, (n, kind, [round(float(v), 3) for v in w], round(theta, 3), [round(float(v), 4) for v in np.tanh(z)]))
    if trial % 10 == 9: print(f"trial {trial+1}: best {best[0]:.3f}", flush=True)
print("BEST", round(best[0], 4)); print("instance", best[1])
