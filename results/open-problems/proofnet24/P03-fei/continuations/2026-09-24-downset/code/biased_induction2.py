# Wider test of the one-coordinate biased step: random monotone 2- and 3-DNF gates on 6-8 inputs, random bias vectors,
# then a coordinate-wise local search on the biases of the worst cases, maximising rho = min_v Lstep_v / Rstep_v.
import math, numpy as np
from biased_induction import rho
rng = np.random.default_rng(23)
def rand_gate(m, w):
    x = np.arange(1 << m); G = np.zeros(1 << m, dtype=bool)
    for _ in range(int(rng.integers(2, 3 * m))):
        S = rng.choice(m, size=w, replace=False); mask = int(sum(1 << int(v) for v in S))
        G |= (x & mask) == mask
    return np.where(G, -1.0, 1.0)
def rand_q(m):
    qs = list(np.exp(rng.uniform(np.log(1e-4), np.log(0.5), size=m)))
    return [qq if rng.random() < 0.5 else 1 - qq for qq in qs]
cands = []
for m, w, ng, nq in ((6, 2, 25, 40), (7, 2, 15, 30), (8, 2, 8, 20), (6, 3, 15, 30), (7, 3, 10, 20)):
    best = 0.0
    for g in range(ng):
        F = rand_gate(m, w)
        if (F == 1).all() or (F == -1).all(): continue
        for t in range(nq):
            q = rand_q(m); r = rho(F, q)
            best = max(best, r); cands.append((r, F, q))
    print('m=%d width %d: %d gates x %d bias vectors, max rho %.4f' % (m, w, ng, nq, best), flush=True)
cands.sort(key=lambda c: -c[0])
top = 0.0
for r0, F, q in cands[:12]:           # local search on the biases of the twelve worst
    q = list(q); r = r0; step = 0.5
    for it in range(60):
        j = int(rng.integers(len(q))); lq = math.log(q[j] / (1 - q[j]))
        for d in (step, -step):
            q2 = list(q); q2[j] = 1 / (1 + math.exp(-(lq + d)))
            q2[j] = min(max(q2[j], 1e-6), 1 - 1e-6)
            r2 = rho(F, q2)
            if r2 > r: r, q = r2, q2
        step *= 0.97
    top = max(top, r)
print('after local search on the worst twelve: max rho %.4f   (2 + 4 log2 e = %.4f)' % (top, 2 + 4 / math.log(2)))
