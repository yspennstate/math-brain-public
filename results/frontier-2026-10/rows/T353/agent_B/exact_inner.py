# T353 T=2 (agent B, 19 Oct 2026). Semi-exact check with no step-2 grid: at each g1 the inner
# hockey-stick I(g1) = int (p - e q)_+ dg2 is computed from the roots of p - e q (brentq) and normal CDFs.
# Frame of t2b1_adaptive.py: step 1 a1 = -1 (record i), v1 = +1 (record j); step 2 ANTI (a2,v2) = (1,-1)
# (the conjectured answers), SAME (1,1). Outer integral by scipy quad split at the switch points.
import sys, json, numpy as np
from scipy import integrate, optimize
from scipy.stats import norm

def inner(g1, s, e, a2, v2, a1=-1.0, v1=1.0, rev=False):
    wa = .5 * norm.pdf(g1, a1, s); w0 = .5 * norm.pdf(g1, 0, s); wc = .5 * norm.pdf(g1, v1, s)
    # p(g2) = wa N(v2) + wc N(a2);  q(g2) = w0 N(v2) + wc N(0)
    P = [(wa, v2), (wc, a2)]; Q = [(w0, v2), (wc, 0.0)]
    if rev: P, Q = Q, P
    f = lambda y: sum(c * norm.pdf(y, m, s) for c, m in P) - e * sum(c * norm.pdf(y, m, s) for c, m in Q)
    xs = np.linspace(-14 * s - 2, 14 * s + 2, 2001)
    fx = f(xs)
    cuts = [-np.inf]
    for k in range(len(xs) - 1):
        if fx[k] == 0 or fx[k] * fx[k + 1] < 0:
            cuts.append(optimize.brentq(f, xs[k], xs[k + 1], xtol=1e-14) if fx[k] != 0 else xs[k])
    cuts.append(np.inf)
    F = lambda lo, hi: (sum(c * (norm.cdf(hi, m, s) - norm.cdf(lo, m, s)) for c, m in P)
                        - e * sum(c * (norm.cdf(hi, m, s) - norm.cdf(lo, m, s)) for c, m in Q))
    tot = 0.0
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        mid = (max(lo, xs[0] - 1) + min(hi, xs[-1] + 1)) / 2 if np.isfinite(lo) or np.isfinite(hi) else 0.0
        if np.isinf(lo) and np.isinf(hi): mid = 0.0
        elif np.isinf(lo): mid = hi - 1.0
        elif np.isinf(hi): mid = lo + 1.0
        else: mid = (lo + hi) / 2
        if f(mid) > 0: tot += F(lo, hi)
    return tot

def run(s, eps, rev=False):
    e = np.exp(eps)
    A = lambda g: inner(g, s, e, 1.0, -1.0, rev=rev)
    S = lambda g: inner(g, s, e, 1.0, 1.0, rev=rev)
    gs = np.linspace(-1 - 10 * s, 1 + 10 * s, 1201)
    d = np.array([S(g) - A(g) for g in gs])
    sw = [optimize.brentq(lambda g: S(g) - A(g), gs[k], gs[k + 1]) for k in range(len(gs) - 1) if d[k] * d[k + 1] < 0]
    pts = [-np.inf] + sw + [np.inf]
    conj = integrate.quad(A, -np.inf, np.inf, limit=400, epsabs=1e-13)[0]
    tot = 0.0; gain_sets = []
    for lo, hi in zip(pts[:-1], pts[1:]):
        m = (hi - 1 if np.isinf(lo) else (lo + 1 if np.isinf(hi) else (lo + hi) / 2))
        fn = S if S(m) > A(m) else A
        if fn is S: gain_sets.append((lo, hi))
        tot += integrate.quad(fn, lo, hi, limit=400, epsabs=1e-13)[0]
    return conj, tot, sw, gain_sets, float(d.max()), float(gs[d.argmax()])

if __name__ == "__main__":
    out = {}
    for s in [float(x) for x in sys.argv[1].split(",")]:
        for eps in [float(x) for x in sys.argv[2].split(",")]:
            r = {}
            for rev in (False, True):
                conj, tot, sw, gset, dmax, gmax = run(s, eps, rev)
                r["rev" if rev else "fwd"] = dict(conj=conj, switch=tot, gain=tot - conj, switch_pts=sw, same_on=[[float(a), float(b)] for a, b in gset], max_pointwise=dmax, at=gmax)
            cmax = max(r["fwd"]["conj"], r["rev"]["conj"]); smax = max(r["fwd"]["switch"], r["rev"]["switch"])
            r["verdict_gap"] = smax - cmax
            out["%g_%g" % (s, eps)] = r
            print("s %.2f eps %.2f conj fwd %.7f rev %.7f | switch fwd %.7f rev %.7f | gap over max %+.3e | SAME on %s" %
                  (s, eps, r["fwd"]["conj"], r["rev"]["conj"], r["fwd"]["switch"], r["rev"]["switch"], r["verdict_gap"],
                   r["fwd"]["same_on"]), flush=True)
    json.dump(out, open(sys.argv[3], "w"), indent=1)
