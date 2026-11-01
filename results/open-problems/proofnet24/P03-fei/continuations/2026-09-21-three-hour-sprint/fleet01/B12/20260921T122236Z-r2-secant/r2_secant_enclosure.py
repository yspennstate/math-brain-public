"""B12 region-2 x in [1,2] tightening for the M=96,c=.003 read-once FEI certificate.

Drop-in companion to code/fei_cert_r1x.py.  The new lower bound keeps the exact
piecewise-linear SECANT in the region-2 A term, instead of either dividing an
interval numerator by v or replacing the secant by the full slope range.

For lambda=L(1-v)=v*ell(v)/ln2 and p=2^-x,
 [Ghat(x)-Ghat(x+lambda)]/v
   = -(ell(v)/ln2) Sec_Gnum(x,lambda) - c p,
where Sec_Gnum=(Gnum(x+lambda)-Gnum(x))/lambda.  The c-term is exact because
2^-lambda=1-v.  If x stays in one source segment, and we cut the
(x,lambda)-rectangle by x+lambda=node, the secant is linear-fractional on
each resulting polygon and therefore reaches both extrema at polygon
vertices.  Those vertices are rectangle corners and intersections of
x+lambda=node with rectangle edges.

The driver is intentionally sharded by y-node index so runs are bounded and
resumable.  It refuses a candidate whose Git blob is not the pinned M=96
candidate used by the c=.003 certificate.
"""
import hashlib
import math
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.normpath(os.path.join(
    HERE, "..", "..", "..", "..", "2026-09-21-readonce-certificate", "code"))
if BASE not in sys.path:
    sys.path.insert(0, BASE)

from fei_cert import Iv, UP, DN, LN2, exp2neg, ell_iv, psi_iv
from fei_cert23 import (
    Ghat_prime_range, psi_prime_iv, psit_over_z_iv, _adaptive)
from fei_cert_r1x import (
    _clip_iv, D_enclose, load_cert)

EXPECTED_CANDIDATE_GIT_BLOB = "1e2a1a5c293fa7b6ec9885b7a410910d6589be80"
EXPECTED_CANDIDATE_BYTES = 70354


