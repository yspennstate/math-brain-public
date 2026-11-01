"""Hasebe and Ueda, ALEA 15 (2018), Conjecture 3.5: if mu and nu are symmetric unimodal measures on R,
is mu box+ nu unimodal?  They prove it when one of them is a semicircle law.

The classical analogue is a theorem of Wintner: a symmetric unimodal measure is, by Khinchin, a mixture
of uniform laws on symmetric intervals, ordinary convolution is linear in each argument, and the
convolution of two such uniforms is a trapezoid, which is symmetric unimodal.  Free convolution is NOT
linear in its arguments, so that argument does not transfer, and the uniform law is the natural test.

For the uniform law U on [-1,1], G_U(z) = arctanh(1/z), so K_U(w) = G_U^{-1}(w) = coth(w), and since
R = K - 1/w adds under free convolution,

    K_{U box+ U}(w) = 2 coth(w) - 1/w.

The density is recovered parametrically: on the support, w = G(x) has Im w < 0 and K(w) is real, so
sweeping w over the curve {Im K(w) = 0} gives x = K(w) and density -Im(w)/pi.  The measure is unimodal
exactly when x is monotone along that curve.
"""
import numpy as np
from scipy.optimize import brentq

def K(w):
    return 2 / np.tanh(w) - 1 / w

def imK(u, v):
    return K(complex(u, v)).imag

def branch(v, umax=60.0, n=20000):
    """all u > 0 with Im K(u+iv) = 0, for fixed v < 0"""
    us = np.linspace(1e-6, umax, n)
    f = np.array([imK(u, v) for u in us])
    out = []
    for i in range(len(us) - 1):
        if np.isfinite(f[i]) and np.isfinite(f[i + 1]) and f[i] * f[i + 1] < 0:
            try:
                out.append(brentq(lambda u: imK(u, v), us[i], us[i + 1], xtol=1e-13))
            except Exception:
                pass
    return out

if __name__ == '__main__':
    print("free convolution of two uniform laws on [-1,1], traced parametrically")
    print(f"{'|v|':>9} {'density':>10} {'x = Re K':>12} {'check Im K':>12}")
    pts = []
    for v in np.concatenate([np.linspace(0.02, 1.0, 25), np.linspace(1.1, 4.0, 20)]):
        sols = branch(-v)
        for u in sols:
            w = complex(u, -v)
            x = K(w).real
            pts.append((v / np.pi, x, u))
    pts.sort()
    for dens, x, u in pts[::3]:
        print(f"{dens*np.pi:>9.4f} {dens:>10.5f} {x:>12.6f} {imK(u, -dens*np.pi):>12.2e}")
    xs = np.array([p[1] for p in pts]); ds = np.array([p[0] for p in pts])
    print(f"\npoints found: {len(pts)}")
    print(f"largest density: {ds.max():.5f} at x = {xs[ds.argmax()]:.6f}")
    # unimodality: along increasing density, |x| must decrease monotonically
    order = np.argsort(ds)
    ax = np.abs(xs[order])
    drops = np.sum(np.diff(ax) > 1e-9)
    print(f"steps where |x| INCREASES as the density rises: {drops} of {len(ax)-1}")
    print("(for a symmetric unimodal density |x| must fall as the density rises; any increase is a dip)")
