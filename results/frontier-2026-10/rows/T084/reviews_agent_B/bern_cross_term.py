"""Deletion-contraction cross term on edge g (g not e, f): N_G = N_{G-g} + lam_g X + lam_g^2 N_{G/g},
X = Ze(G-g) Zf(G/g) + Ze(G/g) Zf(G-g) - Z(G-g) Zef(G/g) - Z(G/g) Zef(G-g). Z(G/g) = sum over A containing g of
lam^(A-g) q^k(A). Is X Bernstein-nonnegative in u (fixed weight vector, its own native degree)? If yes, induction closes."""
import itertools, json, random
from fractions import Fraction
from math import comb
from bern_general import comps


def polys(n, E, lam, e, f, g):
    m = len(E); D = {k: {} for k in ("Z", "Ze", "Zf", "Zef")}; C = {k: {} for k in D}
    for mask in range(1 << m):
        k = comps(n, E, mask); w = Fraction(1)
        for h in range(m):
            if h != g and mask >> h & 1: w *= lam[h]
        T = D if not mask >> g & 1 else C
        for name, cond in (("Z", 1), ("Ze", mask >> e & 1), ("Zf", mask >> f & 1), ("Zef", mask >> e & 1 and mask >> f & 1)):
            if cond: T[name][k] = T[name].get(k, 0) + w
    return D, C


def mul(P, Q):
    o = {}
    for a, x in P.items():
        for b, y in Q.items(): o[a + b] = o.get(a + b, 0) + x * y
    return o


def bern(qk):
    uu = {}
    for kk, c in qk.items():
        for j in range(kk + 1): uu[j] = uu.get(j, 0) + c * comb(kk, j) * (-1) ** j
    uu = {j: c for j, c in uu.items() if c}
    if not uu: return None
    r = min(uu); d = max(uu) - r; a = {j - r: c for j, c in uu.items()}
    return [sum(Fraction(comb(j, k), comb(d, k)) * a[k] for k in a if k <= j) for j in range(d + 1)]


def cross(n, E, lam, e, f, g):
    D, C = polys(n, E, lam, e, f, g)
    X = {}
    for P, s in ((mul(D["Ze"], C["Zf"]), 1), (mul(C["Ze"], D["Zf"]), 1), (mul(D["Z"], C["Zef"]), -1), (mul(C["Z"], D["Zef"]), -1)):
        for k, c in P.items(): X[k] = X.get(k, 0) + s * c
    return bern(X)


if __name__ == "__main__":
    rng = random.Random(4); vals = [Fraction(1, 100), Fraction(1), Fraction(100)]
    K4 = list(itertools.combinations(range(4), 2)); K5 = list(itertools.combinations(range(5), 2))
    for name, n, E, e, f in (("K4 adj", 4, K4, 0, 1), ("K4 dis", 4, K4, 0, 5), ("K5 adj", 5, K5, 0, 1), ("K5 dis", 5, K5, 0, 7)):
        tot = bad = 0; ex = None
        for g in range(len(E)):
            if g in (e, f): continue
            for t in range(6):
                lam = [Fraction(1)] * len(E) if t == 0 else [rng.choice(vals) for _ in E]
                b = cross(n, E, lam, e, f, g)
                if b is None: continue
                tot += 1
                if min(b) < 0:
                    bad += 1; ex = ex or {"g": E[g], "equal_weights": t == 0, "j": b.index(min(b)), "val": float(min(b))}
        print(json.dumps({"graph": name, "checks": tot, "X_negative": bad, "example": ex}), flush=True)
