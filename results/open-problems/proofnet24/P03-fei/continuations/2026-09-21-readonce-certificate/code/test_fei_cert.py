"""unit tests of the interval primitives in fei_cert.py against mpmath at 30 digits"""
import numpy as np, mpmath as mp, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fei_cert as Cc
mp.mp.dps = 90
def psi_mp(z):
    w = (1 - 2 * z) ** 2
    return (-w * mp.log(w, 2) / z) if w > 0 else mp.mpf(0)
def E_mp(p, q):
    L = lambda z: mp.log(1 / z, 2)
    return 8 * p * (1 - q) * L(p) + 8 * q * (1 - p) * L(q) + 8 * (1 - p) * (1 - q) + psi_mp(p * q) - psi_mp(p) - psi_mp(q)
rng = np.random.default_rng(0)
worst = 0; fails = 0; n = 0
for _ in range(3000):
    x = rng.uniform(1, 45); y = rng.uniform(1, 45); w = rng.uniform(0, 0.02)
    X = Cc.Iv(np.array([x]), np.array([x + w])); Y = Cc.Iv(np.array([y]), np.array([y + w]))
    e = Cc.E_iv(X, Y)
    for xx, yy in ((x, y), (x + w, y + w), (x + w / 2, y)):
        v = E_mp(mp.mpf(2) ** (-mp.mpf(xx)), mp.mpf(2) ** (-mp.mpf(yy)))
        n += 1
        if not (e.lo[0] <= v <= e.hi[0]): fails += 1
    worst = max(worst, float(e.hi[0] - e.lo[0]) / max(w, 1e-12))
print("E_iv contains the true value at %d sample points: fails = %d; max width per unit cell width = %.3g" % (n, fails, worst))
for z in (1e-12, 0.1, 0.25, 0.3, 0.5, 0.51, 0.75, 0.9, 1 - 1e-12):
    Z = Cc.Iv(np.array([z]), np.array([z * (1 + 1e-9) if z < 0.9 else z]))
    r = Cc.psi_iv(Z); v = psi_mp(mp.mpf(z))
    print("psi(%g): [%.12g, %.12g] contains %.12g: %s" % (z, r.lo[0], r.hi[0], v, r.lo[0] <= v <= r.hi[0]))
# degenerate-interval E at moderate points vs mpmath, width in ulps
for (p, q) in ((0.5, 0.5), (0.3, 0.7), (2.0 ** -20, 0.41), (2.0 ** -33, 2.0 ** -35), (0.9, 0.95)):
    X = Cc.Iv(np.array([np.log2(1 / p)])); Y = Cc.Iv(np.array([np.log2(1 / q)]))
    e = Cc.E_iv(X, Y)
    v = E_mp(mp.mpf(2) ** (-mp.mpf(np.log2(1 / p))), mp.mpf(2) ** (-mp.mpf(np.log2(1 / q))))
    print("E(%.3g, %.3g) = [%.15g, %.15g] true %.15g contained %s width %.2e" % (p, q, e.lo[0], e.hi[0], v, e.lo[0] <= v <= e.hi[0], e.hi[0] - e.lo[0]))
