# T353 audit (agent C, 19 Oct 2026): independent re-check of REFUTATION_T2 with different code.
# Inner integral exact: for fixed g1 the step-2 densities are equal-variance Gaussian mixtures, so
# p(y) - E q(y) = sum_k c_k phi(y - m_k); its positive part is integrated between sign changes (bracketed on a
# vectorised grid, refined by brentq) with exact normal CDFs. Outer integral: composite Simpson on a fine g1 grid,
# the adaptive policy applied pointwise (SAME where I_same > I_anti). Both orders; the conjectured pair by the same code.
import sys
import numpy as np
from scipy.stats import norm
from scipy.optimize import brentq
from scipy.integrate import simpson

s = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
eps = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
E = np.exp(eps)
phi = lambda x: norm.pdf(x, scale=s)
YS = np.linspace(-12 * s - 4, 12 * s + 4, 2001)


def pos_int(terms):
    c = np.array([t[0] for t in terms]); m = np.array([t[1] for t in terms])
    f = lambda y: float((c * norm.pdf(y - m, scale=s)).sum())
    v = (c[:, None] * norm.pdf(YS[None, :] - m[:, None], scale=s)).sum(0)
    idx = np.nonzero(v[:-1] * v[1:] < 0)[0]
    cuts = [-np.inf] + [brentq(f, YS[k], YS[k + 1], xtol=1e-14) for k in idx] + [np.inf]
    tot = 0.0
    for a, b in zip(cuts[:-1], cuts[1:]):
        mid = 0.5 * (a + b) if np.isfinite(a) and np.isfinite(b) else (b - 1.0 if np.isfinite(b) else (a + 1.0 if np.isfinite(a) else 0.0))
        if f(mid) > 0:
            tot += float((c * (norm.cdf(b, m, s) - norm.cdf(a, m, s))).sum())
    return tot


def inner(g1, mode, rev):
    wa, w0, wc = phi(g1 + 2) / 2, phi(g1 + 1) / 2, phi(g1) / 2
    if mode == "anti":
        P = [(wa, 0.0), (wc, 2.0)]; Q = [(w0, 0.0), (wc, 1.0)]
    else:
        P = [(wa, 0.0), (wc, 0.0)]; Q = [(w0, 0.0), (wc, -1.0)]
    A, B = (Q, P) if rev else (P, Q)
    return pos_int(A + [(-E * cc, mm) for cc, mm in B])


print("sigma %g eps %g" % (s, eps))
for g1 in (-3.0, -2.5, -2.0, -1.0, 0.0):
    a, b = inner(g1, "anti", False), inner(g1, "same", False)
    print("g1 %5.2f I_anti %.12f I_same %.12f diff %+.3e" % (g1, a, b, b - a), flush=True)
G = np.linspace(-2 - 9 * s, 2 + 9 * s, 1601)
for rev in (False, True):
    ia = np.array([inner(g, "anti", rev) for g in G]); isame = np.array([inner(g, "same", rev) for g in G])
    conj, best = simpson(ia, x=G), simpson(np.maximum(ia, isame), x=G)
    win = G[isame > ia]
    print("order %s conjectured %.6f adaptive %.6f gain %+.6f  SAME wins on g1 in [%s]" % (
        "Q||P" if rev else "P||Q", conj, best, best - conj,
        ("%.2f..%.2f (%d pts)" % (win.min(), win.max(), len(win))) if len(win) else "none"), flush=True)
