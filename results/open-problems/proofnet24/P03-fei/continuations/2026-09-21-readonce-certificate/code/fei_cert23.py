"""Regions 2 and 3 of the certificate check, the one-dimensional tail conditions, and the beyond-grid lemmas.

Notation (fei_cert.py): p = 2^-x, x >= 1 on the small side; for q > 1/2 write v = 1 - q = 2^-y', y' >= 1; for p > 1/2
write u = 1 - p = 2^-x'.  G_hat(x) = G_num(x) + c(1 - 2^-x) is the certificate function Gamma_hat(p)/p on the small side,
Lambda(z) = Gamma_hat(z)/(1-z) = z G_hat(L(z))/(1-z) is Gamma_hat(1-z)/(1-z), the big-side value.  Every quantity below is
an exact algebraic rewriting of Phi = G(p) + G(q) - G(pq) - E(p,q) divided by the small parameter, with mean-value
enclosures (f(b) - f(a) = (b - a) f'(xi)) for differences that would otherwise cancel catastrophically; both the
mean-value and the direct enclosure are computed where useful and the larger lower bound is kept (both are rigorous).

Region 2 (p <= 1/2 < q), lambda = L(1-v) = v ell(v)/ln2:
   Phi/v = [G_hat(x) - G_hat(x+lambda)]/v + G_hat(y')/(1-v) - 8 p x - 8(1-v)(1-p) ell(v)/ln2 - 8(1-p)
           - [Psi(p(1-v)) - Psi(p)]/v + Psi(1-v)/v.
Region 3 (p, q > 1/2, u <= v), w = u + v - uv = 1 - pq:
   Phi/u = G_hat(x')/(1-u) + [Lambda(v) - G(pq)]/u - E(1-u,1-v)/u,
   G(pq) = Lambda(w) if w <= 1/2 else G_hat(L(1-w)),
   E(1-u,1-v)/u = 8(1-u) v ell(u)/ln2 + 8(1-v) v ell(v)/ln2 + 8 v + [Psit(w) - Psit(v)]/u - Psit(u)/u,   Psit(z) = Psi(1-z).
"""
import sys, os, math, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fei_cert import (Iv, asiv, UP, DN, padup, paddn, LN2, FOUR_OVER_LN2, log2_iv, L_iv, exp2neg, ell_pt, ell_iv,
                      phi_pt, phi_iv, psi_iv, E_iv, Cert, verify_region1)

BSTAR = 8 - 4 / math.log(2)

# ----------------------------------------------------------------------------------------------------------------
# slope tables and the derivative of G_hat
# ----------------------------------------------------------------------------------------------------------------
def build_slope_tables(cert):
    s = cert.slopes; n = len(s)
    tmin = [s.copy()]; tmax = [s.copy()]; k = 1
    while (1 << k) <= n:
        pm, px = tmin[-1], tmax[-1]; h = 1 << (k - 1)
        tmin.append(np.minimum(pm[:n - (1 << k) + 1], pm[h:h + n - (1 << k) + 1]))
        tmax.append(np.maximum(px[:n - (1 << k) + 1], px[h:h + n - (1 << k) + 1]))
        k += 1
    cert.smin, cert.smax = tmin, tmax

def _range_slopes(cert, i, j):
    ln = np.floor(np.log2(np.maximum(j - i + 1, 1))).astype(int)
    mn = np.empty(len(i)); mx = np.empty(len(i))
    for k in np.unique(ln):
        sel = ln == k; a = i[sel]; b = j[sel] - (1 << int(k)) + 1
        mn[sel] = np.minimum(cert.smin[k][a], cert.smin[k][b]); mx[sel] = np.maximum(cert.smax[k][a], cert.smax[k][b])
    return mn, mx

def slope_range(cert, a, b):
    """interval containing G_num'(t) for every t in [a, b] (pieces touching the interval, tail included)"""
    a = np.asarray(a, float); b = np.asarray(b, float); n = len(cert.xs) - 1
    i = np.clip(np.searchsorted(cert.xs, a, side="right") - 1, 0, n - 1)
    j = np.clip(np.searchsorted(cert.xs, b, side="left") - 1, 0, n - 1)
    j = np.maximum(i, j)
    mn, mx = _range_slopes(cert, i, j)
    tail = b > cert.K
    mn = np.where(tail, np.minimum(mn, cert.tail_slope), mn); mx = np.where(tail, np.maximum(mx, cert.tail_slope), mx)
    only_tail = a >= cert.K
    mn = np.where(only_tail, cert.tail_slope, mn); mx = np.where(only_tail, cert.tail_slope, mx)
    return Iv(mn, mx)

def Ghat_prime_range(cert, xiv):
    """G_hat' = G_num' + c ln2 2^-x on an interval of x"""
    return slope_range(cert, xiv.lo, xiv.hi) + Iv(cert.c) * LN2 * exp2neg(xiv)

