"""Multivariate E1: does good >= bad hold at every fixed edge multiset of X + Y (each edge weighted by its own
lam_g) and k(X)+k(Y)? python e1_multi.py kn n adj|dis | rand V seed cnt lo hi"""
import sys, itertools, random
from collections import defaultdict
from e1_swap import comps


def neg_rows(n, E, e, f):
    rest = [x for x in E if x != e]
    u, v = e
    sep, con = [], []
    for mask in range(1 << len(rest)):
        k, find = comps(n, [rest[j] for j in range(len(rest)) if mask >> j & 1])
        (con if find(u) == find(v) else sep).append((mask, k))
    fb = 1 << rest.index(f)
    T = defaultdict(int)
    for mx, kx in sep:
        for my, ky in con:
            if bool(mx & fb) == bool(my & fb):
                continue
            T[(mx & my, mx ^ my, kx + ky)] += 1 if my & fb else -1
    return sum(1 for c in T.values() if c < 0), len(T)


if __name__ == '__main__':
    if sys.argv[1] == 'kn':
        n, kind = int(sys.argv[2]), sys.argv[3]
        E = list(itertools.combinations(range(n), 2))
        print('K_%d %s: negative multiset rows %d of %d' % ((n, kind) + neg_rows(n, E, (0, 1), (1, 2) if kind == 'adj' else (2, 3))), flush=True)
    else:
        V, seed, cnt, lo, hi = map(int, sys.argv[2:7])
        rnd = random.Random(seed)
        allE = list(itertools.combinations(range(V), 2))
        pairs = bad = 0
        for t in range(cnt):
            E = sorted(rnd.sample(allE, rnd.randint(lo, hi)))
            for e, f in itertools.permutations(E, 2):
                pairs += 1
                bad += neg_rows(V, E, e, f)[0] > 0
        print('%d random graphs on %d vertices (seed %d): ordered pairs %d, with a negative multiset row %d' % (cnt, V, seed, pairs, bad), flush=True)
