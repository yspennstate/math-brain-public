import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
import numpy as np
from orbsearch import *
from orbits import values_from_c0
G = np.load('../logs/numaro_gens.npy')
gens = [(tuple(int(t) for t in r[:9]), int(r[9])) for r in G]
M = OrbitModel(9, gens)
c0 = np.load('../logs/numaro_core_c0.npy').astype(np.int64)
v = values_from_c0(c0, M.rep, M.sgn, M.no)
print(M.evaluate(v), check_I2(M, v))
rng = np.random.default_rng(0)
for t in range(5):
    w = rng.integers(-1, 2, M.no)
    print(check_I2(M, w), M.evaluate(w)[0], summarize(M.c0(w), 9)['R'])
