import json, math
from enum_maxdim import conjugate, hooks_dim
recs = {}
for line in open("maxdim_results.jsonl", encoding="utf-8"):
    r = json.loads(line); recs[r["n"]] = r
bfile = {int(l.split()[0]): int(l.split()[1]) for l in open("b003040.txt") if l.strip() and not l.startswith("#")}
N = max(recs)
print("n range", min(recs), N)
bad = []
rows = []
for n in range(1, N + 1):
    r = recs[n]
    lam = tuple(r["maximisers"][0])
    d, _ = hooks_dim(lam)                       # independent exact recomputation
    assert str(d) == r["dmax"], n
    agree = (bfile.get(n) == d)
    if not agree: bad.append(n)
    lc = conjugate(lam)
    core = tuple(min(a, b) for a, b in zip(lam + (0,)*len(lc), lc + (0,)*len(lam)))
    core = tuple(x for x in core if x > 0)
    # boxes of lam not in core
    A = [(i, j) for i, li in enumerate(lam) for j in range(li) if not (i < len(core) and j < core[i])]
    below = [(i, j) for (i, j) in A if i > j]; above = [(i, j) for (i, j) in A if i < j]
    onerow = len(set(i for i, j in below)) == len(below); onecol = len(set(j for i, j in above)) == len(above)
    one_side = (len(below) == 0 or len(above) == 0)
    duzhin_ok = one_side and ((len(above) == 0 and onerow) or (len(below) == 0 and onecol))
    rows.append((n, r["classes_up_to_conjugation"], r["self_conjugate"], lam[0], len(lam), len(A), one_side, duzhin_ok, (r["log_gap_to_next"] if r["log_gap_to_next"] is not None else 99.0), agree))
    print(n, "classes", r["classes_up_to_conjugation"], "selfconj", int(r["self_conjugate"]), "l1", lam[0], "rows", len(lam), "|A|", len(A), "oneside", int(one_side), "duzhin", int(duzhin_ok), "gap %s" % r["log_gap_to_next"], "oeis", int(agree), lam)
print("all unique up to conjugation:", all(x[1] == 1 for x in rows))
print("disagree with OEIS/Duzhin b-file at n =", bad)
print("self-conjugate n:", [x[0] for x in rows if x[2]])
print("lambda_1 - rows:", sorted(set(x[3] - x[4] for x in rows)))
print("|A| max", max(x[5] for x in rows), "all one side:", all(x[6] for x in rows), "all Duzhin:", all(x[7] for x in rows))
print("min gap n:", min(rows, key=lambda x: x[8])[:1], min(x[8] for x in rows))
print("gaps below 0.01:", [(x[0], round(x[8], 5)) for x in rows if x[8] < 0.01])
