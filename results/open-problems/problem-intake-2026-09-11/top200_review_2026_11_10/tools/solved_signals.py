"""Rows of rows_status.tsv that carry a solved / settled / posted signal, one short line each.
usage: python -I -X utf8 solved_signals.py rows_status.tsv out.txt
"""
import csv, re, sys
rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter="\t"))
pat_l = re.compile(r"^solved|settled|answered|proved|disproved|refuted", re.I)
pat_k = re.compile(r"settled|proved|solved", re.I)
pat_m = re.compile(r"posted|solved|proved|settled|answered|refuted|disproved", re.I)
out = []
for r in rows:
    if pat_l.search(r["lit"]) or pat_k.search(r["move_kinds"]) or pat_m.search(r["memories"]):
        out.append("%s | %s | lit: %s | kinds: %s | mem: %s" % (r["id"], r["title"][:60], r["lit"][:100], r["move_kinds"][:50], r["memories"][:170]))
open(sys.argv[2], "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
print(len(out), "rows with a signal")
