"""Cross-check of the region-1 exact enclosure (fei_cert_r1x.phi1_lower_exact) against 40-digit arithmetic.

Three checks.  (1) Soundness: on random cells inside one segment each (node cells and narrower ones) the bound never
exceeds Phi at the cell's corners, at three interior points, and at every vertex where a line x+y = node meets an
edge, all evaluated with mpmath at 40 digits from the same certificate.  (2) The piecewise-linear part: P_min_exact
is at most the minimum of P over a dense grid of the cell (plus the diagonal vertices) and within 1e-9 of it.
(3) A way to fail: with a negative margin c there are cells whose sampled Phi is negative, and the bound is below
those values as well.  Also reports how much tighter the new bound is than the decoupled one on the same cells.
usage: crosscheck_r1x.py <npz> <c> [n_cells]
"""
import numpy as np, math, sys, os, time, mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fei_cert as Cc, fei_cert23 as C2, fei_cert_r1x as R
from fei_cert import Iv
mp.mp.dps = 40
src = sys.argv[1] if len(sys.argv) > 1 else "cert_vi_h24k40.npz"; c = float(sys.argv[2]) if len(sys.argv) > 2 else 0.01
n = int(sys.argv[3]) if len(sys.argv) > 3 else 600
cert, C0 = R.load_cert(src, c)
xs, G = cert.xs, cert.G; K = float(xs[-1])
XS = [mp.mpf(float(x)) for x in xs]; GS = [mp.mpf(float(g)) for g in G]; KM = mp.mpf(K); SIG = mp.mpf(float(cert.tail_slope)); CM = mp.mpf(c)


def Gnum_mp(x):
    if x >= KM:
        return GS[-1] + (x - KM) * SIG
    j = int(np.searchsorted(xs, float(x), side="right") - 1); j = max(0, min(j, len(xs) - 2))
    return GS[j] + (x - XS[j]) * (GS[j + 1] - GS[j]) / (XS[j + 1] - XS[j])


def Ghat_mp(x): return Gnum_mp(x) + CM * (1 - mp.mpf(2) ** (-x))
def psi_mp(z):
    w = (1 - 2 * z) ** 2; return -w * mp.log(w, 2) / z if w > 0 else mp.mpf(0)
def L(z): return mp.log(1 / z, 2)
def E_mp(p, q): return 8 * p * (1 - q) * L(p) + 8 * q * (1 - p) * L(q) + 8 * (1 - p) * (1 - q) + psi_mp(p * q) - psi_mp(p) - psi_mp(q)
def Phi_xy(x, y):
    x = mp.mpf(x); y = mp.mpf(y); p = mp.mpf(2) ** (-x); q = mp.mpf(2) ** (-y)
    return Ghat_mp(x) + Ghat_mp(y) - Ghat_mp(x + y) - E_mp(p, q)
def P_xy(x, y):
    x = mp.mpf(x); y = mp.mpf(y); return Gnum_mp(x) + Gnum_mp(y) - Gnum_mp(x + y)


def cells(rng, n):
    i = rng.integers(0, len(xs) - 1, n); j = rng.integers(0, len(xs) - 1, n)
    keep = i <= j; i, j = i[keep], j[keep]
    fx = rng.uniform(0, 1, len(i)); fy = rng.uniform(0, 1, len(i)); wx = 2.0 ** -rng.integers(0, 6, len(i)); wy = 2.0 ** -rng.integers(0, 6, len(i))
    full = rng.uniform(0, 1, len(i)) < 0.4                   # two fifths are whole node cells
    wx = np.where(full, 1.0, wx); wy = np.where(full, 1.0, wy); fx = np.where(full, 0.0, fx); fy = np.where(full, 0.0, fy)
    x0 = xs[i] + fx * (1 - wx) * (xs[i + 1] - xs[i]); x1 = np.where(full, xs[i + 1], x0 + wx * (xs[i + 1] - xs[i]))
    y0 = xs[j] + fy * (1 - wy) * (xs[j + 1] - xs[j]); y1 = np.where(full, xs[j + 1], y0 + wy * (xs[j + 1] - xs[j]))
    return x0, x1, y0, y1


def sample_points(x0, x1, y0, y1, rng):
    pts = [(x0, y0), (x0, y1), (x1, y0), (x1, y1)]
    for _ in range(3):
        pts.append((x0 + rng.uniform(0, 1) * (x1 - x0), y0 + rng.uniform(0, 1) * (y1 - y0)))
    lo_s = x0 + y0; hi_s = x1 + y1
    for s in xs[(xs > lo_s) & (xs < hi_s)]:                  # diagonal vertices, in float (the mp value is exact there)
        for (px, py) in ((x0, s - x0), (x1, s - x1), (s - y0, y0), (s - y1, y1)):
            if x0 - 1e-12 <= px <= x1 + 1e-12 and y0 - 1e-12 <= py <= y1 + 1e-12:
                pts.append((min(max(px, x0), x1), min(max(py, y0), y1)))
    return pts


