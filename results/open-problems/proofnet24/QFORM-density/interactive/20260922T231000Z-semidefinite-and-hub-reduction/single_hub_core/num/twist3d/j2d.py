# J_2(kappa) = int int |E exp(i(yL + tV + kappa L P))| dy dt for comb laws on the spread 3D Walsh frame.
# Exact for Gaussian cells: given L = l the twist is linear in the cell's P-part, so the complex density of (L, V) is
#   A(l, v) = exp(-sigma^2 kappa^2 l^2 / 2) sum_z p_z exp(i kappa l P_z) g_sigma(l - L_z) g_sigma(v - V_z).
# A is deposited on a grid of spacing sigma/3 (separable bumps), T = FFT2(A); the grid is padded 2x so that
# the Riemann sum of |T|^2 is exact and that of |T| is close.
import sys, math, time
import numpy as np
from jperp import triple_law, rot

def j2(N, R, kappas, pad=2.0, chunk=4000):
    z, p = triple_law(N)
    y = z @ R / math.sqrt(8.0)
    L, V, P = y[:, 0], y[:, 1], y[:, 2]
    s = 1.0 / (math.sqrt(12.0) * N); h = s / 3.0; W = 12
    l0 = L.min() - 5 * s; v0 = V.min() - 5 * s
    nl = int(pad * (L.max() - L.min() + 10 * s) / h) + 1; nv = int(pad * (V.max() - V.min() + 10 * s) / h) + 1
    nl += nl % 2; nv += nv % 2
    cl = np.rint((L - l0) / h).astype(np.int64); cv = np.rint((V - v0) / h).astype(np.int64)
    off = np.arange(-W, W + 1)
    gl = np.exp(-0.5 * ((l0 + (cl[:, None] + off[None, :]) * h - L[:, None]) / s) ** 2) / (math.sqrt(2 * math.pi) * s)
    gv = np.exp(-0.5 * ((v0 + (cv[:, None] + off[None, :]) * h - V[:, None]) / s) ** 2) / (math.sqrt(2 * math.pi) * s)
    lgrid = l0 + (cl[:, None] + off[None, :]) * h
    out = []
    for kappa in kappas:
        A = np.zeros(nl * nv, dtype=np.complex128)
        for c0 in range(0, len(p), chunk):
            sl = slice(c0, c0 + chunk)
            lv = p[sl, None] * np.exp(1j * kappa * lgrid[sl] * P[sl, None] - 0.5 * (s * kappa * lgrid[sl]) ** 2) * gl[sl]
            idx = ((cl[sl, None, None] + off[None, :, None]) * nv + (cv[sl, None, None] + off[None, None, :])).ravel()
            wts = (lv[:, :, None] * gv[sl, None, :]).ravel()
            A += np.bincount(idx, weights=wts.real, minlength=nl * nv) + 1j * np.bincount(idx, weights=wts.imag, minlength=nl * nv)
        T = np.fft.fft2(A.reshape(nl, nv)) * h * h
        dy = 2 * math.pi / (nl * h); dt = 2 * math.pi / (nv * h)
        out.append((kappa, float(np.abs(T).sum() * dy * dt), float((np.abs(T) ** 2).sum() * dy * dt), float(np.abs(T).max())))
        del A, T
    return len(p), (nl, nv), out

if __name__ == "__main__":
    N = int(sys.argv[1]); which = sys.argv[2]
    kappas = [float(x) for x in sys.argv[3].split(",")] if len(sys.argv) > 3 else [0.0, 0.25, 0.5, 1.0, 2.0]
    R = np.eye(3) if which == "rat" else rot([1, 2, 0], math.atan(math.sqrt(2))) @ rot([0, 1, 3], math.atan(math.sqrt(3)))
    t0 = time.time()
    npts, shape, out = j2(N, R, kappas)
    print("N=%d frame=%s points=%d grid=%s (%.0fs)" % (N, which, npts, shape, time.time() - t0))
    for kappa, j1, j2v, mx in out:
        print("  kappa=%5.2f  J2=%8.3f  int|T|^2=%8.4f  max|T|=%.3f" % (kappa, j1, j2v, mx))
    print("(4 pi)^2 = %.1f" % ((4 * math.pi) ** 2))
