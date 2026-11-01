"""Where the move (X, Y) -> (X - f, Y + f) breaks the cluster total, for E1 in the separating/connecting form
(see README, 'E1 as a comparison'). Per (size, cluster total): G = #{f in Y - X}, B = #{f in X - Y}, B split by the
shift d = [f bridge of X] - [f joins two components of Y] in {-1, 0, +1}, and Gx = good pairs outside the move's
image (X + f connects u, v, or Y - f does not). python e1_types.py n kind(adj|dis)"""
import sys, itertools
from collections import defaultdict
from e1_swap import comps
n, kind = int(sys.argv[1]), sys.argv[2]
E = list(itertools.combinations(range(n), 2))
e = (0, 1); f = (1, 2) if kind == 'adj' else (2, 3)
rest = [x for x in E if x != e]
u, v = e
info = {}
for mask in range(1 << len(rest)):
    S = frozenset(rest[j] for j in range(len(rest)) if mask >> j & 1)
    k, find = comps(n, S)
    info[S] = (len(S), k, find(u) == find(v))
T = defaultdict(lambda: defaultdict(int))
sep = [S for S in info if not info[S][2]]
con = [S for S in info if info[S][2]]
for X in sep:
    sx, kx, _ = info[X]
    for Y in con:
        sy, ky, _ = info[Y]
        key = (sx + sy, kx + ky)
        if f in Y and f not in X:
            T[key]['G'] += 1
            if info[X | {f}][2] or not info[Y - {f}][2]:
                T[key]['Gx'] += 1
        if f in X and f not in Y:
            T[key]['B'] += 1
            d = (info[X - {f}][1] - kx) - (ky - info[Y | {f}][1])
            T[key]['B%+d' % d] += 1
print('size k : G B | B-1 B+0 B+1 | Gx | G-B')
for key in sorted(T):
    t = T[key]
    if t['G'] or t['B']:
        print(key, ':', t['G'], t['B'], '|', t['B-1'], t['B+0'], t['B+1'], '|', t['Gx'], '|', t['G'] - t['B'])
