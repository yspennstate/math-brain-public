"""Targeted exact checks at n = 20 and 22: every lemma, and Lemma 2 pointwise in x for every
coordinate, on the adversarial profiles that came out worst at smaller n.
usage: python targeted_large.py n
"""
import math, sys, time
import numpy as np
import ltf_ref as L

L.be_polite()
n = int(sys.argv[1])


def theta_at_quantile(w, a):
    v = np.sort(L.linear_values(w).astype(np.float64))
    return float(v[min(len(v) - 1, int(round(a * len(v))))])


cases = []
cases.append(("maj theta=0 (ties at 0 for even n)", [1] * n, 0))
cases.append(("maj theta=-2", [1] * n, -2))
cases.append(("sym near-AND theta=n-4", [1] * n, n - 4))
g5 = [0.5 ** j for j in range(n)]
cases.append(("geom0.5 (lexicographic) near edge", g5, theta_at_quantile(g5, 1 - 2 ** -12)))
cases.append(("geom0.5 (lexicographic) balanced", g5, theta_at_quantile(g5, 0.5) + 1e-9))
g9 = [0.9 ** j for j in range(n)]
cases.append(("geom0.9 balanced (attained value)", g9, theta_at_quantile(g9, 0.5)))
nt = [10 ** 6 + j for j in range(n)]
cases.append(("near-ties M+j, balanced", nt, int(theta_at_quantile(nt, 0.5))))
ht = [10 ** 6] * 2 + [j + 1 for j in range(n - 2)]
cases.append(("heavy pair + tiny, heavy sum 0", ht, 0))
hg = [n - 1] + [1] * (n - 1)
cases.append(("one huge weight n-1, theta 0", hg, 0))
fib = [1, 2]
while len(fib) < n:
    fib.append(fib[-1] + fib[-2])
fib = fib[::-1][:n]
cases.append(("fibonacci balanced", fib, int(theta_at_quantile(fib, 0.5))))
wz = [5, 5, 3, 0, 2, 0, 1] + [1] * (n - 7)
cases.append(("zero weights present", wz, 1))

t0 = time.time()
for name, w, t in cases:
    tab = L.ltf_table(w, t)
    sp = L.Spec(tab)
    absw = [abs(x) for x in w]
    out = L.lemma_checks(sp, absw)
    r, U, N = L.ranks_and_U(absw)
    inf = sp.influences()
    pa = pb = pc = 0.0
    for i in range(n):
        if inf[i] < 1e-15 or N[i] < 2:
            continue
        cs = sorted(set([c for c in [1.0, 2.0, 3.0, N[i] / 4, N[i] / 2, N[i]] if 0 < c <= N[i]]))
        for (c, maxP, ra, rb, rc) in L.lemma2_pointwise(tab, absw, i, U[i], N[i], cs):
            pa, pb, pc = max(pa, ra), max(pb, rb), max(pc, rc)
    print(f"[{time.time() - t0:6.0f}s] n={n} {name}: H/I={out['HI']:.5f} L2avg={out['L2avg']:.4f} "
          f"L3={out['L3']:.4f} L3tail={out['L3tail']:.4f} L4={out['L4']:.4f} L5={out['L5']:.4f} "
          f"L6={out['L6']:.4f} T1={out['T1']:.4f} | pointwise: vs lemma {pa:.4f}, vs sqrt-LO {pb:.4f}, "
          f"vs exact LO {pc:.9f}", flush=True)
