"""FEI+ for Boolean functions of m regular functions: audit.
 (1) every coordinate with nu_i(empty) > 1/2 has r_l(i) < 4 m^2 for some l;
 (2) RR+ = sum_{|S|>=2} P(S) sum_{i in S} min_l ln+(r_l(i)/|S|)  <=  (8 ln m + 9.86) J;
 (3) the true FEI+ ratio H^+/(I - Var)."""
import math, numpy as np
from feicore import spectrum, popcounts, polite
from multiorder import ltf_tt
polite()

def run(n, Ws, thetas, gate):
    m = len(Ws); N = 1 << n; xs = np.arange(N); pc = popcounts(n)
    V = np.stack([ltf_tt(w, th, n) for w, th in zip(Ws, thetas)])
    if gate == 'AND': out = V.all(axis=0)
    elif gate == 'OR': out = V.any(axis=0)
    elif gate == 'MAJ': out = V.sum(axis=0) * 2 > m
    else: out = (V.sum(axis=0) % 2) == 1
    if out.all() or (~out).all(): return None
    P = spectrum(np.where(out, -1.0, 1.0))
    ranks = []
    for w in Ws:
        order = sorted(range(n), key=lambda j: (-abs(w[j]), j)); r = np.empty(n, dtype=int)
        for pos, j in enumerate(order): r[j] = pos + 1
        ranks.append(r)
    ranks = np.array(ranks)
    big = pc >= 2; J = float((P * pc)[big].sum())
    if J < 1e-12: return None
    bad = 0
    RR = 0.0
    for i in range(n):
        inS = ((xs >> i) & 1) == 1
        inf_i = float(P[inS].sum()); a = float(P[1 << i])
        if inf_i > 0 and a / inf_i > 0.5 and ranks[:, i].min() >= 4 * m * m: bad += 1
        vals = np.log(np.maximum(1.0, ranks[:, i][:, None] / np.maximum(pc, 1)[None, :])).min(axis=0)
        RR += float((P * (inS & big) * vals).sum())
    nz = P > 1e-300
    H = float(-(P[nz] * np.log2(P[nz])).sum()); Hp = H - (P[0] * math.log2(1 / P[0]) if P[0] > 0 else 0)
    I = float((P * pc).sum()); Var = 1 - float(P[0])
    return dict(bad=bad, RR=RR / J, bound=8 * math.log(m) + 9.86, fp=Hp / (I - Var))

rng = np.random.default_rng(77)
worst = {}
for n in (8, 10, 12):
    for m in (2, 3, 4):
        for gate in ('AND', 'OR', 'MAJ', 'XOR'):
            if gate == 'MAJ' and m % 2 == 0: continue
            for r in range(6):
                if r < 2:
                    base = np.arange(n, 0, -1).astype(float)
                    Ws = [(base if l % 2 == 0 else base[::-1].copy()) * rng.choice([-1, 1], size=n) for l in range(m)]
                elif r == 2:   # a near-dictator member: one heavy weight
                    Ws = [rng.normal(size=n) for _ in range(m)]; Ws[0][0] = 50.0
                else:
                    Ws = [rng.normal(size=n) * rng.exponential(size=n) for _ in range(m)]
                thetas = [float(rng.uniform(-0.5, 0.5) * np.abs(w).sum()) for w in Ws]
                a = run(n, Ws, thetas, gate)
                if a is None: continue
                w = worst.setdefault((m, gate), dict(bad=0, RR=0.0, fp=0.0, bound=a['bound']))
                w['bad'] += a['bad']; w['RR'] = max(w['RR'], a['RR']); w['fp'] = max(w['fp'], a['fp'])
for (m, gate), w in sorted(worst.items()):
    print(f"m={m} {gate:3s}: violations of (1): {w['bad']}  max RR+/J = {w['RR']:.3f} (bound {w['bound']:.2f})  max FEI+ ratio = {w['fp']:.3f}", flush=True)
