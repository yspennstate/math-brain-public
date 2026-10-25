"""Recompute the four-arm locate table from rows.json: counts by arm and family, paired exact McNemar, cost and effort."""
import json, os, statistics
from math import comb

D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "rows.json"), encoding="utf-8"))
rows = D["rows"]
ARMS = ["both", "files", "connected", "sterile"]
GRADES = ["correct", "unknown", "wrong", "error"]


def med(xs):
    xs = [x for x in xs if x is not None]
    return statistics.median(xs) if xs else None


print("arm          n  " + "  ".join("%7s" % g for g in GRADES) + "   in_tok_med  turns_med  sec_med  usd_sum")
for a in ARMS:
    g = [r[a]["grade"] for r in rows]
    print("%-10s %3d  " % (a, len(g)) + "  ".join("%7d" % g.count(x) for x in GRADES)
          + "   %10s  %9s  %7.1f  %7.2f" % (med(r[a].get("input_tokens") for r in rows), med(r[a].get("turns") for r in rows),
                                           med(r[a].get("seconds") for r in rows), sum(r[a].get("usd") or 0 for r in rows)))

print()
fams = sorted({(r["bank"], r["family"]) for r in rows})
for b, f in fams:
    sub = [r for r in rows if (r["bank"], r["family"]) == (b, f)]
    print("%-24s n %3d  " % (b + "/" + f, len(sub)) + "  ".join("%s %d" % (a, sum(r[a]["grade"] == "correct" for r in sub)) for a in ARMS))


def mcnemar(x, y):
    n = x + y
    if n == 0:
        return 1.0
    k = min(x, y)
    return min(1.0, 2 * sum(comb(n, i) for i in range(k + 1)) / 2 ** n)


print()
for a, b in [("both", "files"), ("both", "connected"), ("both", "sterile"), ("connected", "files"), ("files", "sterile")]:
    x = sum(r[a]["grade"] == "correct" and r[b]["grade"] != "correct" for r in rows)
    y = sum(r[b]["grade"] == "correct" and r[a]["grade"] != "correct" for r in rows)
    print("%-9s vs %-9s  %s right only %d, %s right only %d, exact McNemar p = %.3g" % (a, b, a, x, b, y, mcnemar(x, y)))

print()
v = [r for r in rows if r["served_block_holds_value"]]
print("served block holds the value on %d of %d; connected correct on those %d, both correct on those %d"
      % (len(v), len(rows), sum(r["connected"]["grade"] == "correct" for r in v), sum(r["both"]["grade"] == "correct" for r in v)))