# ----------------------------------------------------------------------------------------------------------------
# derivative enclosures: ell', Psi', g(m) = m phi'(m^2), Psit, Psit'
# ----------------------------------------------------------------------------------------------------------------
def ellprime_pt(u, N=64):
    """ell'(u) = sum_{n>=1} n u^(n-1)/(n+1) at float u in (0, 1/2], as an interval (series + tail bound)"""
    u = np.asarray(u, float)
    acc = Iv(np.zeros_like(u))
    pw = Iv(np.ones_like(u))
    U = Iv(u)
    for n in range(1, N + 1):
        acc = acc + Iv(n / (n + 1)) * pw
        pw = pw * U
    tail_hi = padup(u ** N / (1 - u))          # sum_{n>N} u^(n-1) = u^N/(1-u) >= the tail
    return Iv(acc.lo, UP(acc.hi + tail_hi))

def ellprime_iv(u):
    """ell' is increasing on (0,1)"""
    assert np.all(u.lo > 0) and np.all(u.hi < 1.0)
    return Iv(ellprime_pt(u.lo).lo, ellprime_pt(u.hi).hi)

def _psi_prime_small(z):
    """Psi'(z) for z subset of (0, 1/4]: (4/ln2)[-4(1-2z) ell(2z) + 2(1-2z)^2 ell'(2z)]"""
    u = 2 * z
    return FOUR_OVER_LN2 * ((-4) * (1 - 2 * z) * ell_iv(u) + 2 * (1 - 2 * z).sq() * ellprime_iv(u))

G_MSTAR = math.exp(-1.5)
def g_pt(m):
    """g(m) = m (2 L(m) - 1/ln2) at float m in [0, 1/2]"""
    m = np.asarray(m, float); safe = np.where(m > 0, m, 1.0)
    val = Iv(safe) * (2 * L_iv(Iv(safe)) - 1 / LN2)
    zero = m <= 0
    return Iv(np.where(zero, 0.0, val.lo), np.where(zero, 0.0, val.hi))

def g_iv(m):
    """range of g over an interval m subset of [0, 1/2]; g increases on [0, e^-1.5], decreases after"""
    a, b = g_pt(m.lo), g_pt(m.hi)
    lo = np.minimum(a.lo, b.lo); hi = np.maximum(a.hi, b.hi)
    inside = (m.lo < G_MSTAR) & (m.hi > G_MSTAR)
    if inside.any():
        gm = g_pt(np.full(int(inside.sum()), G_MSTAR))
        hi[inside] = np.maximum(hi[inside], padup(gm.hi))
    return Iv(lo, hi)

def _psi_prime_mid(z):
    """Psi'(z) for z subset of [1/4, 1/2]: -4 g(m)/z - phi(m^2)/z^2, m = 1 - 2z in [0, 1/2]"""
    m = 1 - 2 * z; m = Iv(np.maximum(m.lo, 0.0), np.minimum(m.hi, 1.0))
    w = m.sq(); w = Iv(np.maximum(w.lo, 0.0), np.minimum(w.hi, 1.0))
    return (-4) * g_iv(m) / z - phi_iv(w) / z.sq()

def psi_prime_iv(z):
    """Psi'(z) on an interval z subset of (0, 1/2] (split at 1/4, union)"""
    assert np.all(z.lo > 0) and np.all(z.hi <= 0.5 + 1e-9)
    lo = np.full_like(z.lo, np.inf); hi = np.full_like(z.hi, -np.inf)
    A = z.lo < 0.25
    if A.any():
        zz = Iv(z.lo[A], np.minimum(z.hi[A], 0.25)); r = _psi_prime_small(zz)
        lo[A] = np.minimum(lo[A], r.lo); hi[A] = np.maximum(hi[A], r.hi)
    B = z.hi > 0.25
    if B.any():
        zz = Iv(np.maximum(z.lo[B], 0.25), np.minimum(z.hi[B], 0.5)); r = _psi_prime_mid(zz)
        lo[B] = np.minimum(lo[B], r.lo); hi[B] = np.maximum(hi[B], r.hi)
    return Iv(lo, hi)

def psit_iv(z):
    """Psit(z) = Psi(1-z) on z subset of (0, 1)"""
    return psi_iv(1 - z)

def psit_over_z_iv(z):
    """Psit(z)/z on z subset of (0, 1/2]: (1-2z)^2 4 ell(2z)/((1-z) ln2) for z <= 1/4, else phi((1-2z)^2)/((1-z) z)"""
    lo = np.empty_like(z.lo); hi = np.empty_like(z.hi)
    A = z.hi <= 0.25
    if A.any():
        zz = Iv(z.lo[A], z.hi[A]); r = (1 - 2 * zz).sq() * 4 * ell_iv(2 * zz) / ((1 - zz) * LN2)
        lo[A], hi[A] = r.lo, r.hi
    B = ~A
    if B.any():
        zz = Iv(z.lo[B], z.hi[B]); m = 1 - 2 * zz; m = Iv(np.maximum(m.lo, 0.0), m.hi); w = m.sq()
        w = Iv(np.maximum(w.lo, 0.0), np.minimum(w.hi, 1.0))
        r = phi_iv(w) / ((1 - zz) * zz); lo[B], hi[B] = r.lo, r.hi
    return Iv(lo, hi)

