"""Gval at n = 5 next to a double top eigenvalue (an agent, 11 Nov 2026).

1. Re-run the unconstrained local search from the two printed weightings (as canon_gap.py does) to recover the
   minimisers with a double top eigenvalue.
2. At the minimiser, scan Gval over all unit x in the top two-plane (lam = top eigenvalue).
3. For the worst x, add delta times a small graph H chosen so that x becomes the unique top eigenvector
   (H = the graph with weights max(0, -x_i x_j) scaled; its Laplacian has Rayleigh quotient largest near x), and
   report Gval and the gap for delta = 1e-6 .. 1e-2 with the unique numerical top eigenvector.
4. Search with a gap floor of 1e-5, 1e-4.
"""
import sys
import numpy as np
from scipy.optimize import minimize

sys.path.insert(0, "~/brain-repo/06_math_research/t104_alon_agent_2026_11_11")
sys.path.insert(0, "~/fillq_ctl/codex_audit/PSI")
from canon_spectral import build  # noqa: E402
from gval_n5_check_lib import n, pairs, from_text, lap, gval_x, gval  # noqa: E402

cases = [
    "12:0.0031 13:0.0259 14:0.2021 15:0.2067 23:0.2972 24:0.0078 34:0.0297 35:0.0235 45:0.2038",
    "12:0.2143 13:0.2116 14:0.0134 23:0.2115 24:0.0134 34:0.0172 35:0.0043 45:0.3142",
]
rng = np.random.default_rng(11)


def f(z):
    return gval(z * z)[0]


for s in cases:
    print("case:", s)
    w0 = from_text(s)
    best = None
    for trial in range(10):
        z0 = np.sqrt(np.abs(w0 + (0.0 if trial == 0 else 0.003) * rng.normal(0, 1, len(pairs))))
        res = minimize(f, z0, method="Nelder-Mead", options={"xatol": 1e-11, "fatol": 1e-15, "maxiter": 20000})
        res = minimize(f, res.x, method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-16, "maxiter": 20000})
        g, gap = gval(res.x ** 2)
        if best is None or g < best[0]:
            best = (g, gap, res.x ** 2 / (res.x ** 2).sum())
    g, gap, w = best
    print("  unconstrained minimiser: Gval %.6e, gap %.3e" % (g, gap))
    print("     weights " + " ".join("%d%d:%.8f" % (i + 1, j + 1, v) for (i, j), v in zip(pairs, w) if v > 1e-10))
    ev, U = np.linalg.eigh(lap(w))
    print("     spectrum " + " ".join("%.6f" % e for e in ev))
    u1, u2 = U[:, -1], U[:, -2]
    ts = np.linspace(0, np.pi, 721)
    vals = np.array([gval_x(w, np.cos(t) * u1 + np.sin(t) * u2) for t in ts])
    k = int(vals.argmin())
    print("  over the top two-plane: min %.6e, max %.6e, fraction of the circle with Gval < 0: %.3f"
          % (vals.min(), vals.max(), float((vals < 0).mean())))
    xw = np.cos(ts[k]) * u1 + np.sin(ts[k]) * u2
    # make xw the unique top vector: add delta * H, H a nonnegative graph whose Laplacian favours xw in the plane
    H = np.array([max(0.0, -xw[i] * xw[j]) for (i, j) in pairs])
    LH = lap(H)
    a = np.array([[u1 @ LH @ u1, u1 @ LH @ u2], [u2 @ LH @ u1, u2 @ LH @ u2]])
    e2, V2 = np.linalg.eigh(a)
    xt = V2[0, -1] * u1 + V2[1, -1] * u2
    print("  H restricted to the plane picks a top vector with |cos| to the worst x: %.4f" % abs(xt @ xw))
    for delta in (1e-6, 1e-5, 1e-4, 1e-3, 1e-2):
        g, gap = gval(w + delta * H)
        print("     w + %.0e H: Gval %.6e, gap %.3e" % (delta, g, gap))
    for gmin in (1e-5, 1e-4, 3e-4):
        def fp(z):
            g, gap = gval(z * z)
            return g + 200.0 * max(0.0, gmin - gap) ** 2 / gmin
        bestc = None
        for trial in range(16):
            z0 = np.sqrt(np.abs(w + 0.002 * rng.normal(0, 1, len(pairs))))
            res = minimize(fp, z0, method="Nelder-Mead", options={"xatol": 1e-11, "fatol": 1e-15, "maxiter": 12000})
            g, gap = gval(res.x ** 2)
            if gap >= 0.9 * gmin and (bestc is None or g < bestc[0]):
                bestc = (g, gap)
        if bestc:
            print("  gap floor %.0e: smallest Gval %.6e at gap %.4e" % (gmin, bestc[0], bestc[1]))
