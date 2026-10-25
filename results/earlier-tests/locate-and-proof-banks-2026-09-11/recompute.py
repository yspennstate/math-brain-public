"""Recompute every number in README.md from the verdict rows in rows/ and check it against the table below."""
import json, os
from math import comb
HERE = os.path.dirname(os.path.abspath(__file__))
# file: (n, right without, right with, wrong under the brain, helped, harmed)
CLAIMS = {
    "L1_r1": (60, 3, 38, 0, 35, 0), "L1_r2": (60, 3, 50, 0, 47, 0), "L1_r3": (60, 3, 54, 0, 51, 0),
    "L1_r4": (60, 3, 55, 0, 52, 0), "L1_r5": (60, 3, 57, 0, 54, 0),
    "L2_r3": (40, 0, 37, 0, 37, 0), "L2_r4": (40, 0, 27, 0, 27, 0), "L2_r4b": (40, 0, 29, 0, 29, 0),
    "L2_r5": (40, 0, 40, 0, 40, 0),
    "L3_r1": (30, 0, 4, 0, 4, 0), "L3_r2": (30, 0, 11, 0, 11, 0), "L3_r3": (30, 0, 30, 0, 30, 0),
    "bank100_0911": (100, 87, 90, None, 5, 2), "harder35_0911": (35, 32, 31, None, 0, 1),
    "bank100_0912": (100, 91, 94, None, 4, 1), "harder35_0912": (35, 29, 33, None, 5, 1),
    "harder35_0922": (35, 34, 34, None, 0, 0),
}
def mcnemar(b, c):
    n = b + c
    return 1.0 if n == 0 else min(1.0, 2 * sum(comb(n, k) for k in range(min(b, c) + 1)) / 2 ** n)
bad = 0
for name, claim in CLAIMS.items():
    rows = json.load(open(os.path.join(HERE, "rows", name + ".json"), encoding="utf-8"))
    if "without" in rows[0]:
        a = [r["without"] == "correct" for r in rows]; b = [r["with_brain"] == "correct" for r in rows]
        wrong = sum(r["with_brain"] == "wrong" for r in rows)
    else:
        a = [r["without_right"] for r in rows]; b = [r["with_brain_right"] for r in rows]; wrong = None
    helped = sum(y and not x for x, y in zip(a, b)); harmed = sum(x and not y for x, y in zip(a, b))
    got = (len(rows), sum(a), sum(b), wrong, helped, harmed)
    ok = got == claim
    bad += not ok
    print("%-14s n=%3d without %3d with %3d wrong %s helped %2d harmed %d  McNemar p=%.3g  %s"
          % (name, got[0], got[1], got[2], got[3], helped, harmed, mcnemar(helped, harmed), "ok" if ok else "MISMATCH %s" % (claim,)))
print("every claim matches" if not bad else "%d claims do not match" % bad)
