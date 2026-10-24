"""Region-1 lower bound that keeps the cancellation between the three potential terms.

Phi(x,y) = Ghat(x) + Ghat(y) - Ghat(x+y) - E(x,y) on a cell X x Y = [x0,x1] x [y0,y1], p = 2^-x, q = 2^-y, with
Ghat(x) = G_num(x) + c(1 - 2^-x).  The decoupled bound of fei_cert.verify_region1 adds the widths of the three Ghat
ranges and of E and loses about thirty grid steps of width per node cell.  Here the pieces are enclosed one by one,
each exactly up to rounding, and a centred form is taken as well; the cell's bound is the larger of the two.

  (a) P(x,y) = G_num(x) + G_num(y) - G_num(x+y) is piecewise linear.  On a cell whose x side and y side each lie in
      one segment of the node grid, P is linear on every piece of the subdivision of the cell by the lines x+y = node,
      so its minimum over the cell is attained at a vertex of that subdivision: a corner of the cell, or a point where
      a line x+y = node meets an edge of the cell.  Every such vertex is evaluated in interval arithmetic with its
      coordinates as one-ulp intervals clipped to the cell (a vertex outside the cell becomes a point inside it, which
      is harmless), so the minimum over the evaluated set is a lower bound of P on the cell and is exact to rounding.
  (b) M(x,y) = c(1-p)(1-q) is monotone in x and in y (increasing for c > 0); its minimum is at a corner.
  (c) E is smooth; its maximum is bounded by the interval evaluation E_iv and by the mean-value form
      E(xc,yc) + rx max|dE/dx| + ry max|dE/dy|, the partial derivatives enclosed over the cell; the smaller is used.
      Phi_lo1 = P_min + M_min - E_max.
  (d) The centred form Phi_lo2 = Phi(xc,yc) - rx max|dPhi/dx| - ry max|dPhi/dy| with
      dPhi/dx = G_num'(x) - G_num'(x+y) + c ln2 p(1-q) - dE/dx, where G_num'(x) is the slope of the one segment
      containing the x side and G_num'(x+y) ranges over the slopes of the segments met by [x0+y0, x1+y1] (the tail
      slope beyond K).  Phi is Lipschitz, so the mean-value inequality holds with the essential supremum of the
      derivative along axis-parallel paths inside the cell.
  dE/dx = p [ 8(1-q)(1 - x ln2) + 8 q y ln2 + 8(1-q) ln2 - Psi'(pq) q ln2 + Psi'(p) ln2 ],  and symmetrically in y
  (dp/dx = -p ln2; Psi' from fei_cert23.psi_prime_iv on (0, 1/2]).
A cell whose x side or y side crosses a node (never a node cell or one of its bisections) falls back to the
decoupled bound.  Cross-checked against 40-digit arithmetic by crosscheck_r1x.py.
"""
import sys, os, math, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fei_cert import Iv, UP, DN, LN2, exp2neg, E_iv, Cert, ell_iv, psi_iv
from fei_cert23 import (psi_prime_iv, build_slope_tables, slope_range, _adaptive, BSTAR, phi1_lower,
                        psit_over_z_iv, Ghat_prime_range, phi2_over_v_lower)


def _clip_iv(v, lo, hi):
    """one-ulp interval around the float array v, clipped into [lo, hi] elementwise"""
    return Iv(np.minimum(np.maximum(DN(v), lo), hi), np.minimum(np.maximum(UP(v), lo), hi))


def _seg(cert, a, b):
    """segment index of a (side right) and of b (side left); equal iff [a, b] lies in one segment"""
    n = len(cert.xs) - 1
    ia = np.clip(np.searchsorted(cert.xs, a, side="right") - 1, 0, n - 1)
    ib = np.clip(np.searchsorted(cert.xs, b, side="left") - 1, 0, n - 1)
    return ia, np.maximum(ia, ib)


def P_at(cert, X, Y):
    """lower bound of G_num(x) + G_num(y) - G_num(x+y) over the (tiny) cell X x Y"""
    return cert.Gnum_range(X).lo + cert.Gnum_range(Y).lo - cert.Gnum_range(X + Y).hi