rng = np.random.default_rng(11)
x0, x1, y0, y1 = cells(rng, n)
X = Iv(x0, x1); Y = Iv(y0, y1)
t0 = time.time()
lo, wx, wy = R.phi1_lower_exact(cert, X, Y)
old = C2.phi1_lower(cert, X, Y)[0]
print("bound on %d cells in %.2f s; new - old lower bound: median %.3e, min %.3e, max %.3e" % (len(x0), time.time() - t0, np.median(lo - old), (lo - old).min(), (lo - old).max()))
# (1) soundness against 40-digit Phi
bad = 0; worst = (mp.inf, None); checked = 0; slack = []
for k in range(len(x0)):
    vals = [Phi_xy(px, py) for (px, py) in sample_points(x0[k], x1[k], y0[k], y1[k], rng)]
    mn = min(vals); checked += len(vals)
    gap = mn - mp.mpf(float(lo[k])); slack.append(float(gap))
    if gap < -1e-9:
        bad += 1
        if gap < worst[0]: worst = (gap, k)
print("(1) %d cells, %d points at 40 digits: bound above the true value %d times; slack (sampled min - bound): median %.3e, max %.3e, min %.3e" % (len(x0), checked, bad, np.median(slack), max(slack), min(slack)))
if bad:
    k = worst[1]; print("   worst cell x=[%.9f,%.9f] y=[%.9f,%.9f] bound %.9g gap %s" % (x0[k], x1[k], y0[k], y1[k], lo[k], mp.nstr(worst[0], 8)))
# widths for reference: the decoupled bound's slack on the same cells
slack_old = [float(min(Phi_xy(px, py) for (px, py) in sample_points(x0[k], x1[k], y0[k], y1[k], np.random.default_rng(k))) - mp.mpf(float(old[k]))) for k in range(min(len(x0), 150))]
print("    decoupled bound's slack on the first %d cells: median %.3e, max %.3e" % (len(slack_old), np.median(slack_old), max(slack_old)))
# (2) the piecewise-linear part against a dense grid
Pm = R.P_min_exact(cert, x0, x1, y0, y1)
bad2 = 0; loose = 0.0
for k in range(min(len(x0), 200)):
    gx = np.linspace(x0[k], x1[k], 41); gy = np.linspace(y0[k], y1[k], 41)
    GX, GY = np.meshgrid(gx, gy); pts = list(zip(GX.ravel(), GY.ravel()))
    lo_s = x0[k] + y0[k]; hi_s = x1[k] + y1[k]
    for s in xs[(xs > lo_s) & (xs < hi_s)]:
        for (px, py) in ((x0[k], s - x0[k]), (x1[k], s - x1[k]), (s - y0[k], y0[k]), (s - y1[k], y1[k])):
            if x0[k] <= px <= x1[k] and y0[k] <= py <= y1[k]: pts.append((px, py))
    mn = min(P_xy(px, py) for (px, py) in pts)
    d = float(mn - mp.mpf(float(Pm[k])))
    if d < -1e-9: bad2 += 1
    loose = max(loose, d)
print("(2) P_min_exact on %d cells: below the dense-grid minimum %d times violated; largest excess of the grid minimum over the bound %.3e" % (min(len(x0), 200), bad2, loose))
# (3) a way to fail: negative margin
cneg = -0.2
cert_n, _ = R.load_cert(src, cneg)
lo_n = R.phi1_lower_exact(cert_n, X, Y)[0]
CM = mp.mpf(cneg); neg_true = 0; neg_flag = 0; unsound = 0
for k in range(len(x0)):
    vals = [Phi_xy(px, py) for (px, py) in sample_points(x0[k], x1[k], y0[k], y1[k], rng)]
    mn = min(vals)
    if mn < 0: neg_true += 1
    if lo_n[k] < 0: neg_flag += 1
    if mn - mp.mpf(float(lo_n[k])) < -1e-9: unsound += 1
print("(3) c = %g: cells with a negative sampled Phi %d, cells the bound flags %d, bound above the truth %d times" % (cneg, neg_true, neg_flag, unsound))
ok = (bad == 0) and (bad2 == 0) and (unsound == 0) and (neg_true > 0) and (neg_flag >= neg_true)
print("CROSSCHECK", "PASS" if ok else "FAIL")
