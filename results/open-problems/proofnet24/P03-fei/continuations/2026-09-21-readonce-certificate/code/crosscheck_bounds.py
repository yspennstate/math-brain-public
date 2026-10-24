"""consistency test of the three region bounds: for random cells and random points inside them, the interval lower
bound must be <= the floating-point value of the same normalised quantity computed directly from the definitions
(Phi, Phi/v, Phi/u with the same Gamma_hat).  A transcription error in a region formula would show as a violation."""
import numpy as np, math, sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import fei_cert as Cc, fei_cert23 as C2, fei_cert_vi as V
from fei_cert import Iv
src = sys.argv[1] if len(sys.argv) > 1 else "cert_vi_h24k40.npz"; c = float(sys.argv[2]) if len(sys.argv) > 2 else 0.05
d = np.load(src); xs, G = d["xs"], d["G"]; K = float(xs[-1]); bstar = 8 - 4 / math.log(2); sig_t = (G[-1] - bstar) / K
cert = Cc.Cert(xs, G, c, tail_slope=sig_t); C2.build_slope_tables(cert)
def Ghat(x):
    x = np.asarray(x, float); inside = x <= K
    return np.where(inside, np.interp(np.minimum(x, K), xs, G), G[-1] + (x - K) * sig_t) + c * (1 - 2.0 ** -x)
def Gam(z):
    z = np.asarray(z, float); s = np.minimum(z, 1 - z); return s * Ghat(np.log2(1 / s))
def Phi(p, q):
    E = V.E_fun(p, q, np.log2(1 / p), np.log2(1 / q))
    return Gam(p) / p + Gam(q) / q - Gam(p * q) / (p * q) - E
rng = np.random.default_rng(5); n = 40000; viol = {}
# region 1: cells in x, y in [1, K]; points p = 2^-x, q = 2^-y
for name, fn, tr in (("R1", C2.phi1_lower, lambda x, y: Phi(2.0 ** -x, 2.0 ** -y)),
                     ("R2", C2.phi2_over_v_lower, lambda x, yp: Phi(2.0 ** -x, 1 - 2.0 ** -yp) / 2.0 ** -yp),
                     ("R3", C2.phi3_over_u_lower, lambda xp, yp: Phi(1 - 2.0 ** -xp, 1 - 2.0 ** -yp) / 2.0 ** -xp)):
    i = rng.integers(0, len(xs) - 1, n); j = rng.integers(0, len(xs) - 1, n)
    if name == "R3":
        keep = i >= j; i, j = i[keep], j[keep]
    # random sub-cells (random depth) inside node pieces
    fx = rng.uniform(0, 1, len(i)); fy = rng.uniform(0, 1, len(i)); wx = 2.0 ** -rng.integers(0, 6, len(i)); wy = 2.0 ** -rng.integers(0, 6, len(i))
    x0 = xs[i] + fx * (1 - wx) * (xs[i + 1] - xs[i]); x1 = x0 + wx * (xs[i + 1] - xs[i])
    y0 = xs[j] + fy * (1 - wy) * (xs[j + 1] - xs[j]); y1 = y0 + wy * (xs[j + 1] - xs[j])
    t0 = time.time(); lo = fn(cert, Iv(x0, x1), Iv(y0, y1)); lo = lo[0] if isinstance(lo, tuple) else lo
    bad = 0; worst = np.inf
    for _ in range(5):
        px = x0 + rng.uniform(0, 1, len(i)) * (x1 - x0); py = y0 + rng.uniform(0, 1, len(i)) * (y1 - y0)
        val = tr(px, py)
        gap = val - lo
        bad += int((gap < -1e-9).sum()); worst = min(worst, float(gap.min()))
    # also the cell corners
    for px, py in ((x0, y0), (x1, y0), (x0, y1), (x1, y1)):
        val = tr(px, py); gap = val - lo; bad += int((gap < -1e-9).sum()); worst = min(worst, float(gap.min()))
    print("%s: %d cells x 9 points: lower bound exceeded the true value %d times (most negative gap %.3e); %.1f s" % (name, len(i), bad, worst, time.time() - t0))
