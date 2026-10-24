# Wider test of the biased strengthened inequality on monotone 2- and 3-DNF gates with up to 10 inputs:
# random graphs / hypergraphs, random product measures (log-uniform biases towards 0 or 1), and a greedy local search
# on the biases maximising the ratio. Prints the largest ratio against 2 + 4 log2 e.
import itertools, math, random, numpy as np
from biased_gate import biased_transform

def ratio_terms(terms, m, q):
    N = 1 << m; x = np.arange(N)
    G = np.zeros(N, dtype=bool)
    for t in terms:
        mm = 0
        for v in t: mm |= 1 << v
        G |= (x & mm) == mm
    c = biased_transform(np.where(G, -1.0, 1.0), q)
    P = c * c
    sig2 = [1 - (2 * qq - 1) ** 2 for qq in q]
    logsig = np.zeros(N); pc = np.zeros(N)
    for j in range(m):
        has = ((x >> j) & 1).astype(bool); logsig[has] += math.log2(sig2[j]); pc[has] += 1
    nz = (np.arange(N) > 0) & (P > 1e-300)
    L = float((P[nz] * (logsig[nz] - np.log2(P[nz]))).sum())
    D = float((P * pc).sum()) - float(P[1:].sum())
    return L / D if D > 1e-12 else 0.0

rng = random.Random(3)
best = (0.0, None)
for trial in range(120):
    m = rng.randint(4, 10); w = rng.choice([2, 2, 3])
    nterms = rng.randint(2, 3 * m)
    terms = list({tuple(sorted(rng.sample(range(m), w))) for _ in range(nterms)})
    q = [math.exp(rng.uniform(math.log(1e-4), math.log(0.5))) for _ in range(m)]
    q = [qq if rng.random() < 0.5 else 1 - qq for qq in q]
    r = ratio_terms(terms, m, q)
    for it in range(150):                      # greedy local search on the biases
        j = rng.randrange(m); old = q[j]
        cand = min(1 - 1e-5, max(1e-5, old * math.exp(rng.gauss(0, 1.0)) if rng.random() < 0.5 else 1 - (1 - old) * math.exp(rng.gauss(0, 1.0))))
        q[j] = cand
        r2 = ratio_terms(terms, m, q)
        if r2 >= r: r = r2
        else: q[j] = old
    if r > best[0]: best = (r, (m, w, terms, [round(v, 6) for v in q]))
print('largest ratio over 120 random 2/3-DNF gates with searched biases: %.5f (2 + 4 log2 e = %.5f)' % (best[0], 2 + 4 / math.log(2)))
print('attained by', best[1])
