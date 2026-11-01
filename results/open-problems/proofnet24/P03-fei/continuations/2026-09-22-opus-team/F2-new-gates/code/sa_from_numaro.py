import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
import numpy as np, time, sys
from holecore import anneal, make_phi, make_par, summarize
m = int(sys.argv[1]); start = sys.argv[2]; iters = int(sys.argv[3]); runs = int(sys.argv[4])
N = 1 << m; phi = make_phi(N); par = make_par(N)
c = np.load(start).astype(np.int64)
base = summarize(c, m)['R']
best_all = base
for T0 in (0.003, 0.01, 0.03):
    for r in range(runs):
        t = time.time()
        b, bR, acc = anneal(c, m, iters, T0, 1e-5, 1000 * r + int(T0 * 1e4), phi, par, 96, True)
        s = summarize(b, m)
        print(f"m={m} T0={T0} run {r}: best R={bR:.12f} ({bR-base:+.2e}) holes={s['holes']} ncomp={s['ncomp']} nvars={s['nvars']} acc={acc} t={time.time()-t:.0f}s", flush=True)
        if bR > best_all + 1e-12:
            best_all = bR
            np.save(f"../logs/sa_numaro_improved_m{m}.npy", b.astype(np.int8))
print("BEST", best_all, "base", base)
