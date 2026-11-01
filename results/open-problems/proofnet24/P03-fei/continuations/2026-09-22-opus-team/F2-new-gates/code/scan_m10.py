import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
import numpy as np, time
from holecore import *
c0 = np.load('../logs/numaro_core_c0.npy').astype(np.int64)
c10 = np.concatenate([c0, c0])
m = 10; N = 1024; phi = make_phi(N); par = make_par(N)
base = summarize(c10, m)['R']
t = time.time()
R, mv = scan_2cell(c10, m, phi, par, 80, 12)
print('scan time', time.time() - t, 'base', base)
for r, (x, na, y, nb) in zip(R, mv):
    print(f'{r:.12f} {r-base:+.3e}  x={x} {c10[x]}->{na}  y={y} {c10[y]}->{nb}')
