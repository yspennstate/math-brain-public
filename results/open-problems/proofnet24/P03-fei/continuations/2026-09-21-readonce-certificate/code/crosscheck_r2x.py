"""40-digit cross-check of the region-2 bound with the exact A term (fei_cert_r1x.phi2_over_v_lower_exact).

Region 2 is p <= 1/2 < q, v = 1-q, and the bound is on Phi/v.  Three checks: (1) the bound never exceeds the true
value of Phi(p, 1-v)/v at corners, interior points and the diagonal vertices x + lam = node, all evaluated at 40
digits from the same certificate; (2) the D enclosure contains the true G_num(x) - G_num(x+lam) on a dense grid of
the (x, lam) rectangle; (3) a negative-margin control in which cells must fail and the bound must flag them.
usage: crosscheck_r2x.py <npz> <c> [n_cells]"""
import numpy as np, math, sys, os, time, mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fei_cert as Cc, fei_cert23 as C2, fei_cert_r1x as R
from fei_cert import Iv
mp.mp.dps = 40
src = sys.argv[1] if len(sys.argv) > 1 else "cert_vi_h96k40.npz"
c = float(sys.argv[2]) if len(sys.argv) > 2 else 0.003
n = int(sys.argv[3]) if len(sys.argv) > 3 else 400
cert, C0 = R.load_cert(src, c)
xs, G = cert.xs, cert.G; K = float(xs[-1])
XS = [mp.mpf(float(x)) for x in xs]; GS = [mp.mpf(float(g)) for g in G]; KM = mp.mpf(K); SIG = mp.mpf(float(cert.tail_slope))
CM = [mp.mpf(c)]

def Gnum_mp(x):
    if x >= KM: return GS[-1] + (x - KM) * SIG
    j = int(np.searchsorted(xs, float(x), side="right") - 1); j = max(0, min(j, len(xs) - 2))
    return GS[j] + (x - XS[j]) * (GS[j + 1] - GS[j]) / (XS[j + 1] - XS[j])
def Ghat_mp(x): return Gnum_mp(x) + CM[0] * (1 - mp.mpf(2) ** (-x))
def Gam_mp(z):
    s = min(z, 1 - z); return s * Ghat_mp(mp.log(1 / s, 2))
def psi_mp(z):
    w = (1 - 2 * z) ** 2; return -w * mp.log(w, 2) / z if w > 0 else mp.mpf(0)
def L(z): return mp.log(1 / z, 2)
def E_mp(p, q): return 8*p*(1-q)*L(p) + 8*q*(1-p)*L(q) + 8*(1-p)*(1-q) + psi_mp(p*q) - psi_mp(p) - psi_mp(q)
def Phi_mp(p, q): return Gam_mp(p)/p + Gam_mp(q)/q - Gam_mp(p*q)/(p*q) - E_mp(p, q)

def cells(rng, n):
    i = rng.integers(0, len(xs) - 1, n); j = rng.integers(0, len(xs) - 1, n)
    fx = rng.uniform(0, 1, n); fy = rng.uniform(0, 1, n)
    wx = 2.0 ** -rng.integers(0, 6, n); wy = 2.0 ** -rng.integers(0, 6, n)
    full = rng.uniform(0, 1, n) < 0.4
    wx = np.where(full, 1.0, wx); wy = np.where(full, 1.0, wy); fx = np.where(full, 0.0, fx); fy = np.where(full, 0.0, fy)
    x0 = xs[i] + fx*(1-wx)*(xs[i+1]-xs[i]); x1 = np.where(full, xs[i+1], x0 + wx*(xs[i+1]-xs[i]))
    y0 = xs[j] + fy*(1-wy)*(xs[j+1]-xs[j]); y1 = np.where(full, xs[j+1], y0 + wy*(xs[j+1]-xs[j]))
    return x0, x1, y0, y1

