"""Print rows a..b of the top-200 list compactly for the deserve pass. an agent."""
import json, sys
p = sys.argv[1]; a = int(sys.argv[2]); b = int(sys.argv[3]); n = int(sys.argv[4]) if len(sys.argv) > 4 else 260
rows = [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]
if a == 0:
    print(len(rows), sorted(rows[0].keys())); sys.exit(0)
for r in rows[a - 1:b]:
    st = (r.get("statement") or r.get("problem") or "")
    print("%s | %s | %s | %s | %s" % (r.get("problem_id"), r.get("list"), r.get("domain"), r.get("title"), " ".join(str(st).split())[:n]))