def _psit_prime_small(z):
    """Psit'(z), z subset of (0,1/4]: (4/ln2) d/dz [ z (1-2z)^2 ell(2z) / (1-z) ]"""
    m = 1 - 2 * z; u = 2 * z; e = ell_iv(u); ep = ellprime_iv(u); om = 1 - z
    t = m.sq() * e / om + z * ((-4) * m) * e / om + z * m.sq() * 2 * ep / om + z * m.sq() * e / om.sq()
    return FOUR_OVER_LN2 * t

def _psit_prime_mid(z):
    """Psit'(z), z subset of [1/4, 1/2]: -4 g(m)/(1-z) + phi(m^2)/(1-z)^2, m = 1-2z"""
    m = 1 - 2 * z; m = Iv(np.maximum(m.lo, 0.0), np.minimum(m.hi, 1.0)); w = m.sq()
    w = Iv(np.maximum(w.lo, 0.0), np.minimum(w.hi, 1.0)); om = 1 - z
    return (-4) * g_iv(m) / om + phi_iv(w) / om.sq()

def psit_prime_iv(z):
    """Psit'(z) on z subset of (0, 3/4]; for z > 1/2 use Psit'(z) = -Psi'(1-z)"""
    assert np.all(z.lo > 0) and np.all(z.hi <= 0.75 + 1e-9)
    lo = np.full_like(z.lo, np.inf); hi = np.full_like(z.hi, -np.inf)
    A = z.lo < 0.25
    if A.any():
        zz = Iv(z.lo[A], np.minimum(z.hi[A], 0.25)); r = _psit_prime_small(zz)
        lo[A] = np.minimum(lo[A], r.lo); hi[A] = np.maximum(hi[A], r.hi)
    B = (z.hi > 0.25) & (z.lo < 0.5)
    if B.any():
        zz = Iv(np.maximum(z.lo[B], 0.25), np.minimum(z.hi[B], 0.5)); r = _psit_prime_mid(zz)
        lo[B] = np.minimum(lo[B], r.lo); hi[B] = np.maximum(hi[B], r.hi)
    Cc = z.hi > 0.5
    if Cc.any():
        zz = Iv(np.maximum(z.lo[Cc], 0.5), np.minimum(z.hi[Cc], 0.75))
        r = -psi_prime_iv(1 - zz)                        # 1 - z in [1/4, 1/2]
        lo[Cc] = np.minimum(lo[Cc], r.lo); hi[Cc] = np.maximum(hi[Cc], r.hi)
    return Iv(lo, hi)

# ----------------------------------------------------------------------------------------------------------------
# Lambda and its derivative
# ----------------------------------------------------------------------------------------------------------------
def Lambda_range(cert, z):
    """Lambda(z) = z G_hat(L(z))/(1-z) on z subset of (0, 1/2]"""
    xi = L_iv(z)                                        # decreasing map: xi in [L(z.hi), L(z.lo)]
    return z * cert.Ghat_range(xi) / (1 - z)

def Lambda_prime_range(cert, z):
    """Lambda'(z) = [G_hat(xi) - G_hat'(xi)/ln2]/(1-z) + z G_hat(xi)/(1-z)^2, xi = L(z), on z subset of (0, 1/2]"""
    xi = L_iv(z); G = cert.Ghat_range(xi); Gp = Ghat_prime_range(cert, xi); om = 1 - z
    return (G - Gp / LN2) / om + z * G / om.sq()

# ----------------------------------------------------------------------------------------------------------------
# region 2
# ----------------------------------------------------------------------------------------------------------------
def phi2_over_v_lower(cert, X, Yp):
    """lower bound of Phi/v on the cell x in X, y' in Yp (both intervals)"""
    p = exp2neg(X); v = exp2neg(Yp); ellv = ell_iv(v); lam = v * ellv / LN2          # lambda = L(1-v)
    # A = [G_hat(x) - G_hat(x+lam)]/v : mean value (-(ell(v)/ln2) G_hat'(xi)) and direct
    Xl = Iv(X.lo, UP(X.hi + lam.hi))
    A_mv = -(ellv / LN2) * Ghat_prime_range(cert, Xl)
    A_dir = (cert.Ghat_range(X) - cert.Ghat_range(X + lam)) / v
    A_lo = np.maximum(A_mv.lo, A_dir.lo)
    B = cert.Ghat_range(Yp) / (1 - v)
    Cc = (-8) * p * X
    D = (-8) * (1 - v) * (1 - p) * ellv / LN2
    Ee = (-8) * (1 - p)
    # F = -[Psi(p(1-v)) - Psi(p)]/v = p * mean(Psi') over [p(1-v), p]  (direct alternative)
    zlo = np.maximum(DN(p.lo * (1 - v.hi)), 1e-300); Z = Iv(zlo, p.hi)
    F_mv = p * psi_prime_iv(Z)
    F_dir = (psi_iv(p) - psi_iv(p * (1 - v))) / v
    F_lo = np.maximum(F_mv.lo, F_dir.lo)
    Gg = psit_over_z_iv(v)                                                             # Psi(1-v)/v
    lo = A_lo + B.lo + Cc.lo + D.lo + Ee.lo + F_lo + Gg.lo
    gp = Ghat_prime_range(cert, Xl); smax = np.maximum(np.abs(gp.lo), np.abs(gp.hi))
    wx = 2 * cert.Ghat_range(X).width() / v.lo + Cc.width() + p.width() * np.abs(psi_prime_iv(Z).lo)
    wy = B.width() + D.width() + Gg.width() + smax * lam.width() / v.lo
    return lo, wx, wy

