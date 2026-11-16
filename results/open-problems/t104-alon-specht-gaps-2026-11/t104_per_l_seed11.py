"""At the seed-11 stratum point (n = 5) and at C_5: per low eigenvector v_l, the gap g_l = lambda - mu_l and the traces
over Top P_l = sum_k P(u_k, v_l), Q_l = sum_k 2 sum_e w_e q_e^2, so the target is sum_l g_l (P_l - Q_l) >= 0.
usage: python t104_per_l_seed11.py
"""
import sys
import numpy as np

here = __file__.replace("t104_per_l_seed11.py", "t104_trace_terms.py")
src = open(here, encoding="utf-8").read().split("\nnames = ")[0]
sys.argv = ["t104_trace_terms.py", "5", "0", "0"]
g = {"__file__": here, "__name__": "tt_mod"}
exec(compile(src, here, "exec"), g)
h, terms = g["h"], g["terms"]
n = 5; c = 2.0 * n / (n - 2)
Bs = []
for (i, j) in h.pairs:
    b = np.zeros(n); b[i], b[j] = 1, -1; Bs.append(b)
Bs = np.array(Bs)
W11 = {(0, 1): 0.12518221, (0, 2): 0.34344950, (0, 3): 0.02497551, (0, 4): 0.00149480, (1, 2): 0.13304193,
       (1, 3): 0.32605611, (1, 4): 0.00032333, (2, 3): 0.04149927, (2, 4): 0.00055063, (3, 4): 0.00342672}
C5 = {(0, 1): 1, (1, 2): 1, (2, 3): 1, (3, 4): 1, (0, 4): 1}
for name, W in [("seed11", W11), ("C5", C5)]:
    w = np.array([W.get(p, 0.0) for p in h.pairs], float); w /= w.sum()
    L = Bs.T @ np.diag(w) @ Bs
    ev, U = np.linalg.eigh(L - h.ONES)
    lam = ev[-1]
    top = [k for k in range(1, n) if ev[k] > lam * (1 - 1e-6)]
    low = [l for l in range(1, n) if ev[l] <= lam * (1 - 1e-6)]
    print("%s  lambda %.6f  low mu %s" % (name, lam, np.round(ev[low], 6)))
    S = 0.0; lam2, D, X1, X2, X3, Y = terms(w)
    for l in low:
        v, mu = U[:, l], ev[l]; P = Q = 0.0
        for k in top:
            u = U[:, k]; p = u * v
            P += mu + c * (lam * p @ p - p @ L @ p) + (1 - lam) * (1 - c * p @ p) / (n - 2)
            Q += 2 * np.sum(w * (Bs @ u) ** 2 * (Bs @ v) ** 2)
        gl = lam - mu; S += gl * (P - Q)
        print("  l mu %.6f  g %.6f  P_l %.6f  Q_l %.6f  Q/P %.4f  g(P-Q) %+.6f" % (mu, gl, P, Q, Q / P, gl * (P - Q)))
    print("  sum g(P-Q) %.9f   trace form X1+X2+X3-Y %.9f" % (S, X1 + X2 + X3 - Y))
