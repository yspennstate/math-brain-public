"""Disjoint pairs, separate edge weights: monomial-wise positivity fails (bern_multivariate.jsonl). Does Bernstein positivity
still hold for every fixed positive weight VECTOR? Evaluate b_j(lam_vec) exactly (Fractions) for random weight vectors drawn
from {1/100, 1/10, 1, 10, 100} per edge, at the common degree d and at elevation 2."""
import itertools, json, random
from fractions import Fraction
from math import comb
from bern_general import comps


def Npoly(n, edges, e, f):
    m = len(edges); Z, Ze, Zf, Zef = [], [], [], []
    for mask in range(1 << m):
        k = comps(n, edges, mask)
        Z.append((mask, k))
        if mask >> e & 1: Ze.append((mask, k))
        if mask >> f & 1: Zf.append((mask, k))
        if mask >> e & 1 and mask >> f & 1: Zef.append((mask, k))
    return m, Z, Ze, Zf, Zef


def bcoefs(n, edges, e, f, lam, elev, cache={}):
    key = (n, tuple(edges), e, f)
    if key not in cache: cache[key] = Npoly(n, edges, e, f)
    m, Z, Ze, Zf, Zef = cache[key]
    def zpoly(L):  # u-polynomial sum_A w(A) (1-u)^k as dict over k
        out = {}
        for mask, k in L:
            w = Fraction(1)
            for g in range(m):
                if mask >> g & 1: w *= lam[g]
            out[k] = out.get(k, 0) + w
        return out
    def mul(P, Q):
        o = {}
        for a, x in P.items():
            for b, y in Q.items(): o[a + b] = o.get(a + b, 0) + x * y
        return o
    P = mul(zpoly(Ze), zpoly(Zf)); Q = mul(zpoly(Z), zpoly(Zef))
    qk = {k: P.get(k, 0) - Q.get(k, 0) for k in set(P) | set(Q)}
    uu = {}
    for kk, c in qk.items():
        for j in range(kk + 1): uu[j] = uu.get(j, 0) + c * comb(kk, j) * (-1) ** j
    uu = {j: c for j, c in uu.items() if c}
    r = min(uu); d = max(uu) - r + elev; a = {j - r: c for j, c in uu.items()}
    return [sum(Fraction(comb(j, k), comb(d, k)) * a[k] for k in a if k <= j) for j in range(d + 1)]


if __name__ == "__main__":
    K4 = list(itertools.combinations(range(4), 2)); K5 = list(itertools.combinations(range(5), 2))
    K33 = [(i, j) for i in range(3) for j in range(3, 6)]
    vals = [Fraction(1, 100), Fraction(1, 10), Fraction(1), Fraction(10), Fraction(100)]
    rng = random.Random(3)
    for name, n, E, e, f, T in (("K4 dis", 4, K4, 0, 5, 300), ("K5 dis", 5, K5, 0, 7, 60), ("K33 dis", 6, K33, 0, 4, 60),
                                ("K4 adj", 4, K4, 0, 1, 300), ("K5 adj", 5, K5, 0, 1, 60)):
        out = {"graph": name, "trials": T}
        for el in (0, 2):
            bad = 0; ex = None
            for t in range(T):
                lam = [rng.choice(vals) for _ in E]
                b = bcoefs(n, E, e, f, lam, el)
                if min(b) < 0:
                    bad += 1; ex = ex or ([str(x) for x in lam], b.index(min(b)), float(min(b)))
            out["elev%d_negative_vectors" % el] = bad; out["elev%d_example" % el] = ex
        print(json.dumps(out), flush=True)
