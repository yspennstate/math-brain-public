"""C_5 (n = 5, w = 1/5 on the cycle) as the test case for the edge-sum target: lambda = (2/5)(1 + cos(pi/5)),
tau_e = 2 lambda on every edge, gamma_e = 2 lambda - 6/5, X1 = 2 gamma, E = gamma (4 lambda - 2). Prints these
closed forms against t104_trace_terms.terms, and X2, X3.
usage: python t104_c5_terms.py
"""
import sys
import numpy as np

here = __file__.replace("t104_c5_terms.py", "t104_trace_terms.py")
src = open(here, encoding="utf-8").read().split("\nnames = ")[0]
sys.argv = ["t104_trace_terms.py", "5", "0", "0"]
g = {"__file__": here, "__name__": "tt_mod"}
exec(compile(src, here, "exec"), g)
h, terms = g["h"], g["terms"]
idx = {p: k for k, p in enumerate(h.pairs)}
w = np.zeros(h.m)
for e in [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)]:
    w[idx[e]] = 0.2
lam, D, X1, X2, X3, Y = terms(w)
lam0 = 0.4 * (1 + np.cos(np.pi / 5)); gam = 2 * lam0 - 1.2
print("lambda %.12f closed %.12f" % (lam, lam0))
print("X1 %.12f closed 2 gamma %.12f" % (X1, 2 * gam))
print("Y - X1 %.12f closed gamma (4 lambda - 2) %.12f" % (Y - X1, gam * (4 * lam0 - 2)))
print("X2 %.12f  X3 %.12f  ratio (Y - X1)/(X2 + X3) %.6f" % (X2, X3, (Y - X1) / (X2 + X3)))
