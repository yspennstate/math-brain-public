"""Read-once (AND/OR/NOT/XOR) fixed point at a constant C on the default grid (or the fine grid); saves logs/ro_<tag>.npz.
usage: ro_fp.py C tag [fine]"""
import os, sys, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import vicore as V
V.lowprio(4)
C = float(sys.argv[1]); tag = sys.argv[2]
fine = len(sys.argv) > 3 and sys.argv[3] == "fine"
grid = V.Grid(fine=(0.44, 2.0 ** -13)) if fine else V.Grid()
t0 = time.time()
res = V.iterate(grid, C, use_xor=True, verbose=True, every=20, iters=6000)
np.savez(os.path.join(HERE, "..", "logs", "ro_%s.npz" % tag), xs=grid.xs, G=res["G"], C=C, M=grid.M, K=grid.K)
print("C = %.12f: %s after %d sweeps (%.0f s)" % (C, res["reason"], res["it"], time.time() - t0))
for p in (0.5, 0.4999, 0.4995, 0.499, 0.4974, 0.495, 0.49, 0.48, 0.45, 0.4, 0.3, 0.25):
    print("  V(%.4f) - C = %+.6e" % (p, float(grid.V(res["G"], p)[0]) - C))
