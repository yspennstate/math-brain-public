import json
from datetime import datetime, timezone
from pathlib import Path

base = Path(__file__).resolve().parent
required = ["STATUS.md", "SOURCE_STATUS.json", "ATTEMPT.md", "CLAIMS.jsonl", "REVIEW_PACKET.md", "REPORT.md", "SIMPLEX_PROOF.md", "REFEREE_VERDICTS.json", "MEASUREMENTS.json", "POLYNOMIAL_CHECK.json", "BUNDLE_VALIDATION.json", "PATCH_VALIDATION.json", "BRAIN_DELIVERY.json", "DEDUP_MAP.json", "RELATION_EVIDENCE.jsonl", "PUBLISH_PROGRESS.ps1"]
for name in required:
    assert (base / name).is_file(), name
claims = [json.loads(line) for line in (base / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line]
assert len(claims) == 5 and len({row["id"] for row in claims}) == 5
for row in claims:
    assert all(field in row for field in ("statement", "assumptions", "source", "proof", "independent_reviewer", "remaining_gap", "status"))
    assert row["status"] == "independently checked proof"
validation = json.loads((base / "BUNDLE_VALIDATION.json").read_text(encoding="utf-8"))
draft = json.loads((base / "drafts" / "bundle_001.json").read_text(encoding="utf-8"))
assert validation["errors"] == [] and validation["validated_payload"] == draft
assert len(draft["entries"]) == 2 and len(draft["relations"]) == 3
assert all(row["kind"] == "concept" and row["proof_text"] is None for row in draft["entries"])
patches = json.loads((base / "PATCH_VALIDATION.json").read_text(encoding="utf-8"))["receipts"]
assert len(patches) == 2 and all(row["exit_code"] == 0 for row in patches)
delivery_path = base / "BRAIN_DELIVERY.json"
delivery = json.loads(delivery_path.read_text(encoding="utf-8"))
assert delivery["submitted"]["complete"] is True
assert delivery["integration_attempted"] is False
inbox = Path(delivery["submitted"]["file"])
present = inbox.exists()
if present:
    assert json.loads(inbox.read_text(encoding="utf-8")) == draft
delivery["ingested"] = {"complete": False, "status": "not verified; validating coordinator admission pending"}
delivery["retrievable"] = {"complete": False, "status": "not verified; no claim of global recall impact"}
delivery["reviewed"]["additional_general_family_row"] = "claim 005: w355 independently checked Section 5; explicit w356 unit verdict requested in msg-e1d07dab85"
delivery_path.write_text(json.dumps(delivery, indent=2), encoding="utf-8")
receipt = {"checked_at": datetime.now(timezone.utc).isoformat(), "required_artifacts": len(required), "claims": 5, "referee_claim_keeps": 4, "additional_general_family_review": "w355 complete-proof KEEP; explicit w356 row pending", "schema_errors": 0, "concepts": 2, "relations": 3, "patch_checks_passed": 2, "submitted": True, "inbox_copy_present": present, "ingestion_verified": False, "retrieval_verified": False, "formal_proof_claimed": False, "full_kls_proof_claimed": False, "hook": "staged, not globally posted", "progress": "command staged, not posted because worker write scope excludes those outputs"}
(base / "FINAL_CHECK.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps(receipt, indent=2))
status_path = base / "STATUS.md"
status = status_path.read_text(encoding="utf-8")
lines = status.splitlines()
lines[0] = "STATE: NEEDS_REVIEW"
for index, line in enumerate(lines):
    if line.startswith("NEXT:"):
        lines[index] = "NEXT: Coordinator admits the deduplicated draft and staged hook; test any transverse-energy decorrelation estimate against the saved exact polynomial family."
lines.append(f"{receipt['checked_at']}: Final handoff complete: five saved claims, four w356 KEEP units plus w355 general-family audit; two concepts and three relations submitted; schema and both patch checks pass. Global ingestion/retrieval remain unverified; hook and progress command are staged for the reviewer.")
status_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
