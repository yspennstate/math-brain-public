"""Derive AB30's reported quantities from the rows in this folder and write them to results.json, keyed by claim id.
It knows nothing of the reported values: those are in CLAIMS.json, and check.py compares the two.

    python derive.py [results.json]

The counted run of an item and arm is the last row for that (id, arm) in results.jsonl: the runner appends a re-run
after a failed or session-limited attempt (DEVIATION.md items 7-9). In rounds 4 and 5a an item one arm timed out on is
in no RESULT file (the result builder pairs arms); its other arms were graded by two extra graders, whose grades are in
timeout_items_grades.jsonl. A timeout scores zero (PREREG.md). An answered run whose two extra grades are not both
"full" is listed under not_recomputable and adds nothing.
"""
import io
import json
import os
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def jl(p):
    return [json.loads(l) for l in io.open(os.path.join(HERE, p), encoding="utf-8") if l.strip()]


def js(p):
    return json.load(io.open(os.path.join(HERE, p), encoding="utf-8"))


def counted(rows):
    last = {}
    for r in rows:
        last[(r["id"], r["arm"])] = r
    return last


def cost_table(rows, arm):
    c = [r.get("cost_usd_list") or 0.0 for (i, a), r in counted(rows).items() if a == arm]
    return round(sum(c), 2), round(statistics.median(c), 2), len(c)


def derive():
    v, notes, open_claims = {}, {}, []
    r1 = js("round1/RESULT_final.json")
    for fam in ("all", "proof_audit", "house_results"):
        b = r1["by_family"][fam]
        v["R1.points.%s" % fam] = [b["on_points"], b["off_points"]]
        items = [i for i in r1["items"] if fam == "all" or i["family"] == fam]
        v["R1.points_from_item_rows.%s" % fam] = [sum(i["on_pts"] for i in items), sum(i["off_pts"] for i in items)]
    rows1 = jl("round1/results.jsonl")
    for arm in ("on", "off"):
        tot, med, n = cost_table(rows1, arm)
        v["R1.cost.%s" % arm] = [tot, med]
        notes["R1.cost.%s" % arm] = "%d counted runs" % n
    rows2 = jl("round2/results.jsonl")
    for arm in ("on", "ondiet"):
        tot, med, n = cost_table(rows2, arm)
        v["R2.cost_total.%s" % arm] = tot
        notes["R2.cost_total.%s" % arm] = "%d counted runs" % n
    for g in ("A", "B"):
        b = js("round3/RESULT_r3_%s.json" % g)["by_family"]["all"]
        v["R3.points.grader_%s" % g] = [b["on_points"], b["off_points"]]
    rows3 = jl("round3/results.jsonl")
    for arm in ("on", "off"):
        tot, med, n = cost_table(rows3, arm)
        v["R3.cost.%s" % arm] = [tot, med]
        notes["R3.cost.%s" % arm] = "%d counted runs" % n
    for rnd, tag, arms in (("round4", "R4", ("on", "off")), ("round5a", "R5A", ("on", "off", "onlegacy"))):
        rep = js("%s/REPORT_%s_final.json" % (rnd, "r4" if rnd == "round4" else "r5a"))
        rows = rep["rows"]
        pts = {a: sum((r.get(a) or {}).get("pts") or 0 for r in rows) for a in arms}
        if rnd == "round4":
            v["R4.points.graded_in_both_arms"] = [pts["on"], pts["off"]]
        v["%s.median_item_cost.on_over_off" % tag] = round(statistics.median(r["on"]["cost"] / r["off"]["cost"]
                                                                            for r in rows), 3)
        notes["%s.median_item_cost.on_over_off" % tag] = "%d items" % len(rows)
        if rnd == "round5a":
            v["R5A.median_item_cost.on_over_onlegacy"] = round(statistics.median(r["on"]["cost"] / r["onlegacy"]["cost"]
                                                                                 for r in rows), 2)
        graded = {r["id"] for r in rows}
        runs = counted(jl("%s/results.jsonl" % rnd))
        others = sorted({i for (i, a) in runs} - graded)
        extra = {}
        for g in jl("timeout_items_grades.jsonl"):
            if g["round"] == rnd:
                extra.setdefault((g["id"], g["arm"]), []).append(g["grade"])
        tot = dict(pts)
        for i in others:
            for a in arms:
                r = runs.get((i, a))
                if r is None or r.get("timed_out"):
                    continue
                gs = extra.get((i, a), [])
                if len(gs) == 2 and gs[0] == gs[1] == "full":
                    tot[a] += 1
                else:
                    open_claims.append("%s %s %s: answered, but graded %s" % (rnd, i, a, gs or "by nobody"))
        v["%s.totals_with_timeout_items" % tag] = {a: int(tot[a]) for a in arms}
        notes["%s.totals_with_timeout_items" % tag] = "%d items; a timeout scores 0" % (len(graded) + len(others))
    v["STATUS.pairs_done"] = len(r1["items"])
    notes["STATUS.pairs_done"] = "round 1 items with a result; STATUS.json is compared with this by check.py"
    return {"values": v, "notes": notes, "not_recomputable": open_claims}


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "results.json")
    res = derive()
    with io.open(out, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(res, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print("derived %d quantities -> %s" % (len(res["values"]), out))


if __name__ == "__main__":
    main()
