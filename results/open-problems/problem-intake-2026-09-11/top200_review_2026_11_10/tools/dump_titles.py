"""Print rank, id, domain and title (and optionally a field) for one list of list.jsonl.
usage: python -I -X utf8 dump_titles.py list.jsonl LISTNAME out.txt [field width]
"""
import json, sys
rows = [json.loads(l) for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
rows = [r for r in rows if r.get("list") == sys.argv[2]]
rows.sort(key=lambda r: r.get("rank") or 0)
field = sys.argv[4] if len(sys.argv) > 4 else ""
width = int(sys.argv[5]) if len(sys.argv) > 5 else 120
out = []
for r in rows:
    s = "%s %s [%s] %s" % (r.get("rank"), r["problem_id"], r.get("domain_name") or r.get("domain"), r["title"])
    if field:
        s += " || " + " ".join(str(r.get(field) or "").split())[:width]
    out.append(s)
open(sys.argv[3], "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
print(len(out))
