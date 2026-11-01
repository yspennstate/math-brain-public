"""Simulated annealing driver over balanced partial cores c0 in {-1,0,1}^(2^m).
usage: python sa_driver.py m restarts iters T0 T1 seed [start.npy] [max_holes]
"""
import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
import sys, time, json
import numpy as np
from holecore import anneal, make_phi, make_par, summarize

m = int(sys.argv[1]); restarts = int(sys.argv[2]); iters = int(sys.argv[3])
T0 = float(sys.argv[4]); T1 = float(sys.argv[5]); seed = int(sys.argv[6])
start = sys.argv[7] if len(sys.argv) > 7 and sys.argv[7] != '-' else None
max_holes = int(sys.argv[8]) if len(sys.argv) > 8 else (1 << m) // 4
N = 1 << m
phi = make_phi(N); par = make_par(N)
rng = np.random.default_rng(seed)
overall = None
for r in range(restarts):
    if start:
        c = np.load(start).astype(np.int64)
    else:
        c = np.ones(N, dtype=np.int64); c[rng.permutation(N)[:N // 2]] = -1
    t = time.time()
    best, bR, acc = anneal(c, m, iters, T0, T1, seed * 1000 + r, phi, par, max_holes, True)
    # polish at zero temperature
    best, bR, acc2 = anneal(best, m, iters // 4, 1e-12, 1e-13, seed * 1000 + r + 500, phi, par, max_holes, True)
    s = summarize(best, m)
    print(f"m={m} restart {r}: R={s['R']:.12f} H={s['H']:.6f} I={s['I']:.6f} holes={s['holes']} ncomp={s['ncomp']} maxcomp={s['maxcomp']} nvars={s['nvars']} acc={acc} t={time.time()-t:.1f}s", flush=True)
    if overall is None or s['R'] > overall[0]:
        overall = (s['R'], best.copy(), s)
tag = f"m{m}_s{seed}"
np.save(f"../logs/sa_best_{tag}.npy", overall[1].astype(np.int8))
print("BEST", tag, json.dumps({k: (float(v) if isinstance(v, float) else v) for k, v in overall[2].items()}))
