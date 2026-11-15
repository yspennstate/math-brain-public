"""H at a uniformly weighted K_k on k of the n vertices (the rest isolated): the top eigenvalue of L has
multiplicity k - 1, so these sit on the degenerate-top stratum. Prints H (and its limit along small random
perturbations, since H can jump where every gap at the top vanishes) and the slack.
usage: python t104_subclique.py nmin nmax
"""
import importlib.util
import sys
import numpy as np

here = __file__.replace("t104_subclique.py", "t104_np_hsearch.py")
nmin, nmax = int(sys.argv[1]), int(sys.argv[2])
for n in range(nmin, nmax + 1):
    sys.argv = ["t104_np_hsearch.py", str(n), "1", "1", "1", "1"]
    spec = importlib.util.spec_from_file_location("hs%d" % n, here)
    h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
    rng = np.random.default_rng(3)
    for k in range(2, n + 1):
        w = np.array([1.0 if (i < k and j < k) else 0.0 for (i, j) in h.pairs]); w /= w.sum()
        v, sl, g = h.values(w[None, :], h.GRID)
        V = rng.exponential(size=(200, h.m)); V /= V.sum(1, keepdims=True)
        lim = h.values(w[None, :] + 1e-6 * (V - w[None, :]), h.GRID)[0].min()
        print("n %d  K_%d  H %+.6f  min H at 1e-6 over 200 dirs %+.6f  slack %+.6f  gap12 %.1e"
              % (n, k, v[0], lim, sl[0], g[0]), flush=True)
