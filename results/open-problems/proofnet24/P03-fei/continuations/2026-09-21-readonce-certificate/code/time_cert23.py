import numpy as np, math, sys, time, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import fei_cert as Cc, fei_cert23 as C2
from fei_cert import Iv
d = np.load("cert_vi_h24k40.npz"); xs, G = d["xs"], d["G"]; K = float(xs[-1]); bstar = 8 - 4 / math.log(2)
cert = Cc.Cert(xs, G, 0.05, tail_slope=(G[-1] - bstar) / K); C2.build_slope_tables(cert)
rng = np.random.default_rng(0); n = 20000
i = rng.integers(0, len(xs) - 1, n); j = rng.integers(0, len(xs) - 1, n); keep = i >= j; i, j = i[keep], j[keep]
X = Iv(xs[i], xs[i + 1]); Y = Iv(xs[j], xs[j + 1])
t0 = time.time(); lo, wx, wy = C2.phi3_over_u_lower(cert, X, Y); dt = time.time() - t0
print("phi3 on %d cells: %.2f s -> %.1f us/cell; failing %d, min %.3f; median wx %.3f wy %.3f" % (len(i), dt, 1e6 * dt / len(i), (lo < 0).sum(), lo.min(), np.median(wx), np.median(wy)))
t0 = time.time(); lo2, wx2, wy2 = C2.phi2_over_v_lower(cert, X, Y); dt2 = time.time() - t0
print("phi2 on %d cells: %.2f s -> %.1f us/cell; failing %d, min %.3f" % (len(i), dt2, 1e6 * dt2 / len(i), (lo2 < 0).sum(), lo2.min()))
t0 = time.time(); lo1, a, b = C2.phi1_lower(cert, X, Y); print("phi1: %.2f s; failing %d" % (time.time() - t0, (lo1 < 0).sum()))
