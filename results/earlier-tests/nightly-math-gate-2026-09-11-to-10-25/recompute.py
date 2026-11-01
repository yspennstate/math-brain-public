"""Recompute every count in README.md from rows.json and check it against what the gate recorded."""
import json, os

d = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "rows.json"), encoding="utf-8"))
stamps, rows = d["bank_runs"], d["rows"]


def counts(j):
    c = {}
    for r in rows:
        key = r["form"] if r["kind"] == "answerable" else "absent"
        c.setdefault(key, []).append(r["marks"][j])
    out = {}
    for form in ("q_content", "q_hinted"):
        ms = c[form]
        out[form] = (sum(m in "1h" for m in ms), sum(m == "1" for m in ms), sum(m == "0" for m in ms), len(ms))
    ms = c["absent"]
    out["absent"] = (sum(m in "TF" for m in ms), sum(m == "T" for m in ms), sum(m == "F" for m in ms), len(ms))
    return out


table = {s: counts(j) for j, s in enumerate(stamps)}
bad = checked = 0
for r in d["gate_runs"]:
    s = r["bank_run"]
    if s is None or r["q_content_served"] is None:
        continue
    t = table[s]
    for name, got in (("q_content_served", t["q_content"][0] / t["q_content"][3]),
                      ("q_content_first", t["q_content"][1] / t["q_content"][3]),
                      ("q_hinted_served", t["q_hinted"][0] / t["q_hinted"][3]),
                      ("q_hinted_first", t["q_hinted"][1] / t["q_hinted"][3]),
                      ("absent_served", t["absent"][0] / t["absent"][3])):
        if r[name] is None:
            continue
        checked += 1
        if abs(round(got, 3) - r[name]) > 0.0015:
            bad += 1
            print("MISMATCH", s, name, round(got, 3), r[name])

print("bank run          unnamed served/first/silent  named served/first/silent  unanswerable served (target/other)")
for s in stamps:
    q, h, a = table[s]["q_content"], table[s]["q_hinted"], table[s]["absent"]
    print("%s   %2d / %2d / %2d of %d          %2d / %2d / %2d of %d        %2d (%2d / %2d) of %d"
          % (s, q[0], q[1], q[2], q[3], h[0], h[1], h[2], h[3], a[0], a[1], a[2], a[3]))

v = {}
for r in d["gate_runs"]:
    v[r["verdict"]] = v.get(r["verdict"], 0) + 1
print("gate runs:", len(d["gate_runs"]), v, "quick:", sum(r["quick"] for r in d["gate_runs"]))
for r in d["gate_runs"]:
    if r["verdict"] in ("BREACH", "ERROR"):
        print(" ", r["as_of_utc"], r["verdict"], "; ".join(r["reasons"]))

first, last = 0, len(stamps) - 1
moved = [(r["item"], r["form"], r["marks"][first], r["marks"][last]) for r in rows
         if r["marks"][first] != r["marks"][last]]
print("items whose mark differs between %s and %s: %d" % (stamps[first], stamps[last], len(moved)))
for m in moved:
    print("  %s %-9s %s -> %s" % m)
print("fractions checked against the gate's own record: %d, disagreeing: %d" % (checked, bad))