def P_min_exact(cert, x0, x1, y0, y1):
    """minimum, exact to rounding, of the piecewise-linear part over cells whose x and y sides lie in one segment each"""
    best = np.full(len(x0), np.inf)
    for xa, ya in ((x0, y0), (x0, y1), (x1, y0), (x1, y1)):
        best = np.minimum(best, P_at(cert, Iv(xa), Iv(ya)))
    xs = cert.xs
    slo = DN(x0 + y0); shi = UP(x1 + y1)
    i_lo = np.searchsorted(xs, slo, side="right")          # first node strictly above slo
    i_hi = np.searchsorted(xs, shi, side="left") - 1       # last node strictly below shi
    ncross = np.maximum(i_hi - i_lo + 1, 0)
    for j in range(int(ncross.max()) if len(ncross) else 0):
        m = ncross > j
        if not m.any():
            break
        s = xs[i_lo[m] + j]
        mx0, mx1, my0, my1 = x0[m], x1[m], y0[m], y1[m]
        cand = np.full(int(m.sum()), np.inf)
        for xa, yv in ((mx0, s - mx0), (mx1, s - mx1)):          # the line meets the edges x = x0, x = x1
            cand = np.minimum(cand, P_at(cert, Iv(xa), _clip_iv(yv, my0, my1)))
        for xv, ya in ((s - my0, my0), (s - my1, my1)):          # and the edges y = y0, y = y1
            cand = np.minimum(cand, P_at(cert, _clip_iv(xv, mx0, mx1), Iv(ya)))
        best[m] = np.minimum(best[m], cand)
    return best


def dE_dx(X, Y):
    """enclosure of dE/dx over the cell X x Y (x, y >= 1)"""
    p, q = exp2neg(X), exp2neg(Y)
    return p * (8 * (1 - q) * (1 - X * LN2) + 8 * q * Y * LN2 + 8 * (1 - q) * LN2 - psi_prime_iv(p * q) * q * LN2 + psi_prime_iv(p) * LN2)


def dE_dy(X, Y):
    return dE_dx(Y, X)


def _amax(iv):
    return np.maximum(np.abs(iv.lo), np.abs(iv.hi))


def phi1_lower_exact(cert, X, Y):
    """region-1 lower bound of Phi with the exact piecewise-linear minimum, the exact margin minimum, the tighter of the
    two E maxima, and the centred form; returns (lower bound, width attributed to x, width attributed to y)"""
    x0, x1, y0, y1 = X.lo, X.hi, Y.lo, Y.hi
    c = Iv(cert.c)
    # (a)+(b)+(c)
    P_min = P_min_exact(cert, x0, x1, y0, y1)
    # M is monotone in each variable (increasing for c > 0), so its minimum over the cell is at a corner
    M_min = np.minimum.reduce([(c * (1 - exp2neg(Iv(xa))) * (1 - exp2neg(Iv(ya)))).lo for xa, ya in ((x0, y0), (x0, y1), (x1, y0), (x1, y1))])
    xc = (x0 + x1) / 2; yc = (y0 + y1) / 2
    rx = UP(np.maximum(x1 - xc, xc - x0)); ry = UP(np.maximum(y1 - yc, yc - y0))
    Xc, Yc = Iv(xc), Iv(yc)
    Ec = E_iv(Xc, Yc)
    dEx = dE_dx(X, Y); dEy = dE_dy(X, Y)
    aEx = _amax(dEx); aEy = _amax(dEy)
    E_max = np.minimum(E_iv(X, Y).hi, (Ec + Iv(rx) * Iv(aEx) + Iv(ry) * Iv(aEy)).hi)
    lo1 = (Iv(P_min) + Iv(M_min) - Iv(E_max)).lo
    # (d) the centred form
    ix0, ix1 = _seg(cert, x0, x1); iy0, iy1 = _seg(cert, y0, y1)
    clean = (ix0 == ix1) & (iy0 == iy1)
    Phi_c = cert.Ghat_range(Xc) + cert.Ghat_range(Yc) - cert.Ghat_range(Xc + Yc) - Ec
    S_sum = slope_range(cert, DN(x0 + y0), UP(x1 + y1))
    p, q = exp2neg(X), exp2neg(Y)
    dPx = Iv(cert.slopes[ix0]) - S_sum + c * LN2 * p * (1 - q) - dEx
    dPy = Iv(cert.slopes[iy0]) - S_sum + c * LN2 * q * (1 - p) - dEy
    aPx = _amax(dPx); aPy = _amax(dPy)
    lo2 = (Phi_c - Iv(rx) * Iv(aPx) - Iv(ry) * Iv(aPy)).lo
    lo = np.maximum(lo1, lo2)
    if not clean.all():                                     # a side crossing a node: the decoupled bound there
        old = phi1_lower(cert, X, Y)[0]
        lo = np.where(clean, lo, old)
    return lo, rx * aPx, ry * aPy


