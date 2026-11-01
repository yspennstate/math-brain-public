"""Recompute the tables in README.md from rows.json."""
import json, os
from math import comb
HERE = os.path.dirname(os.path.abspath(__file__))
# per arm: q_content and q_hinted (n, served the theorem, theorem first, silent);
# unanswerable (n, served anything, served the target the store now holds)
CLAIMS = {
    "namedfam_off": {
        "q_content": [
            89,
            72,
            57,
            9
        ],
        "q_hinted": [
            89,
            83,
            80,
            4
        ],
        "unanswerable": [
            40,
            28,
            7
        ]
    },
    "namedfam_on": {
        "q_content": [
            89,
            73,
            57,
            8
        ],
        "q_hinted": [
            89,
            86,
            83,
            1
        ],
        "unanswerable": [
            40,
            28,
            7
        ]
    },
    "alias_off": {
        "q_content": [
            89,
            73,
            57,
            8
        ],
        "q_hinted": [
            89,
            86,
            83,
            1
        ],
        "unanswerable": [
            40,
            28,
            7
        ]
    },
    "alias_on": {
        "q_content": [
            89,
            73,
            57,
            8
        ],
        "q_hinted": [
            89,
            86,
            83,
            1
        ],
        "unanswerable": [
            40,
            28,
            7
        ]
    }
}
def mcnemar(b, c):
    n = b + c
    return 1.0 if n == 0 else min(1.0, 2 * sum(comb(n, i) for i in range(min(b, c) + 1)) / 2 ** n)
rows = json.load(open(os.path.join(HERE, "rows.json"), encoding="utf-8"))
bad = 0
for arm, claim in CLAIMS.items():
    for form in ("q_content", "q_hinted"):
        sel = [r[arm] for r in rows if r["form"] == form]
        got = [len(sel), sum(c["hit"] for c in sel), sum(c["rank1"] for c in sel), sum(not c["served"] for c in sel)]
        ok = got == claim[form]; bad += not ok
        print("%-13s %-10s n=%d theorem %d first %d silent %d  %s" % (arm, form, *got, "ok" if ok else "MISMATCH %s" % claim[form]))
    sel = [r[arm] for r in rows if r["kind"] == "unanswerable"]
    got = [len(sel), sum(c["served"] for c in sel), sum(c["target_served"] for c in sel)]
    ok = got == claim["unanswerable"]; bad += not ok
    print("%-13s unanswerable n=%d served %d target now held %d (strict false fires %d of %d)  %s"
          % (arm, *got, got[1] - got[2], got[0] - got[2], "ok" if ok else "MISMATCH %s" % claim["unanswerable"]))
for off, on in (("namedfam_off", "namedfam_on"), ("alias_off", "alias_on")):
    for form in ("q_content", "q_hinted"):
        sel = [r for r in rows if r["form"] == form]
        gained = [r["item"] for r in sel if r[on]["hit"] and not r[off]["hit"]]
        lost = [r["item"] for r in sel if r[off]["hit"] and not r[on]["hit"]]
        print("%s vs %s %-10s gained %s lost %s  McNemar p=%.2g" % (on, off, form, gained, lost, mcnemar(len(gained), len(lost))))
print("every claim matches" if not bad else "%d claims do not match" % bad)
