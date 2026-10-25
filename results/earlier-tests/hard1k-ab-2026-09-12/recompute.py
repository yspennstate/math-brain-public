"""Recompute every number in README.md from rows/GRADE_ROWS.json and check it."""
import json, os
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
rows = json.load(open(os.path.join(HERE, "rows", "GRADE_ROWS.json"), encoding="utf-8"))

# family: (n, right without, right with the brain, helped, harmed)
CLAIMS = {
    "op_pagesum": (260, 0, 260, 260, 0),
    "op_pagediff": (150, 0, 150, 150, 0),
    "op_pagemax": (73, 21, 73, 52, 0),
    "op_oddsource": (140, 140, 140, 0, 0),
    "saw": (300, 300, 300, 0, 0),
    "proof_audit": (77, 77, 77, 0, 0),
    "all": (1000, 538, 1000, 462, 0),
}

def group(r):
    if r["kind"] == "proof_audit":
        return "proof_audit"
    return "saw" if r["family"].startswith("saw_") else r["family"]

def tally(sel):
    return (len(sel), sum(r["without"] for r in sel), sum(r["with_brain"] for r in sel),
            sum(r["with_brain"] and not r["without"] for r in sel),
            sum(r["without"] and not r["with_brain"] for r in sel))

def mcnemar(b, c):
    n = b + c
    k = min(b, c)
    return min(1.0, 2 * sum(comb(n, i) for i in range(k + 1)) / 2 ** n)

ok = True
for g, claim in CLAIMS.items():
    got = tally(rows if g == "all" else [r for r in rows if group(r) == g])
    print(f"{g:14s} n={got[0]:5d} without={got[1]:4d} with={got[2]:5d} helped={got[3]:4d} harmed={got[4]}",
          "ok" if got == claim else f"MISMATCH, claimed {claim}")
    ok &= got == claim
p = mcnemar(CLAIMS["all"][3], CLAIMS["all"][4])
print(f"exact McNemar, two-sided: p = {p:.2g}")
ok &= f"{p:.2g}" == "1.7e-139"
print("every claim matches" if ok else "A CLAIM DOES NOT MATCH")
