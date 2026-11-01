"""Swap reduction: Cov <= 0 iff sum_{d1=1,d2=0} w >= q sum_{d1=0,d2=1} w over A not containing e, B containing e and f.
Count P[s][K] (d1=1,d2=0) and Q[s][K] (d1=0,d2=1), s = |A|+|B|, K = k(A)+k(B). A per-lam-power matching sending each Q-pair at K
to a P-pair at K' <= K+1 exists iff for every s, K0: sum_{K<=K0} P[s][K] >= sum_{K<=K0-1} Q[s][K] (Hall, monotone). Test it."""
import itertools, json, sys
from bern_general import comps


def run(n, E, e, f):
    m = len(E); kk = [comps(n, E, x) for x in range(1 << m)]
    pc = [bin(x).count("1") for x in range(1 << m)]
    P, Q = {}, {}
    for A in range(1 << m):
        if A >> e & 1: continue
        d1 = kk[A | 1 << e] < kk[A]
        for B in range(1 << m):
            if not (B >> e & 1 and B >> f & 1): continue
            d2 = kk[B & ~(1 << e)] > kk[B]
            if d1 == d2: continue
            s, K = pc[A] + pc[B], kk[A] + kk[B]
            T = P if d1 else Q
            T.setdefault(s, {}); T[s][K] = T[s].get(K, 0) + 1
    fail = []
    for s in set(P) | set(Q):
        Ks = sorted(set(P.get(s, {})) | set(Q.get(s, {})) | {k + 1 for k in Q.get(s, {})})
        for K0 in Ks:
            lhs = sum(c for K, c in P.get(s, {}).items() if K <= K0); rhs = sum(c for K, c in Q.get(s, {}).items() if K <= K0 - 1)
            if lhs < rhs: fail.append((s, K0, lhs, rhs))
    tight = sum(1 for s in Q for K in Q[s])
    return {"P_total": sum(sum(v.values()) for v in P.values()), "Q_total": sum(sum(v.values()) for v in Q.values()),
            "hall_failures": len(fail), "first": fail[:3]}


if __name__ == "__main__":
    K4 = list(itertools.combinations(range(4), 2)); K5 = list(itertools.combinations(range(5), 2))
    C4c = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]; K33 = [(i, j) for i in range(3) for j in range(3, 6)]
    for name, n, E, e, f in (("triangle", 3, [(0, 1), (1, 2), (0, 2)], 0, 1), ("C4+chord", 4, C4c, 0, 1), ("K4 adj", 4, K4, 0, 1),
                             ("K4 dis", 4, K4, 0, 5), ("K33 adj", 6, K33, 0, 1), ("K5 adj", 5, K5, 0, 1), ("K5 dis", 5, K5, 0, 7)):
        print(json.dumps({"graph": name, **run(n, E, e, f)}), flush=True)
