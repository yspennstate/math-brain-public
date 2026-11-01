#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

def forest_masks(n, edges):
    out = []
    for mask in range(1 << len(edges)):
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        ok = True
        k = 0
        for i, (u, v) in enumerate(edges):
            if (mask >> i) & 1:
                ru, rv = find(u), find(v)
                if ru == rv:
                    ok = False
                    break
                parent[ru] = rv
                k += 1
        if ok:
            out.append((mask, k))
    return out

def comp_roots(n, edges, mask):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for i, (u, v) in enumerate(edges):
        if (mask >> i) & 1:
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
    return [find(i) for i in range(n)]

def boundary_stats(n, G, e, f, weights):
    H = [h for h in G if h != e and h != f]
    A = B = C = D = Q = EF = 0
    sumK = sumK2 = sumEK = sumFK = 0
    for mask, k in forest_masks(n, H):
        wt = 1
        for i, h in enumerate(H):
            if (mask >> i) & 1:
                wt *= weights[h]
        roots = comp_roots(n, H, mask)
        ae = roots[e[0]] != roots[e[1]]
        af = roots[f[0]] != roots[f[1]]
        ce = tuple(sorted((roots[e[0]], roots[e[1]])))
        cf = tuple(sorted((roots[f[0]], roots[f[1]])))
        jointly_addable = ae and af and ce != cf
        reconnects = ae and af and not jointly_addable
        A += wt
        B += wt * ae
        C += wt * af
        D += wt * jointly_addable
        Q += wt * reconnects
        EF += wt * (ae and af)
        sumK += wt * k
        sumK2 += wt * k * k
        sumEK += wt * k * ae
        sumFK += wt * k * af

    mu = Fraction(sumK, A)
    varK = Fraction(sumK2, A) - mu * mu
    a = Fraction(B, A)
    b = Fraction(C, A)
    j = Fraction(D, A)
    q = Fraction(Q, A)
    cov = Fraction(EF, A) - a * b
    ue = a + Fraction(sumEK, A) - a * mu
    uf = b + Fraction(sumFK, A) - b * mu
    m = len(G)  # ALOV homogenization degree is the ground-set size.
    r = Fraction(m, 1) - mu - varK
    gap = a * b - j
    return {
        "A": A, "B": B, "C": C, "D": D, "Q": Q,
        "mu": mu, "varK": varK, "a": a, "b": b, "j": j, "q": q,
        "cov": cov, "ue": ue, "uf": uf, "r": r, "gap": gap
    }

def det3(M):
    a,b,c = M[0]
    d,e,f = M[1]
    g,h,i = M[2]
    return a*(e*i-f*h) - b*(d*i-f*g) + c*(d*h-e*g)

def check_regime(weighted):
    totals = {
        "graphs": 0,
        "pairs": 0,
        "identity_fail": 0,
        "psd_fail": 0,
        "factor2_fail": 0,
        "target_fail": 0,
        "schur_certificate": 0,
        "positive_addability_cov": 0,
    }
    max_ratio = Fraction(0, 1)
    for n in range(2, 6):
        all_edges = list(combinations(range(n), 2))
        for gm in range(1 << len(all_edges)):
            G = [all_edges[i] for i in range(len(all_edges)) if (gm >> i) & 1]
            totals["graphs"] += 1
            if weighted:
                weights = {h: 1 + ((all_edges.index(h) + 2*n) % 3) for h in G}
            else:
                weights = {h: 1 for h in G}
            for e, f in combinations(G, 2):
                totals["pairs"] += 1
                s = boundary_stats(n, G, e, f, weights)

                # Exact reconnection identity:
                # Delta/A^2 = ab-j = q-Cov(A_e,A_f).
                if s["gap"] != s["q"] - s["cov"]:
                    totals["identity_fail"] += 1
                if s["gap"] < 0:
                    totals["target_fail"] += 1

                if s["cov"] > 0:
                    totals["positive_addability_cov"] += 1
                    if s["q"] > 0:
                        max_ratio = max(max_ratio, s["cov"] / s["q"])

                r,a,b,ue,uf,t = s["r"],s["a"],s["b"],s["ue"],s["uf"],s["gap"]
                M = [[r,ue,uf],[ue,a*a,t],[uf,t,b*b]]
                principal = [
                    r, a*a, b*b,
                    r*a*a - ue*ue,
                    r*b*b - uf*uf,
                    a*a*b*b - t*t,
                    det3(M),
                ]
                if any(x < 0 for x in principal):
                    totals["psd_fail"] += 1
                if abs(t) > a*b:
                    totals["factor2_fail"] += 1

                # A sufficient sign certificate obtained from the Schur interval.
                if (r > 0 and a > 0 and b > 0 and ue*uf >= 0
                        and (ue/a)**2 + (uf/b)**2 >= r):
                    totals["schur_certificate"] += 1

    return totals, max_ratio

unit, unit_ratio = check_regime(False)
weighted, weighted_ratio = check_regime(True)

# Negative control: replacing the ALOV ground-set homogenizing degree |E|
# by graphic rank is not licensed and the claimed PSD block already fails on K3.
G3 = list(combinations(range(3), 2))
s3 = boundary_stats(3, G3, G3[0], G3[1], {h:1 for h in G3})
rank_r = Fraction(2,1) - s3["mu"] - s3["varK"]
rank_matrix = [
    [rank_r, s3["ue"], s3["uf"]],
    [s3["ue"], s3["a"]**2, s3["gap"]],
    [s3["uf"], s3["gap"], s3["b"]**2],
]
rank_det = det3(rank_matrix)

print("UNIT", unit)
print("UNIT_MAX_POSITIVE_COV_OVER_RECONNECTION", unit_ratio)
print("WEIGHTED_1_2_3", weighted)
print("WEIGHTED_MAX_POSITIVE_COV_OVER_RECONNECTION", weighted_ratio)
print("K3_RANK_HOMOGENIZATION_NEGATIVE_CONTROL_DET", rank_det)

assert unit["identity_fail"] == unit["psd_fail"] == unit["factor2_fail"] == unit["target_fail"] == 0
assert weighted["identity_fail"] == weighted["psd_fail"] == weighted["factor2_fail"] == weighted["target_fail"] == 0
assert unit_ratio == Fraction(119,134)
assert weighted_ratio == Fraction(21325,21984)
assert rank_det == Fraction(-1,16)
print("STATUS=ALL_EXACT_CHECKS_PASS")
