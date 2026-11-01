# T354 rigorous remainder, random reshuffling, beta1 = 0, eps >= 0 (agent B, 20 Oct 2026). remainder_rr.py with
# phi(y) = y^(-1/2) replaced by psi(y) = (s + eps)/(s sqrt(y) + eps), s = sqrt(V), so that (s + eps) D = E[g psi(v/V)].
# psi(1) = 1, psi'(1) = -r/2, psi''(1) = r/4 + r^2/2, r = s/(s + eps) (eps = 0: -1/2, 3/4). Cubic remainder |R| <= (e^3/6) M3,
# M3 = max |psi'''| on [1-e, 1+e]. With q = s sqrt(y) + eps, (1/q)''' = -q'''/q^2 + 6 q'q''/q^3 - 6 q'^3/q^4 and every term has
# the same sign and grows as y falls, so M3 = (s + eps)(q'''/q^2 + 6 q'|q''|/q^3 + 6 q'^3/q^4) at y = 1 - e (eps = 0: (15/8)(1-e)^(-7/2)).
# Everything else (the deterministic |y - 1| <= e_p bound, E[g(y-1)] = d K C/V, Q2, X) is unchanged. Argv: beta2 eps.
import sys, itertools, numpy as np
from kfactor import K_rr
b2 = float(sys.argv[1]); EPS = float(sys.argv[2]); d = 1 - b2; n = 10
B = np.array([9.0] + [-1.0] * 9); K = K_rr(n, 0.0, b2)
def moments(g, Z):
    idx = range(n)
    M00 = np.mean(g * Z * Z)
    M0l = np.mean([g[a] * Z[a] * Z[b] for a, b in itertools.permutations(idx, 2)])
    Mjj = np.mean([g[a] * Z[b] * Z[b] for a, b in itertools.permutations(idx, 2)])
    Mjl = np.mean([g[a] * Z[b] * Z[c] for a, b, c in itertools.permutations(idx, 3)])
    return M00, M0l, Mjj, Mjl
def M3(s, e):
    y = 1 - e; q = s * np.sqrt(y) + EPS
    q1, q2, q3 = s / (2 * np.sqrt(y)), s / (4 * y ** 1.5), 3 * s / (8 * y ** 2.5)
    return (s + EPS) * (q3 / q ** 2 + 6 * q1 * q2 / q ** 3 + 6 * q1 ** 3 / q ** 4)
def F(x):
    g = x + B; V = np.mean(g * g); s = np.sqrt(V); r = s / (s + EPS); Z = g * g - V; C = np.mean(g ** 3) - x * V
    p1, p2 = -r / 2, r / 4 + r * r / 2
    M00, M0l, Mjj, Mjl = moments(g, Z)
    Smax = Z[Z > 0].sum(); SA = np.abs(Z).sum()
    Q2 = 0.0; rem = 0.0; ef_max = 0.0; G = np.abs(g).max()
    for p in range(n):
        w = b2 ** np.arange(p + 1)
        s1 = w[1:].sum(); s2 = (w[1:] ** 2).sum()
        Q2 += M00 + 2 * s1 * M0l + s2 * Mjj + (s1 * s1 - s2) * Mjl
        cur = b2 ** p * Smax + (1 - b2 ** p) * SA
        full = b2 ** (p + 1) / (1 - b2 ** n) * (1 - b2 ** (n - 1)) / 2 * SA
        e = d * (cur + full) / V; ef = d * full / V; ef_max = max(ef_max, ef)
        if e >= 1: return None
        rem += G * e ** 3 / 6 * M3(s, e)
    Q2 *= d * d / (V * V) / n; rem /= n
    core = x + p1 * d * K * C / V + p2 / 2 * Q2
    Xlo, Xhi = sorted([0.0, p2 / 2 * x * ef_max ** 2])
    return core + Xlo - rem, core + Xhi + rem
x0 = d * K * 72 / 18 * 3 / (3 + EPS)        # first order: x*(0) s/(s+eps), s = 3 at x = 0
def bis(fn):
    a, c = 0.0, 3 * x0
    for _ in range(60):
        mid = (a + c) / 2
        a, c = (mid, c) if fn(mid) else (a, mid)
    return a
xl = bis(lambda x: F(x)[1] < 0); xh = bis(lambda x: F(x)[0] <= 0)
bad = [x for x in [3 * x0 * k / 600 for k in range(1, 601)] if (x < xl and F(x)[1] >= 0) or (x > xh and F(x)[0] <= 0)]
print("RR beta1 0 beta2 %s eps %s x0(eps) %.6g | zero in [%.7g, %.7g] = x0(eps)*[%.5f, %.5f]; grid violations %d"
      % (sys.argv[1], sys.argv[2], x0, xl, xh, xl / x0, xh / x0, len(bad)))
