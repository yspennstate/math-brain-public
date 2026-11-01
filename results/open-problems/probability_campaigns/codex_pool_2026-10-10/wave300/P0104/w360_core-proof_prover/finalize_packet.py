"""Record actual audit receipts and the completed local handoff."""
import datetime
import json
import pathlib

root = pathlib.Path(__file__).resolve().parent
claims_path = root / "CLAIMS.jsonl"
claims = [json.loads(line) for line in claims_path.read_text(encoding="utf-8").splitlines() if line.strip()]
reviews = []
for path in [pathlib.Path("~/brain_workers/w361/AUDIT_VERDICTS.jsonl"), pathlib.Path("~/brain_workers/w362/PEER_REVIEWS.jsonl")]:
    with path.open(encoding="utf-8-sig") as stream:
        for line in stream:
            record = json.loads(line)
            if record.get("claim_id") == "w360-C1" and record.get("verdict") == "KEEP":
                reviews.append({"reviewer":record["reviewer"],"review_id":record["review_id"],"verdict":"KEEP","scope":"C1 finite reduction only","path":str(path)})
assert {r["reviewer"] for r in reviews} == {"w361","w362"}
for row in claims:
    if row["claim_id"] == "w360-C1":
        row.update(status="independently checked proof", review_status="KEEP for C1 only", independent_reviews=reviews, account_separation="not verified; no cross-login admission claim")
assert len(claims) == 9
claims_path.write_text("".join(json.dumps(row,ensure_ascii=False)+"\n" for row in claims),encoding="utf-8")
receipt_path = root / "REVIEW_RECEIPT.json"
receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
assert receipt["submitted"] and receipt["exact_controls"] == 205
receipt.update(c1_independent_reviews=reviews, c4_c8_independent_review="pending", progress_event="logged via pd_progress.py --agent w360 --row S1.1", status="NEEDS_REVIEW")
receipt_path.write_text(json.dumps(receipt,indent=2),encoding="utf-8")
(root / "PROGRESS_EVENT.json").write_text(json.dumps({"agent":"w360","row":"S1.1","event":"P0104 robust-margin special case and first-order floor bridge; 205 exact controls; 3 concept DRAFTs submitted, crossover unproved","evidence":str(root/"REVIEW_PACKET.md"),"result":"logged"},indent=2),encoding="utf-8")
required = ["STATUS.md","SOURCE_STATUS.json","ATTEMPT.md","CLAIMS.jsonl","REPORT.md","REVIEW_PACKET.md","MEASUREMENTS.json","COMPUTE_GATE.json","REVIEW_RECEIPT.json","drafts/bundle_001.json","patches/01_p0104_draft_bundle.diff","hooks/math-w360.jsonl"]
assert all((root/name).is_file() and (root/name).stat().st_size>0 for name in required)
source = json.loads((root/"SOURCE_STATUS.json").read_text(encoding="utf-8"))
assert source["current_openness"] == "UNKNOWN" and not source["parent_problem_solved"]
report_path = root/"REPORT.md"
report = report_path.read_text(encoding="utf-8")
report += "\nIndependent audit receipts: C1 has KEEP from w361-A001 and w362-R002. C4/C8 and the complete continuous packet await w362. Account separation was not verified and no admission count is claimed. Progress event logged.\n"
report_path.write_text(report,encoding="utf-8")
print(json.dumps({"deliverables_present":len(required),"claim_rows":9,"submitted_concept_drafts":3,"exact_controls":205,"c1_keep_receipts":2,"c4_c8_review":"pending","parent_solved":False,"ready_for_status":"NEEDS_REVIEW"}))
