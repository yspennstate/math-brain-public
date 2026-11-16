"""Check of the sub-clique lemma's key step: at the uniform K_k inside n vertices every projected
a = B^t sym(u (x) v), u in Top, v in Zero, is an eigenvector of M with eigenvalue 2/(k-1)."""
import importlib.util
import sys
import numpy as np

here = __file__.replace("t104_subclique_eig.py", "t104_np_hsearch.py")
for n in range(5, 9):
    sys.argv = ["t104_np_hsearch.py", str(n), "1", "1", "1", "1"]
    spec = importlib.util.spec_from_file_location("hs%d" % n, here)
    h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
    rng = np.random.default_rng(1)
    for k in range(3, n):
        w = np.array([1.0 if (i < k and j < k) else 0.0 for (i, j) in h.pairs]); w /= w.sum()
        M = np.tensordot(w, h.SW, axes=1)
        worst = 0.0; amin = np.inf
        for _ in range(50):
            u = np.zeros(n); u[:k] = rng.normal(size=k); u[:k] -= u[:k].mean()
            v = np.zeros(n); v[k:] = rng.normal(size=n - k); v[:k] = rng.normal()
            v -= v.mean()
            s = ((np.outer(u, v) + np.outer(v, u)) / 2 ** 0.5).ravel()
            a = h.B.T @ s
            amin = min(amin, np.linalg.norm(a))
            worst = max(worst, np.linalg.norm(M @ a - 2.0 / (k - 1) * a) / np.linalg.norm(a))
        print("n %d k %d  max |M a - (2/(k-1)) a| / |a| over 50 pairs: %.1e  (smallest |a| %.2f)" % (n, k, worst, amin))
