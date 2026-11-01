"""The cluster swap reduction for E1 (README). For pairs (X, Y) of edge sets of G - e, X separating u, v and Y
connecting them, let W be the cluster of X + Y containing f. When W misses u (hence v), swapping X and Y on the edges
inside W keeps |X|+|Y|, k(X)+k(Y), both properties, and moves f between X - Y and Y - X: good and bad pairs cancel
there exactly. This script checks that cancellation (G_out = B_out in every (size, k) row) and that E1 holds on the
remaining pairs, those with f in the cluster of u (G_in >= B_in). python e1_reduce.py kn n adj|dis | rand V seed cnt lo hi"""
import sys, itertools, random
from collections import defaultdict
from e1_swap import comps


def table(n, E, e, f):
    rest = [x for x in E if x != e]
    u, v = e
    info = {}
    for mask in range(1 << len(rest)):
        S = frozenset(rest[j] for j in range(len(rest)) if mask >> j & 1)
        k, find = comps(n, S)
        info[S] = (len(S), k, find(u) == find(v))
    sep = [S for S in info if not info[S][2]]
    con = [S for S in info if info[S][2]]
    T = defaultdict(lambda: [0, 0, 0, 0])  # G_in, B_in, G_out, B_out
    for X in sep:
        sx, kx, _ = info[X]
        for Y in con:
            sy, ky, _ = info[Y]
            if (f in X) == (f in Y):
                continue
            _, find = comps(n, X | Y)
            inside = find(f[0]) == find(u)
            j = (0 if f in Y else 1) + (0 if inside else 2)
            T[(sx + sy, kx + ky)][j] += 1
    return T


def check(T):
    cancel_bad = [k for k, t in T.items() if t[2] != t[3]]
    e1_bad = [k for k, t in T.items() if t[0] < t[1]]
    return cancel_bad, e1_bad


if __name__ == '__main__':
    if sys.argv[1] == 'kn':
        n, kind = int(sys.argv[2]), sys.argv[3]
        E = list(itertools.combinations(range(n), 2))
        T = table(n, E, (0, 1), (1, 2) if kind == 'adj' else (2, 3))
        c, b = check(T)
        tot = [sum(t[j] for t in T.values()) for j in range(4)]
        print('K_%d %s: rows %d, cancellation fails %d, E1-in fails %d; totals G_in B_in G_out B_out %s'
              % (n, kind, len(T), len(c), len(b), tot), flush=True)
    else:
        V, seed, cnt, lo, hi = map(int, sys.argv[2:7])
        rnd = random.Random(seed)
        allE = list(itertools.combinations(range(V), 2))
        pairs = cf = ef = 0
        for t in range(cnt):
            E = sorted(rnd.sample(allE, rnd.randint(lo, hi)))
            for e, f in itertools.permutations(E, 2):
                c, b = check(table(V, E, e, f))
                pairs += 1
                cf += bool(c)
                ef += bool(b)
        print('%d random graphs on %d vertices (seed %d, %d..%d edges): ordered pairs %d, cancellation fails %d, '
              'E1-in fails %d' % (cnt, V, seed, lo, hi, pairs, cf, ef), flush=True)
