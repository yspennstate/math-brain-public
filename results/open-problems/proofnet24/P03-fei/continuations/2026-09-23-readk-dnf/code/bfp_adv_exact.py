"""Replay the float read-k DNF bias search of bfp_adv.py (same seed and steps), keep each trial's exact best
biases, and re-evaluate the top instances in 50-digit arithmetic against 2 + 4 log2 e."""
import math, numpy as np, mpmath as mp
from biased_feiplus import feiplus
from readk_nonmono import random_nonmono
from feicore import polite
from bfp_exact import exact_ratio
polite()
mp.mp.dps = 50
BOUND = 2 + 4 / mp.log(2)
rng = np.random.default_rng(77)
def ratio(n, terms, mu):
    Hp, Inf, Var, _ = feiplus(n, terms, mu)
    ex = Inf - Var
    return Hp / ex if ex > 1e-13 else 0.0
cands = []
for trial in range(40):
    n = int(rng.choice([8, 10, 12])); k = int(rng.choice([1, 2, 3]))
    wl = list(rng.integers(1, 5, size=int(rng.integers(3, 9))))
    terms = random_nonmono(n, k, wl, rng, pneg=float(rng.choice([0.0, 0.5])))
    if not terms: continue
    z = rng.normal(size=n) * 2
    mu = np.tanh(z); r = ratio(n, terms, mu)
    for it in range(150):
        z2 = z.copy(); j = rng.integers(n); z2[j] += rng.normal() * 1.5
        z2 = np.clip(z2, -6, 6)
        mu2 = np.tanh(z2); r2 = ratio(n, terms, mu2)
        if r2 > r: z, mu, r = z2, mu2, r2
    cands.append((r, n, terms, z.copy()))
cands.sort(key=lambda c: -c[0])
print('float ratios of the 6 best trials:', [round(c[0], 5) for c in cands[:6]], flush=True)
for r, n, terms, z in cands[:6]:
    N = 1 << n; xs = np.arange(N); sat = np.zeros(N, dtype=bool)
    for (m_, v) in terms: sat |= (xs & m_) == v
    F = np.where(sat, -1, 1)
    mu = [mp.tanh(mp.mpf(float(v))) for v in z]
    e = exact_ratio(F.tolist(), mu)
    print('n=%2d float %.6f exact %s  exact - bound = %s' % (n, r, mp.nstr(e, 10), mp.nstr(e - BOUND, 5)), flush=True)
