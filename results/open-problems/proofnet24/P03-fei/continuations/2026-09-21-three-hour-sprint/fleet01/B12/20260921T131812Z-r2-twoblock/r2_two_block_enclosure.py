"""B12 region-2 x in [1,2] two-block tightening for the M=96,c=.003 read-once FEI certificate.

This is a fail-safe companion to the preceding B12 secant enclosure.  It uses an
exact regrouping of all region-2 terms before intervalization:

  Phi/v = DD[K0](x,lambda) + c(1-p) + CE(x) + Q_p(y),

where p=2^-x, v=2^-y, lambda=-log2(1-v),

  K0(t) = G_num(t) + Psi(2^-t),
  DD[K0] = [K0(x)-K0(x+lambda)]/v,
  CE(x) = -8[1+p(x-1)],
  Q_p(y) = G_num(y)/(1-v)
           - 8(1-p)(1-v)ell(v)/ln2 + Psi(1-v)/v.

The certificate-margin terms are therefore extracted EXACTLY as c(1-p).  This
is stronger than bounding the margin inside two different divided differences.
For Q, the negative D term is worst at x_hi, so p may be replaced by
p*=2^-x_hi.  On each y-node segment the remaining one-variable Q_{p*} has the
exact derivative

 Q'(y) = s/(1-v) - ln2*v*G_num(y)/(1-v)^2
         - ln2*(Psit'(v)-Psit(v)/v)
         + 8(1-p*)[1-ell(v)],

with s the segment slope and Psit(v)=Psi(1-v).  A fixed-sign derivative reduces
the cell minimum to an endpoint; otherwise a centred mean-value enclosure is
used.  The old B12 lower bound is retained and the final lower bound is the
maximum, so this module cannot weaken a valid certificate.
"""
import importlib.util
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
PREV = os.path.normpath(os.path.join(
    HERE, "..", "20260921T122236Z-r2-secant", "r2_secant_enclosure.py"))
_spec = importlib.util.spec_from_file_location("b12_r2_prev", PREV)
if _spec is None or _spec.loader is None:
    raise ImportError("cannot load preceding B12 secant enclosure")
R2 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(R2)

Iv = R2.Iv
UP = R2.UP
DN = R2.DN
LN2 = R2.LN2
exp2neg = R2.exp2neg
ell_iv = R2.ell_iv
psi_prime_iv = R2.psi_prime_iv
psit_over_z_iv = R2.psit_over_z_iv
_adaptive = R2._adaptive

# fei_cert23 exports the derivative of Psit(v)=Psi(1-v).
from fei_cert23 import psit_prime_iv

EXPECTED_CANDIDATE_GIT_BLOB = R2.EXPECTED_CANDIDATE_GIT_BLOB
EXPECTED_CANDIDATE_BYTES = R2.EXPECTED_CANDIDATE_BYTES


def _build_k0prime_tables(cert):
    """Sparse range tables for K0'=G_num' - ln2*r*Psi'(r)."""
    if hasattr(cert, "_b12_k0p_min"):
        return
    T = Iv(cert.xs[:-1], cert.xs[1:])
    r = exp2neg(T)
    kp = Iv(cert.slopes) - LN2 * r * psi_prime_iv(r)
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
    cert._b12_k0p_min = mins
    cert._b12_k0p_max = maxs


def _k0prime_range(cert, a, b):
    """Safe range of K0' on [a,b] inside the finite candidate grid."""
    _build_k0prime_tables(cert)
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    if np.any(a < cert.xs[0]) or np.any(b > cert.K):
        raise ValueError("B12 K0' range is only implemented inside candidate grid")
    n = len(cert.slopes)
    i = np.clip(np.searchsorted(cert.xs, a, side="right") - 1, 0, n - 1)
    j = np.clip(np.searchsorted(cert.xs, b, side="left") - 1, 0, n - 1)
    j = np.maximum(i, j)
    ln = np.floor(np.log2(np.maximum(j-i+1, 1))).astype(int)
    lo = np.empty(len(i))
    hi = np.empty(len(i))
    for k in np.unique(ln):
        sel = ln == k
        h = 1 << int(k)
        left = i[sel]
        right = j[sel] - h + 1
        lo[sel] = np.minimum(cert._b12_k0p_min[k][left],
                             cert._b12_k0p_min[k][right])
        hi[sel] = np.maximum(cert._b12_k0p_max[k][left],
                             cert._b12_k0p_max[k][right])
    return Iv(lo, hi)


def _af0_joint_lower(cert, X, lam, ellv):
    """Lower bound for [K0(x)-K0(x+lambda)]/v by a joint MVT."""
    K0p = _k0prime_range(cert, X.lo, UP(X.hi + lam.hi))
    r = -(ellv / LN2) * K0p
    return r.lo, r.width()


def _q_point(cert, pstar, y):
    """Interval value of Q_{pstar}(y) at point-interval y."""
    v = exp2neg(y)
    return (cert.Gnum_range(y) / (1 - v)
            - 8 * (1 - pstar) * (1 - v) * ell_iv(v) / LN2
            + psit_over_z_iv(v))


