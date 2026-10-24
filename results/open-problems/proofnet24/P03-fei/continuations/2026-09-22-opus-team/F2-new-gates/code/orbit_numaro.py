import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
import numpy as np
from autgroup import aut_group
from orbits import *
from holecore import summarize
c0 = np.load('../logs/numaro_core_c0.npy').astype(np.int64)
A = aut_group(c0, 9)
gens = [(p, 1 if t == 'plain' else -1) for p, t in A]
rep, sgn, forced = orbit_structure(9, gens)
no = len(forced)
sz = orbit_sizes(rep, no)
print('orbits:', no, ' forced-zero:', int(forced.sum()), ' sizes:', sorted(sz.tolist()))
v = values_from_c0(c0, rep, sgn, no)
print('Numaro values per orbit:', v.tolist())
free = [o for o in range(no) if not forced[o]]
print('free orbits:', len(free))
# layers of each orbit
pc = np.array([bin(x).count('1') for x in range(512)])
for o in range(no):
    xs = np.where(rep == o)[0]
    print(o, 'size', sz[o], 'weights', sorted(set(pc[xs].tolist())), 'forced' if forced[o] else '', 'v=', v[o])
np.save('../logs/numaro_gens.npy', np.array([list(p) + [s] for p, s in gens], dtype=np.int64))
