import json, glob, statistics as st
rows = {}
for f in glob.glob("pmrca_eps*.jsonl"):
    for line in open(f, encoding="utf-8"):
        r = json.loads(line); key = (r["eps"], r["h"], r.get("HALF", 10.0))
        rows.setdefault(key, []).append(r)
print("eps    h      strip  n   PMRCA mean (se)     all-meetings mean   PMRCA*: eps x all-meetings")
for key in sorted(rows, key=lambda k: (-k[1], k[0])):
    rs = rows[key]; p = [r["pmrca"] for r in rs]; m = [r["meet_all"] for r in rs]
    se = st.stdev(p)/len(p)**0.5 if len(p) > 1 else float('nan')
    print(f"{key[0]:<6} {key[1]:<6} {key[2]:<6} {len(p):<3} {st.mean(p):7.1f} ({se:4.1f})       {st.mean(m):8.1f}            {key[1]*st.mean(m):6.2f}")
