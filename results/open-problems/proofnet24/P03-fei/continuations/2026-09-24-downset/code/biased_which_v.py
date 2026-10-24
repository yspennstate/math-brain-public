# Which coordinate makes the biased step work? For random monotone 2-DNF gates and random biases, test candidate rules
# for choosing v and record the worst ratio Lstep_v / Rstep_v each rule gives (the best coordinate gives <= 7.77).
import math, numpy as np, biased_induction as BI
rng = np.random.default_rng(29)
def pieces(F, q):
    m = len(q); L, R = BI.LR(F, q); out = []
    for v in range(m):
        qq = q[:v] + q[v + 1:]
        L0, R0 = BI.LR(BI.restrict(F, m, v, 0), qq); L1, R1 = BI.LR(BI.restrict(F, m, v, 1), qq)
        Ls = L - ((1 - q[v]) * L0 + q[v] * L1); Rs = R - ((1 - q[v]) * R0 + q[v] * R1)
        out.append((Ls, Rs))
    return out
def piv(F, q, v):
    m = len(q); x = np.arange(1 << m); w = np.ones(1 << m)
    for j in range(m): w *= np.where((x >> j) & 1, q[j], 1 - q[j])
    lo = x[((x >> v) & 1) == 0]; hi = lo | (1 << v)
    wl = w[lo] / (1 - q[v])
    return float(wl[F[lo] != F[hi]].sum())
rules = {'best': None, 'max Rstep': None, 'max Rstep/m-ish (relative pivotality)': None, 'max bias q_v': None,
         'max degree': None, 'max Pr[piv]': None}
worst = {k: 0.0 for k in rules}
for trial in range(400):
    m = int(rng.integers(3, 7)); x = np.arange(1 << m); G = np.zeros(1 << m, dtype=bool); deg = [0] * m
    for _ in range(int(rng.integers(1, 2 * m))):
        u, w_ = rng.choice(m, size=2, replace=False); G |= ((x >> int(u)) & 1).astype(bool) & ((x >> int(w_)) & 1).astype(bool)
        deg[u] += 1; deg[w_] += 1
    F = np.where(G, -1.0, 1.0)
    if (F == 1).all() or (F == -1).all(): continue
    qs = list(np.exp(rng.uniform(np.log(1e-3), np.log(0.5), size=m))); q = [qq if rng.random() < 0.5 else 1 - qq for qq in qs]
    ps = pieces(F, q); ratios = [Ls / Rs if Rs > 1e-14 else math.inf for Ls, Rs in ps]
    pv = [piv(F, q, v) for v in range(m)]
    pr1 = 1 - float(np.prod([1.0]))
    choice = {'best': int(np.argmin(ratios)), 'max Rstep': int(np.argmax([Rs for _, Rs in ps])),
              'max Rstep/m-ish (relative pivotality)': int(np.argmax([Rs / (4 * q[v] * (1 - q[v])) for v, (_, Rs) in enumerate(ps)])),
              'max bias q_v': int(np.argmax(q)), 'max degree': int(np.argmax(deg)), 'max Pr[piv]': int(np.argmax(pv))}
    for k, v in choice.items():
        r = ratios[v]
        if r < math.inf: worst[k] = max(worst[k], r)
for k, v in worst.items(): print('%-42s worst ratio %.3f' % (k, v))
