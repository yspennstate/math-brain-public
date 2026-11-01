# T353 second audit of the T=3 certificate and the every-T reduction (agent C, 19 Oct 2026).
# Own code throughout except where cert_t3_arb.diff is called on purpose as the object under audit.
#  (1) the reduction: cert_t3_arb.diff(g1, g2) == beta_3 * Delta(A, G) with Delta from MY exact-root integrator and MY
#      map g -> (A, G) (normalised coordinates gn1 = -g1, gn2 = g2, x_t = exp(gn_t - 1/2));
#  (2) the transfer: for m = 3, 4, 6 a prefix built to land on the same (A, G) as a B point, I_SAME - I_ANTI computed
#      DIRECTLY from the m-batch mixture (no Delta), compared with beta_T * Delta and checked positive;
#  (3) the range: e A / G^2 over B's corners, and the m = 2 Jacobian sign over B;
#  (4) Monte Carlo of D(P_S||Q_S) and the last-step gain at T = 2, 3, 4 by a different integrator (a y grid, vectorised).
import sys, math
import numpy as np
from scipy.stats import norm
from scipy.optimize import brentq
sys.path.insert(0, "../agent_B")
E = math.exp(0.5)
YS = np.linspace(-14, 16, 3001)

def pos_int(terms):
    c = np.array([t[0] for t in terms]); m = np.array([t[1] for t in terms])
    f = lambda y: float((c * norm.pdf(y - m)).sum())
    v = (c[:, None] * norm.pdf(YS[None, :] - m[:, None])).sum(0)
    idx = np.nonzero(v[:-1] * v[1:] < 0)[0]
    cuts = [-np.inf] + [brentq(f, YS[k], YS[k + 1], xtol=1e-15) for k in idx] + [np.inf]
    tot = 0.0
    for a, b in zip(cuts[:-1], cuts[1:]):
        mid = 0.5 * (a + b) if np.isfinite(a) and np.isfinite(b) else (b - 1.0 if np.isfinite(b) else (a + 1.0 if np.isfinite(a) else 0.0))
        if f(mid) > 0:
            tot += float((c * (norm.cdf(b - m) - norm.cdf(a - m))).sum())
    return tot

def last_step(al, be, ga, mode):
    # p = al phi(y) + be phi(y - mx), q = ga phi(y) + be phi(y - mq); ANTI (mx, mq) = (2, 1), SAME (0, -1)
    mx, mq = (2.0, 1.0) if mode == "anti" else (0.0, -1.0)
    return pos_int([(al, 0.0), (be, mx), (-E * ga, 0.0), (-E * be, mq)])

def Delta(A, G):
    return last_step(A, 1.0, G, "same") - last_step(A, 1.0, G, "anti")

def AG(xs):
    xs = np.asarray(xs, float); return float((xs ** 2).sum() / math.e), float(xs.sum())

def direct(gn):
    # the m-batch mixture written out: record in batch t <= m (mean 2 | 1 in coordinate t), or in batch T
    m = len(gn); T = m + 1; ph = norm.pdf
    al = sum(ph(gn[t] - 2) * np.prod([ph(gn[s]) for s in range(m) if s != t]) for t in range(m)) / T
    ga = sum(ph(gn[t] - 1) * np.prod([ph(gn[s]) for s in range(m) if s != t]) for t in range(m)) / T
    be = np.prod([ph(g) for g in gn]) / T
    return last_step(al, be, ga, "same") - last_step(al, be, ga, "anti"), be

print("(1) cert diff vs beta_3 * Delta(A, G), my map")
try:
    from cert_t3_arb import diff as cdiff
    from flint import arb
    have = True
except Exception as e:
    have = False; print("  cert import failed:", e)
