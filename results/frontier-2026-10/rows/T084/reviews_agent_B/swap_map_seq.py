"""Sequential crossing rules (see swap_map_rules.py). 'seq': move A-edges crossing L (fixed L from B - e) in index order until e
separates the ends in A. 'seq_dyn': same, but recompute L from the current B' - e after each move, and stop as soon as the pair is
good (e separates in A' and e is not a bridge of B'). Report not-good images, q loss > 1, collisions."""
import itertools, json
from bern_general import comps
from swap_map_rules import cluster_of


def run(n, E, e, f, rule):
    m = len(E); kk = [comps(n, E, x) for x in range(1 << m)]; a0 = E[e][0]
    st = {"bad": 0, "not_good": 0, "q_loss_gt1": 0, "collisions": 0}; seen = set()
    good = lambda A, B: kk[A | 1 << e] < kk[A] and not kk[B & ~(1 << e)] > kk[B]
    for A in range(1 << m):
        if A >> e & 1 or kk[A | 1 << e] < kk[A]: continue
        for B in range(1 << m):
            if not (B >> e & 1 and B >> f & 1) or not kk[B & ~(1 << e)] > kk[B]: continue
            st["bad"] += 1; A2, B2 = A, B
            L = cluster_of(n, E, B & ~(1 << e), a0)
            for _ in range(m):
                if rule == "seq_dyn":
                    if good(A2, B2): break
                    L = cluster_of(n, E, B2 & ~(1 << e), a0)
                elif kk[A2 | 1 << e] < kk[A2]: break
                cr = [g for g in range(m) if A2 >> g & 1 and ((E[g][0] in L) != (E[g][1] in L))]
                if not cr: break
                A2 &= ~(1 << cr[0]); B2 |= 1 << cr[0]
            if not good(A2, B2): st["not_good"] += 1
            if kk[A2] + kk[B2] > kk[A] + kk[B] + 1: st["q_loss_gt1"] += 1
            if (A2, B2) in seen: st["collisions"] += 1
            seen.add((A2, B2))
    return st


if __name__ == "__main__":
    K4 = list(itertools.combinations(range(4), 2)); K5 = list(itertools.combinations(range(5), 2))
    for name, n, E, e, f in (("K4 adj", 4, K4, 0, 1), ("K4 dis", 4, K4, 0, 5), ("K5 adj", 5, K5, 0, 1), ("K5 dis", 5, K5, 0, 7)):
        for rule in ("seq", "seq_dyn"):
            print(json.dumps({"graph": name, "rule": rule, **run(n, E, e, f, rule)}), flush=True)
