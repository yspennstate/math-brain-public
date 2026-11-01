"""Exact (quadrature, bin-free) partial densities for n = 3 quadratic polynomials
Q(x) = x^T A x + b^T x with independent coordinates, each uniform on a finite union of intervals.

g_i(t) = density of Q at s given X_i = t
       = int f_j(u) sum_{w: q(u,w)=s} f_k(w) |d_w q| / |grad q|^2 du
       + int f_k(w) sum_{u: q(u,w)=s} f_j(u) |d_u q| / |grad q|^2 dw,
where q(u,w) = Q with x_i = t, x_j = u, x_k = w and grad is over (u,w)  (partition of unity).
The integrands are bounded by 1/|grad q| and vanish at tangencies, so midpoint quadrature converges.
p_Q(s) = int f_i(t) g_i(t) dt.
"""
try:
    import psutil
    psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np


class Law:
    """uniform density 1 on a union of disjoint intervals of total length 1 (or density c on them)"""
    def __init__(self, a, b):
        a = np.atleast_1d(np.asarray(a, float)); b = np.atleast_1d(np.asarray(b, float))
        o = np.argsort(a); self.a, self.b = a[o], b[o]
        tot = np.sum(self.b - self.a)
        self.c = 1.0/tot

    def pdf(self, x):
        x = np.asarray(x, float)
        k = np.searchsorted(self.a, x, side='right') - 1
        kk = np.clip(k, 0, len(self.a)-1)
        ok = (k >= 0) & (x >= self.a[kk]) & (x < self.b[kk])
        return np.where(ok, self.c, 0.0)

    def nodes(self, m_per_unit=400):
        pts = []; wts = []
        for a, b in zip(self.a, self.b):
            m = max(8, int(np.ceil((b-a)*m_per_unit)))
            h = (b-a)/m
            pts.append(a + h*(np.arange(m)+0.5)); wts.append(np.full(m, h*self.c))
        return np.concatenate(pts), np.concatenate(wts)


def _branch(M, bb, t, U, s, lawW, wU, eta=0.0):
    """coordinates ordered (t,u,w); M 3x3, bb linear; integrate over u (nodes U, weights wU), solve w."""
    a = M[2, 2]
    T = t[:, None]; Uu = U[None, :]
    bhalf = M[2, 1]*Uu + M[2, 0]*T + bb[2]/2
    c0 = M[0, 0]*T*T + 2*M[0, 1]*T*Uu + M[1, 1]*Uu*Uu + bb[0]*T + bb[1]*Uu - s
    out = np.zeros((len(t), len(U)))
    if abs(a) < 1e-13:
        with np.errstate(divide='ignore', invalid='ignore'):
            W = -c0/(2*bhalf)
        roots = [(W, np.isfinite(W))]
    else:
        disc = bhalf*bhalf - a*c0
        ok = disc >= 0
        sq = np.sqrt(np.where(ok, disc, 0))
        qq = -(bhalf + np.copysign(sq, bhalf))
        with np.errstate(divide='ignore', invalid='ignore'):
            W1 = qq/a
            W2 = np.where(qq != 0, c0/qq, -bhalf/a)
        roots = [(W1, ok), (W2, ok)]
    for W, ok in roots:
        W = np.where(ok, W, 0.0)
        f = lawW.pdf(W) * ok
        dw = 2*(a*W + bhalf)
        du = 2*(M[1, 1]*Uu + M[1, 2]*W + M[1, 0]*T) + bb[1]
        with np.errstate(divide='ignore', invalid='ignore'):
            val = np.where(f > 0, f*np.abs(dw)/np.maximum(dw*dw + du*du, eta*eta), 0.0)
        out += val
    return out @ wU


def g_partial(A, b, s, i, laws, tvals, m_per_unit=400, eta=0.0):
    order = [i] + [j for j in range(3) if j != i]
    M = A[np.ix_(order, order)]; bb = b[order]
    j, k = order[1], order[2]
    Uj, wj = laws[j].nodes(m_per_unit)
    Uk, wk = laws[k].nodes(m_per_unit)
    tvals = np.atleast_1d(np.asarray(tvals, float))
    g = _branch(M, bb, tvals, Uj, s, laws[k], wj, eta)
    M2 = M[np.ix_([0, 2, 1], [0, 2, 1])]; bb2 = bb[[0, 2, 1]]
    g += _branch(M2, bb2, tvals, Uk, s, laws[j], wk, eta)
    return g


def density(A, b, s, laws, i=0, m_per_unit=300, eta=None):
    T, wT = laws[i].nodes(m_per_unit)
    if eta is None: eta = 1.0/m_per_unit
    g = g_partial(A, b, s, i, laws, T, m_per_unit, eta)
    return float(np.sum(g*wT))


def top_set(g, grid_x, h):
    """top measure-one superlevel set of g sampled on a uniform grid (cell width h); returns
    (value = int over top set, list of intervals)"""
    k = int(round(1.0/h))
    order = np.argsort(-g)
    sel = np.zeros(len(g), bool); sel[order[:k]] = True
    val = np.sum(g[sel])*h
    # intervals
    ivs = []
    inrun = False
    for idx in range(len(g)):
        if sel[idx] and not inrun:
            start = grid_x[idx] - h/2; inrun = True
        if inrun and (idx == len(g)-1 or not sel[idx+1]):
            ivs.append((start, grid_x[idx] + h/2)); inrun = False
    return val, ivs
