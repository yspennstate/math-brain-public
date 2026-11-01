# TL_perp on the spread frame: J(kappa) = int int |E exp(i(yL + tV + kappa P^2))| dy dt, P orthogonal to the frame (w, v).
# In the lattice + Gaussian-cell model the twist depends on the cell only through its P-part, independent of the (L, V)
# part, so each lattice point carries the exact weight (1 - 2 i kappa s^2)^{-1/2} exp(i kappa P_z^2/(1 - 2 i kappa s^2)).
import sys, math, time
import numpy as np
from jperp import triple_law, rot

def jperp2(N, R, kappas, pad=2.0, chunk=4000):
    z, p = triple_law(N)
    y = z @ R / math.sqrt(8.0)
    L, V, P = y[:, 0], y[:, 1], y[:, 2]
    s = 1.0 / (math.sqrt(12.0) * N); h = s / 3.0; W = 12
    l0 = L.min() - 5 * s; v0 = V.min() - 5 * s
    nl = int(pad * (L.max() - L.min() + 10 * s) / h) + 1; nv = int(pad * (V.max() - V.min() + 10 * s) / h) + 1
    cl = np.rint((L - l0) / h).astype(np.int64); cv = np.rint((V - v0) / h).astype(np.int64)
    off = np.arange(-W, W + 1)
    gl = np.exp(-0.5 * ((l0 + (cl[:, None] + off[None, :]) * h - L[:, None]) / s) ** 2) / (math.sqrt(2 * math.pi) * s)
    gv = np.exp(-0.5 * ((v0 + (cv[:, None] + off[None, :]) * h - V[:, None]) / s) ** 2) / (math.sqrt(2 * math.pi) * s)
    out = []
    for kappa in kappas:
        c = p * np.exp(1j * kappa * P ** 2 / (1 - 2j * kappa * s * s)) / np.sqrt(1 - 2j * kappa * s * s)
        A = np.zeros(nl * nv, dtype=np.complex128)
        for c0 in range(0, len(p), chunk):
            sl = slice(c0, c0 + chunk)
            idx = ((cl[sl, None, None] + off[None, :, None]) * nv + (cv[sl, None, None] + off[None, None, :])).ravel()
            wts = (c[sl, None, None] * gl[sl, :, None] * gv[sl, None, :]).ravel()
            A += np.bincount(idx, weights=wts.real, minlength=nl * nv) + 1j * np.bincount(idx, weights=wts.imag, minlength=nl * nv)
        T = np.abs(np.fft.fft2(A.reshape(nl, nv)) * h * h)
        out.append((kappa, float(T.sum() * (2 * math.pi / (nl * h)) * (2 * math.pi / (nv * h)))))
    return len(p), out

if __name__ == "__main__":
    kappas = [0.0, 0.05, 0.2, 0.5, 1.0]
    for which in ("irr", "irr2"):
        R = rot([1, 2, 0], math.atan(math.sqrt(2))) @ rot([0, 1, 3], math.atan(math.sqrt(3))) if which == "irr" else \
            rot([3, -1, 2], math.atan(math.sqrt(5))) @ rot([1, 1, 1], math.atan(math.sqrt(7)))
        for N in (4, 6, 8):
            t0 = time.time(); n, out = jperp2(N, R, kappas)
            print("%s N=%d  " % (which, N) + "  ".join("k=%.2f: %7.3f" % (k, v) for k, v in out) + "   (%.0fs)" % (time.time() - t0), flush=True)
