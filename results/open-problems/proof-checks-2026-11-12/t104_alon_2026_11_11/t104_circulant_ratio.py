"""The margin ratio sum_l g_l Q_l / sum_l g_l P_l (target: at most 1) on circulant weightings of K_n, n odd: every nonzero
eigenvalue of a circulant on odd n is double, so every circulant lies on the double-top stratum. Prints C_n, then 40
random circulants (weight a_d on all edges at cyclic distance d, d = 1..(n-1)/2) per n, and the largest ratio found.
usage: python t104_circulant_ratio.py n seed
"""
import sys
import numpy as np

n, SEED = int(sys.argv[1]), int(sys.argv[2])
here = __file__.replace("t104_circulant_ratio.py", "t104_trace_terms.py")
src = open(here, encoding="utf-8").read().split("\nnames = ")[0]
sys.argv = ["t104_trace_terms.py", str(n), "0", "0"]
g = {"__file__": here, "__name__": "tt_mod"}
exec(compile(src, here, "exec"), g)
h = g["h"]
c = 2.0 * n / (n - 2)
Bs = []
for (i, j) in h.pairs:
    b = np.zeros(n); b[i], b[j] = 1, -1; Bs.append(b)
Bs = np.array(Bs)


def ratio(w, tol=1e-7):
    w = w / w.sum()
    L = Bs.T @ np.diag(w) @ Bs
    ev, U = np.linalg.eigh(L - h.ONES)
    lam = ev[-1]
    top = [k for k in range(1, n) if ev[k] > lam * (1 - tol)]
    low = [l for l in range(1, n) if ev[l] <= lam * (1 - tol)]
    num = den = 0.0
    for l in low:
        v, mu = U[:, l], ev[l]; P = Q = 0.0
        for k in top:
            u = U[:, k]; p = u * v
            P += mu + c * (lam * p @ p - p @ L @ p) + (1 - lam) * (1 - c * p @ p) / (n - 2)
            Q += 2 * np.sum(w * (Bs @ u) ** 2 * (Bs @ v) ** 2)
        num += (lam - mu) * Q; den += (lam - mu) * P
    return lam, len(top), num / den


def circ(a):
    w = np.zeros(h.m)
    for k, (i, j) in enumerate(h.pairs):
        d = min(j - i, n - (j - i)); w[k] = a[d - 1]
    return w


half = (n - 1) // 2
lam, D, r = ratio(circ(np.eye(half)[0]))
print("C_%d  lambda %.6f  D %d  ratio %.6f" % (n, lam, D, r), flush=True)
rng = np.random.default_rng(SEED); best = (r, "C_n")
for t in range(40):
    a = rng.random(half) ** rng.choice([1, 3, 6])
    lam, D, r = ratio(circ(a))
    if D != 2:
        continue
    if r > best[0]:
        best = (r, " ".join("%.3f" % x for x in a / a.sum()))
print("n %d  largest ratio %.6f at distance weights %s" % (n, best[0], best[1]), flush=True)
