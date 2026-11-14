"""Monte Carlo of the area of the typical cell of the Poisson-Voronoi tessellation of H^2 (curvature -1) at
intensity lam, by exact polygons in the Klein model.

By Slivnyak's theorem the typical cell is the cell of a nucleus added at o. Ordering the other nuclei by distance,
lam times the area of the ball B(o, a_i) is a rate-one Poisson process, so the nearest K nuclei are generated
directly: s_i = E_1 + ... + E_i, cosh a_i = 1 + s_i / (2 pi lam), uniform angles phi_i.

In the Klein model the bisector of o and a point at distance a in direction phi is the line k . e_phi = tanh(a/2),
so the cell is the Euclidean polygon {k : k . e_i <= h_i}, h_i = tanh(a_i / 2). Nuclei beyond the K-th cannot cut
it once every vertex has Klein norm below h_K. For an edge on the line (h, phi), the hyperbolic area of the sector
from o is the integral of cosh(rho) - 1 over the polar angle, with tanh(rho) = h / cos(psi), psi = theta - phi,
which integrates to F(psi) = arcsin(sin(psi) / sqrt(1 - h^2)) - psi."""
import math
import sys
import time
import numpy as np
from scipy.spatial import ConvexHull


def cell_area(lam, rng, K0=64):
    K = K0
    s = np.cumsum(rng.exponential(size=K))
    phi = rng.uniform(0, 2 * math.pi, size=K)
    while True:
        c = s / (2 * math.pi * lam)                   # cosh a - 1
        h = np.sqrt(c / (c + 2))                      # tanh(a/2)
        e = np.stack([np.cos(phi), np.sin(phi)], 1)
        hull = ConvexHull(e / h[:, None])             # polar dual: hull vertices = edges of the cell
        idx = hull.vertices                           # counterclockwise
        n1, h1 = e[idx], h[idx]
        n2, h2 = np.roll(n1, -1, 0), np.roll(h1, -1)
        det = n1[:, 0] * n2[:, 1] - n1[:, 1] * n2[:, 0]
        vx = (h1 * n2[:, 1] - h2 * n1[:, 1]) / det    # vertex between edge j and edge j+1
        vy = (n1[:, 0] * h2 - n2[:, 0] * h1) / det
        R = np.hypot(vx, vy).max()
        if R < h[-1] and R < 1:
            break
        extra = rng.exponential(size=K)
        s = np.concatenate([s, s[-1] + np.cumsum(extra)])
        phi = np.concatenate([phi, rng.uniform(0, 2 * math.pi, size=K)])
        K *= 2
    th_v = np.arctan2(vy, vx)                         # vertex j ends edge j and starts edge j+1
    th_start = np.roll(th_v, 1)
    ph = phi[idx]
    def F(psi, hh):
        x = np.sin(psi) / np.sqrt(1 - hh * hh)
        return np.arcsin(np.clip(x, -1, 1)) - psi
    wrap = lambda z: (z + math.pi) % (2 * math.pi) - math.pi
    a = F(wrap(th_v - ph), h1) - F(wrap(th_start - ph), h1)
    return float(a.sum()), len(idx), K


if __name__ == '__main__':
    lam = float(sys.argv[1]); n = int(sys.argv[2]); seed = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    rng = np.random.default_rng(seed)
    t0 = time.time()
    A = np.empty(n); E = np.empty(n)
    for i in range(n):
        A[i], E[i], _ = cell_area(lam, rng)
    m, v = A.mean(), A.var(ddof=1)
    # standard error of the variance from the fourth central moment
    m4 = ((A - m) ** 4).mean()
    se_v = math.sqrt(max(m4 - v * v, 0) / n)
    print(f'lam={lam:g} n={n} seed={seed}: mean area {m:.5f} (1/lam = {1 / lam:.5f}, se {A.std() / math.sqrt(n):.5f})  '
          f'lam*Var = {lam * v:.4f} +- {lam * se_v:.4f}  lam^2*Var = {lam * lam * v:.5f}  mean edges {E.mean():.1f} '
          f'(6 + 3/(pi lam) = {6 + 3 / (math.pi * lam):.1f})  {time.time() - t0:.0f}s', flush=True)
