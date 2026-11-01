"""The dangling-side swap for E1 (README). For (X, Y) as in e1_reduce.py with f in exactly one of them, remove f from
X + Y; if the cluster D of an endpoint of f misses both u and v, swap X and Y on the edges inside D and on f. f is the
only edge of X + Y joining D to the rest, so the swap keeps |X|+|Y|, k(X)+k(Y), X separating and Y connecting, and moves
f to the other side; X + Y and D are unchanged, so it is an involution (take the endpoint with the smaller label when both
sides qualify). Checks: the dangling counts cancel row by row, and E1 holds on the rest, where both ends of f reach
{u, v} without f. python e1_reduce2.py kn n adj|dis | rand V seed cnt lo hi"""
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
    T = defaultdict(lambda: [0, 0, 0, 0])  # G_rest, B_rest, G_dangling, B_dangling
    for X in sep:
        sx, kx, _ = info[X]
        for Y in con:
            sy, ky, _ = info[Y]
            if (f in X) == (f in Y):
                continue
            _, find = comps(n, (X | Y) - {f})
            dang = any(find(w) not in (find(u), find(v)) for w in f)
            j = (0 if f in Y else 1) + (2 if dang else 0)
            T[(sx + sy, kx + ky)][j] += 1
    return T


def check(T):
    return [k for k, t in T.items() if t[2] != t[3]], [k for k, t in T.items() if t[0] < t[1]]


if __name__ == '__main__':
    if sys.argv[1] == 'kn':
        n, kind = int(sys.argv[2]), sys.argv[3]
        E = list(itertools.combinations(range(n), 2))
        T = table(n, E, (0, 1), (1, 2) if kind == 'adj' else (2, 3))
        c, b = check(T)
        tot = [sum(t[j] for t in T.values()) for j in range(4)]
        print('K_%d %s: rows %d, cancellation fails %d, E1-rest fails %d; totals G_rest B_rest G_dang B_dang %s'
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
              'E1-rest fails %d' % (cnt, V, seed, lo, hi, pairs, cf, ef), flush=True)
