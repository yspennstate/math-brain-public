"""Hall test (added 07:4x 18 Oct): can a level-preserving injection of the leftover bad colourings into good colourings be made of
vertex-set swaps (recolour every edge inside some vertex set)? Prints matched counts and one colouring with no such swap.
Is the block-path swap an involution between bad and good? phi(bad) swaps on P_red(v,w); psi(good) swaps on P_blue(v,w).
Counts bad colourings with psi(phi(x)) == x, by shift; and whether the involution-closed part is level-preserving."""
import sys, random, itertools
from collections import Counter, defaultdict
sys.path.insert(0, '.')
from e1_swap import comps
exec(open(r'colour_blockpath_swap.py').read().split('V, m, seed')[0].split('from e1_swap import comps')[1])
V, m, seed, cnt = map(int, sys.argv[1:5]); rnd = random.Random(seed); st = Counter()
for t in range(cnt):
    H = [tuple(sorted(rnd.sample(range(V), 2))) for _ in range(m)]
    cfg = {}
    for mask in range(1 << m):
        kr, fr = comps(V, [H[j] for j in range(m) if mask >> j & 1]); kb, fb = comps(V, [H[j] for j in range(m) if not mask >> j & 1])
        cfg[mask] = (kr + kb, [fr(x) for x in range(V)], [fb(x) for x in range(V)])
    def sw(mask, P): return mask ^ sum(1 << j for j in range(m) if H[j][0] in P and H[j][1] in P)
    for u, v, w in itertools.permutations(range(V), 3):
        bad, good = [], set()
        for mask, (k, r, b) in cfg.items():
            if r[u] == r[v] or r[u] == r[w] or b[u] != b[v]: continue
            if r[v] == r[w] and b[v] != b[w]: bad.append(mask)
            if b[v] == b[w] and r[v] != r[w]: good.add(mask)
        inv_img = set(); rest = []
        for mask in bad:
            m2 = sw(mask, onpath(V, [H[j] for j in range(m) if mask >> j & 1], v, w))
            m3 = sw(m2, onpath(V, [H[j] for j in range(m) if not m2 >> j & 1], v, w))
            if m3 == mask: inv_img.add(m2); st['inv shift %d' % (cfg[m2][0] - cfg[mask][0])] += 1
            else: rest.append((mask, m2))
        # Hall test: can EVERY remaining bad colouring go, injectively and level-preserving, to a leftover good colouring
        # obtained by swapping colours on SOME vertex set (any of the 2^V sets)? Max bipartite matching (Kuhn).
        left = good - inv_img
        adj = {}
        for mask, _ in rest:
            k = cfg[mask][0]
            adj[mask] = sorted({sw(mask, {x for x in range(V) if S >> x & 1}) for S in range(1 << V)} & {g for g in left if cfg[g][0] == k})
        match = {}
        def aug(x, seen):
            for g in adj[x]:
                if g in seen: continue
                seen.add(g)
                if g not in match or aug(match[g], seen): match[g] = x; return True
            return False
        got = sum(aug(x, set()) for x, _ in rest)
        st['rest'] += len(rest); st['matched by some vertex-set swap'] += got
        st['rest with no swap candidate at all'] += sum(1 for x, _ in rest if not adj[x])
        st['rest with no swap into ANY good at its level'] += sum(1 for x, _ in rest if not ({sw(x, {y for y in range(V) if S >> y & 1}) for S in range(1 << V)} & {g for g in good if cfg[g][0] == cfg[x][0]}))
        for x, _ in rest:
            if 'example' not in st and not ({sw(x, {y for y in range(V) if S >> y & 1}) for S in range(1 << V)} & {g for g in good if cfg[g][0] == cfg[x][0]}):
                st['example'] = dict(H=H, uvw=(u, v, w), red=[H[j] for j in range(m) if x >> j & 1], blue=[H[j] for j in range(m) if not x >> j & 1], level=cfg[x][0], good_at_level=sum(1 for g in good if cfg[g][0] == cfg[x][0]))
print(V, m, seed, dict(st))
