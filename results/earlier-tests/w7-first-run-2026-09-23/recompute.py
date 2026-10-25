"""Recompute the tables in README.md from rows.json."""
import json, os
from math import comb
HERE = os.path.dirname(os.path.abspath(__file__))
# (n, full credit with the brain, full credit without, helped, harmed)
CLAIMS = {
    "adjudicated/store": (
        49,
        49,
        8,
        41,
        0
    ),
    "adjudicated/conjecture": (
        10,
        10,
        4,
        6,
        0
    ),
    "adjudicated/control": (
        20,
        20,
        20,
        0,
        0
    ),
    "adjudicated/all": (
        79,
        79,
        32,
        47,
        0
    ),
    "as_keyed/store": (
        49,
        47,
        7,
        40,
        0
    ),
    "as_keyed/conjecture": (
        10,
        10,
        4,
        6,
        0
    ),
    "as_keyed/control": (
        20,
        19,
        19,
        0,
        0
    ),
    "as_keyed/all": (
        79,
        76,
        30,
        46,
        0
    )
}
def mcnemar(b, c):
    n = b + c
    return 1.0 if n == 0 else min(1.0, 2 * sum(comb(n, i) for i in range(min(b, c) + 1)) / 2 ** n)
rows = json.load(open(os.path.join(HERE, "rows.json"), encoding="utf-8"))
bad = 0
for name, claim in CLAIMS.items():
    tag, kind = name.split("/")
    bk, ck = ("brain", "control") if tag == "adjudicated" else ("brain_as_keyed", "control_as_keyed")
    sel = [r for r in rows if kind == "all" or r["kind"] == kind]
    b = [r[bk] == 1.0 for r in sel]; c = [r[ck] == 1.0 for r in sel]
    helped = sum(x and not y for x, y in zip(b, c)); harmed = sum(y and not x for x, y in zip(b, c))
    got = [len(sel), sum(b), sum(c), helped, harmed]
    ok = tuple(got) == claim
    bad += not ok
    print("%-24s n=%2d brain %2d control %2d helped %2d harmed %d  McNemar p=%.2g  %s"
          % (name, got[0], got[1], got[2], helped, harmed, mcnemar(helped, harmed), "ok" if ok else "MISMATCH %s" % (claim,)))
print("every claim matches" if not bad else "%d claims do not match" % bad)
