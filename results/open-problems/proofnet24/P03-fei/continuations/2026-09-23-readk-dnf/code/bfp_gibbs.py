"""Biased FEI+ for LTFs: is the proposed Gibbs bound bounded under adversarial biases?
Bound B = (2/ln2) J + W log2(1/W) + sum_{|S|>=2} P(S) log2(sigma_S^2 / Q(S)),
Q(S) = 2^{-(|S|-1)} sigma_S^2 theta_k(S) / Z_k,  Z_k = e_k(sigma^2 theta_k),  theta_k(j) = min(1, (k/M_j)^a),
M_j = mass rank = sum of sigma^2 over coordinates at least as desirable (order by |w| decreasing), relevant coords only.
Report max over searches of B/J and of H^+/J, and the split of B into its parts."""
import math, numpy as np
from biased_feiplus import biased_coeffs
from feicore import popcounts, polite
def ltf_pm(w, theta, n):
    xs = np.arange(1 << n)
    x = 1 - 2 * ((xs[:, None] >> np.arange(n)[None, :]) & 1)
    return np.where(x @ w - theta > 0, 1, -1)
polite()
A = 1.2

def parts(F, mu, w, n, pc, xs):
    Ft = biased_coeffs(F, mu); P = Ft ** 2
    sig2 = 1 - np.asarray(mu) ** 2
    logsig = np.zeros(1 << n)
    for i in range(n): logsig += ((xs >> i) & 1) * math.log2(sig2[i])
    big = pc >= 2; W = float(P[big].sum()); J = float((P * pc)[big].sum())
    if J < 1e-14: return None
    nz = P > 1e-300
    Hp = float((P[nz & (xs > 0)] * (logsig[nz & (xs > 0)] - np.log2(P[nz & (xs > 0)]))).sum())
    # relevant coordinates: positive influence
    infl = np.array([float(P[((xs >> i) & 1) == 1].sum()) for i in range(n)])
    rel = infl > 1e-200
    relmask = 0
    for i in range(n):
        if rel[i]: relmask |= 1 << i
    inrel = (xs & ~relmask) == 0
    order = sorted([i for i in range(n) if rel[i]], key=lambda j: (-abs(w[j]), j))
    M = np.zeros(n); acc = 0.0
    for j in order: acc += sig2[j]; M[j] = acc
    cost = 0.0
    for kk in range(2, n + 1):
        selk = big & nz & (pc == kk) & inrel
        if not selk.any(): continue
        th = np.where(rel, np.minimum(1.0, np.exp(A * (math.log(kk) - np.log(np.maximum(M, 1e-300))))), 0.0)
        e = np.zeros(kk + 1); e[0] = 1.0
        for j in range(n):
            e[1:] = e[1:] + sig2[j] * th[j] * e[:-1]
        logZ = math.log2(e[kk])
        logth = np.zeros(1 << n)
        for j in range(n):
            logth += ((xs >> j) & 1) * (math.log2(th[j]) if th[j] > 0 else -1e9)
        cost += float((P[selk] * ((kk - 1) + logZ - logth[selk])).sum())
    B = (2 / math.log(2)) * J + (W * math.log2(1 / W) if W > 0 else 0) + cost
    return dict(B=B / J, Hp=Hp / J, WlogW=(W * math.log2(1 / W)) / J if W > 0 else 0, cost=cost / J)

rng = np.random.default_rng(99)
best = dict(B=0, Hp=0)
for trial in range(40):
    n = int(rng.choice([5, 7, 9]))
    xs = np.arange(1 << n); pc = popcounts(n)
    if trial % 2 == 0: w = np.ones(n) + 0.01 * np.arange(n)[::-1]; theta = 0.0
    else: w = rng.exponential(size=n); theta = float(rng.uniform(-1, 1) * w.sum() * 0.5)
    F = ltf_pm(w, theta, n)
    if np.all(F == F[0]): continue
    z = rng.normal(size=n) * 1.5
    a = parts(F, np.tanh(z), w, n, pc, xs)
    if a is None: continue
    r = a['B']
    for it in range(150):
        z2 = z.copy(); j = rng.integers(n); z2[j] += rng.normal() * 1.5; z2 = np.clip(z2, -7, 7)
        a2 = parts(F, np.tanh(z2), w, n, pc, xs)
        if a2 is not None and a2['B'] > r: z, r, a = z2, a2['B'], a2
    if a['B'] > best['B']: best = dict(a, mu=[round(float(v), 4) for v in np.tanh(z)], n=n, w=[round(float(v), 3) for v in w], theta=theta)
    if trial % 10 == 9: print(f"trial {trial+1}: max B/J {best['B']:.3f} (H+/J there {best['Hp']:.3f}, WlogW/J {best['WlogW']:.3f}, cost/J {best['cost']:.3f})", flush=True)
print("worst instance:", best)
