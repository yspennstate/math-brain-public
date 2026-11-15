import json, sys
rows = [json.loads(l) for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
for r in rows:
    if r.get("list") == "TOP200_RETIRED":
        print("%s | %s | %s" % (r["problem_id"], r["title"][:60], " ".join(str(r.get("retired_reason")).split())[:int(sys.argv[2])]))
