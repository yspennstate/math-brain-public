"""Adjacent colouring form (README, flip-of-f split). Is there an injection from the delta = +1 colourings at total k
into the delta = -1 colourings at total k + 1 that recolours at most d edges other than f? Maximum bipartite matching
per case. python colour_pm_match.py V m seed cnt d"""
import sys, random
from collections import defaultdict
import networkx as nx
from e1_swap import comps

V, m, seed, cnt, d = map(int, sys.argv[1:6])
rnd = random.Random(seed)
cases = short = unmatched = total = 0
ex = None
for t in range(cnt):
    H = [tuple(sorted(rnd.sample(range(V), 2))) for _ in range(m)]
    for fi in range(m):
        for v, w in (H[fi], H[fi][::-1]):
            for u in range(V):
                if u in (v, w):
                    continue
                P = defaultdict(list); M = defaultdict(list)
                for mask in range(1 << m):
                    if mask >> fi & 1:
                        continue
                    red = [H[j] for j in range(m) if mask >> j & 1]
                    blue = [H[j] for j in range(m) if not mask >> j & 1]
                    kr, fr = comps(V, red)
                    if fr(u) == fr(v):
                        continue
                    kb, fb = comps(V, blue)
                    if fb(u) != fb(v) or fr(w) == fr(u):
                        continue
                    kb2, fb2 = comps(V, [H[j] for j in range(m) if not mask >> j & 1 and j != fi])
                    if fb2(u) != fb2(v):
                        continue
                    dl = (kb2 - kb) - (1 if fr(v) != fr(w) else 0)
                    if dl == 1:
                        P[kr + kb].append(mask)
                    elif dl == -1:
                        M[kr + kb].append(mask)
                if not P:
                    continue
                cases += 1
                miss = 0
                for k, ps in P.items():
                    G = nx.Graph()
                    G.add_nodes_from(('p', a) for a in ps)
                    for a in ps:
                        for b in M.get(k + 1, []):
                            if bin(a ^ b).count('1') <= d:
                                G.add_edge(('p', a), ('m', b))
                    mt = nx.bipartite.hopcroft_karp_matching(G, top_nodes=[('p', a) for a in ps])
                    miss += len(ps) - sum(1 for x in mt if x[0] == 'p')
                    total += len(ps)
                if miss:
                    short += 1
                    unmatched += miss
                    if ex is None:
                        ex = (H, (v, w), u)
print('V %d m %d seed %d d %d: cases with delta=+1 colourings %d, %d colourings in all; cases with an unmatched one %d, '
      'unmatched %d' % (V, m, seed, d, cases, total, short, unmatched))
if ex:
    print('first case with an unmatched colouring:', ex)
