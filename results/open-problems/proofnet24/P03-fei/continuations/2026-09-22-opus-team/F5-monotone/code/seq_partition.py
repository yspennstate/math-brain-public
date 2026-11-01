"""Growth rate b(a) = sup_k (1/k) ln Z_k(a), Z_k(a) = sum_{1<=r_1<...<r_k} prod_j (j/r_j)^a,
for a sequential (rank-order) reference measure.  DP with prefix sums, ranks truncated at R
(the neglected tail is bounded by the last-factor tail and printed)."""
import numpy as np, math, sys
R = 200000
for a in [1.1, 1.2, 1.3, 1.5, 2.0, 3.0]:
    r = np.arange(1, R + 1, dtype=np.float64)
    G = r ** (-a)                       # j = 1
    out = []
    lnscale = 0.0
    for j in range(2, 41):
        P = np.concatenate([[0.0], np.cumsum(G)[:-1]])   # sum_{s<r} G(s)
        G = (j / r) ** a * P
        tot = G.sum()
        G /= tot; lnscale += math.log(tot)
        if j in (5, 10, 20, 40):
            out.append((j, lnscale / j))
    print("a=%.2f  (k, ln Z_k / k): %s" % (a, ["%d:%.4f" % t for t in out]), flush=True)
