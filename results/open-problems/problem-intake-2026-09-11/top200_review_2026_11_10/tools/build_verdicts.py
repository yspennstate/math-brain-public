"""Merge verdict_overrides.tsv with rows_status.tsv into VERDICTS.tsv (one row per listed problem).

usage: python -I -X utf8 build_verdicts.py rows_status.tsv verdict_overrides.tsv VERDICTS.tsv
Rows with no override are KEEP. Retired rows are passed through as RETIRED with their recorded reason.
"""
import csv, sys
from collections import Counter

rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter="\t"))
ov = {r["id"]: r for r in csv.DictReader(open(sys.argv[2], encoding="utf-8"), delimiter="\t")}
ids = {r["id"] for r in rows}
missing = sorted(set(ov) - ids)
if missing:
    sys.exit("override ids not in the list: " + ", ".join(missing))
out = []
for r in rows:
    if r["list"] == "TOP200_RETIRED":
        v, why = "RETIRED", r["retired_reason"]
    elif r["id"] in ov:
        v, why = ov[r["id"]]["verdict"], ov[r["id"]]["reason"]
    else:
        v, why = "KEEP", ""
    out.append({"list": r["list"], "rank": r["rank"], "id": r["id"], "domain": r["domain"], "title": r["title"],
                "verdict": v, "reason": why, "lit": r["lit"][:200]})
with open(sys.argv[3], "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(out[0].keys()), delimiter="\t", lineterminator="\n")
    w.writeheader()
    w.writerows(out)
c = Counter((o["list"], o["verdict"]) for o in out)
for k in sorted(c):
    print(k[0], k[1], c[k])
