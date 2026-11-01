"""Multivariate E1 split by pair type on random graphs: adjacent (e, f share a vertex) against disjoint.
python e1_multi_adj.py V seed cnt lo hi"""
import sys, itertools, random
from e1_multi import neg_rows

V, seed, cnt, lo, hi = map(int, sys.argv[1:6])
rnd = random.Random(seed)
allE = list(itertools.combinations(range(V), 2))
c = {'adj': [0, 0], 'dis': [0, 0]}
for t in range(cnt):
    E = sorted(rnd.sample(allE, rnd.randint(lo, hi)))
    for e, f in itertools.permutations(E, 2):
        kind = 'adj' if set(e) & set(f) else 'dis'
        c[kind][0] += 1
        c[kind][1] += neg_rows(V, E, e, f)[0] > 0
        if kind == 'adj' and c[kind][1] == 1 and neg_rows(V, E, e, f)[0]:
            print('first adjacent failure', E, e, f, flush=True)
print('%d random graphs on %d vertices (seed %d, %d..%d edges): adjacent pairs %d, failing %d; disjoint pairs %d, failing %d'
      % (cnt, V, seed, lo, hi, c['adj'][0], c['adj'][1], c['dis'][0], c['dis'][1]), flush=True)