rng = np.random.default_rng(23)
x0, x1, y0, y1 = cells(rng, n)
X = Iv(x0, x1); Y = Iv(y0, y1)
t0 = time.time(); lo, wx, wy = R.phi2_over_v_lower_exact(cert, X, Y); t_new = time.time() - t0
old = C2.phi2_over_v_lower(cert, X, Y)[0]
print("region 2, %d cells in %.2f s; new - old lower bound: median %.3e, min %.3e, max %.3e"
      % (len(x0), t_new, np.median(lo - old), (lo - old).min(), (lo - old).max()))

def pts(k, rng):
    out = [(x0[k], y0[k]), (x0[k], y1[k]), (x1[k], y0[k]), (x1[k], y1[k])]
    for _ in range(3):
        out.append((x0[k] + rng.uniform(0, 1)*(x1[k]-x0[k]), y0[k] + rng.uniform(0, 1)*(y1[k]-y0[k])))
    return out

bad = 0; worst = (mp.inf, None); slack = []; checked = 0
for k in range(len(x0)):
    vals = []
    for (px, py) in pts(k, rng):
        p = mp.mpf(2) ** (-mp.mpf(px)); v = mp.mpf(2) ** (-mp.mpf(py))
        vals.append(Phi_mp(p, 1 - v) / v); checked += 1
    mn = min(vals); gap = mn - mp.mpf(float(lo[k])); slack.append(float(gap))
    if gap < -1e-9:
        bad += 1
        if gap < worst[0]: worst = (gap, k)
print("(1) %d points at 40 digits: bound above the true value %d times; slack median %.3e, min %.3e"
      % (checked, bad, np.median(slack), min(slack)))
if bad:
    k = worst[1]; print("   worst cell x=[%.9f,%.9f] y'=[%.9f,%.9f] bound %.9g gap %s" % (x0[k], x1[k], y0[k], y1[k], lo[k], mp.nstr(worst[0], 8)))

# (2) the D enclosure against a dense grid of the (x, lam) rectangle
from fei_cert import exp2neg, ell_iv, LN2
v = exp2neg(Y); lam = v * ell_iv(v) / LN2
D = R.D_enclose(cert, X.lo, X.hi, lam.lo, lam.hi)
bad2 = 0; loose = 0.0
for k in range(min(len(x0), 150)):
    gx = np.linspace(x0[k], x1[k], 25); gl = np.linspace(lam.lo[k], lam.hi[k], 25)
    GX, GL = np.meshgrid(gx, gl)
    d = cert.Gnum_pt(GX.ravel()).lo - cert.Gnum_pt((GX + GL).ravel()).hi
    dhi = cert.Gnum_pt(GX.ravel()).hi - cert.Gnum_pt((GX + GL).ravel()).lo
    if d.min() < D.lo[k] - 1e-9 or dhi.max() > D.hi[k] + 1e-9: bad2 += 1
    loose = max(loose, float(d.min() - D.lo[k]))
print("(2) D enclosure on %d cells against a 25x25 grid: %d violations; largest gap below the grid minimum %.3e"
      % (min(len(x0), 150), bad2, loose))

# (3) a way to fail
cneg = -0.2
cert_n, _ = R.load_cert(src, cneg); CM[0] = mp.mpf(cneg)
lo_n = R.phi2_over_v_lower_exact(cert_n, X, Y)[0]
neg_true = 0; neg_flag = 0; unsound = 0
for k in range(len(x0)):
    mn = min(Phi_mp(mp.mpf(2)**(-mp.mpf(px)), 1 - mp.mpf(2)**(-mp.mpf(py))) / (mp.mpf(2)**(-mp.mpf(py)))
             for (px, py) in pts(k, rng))
    if mn < 0: neg_true += 1
    if lo_n[k] < 0: neg_flag += 1
    if mn - mp.mpf(float(lo_n[k])) < -1e-9: unsound += 1
print("(3) c = %g: cells with a negative sampled Phi/v %d, flagged by the bound %d, bound above the truth %d times"
      % (cneg, neg_true, neg_flag, unsound))
ok = (bad == 0) and (bad2 == 0) and (unsound == 0) and (neg_true > 0) and (neg_flag >= neg_true)
print("CROSSCHECK", "PASS" if ok else "FAIL")
