# Exact Delta_v / Inf_v for the perfect matching M_k = OR_{i<=k} (x_{a_i} AND x_{b_i}) at any k, from the product
# structure: for f = OR of independent parts h_i with g_i = 1 - h_i, F = 2 prod g_i - 1 and P(S) = 4 prod_i w_i(S_i) for S
# nonempty, where w_i(A) = ghat_i(A)^2 has total p_i = Pr[h_i = 0]. So, with H_i = -sum_A w_i(A) log2 w_i(A),
#   H(f) = -8 prod p + 4 sum_i (prod_{j != i} p_j) H_i - phi(4 prod w_i(empty)) + phi((2 prod p - 1)^2).
# Restricting an endpoint v of edge 1: f_0 = M_{k-1} (edge 1 killed), f_1 = x_u OR M_{k-1}.
import math
def phi(t): return 0.0 if t <= 0 else -t * math.log2(t)
def H_or(parts):
    """parts: list of (p, Hpart, w_empty)"""
    prodp = 1.0; prodw = 1.0
    for p, h, we in parts: prodp *= p; prodw *= we
    tot = -8 * prodp
    for i, (p, h, we) in enumerate(parts):
        tot += 4 * (prodp / p) * h
    return tot - phi(4 * prodw) + phi((2 * prodp - 1) ** 2)
edge = (0.75, -(9/16 * math.log2(9/16) + 3 * (1/16) * math.log2(1/16)), 9/16)
single = (0.5, 1.0, 0.25)
# sanity: brute force for small k
import numpy as np
from gdnf import truth_table
def brute(k):
    n = 2 * k; f = truth_table(n, [(2*i, 2*i+1) for i in range(k)])
    N = 1 << n; G = np.where(f, -1.0, 1.0)
    h = 1; a = G.copy()
    while h < N:
        a = a.reshape(-1, 2, h); u = a[:, 0, :].copy(); w = a[:, 1, :]; a[:, 0, :] = u + w; a[:, 1, :] = u - w; a = a.reshape(N); h *= 2
    P = (a / N) ** 2
    return float(-(P[P > 0] * np.log2(P[P > 0])).sum())
for k in (1, 2, 3, 4, 6, 8):
    print('k=%d: product formula H %.10f  brute %.10f' % (k, H_or([edge] * k), brute(k)))
best = (0, 0)
for k in list(range(1, 60)) + [80, 100, 150, 200, 400, 1000]:
    Hk = H_or([edge] * k)
    H0 = H_or([edge] * (k - 1)) if k > 1 else 0.0
    H1 = H_or([single] + [edge] * (k - 1))
    delta = Hk - 0.5 * (H0 + H1)
    inf = 0.5 * 0.75 ** (k - 1)
    r = delta / inf
    if r > best[0]: best = (r, k)
    if k <= 20 or k in (30, 40, 50, 59, 80, 100, 150, 200, 400, 1000):
        print('k=%4d  Pr[M=1]=%.4f  Delta/Inf = %.5f' % (k, 1 - 0.75 ** k, r))
print('sup over k of Delta/Inf for perfect matchings: %.5f at k=%d' % best)
