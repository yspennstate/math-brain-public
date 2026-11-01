"""Which refinements of E1 hold? E1 compares, at fixed |X|+|Y| and k(X)+k(Y), good pairs (f in Y - X) with bad
pairs (f in X - Y), X separating u from v and Y connecting them. R1 also fixes |X| (hence |Y|); R2 fixes k(X) instead;
R3 fixes all four. python e1_refine.py kn n adj|dis | rand V seed cnt lo hi"""
import sys, itertools, random
from collections import defaultdict
from e1_swap import comps

KEYS = {'E1': lambda a, b, c, d: (a + c, b + d), 'R1': lambda a, b, c, d: (a, c, b + d),
        'R2': lambda a, b, c, d: (a + c, b, d), 'R3': lambda a, b, c, d: (a, b, c, d)}


def fails(n, E, e, f):
    rest = [x for x in E if x != e]
    u, v = e
    sep, con = [], []
    for mask in range(1 << len(rest)):
        S = frozenset(rest[j] for j in range(len(rest)) if mask >> j & 1)
        k, find = comps(n, S)
        (con if find(u) == find(v) else sep).append((S, len(S), k))
    T = {name: defaultdict(int) for name in KEYS}
    for X, sx, kx in sep:
        for Y, sy, ky in con:
            if (f in X) == (f in Y):
                continue
            d = 1 if f in Y else -1
            for name, key in KEYS.items():
                T[name][key(sx, kx, sy, ky)] += d
    return {name: sum(1 for c in t.values() if c < 0) for name, t in T.items()}


if __name__ == '__main__':
    if sys.argv[1] == 'kn':
        n, kind = int(sys.argv[2]), sys.argv[3]
        E = list(itertools.combinations(range(n), 2))
        print('K_%d %s: negative rows %s' % (n, kind, fails(n, E, (0, 1), (1, 2) if kind == 'adj' else (2, 3))),
              flush=True)
    else:
        V, seed, cnt, lo, hi = map(int, sys.argv[2:7])
        rnd = random.Random(seed)
        allE = list(itertools.combinations(range(V), 2))
        bad = defaultdict(int)
        pairs = 0
        for t in range(cnt):
            E = sorted(rnd.sample(allE, rnd.randint(lo, hi)))
            for e, f in itertools.permutations(E, 2):
                pairs += 1
                for name, c in fails(V, E, e, f).items():
                    bad[name] += c > 0
        print('%d random graphs on %d vertices (seed %d): ordered pairs %d, pairs with a negative row %s'
              % (cnt, V, seed, pairs, dict(bad)), flush=True)
