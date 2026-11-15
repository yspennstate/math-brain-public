"""Rigorous (interval-arithmetic) verification of the one-variable inequality (A) for a certificate potential.

The AND constraint (A) of THEOREM_NOTE.md, divided by pq, reads Phi(p,q) >= 0 with
    Phi = G(p) + G(q) - G(pq) - E(p,q),   G(p) = Gamma(p)/p,
    E(p,q) = 8p(1-q)L(p) + 8q(1-p)L(q) + 8(1-p)(1-q) + Psi(pq) - Psi(p) - Psi(q),
    L(z) = log2(1/z), Psi(z) = phi((1-2z)^2)/z, phi(w) = w log2(1/w).
(Identity checked at 40 digits, see fei_cert_vi.py.)  The certificate potential is
    Gamma_hat(p) = p G_num(x) + c p (1-p),  x = log2(1/p),  p <= 1/2,   Gamma_hat(1-p) = Gamma_hat(p),
with G_num piecewise linear in x through nodes (x_j, G_j), linear tail beyond x = K.  Then Gamma_hat(1/2) = C0 + c/4.

Interval arithmetic: numpy float64 with outward rounding by nextafter after every operation; transcendental
functions (log2, log1p, exp2) padded by PAD ulps (assumption: the numpy implementations are accurate to fewer
than PAD ulps).  Region 1 here: p, q <= 1/2 (x, y >= 1).  Cells in (x, y) are products of node intervals; a cell
whose lower bound is negative is split in four, up to a maximum depth.
"""
import sys, os, math, time
import numpy as np
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

INF = np.inf
def UP(a): return np.nextafter(a, INF)
def DN(a): return np.nextafter(a, -INF)
PAD = 8
def padup(a):
    for _ in range(PAD): a = UP(a)
    return a
def paddn(a):
    for _ in range(PAD): a = DN(a)
    return a

class Iv:
    __slots__ = ("lo", "hi")
    def __init__(self, lo, hi=None):
        lo = np.asarray(lo, dtype=float)
        if hi is None:
            self.lo = lo; self.hi = lo
        else:
            hi = np.asarray(hi, dtype=float)
            if lo.shape != hi.shape:
                lo, hi = np.broadcast_arrays(lo, hi); lo = np.array(lo); hi = np.array(hi)
            self.lo = lo; self.hi = hi
    def __repr__(self): return "Iv(%s, %s)" % (self.lo, self.hi)
    def __add__(s, o): o = asiv(o); return Iv(DN(s.lo + o.lo), UP(s.hi + o.hi))
    __radd__ = __add__
    def __neg__(s): return Iv(-s.hi, -s.lo)
    def __sub__(s, o): o = asiv(o); return Iv(DN(s.lo - o.hi), UP(s.hi - o.lo))
    def __rsub__(s, o): return asiv(o) - s
    def __mul__(s, o):
        o = asiv(o)
        a, b, c, d = s.lo * o.lo, s.lo * o.hi, s.hi * o.lo, s.hi * o.hi
        return Iv(DN(np.minimum(np.minimum(a, b), np.minimum(c, d))), UP(np.maximum(np.maximum(a, b), np.maximum(c, d))))
    __rmul__ = __mul__
    def __truediv__(s, o):
        o = asiv(o)
        if not (np.all(o.lo > 0) or np.all(o.hi < 0)):
            raise ZeroDivisionError("interval division by an interval containing 0")
        a, b, c, d = s.lo / o.lo, s.lo / o.hi, s.hi / o.lo, s.hi / o.hi
        return Iv(DN(np.minimum(np.minimum(a, b), np.minimum(c, d))), UP(np.maximum(np.maximum(a, b), np.maximum(c, d))))
    def __rtruediv__(s, o): return asiv(o) / s
    def sq(s):
        lo2, hi2 = s.lo * s.lo, s.hi * s.hi
        both_pos = s.lo >= 0; both_neg = s.hi <= 0
        lo = np.where(both_pos, lo2, np.where(both_neg, hi2, 0.0))
        hi = np.maximum(lo2, hi2)
        return Iv(DN(lo), UP(hi))
    def width(s): return s.hi - s.lo

def asiv(o):
    return o if isinstance(o, Iv) else Iv(np.asarray(o, dtype=float))

LN2 = Iv(paddn(np.log(2.0)), padup(np.log(2.0)))
FOUR_OVER_LN2 = Iv(4.0) / LN2

def log2_iv(a):
    assert np.all(a.lo > 0)
    return Iv(paddn(np.log2(a.lo)), padup(np.log2(a.hi)))

def L_iv(a):                       # log2(1/a)
    return -log2_iv(a)

def exp2neg(x):                    # 2^-x, decreasing
    return Iv(paddn(np.exp2(-x.hi)), padup(np.exp2(-x.lo)))

