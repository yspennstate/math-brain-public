import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
import numpy as np, time
from orbits import *
from holecore import *
G = np.load('../logs/numaro_gens.npy')
gens = [(tuple(int(t) for t in r[:9]), int(r[9])) for r in G]
rep, sgn, forced = orbit_structure(9, gens)
no = len(forced)
m = 9; N = 512; phi = make_phi(N); par = make_par(N)
ol = np.array([o for o in range(no) if not forced[o]], dtype=np.int64)
t = time.time()
R, V = enum_orbits(rep, sgn, ol, m, phi, par, 20, True)
print('time', time.time() - t)
for r, v in zip(R, V):
    c0 = c0_from_values(v, rep, sgn)
    s = summarize(c0, 9)
    print(f"{r:.12f} v={v.tolist()} holes={s['holes']} ncomp={s['ncomp']} maxcomp={s['maxcomp']} I={s['I']:.6f}")
