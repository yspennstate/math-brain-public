"""Print chosen fields of chosen rows of list.jsonl.
usage: python -I -X utf8 show_rows.py list.jsonl "T004,T067" "statement,where_it_stands" [width]
"""
import json, sys
want = set(sys.argv[2].split(","))
fields = sys.argv[3].split(",")
width = int(sys.argv[4]) if len(sys.argv) > 4 else 400
for l in open(sys.argv[1], encoding="utf-8"):
    if not l.strip():
        continue
    r = json.loads(l)
    if r["problem_id"] in want:
        print("==", r["problem_id"], r.get("list"), "|", r["title"])
        for f in fields:
            print("  %s: %s" % (f, " ".join(str(r.get(f) or "").split())[:width]))
