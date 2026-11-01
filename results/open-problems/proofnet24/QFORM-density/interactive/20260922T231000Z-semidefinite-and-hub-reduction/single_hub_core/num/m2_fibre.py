"""M_2 for m = 3 coordinates whose 2D projection has the rational fibre (1,1,1)/sqrt3, with the basis (v, b) of the
orthogonal plane rotated by an angle alpha.  Prediction: for irrational alpha the diagonal fibre lines through N teeth
project to N^2 points with distinct s-coordinates, and M_2 grows like N; for alpha = 0 the s-coordinates coincide."""
import numpy as np
import m2_comb as t
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
e1 = np.array([1, -1, 0]) / np.sqrt(2); e2 = np.array([1, 1, -2]) / np.sqrt(6)
for name, al in (("alpha=0", 0.0), ("alpha=golden", 0.5 * (np.sqrt(5) - 1)), ("alpha=0.3", 0.3)):
    v = np.cos(al) * e1 + np.sin(al) * e2; b = -np.sin(al) * e1 + np.cos(al) * e2
    for N in (4, 8, 16):
        r = t.m2(v, b, "comb", N, 1.0, 1.0 / (6 * N))
        if r is None:
            print(name, N, "skipped", flush=True); continue
        ru = t.m2(v, b, "unif", N, 1.0, 1.0 / (6 * N))
        print(f"m=3 fibre(1,1,1) {name:13s} N={N:2d}  comb M2={r[0]:.3f} peak={r[2]:.3f}   uniform M2={ru[0]:.4f}", flush=True)
