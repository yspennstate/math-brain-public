"""Adjacent pairs: within each fixed edge multiset and cluster total, can every bad pair (f in X - Y) be matched to
a good pair by sending f to Y, alone or with one other single-copy edge s sent either way (X->Y or Y->X)?
python e1_adj_match.py kn n | rand V seed cnt lo hi"""
import sys, itertools, random
from collections import defaultdict
import networkx as nx
from e1_swap import comps


def unmatched(n, E, e, f):
    rest = [x for x in E if x != e]
    u, v = e
    info = {}
    for mask in range(1 << len(rest)):
        k, find = comps(n, [rest[j] for j in range(len(rest)) if mask >> j & 1])
        info[mask] = (k, find(u) == find(v))
    fb = 1 << rest.index(f)
    bits = [1 << j for j in range(len(rest))]
    rows = defaultdict(list)
    for X in info:
        if info[X][1] or not X & fb:
            continue
        for Y in info:
            if info[Y][1] and not Y & fb:
                rows[(X & Y, X ^ Y, info[X][0] + info[Y][0])].append((X, Y))
    left = 0
    for key, bs in rows.items():
        G = nx.Graph()
        G.add_nodes_from(('b', p) for p in bs)
        for X, Y in bs:
            X0, Y0 = X ^ fb, Y | fb
            cands = [(X0, Y0)]
            for b in bits:
                if b == fb:
                    continue
                if X0 & b and not Y0 & b:
                    cands.append((X0 ^ b, Y0 | b))
                if Y0 & b and not X0 & b:
                    cands.append((X0 | b, Y0 ^ b))
            for X2, Y2 in cands:
                if not info[X2][1] and info[Y2][1] and info[X2][0] + info[Y2][0] == key[2]:
                    G.add_edge(('b', (X, Y)), ('g', (X2, Y2)))
        M = nx.bipartite.hopcroft_karp_matching(G, [('b', p) for p in bs])
        left += sum(1 for p in bs if ('b', p) not in M)
    return left


if __name__ == '__main__':
    if sys.argv[1] == 'kn':
        n = int(sys.argv[2])
        print('K_%d adjacent: unmatched bad pairs %d' % (n, unmatched(n, list(itertools.combinations(range(n), 2)), (0, 1), (1, 2))), flush=True)
    else:
        V, seed, cnt, lo, hi = map(int, sys.argv[2:7])
        rnd = random.Random(seed)
        allE = list(itertools.combinations(range(V), 2))
        pairs = fails = 0
        for t in range(cnt):
            E = sorted(rnd.sample(allE, rnd.randint(lo, hi)))
            for e, f in itertools.permutations(E, 2):
                if set(e) & set(f):
                    pairs += 1
                    fails += unmatched(V, E, e, f) > 0
        print('%d random graphs on %d vertices (seed %d): adjacent pairs %d, with an unmatched bad pair %d' % (cnt, V, seed, pairs, fails), flush=True)
