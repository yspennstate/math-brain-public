"""Evaluate t104_gpu_hsearch.values (batched) and direct() at the n = 5 graphs where minbeta_n5 found failures."""
import sys
sys.argv = ["t104_gpu_hsearch.py", "5", "1", "1", "1", "1", "--cpu"]
import numpy as np
import torch
import t104_gpu_hsearch as T

G = {
    "bad1_ctrl": "12:0.2130123305 13:0.2127073055 14:0.0139801510 15:0.0000219906 23:0.2118146499 24:0.0152514065 25:0.0014452512 34:0.0156795013 35:0.0019245224 45:0.3141628909",
    "bad2_ctrl": "12:0.0001574615 13:0.0200385777 14:0.2081196625 15:0.2091358173 23:0.3049773720 24:0.0037473146 25:0.0021195765 34:0.0230768831 35:0.0216992298 45:0.2069281050",
    "star_b10": "12:0.2500889069 13:0.2500001095 14:0.2499108570 15:0.2500001266 23:0 24:0 25:0 34:0 35:0 45:0",
}
for name, s in G.items():
    d = {k: float(v) for k, v in (t.split(":") for t in s.split())}
    w = np.array([d["%d%d" % (i + 1, j + 1)] for (i, j) in T.pairs])
    wt = torch.tensor(w[None, :] + 1e-300, dtype=T.dt, device=T.dev)
    for grid in ([10.0], [30.0], [1e6], T.GRID):
        v, sl, g = T.values(wt, grid)
        print("%-10s grid %-28s batched %+.9e  direct %+.9e  slack %+.6e  gap12 %.2e" % (
            name, str(grid)[:28], float(v[0]), T.direct(w, grid), float(sl[0]), float(g[0])), flush=True)
