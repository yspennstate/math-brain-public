"""Aut(H)-invariant partial cores on the edge set of a graph H.
usage: python run_graph.py H restarts iters T0 T1 pen [start: pm|rand]
H in: k33, k34, k35, k44, k25, k26, k5, k6, q3, petersen
"""
import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
import sys, time, json
import numpy as np
import graphs
from orbsa2 import Model2, anneal_pen
from holecore import summarize

name = sys.argv[1]; restarts = int(sys.argv[2]); iters = int(sys.argv[3])
T0 = float(sys.argv[4]); T1 = float(sys.argv[5]); pen = float(sys.argv[6])
start = sys.argv[7] if len(sys.argv) > 7 else 'pm'
bip = {'k33': (3, 3), 'k34': (3, 4), 'k35': (3, 5), 'k44': (4, 4), 'k25': (2, 5), 'k26': (2, 6), 'k36': (3, 6)}
if name in bip:
    a, b = bip[name]; m, perms, E = graphs.kab(a, b)
elif name in ('k5', 'k6'):
    m, perms, E = graphs.kn(int(name[1]))
elif name == 'q3':
    m, perms, E = graphs.cube3()
elif name == 'petersen':
    m, perms, E = graphs.petersen()
t = time.time()
M = Model2(m, perms)
print(f"{name}: m={m} orbits={M.no} build {time.time()-t:.1f}s", flush=True)
N = 1 << m
# property start
if name in bip:
    a, b = bip[name]
    prop = np.array([-1 if graphs.has_pm_bip(x, E, a, b) else 1 for x in range(N)], dtype=np.int64)
    print(f"  Pr[saturating matching] = {(prop == -1).sum()}/{N}", flush=True)
else:
    prop = None
rng = np.random.default_rng(7)
bestall = (-1e9, None)
for r in range(restarts):
    if start == 'pm' and prop is not None and r % 2 == 0:
        v0 = np.zeros(M.no, dtype=np.int64)
        for x in range(N):
            v0[M.rep[x]] = prop[x]
    else:
        v0 = rng.choice([-1, 1], size=M.no).astype(np.int64)
    t = time.time()
    b, bR = anneal_pen(M, v0, iters, T0, T1, 11 + r, pen=pen)
    if bR > -1e8:
        b, bR = anneal_pen(M, b, max(iters // 5, 1000), 1e-9, 1e-10, 99 + r, pen=pen)
    c = M.c0(b)
    s = summarize(c, m) if bR > -1e8 else {}
    print(f"  restart {r} ({'pm' if (start=='pm' and prop is not None and r%2==0) else 'rand'}): balanced R = {bR:.12f} "
          f"holes={int((c==0).sum())} ncomp={s.get('ncomp')} nvars={s.get('nvars')} I={s.get('I', 0):.6f} t={time.time()-t:.0f}s", flush=True)
    if bR > bestall[0]:
        bestall = (bR, b.copy())
np.save(f"../logs/graph_best_{name}.npy", M.c0(bestall[1]).astype(np.int8))
print("BEST", name, bestall[0])
