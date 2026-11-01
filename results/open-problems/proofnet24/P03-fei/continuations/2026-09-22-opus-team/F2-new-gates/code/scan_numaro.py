import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
import numpy as np, time
from holecore import *
c0 = np.load('../logs/numaro_core_c0.npy').astype(np.int64)
m=9; N=512; phi=make_phi(N); par=make_par(N)
t=time.time()
R, mv = scan_2cell(c0, m, phi, par, 200, 25)
print('scan time', time.time()-t)
base = summarize(c0, 9)['R']
print('base R', base)
for r, (x, na, y, nb) in zip(R, mv):
    print(f'{r:.12f} {r-base:+.3e}  x={x} (w{bin(x).count("1")}) {c0[x]}->{na}   y={y} (w{bin(y).count("1")}) {c0[y]}->{nb}')
