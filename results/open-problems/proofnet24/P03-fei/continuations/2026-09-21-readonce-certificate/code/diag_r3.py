"""decompose the worst region-3 cells at depth 0 and after a few halvings"""
import numpy as np, math, sys, time, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import fei_cert as Cc, fei_cert23 as C2
from fei_cert import Iv, exp2neg, ell_iv, LN2, UP, DN
d = np.load("cert_vi_h24k40.npz"); xs, G = d["xs"], d["G"]; K = float(xs[-1]); bstar = 8 - 4 / math.log(2)
cert = Cc.Cert(xs, G, 0.05, tail_slope=(G[-1] - bstar) / K); C2.build_slope_tables(cert)
xn = np.concatenate([xs, K + np.arange(1, 21)])
nx, ny = len(xn) - 1, len(xs) - 1
I, J = np.meshgrid(np.arange(nx), np.arange(ny), indexing="ij"); I = I.ravel(); J = J.ravel(); keep = I >= J; I, J = I[keep], J[keep]
x0, x1, y0, y1 = xn[I], xn[I + 1], xs[J], xs[J + 1]
t0 = time.time(); lo = np.empty(len(x0)); wx = np.empty(len(x0)); wy = np.empty(len(x0))
for s in range(0, len(x0), 500000):
    e = min(len(x0), s + 500000); lo[s:e], wx[s:e], wy[s:e] = C2.phi3_over_u_lower(cert, Iv(x0[s:e], x1[s:e]), Iv(y0[s:e], y1[s:e]))
print("depth 0: %d cells, %d failing, min %.3f (%.0f s)" % (len(x0), (lo < 0).sum(), lo.min(), time.time() - t0))
bad = lo < 0
print("failing by x' range: x'<1.05: %d, 1.05-2: %d, 2-5: %d, 5-40: %d, >40: %d" % ((bad & (x0 < 1.05)).sum(), (bad & (x0 >= 1.05) & (x0 < 2)).sum(), (bad & (x0 >= 2) & (x0 < 5)).sum(), (bad & (x0 >= 5) & (x0 < 40)).sum(), (bad & (x0 >= 40)).sum()))
print("failing by y' range: y'<1.05: %d, 1.05-2: %d, 2-5: %d, 5-40: %d" % ((bad & (y0 < 1.05)).sum(), (bad & (y0 >= 1.05) & (y0 < 2)).sum(), (bad & (y0 >= 2) & (y0 < 5)).sum(), (bad & (y0 >= 5)).sum()))
print("failing on the diagonal (I==J): %d of %d diagonal cells" % ((bad & (I == J)).sum(), (I == J).sum()))

def decompose(a0, a1, b0, b1):
    Xp = Iv(np.array([a0]), np.array([a1])); Yp = Iv(np.array([b0]), np.array([b1]))
    u = exp2neg(Xp); v = exp2neg(Yp); ellu = ell_iv(u); ellv = ell_iv(v); w = u + v - u * v
    P1 = cert.Ghat_range(Xp) / (1 - u)
    out = "  cell x'=[%.5f,%.5f] y'=[%.5f,%.5f] u=[%.3g,%.3g] v=[%.3g,%.3g] w=[%.4f,%.4f]: P1=[%.2f,%.2f]" % (a0, a1, b0, b1, u.lo[0], u.hi[0], v.lo[0], v.hi[0], w.lo[0], w.hi[0], P1.lo[0], P1.hi[0])
    if w.lo[0] <= 0.5:
        wa = Iv(w.lo, np.minimum(w.hi, 0.5)); Zr = Iv(v.lo, wa.hi)
        P2_mv = -(1 - v) * C2.Lambda_prime_range(cert, Zr); P2_dir = (C2.Lambda_range(cert, v) - C2.Lambda_range(cert, wa)) / u
        out += " P2a_mv=[%.2f,%.2f] P2a_dir=[%.2f,%.2f]" % (P2_mv.lo[0], P2_mv.hi[0], P2_dir.lo[0], P2_dir.hi[0])
    if w.hi[0] >= 0.5:
        mlo = DN(-np.expm1((1 - Yp.lo) * np.log(2.0))); mhi = UP(-np.expm1((1 - Yp.hi) * np.log(2.0)))
        m = Iv(np.maximum(mlo, 0.0), np.maximum(mhi, 0.0)); l1pm = Iv(DN(np.log1p(m.lo)), UP(np.log1p(m.hi)))
        Lpq_m1 = (u * ell_iv(u) - l1pm) / LN2; Lpq_m1 = Iv(np.maximum(Lpq_m1.lo, 0.0), np.maximum(Lpq_m1.hi, 0.0))
        Z1 = Iv(v.lo, np.full_like(v.lo, 0.5)); lam1 = C2.Lambda_prime_range(cert, Z1); X1 = Iv(np.ones_like(u.lo), UP(1 + Lpq_m1.hi)); gp1 = C2.Ghat_prime_range(cert, X1)
        P2_mv = -((m / 2) / u) * lam1 - (Lpq_m1 / u) * gp1; P2_dir = (C2.Lambda_range(cert, v) - cert.Ghat_range(1 + Lpq_m1)) / u
        out += " P2b_mv=[%.2f,%.2f] P2b_dir=[%.2f,%.2f]" % (P2_mv.lo[0], P2_mv.hi[0], P2_dir.lo[0], P2_dir.hi[0])
    T1 = 8 * (1 - u) * v * ellu / LN2; T2 = 8 * (1 - v) * v * ellv / LN2; T3 = 8 * v
    Zw = Iv(v.lo, np.minimum(w.hi, 0.75)); T4_mv = (1 - v) * C2.psit_prime_iv(Zw); T4_dir = (C2.psit_iv(w) - C2.psit_iv(v)) / u; T5 = C2.psit_over_z_iv(u)
    out += " T1=[%.2f,%.2f] T2=[%.2f,%.2f] T3=[%.2f,%.2f] T4mv=[%.2f,%.2f] T4dir=[%.2f,%.2f] T5=[%.2f,%.2f]" % (T1.lo[0], T1.hi[0], T2.lo[0], T2.hi[0], T3.lo[0], T3.hi[0], T4_mv.lo[0], T4_mv.hi[0], T4_dir.lo[0], T4_dir.hi[0], T5.lo[0], T5.hi[0])
    return out

order = np.argsort(lo)[:4]
for j in order:
    print("lo=%.3f wx=%.3f wy=%.3f" % (lo[j], wx[j], wy[j])); print(decompose(x0[j], x1[j], y0[j], y1[j]))
# refine the worst cell 8 times along the wider attributed axis and watch the bound
a0, a1, b0, b1 = x0[order[0]], x1[order[0]], y0[order[0]], y1[order[0]]
for k in range(10):
    cand = [(a0, (a0 + a1) / 2, b0, b1), ((a0 + a1) / 2, a1, b0, b1), (a0, a1, b0, (b0 + b1) / 2), (a0, a1, (b0 + b1) / 2, b1)]
    res = [C2.phi3_over_u_lower(cert, Iv(np.array([c[0]]), np.array([c[1]])), Iv(np.array([c[2]]), np.array([c[3]]))) for c in cand]
    los = [float(r[0][0]) for r in res]
    print("  split %d: x-children %.3f %.3f | y-children %.3f %.3f" % (k, los[0], los[1], los[2], los[3]))
    jbest = int(np.argmin(los)); a0, a1, b0, b1 = cand[jbest]
print(decompose(a0, a1, b0, b1))
