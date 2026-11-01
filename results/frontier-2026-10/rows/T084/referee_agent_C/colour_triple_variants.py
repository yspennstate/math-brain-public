"""Which conditions in statement S matter? Colouring form, at fixed k(red) + k(blue), #(v~w blue not red) >= #(v~w red
not blue), under: (a) S as stated (red: u !~ v, u !~ w; blue: u ~ v); (b) red only u !~ v; (c) blue only, no red
condition; (d) red u !~ v, u !~ w, no blue condition. python colour_triple_variants.py"""
import random, itertools
from collections import defaultdict
from e1_swap import comps

conds = {
    'a S as stated': lambda r, b, u, v, w: r[u] != r[v] and r[u] != r[w] and b[u] == b[v],
    'b red only u!~v': lambda r, b, u, v, w: r[u] != r[v] and b[u] == b[v],
    'c no red condition': lambda r, b, u, v, w: b[u] == b[v],
    'd no blue condition': lambda r, b, u, v, w: r[u] != r[v] and r[u] != r[w],
}
fails = defaultdict(int); tot = 0
for V, m, seed, cnt in ((4, 7, 1, 30), (5, 8, 3, 15)):
    rnd = random.Random(seed)
    for t in range(cnt):
        H = [tuple(sorted(rnd.sample(range(V), 2))) for _ in range(m)]
        cfg = []
        for mask in range(1 << m):
            kr, fr = comps(V, [H[j] for j in range(m) if mask >> j & 1])
            kb, fb = comps(V, [H[j] for j in range(m) if not mask >> j & 1])
            cfg.append((kr + kb, [fr(x) for x in range(V)], [fb(x) for x in range(V)]))
        for u, v, w in itertools.permutations(range(V), 3):
            tot += 1
            for name, c in conds.items():
                T = defaultdict(int)
                for k, r, b in cfg:
                    if c(r, b, u, v, w) and (b[v] == b[w]) != (r[v] == r[w]):
                        T[k] += 1 if b[v] == b[w] else -1
                fails[name] += any(x < 0 for x in T.values())
for name in conds:
    print('%-22s fails %d of %d triples' % (name, fails[name], tot))
