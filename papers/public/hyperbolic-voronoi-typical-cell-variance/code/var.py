"""Variance of the typical cell area of the Poisson-Voronoi tessellation of H^2 (Question 7.7 of D'Achille, Curien,
Enriquez, Lyons, Unel, Ideal Poisson-Voronoi tessellations on hyperbolic spaces, arXiv 2303.16831). Poisson nuclei of intensity lam in H^2 (curvature -1), V = area of the typical
cell, V0 = area of the zero cell. E V = 1/lam and E V0 = E V^2 / E V, so lam Var(V) = E V0 - 1/lam, and
    E V0 = int_{H^2} P(o and x have the same nearest nucleus) dx,
    P(o ~ x) = lam int_{H^2} exp(-lam |B(o, |y|) u B(x, d(x, y))|) dy,
    1/lam    = int_{H^2} exp(-lam |B(x, |x|)|) dx.
Change variables to areas: t = lam 2 pi (cosh r - 1) for |x| = r, s = lam 2 pi (cosh a - 1) for |y| = a. Then
    lam^2 Var(V) = int_0^inf (p(t) - e^{-t}) dt,   p = (1/pi) int_0^inf ds int_0^pi dth exp(-lam U),
with U = A(a) + A(b) - lens(a, b, r), A(u) = 2 pi (cosh u - 1), b = d(x, y) from the law of cosines, and the lens
(the intersection of the two disks, whose circles meet at y) = 2 al cosh a + 2 be cosh b + 2 ga - 2 pi, where al, be, ga
are the angles of the triangle o x y at o, x, y (Gauss-Bonnet). Positive control: as lam -> inf the tessellation is
locally Euclidean and lam^2 Var -> 0.2802 (variance of the typical planar Poisson-Voronoi cell area at unit intensity)."""
import math, sys, time
import numpy as np

def gl_pieces(cuts, n):
    xs, ws = [], []
    g, w = np.polynomial.legendre.leggauss(n)
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        xs.append((lo + hi) / 2 + (hi - lo) / 2 * g); ws.append((hi - lo) / 2 * w)
    return np.concatenate(xs), np.concatenate(ws)

def acosh1(z):                      # u with cosh u = 1 + z, accurate for small z
    return np.log1p(z + np.sqrt(z * (z + 2)))

def geometry(a, r, th):
    """cosh b - 1 and the lens area for the triangle o x y with |x| = r, |y| = a and angle th at o.
    cosh b - 1 = 2 sinh^2((a - r)/2) + 2 sinh a sinh r sin^2(th/2), a sum of nonnegative terms, and the angles at x and y
    come from tan(angle at x) = sinh a sin th / (sinh(r - a) + 2 cosh r sinh a sin^2(th/2)) and the same with a and r
    exchanged, evaluated with atan2; the angle at o is th itself. No step subtracts nearly equal numbers."""
    sa, ca, sr, cr = np.sinh(a), np.cosh(a), np.sinh(r), np.cosh(r)
    h = np.sin(th / 2) ** 2
    cbm1 = 2 * np.sinh((a - r) / 2) ** 2 + 2 * sa * sr * h
    be = np.arctan2(sa * np.sin(th), np.sinh(r - a) + 2 * sa * cr * h)
    ga = np.arctan2(sr * np.sin(th), np.sinh(a - r) + 2 * ca * sr * h)
    lens = 2 * th * ca + 2 * be * (1 + cbm1) + 2 * ga - 2 * math.pi
    return cbm1, lens

def p_of(t, lam, S, TH):
    """P(o ~ x) for x at area-distance t."""
    r = acosh1(t / (2 * math.pi * lam))
    s, ws = S; th, wth = TH
    a = acosh1(s / (2 * math.pi * lam))[:, None]
    cbm1, L = geometry(a, r, th[None, :])
    sb_area = lam * 2 * math.pi * cbm1
    U = s[:, None] + sb_area - lam * L
    return float((ws[:, None] * wth[None, :] * np.exp(-U)).sum() / math.pi)

def lam2var(lam, n_out=40, n_in=40, n_th=60):
    cutsT = [0, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64]
    T = gl_pieces(cutsT, n_out); S = gl_pieces(cutsT, n_in)
    TH = gl_pieces([0, 0.02, 0.1, 0.3, 0.8, 1.6, math.pi], n_th)
    p = np.array([p_of(t, lam, S, TH) for t in T[0]])
    return float((T[1] * (p - np.exp(-T[0]))).sum()), p, T

if __name__ == '__main__':
    lams = [float(x) for x in sys.argv[1:]] or [100.0, 10.0, 1.0, 0.1, 0.01, 1e-3, 1e-4]
    for lam in lams:
        t0 = time.time()
        v1, p, T = lam2var(lam)
        v2, _, _ = lam2var(lam, 60, 60, 90)
        print(f'lam={lam:<8g} lam^2 Var={v1:.10f} (finer {v2:.10f}, diff {v2 - v1:+.1e})  lam*Var={v2 / lam:.8f}  '
              f'p(0+)={p[0]:.6f}  ({time.time() - t0:.0f}s)', flush=True)
