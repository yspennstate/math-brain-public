"""Biased FEI+ for LTFs with biases confined to |mu_j| <= mu_max (i.e. p_j in [delta, 1-delta]).
For each mu_max, adversarial search over biases in the box and over LTFs; report
 - max true ratio H^+/(I-Var),
 - max of the Gibbs bound / J with the UNWEIGHTED rank reference (singletons by Lemma A, W log(1/W), rank cost),
 - max of W log(1/W) / J (the biased Lemma B quantity without sigma weights)."""
import math, numpy as np
from biased_feiplus import biased_coeffs
from feicore import popcounts, polite
polite()
A = 1.2

def ltf_pm(w, theta, n):
    xs = np.arange(1 << n)
    x = 1 - 2 * ((xs[:, None] >> np.arange(n)[None, :]) & 1)
    return np.where(x @ w - theta > 0, 1, -1)

def quantities(F, mu, w, n, pc, xs):
    P = biased_coeffs(F, mu) ** 2
    sig2 = 1 - np.asarray(mu) ** 2
    logsig = np.zeros(1 << n)
    for i in range(n): logsig += ((xs >> i) & 1) * math.log2(sig2[i])
    big = pc >= 2; W = float(P[big].sum()); J = float((P * pc)[big].sum())
    I = float((P * pc).sum()); Var = float(P[1:].sum())
    if J < 1e-12 or W <= 0: return None
    nz = P > 1e-300
    sel1 = nz & (xs > 0)
    Hp = float((P[sel1] * (logsig[sel1] - np.log2(P[sel1]))).sum())
    # unweighted rank reference over relevant coords ordered by |w|
    infl = np.array([float(P[((xs >> i) & 1) == 1].sum()) for i in range(n)])
    order = sorted([i for i in range(n) if infl[i] > 1e-200], key=lambda j: (-abs(w[j]), j))
    r = np.full(n, 10 ** 9, dtype=float)
    for pos, j in enumerate(order): r[j] = pos + 1
    cost = 0.0
    for kk in range(2, n + 1):
        selk = big & nz & (pc == kk)
        if not selk.any(): continue
        th = np.minimum(1.0, (kk / r) ** A)
        e = np.zeros(kk + 1); e[0] = 1.0
        for j in range(n): e[1:] = e[1:] + th[j] * e[:-1]
        logth = np.zeros(1 << n)
        for j in range(n): logth += ((xs >> j) & 1) * math.log2(th[j])
        # biased entropy term uses log(sigma_S^2/Q): sigma part <= 0, keep it (it only helps)
        cost += float((P[selk] * (logsig[selk] + (kk - 1) + math.log2(e[kk]) - logth[selk])).sum())
    single = 0.0
    for i in range(n):
        p1 = float(P[1 << i])
        if p1 > 1e-300: single += p1 * (math.log2(sig2[i]) - math.log2(p1))
    bound = single + W * math.log2(1 / W) + cost
    return dict(fp=Hp / (I - Var), gib=bound / J, WlogW=W * math.log2(1 / W) / J)

rng = np.random.default_rng(11)
for mu_max in (0.5, 0.8, 0.95):
    best = dict(fp=0, gib=0, WlogW=0)
    for trial in range(30):
        n = int(rng.choice([5, 7, 9]))
        xs = np.arange(1 << n); pc = popcounts(n)
        w = rng.exponential(size=n) if trial % 2 else np.ones(n) + 0.01 * np.arange(n)[::-1]
        theta = float(rng.uniform(-1, 1) * w.sum() * 0.5) if trial % 2 else 0.0
        F = ltf_pm(w, theta, n)
        if np.all(F == F[0]): continue
        z = rng.uniform(-1, 1, size=n) * mu_max
        q = quantities(F, z, w, n, pc, xs)
        if q is None: continue
        cur = q['gib']
        for it in range(150):
            z2 = z.copy(); j = rng.integers(n); z2[j] = np.clip(z2[j] + rng.normal() * 0.5, -mu_max, mu_max)
            q2 = quantities(F, z2, w, n, pc, xs)
            if q2 is not None and q2['gib'] > cur: z, cur, q = z2, q2['gib'], q2
        for kk in best: best[kk] = max(best[kk], q[kk])
    print(f"|mu| <= {mu_max}: max FEI+ ratio {best['fp']:.3f}, max Gibbs/J {best['gib']:.3f}, max W log(1/W)/J {best['WlogW']:.3f}", flush=True)
