# T354 rigorous enclosure under random reshuffling WITH momentum, eps = 0 (agent B, 20 Oct 2026). Extends remainder_rr.py.
# m_k = (1-b1) sum_i b1^i g_{k-i}, |m_k| <= G. The deterministic bound |v_k/V - 1| <= eps_p is the same as in remainder_rr.py, so
#   sqrt(V) D = sum_i (1-b1) b1^i { E[g_{k-i}] - (1/2) E[g_{k-i}(y-1)] + (3/8) E[g_{k-i}(y-1)^2] } + E[m_k r],  |E[m_k r]| <= G max r,
#   E[g_{k-i}] = f';  sum_i (1-b1) b1^i E[g_{k-i}(y-1)] = d K C/V with K = K_rr(n, b1, b2) (kfactor.py);
#   E[g_{k-i}(y-1)^2] = (both Z lags in lag i's epoch: exact from the moments M00, M0l, Mjj, Mjl) + f' * (both in one other epoch),
#   the latter in [0, f' eps_tot^2] for f' >= 0 (other patterns vanish: an epoch holding a single Z and no g has E Z = 0).
# Lags truncated at L with (b1^L + b2^L) negligible (tail of the linear and quadratic sums bounded and added to the remainder).
# Argv: beta2 beta1. Model: n = 10, a_i = 1, b = (9, -1 x 9).
import sys, itertools, numpy as np
from kfactor import K_rr
b2 = float(sys.argv[1]); b1 = float(sys.argv[2]); d = 1 - b2; n = 10
B = np.array([9.0] + [-1.0] * 9); K = K_rr(n, b1, b2)
L = int(np.ceil(60 * max(1 / d, 1 / (1 - b1)) / n)) * n + n
lag = np.arange(L)
def moments(g, Z):
    idx = range(n)
    return (np.mean(g * Z * Z), np.mean([g[a] * Z[a] * Z[b] for a, b in itertools.permutations(idx, 2)]),
            np.mean([g[a] * Z[b] * Z[b] for a, b in itertools.permutations(idx, 2)]),
            np.mean([g[a] * Z[b] * Z[c] for a, b, c in itertools.permutations(idx, 3)]))
def F(x):
    g = x + B; V = np.mean(g * g); Z = g * g - V; C = np.mean(g ** 3) - x * V
    M00, M0l, Mjj, Mjl = moments(g, Z); Smax = Z[Z > 0].sum(); SA = np.abs(Z).sum(); G = np.abs(g).max()
    wm = (1 - b1) * b1 ** lag; c = d * b2 ** lag / V
    Q = 0.0; rem = 0.0; etot_max = 0.0
    for p in range(n):
        ep = np.where(lag <= p, 0, (lag - p - 1) // n + 1)
        S1 = np.bincount(ep, weights=c); S2 = np.bincount(ep, weights=c * c)
        s1, s2 = S1[ep], S2[ep]
        Q += np.sum(wm * (c * c * M00 + 2 * c * (s1 - c) * M0l + (s2 - c * c) * Mjj + ((s1 - c) ** 2 - (s2 - c * c)) * Mjl))
        cur = b2 ** p * Smax + (1 - b2 ** p) * SA
        full = b2 ** (p + 1) / (1 - b2 ** n) * (1 - b2 ** (n - 1)) / 2 * SA
        eps = d * (cur + full) / V; etot_max = max(etot_max, eps)
        if eps >= 1: return None
        rem += G * 5 / 16 * eps ** 3 * (1 - eps) ** -3.5
    Q /= n; rem /= n
    tail = b1 ** L * (G + G * etot_max + G * etot_max ** 2)       # truncated momentum lags, crude
    core = x - 0.5 * d * K * C / V + 3 / 8 * Q
    return core - rem - tail, core + 3 / 8 * x * etot_max ** 2 + rem + tail
x0 = d * K * 72 / 18
def bis(fn):
    a, cc = 0.0, 3 * x0
    for _ in range(60):
        mid = (a + cc) / 2
        a, cc = (mid, cc) if fn(mid) else (a, mid)
    return a
xl = bis(lambda x: F(x)[1] < 0); xh = bis(lambda x: F(x)[0] <= 0)
bad = [x for x in [3 * x0 * k / 300 for k in range(1, 301)] if (x < xl and F(x)[1] >= 0) or (x > xh and F(x)[0] <= 0)]
print("RR beta1 %s beta2 %s K %.6f x0 %.6g | zero enclosed in [%.7g, %.7g] = x0*[%.5f, %.5f]; grid violations %d"
      % (sys.argv[2], sys.argv[1], K, x0, xl, xh, xl / x0, xh / x0, len(bad)))
