# T353 sub-1 audit 2 (agent C): does the adaptive method beat max(D_al(P||Q), D_al(Q||P)), not only the same-direction
# value? Float quadrature, row by row in g1 (step 0.005 s, Simpson-free plain sum; both integrands are smooth Gaussian mixtures,
# so the Riemann sum is spectrally accurate), the note's model in its shifted g1 coordinate; SAME on [lo, hi], ANTI elsewhere.
import numpy as np
from math import log
def run(s, lo, hi):
    h = 0.005 * s; g = np.arange(-12 * s - 3, 12 * s + 3, h)
    N = lambda x, m: np.exp(-(x - m) ** 2 / (2 * s * s)) / (s * np.sqrt(2 * np.pi))
    als = (0.25, 0.5, 0.75); acc = {k: np.zeros(3) for k in ("A_pq", "A_qp", "M_pq", "M_qp")}
    for g1 in g:
        for lab, (a, c) in (("A", (2, 1)), ("S", (0, -1))):
            p = 0.5 * N(g1, -2) * N(g, 0) + 0.5 * N(g1, 0) * N(g, a)
            q = 0.5 * N(g1, -1) * N(g, 0) + 0.5 * N(g1, 0) * N(g, c)
            jpq = np.array([np.sum(p ** al * q ** (1 - al)) * h for al in als])
            jqp = np.array([np.sum(q ** al * p ** (1 - al)) * h for al in als])
            if lab == "A": acc["A_pq"] += jpq * h; acc["A_qp"] += jqp * h
            if (lab == "S") == (lo <= g1 <= hi): acc["M_pq"] += jpq * h; acc["M_qp"] += jqp * h
    for i, al in enumerate(als):
        D = {k: log(v[i]) / (al - 1) for k, v in acc.items()}; mx = max(D["A_pq"], D["A_qp"])
        print("s %g al %.2f  pair P||Q %.10f  Q||P %.10f | adaptive x||x' %.10f (beats max: %s)  x'||x %.10f (beats max: %s)" % (
            s, al, D["A_pq"], D["A_qp"], D["M_pq"], D["M_pq"] > mx, D["M_qp"], D["M_qp"] > mx), flush=True)
run(1.0, -2.3, -2.2); run(2.0, -3.05, -2.95); run(0.5, -2.250001, -2.249999)
