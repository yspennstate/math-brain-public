"""Curved slicing test.  For the projection (V, B) of three comb coordinates with the rational fibre (1,1,1)/sqrt3 and an
irrational basis (where M_2 grows like N), compute the density of Y = lambda V^2 + beta B restricted to |V| > r, by
pushing the grid density forward, and compare its supremum across N.  (CS) predicts a bound C/(|lambda| r)."""
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

e1 = np.array([1, -1, 0]) / np.sqrt(2); e2 = np.array([1, 1, -2]) / np.sqrt(6)
al = 0.5 * (np.sqrt(5) - 1)
v = np.cos(al) * e1 + np.sin(al) * e2; b = -np.sin(al) * e1 + np.cos(al) * e2
lam, r = 1.0, 0.5
for N in (4, 8, 16):
    h = 1.0 / (6 * N)
    u, s, dens = density_grid(v, b, N, h)
    U, S = np.meshgrid(u, s, indexing="ij")
    M2 = dens.max(axis=0).sum() * h
    out = [f"N={N:2d} M2={M2:.2f}"]
    for beta in (0.02, 0.1, 0.5):
        for V0 in (0.0, float(np.average(u, weights=dens.sum(1)))):
            mask = np.abs(U - V0) > r
            Y = lam * (U - V0) ** 2 + beta * S
            w = dens * h * h * mask
            bw = 1.0 / (8 * N)
            hist, edges = np.histogram(Y.ravel(), bins=np.arange(Y[mask].min(), Y[mask].max() + bw, bw), weights=w.ravel())
            out.append(f"beta={beta} V0={V0:+.1f}: sup={hist.max() / bw:.3f}")
    print("  ".join(out), f"(bound 2/(lambda r) for beta=0 is {2/(lam*r):.1f})", flush=True)
