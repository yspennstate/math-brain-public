"""Append problem+attempt rows from a batch json file into the F intake ledger."""
import json, os, sys
from datetime import datetime, timezone
from pathlib import Path
HERE = Path(__file__).resolve().parent
def now(): return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
def append(path, row):
    with path.open("a", encoding="utf-8", newline="\n") as s:
        s.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n"); s.flush(); os.fsync(s.fileno())
batch = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
existing_p = {}
pp = HERE/"problems.jsonl"
if pp.exists():
    for l in pp.read_text(encoding="utf-8").splitlines():
        if l.strip():
            r=json.loads(l); existing_p[r["problem_id"]]=r
seen_dedup = {r.get("dedup_key") for r in existing_p.values()}
seen_loc = {(r["source_id"], r["locator"]) for r in existing_p.values()}
n_p=n_a=0
for item in batch:
    pid = item["problem_id"]
    if pid in existing_p: raise SystemExit(f"duplicate problem_id {pid}")
    key = (item["source_id"], item["locator"])
    if key in seen_loc: raise SystemExit(f"duplicate (source,locator) {key}")
    seen_loc.add(key)
    dk = item.get("dedup_key") or (item["source_id"] + "::" + item["locator"].split(",")[0].strip().lower().replace(" ", "_"))
    if dk in seen_dedup: print(f"note: shared dedup_key {dk} (counts once)")
    seen_dedup.add(dk)
    prow = {"schema":"probability-problem.v1","problem_id":pid,"title":item["title"],
            "source_id":item["source_id"],"locator":item["locator"],"statement":item["statement"],
            "historical_status":item.get("historical_status","source_says_open"),
            "current_status":item.get("current_status","unverified"),
            "status_search":item["status_search"],"admitted":item.get("admitted",True),
            "dedup_key":dk,"result_status":item.get("result_status","attempted_unsolved"),
            "verification":item.get("verification","unreviewed"),
            "intake":"F_20260908","recorded_at":now()}
    if item.get("resolved_by"): prow["resolved_by"]=item["resolved_by"]
    append(pp, prow); n_p+=1
    at = item.get("attempt")
    if at:
        arow = {"schema":"probability-attempt.v1","attempt_id":pid+"-A001","problem_id":pid,
                "author":"claude-prob1000-F-0908","method":at["method"],"result":at["result"],
                "obstruction":at["obstruction"],"key_identity":at.get("key_identity",""),
                "substantive":at.get("substantive",True),"independent_check":at.get("independent_check",""),
                "recorded_at":now()}
        append(HERE/"attempts.jsonl", arow); n_a+=1
print(json.dumps({"problems_appended":n_p,"attempts_appended":n_a}))
