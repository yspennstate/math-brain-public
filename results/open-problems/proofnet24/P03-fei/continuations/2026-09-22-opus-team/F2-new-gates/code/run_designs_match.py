"""Group-invariant partial-core search on design groups, with complement duality.
usage: python run_designs.py name [maxfree_exhaustive] [sa_restarts] [sa_iters] [dual:1/0]
"""
import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
import sys, time, json
import numpy as np
import designs
from orbits import group_closure
from orbsearch_match import OrbitModel, run_enum, anneal_orbits

name = sys.argv[1]
maxfree = int(sys.argv[2]) if len(sys.argv) > 2 else 16
restarts = int(sys.argv[3]) if len(sys.argv) > 3 else 4
iters = int(sys.argv[4]) if len(sys.argv) > 4 else 20000
dual = int(sys.argv[5]) if len(sys.argv) > 5 else 1
if name.startswith('cyclic'):
    parts = name.split('_')
    m, perms = designs.cyclic(int(parts[1]), int(parts[2]) if len(parts) > 2 else None)
else:
    m, perms = getattr(designs, name)()
gens = [(p, 1) for p in perms]
order = len(group_closure(gens, m))
if dual:
    gens.append((tuple(range(m)), -1))
t = time.time()
M = OrbitModel(m, gens)
nfree = int((~M.forced).sum())
print(f"{name}: m={m} |G|={order} dual={dual} orbits={M.no} free={nfree} forced={int(M.forced.sum())} build {time.time()-t:.1f}s", flush=True)
out = dict(name=name, m=m, order=order, dual=dual, orbits=M.no, free=nfree)
if nfree <= maxfree:
    t = time.time()
    R, V = run_enum(M, topk=5)
    out['mode'] = 'exhaustive'
    out['top'] = [(float(r), v.tolist()) for r, v in zip(R, V)]
    c = M.c0(V[0])
    out['best_holes'] = int((c == 0).sum())
    print(f"  exhaustive {time.time()-t:.1f}s best R={R[0]:.12f} holes={out['best_holes']}", flush=True)
    for r, v in zip(R, V):
        print(f"   {r:.12f} {v.tolist()}")
else:
    out['mode'] = 'sa'
    rng = np.random.default_rng(1)
    bestall = (-1e9, None)
    for r in range(restarts):
        v0 = rng.choice([-1, 1], size=M.no).astype(np.int64)
        v0[M.forced] = 0
        t = time.time()
        b, bR = anneal_orbits(M, v0, iters, 0.05, 1e-4, 100 + r)
        b, bR = anneal_orbits(M, b, iters // 4, 1e-9, 1e-10, 200 + r)
        c = M.c0(b)
        print(f"  SA restart {r}: R={bR:.12f} holes={int((c==0).sum())} t={time.time()-t:.1f}s", flush=True)
        if bR > bestall[0]:
            bestall = (bR, b.copy())
    out['best'] = float(bestall[0]); out['v'] = bestall[1].tolist()
    np.save(f"../logs/design_best_{name}_d{dual}_match.npy", M.c0(bestall[1]).astype(np.int8))
json.dump(out, open(f"../logs/design_{name}_d{dual}_match.json", 'w', encoding='utf-8'), indent=1)
