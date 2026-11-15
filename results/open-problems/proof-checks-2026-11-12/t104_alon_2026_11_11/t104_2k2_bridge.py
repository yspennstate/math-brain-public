"""H along two disjoint edges joined by a light bridge: w = (1-t)/2 on 14 and 23, t on 12 (n = 5, vertex 5 isolated).
At t = 0 the top eigenvalue is double and H = 1 (clique-union lemma, D = 2); for t > 0 it splits. Prints H, the
top gap gap12 = lambda_1 - lambda_2 (lambda_1 = 1 + O(t^2)) and (1 - H)/gap12, to show how fast H leaves 1 off the stratum.
beta runs over the search grid extended by 1e7..1e10 (the search grid stops at 1e6, too small when gap12 < 1e-5).
usage: python t104_2k2_bridge.py
"""
import importlib.util
import sys
import numpy as np

here = __file__.replace("t104_2k2_bridge.py", "t104_np_hsearch.py")
sys.argv = ["t104_np_hsearch.py", "5", "1", "1", "1", "1"]
spec = importlib.util.spec_from_file_location("hs", here)
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
idx = {p: k for k, p in enumerate(h.pairs)}
for t in [0.0, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 0.05, 0.1]:
    w = np.zeros(h.m)
    w[idx[(0, 3)]] = w[idx[(1, 2)]] = (1 - t) / 2
    w[idx[(0, 1)]] = t
    v, sl, g = h.values(w[None, :] + 1e-300, h.GRID + [1e7, 1e8, 1e9, 1e10])
    lam1 = float(np.linalg.eigvalsh(h.E.T @ np.diag(w / w.sum()) @ h.E)[-1])
    r = (1 - v[0]) / g[0] if g[0] > 0 else float("nan")
    print("t %.0e  H %+.9f  gap12 %.3e  lam1 %.6f  (1-H)/gap12 %+.4f  upper (n-2)topM-need %+.4f" % (t, v[0], g[0], lam1, r, sl[0]), flush=True)
