"""Adjacent pair e = ab, f = bc on K_n. The all-edge injection identity  lambda * sum_B w |U||V| = sum_J w N  gives exactly
J / B = lambda * E_B[|U||V|] / E_J[N]   (w = lambda^|A| q^k, A the edges outside e, f).
So a K_n proof of J >= s B for lambda >= C/n is the pair of measure estimates E_B[|U||V|] >= c1 n and E_J[N] <= c2.
This prints both means over a lambda grid, by enumeration (N counted from the B side; equal to the bridge count, checked
in all_edge_injection.py)."""
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


n = int(sys.argv[1]); q = float(sys.argv[2])
E = list(itertools.combinations(range(n), 2))
e, f = (0, 1), (1, 2); a, c = 0, 2
rest = [x for x in E if x not in (e, f)]
Bw = defaultdict(int); BUV = defaultdict(int); Jw = defaultdict(int); JN = defaultdict(int)   # keyed (k, |A|)
pre = defaultdict(int); Jk = {}
for mask in range(1 << len(rest)):
    A = frozenset(rest[i] for i in range(len(rest)) if mask >> i & 1)
    k, _ = comps(n, list(A) + [e, f]); ke, _ = comps(n, list(A) + [f]); kf, _ = comps(n, list(A) + [e])
    if ke > k and kf > k:
        _, lab = comps(n, list(A))
        U = [x for x in range(n) if lab[x] == lab[a]]; V = [x for x in range(n) if lab[x] == lab[c]]
        Bw[(k, len(A))] += 1; BUV[(k, len(A))] += len(U) * len(V)
        for u in U:
            for v in V:
                pre[A | {(min(u, v), max(u, v))}] += 1
    elif ke == k and kf == k and comps(n, list(A))[0] > k:
        Jk[A] = k
for A, k in Jk.items():
    Jw[(k, len(A))] += 1; JN[(k, len(A))] += pre.get(A, 0)
ev = lambda P, lam: sum(v * lam ** m * q ** k for (k, m), v in P.items())
rows = []
for nl in [0.5, 1, 1.5, 2, 3, 4, 6, 8, 12, 16, 24, 32]:
    lam = nl / n
    b, j = ev(Bw, lam), ev(Jw, lam)
    rows.append({"n_lambda": nl, "E_B_UV": ev(BUV, lam) / b, "E_J_N": ev(JN, lam) / j, "J_over_B": j / b})
out = {"n": n, "q": q, "rows": rows}
print(json.dumps(out, indent=0)); json.dump(out, open(f"injection_means_K{n}_q{q}.json", "w"), indent=1)
