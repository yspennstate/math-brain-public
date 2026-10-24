"""Adversarial (CS) check: rational fibre (1,1,1) and RATIONAL basis (alpha = 0), where the image lattice is
{(a/sqrt2, b/sqrt6)}; with lambda = 1 and beta = sqrt6/2 the parabola u^2 + beta s = y meets a lattice point in every
column a when 2y is an integer of the right parity.  Report the supremum over y of the density of Y off the fold."""
import numpy as np
import m2_comb as t
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

def density_grid(v, b, N, h):
    m = len(v); D = np.stack([v, b], 1)
    span = (np.abs(D).sum(0) * N).max() + 4 * h * m
    n = int(2 ** np.ceil(np.log2(span / h + 8)))
    F = None; lo = np.zeros(2)
    for i in range(m):
        lo_i = np.minimum(0, D[i]) * N - h
        lo += lo_i
        G = np.fft.rfft2(t.line_measure(n, h, lo_i, D[i], "comb", N, 1.0))
        F = G if F is None else F * G
    dens = np.maximum(np.fft.irfft2(F, s=(n, n)), 0) / (h * h)
    u = lo[0] + (np.arange(n) + 0.5) * h; s = lo[1] + (np.arange(n) + 0.5) * h
    return u, s, dens

v = np.array([1, -1, 0]) / np.sqrt(2); b = np.array([1, 1, -2]) / np.sqrt(6)
lam, r = 1.0, 0.5
for N in (4, 8, 16):
    h = 1.0 / (6 * N)
    u, s, dens = density_grid(v, b, N, h)
    U, S = np.meshgrid(u, s, indexing="ij")
    out = [f"N={N:2d}"]
    for beta in (np.sqrt(6) / 4, np.sqrt(6) / 2, np.sqrt(6), 1.0):
        mask = np.abs(U) > r
        Y = lam * U ** 2 + beta * S
        bw = 1.0 / (8 * N)
        hist, edges = np.histogram(Y.ravel(), bins=np.arange(Y[mask].min(), Y[mask].max() + bw, bw), weights=(dens * h * h * mask).ravel())
        out.append(f"beta={beta:.3f}: sup={hist.max() / bw:.3f}")
    print("  ".join(out), flush=True)
