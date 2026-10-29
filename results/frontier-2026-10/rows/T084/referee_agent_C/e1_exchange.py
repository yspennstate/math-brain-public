"""Does E1 follow from an exchange matching? Bad pairs (X, Y) have f in X - Y; a move sends one to a good pair
with the same |X|+|Y| and k(X)+k(Y): either (X - f, Y + f) ('plain') or (X - f + s, Y + f - s) for s in Y - X
('trade'). This script asks whether a matching saturates every bad pair, row by row (Hopcroft-Karp).
python e1_exchange.py kn n adj|dis | rand V seed cnt lo hi"""
import sys, itertools, random
from collections import defaultdict
import networkx as nx
from e1_swap import comps


def run(n, E, e, f, trades=True):
    rest = [x for x in E if x != e]
    u, v = e
    info = {}
    for mask in range(1 << len(rest)):
        S = frozenset(rest[j] for j in range(len(rest)) if mask >> j & 1)
        k, find = comps(n, S)
        info[S] = (k, find(u) == find(v))
    sep = [S for S in info if not info[S][1]]
    con = [S for S in info if info[S][1]]
    bad = [(X, Y) for X in sep if f in X for Y in con if f not in Y]
    short = 0
    rows = defaultdict(list)
    for X, Y in bad:
        rows[(len(X) + len(Y), info[X][0] + info[Y][0])].append((X, Y))
    for key, bs in rows.items():
        G = nx.Graph()
        G.add_nodes_from(('b', p) for p in bs)
        for X, Y in bs:
            kt = info[X][0] + info[Y][0]
            cands = [(X - {f}, Y | {f})]
            if trades:
                cands += [((X - {f}) | {s}, (Y | {f}) - {s}) for s in Y - X]
            for X2, Y2 in cands:
                if not info[X2][1] and info[Y2][1] and info[X2][0] + info[Y2][0] == kt:
                    G.add_edge(('b', (X, Y)), ('g', (X2, Y2)))
        M = nx.bipartite.hopcroft_karp_matching(G, [('b', p) for p in bs])
        short += sum(1 for p in bs if ('b', p) not in M)
    return len(bad), short


if __name__ == '__main__':
    if sys.argv[1] == 'kn':
        n, kind = int(sys.argv[2]), sys.argv[3]
        E = list(itertools.combinations(range(n), 2))
        f = (1, 2) if kind == 'adj' else (2, 3)
        for tr in (False, True):
            b, s = run(n, E, (0, 1), f, tr)
            print('K_%d %s %s: bad pairs %d, unmatched %d' % (n, kind, 'plain+trade' if tr else 'plain', b, s), flush=True)
    else:
        V, seed, cnt, lo, hi = map(int, sys.argv[2:7])
        rnd = random.Random(seed)
        allE = list(itertools.combinations(range(V), 2))
        pairs = fails = 0
        for t in range(cnt):
            E = sorted(rnd.sample(allE, rnd.randint(lo, hi)))
            for e, f in itertools.permutations(E, 2):
                b, s = run(V, E, e, f)
                pairs += 1
                fails += s > 0
        print('%d random graphs on %d vertices (seed %d): ordered pairs %d, pairs with an unmatched bad pair %d'
              % (cnt, V, seed, pairs, fails), flush=True)
