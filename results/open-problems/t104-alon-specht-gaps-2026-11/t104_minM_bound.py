"""How much of the cone does the cheap bound H >= (n-2) lambda_min(M) - need settle?

H is (n-2) times a positive-weighted average of Rayleigh quotients of M on V_[n-2,2], minus need, so it lies between
(n-2) lambda_min(M) - need and the slack (n-2) lambda_max(M) - need. Samples: the same start families as the search.
usage: python t104_minM_bound.py nmin nmax N
"""
import importlib.util
import sys
import numpy as np

here = __file__.replace("t104_minM_bound.py", "t104_np_hsearch.py")
nmin, nmax, N = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
for n in range(nmin, nmax + 1):
    sys.argv = ["t104_np_hsearch.py", str(n), "1", "1", "1", "1"]
    spec = importlib.util.spec_from_file_location("hs%d" % n, here)
    h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
    rng = np.random.default_rng(11)
    W = h.starts(N, rng)
    W = W / W.sum(1, keepdims=True)
    L = np.einsum("km,nk,kj->nmj", h.E, W, h.E)
    lam = np.linalg.eigvalsh(L - h.ONES)[:, -1]
    need = (n - 1) * lam - 2.0
    M = np.einsum("nk,kab->nab", W, h.SW)
    em = np.linalg.eigvalsh(M)
    low = (n - 2) * em[:, 0] - need
    print("n %d  samples %d  need<=0: %.3f  cheap bound settles: %.3f  min lambda_min(M) %.4f  at K_n 4/n = %.4f"
          % (n, N, (need <= 0).mean(), (low >= 0).mean(), em[:, 0].min(), 4.0 / n), flush=True)
