"""Bivariate E1: one edge g with its own weight, every other edge lam. Grading (copies of g in X + Y, |X|+|Y|,
k(X)+k(Y)). Reports, for each g other than e and f, whether some row has more bad than good pairs.
python e1_biv.py kn n adj|dis | rand V seed cnt lo hi"""
import sys, itertools, random
from collections import defaultdict
from e1_swap import comps


def failing_g(n, E, e, f):
    rest = [x for x in E if x != e]
    u, v = e
    sep, con = [], []
    for mask in range(1 << len(rest)):
        k, find = comps(n, [rest[j] for j in range(len(rest)) if mask >> j & 1])
        (con if find(u) == find(v) else sep).append((mask, bin(mask).count('1'), k))
    fb = 1 << rest.index(f)
    out = []
    for g in rest:
        if g == f:
            continue
        gb = 1 << rest.index(g)
        T = defaultdict(int)
        for mx, sx, kx in sep:
            for my, sy, ky in con:
                if bool(mx & fb) == bool(my & fb):
                    continue
                T[(bool(mx & gb) + bool(my & gb), sx + sy, kx + ky)] += 1 if my & fb else -1
        if any(c < 0 for c in T.values()):
            out.append(g)
    return out


if __name__ == '__main__':
    if sys.argv[1] == 'kn':
        n, kind = int(sys.argv[2]), sys.argv[3]
        E = list(itertools.combinations(range(n), 2))
        print('K_%d %s: edges g whose own weight breaks E1: %s' % (n, kind, failing_g(n, E, (0, 1), (1, 2) if kind == 'adj' else (2, 3))), flush=True)
    else:
        V, seed, cnt, lo, hi = map(int, sys.argv[2:7])
        rnd = random.Random(seed)
        allE = list(itertools.combinations(range(V), 2))
        pairs = bad = 0
        for t in range(cnt):
            E = sorted(rnd.sample(allE, rnd.randint(lo, hi)))
            for e, f in itertools.permutations(E, 2):
                pairs += 1
                bad += bool(failing_g(V, E, e, f))
        print('%d random graphs on %d vertices (seed %d): ordered pairs %d, with some g breaking E1 %d' % (cnt, V, seed, pairs, bad), flush=True)
