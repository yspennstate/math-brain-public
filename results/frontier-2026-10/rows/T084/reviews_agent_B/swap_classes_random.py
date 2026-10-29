"""swap_classes Hall test on random 6-vertex graphs (8-10 edges), adjacent and disjoint pairs; also the no-q-loss variant
(Q at K matched to P at K' <= K), to see which is the true shape."""
import itertools, json, random
from bern_general import comps


def hall(n, E, e, f, shift):
    m = len(E); kk = [comps(n, E, x) for x in range(1 << m)]; pc = [bin(x).count("1") for x in range(1 << m)]
    P, Q = {}, {}
    for A in range(1 << m):
        if A >> e & 1: continue
        d1 = kk[A | 1 << e] < kk[A]
        for B in range(1 << m):
            if not (B >> e & 1 and B >> f & 1): continue
            d2 = kk[B & ~(1 << e)] > kk[B]
            if d1 == d2: continue
            T = P if d1 else Q; s, K = pc[A] + pc[B], kk[A] + kk[B]
            T.setdefault(s, {}); T[s][K] = T[s].get(K, 0) + 1
    for s in set(P) | set(Q):
        for K0 in range(0, 4 * n):
            if sum(c for K, c in P.get(s, {}).items() if K <= K0) < sum(c for K, c in Q.get(s, {}).items() if K <= K0 - shift):
                return False
    return True


rng = random.Random(9); allE = list(itertools.combinations(range(6), 2)); res = {}
for g in range(10):
    E = sorted(rng.sample(allE, rng.randint(8, 10)))
    for e, f in itertools.combinations(range(len(E)), 2):
        if rng.random() > 0.25: continue
        kind = "adj" if set(E[e]) & set(E[f]) else "dis"
        for shift in (1, 0):
            key = "%s_shift%d" % (kind, shift); r = res.setdefault(key, [0, 0])
            r[0] += 1; r[1] += 0 if hall(6, E, e, f, shift) else 1
for k, (t, b) in sorted(res.items()): print(json.dumps({"case": k, "pairs": t, "hall_failures": b}))
K4 = list(itertools.combinations(range(4), 2)); K5 = list(itertools.combinations(range(5), 2))
print(json.dumps({"no_loss_K4adj": hall(4, K4, 0, 1, 0), "no_loss_K4dis": hall(4, K4, 0, 5, 0), "no_loss_K5adj": hall(5, K5, 0, 1, 0)}))
