import json, sys
P = r"~\brain-repo\06_math_research\top200_probability_2026_10_14\list.jsonl"
want = set(sys.argv[1:])
for line in open(P, encoding="utf-8"):
    line = line.strip()
    if not line:
        continue
    r = json.loads(line)
    i = r.get("id") or r.get("problem_id") or r.get("tid")
    if i in want:
        keys = [k for k in r if k not in ("statement", "why_important", "title")]
        print(i, "|", r.get("title"))
        for k in keys:
            v = r[k]
            if isinstance(v, str) and len(v) > 0 and k not in ("id",):
                print("   ", k, ":", v[:700])
            elif not isinstance(v, str):
                print("   ", k, ":", str(v)[:200])