def verify_region2(cert, max_depth=14, xmax=None, ypmax=None):
    xs = cert.xs; K = cert.K
    xn = xs if xmax is None else np.concatenate([xs, K + np.arange(1, xmax - K + 1)])
    yn = xs if ypmax is None else np.concatenate([xs, K + np.arange(1, ypmax - K + 1)])
    I, J = np.meshgrid(np.arange(len(xn) - 1), np.arange(len(yn) - 1), indexing="ij"); I = I.ravel(); J = J.ravel()
    x0, x1, y0, y1 = xn[I], xn[I + 1], yn[J], yn[J + 1]
    return _adaptive(lambda X, Y: phi2_over_v_lower(cert, X, Y), x0, x1, y0, y1, max_depth, "region 2")

# ----------------------------------------------------------------------------------------------------------------
# region 3
# ----------------------------------------------------------------------------------------------------------------
def phi3_over_u_lower(cert, Xp, Yp):
    """lower bound of Phi/u on the cell x' in Xp, y' in Yp (u = 2^-x' <= v = 2^-y'); returns (lo, wx, wy) where wx, wy
    are the widths attributable to the x' and y' axes through the enclosures actually used"""
    n = len(Xp.lo)
    u = exp2neg(Xp); v = exp2neg(Yp); ellu = ell_iv(u); ellv = ell_iv(v)
    w = u + v - u * v                                    # w = 1 - pq
    ulo = np.maximum(u.lo, 1e-300)
    P1 = cert.Ghat_range(Xp) / (1 - u)
    res_a = np.full(n, np.inf); res_b = np.full(n, np.inf)
    wax = np.zeros(n); way = np.zeros(n); wbx = np.zeros(n); wby = np.zeros(n)
    # case (a): w <= 1/2 -> G(pq) = Lambda(w); valid on the part of the cell where w <= 1/2
    a_mask = w.lo <= 0.5
    if a_mask.any():
        sel = a_mask
        va = Iv(v.lo[sel], v.hi[sel]); wa = Iv(w.lo[sel], np.minimum(w.hi[sel], 0.5)); ua = Iv(u.lo[sel], u.hi[sel])
        Zr = Iv(va.lo, wa.hi)
        P2_mv = -(1 - va) * Lambda_prime_range(cert, Zr)
        Lv = Lambda_range(cert, va); Lw = Lambda_range(cert, wa)
        P2_dir = (Lv - Lw) / ua
        use_dir = P2_dir.lo >= P2_mv.lo
        res_a[sel] = np.maximum(P2_mv.lo, P2_dir.lo)
        # widths of the used form: direct -> Lambda(v) width (y), Lambda(w) width (half x, half y), |P2| du/u (x);
        # mean value -> (1-v) Lambda' width over [v, w]: shrinks with v only through the z-range, attribute to y
        dx = np.where(use_dir, 0.5 * Lw.width() / ulo[sel] + np.abs(P2_dir.lo) * ua.width() / ulo[sel], np.abs(P2_mv.lo) * 0.0)
        dy = np.where(use_dir, (Lv.width() + 0.5 * Lw.width()) / ulo[sel], P2_mv.width())
        wax[sel] = dx; way[sel] = dy
    # case (b): w >= 1/2 -> G(pq) = G_hat(L(pq)), L(pq) = 1 + [u ell(u)/ln2 - log1p(m)/ln2], m = 1 - 2v = -expm1((1-y') ln2)
    b_mask = w.hi >= 0.5
    if b_mask.any():
        sel = b_mask
        ub = Iv(u.lo[sel], u.hi[sel]); vb = Iv(v.lo[sel], v.hi[sel]); Yb = Iv(Yp.lo[sel], Yp.hi[sel])
        mlo = paddn(-np.expm1((1 - Yb.lo) * np.log(2.0))); mhi = padup(-np.expm1((1 - Yb.hi) * np.log(2.0)))
        m = Iv(np.maximum(mlo, 0.0), np.maximum(mhi, 0.0))
        l1pm = Iv(paddn(np.log1p(m.lo)), padup(np.log1p(m.hi)))
        Lpq_m1 = (ub * ell_iv(ub) - l1pm) / LN2
        Lpq_m1 = Iv(np.maximum(Lpq_m1.lo, 0.0), np.maximum(Lpq_m1.hi, 0.0))
        half_minus_v = m / 2
        Z1 = Iv(vb.lo, np.full_like(vb.lo, 0.5))
        lam1 = Lambda_prime_range(cert, Z1)
        X1 = Iv(np.ones_like(ub.lo), UP(1 + Lpq_m1.hi))
        gp1 = Ghat_prime_range(cert, X1)
        P2_mv = -(half_minus_v / ub) * lam1 - (Lpq_m1 / ub) * gp1
        Lv = Lambda_range(cert, vb); GL = cert.Ghat_range(1 + Lpq_m1)
        P2_dir = (Lv - GL) / ub
        use_dir = P2_dir.lo >= P2_mv.lo
        res_b[sel] = np.maximum(P2_mv.lo, P2_dir.lo)
        dx = np.where(use_dir, 0.5 * GL.width() / ulo[sel] + np.abs(P2_dir.lo) * ub.width() / ulo[sel], 0.5 * P2_mv.width())
        dy = np.where(use_dir, (Lv.width() + 0.5 * GL.width()) / ulo[sel], 0.5 * P2_mv.width())
        wbx[sel] = dx; wby[sel] = dy
    P2_lo = np.minimum(res_a, res_b)
    # the case whose bound is the binding one contributes its widths
    use_a = res_a <= res_b
    wPx = np.where(use_a, wax, wbx); wPy = np.where(use_a, way, wby)
    # P3 = E/u
    T1 = 8 * (1 - u) * v * ellu / LN2
    T2 = 8 * (1 - v) * v * ellv / LN2
    T3 = 8 * v
    Zw = Iv(v.lo, np.minimum(w.hi, 0.75))
    T4_mv = (1 - v) * psit_prime_iv(Zw)                              # [Psit(w) - Psit(v)]/u = (1-v) Psit'(xi)
    T4_dir = (psit_iv(w) - psit_iv(v)) / u
    T4_hi = np.minimum(T4_mv.hi, T4_dir.hi)
    T4_w = np.minimum(T4_mv.width(), T4_dir.width())
    T5 = psit_over_z_iv(u)                                           # Psit(u)/u
    P3_hi = T1.hi + T2.hi + T3.hi + T4_hi - T5.lo
    wx = P1.width() + T1.width() + T5.width() + wPx + 0.5 * T4_w
    wy = T2.width() + T3.width() + wPy + 0.5 * T4_w
    return P1.lo + P2_lo - P3_hi, wx, wy

