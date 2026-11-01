"""Bernstein-in-u positivity of N/u^r (N = Z_e Z_f - Z Z_ef, RC weights lam^|A| q^k, u = 1 - q) on general small graphs, by
enumeration. For each random graph and edge pair with N != 0: r = order of vanishing at u = 0, then the Bernstein coefficients
b_j(lam) of N/u^r on [0,1]; count pairs with a negative lam-coefficient, and pairs where N itself is negative somewhere."""
import sys, random, json, itertools
from fractions import Fraction
from math import comb


def comps(n, edges, mask):
    p = list(range(n)); k = n
    def f(x):
        while p[x] != x: p[x] = p[p[x]]; x = p[x]
        return x
    for i, (a, b) in enumerate(edges):
        if mask >> i & 1:
            ra, rb = f(a), f(b)
            if ra != rb: p[ra] = rb; k -= 1
    return k


def polys(n, edges, e, f):
    m = len(edges); Z, Ze, Zf, Zef = {}, {}, {}, {}
    for mask in range(1 << m):
        key = (bin(mask).count("1"), comps(n, edges, mask))
        Z[key] = Z.get(key, 0) + 1
        ie, jf = mask >> e & 1, mask >> f & 1
        if ie: Ze[key] = Ze.get(key, 0) + 1
        if jf: Zf[key] = Zf.get(key, 0) + 1
        if ie and jf: Zef[key] = Zef.get(key, 0) + 1
    return Z, Ze, Zf, Zef


def to_lam_u(P, n):  # sum c lam^i q^k, q = 1 - u  ->  {(i, j): coeff of lam^i u^j}
    out = {}
    for (i, k), c in P.items():
        for j in range(k + 1):
            out[(i, j)] = out.get((i, j), 0) + c * comb(k, j) * (-1) ** j
    return out


def mul(A, B):
    out = {}
    for (i1, j1), c1 in A.items():
        for (i2, j2), c2 in B.items():
            out[(i1 + i2, j1 + j2)] = out.get((i1 + i2, j1 + j2), 0) + c1 * c2
    return out


def numerator(n, edges, e, f):
    Z, Ze, Zf, Zef = (to_lam_u(P, n) for P in polys(n, edges, e, f))
    N = mul(Ze, Zf)
    for k, c in mul(Z, Zef).items(): N[k] = N.get(k, 0) - c
    return {k: c for k, c in N.items() if c}


def bernstein_neg(N):
    r = min(j for (i, j) in N); a = {}
    for (i, j), c in N.items(): a.setdefault(j - r, {})[i] = c
    d = max(a); neg = 0
    for j in range(d + 1):
        bj = {}
        for k in range(j + 1):
            if k in a:
                fr = Fraction(comb(j, k), comb(d, k))
                for i, c in a[k].items(): bj[i] = bj.get(i, 0) + fr * c
        neg += sum(1 for c in bj.values() if c < 0)
    return r, d, neg


def N_min(N, grid=12):
    lo = None
    for x in range(1, grid + 1):
        lam = Fraction(x, 3) ** 2 / 4
        for y in range(1, grid):
            u = Fraction(y, grid); v = sum(c * lam ** i * u ** j for (i, j), c in N.items())
            if lo is None or v < lo: lo = v
    return lo


if __name__ == "__main__":
    rng = random.Random(int(sys.argv[1])); n = int(sys.argv[2]); trials = int(sys.argv[3])
    tot = bneg = nneg = 0; ex = []
    for _ in range(trials):
        allE = list(itertools.combinations(range(n), 2))
        edges = [x for x in allE if rng.random() < rng.uniform(0.4, 0.9)]
        if len(edges) > 13 or len(edges) < 3: continue
        for e, f in itertools.combinations(range(len(edges)), 2):
            N = numerator(n, edges, e, f)
            if not N: continue
            tot += 1; r, d, neg = bernstein_neg(N)
            if neg:
                bneg += 1; mn = N_min(N)
                if mn < 0: nneg += 1
                if len(ex) < 4: ex.append({"edges": edges, "e": edges[e], "f": edges[f], "r": r, "deg": d, "n_neg_bern": neg, "N_grid_min_sign": (mn > 0) - (mn < 0)})
    print(json.dumps({"n": n, "pairs": tot, "bernstein_negative": bneg, "N_negative_on_grid": nneg, "examples": ex}))
