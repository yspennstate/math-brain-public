"""Adjacent colouring form: does the finer grading by (k(red), k(blue)) separately also hold?"""
import sys, random
from collections import defaultdict

from e1_swap import comps
V, m, seed, cnt = map(int, sys.argv[1:5])
rnd = random.Random(seed)
tot = fine_fail = coarse_fail = 0
ex = None
for t in range(cnt):
    H = [tuple(sorted(rnd.sample(range(V), 2))) for _ in range(m)]
    for fi in range(m):
        f = H[fi]
        for u in range(V):
            for v in range(u + 1, V):
                if not ({u, v} & set(f)):
                    continue
                T = defaultdict(int); F = defaultdict(int)
                for mask in range(1 << m):
                    red = [H[j] for j in range(m) if mask >> j & 1]
                    blue = [H[j] for j in range(m) if not mask >> j & 1]
                    kr, fr = comps(V, red)
                    if fr(u) == fr(v): continue
                    kb, fb = comps(V, blue)
                    if fb(u) != fb(v): continue
                    s = -1 if mask >> fi & 1 else 1
                    T[kr + kb] += s; F[(kr, kb)] += s
                tot += 1
                if any(c < 0 for c in T.values()): coarse_fail += 1
                if any(c < 0 for c in F.values()):
                    fine_fail += 1
                    if ex is None: ex = (H, f, u, v, {k: c for k, c in F.items() if c < 0})
print('V %d m %d seed %d: adjacent cases %d, coarse fails %d, fine (kr,kb) fails %d' % (V, m, seed, tot, coarse_fail, fine_fail))
print('first fine failure:', ex)
