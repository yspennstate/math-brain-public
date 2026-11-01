# T084, agent B: is the swap matching possible with EXACTLY one q lost, class by class? Test P[s][K+1] >= Q[s][K]
# for every s, K (pointwise), from the swap counts directly (a path independent of qseries_atlas.py).
import itertools, json, sys
sys.path.insert(0, r'T084\reviews_agent_B')
from bern_general import comps
def counts(n, E, e, f):
    m = len(E); kk = [comps(n, E, x) for x in range(1 << m)]; pc = [bin(x).count("1") for x in range(1 << m)]
    P, Q = {}, {}
    for A in range(1 << m):
        if A >> e & 1: continue
        d1 = kk[A | 1 << e] < kk[A]
        for B in range(1 << m):
            if not (B >> e & 1 and B >> f & 1): continue
            d2 = kk[B & ~(1 << e)] > kk[B]
            if d1 == d2: continue
            key = (pc[A] + pc[B], kk[A] + kk[B]); T = P if d1 else Q; T[key] = T.get(key, 0) + 1
    return P, Q
K4 = list(itertools.combinations(range(4), 2)); K5 = list(itertools.combinations(range(5), 2))
C4c = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]; K33 = [(i, j) for i in range(3) for j in range(3, 6)]
for name, n, E, e, f in (("triangle", 3, [(0, 1), (1, 2), (0, 2)], 0, 1), ("C4+chord", 4, C4c, 0, 1), ("K4 adj", 4, K4, 0, 1),
                         ("K4 dis", 4, K4, 0, 5), ("K33 adj", 6, K33, 0, 1), ("K5 adj", 5, K5, 0, 1), ("K5 dis", 5, K5, 0, 7)):
    P, Q = counts(n, E, e, f)
    fails = [(s, K, Q[(s, K)], P.get((s, K + 1), 0)) for (s, K) in Q if P.get((s, K + 1), 0) < Q[(s, K)]]
    slack = min(P.get((s, K + 1), 0) / Q[(s, K)] for (s, K) in Q)
    print(json.dumps({"graph": name, "Q_classes": len(Q), "pointwise_failures": len(fails), "min_ratio_P_over_Q": round(slack, 4), "first": fails[:3]}), flush=True)
