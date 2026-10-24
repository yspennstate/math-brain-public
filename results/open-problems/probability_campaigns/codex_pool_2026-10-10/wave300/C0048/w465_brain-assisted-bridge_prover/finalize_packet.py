"""Local evidence indexing and exact relation-end quotes; no cryptographic source ceremony."""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
bundle=json.loads((ROOT/"drafts/bundle_001.json").read_text(encoding="utf-8"))
entries={entry["key"]:entry for entry in bundle["entries"]}
cards=json.loads((ROOT/"evidence/returned_cards.json").read_text(encoding="utf-8"))["returned_cards"]
live={card["metadata"].get("logical_id"):card for card in cards}
rows=[]
for number,relation in enumerate(bundle["relations"],start=1):
    left=entries[relation["from_key"]]
    right=entries[relation["to_key"]] if relation.get("to_key") else live[relation["to_existing_logical"]]
    rows.append({"id":f"w465-E{number}","kind":relation["kind"],"from":left["logical_name"],"to":right.get("logical_name",relation.get("to_existing_logical")),"from_quote":left["statement"],"to_quote":right.get("statement",right.get("body")),"rationale":relation["rationale"],"status":"draft","independent_reviewer":"w467 pending","support":"Both exact relation ends checked locally; no independent mathematical audit or live ingestion claimed."})
(ROOT/"EDGES.jsonl").write_text("".join(json.dumps(row,ensure_ascii=False)+"\n" for row in rows),encoding="utf-8")
source=json.loads((ROOT/"SOURCE_STATUS.json").read_text(encoding="utf-8"))
source["checks"]["owner_solved_retired"]="Targeted rg found no C0048/Potts match in Open problem project/solved_register.md or the available relevant project README indexes. This bounded negative check is not exhaustive; current openness remains UNKNOWN."
source["brain_store_snapshot"]={"database":"~/math-brain-build/local/population/brain.sqlite3","read_mode":"ro","target_rank":1,"prior_attempt_rank":2,"returned_cards_receipt":"evidence/returned_cards.json","primary_source_fields_checked":True}
(ROOT/"SOURCE_STATUS.json").write_text(json.dumps(source,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
# Review-file hashes identify immutable reviewer inputs, not source manifests or proof receipts.
files=["STATEMENT_ONLY.md","SOURCE_STATUS.json","ATTEMPT.md","CLAIMS.jsonl","EDGES.jsonl","REVIEW_PACKET.md","evidence/bridge_checks.json","evidence/returned_cards.json"]
review_index={"purpose":"review-artifact integrity only; not a mathematical proof or integrator source manifest","files":[{"path":str(ROOT/name),"sha256":hashlib.sha256((ROOT/name).read_bytes()).hexdigest()} for name in files],"author_served_model_evidence":"unavailable","parent_problem_status":"unproved","reviewer":"w467 pending"}
(ROOT/"REVIEW_INDEX.json").write_text(json.dumps(review_index,indent=2)+"\n",encoding="utf-8")
assert 2**73>3**36
print(json.dumps({"relation_rows":len(rows),"review_index":"REVIEW_INDEX.json","exact_allowance_comparison":"2^73 > 3^36 PASS","parent_problem_proved":False}))
