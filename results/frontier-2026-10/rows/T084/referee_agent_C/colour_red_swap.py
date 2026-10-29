"""python colour_red_swap.py V m seed cnt. S, colouring form. Bad: v~w red, not blue. Map: swap colours on the edges inside C = red component of v, w.
Image is always good? level change? collisions?"""
import sys, random, itertools
from collections import Counter, defaultdict

from e1_swap import comps
V, m, seed, cnt = map(int, sys.argv[1:5])
rnd = random.Random(seed)
st = Counter()
for t in range(cnt):
    H = [tuple(sorted(rnd.sample(range(V), 2))) for _ in range(m)]
    cfg = {}
    for mask in range(1 << m):
        kr, fr = comps(V, [H[j] for j in range(m) if mask >> j & 1])
        kb, fb = comps(V, [H[j] for j in range(m) if not mask >> j & 1])
        cfg[mask] = (kr + kb, [fr(x) for x in range(V)], [fb(x) for x in range(V)])
    for u, v, w in itertools.permutations(range(V), 3):
        img = defaultdict(int)
        for mask, (k, r, b) in cfg.items():
            if r[u] == r[v] or r[u] == r[w] or b[u] != b[v]: continue
            if not (r[v] == r[w] and b[v] != b[w]): continue
            C = {x for x in range(V) if r[x] == r[v]}
            inside = sum(1 << j for j in range(m) if H[j][0] in C and H[j][1] in C)
            m2 = mask ^ inside
            k2, r2, b2 = cfg[m2]
            good = not (r2[u] == r2[v] or r2[u] == r2[w] or b2[u] != b2[v]) and b2[v] == b2[w] and r2[v] != r2[w]
            st['image good' if good else 'image NOT good'] += 1
            st['level %+d' % (k2 - k)] += 1
            img[(m2, k2 - k)] += 1
        st['collisions'] += sum(c - 1 for c in img.values())
print(V, m, seed, dict(st))
