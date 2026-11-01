# Is the one-coordinate restriction step hopeless for biased gates, or only our bound? For a monotone 2-DNF gate G
# under the product measure with biases q, compute at each coordinate v the credited erasure ratio
#     rho_v = (B~_v - Inf~_v log2(1/sigma_v^2)) / Inf~_v,
# where B~_v = H(1[v in S] | S - v) for the biased spectral sample and Inf~_v = sum_{A ni v} P~(A) = sigma_v^2 Pr[v pivotal].
# The step approach needs min_v rho_v bounded; the paper's erasure bound transplanted to mu gives log2(m / Pr[piv]).
import math, numpy as np
from biased_gate import biased_transform
def run(name, m, edges, q):
    N = 1 << m; x = np.arange(N); G = np.zeros(N, dtype=bool)
    for (u, v) in edges: G |= ((x >> u) & 1).astype(bool) & ((x >> v) & 1).astype(bool)
    c = biased_transform(np.where(G, -1.0, 1.0), [q] * m); P = c * c
    sig2 = 4 * q * (1 - q)
    pG = float(np.prod([1.0]) )
    w = np.array([np.prod([q if (xx >> j) & 1 else 1 - q for j in range(m)]) for xx in range(N)])
    p1 = float(w[G].sum()); mm = min(p1, 1 - p1)
    out = []
    for v in range(m):
        low = x[((x >> v) & 1) == 0]; X = P[low]; Y = P[low | (1 << v)]
        def phi(p): return np.where(p > 1e-300, -p * np.log2(np.where(p > 1e-300, p, 1)), 0.0)
        B = float((phi(X) + phi(Y) - phi(X + Y)).sum()); inf = float(Y.sum())
        if inf < 1e-300: continue
        piv = inf / sig2
        out.append(((B - inf * math.log2(1 / sig2)) / inf, math.log2(mm / piv)))
    best = min(out)
    print('%-10s q=%-7g Pr[G=1]=%.3f  min_v rho_v %7.3f   (transplanted bound log2(m/Pr[piv]) at that v: %6.2f)'
          % (name, q, p1, best[0], best[1]), flush=True)
for q in (0.3, 0.1, 0.03, 0.01, 0.003, 0.001):
    run('matching4', 8, [(0, 1), (2, 3), (4, 5), (6, 7)], q)
for q in (0.1, 0.01, 0.001):
    run('path5', 5, [(i, i + 1) for i in range(4)], q)
    run('star4', 5, [(0, i) for i in range(1, 5)], q)
    run('K4', 4, [(i, j) for i in range(4) for j in range(i + 1, 4)], q)
