"""Adjacent pair e = ab, f = bc on K_n. For A in the both-bridges class B, A - e - f has components U (a), M (b), V (c);
every U-V edge g gives A + g in the joint class J with the same component count. Check, by enumeration:
  (1) the preimages of A' in J are exactly the bridges of Q (the a,c side of A' - e - f) that separate a from c;
  (2) lambda * sum_B w |U||V| = sum_J w N(A')  as polynomials (N = number of preimages);
  (3) max over A' of sum_g 1/(|U_g||V_g|) <= 1, so the uniformly averaged injection gives only J >= lambda B.
"""
import itertools, json, sys
from collections import defaultdict


def comps(n, edges):
    p = list(range(n))
    def f(x):
        while p[x] != x:
            p[x] = p[p[x]]; x = p[x]
        return x
    for a, b in edges:
        p[f(a)] = f(b)
    lab = [f(x) for x in range(n)]
    return len(set(lab)), lab


n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
E = list(itertools.combinations(range(n), 2))
e, f = (0, 1), (1, 2); a, b, c = 0, 1, 2
rest = [x for x in E if x not in (e, f)]
lhs = defaultdict(int); rhs = defaultdict(int)          # keyed by (k, |A|-2): lambda * B|U||V| uses m+1
pre_count = defaultdict(int); worst = 0.0; bad = 0
Jset = {}
for mask in range(1 << len(rest)):
    A = frozenset(rest[i] for i in range(len(rest)) if mask >> i & 1)
    k, _ = comps(n, list(A) + [e, f]); ke, _ = comps(n, list(A) + [f]); kf, _ = comps(n, list(A) + [e])
    k0, lab = comps(n, list(A))
    if ke > k and kf > k:                                   # B
        U = [x for x in range(n) if lab[x] == lab[a]]; V = [x for x in range(n) if lab[x] == lab[c]]
        lhs[(k, len(A) + 1)] += len(U) * len(V)
        for u in U:
            for v in V:
                g = (min(u, v), max(u, v))
                pre_count[A | {g}] += 1
    elif ke == k and kf == k and k0 > k:
        Jset[A] = k
for A, k in Jset.items():
    N = pre_count.get(A, 0)
    rhs[(k, len(A))] += N
    # direct count of bridges of Q separating a and c
    _, lab = comps(n, list(A))
    direct = 0; ssum = 0.0
    for g in A:
        _, l2 = comps(n, list(A - {g}))
        if lab[g[0]] == lab[a] and l2[a] != l2[c]:
            direct += 1
            Ug = sum(1 for x in range(n) if l2[x] == l2[a]); Vg = sum(1 for x in range(n) if l2[x] == l2[c])
            ssum += 1.0 / (Ug * Vg)
    bad += direct != N
    worst = max(worst, ssum)
out = {"n": n, "J_configs": len(Jset), "preimage_count_mismatches": bad,
       "identity_holds": {k: v for k, v in lhs.items() if v} == {k: v for k, v in rhs.items() if v}, "J_configs_with_no_preimage": sum(1 for A in Jset if A not in pre_count), "max_sum_inverse_UV": worst}
print(json.dumps(out)); json.dump(out, open(f"all_edge_injection_K{n}.json", "w"))
notJ = [A for A in pre_count if A not in Jset]
print("images outside J:", len(notJ), "lhs-rhs diff keys:", {k: (lhs.get(k, 0), rhs.get(k, 0)) for k in set(lhs) | set(rhs) if lhs.get(k, 0) != rhs.get(k, 0)})
