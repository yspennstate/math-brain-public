"""Explicit maps for the swap matching. Bad pair: A without e (e closes a cycle in A), B with e, f (e a bridge of B). L = the vertex
set of e's first endpoint's cluster in B - e. Rules: 'least' moves the least-index A-edge with exactly one end in L from A to B;
'all' moves every such edge. Report: images that are not good (d1 = 1, d2 = 0), images losing more than one q (K' > K + 1),
collisions (two bad pairs with one image), and collisions with... nothing else (good pairs are the target set, each used once)."""
import itertools, json
from bern_general import comps


def cluster_of(n, E, mask, v):
    adj = {i: [] for i in range(n)}
    for g, (a, b) in enumerate(E):
        if mask >> g & 1: adj[a].append(b); adj[b].append(a)
    seen = {v}; st = [v]
    while st:
        x = st.pop()
        for y in adj[x]:
            if y not in seen: seen.add(y); st.append(y)
    return seen


def run(n, E, e, f, rule):
    m = len(E); kk = [comps(n, E, x) for x in range(1 << m)]; a0 = E[e][0]
    stats = {"bad": 0, "not_good": 0, "q_loss_gt1": 0, "collisions": 0}; seen = {}
    for A in range(1 << m):
        if A >> e & 1 or kk[A | 1 << e] < kk[A]: continue          # need e closing a cycle in A (d1 = 0)
        for B in range(1 << m):
            if not (B >> e & 1 and B >> f & 1) or not kk[B & ~(1 << e)] > kk[B]: continue   # d2 = 1
            stats["bad"] += 1
            L = cluster_of(n, E, B & ~(1 << e), a0)
            cross = [g for g in range(m) if A >> g & 1 and ((E[g][0] in L) != (E[g][1] in L))]
            C = cross[:1] if rule == "least" else cross
            cm = sum(1 << g for g in C); A2, B2 = A & ~cm, B | cm
            d1 = kk[A2 | 1 << e] < kk[A2]; d2 = kk[B2 & ~(1 << e)] > kk[B2]
            if not (d1 and not d2): stats["not_good"] += 1
            if kk[A2] + kk[B2] > kk[A] + kk[B] + 1: stats["q_loss_gt1"] += 1
            if (A2, B2) in seen: stats["collisions"] += 1
            seen[(A2, B2)] = 1
    return stats


if __name__ == "__main__":
    K4 = list(itertools.combinations(range(4), 2)); K5 = list(itertools.combinations(range(5), 2))
    for name, n, E, e, f in (("triangle", 3, [(0, 1), (1, 2), (0, 2)], 0, 1), ("K4 adj", 4, K4, 0, 1), ("K4 dis", 4, K4, 0, 5),
                             ("K5 adj", 5, K5, 0, 1), ("K5 dis", 5, K5, 0, 7)):
        for rule in ("least", "all"):
            print(json.dumps({"graph": name, "rule": rule, **run(n, E, e, f, rule)}), flush=True)
