"""E2, a sharper form of E1 suggested by e1_types.py on K_5. In the separating/connecting form (README), with
G = #{f in Y - X} and B = #{f in X - Y} at fixed |X|+|Y| and k(X)+k(Y), let Gx count the pairs in G with f pivotal:
X + f connects u and v, or Y - f does not. Gx <= G, so Gx >= B at every (size, k) implies E1.
python e2_check.py kn n adj|dis   |   python e2_check.py rand V seed count lo hi"""
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
    T = defaultdict(lambda: [0, 0, 0])  # G, B, Gx
    for X in sep:
        sx, kx, _ = info[X]
        for Y in con:
            sy, ky, _ = info[Y]
            key = (sx + sy, kx + ky)
            if f in Y and f not in X:
                T[key][0] += 1
                if info[X | {f}][2] or not info[Y - {f}][2]:
                    T[key][2] += 1
            elif f in X and f not in Y:
                T[key][1] += 1
    return T


def fails(T):
    e1 = [(k, t) for k, t in T.items() if t[0] < t[1]]
    e2 = [(k, t) for k, t in T.items() if t[2] < t[1]]
    return e1, e2


if __name__ == '__main__':
    if sys.argv[1] == 'kn':
        n, kind = int(sys.argv[2]), sys.argv[3]
        E = list(itertools.combinations(range(n), 2))
        e, f = (0, 1), ((1, 2) if kind == 'adj' else (2, 3))
        e1, e2 = fails(table(n, E, e, f))
        print('K_%d %s: E1 failures %d, E2 failures %d' % (n, kind, len(e1), len(e2)), sorted(e2)[:4], flush=True)
    else:
        V, seed, cnt, lo, hi = map(int, sys.argv[2:7])
        rnd = random.Random(seed)
        allE = list(itertools.combinations(range(V), 2))
        pairs = b1 = b2 = 0
        for t in range(cnt):
            E = sorted(rnd.sample(allE, rnd.randint(lo, hi)))
            for e, f in itertools.permutations(E, 2):
                e1, e2 = fails(table(V, E, e, f))
                pairs += 1
                b1 += bool(e1)
                if e2:
                    b2 += 1
                    if b2 <= 4:
                        print('E2 FAIL', E, e, f, sorted(e2)[:3], flush=True)
        print('%d random graphs on %d vertices (seed %d, %d..%d edges): ordered pairs %d, E1 failures %d, E2 failures %d'
              % (cnt, V, seed, lo, hi, pairs, b1, b2), flush=True)
