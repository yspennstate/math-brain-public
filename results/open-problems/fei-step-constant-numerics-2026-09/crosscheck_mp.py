"""cross-check of the region-2 and region-3 interval lower bounds against the same normalised quantity evaluated in
40-digit arithmetic (the float64 direct value loses everything when Phi is divided by a tiny v or u)"""
import numpy as np, math, sys, os, time, mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import fei_cert as Cc, fei_cert23 as C2
from fei_cert import Iv
mp.mp.dps = 40
src = sys.argv[1] if len(sys.argv) > 1 else "cert_vi_h24k40.npz"; c = float(sys.argv[2]) if len(sys.argv) > 2 else 0.05
d = np.load(src); xs, G = d["xs"], d["G"]; K = float(xs[-1]); bstar = 8 - 4 / math.log(2); sig_t = (G[-1] - bstar) / K
cert = Cc.Cert(xs, G, c, tail_slope=sig_t); C2.build_slope_tables(cert)
XS = [mp.mpf(float(x)) for x in xs]; GS = [mp.mpf(float(g)) for g in G]; KM = mp.mpf(K); SIG = mp.mpf(float(sig_t)); CM = mp.mpf(c)
def Ghat_mp(x):
    if x >= KM: g = GS[-1] + (x - KM) * SIG
    else:
        j = int(np.searchsorted(xs, float(x), side="right") - 1); j = max(0, min(j, len(xs) - 2))
        g = GS[j] + (x - XS[j]) * (GS[j + 1] - GS[j]) / (XS[j + 1] - XS[j])
    return g + CM * (1 - mp.mpf(2) ** (-x))
def Gam_mp(z):
    s = min(z, 1 - z); return s * Ghat_mp(mp.log(1 / s, 2))
def psi_mp(z):
    w = (1 - 2 * z) ** 2; return -w * mp.log(w, 2) / z if w > 0 else mp.mpf(0)
def L(z): return mp.log(1 / z, 2)
def E_mp(p, q): return 8 * p * (1 - q) * L(p) + 8 * q * (1 - p) * L(q) + 8 * (1 - p) * (1 - q) + psi_mp(p * q) - psi_mp(p) - psi_mp(q)
def Phi_mp(p, q): return Gam_mp(p) / p + Gam_mp(q) / q - Gam_mp(p * q) / (p * q) - E_mp(p, q)
rng = np.random.default_rng(9); n = 1500
for name, fn in (("R2", C2.phi2_over_v_lower), ("R3", C2.phi3_over_u_lower)):
    i = rng.integers(0, len(xs) - 1, n); j = rng.integers(0, len(xs) - 1, n)
    if name == "R3":
        keep = i >= j; i, j = i[keep], j[keep]
    fx = rng.uniform(0, 1, len(i)); fy = rng.uniform(0, 1, len(i)); wx = 2.0 ** -rng.integers(0, 6, len(i)); wy = 2.0 ** -rng.integers(0, 6, len(i))
    x0 = xs[i] + fx * (1 - wx) * (xs[i + 1] - xs[i]); x1 = x0 + wx * (xs[i + 1] - xs[i])
    y0 = xs[j] + fy * (1 - wy) * (xs[j + 1] - xs[j]); y1 = y0 + wy * (xs[j + 1] - xs[j])
    lo = fn(cert, Iv(x0, x1), Iv(y0, y1))[0]
    t0 = time.time(); bad = 0; worst = (mp.inf, None); checked = 0
    for k in range(len(i)):
        for (px, py) in ((x0[k], y0[k]), (x1[k], y1[k]), (x0[k] + 0.37 * (x1[k] - x0[k]), y0[k] + 0.61 * (y1[k] - y0[k]))):
            X = mp.mpf(float(px)); Y = mp.mpf(float(py))
            if name == "R2":
                p = mp.mpf(2) ** (-X); v = mp.mpf(2) ** (-Y); val = Phi_mp(p, 1 - v) / v
            else:
                u = mp.mpf(2) ** (-X); v = mp.mpf(2) ** (-Y); val = Phi_mp(1 - u, 1 - v) / u
            gap = val - mp.mpf(float(lo[k])); checked += 1
            if gap < -1e-9:
                bad += 1
                if gap < worst[0]: worst = (gap, (float(x0[k]), float(x1[k]), float(y0[k]), float(y1[k]), float(lo[k]), val))
    print("%s: %d cells, %d points in 40-digit arithmetic: bound exceeded the true value %d times; %.0f s" % (name, len(i), checked, bad, time.time() - t0))
    if bad: print("   worst: cell x=[%.6f,%.6f] y=[%.6f,%.6f] bound %.6g true %s gap %s" % (worst[1][0], worst[1][1], worst[1][2], worst[1][3], worst[1][4], mp.nstr(worst[1][5], 8), mp.nstr(worst[0], 5)))