def verify_region3(cert, max_depth=14, xpmax=None):
    xs = cert.xs; K = cert.K
    xn = xs if xpmax is None else np.concatenate([xs, K + np.arange(1, xpmax - K + 1)])
    nx, ny = len(xn) - 1, len(xs) - 1
    I, J = np.meshgrid(np.arange(nx), np.arange(ny), indexing="ij"); I = I.ravel(); J = J.ravel()
    keep = I >= J                                                    # x' >= y'  (u <= v)
    I, J = I[keep], J[keep]
    x0, x1, y0, y1 = xn[I], xn[I + 1], xs[J], xs[J + 1]
    return _adaptive(lambda X, Y: phi3_over_u_lower(cert, X, Y), x0, x1, y0, y1, max_depth, "region 3")

# ----------------------------------------------------------------------------------------------------------------
# adaptive driver (2-D) and 1-D checks
# ----------------------------------------------------------------------------------------------------------------
def _adaptive(bound_fn, x0, x1, y0, y1, max_depth, name, chunk=1000000, cap=4000000, batch=2000000):
    """bound_fn returns (lower bound, width attributable to x, width attributable to y); a failing cell is split in two
    along the axis with the larger attributed width.  Memory-bounded: the initial cells are processed in batches of
    `batch`, each refined depth-first; whenever a level's failing set exceeds `cap` cells it is cut into pieces that
    are queued separately, so at most about 2*cap cells are alive at any time."""
    t0 = time.time(); n_init = len(x0)
    stack = [(x0[i:i + batch], x1[i:i + batch], y0[i:i + batch], y1[i:i + batch], 0) for i in range(0, n_init, batch)][::-1]
    total_cells = 0; max_depth_seen = 0; worst_final = np.inf; batches_done = 0
    while stack:
        cx0, cx1, cy0, cy1, depth = stack.pop()
        while True:
            lo = np.empty(len(cx0)); wx = np.empty(len(cx0)); wy = np.empty(len(cx0))
            for s in range(0, len(cx0), chunk):
                e = min(len(cx0), s + chunk)
                lo[s:e], wx[s:e], wy[s:e] = bound_fn(Iv(cx0[s:e], cx1[s:e]), Iv(cy0[s:e], cy1[s:e]))
            total_cells += len(cx0); max_depth_seen = max(max_depth_seen, depth)
            bad = lo < 0; nb = int(bad.sum())
            if nb == 0:
                break
            if depth == max_depth:
                j = int(np.argmin(lo)); worst_final = min(worst_final, float(lo[j]))
                print("  %s FAILED at max depth %d: cell [%.6f, %.6f] x [%.6f, %.6f] bound %.3e" % (name, depth, cx0[j], cx1[j], cy0[j], cy1[j], lo[j]), flush=True)
                return False
            bx0, bx1, by0, by1 = cx0[bad], cx1[bad], cy0[bad], cy1[bad]
            sx = wx[bad] >= wy[bad]
            xm = (bx0 + bx1) / 2; ym = (by0 + by1) / 2
            nx0 = np.concatenate([bx0[sx], xm[sx], bx0[~sx], bx0[~sx]]); nx1 = np.concatenate([xm[sx], bx1[sx], bx1[~sx], bx1[~sx]])
            ny0 = np.concatenate([by0[sx], by0[sx], by0[~sx], ym[~sx]]); ny1 = np.concatenate([by1[sx], by1[sx], ym[~sx], by1[~sx]])
            depth += 1
            if len(nx0) > cap:
                # queue the pieces and continue with the first one
                pieces = [(nx0[i:i + cap], nx1[i:i + cap], ny0[i:i + cap], ny1[i:i + cap], depth) for i in range(0, len(nx0), cap)]
                stack.extend(pieces[1:][::-1])
                cx0, cx1, cy0, cy1, depth = pieces[0]
            else:
                cx0, cx1, cy0, cy1 = nx0, nx1, ny0, ny1
        batches_done += 1
        if batches_done % 5 == 0 or not stack:
            print("  %s: %d batches done, %d queued, %d cells evaluated so far, deepest level %d  (%.0f s)" % (name, batches_done, len(stack), total_cells, max_depth_seen, time.time() - t0), flush=True)
    print("  %s VERIFIED: %d initial cells, %d cells evaluated, deepest level %d  (%.0f s)" % (name, n_init, total_cells, max_depth_seen, time.time() - t0), flush=True)
    return True

