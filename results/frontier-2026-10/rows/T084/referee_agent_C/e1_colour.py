"""The 2-colouring form of multivariate E1 on multigraphs (README). H a multigraph containing f, e = uv a pair of
vertices; colour every edge of H red or blue with red not joining u to v and blue joining them. Claim (adjacent
f = vw): at every k(red) + k(blue), #(f blue) >= #(f red). python e1_colour.py V m seed cnt"""
import sys, random
from collections import defaultdict
from e1_swap import comps

V, m, seed, cnt = map(int, sys.argv[1:5])
rnd = random.Random(seed)
tested = {'adj': [0, 0], 'dis': [0, 0]}
for t in range(cnt):
    H = [tuple(sorted(rnd.sample(range(V), 2))) for _ in range(m)]
    for fi in range(m):
        f = H[fi]
        for u in range(V):
            for v in range(u + 1, V):
                kind = 'adj' if {u, v} & set(f) else 'dis'
                T = defaultdict(int)
                for mask in range(1 << m):
                    red = [H[j] for j in range(m) if mask >> j & 1]
                    blue = [H[j] for j in range(m) if not mask >> j & 1]
                    kr, fr = comps(V, red)
                    if fr(u) == fr(v):
                        continue
                    kb, fb = comps(V, blue)
                    if fb(u) != fb(v):
                        continue
                    T[kr + kb] += -1 if mask >> fi & 1 else 1
                tested[kind][0] += 1
                if any(c < 0 for c in T.values()):
                    tested[kind][1] += 1
                    if kind == 'adj' and tested[kind][1] <= 3:
                        print('ADJ FAIL H', H, 'f', f, 'u,v', u, v, dict(T), flush=True)
print('%d random multigraphs, %d vertices, %d edges (seed %d): adjacent cases %d failing %d; disjoint cases %d failing %d'
      % (cnt, V, m, seed, tested['adj'][0], tested['adj'][1], tested['dis'][0], tested['dis'][1]), flush=True)
