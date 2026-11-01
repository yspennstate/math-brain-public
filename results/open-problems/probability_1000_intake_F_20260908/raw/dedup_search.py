"""Keyword search over every problems.jsonl of intakes A-E (Codex tree + claude 0907 + D + E)."""
import json, glob, re, sys, os
files = glob.glob(r"~\<private-repo>\06_math_research\probability_1000_intake_*\problems.jsonl") + [r"~\Downloads\Probability_1000_20h_20260906\problems.jsonl"]
files=[f for f in files if "intake_F_" not in f]
rows=[]
for f in files:
    for l in open(f,encoding="utf-8"):
        if l.strip():
            r=json.loads(l); r["_file"]=os.path.basename(os.path.dirname(f)); rows.append(r)
if __name__=="__main__":
    for kw in sys.argv[1:]:
        pat=re.compile(kw,re.I); hits=[r for r in rows if pat.search(r.get("statement","")+" "+r.get("title",""))]
        print(f"## {kw}: {len(hits)} hits")
        for r in hits[:12]:
            print("  ",r["problem_id"],r["source_id"],"|",r["locator"][:40],"|",r["title"][:90])