def phi1_lower(cert, X, Y):
    """region 1 bound with width attribution (same bound as fei_cert.verify_region1)"""
    GX = cert.Ghat_range(X); GY = cert.Ghat_range(Y); GS = cert.Ghat_range(X + Y); E = E_iv(X, Y)
    lo = GX.lo + GY.lo - GS.hi - E.hi
    return lo, GX.width() + 0.5 * GS.width() + 0.5 * E.width(), GY.width() + 0.5 * GS.width() + 0.5 * E.width()

def verify_region1_dir(cert, max_depth=30):
    xs = cert.xs; n = len(xs) - 1
    I, Kk = np.triu_indices(n)
    return _adaptive(lambda X, Y: phi1_lower(cert, X, Y), xs[I], xs[I + 1], xs[Kk], xs[Kk + 1], max_depth, "region 1")

def _adaptive1d(bound_fn, a0, a1, max_depth, name):
    t0 = time.time()
    for depth in range(max_depth + 1):
        lo = bound_fn(Iv(a0, a1)); bad = lo < 0; nb = int(bad.sum())
        print("  %s depth %2d: %7d cells, %6d failing, min lower bound %+.3e  (%.0f s)" % (name, depth, len(a0), nb, lo.min(), time.time() - t0), flush=True)
        if nb == 0: return True
        if depth == max_depth:
            j = int(np.argmin(lo)); print("  FAILED: worst cell [%.6f, %.6f] bound %.3e" % (a0[j], a1[j], lo[j])); return False
        b0, b1 = a0[bad], a1[bad]; m = (b0 + b1) / 2
        a0 = np.concatenate([b0, m]); a1 = np.concatenate([m, b1])
    return False

def e_iv(Y):
    """e(q) = lim_{p->0} E(p,q) = 8 q y + 8(1-q) - Psi(q) for q = 2^-y"""
    q = exp2neg(Y)
    return 8 * q * Y + 8 * (1 - q) - psi_iv(q)

def check_T2(cert, max_depth=20):
    """tail-interior (p < 2^-K, 2^-K <= q <= 1/2):  G_num(y) - sigma_t y - e(q) + c(1-2^-K)(1-q) - 8(1-q) K 2^-K - (12/ln2) 2^-K >= 0"""
    K = cert.K; pK = Iv(2.0 ** -K); sig = Iv(cert.tail_slope)
    def bound(Y):
        q = exp2neg(Y)
        # G_num range on Y without the margin, then subtract sigma_t * y (interval product)
        Gn = cert.Gnum_range(Y)
        val = Gn - sig * Y - e_iv(Y) + Iv(cert.c) * (1 - pK) * (1 - q) - 8 * (1 - q) * Iv(K) * pK - (12 / LN2) * pK
        return val.lo
    xs = cert.xs
    return _adaptive1d(bound, xs[:-1], xs[1:], max_depth, "T2 (p in tail, q <= 1/2)")

