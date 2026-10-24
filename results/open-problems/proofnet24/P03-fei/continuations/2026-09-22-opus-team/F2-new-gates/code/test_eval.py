import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
import numpy as np, time
from holecore import *
c0 = np.load('../logs/numaro_core_c0.npy').astype(np.int64)
print(summarize(c0, 9))
# embed in m=10 with an irrelevant variable
c10 = np.concatenate([c0, c0])
print(summarize(c10, 10))
m=9; N=512; phi=make_phi(N); par=make_par(N)
t=time.time()
best, bR, acc = anneal(c0, 9, 1000, 1e-9, 1e-10, 1, phi, par, 64, True)
print('compile+1k', time.time()-t)
t=time.time()
best, bR, acc = anneal(c0, 9, 200000, 1e-9, 1e-10, 1, phi, par, 64, True)
print('200k iters', time.time()-t, bR, acc)
print(summarize(best, 9))
