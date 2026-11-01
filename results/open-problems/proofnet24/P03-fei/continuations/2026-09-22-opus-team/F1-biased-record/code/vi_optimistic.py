"""Optimistic variant of vi_g.run: after every sweep V is capped at C everywhere (pretend that at every truth
probability there is a function of slack at most C, i.e. remove the cusp of V at 1/2).  If V(1/2) still stays at C,
the cusp is not what blocks a gain from biased inputs.
Usage: python vi_optimistic.py C families npar"""
import sys, time
import numpy as np
try:
    import psutil
    _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
except Exception:
    pass
from ro_gamma import Grid
import ro_gamma_nb as RB
from vi_g import FAMILIES, build_family, g_move

C = float(sys.argv[1]); names = sys.argv[2].split(","); npar = int(sys.argv[3])
grid = Grid(24, 40); ps = grid.ps; N = len(ps)
rs = np.concatenate([ps, 1 - ps[1:]])
fams = {nm: build_family(FAMILIES[nm][0], FAMILIES[nm][1], rs, np.arange(1, npar) / npar) for nm in names}
Gam = np.full(N, 60.0); Gam[0] = C
Gam = np.minimum(Gam, C); G = Gam / ps
t0 = time.time()
for it in range(300):
    gam_fn = lambda q: grid.gamma_at(G, q)
    Tv = RB.T_op(grid.xs, G, float(grid.K), rs, grid.all_p, grid.Lall)
    for nm in names:
        b, _ = g_move(fams[nm], gam_fn, C, len(rs)); Tv = np.minimum(Tv, b)
    Ts = Tv[:N].copy(); Ts[1:] = np.minimum(Ts[1:], Tv[N:])
    Gam2 = np.minimum(np.minimum(Gam, Ts), C)
    diff = np.max(np.abs(Gam2 - Gam) / ps); Gam = Gam2; G = Gam / ps
    if it % 10 == 0 or diff < 1e-12:
        print("  iter %3d  max dG %.2e  V(1/2) - C = %+.3e  min V %.3e  (%.0f s)" % (it, diff, Gam[0] - C, Gam.min(), time.time() - t0), flush=True)
    if Gam[0] < C - 1e-9 or Gam.min() < -1e-9:
        print("DIVERGES under the optimistic cap: V(1/2) - C = %+.3e" % (Gam[0] - C)); break
    if diff < 1e-12:
        print("converged: V(1/2) = C under the optimistic cap (no gain even without the cusp)"); break
np.savez("../logs/vig_optimistic_%s.npz" % ("_".join(names).replace("+", "p").replace("-", "m")), xs=grid.xs, G=G, C=C, M=24, K=40)