def verify_region1_exact(cert, max_depth=30):
    xs = cert.xs; n = len(xs) - 1
    I, Kk = np.triu_indices(n)
    return _adaptive(lambda X, Y: phi1_lower_exact(cert, X, Y), xs[I], xs[I + 1], xs[Kk], xs[Kk + 1], max_depth, "region 1 (exact PL)")


def load_cert(src, c):
    d = np.load(src); xs, G, C0 = d["xs"], d["G"], float(d["C"]); K = float(xs[-1])
    tail_slope = (G[-1] - BSTAR) / K
    cert = Cert(xs, G, c, tail_slope=tail_slope); build_slope_tables(cert)
    return cert, C0


if __name__ == "__main__":
    src = sys.argv[1]; c = float(sys.argv[2]); max_depth = int(sys.argv[3]) if len(sys.argv) > 3 else 30
    cert, C0 = load_cert(src, c)
    print("certificate %s: C0=%.7f, %d nodes, K=%g, c=%g, tail slope %.6f -> C_cert = %.7f" % (src, C0, len(cert.xs), cert.K, c, cert.tail_slope, cert.C_cert()), flush=True)
    t0 = time.time()
    ok = verify_region1_exact(cert, max_depth)
    print("RESULTS: {'R1x': %s}  (%.0f s)" % (ok, time.time() - t0))
    print("REGION 1 (exact PL enclosure): %s at c=%g (C_cert = %.7f)" % ("VERIFIED" if ok else "NOT verified", c, cert.C_cert()))


# ----------------------------------------------------------------------------------------------------------------
# region 2: the same cancellation, kept
# ----------------------------------------------------------------------------------------------------------------
def D_enclose(cert, x0, x1, l0, l1):
    """Enclosure of D(x, lam) = G_num(x) - G_num(x + lam) over the rectangle [x0,x1] x [l0,l1], exact to rounding.

    The x side lies in one segment of the node grid (a region-2 node cell and every bisection of one), so the only
    lines that break linearity inside the rectangle are the diagonals x + lam = node.  D is linear on each piece, and
    the pieces are convex, so the extrema are at vertices: the four corners, and where each diagonal meets an edge.
    A vertex outside the rectangle is clipped into it, which only adds interior points and keeps the bound valid."""
    def at(Xv, Lv):
        return cert.Gnum_range(Xv) - cert.Gnum_range(Xv + Lv)
    lo = np.full(len(x0), np.inf); hi = np.full(len(x0), -np.inf)
    for xa, la in ((x0, l0), (x0, l1), (x1, l0), (x1, l1)):
        r = at(Iv(xa), Iv(la)); lo = np.minimum(lo, r.lo); hi = np.maximum(hi, r.hi)
    xs = cert.xs
    slo = DN(x0 + l0); shi = UP(x1 + l1)
    i_lo = np.searchsorted(xs, slo, side="right")
    i_hi = np.searchsorted(xs, shi, side="left") - 1
    ncross = np.maximum(i_hi - i_lo + 1, 0)
    for j in range(int(ncross.max()) if len(ncross) else 0):
        m = ncross > j
        if not m.any():
            break
        s = xs[i_lo[m] + j]
        mx0, mx1, ml0, ml1 = x0[m], x1[m], l0[m], l1[m]
        clo = np.full(int(m.sum()), np.inf); chi = np.full(int(m.sum()), -np.inf)
        for Xv, Lv in ((Iv(mx0), _clip_iv(s - mx0, ml0, ml1)),           # the diagonal meets x = x0 and x = x1
                       (Iv(mx1), _clip_iv(s - mx1, ml0, ml1)),
                       (_clip_iv(s - ml0, mx0, mx1), Iv(ml0)),           # and lam = l0 and lam = l1
                       (_clip_iv(s - ml1, mx0, mx1), Iv(ml1))):
            r = at(Xv, Lv); clo = np.minimum(clo, r.lo); chi = np.maximum(chi, r.hi)
        lo[m] = np.minimum(lo[m], clo); hi[m] = np.maximum(hi[m], chi)
    return Iv(lo, hi)


