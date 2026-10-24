# Mixed norms int dt ||T(., t)||_{L^p(dy)}, T(y, t) = E exp(i(yL + tV + kappa L P)); p = 1 is J_2(kappa) = int int |E exp(i(yL + tV + kappa L P))| dy dt for comb laws on the spread 3D Walsh frame.
# Exact for Gaussian cells: given L = l the twist is linear in the cell's P-part, so the complex density of (L, V) is
#   A(l, v) = exp(-sigma^2 kappa^2 l^2 / 2) sum_z p_z exp(i kappa l P_z) g_sigma(l - L_z) g_sigma(v - V_z).
# A is deposited on a grid of spacing sigma/3 (separable bumps), T = FFT2(A); the grid is padded 2x so that
# the Riemann sum of |T|^2 is exact and that of |T| is close.
import sys, math, time
import numpy as np
from jperp import triple_law, rot

PS = (1.0, 1.25, 1.5, 1.75, 2.0)
def j2(N, R, kappas, pad=2.0, chunk=4000, hshift=0.0, fine=False):
    z, p = triple_law(N)
    y = z @ R / math.sqrt(8.0) * (2.0 / N if fine else 1.0)
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
            tw = kappa * lgrid[sl] + hshift
            lv = p[sl, None] * np.exp(1j * tw * P[sl, None] - 0.5 * (s * tw) ** 2) * gl[sl]
            idx = ((cl[sl, None, None] + off[None, :, None]) * nv + (cv[sl, None, None] + off[None, None, :])).ravel()
            wts = (lv[:, :, None] * gv[sl, None, :]).ravel()
            A += np.bincount(idx, weights=wts.real, minlength=nl * nv) + 1j * np.bincount(idx, weights=wts.imag, minlength=nl * nv)
        T = np.fft.fft2(A.reshape(nl, nv)) * h * h
        dy = 2 * math.pi / (nl * h); dt = 2 * math.pi / (nv * h)
        aT = np.abs(T); out.append((kappa, [float((((aT ** p).sum(axis=0) * dy) ** (1.0 / p)).sum() * dt) for p in PS]))
        del A, T, aT
    return len(p), (nl, nv), out

if __name__ == "__main__":
    N = int(sys.argv[1]); which = sys.argv[2]
    kappas = [float(x) for x in sys.argv[3].split(",")] if len(sys.argv) > 3 else [0.0, 0.25, 0.5, 1.0, 2.0]
    hshift = float(sys.argv[4]) if len(sys.argv) > 4 else 0.0
    if which == "rat":
        R = np.eye(3)
    elif which == "irr":
        R = rot([1, 2, 0], math.atan(math.sqrt(2))) @ rot([0, 1, 3], math.atan(math.sqrt(3)))
    else:   # a second irrational rotation
        R = rot([3, -1, 2], math.atan(math.sqrt(5))) @ rot([1, 1, 1], math.atan(math.sqrt(7)))
    t0 = time.time()
    fine = len(sys.argv) > 5 and sys.argv[5] == "fine"
    npts, shape, out = j2(N, R, kappas, hshift=hshift, fine=fine)
    print("N=%d frame=%s shift_P=%.2f %s points=%d grid=%s (%.0fs)" % (N, which, hshift, "fine combs in [0,2]" if fine else "combs at the integers", npts, shape, time.time() - t0))
    print("  mixed norms int dt ||T(., t)||_{L^p(dy)} for p = " + ", ".join(str(p) for p in PS))
    for kappa, vals in out:
        print("  kappa=%5.2f  " % kappa + "  ".join("%8.3f" % v for v in vals))
    print("(4 pi)^2 = %.1f" % ((4 * math.pi) ** 2))
