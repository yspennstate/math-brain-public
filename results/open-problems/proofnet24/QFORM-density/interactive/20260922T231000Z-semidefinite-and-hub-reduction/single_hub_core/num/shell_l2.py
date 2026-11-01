"""Collision (L^2) norm of the density of Y = lambda (V - V0)^2 + beta B on dyadic shells R <= |V - V0| <= 2R.

Same grids as cs_test.py: three comb coordinates, fibre (1,1,1), irrational basis (the case where M_2 grows like N).
Without the slice in L the collision argument bounds each shell by (4/|lambda|) log 2 = 2.77/|lambda|; the printed
value is int h^2 dy for each shell, and 'all' is the whole region |V - V0| >= 1/4."""
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

lam = 1.0
for N in (4, 8, 16):
    hg = 1.0 / (6 * N)
    u, s, dens = density_grid(v, b, N, hg)
    U, S = np.meshgrid(u, s, indexing="ij")
    V0 = float(np.average(u, weights=dens.sum(1)))
    rows = []
    for beta in (0.02, 0.1, 0.5):
        Y = lam * (U - V0) ** 2 + beta * S
        vals = []
        for R in (0.25, 0.5, 1.0, 2.0):
            mask = (np.abs(U - V0) >= R) & (np.abs(U - V0) < 2 * R)
            if not mask.any():
                vals.append("  -  "); continue
            bw = max(1.0 / (8 * N), 2 * lam * R * hg)
            hist, _ = np.histogram(Y[mask], bins=np.arange(Y[mask].min(), Y[mask].max() + bw, bw),
                                   weights=(dens * hg * hg)[mask])
            vals.append(f"{(hist ** 2).sum() / bw:.3f}")
        mask = np.abs(U - V0) >= 0.25
        bw = 1.0 / (8 * N)
        hist, _ = np.histogram(Y[mask], bins=np.arange(Y[mask].min(), Y[mask].max() + bw, bw),
                               weights=(dens * hg * hg)[mask])
        rows.append(f"beta={beta}: shells R=1/4,1/2,1,2: {' '.join(vals)}  all: {(hist ** 2).sum() / bw:.3f}")
    print(f"N={N:2d}  " + "  |  ".join(rows), flush=True)