def neglog1pneg_pt(u):             # -log1p(-u) at float u in (0,1), as an interval
    v = -np.log1p(-u)
    return Iv(paddn(v), padup(v))

def ell_pt(u):                     # ell(u) = -log(1-u)/u at float u
    return neglog1pneg_pt(u) / Iv(u)

def ell_iv(u):                     # increasing on (0,1)
    assert np.all(u.lo > 0) and np.all(u.hi < 1)
    return Iv(ell_pt(u.lo).lo, ell_pt(u.hi).hi)

def phi_pt(w):                     # phi(w) = -w log2 w at float w in [0,1], as an interval
    w = np.asarray(w, dtype=float)
    safe = np.where(w > 0, w, 1.0)
    v = np.where(w > 0, -safe * np.log2(safe), 0.0)
    return Iv(paddn(v), padup(v))

PHI_MAX = Iv(paddn(np.log2(np.e) / np.e), padup(np.log2(np.e) / np.e))
INV_E_LO, INV_E_HI = 0.3678794411714423 - 1e-15, 0.3678794411714424 + 1e-15

def phi_iv(w):                     # w subset of [0,1]; increasing on [0,1/e], decreasing after
    assert np.all(w.lo >= 0) and np.all(w.hi <= 1)
    a, b = phi_pt(w.lo), phi_pt(w.hi)
    lo = np.minimum(a.lo, b.lo)
    hi = np.maximum(a.hi, b.hi)
    straddle = (w.lo < INV_E_HI) & (w.hi > INV_E_LO)
    hi = np.where(straddle, np.maximum(hi, PHI_MAX.hi), hi)
    return Iv(lo, hi)

def psi_iv(z):
    """Psi(z) = phi((1-2z)^2)/z on an interval z subset of (0,1)"""
    assert np.all(z.lo > 0) and np.all(z.hi < 1)
    out_lo = np.empty_like(z.lo); out_hi = np.empty_like(z.hi)
    A = z.hi <= 0.25
    if A.any():
        zz = Iv(z.lo[A], z.hi[A])
        r = FOUR_OVER_LN2 * (1 - 2 * zz).sq() * ell_iv(2 * zz)
        out_lo[A], out_hi[A] = r.lo, r.hi
    B = z.lo >= 0.75
    if B.any():
        zz = Iv(z.lo[B], z.hi[B]); zp = 1 - zz          # zp <= 0.25
        r = (1 - 2 * zp).sq() * (4 * zp) * ell_iv(2 * zp) / (zz * LN2)
        out_lo[B], out_hi[B] = r.lo, r.hi
    Cm = ~(A | B)
    if Cm.any():
        zz = Iv(z.lo[Cm], z.hi[Cm])
        w = (1 - 2 * zz).sq()
        w = Iv(np.maximum(w.lo, 0.0), np.minimum(w.hi, 1.0))
        r = phi_iv(w) / zz
        out_lo[Cm], out_hi[Cm] = r.lo, r.hi
    return Iv(out_lo, out_hi)

def E_iv(x, y):
    """E(p,q) for p = 2^-x, q = 2^-y on interval cells x, y"""
    p, q = exp2neg(x), exp2neg(y)
    omp, omq = 1 - p, 1 - q
    return 8 * p * omq * x + 8 * q * omp * y + 8 * omp * omq + psi_iv(p * q) - psi_iv(p) - psi_iv(q)

