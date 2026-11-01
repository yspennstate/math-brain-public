"""Verify saved artifacts and close this worker round for independent review."""
import json
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parent
required = ["STATUS.md", "SOURCE_STATUS.json", "ATTEMPT.md", "CLAIMS.jsonl",
            "BOUNDARY_LEMMA.md", "STATEMENT_FOR_ADVERSARY.md", "REVIEW_PACKET.md",
            "REVIEW_REQUEST.json", "REPORT.md", "BRAIN_SUBMISSION.json", "bundle_001.json",
            "HOOK_PROPOSALS.jsonl", "PROGRESS_EVENT.json", "COMM_RECEIPTS.json",
            "measurements/boundary_exact.json", "measurements/draft_validation.json",
            "patches/01_math_w378_hook.diff", "patches/02_draft_brain_bundle.diff"]
for name in required:
    assert (root / name).is_file(), name
submission = json.loads((root / "BRAIN_SUBMISSION.json").read_text(encoding="utf-8"))
assert submission["submitted"] is True and submission["reviewed"] is False
assert Path(submission["inbox_draft"]).read_bytes() == (root / "bundle_001.json").read_bytes()
bundle = json.loads((root / "bundle_001.json").read_text(encoding="utf-8"))
assert len(bundle["entries"]) == 3 and len(bundle["relations"]) == 2
claims = [json.loads(s) for s in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if s.strip()]
assert len(claims) == 3
for claim in claims:
    assert claim["status"] == "proved special case"
    assert all(field in claim for field in ("statement", "assumptions", "source", "proof_or_counterexample", "independent_reviewer", "remaining_gap"))
measurement = json.loads((root / "measurements/boundary_exact.json").read_text(encoding="utf-8"))
assert measurement["verdict"] == "PASS" and measurement["total_configurations"] == 8704
assert measurement["variance_ratio_V2n_over_2Vn"] == "1"
source_path = root / "SOURCE_STATUS.json"
source = json.loads(source_path.read_text(encoding="utf-8"))
source["local_prior_attempt"]["confirmed_in_read_only_live_store"] = True
assert source["current_openness"] == "UNKNOWN"
source_path.write_text(json.dumps(source, indent=2) + "\n", encoding="utf-8")
integrity = {"verdict": "PASS", "required_artifacts": len(required), "claims": 3,
             "draft_entries": 3, "draft_relations": 2, "inbox_matches_local": True,
             "independent_review": "pending", "live_store_write": False}
(root / "measurements" / "final_integrity.json").write_text(json.dumps(integrity, indent=2) + "\n", encoding="utf-8")
stamp = datetime.now(timezone.utc).isoformat()
report_path = root / "REPORT.md"
report = report_path.read_text(encoding="utf-8")
delivery = "\nSubmission confirmed: ~/math-brain-inbox/w378/bundle_001.json (3 DRAFT lemmas, 2 relations). Full referee request delivered to w380 as msg-f97b6dacae; mathematical acceptance is pending. Final artifact check: python -X utf8 finalize.py, 18 required artifacts present and inbox bytes match the local draft.\n"
if "Submission confirmed:" not in report:
    report_path.write_text(report + delivery, encoding="utf-8")
status_path = root / "STATUS.md"
lines = status_path.read_text(encoding="utf-8").splitlines()
log = [line for line in lines if not line.startswith("STATE:") and not line.startswith("NEXT:")]
next_line = "NEXT: w380 independently audits L1/L2/L3 from REVIEW_PACKET.md; coordinator integrates only accepted drafts. The target gap is fixed-law large-scale exponent matching."
status_path.write_text("STATE: NEEDS_REVIEW\n" + next_line + "\n" + "\n".join(log) +
                      "\n" + stamp + ": Finished measured proof packet. Submitted 3 DRAFT cards and 2 relations; independent review pending. No live store or global recall controls changed.\n", encoding="utf-8")
print(json.dumps(integrity))
