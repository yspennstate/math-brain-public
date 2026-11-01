"""Replay the float LTF search of bfp_ltf.py (same seed, same steps), keep the exact best instance of each trial,
and re-evaluate the top instances in 50-digit arithmetic against 2 + 4 log2 e."""
import math, numpy as np, mpmath as mp
from biased_feiplus import biased_coeffs
from feicore import popcounts, polite
from bfp_exact import exact_ratio
polite()
mp.mp.dps = 50
BOUND = 2 + 4 / mp.log(2)

def ltf_pm(w, theta, n):
    xs = np.arange(1 << n)
    x = 1 - 2 * ((xs[:, None] >> np.arange(n)[None, :]) & 1)
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
cands = []
for trial in range(60):
    n = int(rng.choice([5, 7, 9, 11]))
    xs = np.arange(1 << n); pc = popcounts(n)
    kind = trial % 3
    if kind == 0: w = np.ones(n); theta = 0.0
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
    cands.append((r, n, F.copy(), z.copy()))
cands.sort(key=lambda c: -c[0])
print('float ratios of the 8 best trials:', [round(c[0], 5) for c in cands[:8]])
for r, n, F, z in cands[:8]:
    mu = [mp.tanh(mp.mpf(float(v))) for v in z]
    e = exact_ratio(F.tolist(), mu)
    print('n=%2d float %.6f exact %s  exact - bound = %s' % (n, r, mp.nstr(e, 10), mp.nstr(e - BOUND, 5)), flush=True)
