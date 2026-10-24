"""Lemma E stress test: for every odd-class product row (nu' = 1 or larger odd) at m = 3, 4, with r = |R| and
w <= 1 - (3/4) 2^{-r}, evaluate  w (4 + sum_i (Ft_i - 4 alpha_i)).  Lemma E says < 2 when nu' = 1."""
import sys, math
sys.path.insert(0, ".")
import rows_v2 as RV, check_identity as CI
import numpy as np
def run(m, pkl=None):
    rows = RV.product_rows(m, pkl)
    worst = (-1e9, None)
    N = 1 << m
    Hm = RV.hadamard(m)
    for row in rows:
        res = CI.analyse(row, m)
        if res is None: continue
        r, pq, nup, odd = res
        if not odd or nup != 1: continue
        V = np.array(row); w = (V*V).sum() / (4.0*N)
        if w > 1 - 0.75 * 2.0**(-r) + 1e-12: continue
        W = Hm @ V; Q = (W*W).astype(float); Q /= Q.sum()
        # actual marginals of active coordinates
        tot = 0.0
        acts = []
        for i in range(m):
            a = sum(Q[U] for U in range(N) if U >> i & 1)
            if 1e-12 < a < 1 - 1e-12: acts.append(a)
        # pair each active coordinate's alpha with its (p,q): match by m = min(a,1-a)
        val = 4.0
        pq_list = list(pq)
        for a in acts:
            mm = min(a, 1 - a)
            # find pair with q^2/(p^2+q^2) == mm
            j = min(range(len(pq_list)), key=lambda t: abs(pq_list[t][1]**2/(pq_list[t][0]**2+pq_list[t][1]**2) - mm))
            p, q = pq_list.pop(j)
            val += CI.Ft(p, q) - 4 * a
        lhs = w * val
        if lhs > worst[0]: worst = (lhs, row, r, pq, w)
    print("m", m, "max of w(4+sum(Ft-4alpha)) over odd rows with nu'=1 and w<=1-(3/4)2^-r:", worst)
run(3); run(4, "../data/prod3_wide.pkl")
