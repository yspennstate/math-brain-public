import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
import numpy as np, time
from orbsearch import *
G = np.load('../logs/numaro_gens.npy')
gens = [(tuple(int(t) for t in r[:9]), int(r[9])) for r in G]
M = OrbitModel(9, gens)
t = time.time()
R, V = run_enum(M, topk=5)
print('time', time.time()-t)
for r, v in zip(R, V): print(r, v.tolist(), M.evaluate(v)[0])
