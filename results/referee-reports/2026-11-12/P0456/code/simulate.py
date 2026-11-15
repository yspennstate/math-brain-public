"""Computations for Section 6 of "The connectivity window of bilateral preference random graphs".

1. The limiting one-vertex integral I_k = (1/k!) int_0^inf Q(s)^k e^{-s} ds with Q(s) = E(s - G_k)^+,
   G_k ~ Gamma(k,1); I_k e^k tends to 1 (Q >= (s-k)^+ gives I_k >= e^{-k}).
2. Direct simulation of LK(n,k): the number Z of isolated vertices, and P(connected) against
   exp(-n e^{-k}); also P(connected | Z = 0).

Run: python simulate.py simulate_out.txt   (numpy and scipy, seed 20261029, about 15 minutes)
"""
import math, sys, time
import numpy as np
from scipy import integrate, stats
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

out = open(sys.argv[1] if len(sys.argv) > 1 else "checks_out.txt", "w")
def P(*a):
    print(*a, file=out, flush=True)

P("== 1. one-root integral I_k / e^{-k}")
for k in [2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 25, 30]:
    G = stats.gamma(k)
    def Q(s):
        # E(s-G)^+ = s F_k(s) - k F_{k+1}(s)
        return s * G.cdf(s) - k * stats.gamma(k + 1).cdf(s)
    f = lambda s: math.exp(k * math.log(max(Q(s), 1e-300)) - s - math.lgamma(k + 1))
    val, err = integrate.quad(f, 0, 2 * k + 60 * math.sqrt(k) + 60, limit=400, points=[k, 2 * k])
    P(f"k={k:3d}  I_k*e^k = {val * math.exp(k):.8f}   (I_k*e^k - 1) = {val * math.exp(k) - 1:.3e}")

P("\n== 2. simulation of LK(n,k)")
rng = np.random.default_rng(20261029)

def one(n, k):
    W = rng.random((n, n))
    W = np.triu(W, 1)
    W = W + W.T
    np.fill_diagonal(W, 2.0)
    top = np.argpartition(W, k, axis=1)[:, :k]          # k lightest per row
    rows = np.repeat(np.arange(n), k)
    cols = top.ravel()
    A = csr_matrix((np.ones(rows.size, dtype=np.int8), (rows, cols)), shape=(n, n))
    M = A.multiply(A.T)                                 # mutual: kept iff in both lists
    deg = np.asarray(M.sum(axis=1)).ravel()
    iso = int((deg == 0).sum())
    ncomp, _ = connected_components(M, directed=False)
    return iso, ncomp == 1

for n, ks, T in [(1000, [6, 7, 8, 9], 300), (3000, [7, 8, 9, 10], 200)]:
    for k in ks:
        t0 = time.time()
        isos, conns = [], []
        for _ in range(T):
            i, c = one(n, k)
            isos.append(i); conns.append(c)
        isos = np.array(isos); conns = np.array(conns)
        lam = n * math.exp(-k)
        mean = isos.mean(); var = isos.var(ddof=1)
        p0 = (isos == 0).mean(); pc = conns.mean()
        se = math.sqrt(max(pc * (1 - pc), 1e-9) / T)
        # P(connected | no isolated vertex)
        cz = conns[isos == 0].mean() if (isos == 0).any() else float("nan")
        P(f"n={n} k={k} T={T}: lam=n e^-k={lam:.3f}  E[Z]={mean:.3f} Var[Z]={var:.3f}  "
          f"P(Z=0)={p0:.3f} exp(-E[Z])={math.exp(-mean):.3f}  P(conn)={pc:.3f}+-{se:.3f}  "
          f"exp(-lam)={math.exp(-lam):.3f}  P(conn|Z=0)={cz:.3f}  ({time.time() - t0:.0f}s)")
P("done")
