"""E1 as a comparison of separating/connecting pairs, checked against fastN.

With e = uv, cancelling the terms common to Z_e Z_f and Z Z_ef and pairing (X+e, Y) with (X, Y+e) gives
    N/(1-q) = lam * sum_{X, Y subset of E-e, f in Y} lam^(|X|+|Y|) q^(k(X)+k(Y)-1)
              * ([u !~ v in X, u ~ v in Y] - [u ~ v in X, u !~ v in Y]).
Swapping X and Y in the second term: E1 holds iff, among pairs (X, Y) of edge sets of G - e with X separating u
from v and Y connecting them, at every fixed |X|+|Y| and k(X)+k(Y),
    #{f in Y - X} >= #{f in X - Y}.
This script checks the identity coefficient by coefficient against fastN's N, and counts how many of the 'f in X - Y'
pairs the injection (X, Y) -> (X - f, Y + f) keeps at the same cluster total (it always keeps the size and the
separating/connecting property). python e1_swap.py V seed count lo hi"""
import sys, random, itertools
from collections import defaultdict
from math import comb
import fastN


def comps(n, E):
    par = list(range(n))

    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    k = n
    for a, b in E:
        x, y = f(a), f(b)
        if x != y:
            par[x] = y
            k -= 1
    return k, f


def e1_q(N):
    """N/(1-q) q-coefficients {(lam, q power): c} from N as {(lam, u power): c}."""
    q = defaultdict(int)
    for (i, k), c in N.items():
        for s in range(k + 1):
            q[(i, s)] += c * comb(k, s) * (-1) ** s
    out = {}
    for i in {i for i, _ in q}:
        acc = 0
        for s in range(max(s for ii, s in q if ii == i) + 1):
            acc += q.get((i, s), 0)
            if acc:
                out[(i, s)] = acc
    return out


def swap_side(n, E, e, f):
    rest = [x for x in E if x != e]
    u, v = e
    sub = []
    for mask in range(1 << len(rest)):
        S = [rest[j] for j in range(len(rest)) if mask >> j & 1]
        k, find = comps(n, S)
        sub.append((frozenset(S), len(S), k, find(u) == find(v)))
    D = defaultdict(int)
    moved = stay = 0
    sep = [s for s in sub if not s[3]]
    con = [s for s in sub if s[3]]
    idx = {s[0]: s for s in sub}
    for X, sx, kx, _ in sep:
        for Y, sy, ky, _ in con:
            key = (sx + sy + 1, kx + ky - 1)
            if f in Y:
                D[key] += 1
            if f in X:  # the swapped negative term
                D[key] -= 1
            if f in X and f not in Y:
                X2, Y2 = idx[X - {f}], idx[Y | {f}]
                if X2[2] + Y2[2] == kx + ky:
                    stay += 1
                else:
                    moved += 1
    return {k: c for k, c in D.items() if c}, stay, moved


if __name__ == '__main__':
    V, seed, T, lo, hi = map(int, sys.argv[1:6])
    rnd = random.Random(seed)
    allE = list(itertools.combinations(range(V), 2))
    agree = disagree = stay = moved = 0
    for t in range(T):
        E = sorted(rnd.sample(allE, rnd.randint(lo, hi)))
        for (e, f), N in fastN.all_N(V, E).items():
            for a, b in ((e, f), (f, e)):  # N is symmetric in e, f; check the formula from both sides
                D, s1, m1 = swap_side(V, E, a, b)
                if D == e1_q(N):
                    agree += 1
                else:
                    disagree += 1
                    if disagree <= 3:
                        print('MISMATCH', E, a, b, sorted(D.items())[:6], sorted(e1_q(N).items())[:6], flush=True)
                stay += s1
                moved += m1
    print('%d graphs on %d vertices (seed %d, %d..%d edges): identity holds %d, fails %d; '
          'f in X - Y pairs kept at the same cluster total by (X-f, Y+f): %d of %d'
          % (T, V, seed, lo, hi, agree, disagree, stay, stay + moved), flush=True)