pts = [(-0.1, 2.2), (0.3, 2.3), (0.1, 2.25), (-0.1, 2.3), (0.3, 2.2), (0.0, 1.8), (-0.5, 2.4)]
for g1, g2 in pts:
    gn = (-g1, g2); xs = [math.exp(g - 0.5) for g in gn]; A, G = AG(xs)
    mine_direct, be = direct(gn)
    mine = be * Delta(A, G)
    c = float(cdiff(arb(str(g1)), arb(str(g2))).mid()) if have else float("nan")
    print("  (%5.2f, %4.2f) cert %+.12e  beta*Delta %+.12e  direct %+.12e  eA/G^2 %.4f" % (g1, g2, c, mine, mine_direct, math.e * A / G ** 2))

print("(2) transfer to m = 3, 4, 6: prefix on the same (A, G) as B points")
for g1, g2 in [(-0.1, 2.2), (0.1, 2.25), (0.3, 2.3)]:
    xs2 = [math.exp(-g1 - 0.5), math.exp(g2 - 0.5)]; A0, G0 = AG(xs2); S0 = math.e * A0
    d3 = Delta(A0, G0)
    for m in (3, 4, 6):
        # m - 2 small equal coordinates c, the remaining two solve a + b = G0 - (m-2)c, a^2 + b^2 = S0 - (m-2)c^2
        c = 0.02; k = m - 2; Gs, Ss = G0 - k * c, S0 - k * c * c
        disc = 2 * Ss - Gs * Gs; assert disc > 0, disc
        a, b = (Gs - math.sqrt(disc)) / 2, (Gs + math.sqrt(disc)) / 2
        xs = [a, b] + [c] * k; A, G = AG(xs)
        gn = [math.log(x) + 0.5 for x in xs]
        dd, be = direct(gn)
        print("  B point (%5.2f, %4.2f) m=%d: |dA| %.1e |dG| %.1e  direct %+.6e  beta*Delta %+.6e  ratio %.9f  positive %s" % (
            g1, g2, m, abs(A - A0), abs(G - G0), dd, be * d3, dd / (be * d3), dd > 0))

print("(3) range over B and the m = 2 Jacobian")
rhos = []
for g1 in (-0.1, 0.3):
    for g2 in (2.2, 2.3):
        r = math.exp(g1 + g2); rhos.append((1 + r * r) / (1 + r) ** 2)
print("  eA/G^2 on B corners: min %.4f max %.4f (m=2 region is (1/2, 1))" % (min(rhos), max(rhos)))
print("  det d(A,G)/d(x1,x2) = (2/e)(x1 - x2); x2/x1 = exp(g1+g2) >= exp(2.1) on B, so det < 0 throughout: local diffeo")

print("(4) Monte Carlo, y-grid integrator (independent of the root method)")
rng = np.random.default_rng(20261019)
yg = np.linspace(-9, 12, 4201); dy = yg[1] - yg[0]
p0 = norm.pdf(yg); p2 = norm.pdf(yg - 2); p1 = norm.pdf(yg - 1); pm1 = norm.pdf(yg + 1)
for T, N in ((2, 200000), (3, 200000), (4, 200000)):
    m = T - 1; Ia, Ig = [], []
    for _ in range(N // 2000):
        g = rng.standard_normal((2000, m)); xs = np.exp(g - 0.5)
        A = (xs ** 2).sum(1) / math.e; G = xs.sum(1)
        anti = np.clip(A[:, None] * p0 + p2 - E * (G[:, None] * p0 + p1), 0, None).sum(1) * dy
        same = np.clip(A[:, None] * p0 + p0 - E * (G[:, None] * p0 + pm1), 0, None).sum(1) * dy
        Ia.append(anti); Ig.append(np.clip(same - anti, 0, None))
    Ia = np.concatenate(Ia) / T; Ig = np.concatenate(Ig) / T
    print("  T=%d  D(P_S||Q_S) %.5f +- %.5f   last-step gain %.4e +- %.1e" % (T, Ia.mean(), Ia.std() / math.sqrt(N), Ig.mean(), Ig.std() / math.sqrt(N)))
