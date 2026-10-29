"""Bernstein positivity (as bern_general.py) on named graphs, edge e = edges[0] (and e = every edge orbit rep when cheap) against
every other edge, one enumeration per e."""
import json, itertools, sys
from bern_general import comps, to_lam_u, mul, bernstein_neg


def graphs():
    G = {}
    G["petersen"] = (10, [(i, (i + 1) % 5) for i in range(5)] + [(i, i + 5) for i in range(5)] + [(5 + i, 5 + (i + 2) % 5) for i in range(5)])
    G["K33"] = (6, [(i, j) for i in range(3) for j in range(3, 6)])
    G["K34"] = (7, [(i, j) for i in range(3) for j in range(3, 7)])
    G["cube"] = (8, [(i, i ^ (1 << b)) for i in range(8) for b in range(3) if i < i ^ (1 << b)])
    G["wheel6"] = (7, [(0, i) for i in range(1, 7)] + [(i, i % 6 + 1) for i in range(1, 7)])
    G["K6-PM"] = (6, [(i, j) for i, j in itertools.combinations(range(6), 2) if (i, j) not in ((0, 1), (2, 3), (4, 5))])
    G["prism5"] = (10, [(i, (i + 1) % 5) for i in range(5)] + [(5 + i, 5 + (i + 1) % 5) for i in range(5)] + [(i, i + 5) for i in range(5)])
    G["K5+pendpath"] = (7, list(itertools.combinations(range(5), 2)) + [(4, 5), (5, 6), (6, 0)])
    G["K7-minus-6"] = (7, list(itertools.combinations(range(7), 2))[6:])
    return G


def run(n, edges, e):
    m = len(edges); Z, Ze = {}, {}; Zf = [dict() for _ in range(m)]; Zef = [dict() for _ in range(m)]
    for mask in range(1 << m):
        key = (bin(mask).count("1"), comps(n, edges, mask))
        Z[key] = Z.get(key, 0) + 1
        ie = mask >> e & 1
        if ie: Ze[key] = Ze.get(key, 0) + 1
        for f in range(m):
            if mask >> f & 1:
                Zf[f][key] = Zf[f].get(key, 0) + 1
                if ie: Zef[f][key] = Zef[f].get(key, 0) + 1
    Zu, Zeu = to_lam_u(Z, n), to_lam_u(Ze, n); res = []
    for f in range(m):
        if f == e: continue
        N = mul(Zeu, to_lam_u(Zf[f], n))
        for k, c in mul(Zu, to_lam_u(Zef[f], n)).items(): N[k] = N.get(k, 0) - c
        N = {k: c for k, c in N.items() if c}
        if N: res.append(bernstein_neg(N)[2])
    return res


if __name__ == "__main__":
    for name, (n, edges) in graphs().items():
        r = run(n, edges, 0)
        print(json.dumps({"graph": name, "n": n, "m": len(edges), "pairs": len(r), "bernstein_negative_pairs": sum(1 for x in r if x)}), flush=True)