def git_blob_sha1(raw):
    return hashlib.sha1(
        b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()


def verify_candidate_file(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    got = git_blob_sha1(raw)
    if len(raw) != EXPECTED_CANDIDATE_BYTES or got != EXPECTED_CANDIDATE_GIT_BLOB:
        raise RuntimeError(
            "candidate mismatch: bytes=%d git_blob=%s" % (len(raw), got))
    return got


def _seg_pair(cert, lo, hi):
    """Segments touched by [lo,hi], with a node assigned to an adjacent segment."""
    n = len(cert.xs) - 1
    a = np.clip(np.searchsorted(cert.xs, lo, side="right") - 1, 0, n - 1)
    b = np.clip(np.searchsorted(cert.xs, hi, side="left") - 1, 0, n - 1)
    return a, np.maximum(a, b)


def _secant_at(cert, Xv, Lv):
    """Interval containing the PL secant at interval-point coordinates.

    When both endpoints provably occupy the same linear segment, return that
    segment slope directly; this avoids cancellation when lambda is tiny.
    """
    Z = Xv + Lv
    r = (cert.Gnum_range(Z) - cert.Gnum_range(Xv)) / Lv
    ia0, ia1 = _seg_pair(cert, Xv.lo, Xv.hi)
    iz0, iz1 = _seg_pair(cert, Z.lo, Z.hi)
    same = (ia0 == ia1) & (iz0 == iz1) & (ia0 == iz0)
    if np.any(same):
        s = cert.slopes[ia0]
        lo = np.where(same, DN(s), r.lo)
        hi = np.where(same, UP(s), r.hi)
        return Iv(lo, hi)
    return r


def secant_slope_enclose(cert, x0, x1, l0, l1):
    """Exact-to-rounding enclosure of Sec_Gnum over rectangles.

    Precondition: each x-side [x0,x1] is contained in one node segment and
    0 < l0 <= l1.  The proof is the linear-fractional vertex lemma in REPORT.md.
    """
    lo = np.full(len(x0), np.inf)
    hi = np.full(len(x0), -np.inf)

    def absorb(Xv, Lv, mask=None):
        nonlocal lo, hi
        if mask is None:
            r = _secant_at(cert, Xv, Lv)
            lo = np.minimum(lo, r.lo)
            hi = np.maximum(hi, r.hi)
        else:
            r = _secant_at(cert, Xv, Lv)
            lo[mask] = np.minimum(lo[mask], r.lo)
            hi[mask] = np.maximum(hi[mask], r.hi)

    for xa, la in ((x0,l0),(x0,l1),(x1,l0),(x1,l1)):
        absorb(Iv(xa), Iv(la))

    xs = cert.xs
    slo = DN(x0 + l0)
    shi = UP(x1 + l1)
    i_lo = np.searchsorted(xs, slo, side="right")
    i_hi = np.searchsorted(xs, shi, side="left") - 1
    ncross = np.maximum(i_hi - i_lo + 1, 0)

    for j in range(int(ncross.max()) if len(ncross) else 0):
        m = ncross > j
        if not np.any(m):
            break
        s = xs[i_lo[m] + j]
        mx0,mx1,ml0,ml1 = x0[m],x1[m],l0[m],l1[m]
        clo = np.full(int(m.sum()), np.inf)
        chi = np.full(int(m.sum()), -np.inf)
        candidates = (
            (Iv(mx0), _clip_iv(s-mx0, ml0, ml1)),
            (Iv(mx1), _clip_iv(s-mx1, ml0, ml1)),
            (_clip_iv(s-ml0, mx0, mx1), Iv(ml0)),
            (_clip_iv(s-ml1, mx0, mx1), Iv(ml1)),
        )
        for Xv,Lv in candidates:
            r = _secant_at(cert, Xv, Lv)
            clo = np.minimum(clo, r.lo)
            chi = np.maximum(chi, r.hi)
        lo[m] = np.minimum(lo[m], clo)
        hi[m] = np.maximum(hi[m], chi)
    return Iv(lo, hi)


def _ce_lower_fleet01(X):
    """Exact endpoint lower bound for -8 p x - 8(1-p), valid on 1<=x<=2."""
    p = exp2neg(X)
    direct = (-8) * (1 + p * (X - 1))
    lo = direct.lo.copy()
    m = (X.lo >= 1.0) & (X.hi <= 2.0)
    if np.any(m):
        xh = Iv(X.hi[m])
        endpoint = (-8) * (1 + exp2neg(xh) * (xh - 1))
        lo[m] = np.maximum(lo[m], endpoint.lo)
    return lo, direct.width()


def _d_lower_monotone(X, Yp):
    """Endpoint lower bound for -8(1-v)(1-p)ell(v)/ln2.

    a(x)=1-2^-x increases in x.  b(v)=(1-v)ell(v) has
    b'(v)=(v+ln(1-v))/v^2 < 0, while v=2^-y decreases in y.
    Hence the negative product is minimized at (x_hi,y_hi).
    """
    p = exp2neg(X)
    v = exp2neg(Yp)
    direct = (-8) * (1 - v) * (1 - p) * ell_iv(v) / LN2
    xh, yh = Iv(X.hi), Iv(Yp.hi)
    ph, vh = exp2neg(xh), exp2neg(yh)
    endpoint = (-8) * (1 - vh) * (1 - ph) * ell_iv(vh) / LN2
    return np.maximum(direct.lo, endpoint.lo), direct.width()


def _build_kprime_tables(cert):
    """Sparse tables for K'(t)=Gnum'(t)+ln2*r*(c-Psi'(r)), r=2^-t."""
    if hasattr(cert, "_b12_kp_min"):
        return
    T = Iv(cert.xs[:-1], cert.xs[1:])
    r = exp2neg(T)
    smooth = LN2 * r * (Iv(cert.c) - psi_prime_iv(r))
    kp = Iv(cert.slopes) + smooth
    mins = [kp.lo.copy()]
    maxs = [kp.hi.copy()]
    n = len(cert.slopes)
    k = 1
    while (1 << k) <= n:
        h = 1 << (k - 1)
        prev_lo, prev_hi = mins[-1], maxs[-1]
        m = n - (1 << k) + 1
        mins.append(np.minimum(prev_lo[:m], prev_lo[h:h+m]))
        maxs.append(np.maximum(prev_hi[:m], prev_hi[h:h+m]))
        k += 1
    cert._b12_kp_min = mins
    cert._b12_kp_max = maxs


def _kprime_range(cert, a, b):
    """Safe range of K' on [a,b] inside the finite candidate grid."""
    _build_kprime_tables(cert)
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    if np.any(a < cert.xs[0]) or np.any(b > cert.K):
        raise ValueError("B12 joint K' range is only implemented inside candidate grid")
    n = len(cert.slopes)
    i = np.clip(np.searchsorted(cert.xs, a, side="right") - 1, 0, n - 1)
    j = np.clip(np.searchsorted(cert.xs, b, side="left") - 1, 0, n - 1)
    j = np.maximum(i, j)
    ln = np.floor(np.log2(np.maximum(j-i+1,1))).astype(int)
    lo = np.empty(len(i))
    hi = np.empty(len(i))
    for k in np.unique(ln):
        sel = ln == k
        h = 1 << int(k)
        left = i[sel]
        right = j[sel] - h + 1
        lo[sel] = np.minimum(cert._b12_kp_min[k][left],
                             cert._b12_kp_min[k][right])
        hi[sel] = np.maximum(cert._b12_kp_max[k][left],
                             cert._b12_kp_max[k][right])
    return Iv(lo,hi)


def _af_joint_lower(cert, X, lam, ellv):
    """Joint lower bound for A+F as one divided difference.

    K(t)=Ghat(t)+Psi(2^-t).  Then
      A+F = [K(x)-K(x+lambda)]/v
          = -(ell(v)/ln2) average_[x,x+lambda] K'(t).
    Bounding K' segment-by-segment preserves the correlation between the
    candidate slope and the Psi derivative which separate A/F bounds discard.
    """
    Kp = _kprime_range(cert, X.lo, UP(X.hi + lam.hi))
    return (-(ellv / LN2) * Kp).lo


def phi2_over_v_lower_secant(cert, X, Yp):
    """Rigorous region-2 lower bound, strengthening the existing exact-A bound."""
    p = exp2neg(X)
    v = exp2neg(Yp)
    ellv = ell_iv(v)
    lam = v * ellv / LN2
    Xl = Iv(X.lo, UP(X.hi + lam.hi))

    # Existing three A enclosures, retained fail-safe.
    A_mv = -(ellv / LN2) * Ghat_prime_range(cert, Xl)
    A_dir = (cert.Ghat_range(X) - cert.Ghat_range(X + lam)) / v
    Dnum = D_enclose(cert, X.lo, X.hi, lam.lo, lam.hi)
    A_ex = (Dnum + Iv(cert.c) * p * (exp2neg(lam) - 1)) / v

    # New secant enclosure.  It removes the small-v division and makes the
    # certificate margin contribution exactly -c p.
    S = secant_slope_enclose(cert, X.lo, X.hi, lam.lo, lam.hi)
    A_sec = -(ellv / LN2) * S - Iv(cert.c) * p
    A_lo = np.maximum.reduce([A_mv.lo, A_dir.lo, A_ex.lo, A_sec.lo])

    B = cert.Ghat_range(Yp) / (1 - v)
    CE_lo, CE_w = _ce_lower_fleet01(X)
    D_lo, D_w = _d_lower_monotone(X, Yp)

    zlo = np.maximum(DN(p.lo * (1 - v.hi)), 1e-300)
    Z = Iv(zlo, p.hi)
    F_mv = p * psi_prime_iv(Z)
    F_dir = (psi_iv(p) - psi_iv(p * (1 - v))) / v
    F_lo = np.maximum(F_mv.lo, F_dir.lo)
    # A+F is also one divided difference of K=Ghat+Psi; this joint MVT
    # preserves candidate-slope/Psi-derivative correlation.
    AF_sep = A_lo + F_lo
    AF_joint = _af_joint_lower(cert, X, lam, ellv)
    AF_lo = np.maximum(AF_sep, AF_joint)
    Gg = psit_over_z_iv(v)

    lo = AF_lo + B.lo + CE_lo + D_lo + Gg.lo

    # Splitting widths are a heuristic only; every lower bound above is
    # independently rigorous.  Use the tightest A width and keep conservative
    # attribution for the remaining terms.
    wA = np.minimum.reduce([A_mv.width(), A_dir.width(), A_ex.width(), A_sec.width()])
    wx = 0.5*wA + CE_w + 0.5*D_w + p.width()*np.abs(psi_prime_iv(Z).lo)
    wy = 0.5*wA + B.width() + 0.5*D_w + Gg.width()
    return lo, wx, wy


def verify_fleet01_shard(cert, y_index_lo, y_index_hi, max_depth=30):
    """Verify the assigned x in [1,2] region for a bounded y-node shard."""
    xs = cert.xs
    xi = np.where((xs[:-1] >= 1.0) & (xs[1:] <= 2.0 + 8*np.finfo(float).eps))[0]
    ylo = max(0, int(y_index_lo))
    yhi = min(len(xs)-1, int(y_index_hi))
    if ylo >= yhi:
        raise ValueError("empty y shard")
    yi = np.arange(ylo, yhi)
    I, J = np.meshgrid(xi, yi, indexing="ij")
    I, J = I.ravel(), J.ravel()
    return _adaptive(
        lambda X,Y: phi2_over_v_lower_secant(cert, X, Y),
        xs[I], xs[I+1], xs[J], xs[J+1],
        max_depth,
        "region 2 B12 x[1,2] yidx[%d,%d)" % (ylo,yhi))


if __name__ == "__main__":
    if len(sys.argv) < 5:
        raise SystemExit(
            "usage: python r2_secant_enclosure.py CANDIDATE.npz C "
            "Y_INDEX_LO Y_INDEX_HI [MAX_DEPTH]")
    src = sys.argv[1]
    c = float(sys.argv[2])
    j0, j1 = int(sys.argv[3]), int(sys.argv[4])
    depth = int(sys.argv[5]) if len(sys.argv) > 5 else 30
    if abs(c - 0.003) > 1e-15:
        raise RuntimeError("this pinned run is for c=0.003 only")
    blob = verify_candidate_file(src)
    cert, C0 = load_cert(src, c)
    print("candidate_git_blob=%s bytes=%d C0=%.7f nodes=%d K=%g c=%g C_cert=%.7f" %
          (blob, EXPECTED_CANDIDATE_BYTES, C0, len(cert.xs), cert.K, c, cert.C_cert()),
          flush=True)
    ok = verify_fleet01_shard(cert, j0, j1, depth)
    print("B12_R2_X1_2_SHARD yidx=[%d,%d) max_depth=%d verified=%s" %
          (j0,j1,depth,ok), flush=True)
