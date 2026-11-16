"""The seed-11 stratum point (n = 5, where R >= lambda fails) edge by edge: w_e, tau_e = |Pi b_e|^2, gamma_e, and the edge
contribution w_e gamma_e (2 tau_e - D) to the left side of the edge-sum target, checked against t104_trace_terms.terms.
usage: python t104_seed11_edges.py
"""
import sys
import numpy as np

here = __file__.replace("t104_seed11_edges.py", "t104_trace_terms.py")
src = open(here, encoding="utf-8").read().split("\nnames = ")[0]
sys.argv = ["t104_trace_terms.py", "5", "0", "0"]
g = {"__file__": here, "__name__": "tt_mod"}
exec(compile(src, here, "exec"), g)
h, terms = g["h"], g["terms"]
W = {(0, 1): 0.12518221, (0, 2): 0.34344950, (0, 3): 0.02497551, (0, 4): 0.00149480, (1, 2): 0.13304193,
     (1, 3): 0.32605611, (1, 4): 0.00032333, (2, 3): 0.04149927, (2, 4): 0.00055063, (3, 4): 0.00342672}
n = 5
w = np.array([W[p] for p in h.pairs]); w /= w.sum()
L = np.zeros((n, n))
for wk, (i, j) in zip(w, h.pairs):
    b = np.zeros(n); b[i], b[j] = 1, -1
    L += wk * np.outer(b, b)
ev, U = np.linalg.eigh(L)
lam = ev[-1]; D = int(np.sum(ev > lam * (1 - 1e-5)))
P = U[:, -D:] @ U[:, -D:].T
d = np.diag(L)
print("eigenvalues", np.round(ev, 6), " lambda %.6f  D %d" % (lam, D))
tot = 0.0
for wk, (i, j) in zip(w, h.pairs):
    b = np.zeros(n); b[i], b[j] = 1, -1
    tau = b @ P @ b; gam = 2 * lam - d[i] - d[j] - 2 * wk
    c = wk * gam * (2 * tau - D); tot += c
    print("edge %d%d  w %.5f  tau %.4f  gamma %+.5f  contribution %+.6f" % (i + 1, j + 1, wk, tau, gam, c))
lam2, D2, X1, X2, X3, Y = terms(w)
print("sum %.9f  terms Y - X1 %.9f  X2 %.6f  X3 %.6f  ratio %.4f" % (tot, Y - X1, X2, X3, (Y - X1) / (X2 + X3)))
