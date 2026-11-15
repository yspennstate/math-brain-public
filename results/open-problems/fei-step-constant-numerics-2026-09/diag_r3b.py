"""region 3: which term keeps the bulk cells (x', y' in [1.05, 2]) failing after directional splits?"""
import numpy as np, math, sys, time, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import fei_cert as Cc, fei_cert23 as C2
from fei_cert import Iv, exp2neg, ell_iv, LN2, UP, DN
d = np.load("cert_vi_h24k40.npz"); xs, G = d["xs"], d["G"]; K = float(xs[-1]); bstar = 8 - 4 / math.log(2)
cert = Cc.Cert(xs, G, 0.05, tail_slope=(G[-1] - bstar) / K); C2.build_slope_tables(cert)
sel = np.where((xs[:-1] >= 1.05) & (xs[:-1] < 2))[0]
I, J = np.meshgrid(sel, sel, indexing="ij"); I = I.ravel(); J = J.ravel(); keep = I >= J; I, J = I[keep], J[keep]
x0, x1, y0, y1 = xs[I], xs[I + 1], xs[J], xs[J + 1]
print("bulk cells:", len(x0))
def parts(x0, x1, y0, y1):
    Xp = Iv(x0, x1); Yp = Iv(y0, y1)
    u = exp2neg(Xp); v = exp2neg(Yp); ellu = ell_iv(u); ellv = ell_iv(v); w = u + v - u * v
    P1 = cert.Ghat_range(Xp) / (1 - u)
    wa = Iv(w.lo, np.minimum(w.hi, 0.5)); Zr = Iv(v.lo, wa.hi)
    A_mv = -(1 - v) * C2.Lambda_prime_range(cert, Zr); A_dir = (C2.Lambda_range(cert, v) - C2.Lambda_range(cert, wa)) / u
    Zw = Iv(v.lo, np.minimum(w.hi, 0.75)); T4_mv = (1 - v) * C2.psit_prime_iv(Zw); T4_dir = (C2.psit_iv(w) - C2.psit_iv(v)) / u
    T1 = 8 * (1 - u) * v * ellu / LN2; T2 = 8 * (1 - v) * v * ellv / LN2; T5 = C2.psit_over_z_iv(u)
    return dict(P1=P1.width(), P2a_mv=A_mv.width(), P2a_dir=A_dir.width(), T4_mv=T4_mv.width(), T4_dir=T4_dir.width(), T1=T1.width(), T2=T2.width(), T5=T5.width(),
                wlo=w.lo, whi=w.hi)
lo, wx, wy = C2.phi3_over_u_lower(cert, Iv(x0, x1), Iv(y0, y1))
bad = lo < 0; print("depth 0: failing %d of %d, min %.3f" % (bad.sum(), len(lo), lo.min()))
P = parts(x0[bad], x1[bad], y0[bad], y1[bad])
for k in ("P1", "P2a_mv", "P2a_dir", "T4_mv", "T4_dir", "T1", "T2", "T5"):
    print("  median width %-8s %.3f   (90th pct %.3f)" % (k, np.median(P[k]), np.percentile(P[k], 90)))
print("  fraction of failing cells with w straddling 1/2: %.3f, w entirely > 1/2: %.3f" % (((P["wlo"] < 0.5) & (P["whi"] > 0.5)).mean(), (P["wlo"] >= 0.5).mean()))
# follow the driver for 8 directional splits on the failing set (cap at 300k cells) and re-measure
bx0, bx1, by0, by1 = x0[bad], x1[bad], y0[bad], y1[bad]
for depth in range(8):
    lo, wx, wy = C2.phi3_over_u_lower(cert, Iv(bx0, bx1), Iv(by0, by1))
    b = lo < 0
    print("  split %d: %d cells, %d failing, min %.3f, x-splits %.2f" % (depth, len(bx0), b.sum(), lo.min(), (wx[b] >= wy[b]).mean() if b.any() else 0))
    if not b.any(): break
    bx0, bx1, by0, by1 = bx0[b], bx1[b], by0[b], by1[b]; sx = wx[b] >= wy[b]
    xm = (bx0 + bx1) / 2; ym = (by0 + by1) / 2
    nx0 = np.concatenate([bx0[sx], xm[sx], bx0[~sx], bx0[~sx]]); nx1 = np.concatenate([xm[sx], bx1[sx], bx1[~sx], bx1[~sx]])
    ny0 = np.concatenate([by0[sx], by0[sx], by0[~sx], ym[~sx]]); ny1 = np.concatenate([by1[sx], by1[sx], ym[~sx], by1[~sx]])
    bx0, bx1, by0, by1 = nx0, nx1, ny0, ny1
    if len(bx0) > 300000:
        idx = np.random.default_rng(0).choice(len(bx0), 300000, replace=False); bx0, bx1, by0, by1 = bx0[idx], bx1[idx], by0[idx], by1[idx]
lo, wx, wy = C2.phi3_over_u_lower(cert, Iv(bx0, bx1), Iv(by0, by1)); b = lo < 0
if b.any():
    P = parts(bx0[b], bx1[b], by0[b], by1[b])
    print("after splits, failing cells' median widths:")
    for k in ("P1", "P2a_mv", "P2a_dir", "T4_mv", "T4_dir", "T1", "T2", "T5"):
        print("  %-8s %.3f" % (k, np.median(P[k])))
    j = int(np.argmin(lo)); print("  worst: x'=[%.5f,%.5f] y'=[%.5f,%.5f] lo=%.3f" % (bx0[j], bx1[j], by0[j], by1[j], lo[j]))
