"""python colour_cut_match.py V m seed cnt. delta=+1 -> delta=-1 one level up, allowed changes: (A) only cut(W) edges red->blue; (B) any change on edges
touching W (cut(W) and inside W). Maximum matching per level."""
import sys, random
from collections import defaultdict, Counter
import networkx as nx

from e1_swap import comps
V, m, seed, cnt = map(int, sys.argv[1:5])
rnd = random.Random(seed)
res = Counter()
def info(H, fi, u, v, w, mask):
    red = [H[j] for j in range(m) if mask >> j & 1]
    blue = [H[j] for j in range(m) if not mask >> j & 1]
    kr, fr = comps(V, red)
    if fr(u) == fr(v): return None
    kb, fb = comps(V, blue)
    if fb(u) != fb(v) or mask >> fi & 1 or fr(w) == fr(u): return None
    kb2, fb2 = comps(V, [H[j] for j in range(m) if not mask >> j & 1 and j != fi])
    if fb2(u) != fb2(v): return None
    return (kb2 - kb) - (1 if fr(v) != fr(w) else 0), kr + kb, fb2
for t in range(cnt):
    H = [tuple(sorted(rnd.sample(range(V), 2))) for _ in range(m)]
    for fi in range(m):
        for v, w in (H[fi], H[fi][::-1]):
            for u in range(V):
                if u in (v, w): continue
                P = defaultdict(list); M = defaultdict(list)
                for mask in range(1 << m):
                    r = info(H, fi, u, v, w, mask)
                    if not r: continue
                    if r[0] == 1:
                        Ws = {x for x in range(V) if r[2](x) == r[2](w)}
                        cut = sum(1 << j for j in range(m) if j != fi and (H[j][0] in Ws) != (H[j][1] in Ws))
                        touch = sum(1 << j for j in range(m) if j != fi and (H[j][0] in Ws or H[j][1] in Ws))
                        P[r[1]].append((mask, cut, touch))
                    elif r[0] == -1:
                        M[r[1]].append(mask)
                if not P: continue
                for name in 'AB':
                    miss = 0
                    for k, ps in P.items():
                        G = nx.Graph(); G.add_nodes_from(('p', a) for a, _, _ in ps)
                        for a, cut, touch in ps:
                            for b in M.get(k + 1, []):
                                diff = a ^ b
                                ok = (diff & ~cut) == 0 and (b & diff) == 0 if name == 'A' else (diff & ~touch) == 0
                                if ok: G.add_edge(('p', a), ('m', b))
                        mt = nx.bipartite.hopcroft_karp_matching(G, top_nodes=[('p', a) for a, _, _ in ps])
                        miss += len(ps) - sum(1 for x in mt if x[0] == 'p')
                    res[name + ' cases'] += 1
                    res[name + ' cases short'] += miss > 0
                    res[name + ' unmatched'] += miss
print(V, m, seed, dict(res))
