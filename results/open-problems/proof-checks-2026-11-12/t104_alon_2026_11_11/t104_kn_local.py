"""H next to the third zero, the uniformly weighted complete graph K_n.

At uniform weights every nontrivial eigenvalue of L is 2/(n-1), so need = (n-1) lam - 2 = 0, every gap is zero and
H = -need = 0. This script evaluates H (the same batched code as t104_np_hsearch.py) at K_n + eps v for random
nonnegative directions v (sum 1) and for the two orbit directions of a single edge and a star, and prints the
smallest H / eps and H / eps^2 at each eps.

usage: python t104_kn_local.py nmin nmax ndirs
"""
import importlib.util
import sys
import numpy as np

here = __file__.replace("t104_kn_local.py", "t104_np_hsearch.py")
nmin, nmax, ND = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
for n in range(nmin, nmax + 1):
    sys.argv = ["t104_np_hsearch.py", str(n), "1", "1", "1", "1"]
    spec = importlib.util.spec_from_file_location("hs%d" % n, here)
    h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
    m = h.m
    u = np.full(m, 1.0 / m)
    v0, _, _ = h.values(u[None, :], h.GRID)
    rng = np.random.default_rng(5)
    V = rng.exponential(size=(ND, m)) * (rng.random((ND, m)) < 0.5)
    V[V.sum(1) == 0, 0] = 1.0
    V = V / V.sum(1, keepdims=True)
    edge = np.zeros(m); edge[0] = 1.0
    star = h.STARS[0].copy(); star /= star.sum()
    tri = np.zeros(m)
    for p in ((0, 1), (0, 2), (1, 2)):
        tri[h.pairs.index(p)] = 1.0 / 3
    V = np.vstack([edge, star, tri, V])
    print("n %d  H(K_n) %+.3e" % (n, v0[0]), flush=True)
    for eps in (1e-1, 1e-2, 1e-3):
        W = u[None, :] + eps * (V - u[None, :])   # stays in the simplex, nonnegative for eps <= 1
        val, sl, g = h.values(W, h.GRID)
        i = int(np.argmin(val))
        print("  eps %.0e  edge %+.4e  star %+.4e  triangle %+.4e  min over %d dirs %+.4e (H/eps^2 %+.4f, slack %+.3e, gap12 %.2e)  below -1e-12: %d"
              % (eps, val[0], val[1], val[2], ND, val[i], val[i] / eps ** 2, sl[i], g[i], int((val < -1e-12).sum())), flush=True)
