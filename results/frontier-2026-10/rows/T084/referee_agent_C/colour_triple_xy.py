"""Statement S for two independent edge sets instead of a colouring: X, Y subsets of E(H), X separating u from v and
from w, Y joining u to v; at fixed |X| + |Y| and k(X) + k(Y), #{v ~ w in Y, not in X} >= #{v ~ w in X, not in Y}?
Also the per-edge-weight form (grading by the multiset X + Y, i.e. by (X & Y, X ^ Y) and k(X) + k(Y)).
python colour_triple_xy.py V m seed cnt"""
import sys, random
from collections import defaultdict
from e1_swap import comps

V, m, seed, cnt = map(int, sys.argv[1:5])
rnd = random.Random(seed)
cases = f1 = f2 = 0
for t in range(cnt):
    H = [tuple(sorted(rnd.sample(range(V), 2))) for _ in range(m)]
    info = []
    for mask in range(1 << m):
        k, fd = comps(V, [H[j] for j in range(m) if mask >> j & 1])
        info.append((k, [fd(x) for x in range(V)]))
    for u in range(V):
        for v in range(V):
            for w in range(V):
                if len({u, v, w}) < 3:
                    continue
                Xs = [x for x in range(1 << m) if info[x][1][u] not in (info[x][1][v], info[x][1][w])]
                Ys = [y for y in range(1 << m) if info[y][1][u] == info[y][1][v]]
                T1 = defaultdict(int); T2 = defaultdict(int)
                for x in Xs:
                    cx = info[x][1]; xvw = cx[v] == cx[w]
                    for y in Ys:
                        cy = info[y][1]; yvw = cy[v] == cy[w]
                        if xvw == yvw:
                            continue
                        s = 1 if yvw else -1
                        kk = info[x][0] + info[y][0]
                        T1[(bin(x).count('1') + bin(y).count('1'), kk)] += s
                        T2[(x & y, x ^ y, kk)] += s
                cases += 1
                f1 += any(c < 0 for c in T1.values())
                f2 += any(c < 0 for c in T2.values())
print('V %d m %d seed %d: triples %d, S(X,Y) fails %d, per-edge-weight form fails %d' % (V, m, seed, cases, f1, f2))
