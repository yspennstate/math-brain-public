"""n <= 4: sup_f min_{delta in [delta0, 1)} kappa_delta(f)  (each function picks its own rate; the induction still closes)."""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mslib import polite
polite()
from sweep_n4 import EHa, Ha, Ia, pc, nz, n   # re-runs the exact sweep (a few seconds)
grid = np.linspace(0.02, 0.98, 49)
K = np.stack([(Ha - EHa @ (x ** pc * (1 - x) ** (n - pc))) / ((1 - x) * np.where(nz, Ia, 1)) for x in grid], axis=1)
for d0 in (0.1, 0.25, 0.5, 0.75, 0.9):
    sel = grid >= d0 - 1e-12
    val = np.where(nz, K[:, sel].min(axis=1), 0).max()
    print(f"delta0={d0}: sup_f min_(delta>=delta0) kappa_delta(f) = {val:.6f}   (fixed delta0: {np.where(nz, K[:, np.argmin(abs(grid - d0))], 0).max():.6f})")
