"""Recompute the table in README.md from rows.json."""
import json, os
from math import comb
HERE = os.path.dirname(os.path.abspath(__file__))
rows = json.load(open(os.path.join(HERE, "rows.json"), encoding="utf-8"))
CLAIM = {"n": 27, "brain_correct": 27, "control_correct": 1, "control_partial": 1, "control_abstain": 25,
         "helped": 26, "harmed": 0}
b = [r["brain"] == "correct" for r in rows]; c = [r["control"] == "correct" for r in rows]
got = {"n": len(rows), "brain_correct": sum(b), "control_correct": sum(c),
       "control_partial": sum(r["control"] == "partial" for r in rows),
       "control_abstain": sum(r["control"] == "abstain" for r in rows),
       "helped": sum(x and not y for x, y in zip(b, c)), "harmed": sum(y and not x for x, y in zip(b, c))}
n = got["helped"] + got["harmed"]
p = 1.0 if n == 0 else min(1.0, 2 * sum(comb(n, i) for i in range(min(got["helped"], got["harmed"]) + 1)) / 2 ** n)
print(got, "exact sign test p = %.2g" % p)
print("every claim matches" if got == CLAIM else "MISMATCH: claimed %s" % CLAIM)
