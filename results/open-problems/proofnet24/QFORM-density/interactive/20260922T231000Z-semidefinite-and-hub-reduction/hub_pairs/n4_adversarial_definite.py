"""N4. Adversarial checks of Conjecture 6(i): anisotropic definite hub blocks diag(.2, .2 e) and a rotated rank-one
block b u u^T (u = (1,1)/sqrt2), remainders 0, the Schur match L^T B^+ L and half of it, spread and uniform hub laws."""
try:
    import psutil
    psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import sys, time
import numpy as np
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hubpair_lib import UnionLaw, pair_prob, spread_rows
rng = np.random.default_rng(3)
m = 60
A = spread_rows(m, 1.0, rng)
N = 100_000
Xp = rng.random((N, m)) - 0.5
L = Xp @ A.T
c = 2 * L
t0 = time.time()
laws = {"uniform": (UnionLaw.interval(), UnionLaw.interval()),
        "spread": (UnionLaw.spread(5, 8.0, rng), UnionLaw.spread(7, 12.0, rng))}
def supd(B, r, law1, law2, grid):
    x1 = law1.sample(N, rng)
    v = [pair_prob(B, c[:, 0], c[:, 1], r, x1, s, 3e-3, law2).mean() / 6e-3 for s in grid]
    k = int(np.argmax(v)); s0 = grid[k]; ds = grid[1] - grid[0]
    f = [pair_prob(B, c[:, 0], c[:, 1], r, x1, s, 3e-4, law2).mean() / 6e-4 for s in np.linspace(s0 - ds, s0 + ds, 11)]
    return max(max(v), max(f))
cases = []
for e in [1.0, 0.1, 0.01, 0.001]:
    cases.append((f"diag(.2, .2*{e})", np.array([[0.2, 0], [0, 0.2 * e]])))
u = np.array([1.0, 1.0]) / np.sqrt(2)
cases.append(("rotated rank one .2 u u^T", 0.2 * np.outer(u, u)))
cases.append(("near rank one .2 u u^T + .002 n n^T", 0.2 * np.outer(u, u) + 0.002 * np.outer([1, -1], [1, -1]) / 2))
for name, B in cases:
    Bp = np.linalg.pinv(B)
    S = np.einsum('ni,ij,nj->n', L, Bp, L)
    for lname, (l1, l2) in laws.items():
        row = []
        for tt in [0.0, 0.5, 1.0]:
            r = tt * S
            span = 3 + np.percentile(np.abs(r), 99) if tt > 0 else 3.0
            grid = np.linspace(-span, span, 81)
            row.append(supd(B, r, l1, l2, grid))
        print(f"{name:38s} {lname:8s} sup density for R = 0, .5 Schur, Schur: " + "  ".join(f"{x:6.3f}" for x in row) + f"  [{time.time()-t0:.0f}s]", flush=True)
print("done", flush=True)