def check_T3(cert, max_depth=20, psip_max=None):
    """tail p (x > K) with q > 1/2:  G_hat(y')/(1-v) - (ell(v)/ln2) sigma_t - 8(1-v) ell(v)/ln2 - 8 + Psi(1-v)/v - corr >= 0,
       corr = 2^-K (c + 8K + |Psi'|_max) covers every p-dependent term for p <= 2^-K: the margin part -c p, the term
       -8 p x <= 8 K 2^-K (x 2^-x decreasing for x >= K), and p Psi'(zeta); the factors (1-p) in D and E were kept as 1"""
    K = cert.K; pK = 2.0 ** -K; sig = Iv(cert.tail_slope)
    if psip_max is None: psip_max = psi_prime_abs_max()
    corr = Iv(padup(pK * (cert.c + 8 * K + psip_max)))
    def bound(Yp):
        v = exp2neg(Yp); ellv = ell_iv(v)
        val = cert.Ghat_range(Yp) / (1 - v) - (ellv / LN2) * sig - 8 * (1 - v) * ellv / LN2 - 8 + psit_over_z_iv(v) - corr
        return val.lo
    xs = cert.xs
    return _adaptive1d(bound, xs[:-1], xs[1:], max_depth, "T3 (p in tail, q > 1/2)")

def psi_prime_abs_max():
    """rigorous bound on |Psi'| over (0, 1/2]: computed on a fine partition"""
    z0 = np.concatenate([2.0 ** -np.arange(60, 2, -1) / 1.0, np.linspace(0.25, 0.5, 2000)[:-1]])
    z1 = np.concatenate([2.0 ** -np.arange(59, 1, -1), np.linspace(0.25, 0.5, 2000)[1:]])
    z0 = np.concatenate([[1e-300], z0]); z1 = np.concatenate([[2.0 ** -60], z1])
    r = psi_prime_iv(Iv(z0, z1))
    return float(np.max(np.maximum(np.abs(r.lo), np.abs(r.hi))))

# ----------------------------------------------------------------------------------------------------------------
# beyond-grid lemmas (explicit constants from the certificate)
# ----------------------------------------------------------------------------------------------------------------
def lemma_T1(cert):
    """both p, q < 2^-K: Phi = b_t + c(1-p)(1-q) - E(p,q) with b_t = G_J - sigma_t K and E - b* <= (16K + 19) 2^-K"""
    K = cert.K; bt = Iv(cert.G[-1]) - Iv(cert.tail_slope) * K
    eta = Iv(padup((16 * K + 19) * 2.0 ** -K))
    val = bt - BSTAR + Iv(cert.c) * (1 - 2.0 ** -K) ** 2 - eta          # (1-p)(1-q) >= (1-2^-K)^2
    print("  T1 (both p, q < 2^-K): b_t - b* = %+.3e, margin lower bound %+.3e -> %s" % ((bt - BSTAR).lo, val.lo, "OK" if val.lo > 0 else "FAIL"))
    return val.lo > 0

def lemma_region2_deep_v(cert, sig_max, psip_max):
    """region 2 with v < 2^-K (q > 1 - 2^-K), any p <= 1/2:
       Phi/v >= G_hat(K)/(1-v) - (ell(v)/ln2) max|G_hat'| - 8 max(p x) - 8 ell(v)/ln2 - 8 - (1/2) |Psi'|_max, ell(v) <= ell(2^-K)"""
    K = cert.K; vK = Iv(2.0 ** -K); ellK = ell_pt(2.0 ** -K)
    GK = cert.Ghat_range(Iv(K))
    val = GK - (ellK / LN2) * Iv(sig_max) - 8 * Iv(1 / (math.e * math.log(2))) - 8 * ellK / LN2 - 8 - 0.5 * Iv(psip_max)
    print("  region 2, v < 2^-K: lower bound %+.3f -> %s" % (val.lo, "OK" if val.lo > 0 else "FAIL"))
    return val.lo > 0

