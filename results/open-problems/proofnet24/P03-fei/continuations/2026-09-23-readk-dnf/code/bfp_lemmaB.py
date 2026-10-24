"""Candidate biased Lemma B:  W log2(1/W) <= C J + sum_{|S|>=2} P(S) log2(1/sigma_S^2)   (any f, any product measure).
Adversarial search over biases for random functions, LTFs and read-k DNFs; report max of
R = (W log(1/W) - sum_{|S|>=2} P log(1/sigma_S^2)) / J."""
import math, numpy as np
from biased_feiplus import biased_coeffs
from feicore import popcounts, polite
from readk_nonmono import random_nonmono
polite()

def ltf_pm(w, theta, n):
    xs = np.arange(1 << n)
    x = 1 - 2 * ((xs[:, None] >> np.arange(n)[None, :]) & 1)
    return np.where(x @ w - theta > 0, 1, -1)

def R(F, mu, n, pc, xs):
    P = biased_coeffs(F, mu) ** 2
    sig2 = 1 - np.asarray(mu) ** 2
    logsig = np.zeros(1 << n)
    for i in range(n): logsig += ((xs >> i) & 1) * math.log2(max(sig2[i], 1e-300))
    big = pc >= 2; W = float(P[big].sum()); J = float((P * pc)[big].sum())
    if J < 1e-15 or W <= 0: return None
    val = W * math.log2(1 / W) + float((P[big] * logsig[big]).sum())
    return val / J

rng = np.random.default_rng(4242)
best = {}
for trial in range(90):
    n = int(rng.choice([4, 5, 6, 7, 8]))
    xs = np.arange(1 << n); pc = popcounts(n)
    kind = ['random', 'ltf', 'dnf'][trial % 3]
    if kind == 'random': F = np.where(rng.random(1 << n) < rng.uniform(0.05, 0.5), -1, 1)
    elif kind == 'ltf':
        w = rng.exponential(size=n); F = ltf_pm(w, float(rng.uniform(-1, 1) * w.sum() * 0.5), n)
    else:
        terms = random_nonmono(n, 2, [2, 2, 3, 3, 2], rng, pneg=0.5)
        sat = np.zeros(1 << n, dtype=bool)
        for (mm, v) in terms: sat |= (xs & mm) == v
        F = np.where(sat, -1, 1)
    if np.all(F == F[0]): continue
    z = rng.normal(size=n) * 1.5
    r = R(F, np.tanh(z), n, pc, xs)
    if r is None: continue
    for it in range(200):
        z2 = z.copy(); j = rng.integers(n); z2[j] += rng.normal() * 2.0; z2 = np.clip(z2, -9, 9)
        r2 = R(F, np.tanh(z2), n, pc, xs)
        if r2 is not None and r2 > r: z, r = z2, r2
    b = best.get(kind)
    if b is None or r > b[0]: best[kind] = (r, n, [round(float(v), 5) for v in np.tanh(z)])
    if trial % 15 == 14: print(f"trial {trial+1}: " + ", ".join(f"{k} {v[0]:.3f}" for k, v in best.items()), flush=True)
for k, v in best.items(): print(k, v)
