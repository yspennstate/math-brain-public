"""Multivariate Bernstein positivity: separate weight lam_g per edge. N = Z_e Z_f - Z Z_ef as a polynomial in (lam_1..lam_m, u);
for every lam-monomial (exponent vector) the u-polynomial divided by u^r (r = global order at u = 0) is written in the
Bernstein basis of one common degree d; count negative coefficients."""
import sys, json, itertools
from fractions import Fraction
from math import comb
from bern_general import comps


def run(n, edges, e, f, elev=0):
    m = len(edges); Z, Ze, Zf, Zef = {}, {}, {}, {}
    for mask in range(1 << m):
        k = comps(n, edges, mask)
        for D, cond in ((Z, True), (Ze, mask >> e & 1), (Zf, mask >> f & 1), (Zef, mask >> e & 1 and mask >> f & 1)):
            if cond: D[(mask, k)] = 1
    def prod(A, B):
        out = {}
        for (ma, ka) in A:
            for (mb, kb) in B:
                key = tuple(((ma >> g) & 1) + ((mb >> g) & 1) for g in range(m))
                d = out.setdefault(key, {}); d[ka + kb] = d.get(ka + kb, 0) + 1
        return out
    P1, P2 = prod(Ze, Zf), prod(Z, Zef); N = {}
    for key in set(P1) | set(P2):
        qk = dict(P1.get(key, {}))
        for kk, c in P2.get(key, {}).items(): qk[kk] = qk.get(kk, 0) - c
        uu = {}
        for kk, c in qk.items():
            for j in range(kk + 1): uu[j] = uu.get(j, 0) + c * comb(kk, j) * (-1) ** j
        uu = {j: c for j, c in uu.items() if c}
        if uu: N[key] = uu
    if not N: return None
    r = min(min(u) for u in N.values()); d = max(max(u) for u in N.values()) - r + elev
    neg = 0; worst = None
    for key, uu in N.items():
        a = {j - r: c for j, c in uu.items()}
        for j in range(d + 1):
            bj = sum(Fraction(comb(j, k), comb(d, k)) * a[k] for k in a if k <= j)
            if bj < 0:
                neg += 1
                if worst is None: worst = (key, j, float(bj))
    return {"monomials": len(N), "r": r, "d": d, "negative": neg, "example": worst}


if __name__ == "__main__":
    tests = [("K4 adj", 4, list(itertools.combinations(range(4), 2)), 0, 1), ("K4 dis", 4, list(itertools.combinations(range(4), 2)), 0, 5),
             ("C4+chord adj", 4, [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)], 0, 1), ("C4 opposite", 4, [(0, 1), (1, 2), (2, 3), (3, 0)], 0, 2),
             ("K5 adj", 5, list(itertools.combinations(range(5), 2)), 0, 1), ("K5 dis", 5, list(itertools.combinations(range(5), 2)), 0, 7),
             ("K33", 6, [(i, j) for i in range(3) for j in range(3, 6)], 0, 4)]
    for name, n, E, e, f in tests:
        print(json.dumps({"graph": name, "e": E[e], "f": E[f], **run(n, E, e, f)}), flush=True)
