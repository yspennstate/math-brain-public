# T354 rigorous second-order expansion with a cubic remainder, random reshuffling, beta1 = 0, eps = 0 (agent B, 20 Oct 2026).
# Frozen x; sample k sits at position p (0..n-1) of its epoch, uniformly. y = v_k/V = 1 + sum_{j>=0} d beta2^j Z_{k-j}/V, Z = g^2 - V.
# DETERMINISTIC BOUND |y - 1| <= eps_p. Current epoch (lags 0..p, distinct indices): sum beta^j Z_j = beta^p sum Z_j + sum (beta^j - beta^p) Z_j,
# so |.| <= beta^p Smax + (1 - beta^p) sum_i |Z_i|, Smax = sum of the positive Z_i (= sum of |negative| ones, since sum Z_i = 0).
# Each earlier full epoch starting at lag s is a permutation of all Z_i (sum 0): |sum_r beta^(s+r) Z| <= beta^s (1 - beta^(n-1))/2 sum_i |Z_i|.
# Then phi(y) = y^(-1/2) = 1 - (y-1)/2 + (3/8)(y-1)^2 + r, |r| <= (5/16) eps^3 (1 - eps)^(-7/2), and
#   sqrt(V) D = f' - (1/2) E[g (y-1)] + (3/8) E[g (y-1)^2] + E[g r],
#   E[g (y-1)] = d K C/V exactly (K = K_rr, kfactor.py: same index C, same epoch other index -C/(n-1), other epochs 0),
#   E[g (y-1)^2] = Q2 + X: Q2 = the terms with both Z lags in the current epoch (exact, from the without-replacement moments of
#   (g_a, Z_b, Z_c) by enumeration); X = terms with both lags in one earlier epoch = f' E[(epoch part)^2], 0 <= X/f' <= eps_full^2
#   (mixed current/earlier or two different earlier epochs vanish: the earlier epoch is independent and E Z = 0).
# Argv: beta2. Model: n = 10, a_i = 1, b = (9, -1 x 9) (f'(x) = x).
import sys, itertools, numpy as np
from kfactor import K_rr
b2 = float(sys.argv[1]); d = 1 - b2; n = 10
B = np.array([9.0] + [-1.0] * 9); K = K_rr(n, 0.0, b2)
def moments(g, Z):
    idx = range(n)
    M00 = np.mean(g * Z * Z)
    M0l = np.mean([g[a] * Z[a] * Z[b] for a, b in itertools.permutations(idx, 2)])
    Mjj = np.mean([g[a] * Z[b] * Z[b] for a, b in itertools.permutations(idx, 2)])
    Mjl = np.mean([g[a] * Z[b] * Z[c] for a, b, c in itertools.permutations(idx, 3)])
    return M00, M0l, Mjj, Mjl
def F(x):
    g = x + B; V = np.mean(g * g); Z = g * g - V; C = np.mean(g ** 3) - x * V
    M00, M0l, Mjj, Mjl = moments(g, Z)
    Smax = Z[Z > 0].sum(); SA = np.abs(Z).sum()
    Q2 = 0.0; rem = 0.0; ef_max = 0.0
    for p in range(n):
        w = b2 ** np.arange(p + 1)                       # lags 0..p in the current epoch
        s1 = w[1:].sum(); s2 = (w[1:] ** 2).sum()
        Q2 += M00 + 2 * s1 * M0l + s2 * Mjj + (s1 * s1 - s2) * Mjl
        cur = b2 ** p * Smax + (1 - b2 ** p) * SA
        full = b2 ** (p + 1) / (1 - b2 ** n) * (1 - b2 ** (n - 1)) / 2 * SA
        eps = d * (cur + full) / V; ef = d * full / V; ef_max = max(ef_max, ef)
        if eps >= 1: return None
        G = np.abs(g).max()
        rem += G * 5 / 16 * eps ** 3 * (1 - eps) ** -3.5
    Q2 *= d * d / (V * V) / n; rem /= n
    core = x - 0.5 * d * K * C / V + 3 / 8 * Q2
    Xlo, Xhi = sorted([0.0, x * ef_max ** 2])
    return core + 3 / 8 * Xlo - rem, core + 3 / 8 * Xhi + rem, d * K * C / (2 * V)
x0 = d * K * 72 / 18
def bis(fn):
    a, c = 0.0, 3 * x0
    for _ in range(60):
        mid = (a + c) / 2
        a, c = (mid, c) if fn(mid) else (a, mid)
    return a
xl = bis(lambda x: F(x)[1] < 0); xh = bis(lambda x: F(x)[0] <= 0)
bad = [x for x in [3 * x0 * k / 600 for k in range(1, 601)] if (x < xl and F(x)[1] >= 0) or (x > xh and F(x)[0] <= 0)]
lo, hi, lead = F(x0)
print("RR beta1 0 beta2 %s K %.6f x0 %.6g | zero enclosed in [%.7g, %.7g] = x0*[%.5f, %.5f] (width/x0 %.2g); grid violations %d"
      % (sys.argv[1], K, x0, xl, xh, xl / x0, xh / x0, (xh - xl) / x0, len(bad)))
# second-order centre: the zero of core alone (no X, no cubic remainder)
xc = bis(lambda x: F(x)[0] + F(x)[1] < 0)  # midpoint of the bounds is core + (3/8) X/2, X tiny
print("  second-order centre x*/x0 ~ %.5f" % (xc / x0))