def phi2_over_v_lower_exact(cert, X, Yp):
    """region-2 lower bound of Phi/v with the A term's cancellation kept: A = [Ghat(x) - Ghat(x+lam)]/v with
    Ghat(x) - Ghat(x+lam) = D(x, lam) + c p (2^-lam - 1), D enclosed exactly over the cell and lam relaxed to its
    range over the cell (a valid relaxation).  Every other term is as in fei_cert23.phi2_over_v_lower, and the
    result is the best of the three A forms (exact, mean-value, direct)."""
    p = exp2neg(X); v = exp2neg(Yp); ellv = ell_iv(v); lam = v * ellv / LN2
    Xl = Iv(X.lo, UP(X.hi + lam.hi))
    A_mv = -(ellv / LN2) * Ghat_prime_range(cert, Xl)
    A_dir = (cert.Ghat_range(X) - cert.Ghat_range(X + lam)) / v
    D = D_enclose(cert, X.lo, X.hi, lam.lo, lam.hi)
    A_ex = (D + Iv(cert.c) * p * (exp2neg(lam) - 1)) / v
    A_lo = np.maximum(np.maximum(A_mv.lo, A_dir.lo), A_ex.lo)
    B = cert.Ghat_range(Yp) / (1 - v)
    Cc = (-8) * p * X
    Dd = (-8) * (1 - v) * (1 - p) * ellv / LN2
    Ee = (-8) * (1 - p)
    zlo = np.maximum(DN(p.lo * (1 - v.hi)), 1e-300); Z = Iv(zlo, p.hi)
    F_mv = p * psi_prime_iv(Z)
    F_dir = (psi_iv(p) - psi_iv(p * (1 - v))) / v
    F_lo = np.maximum(F_mv.lo, F_dir.lo)
    Gg = psit_over_z_iv(v)
    lo = A_lo + B.lo + Cc.lo + Dd.lo + Ee.lo + F_lo + Gg.lo
    # width attribution for the splitting rule: the A term's width now follows the cell, not the ranges
    wA = np.minimum(np.minimum(A_mv.width(), A_dir.width()), A_ex.width())
    wx = 0.5 * wA + Cc.width() + p.width() * np.abs(psi_prime_iv(Z).lo)
    wy = 0.5 * wA + B.width() + Dd.width() + Gg.width()
    return lo, wx, wy


def verify_region2_exact(cert, max_depth=30, xmax=None, ypmax=None):
    xs = cert.xs; K = cert.K
    xn = xs if xmax is None else np.concatenate([xs, K + np.arange(1, xmax - K + 1)])
    yn = xs if ypmax is None else np.concatenate([xs, K + np.arange(1, ypmax - K + 1)])
    I, J = np.meshgrid(np.arange(len(xn) - 1), np.arange(len(yn) - 1), indexing="ij"); I = I.ravel(); J = J.ravel()
    return _adaptive(lambda X, Y: phi2_over_v_lower_exact(cert, X, Y), xn[I], xn[I + 1], yn[J], yn[J + 1],
                     max_depth, "region 2 (exact A)")
