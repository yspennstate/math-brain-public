"""C-swap refined: swap colours only on edges with both ends in P = vertices on some simple red v-w path."""
import sys, random, itertools
from collections import Counter, defaultdict
sys.path.insert(0, '.')
from e1_swap import comps
def onpath(V, edges, v, w):
    adj = defaultdict(set)
    for a, b in edges:
        if a != b: adj[a].add(b); adj[b].add(a)
    P = set()
    def dfs(x, seen):
        if x == w: P.update(seen); return
        for y in adj[x]:
            if y not in seen: dfs(y, seen | {y})
    dfs(v, frozenset([v]))
    return P
V, m, seed, cnt = map(int, sys.argv[1:5])
rnd = random.Random(seed); st = Counter()
for t in range(cnt):
    H = [tuple(sorted(rnd.sample(range(V), 2))) for _ in range(m)]
    cfg = {}
    for mask in range(1 << m):
        kr, fr = comps(V, [H[j] for j in range(m) if mask >> j & 1])
        kb, fb = comps(V, [H[j] for j in range(m) if not mask >> j & 1])
        cfg[mask] = (kr + kb, [fr(x) for x in range(V)], [fb(x) for x in range(V)])
    for u, v, w in itertools.permutations(range(V), 3):
        img = defaultdict(int); img0 = defaultdict(int)
        lv = Counter()
        for mask, (k, r, b) in cfg.items():
            if r[u] == r[v] or r[u] == r[w] or b[u] != b[v]: continue
            bad = r[v] == r[w] and b[v] != b[w]
            good = b[v] == b[w] and r[v] != r[w]
            if good: lv[('g', k)] += 1
            if not bad: continue
            lv[('b', k)] += 1
            P = onpath(V, [H[j] for j in range(m) if mask >> j & 1], v, w)
            inside = sum(1 << j for j in range(m) if H[j][0] in P and H[j][1] in P)
            m2 = mask ^ inside
            k2, r2, b2 = cfg[m2]
            ok = not (r2[u] == r2[v] or r2[u] == r2[w] or b2[u] != b2[v]) and b2[v] == b2[w] and r2[v] != r2[w]
            st['image good' if ok else 'image NOT good'] += 1
            st['shift %+d' % (k2 - k)] += 1
            img[m2] += 1
            if k2 == k: img0[m2] += 1
        st['collisions'] += sum(c - 1 for c in img.values())
        st['collisions among shift0'] += sum(c - 1 for c in img0.values())
print(V, m, seed, dict(st))
