"""Recompute the T16 and T17 tallies from rows.json: preference, the four judge counts, the pass bar, by program,
and for T17 without the three situations whose reference held no store claims."""
import collections, json, os

D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "rows.json"), encoding="utf-8"))
KEYS = ("built_on", "redundant", "dead_end", "on_target")


def report(label, rows, need):
    agg = {a: collections.Counter() for a in ("DIGEST", "NONE")}
    pref = collections.Counter(r["preferred"] for r in rows)
    for r in rows:
        for a in agg:
            for k in KEYS:
                agg[a][k] += r[a][k]
    p1 = pref["DIGEST"] >= need
    p2 = agg["DIGEST"]["on_target"] >= agg["NONE"]["on_target"]
    p3 = agg["DIGEST"]["redundant"] + agg["DIGEST"]["dead_end"] < agg["NONE"]["redundant"] + agg["NONE"]["dead_end"]
    print("%s (%d situations): preferred DIGEST %d, NONE %d, equal %d" % (label, len(rows), pref["DIGEST"], pref["NONE"], pref["equal"]))
    for a in agg:
        print("   %-6s " % a + "  ".join("%s %d" % (k, agg[a][k]) for k in KEYS)
              + "  plan words (mean) %.0f" % (sum(r[a]["plan_words"] for r in rows) / len(rows)))
    print("   P1 (DIGEST preferred >= %d) %s, P2 (on_target DIGEST >= NONE) %s, P3 (fewer redundant + dead_end) %s"
          % (need, "pass" if p1 else "fail", "pass" if p2 else "fail", "yes" if p3 else "no"))


for t in ("T16", "T17"):
    rows = [r for r in D["rows"] if r["test"] == t]
    report(t, rows, 5)
    for p in ("FEI", "QFORM"):
        report("  " + t + " " + p, [r for r in rows if r["program"] == p], 3)
    if t == "T17":
        report("  T17 without the empty-store situations", [r for r in rows if not r["reference_store_section_empty"]], 3)
        usd = sum(r[a].get("usd") or 0 for r in rows for a in ("DIGEST", "NONE"))
        print("   T17 planning runs: 16, USD %.2f at API prices" % usd)
    print()