def _qprime_range(cert, pstar, Y):
    """Exact-form interval enclosure of Q' on one y-node segment."""
    iy0, iy1 = R2._seg_pair(cert, Y.lo, Y.hi)
    if np.any(iy0 != iy1):
        raise ValueError("Q derivative cell crosses a candidate node")
    s = Iv(cert.slopes[iy0])
    v = exp2neg(Y)
    G = cert.Gnum_range(Y)
    bprime = s / (1 - v) - LN2 * v * G / (1 - v).sq()
    # d/dy [Psi(1-v)/v] = -ln2 [Psit'(v)-Psit(v)/v].
    gprime = -LN2 * (psit_prime_iv(v) - psit_over_z_iv(v))
    # d/dy[-8(1-p*)(1-v)ell(v)/ln2]
    # = 8(1-p*)[1-ell(v)], a cancellation-free form.
    dprime = 8 * (1 - pstar) * (1 - ell_iv(v))
    return bprime + gprime + dprime


def _q_block_lower(cert, X, Y):
    """Joint lower bound for B0+D+G on XxY, with D worst-case x endpoint exact."""
    # D is decreasing in x on fleet01's x-range, hence p*=2^-x_hi is worst.
    pstar = exp2neg(Iv(X.hi))
    v = exp2neg(Y)
    direct = (cert.Gnum_range(Y) / (1 - v)
              - 8 * (1 - pstar) * (1 - v) * ell_iv(v) / LN2
              + psit_over_z_iv(v))
    qp = _qprime_range(cert, pstar, Y)

    qlo = _q_point(cert, pstar, Iv(Y.lo))
    qhi = _q_point(cert, pstar, Iv(Y.hi))
    sign_pos = qp.lo >= 0
    sign_neg = qp.hi <= 0
    endpoint_lo = np.where(sign_pos, qlo.lo,
                           np.where(sign_neg, qhi.lo, -np.inf))

    yc = (Y.lo + Y.hi) / 2
    ry = UP(np.maximum(Y.hi - yc, yc - Y.lo))
    qc = _q_point(cert, pstar, Iv(yc))
    aqp = np.maximum(np.abs(qp.lo), np.abs(qp.hi))
    mv_lo = (qc - Iv(ry) * Iv(aqp)).lo
    lo = np.maximum.reduce([direct.lo, endpoint_lo, mv_lo])
    width_hint = np.minimum(direct.width(), 2 * ry * aqp)
    return lo, width_hint


def phi2_over_v_lower_twoblock(cert, X, Yp):
    """Strengthened B12 lower bound for Phi/v on x in [1,2]."""
    old_lo, old_wx, old_wy = R2.phi2_over_v_lower_secant(cert, X, Yp)

    p = exp2neg(X)
    v = exp2neg(Yp)
    ellv = ell_iv(v)
    lam = v * ellv / LN2

    af0_lo, af0_w = _af0_joint_lower(cert, X, lam, ellv)
    q_lo, q_w = _q_block_lower(cert, X, Yp)
    ce_lo, ce_w = R2._ce_lower_fleet01(X)

    # Exact total certificate-margin contribution from A+B is c(1-p).
    # It increases with x, so the cell minimum is at x_lo.
    p_at_xlo = exp2neg(Iv(X.lo))
    margin_lo = (Iv(cert.c) * (1 - p_at_xlo)).lo

    new_lo = af0_lo + q_lo + ce_lo + margin_lo
    lo = np.maximum(old_lo, new_lo)

    # Splitting widths affect efficiency only, never validity.
    margin_w = (Iv(cert.c) * (1 - p)).width()
    wx_new = 0.5 * af0_w + ce_w + margin_w
    wy_new = 0.5 * af0_w + q_w
    use_new = new_lo >= old_lo
    wx = np.where(use_new, wx_new, old_wx)
    wy = np.where(use_new, wy_new, old_wy)
    return lo, wx, wy


def verify_fleet01_shard(cert, y_index_lo, y_index_hi, max_depth=30):
    xs = cert.xs
    xi = np.where((xs[:-1] >= 1.0) &
                  (xs[1:] <= 2.0 + 8*np.finfo(float).eps))[0]
    ylo = max(0, int(y_index_lo))
    yhi = min(len(xs)-1, int(y_index_hi))
    if ylo >= yhi:
        raise ValueError("empty y shard")
    yi = np.arange(ylo, yhi)
    I, J = np.meshgrid(xi, yi, indexing="ij")
    I, J = I.ravel(), J.ravel()
    return _adaptive(
        lambda X,Y: phi2_over_v_lower_twoblock(cert, X, Y),
        xs[I], xs[I+1], xs[J], xs[J+1], max_depth,
        "region 2 B12 two-block x[1,2] yidx[%d,%d)" % (ylo,yhi))


if __name__ == "__main__":
    if len(sys.argv) < 5:
        raise SystemExit(
            "usage: python r2_two_block_enclosure.py CANDIDATE.npz C "
            "Y_INDEX_LO Y_INDEX_HI [MAX_DEPTH]")
    src = sys.argv[1]
    c = float(sys.argv[2])
    j0, j1 = int(sys.argv[3]), int(sys.argv[4])
    depth = int(sys.argv[5]) if len(sys.argv) > 5 else 30
    if abs(c - 0.003) > 1e-15:
        raise RuntimeError("this sprint driver is pinned to c=0.003")
    got = R2.verify_candidate_file(src)
    cert, C0 = R2.load_cert(src, c)
    print("candidate git_blob=%s bytes=%d C0=%.7f c=%g C_cert=%.7f" %
          (got, EXPECTED_CANDIDATE_BYTES, C0, c, cert.C_cert()), flush=True)
    ok = verify_fleet01_shard(cert, j0, j1, depth)
    print("B12 TWO-BLOCK SHARD %s" % ("VERIFIED" if ok else "NOT verified"), flush=True)
