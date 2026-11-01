"""Audit of the per-set inequality in the proof of the logarithmic read-k bound:
for every nonempty S (all relevant sets, not only the spectral support),
  L_run(S) <= |S| K1 + kappa W(S),   K1 = log2 k + beta + 1 + 2 log2 3 + 2 log2 e + log2(beta k+1) + log2(beta k),
where L_run = -log2 of the run probability without Lambda.  Also re-checks |U| <= |S| and the root
disjointness, and the summed bound H <= h(Var) + Var Lambda + sum P L_run, on fresh random formulas
including monotone and non-monotone terms and a shared-core design."""
import numpy as np
from math import log2, e
from animalref import code_length, h2
from feicore import spectrum, popcounts, entropy
from mincover import random_readk, tt_dnf
from designdnf import design
rng = np.random.default_rng(99)
worst = 0.0; nsets = 0; nform = 0
for trial in range(24):
    n = 12 if trial % 2 else 11
    k = int(rng.integers(1, 9))
    beta = [2.5, 3.0, 4.0, 8.0][trial % 4]
    if trial % 6 == 5:
        n, V = design(4, min(k, 4) if k > 1 else 2, 2, 1, rng)
        terms = [(np.array(v), np.ones(len(v), dtype=int)) for v in V]
        k = max(np.bincount(np.concatenate([t[0] for t in terms])))
    else:
        terms = random_readk(n, k, rng)
        k = max(np.bincount(np.concatenate([t[0] for t in terms]), minlength=n))
    masks = [sum(1 << int(v) for v in V) for V, _ in terms]; sizes = [len(V) for V, _ in terms]
    pis = [2.0 ** -w for w in sizes]
    tov = {i: [t for t in range(len(masks)) if masks[t] >> i & 1] for i in range(n)}
    lam = 1.0 / k
    K1 = log2(k) + beta + 1 + 2 * log2(3) + 2 * log2(e) + log2(beta * k + 1) + log2(beta * k)
    kap = 1 + log2(e) * (1 / (beta * k) + 1 / (beta * k + 1))
    rel = 0
    for mk in masks: rel |= mk
    P = spectrum(tt_dnf(n, terms)); pc = popcounts(n)
    H = entropy(P); I = float((P * pc).sum()); Var = 1 - P[0]
    Lam = sum(log2(1 + lam * p) for p in pis)
    EL = 0.0
    for S in range(1, 1 << n):
        if S & ~rel: continue
        L, s, W, nu, nv = code_length(S, masks, sizes, pis, lam, k, beta, tov)
        assert nu <= s, (S, nu, s)
        slack = s * K1 + kap * W - L
        worst = min(worst, slack) if nsets else slack
        nsets += 1
        if P[S] > 0: EL += P[S] * L
    assert H <= h2(Var) + Var * Lam + EL + 1e-9
    nform += 1
    print(f"trial {trial:2d} n={n} k={k} beta={beta}: H/I={H/I:5.2f} bound/I={(h2(Var)+Var*Lam+EL)/I:5.2f} min per-set slack so far {worst:8.3f}", flush=True)
print(f"{nform} formulas, {nsets} sets: minimum of |S|K1 + kappa W - L_run = {worst:.4f} (must be >= 0)")