class Cert:
    """certificate potential: nodes xs (increasing, xs[0] = 1, xs[-1] = K), values G_num, tail slope, margin c"""
    def __init__(self, xs, G, c, tail_slope=None):
        self.xs = np.asarray(xs, float); self.G = np.asarray(G, float); self.c = float(c); self.K = float(self.xs[-1])
        self.slopes = np.diff(self.G) / np.diff(self.xs)
        self.tail_slope = float(self.slopes[-1] if tail_slope is None else tail_slope)
        assert self.tail_slope > 0, "the tail must be increasing"
        # sparse tables for range min / max of the node values (a general piecewise-linear G need not be monotone)
        n = len(self.G); self.logn = max(1, int(np.floor(np.log2(n))) + 1)
        self.tmin = [self.G.copy()]; self.tmax = [self.G.copy()]
        k = 1
        while (1 << k) <= n:
            prev_min, prev_max = self.tmin[-1], self.tmax[-1]; h = 1 << (k - 1)
            self.tmin.append(np.minimum(prev_min[:n - (1 << k) + 1], prev_min[h:h + n - (1 << k) + 1]))
            self.tmax.append(np.maximum(prev_max[:n - (1 << k) + 1], prev_max[h:h + n - (1 << k) + 1]))
            k += 1
    def _range_nodes(self, i, j):
        """min and max of G[i..j] inclusive for index arrays with i <= j"""
        ln = np.floor(np.log2(np.maximum(j - i + 1, 1))).astype(int)
        mn = np.empty(len(i)); mx = np.empty(len(i))
        for k in np.unique(ln):
            sel = ln == k; a = i[sel]; b = j[sel] - (1 << int(k)) + 1
            mn[sel] = np.minimum(self.tmin[k][a], self.tmin[k][b]); mx[sel] = np.maximum(self.tmax[k][a], self.tmax[k][b])
        return mn, mx
    def Gnum_pt(self, a):
        """G_num at float array a (>= 1), as an interval"""
        a = np.asarray(a, float)
        j = np.clip(np.searchsorted(self.xs, a, side="right") - 1, 0, len(self.xs) - 2)
        inside = a <= self.K
        x0 = np.where(inside, self.xs[j], self.K); g0 = np.where(inside, self.G[j], self.G[-1])
        sl = np.where(inside, self.slopes[j], self.tail_slope)
        return Iv(g0) + (Iv(a) - Iv(x0)) * Iv(sl)
    def Gnum_range(self, xiv):
        """range of the piecewise-linear G_num over an interval of x: endpoint values and the interior node values"""
        a, b = xiv.lo, xiv.hi
        ea, eb = self.Gnum_pt(a), self.Gnum_pt(b)
        lo = np.minimum(ea.lo, eb.lo); hi = np.maximum(ea.hi, eb.hi)
        i = np.searchsorted(self.xs, a, side="right")          # first node strictly inside (a, b)
        j = np.searchsorted(self.xs, b, side="left") - 1       # last node strictly inside
        has = i <= j
        if has.any():
            mn, mx = self._range_nodes(i[has], j[has])
            lo[has] = np.minimum(lo[has], mn); hi[has] = np.maximum(hi[has], mx)
        return Iv(lo, hi)
    def Ghat_range(self, xiv):
        """range of G_hat = G_num(x) + c(1 - 2^-x) over an interval of x"""
        m = Iv(self.c) * (1 - exp2neg(xiv))
        return self.Gnum_range(xiv) + m
    def C_cert(self):
        return self.G[0] / 2 + self.c / 4      # Gamma_hat(1/2) = (1/2) G_hat(1) = G_num(1)/2 + c/4

def verify_region1(cert, max_depth=14, report_every=True):
    """Phi >= 0 on all cells x, y in [1, K]^2 (x <= y by symmetry); returns (ok, stats)"""
    xs = cert.xs; n = len(xs) - 1
    I, Kk = np.triu_indices(n)                          # cell pairs i <= k
    x0, x1 = xs[I], xs[I + 1]; y0, y1 = xs[Kk], xs[Kk + 1]
    stats = []
    t0 = time.time()
    for depth in range(max_depth + 1):
        X = Iv(x0, x1); Y = Iv(y0, y1)
        phi_lo = cert.Ghat_range(X).lo + cert.Ghat_range(Y).lo - cert.Ghat_range(X + Y).hi - E_iv(X, Y).hi
        bad = phi_lo < 0
        nb = int(bad.sum())
        stats.append((depth, len(x0), nb, float(phi_lo.min())))
        if report_every:
            print("  depth %2d: %9d cells, %8d failing, min lower bound %+.3e  (%.0f s)" % (depth, len(x0), nb, phi_lo.min(), time.time() - t0), flush=True)
        if nb == 0:
            return True, stats
        if depth == max_depth:
            j = int(np.argmin(phi_lo))
            print("  FAILED at max depth: worst cell x in [%.6f, %.6f], y in [%.6f, %.6f], bound %.3e" % (x0[j], x1[j], y0[j], y1[j], phi_lo[j]))
            return False, stats
        bx0, bx1, by0, by1 = x0[bad], x1[bad], y0[bad], y1[bad]
        xm = (bx0 + bx1) / 2; ym = (by0 + by1) / 2
        x0 = np.concatenate([bx0, xm, bx0, xm]); x1 = np.concatenate([xm, bx1, xm, bx1])
        y0 = np.concatenate([by0, by0, ym, ym]); y1 = np.concatenate([ym, ym, by1, by1])
    return False, stats

if __name__ == "__main__":
    src = sys.argv[1]; c = float(sys.argv[2]); max_depth = int(sys.argv[3]) if len(sys.argv) > 3 else 14
    d = np.load(src)
    xs, G, C0 = d["xs"], d["G"], float(d["C"])
    cert = Cert(xs, G, c)
    print("certificate from %s: C0=%.7f, %d nodes, K=%g, c=%g -> C_cert = %.7f" % (src, C0, len(xs), cert.K, c, cert.C_cert()), flush=True)
    ok, stats = verify_region1(cert, max_depth=max_depth)
    print("REGION 1 (p, q <= 1/2): %s" % ("VERIFIED" if ok else "NOT verified"))