def lemma_region3_deep_u(cert, Xmax, sig_max, psitp_max):
    """region 3 with u < 2^-Xmax, 2^-K <= v <= 1/2:
       Phi/u >= G_hat(Xmax) - (1-v) max Lambda' - 1.5 sigma_max ... computed with intervals over v"""
    K = cert.K
    # max of Lambda' over z in [2^-K, 1/2 + 2^-K]: partition in xi
    xi0 = np.concatenate([cert.xs[:-1], [K]]); xi1 = np.concatenate([cert.xs[1:], [K + 1]])
    Z = exp2neg(Iv(xi0, xi1)); Z = Iv(Z.lo, np.minimum(Z.hi, 0.5))
    lam_max = float(np.max(Lambda_prime_range(cert, Z).hi))
    GX = cert.Ghat_range(Iv(Xmax))
    # P2 >= -max(lam_max, lam_max + 1.5 sigma_max) [case b adds -(L(pq)-1)/u * G_hat' with (L(pq)-1)/u <= ell(u)/ln2 <= 1.5]
    # E/u = T1 + T2 + T3 + T4 - T5 with T1 <= 8 v ell(u)/ln2 <= 4 ell(2^-Xmax)/ln2, T2 <= 8 (1-v) v ell(v)/ln2 <= 8 ell(1/2)/ln2 (v <= 1/2),
    # T3 <= 4, T4 = (1-v) Psit'(xi) <= max|Psit'| over (0, 3/4], -T5 <= 0
    p3 = 4 * ell_pt(2.0 ** -Xmax).hi / math.log(2) + 8 * ell_pt(0.5).hi / math.log(2) + 4 + psitp_max
    val = GX.lo - lam_max - 1.5 * max(sig_max, 0.0) - p3
    print("  region 3, u < 2^-%d: max Lambda' = %.2f, lower bound %+.2f -> %s" % (Xmax, lam_max, val, "OK" if val > 0 else "FAIL"))
    return val > 0

def lemma_region3_both_deep(cert):
    """region 3 with u <= v <= 2^-K (both p, q above 1 - 2^-K).  In the linear tail G_hat(xi) <= G_hat(y') <= G_hat(x') for
    xi in [L(w), L(v)] and G_hat' >= sigma_t, and 1/(1-z) <= 1 + 2w <= 1 + 4v for z <= w <= 2v, so
       P1 + P2 >= G_hat(y') - (1-v)[(G_hat(y') - sigma_t/ln2)(1 + 4v) + 2v (1 + 4v)^2 G_hat(y')] >= (1-v) sigma_t/ln2 - 12 v G_hat(y'),
       E/u <= T1 + T2 + T3 + T4 - T5 <= 12v + 12v + 8v + (4/ln2)(3u - v)^+ <= 32v + (4/ln2) 2v <= 45 v,
    and 2^-(y'-K) G_hat(y') <= G_J + sigma_t/(e ln2) + c for y' >= K, so v G_hat(y') <= 2^-K (G_J + sigma_t/(e ln2) + c)."""
    K = cert.K; v = 2.0 ** -K
    GY = cert.G[-1] + cert.tail_slope / (math.e * math.log(2)) + cert.c
    val = (1 - v) * cert.tail_slope / math.log(2) - 12 * v * GY - 45 * v
    print("  region 3, both u, v <= 2^-K: lower bound %+.3f -> %s" % (val, "OK" if val > 0 else "FAIL"))
    return val > 0

if __name__ == "__main__":
    src = sys.argv[1]; c = float(sys.argv[2]); max_depth = int(sys.argv[3]) if len(sys.argv) > 3 else 14
    which = sys.argv[4] if len(sys.argv) > 4 else "all"
    d = np.load(src); xs, G, C0 = d["xs"], d["G"], float(d["C"]); K = float(xs[-1])
    tail_slope = (G[-1] - BSTAR) / K
    cert = Cert(xs, G, c, tail_slope=tail_slope); build_slope_tables(cert)
    print("certificate %s: C0=%.7f, %d nodes, K=%g, c=%g, tail slope %.6f -> C_cert = %.7f" % (src, C0, len(xs), K, c, tail_slope, cert.C_cert()), flush=True)
    sig_max = float(np.max(np.abs(cert.slopes))) + cert.c * math.log(2)
    psip_max = psi_prime_abs_max()
    print("  |G_hat'| <= %.3f, |Psi'| <= %.3f on (0,1/2]" % (sig_max, psip_max), flush=True)
    results = {}
    if which in ("all", "lemmas"):
        results["T1"] = lemma_T1(cert)
        results["R2deep"] = lemma_region2_deep_v(cert, sig_max, psip_max)
        Xmax = int(K + 20)
        z = Iv(np.array([1e-300, 2.0 ** -60]), np.array([2.0 ** -60, 0.75])); psitp_max = float(np.max(np.abs(psit_prime_iv(z).lo)))
        psitp_max = max(psitp_max, float(np.max(np.abs(psit_prime_iv(z).hi))))
        results["R3deep"] = lemma_region3_deep_u(cert, Xmax, sig_max, psitp_max)
        results["R3both"] = lemma_region3_both_deep(cert)
    if which in ("all", "T2"): results["T2"] = check_T2(cert)
    if which in ("all", "T3"): results["T3"] = check_T3(cert, psip_max=psip_max)
    if which in ("all", "R2"): results["R2"] = verify_region2(cert, max_depth)
    if which in ("all", "R3"): results["R3"] = verify_region3(cert, max_depth, xpmax=int(K + 20))
    if which in ("all", "R1"): results["R1"] = verify_region1_dir(cert, max_depth)
    print("RESULTS:", results)
    print("ALL VERIFIED -> H(f) <= %.7f I(f) for every read-once formula" % cert.C_cert() if all(results.values()) else "NOT all verified")
