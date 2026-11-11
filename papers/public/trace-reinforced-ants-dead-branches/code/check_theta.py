# Generalised theta graph: k internally disjoint N-F paths of lengths L_1..L_k (all >= 2).
# Claim: weights a_i^j on the j-th edge of path i, with  sum_i a_i^{L_i} = 1  and  (1-a_i)/(1-a_i^{L_i}) = C for all i,
# form an equilibrium. Compare with the flow limits stored in fam.jsonl (sorted weight multisets).
import json, re, sys
def alpha(C, L):
    lo, hi = 0.0, 1.0   # (1-a)/(1-a^L) decreases from 1 to 1/L
    for _ in range(200):
        mid = (lo + hi) / 2
        if (1 - mid) / (1 - mid ** L) > C: lo = mid
        else: hi = mid
    return (lo + hi) / 2
def solve(Ls):
    lo, hi = max(1.0 / L for L in Ls) + 1e-15, 1.0
    for _ in range(200):
        C = (lo + hi) / 2
        s = sum(alpha(C, L) ** L for L in Ls)
        if s > 1: lo = C
        else: hi = C
    return C, [alpha(C, L) for L in Ls]
worst = 0.0; n = 0
for l in open(sys.argv[1] if len(sys.argv) > 1 else "fam.jsonl"):
    r = json.loads(l); name = r["name"]
    m = re.match(r"theta_k(\d+)_L(\d+)$", name)
    if m: Ls = [int(m.group(2))] * int(m.group(1))
    elif name.startswith("thetamix_"): Ls = [int(x) for x in name.split("_")[1:]]
    else: continue
    if min(Ls) < 2: continue
    C, al = solve(Ls)
    pred = sorted(a ** j for a, L in zip(al, Ls) for j in range(1, L + 1))
    best = None
    for s in r["sols"]:
        w = sorted(s["w"])
        if len(w) != len(pred): continue
        d = max(abs(x - y) for x, y in zip(w, pred))
        best = d if best is None else min(best, d)
    n += 1; worst = max(worst, best if best is not None else 9)
    print(name, "nsol", r["nsol"], "C", round(C, 6), "alphas", [round(a, 6) for a in al], "max |flow - formula|", best)
print("rows", n, "worst", worst)
