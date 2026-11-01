"""Record artifact counts and received audit scope; no mathematical experiment."""
from datetime import datetime, timezone
import json
from pathlib import Path

root = Path(__file__).resolve().parent
claims_path = root / "CLAIMS.jsonl"
claims = [json.loads(row) for row in claims_path.read_text(encoding="utf-8").splitlines() if row]
receipt = "~/brain_workers/w439/AUDIT_W438.md"
brain = json.loads((root / "BRAIN_STATE.json").read_text(encoding="utf-8"))
assert brain["submitted"] is True
published = json.loads(Path(brain["submitted_path"]).read_text(encoding="utf-8"))
assert published == json.loads((root / "bundle_001.json").read_text(encoding="utf-8"))
kept = {"w438-C02", "w438-C03", "w438-C04"}
for claim in claims:
    if claim["id"] in kept:
        claim["independent_reviewer"] = f"w439: KEEP, {receipt}; assigned referee w440 still pending"
        claim["independent_audit"] = {"reviewer": "w439", "verdict": "KEEP", "path": receipt}
    if claim["id"] == "w438-C03":
        claim["analytic_lower_bound"] = "theta_(T_2)(p_c)>=(2-1/sqrt(2))/25"
        claim["independent_audit"]["scope"] = "construction, threshold, rates, global extinction; analytic lower bound added after this review and awaits w440"
    if claim["id"] != "w438-C01":
        claim["brain_state"] = "submitted as labelled DRAFT concept material; ingestion/retrieval unconfirmed"
claims_path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in claims), encoding="utf-8")
brain["state_semantics"] = "false review/ingestion/retrieval fields mean not confirmed by this worker, not a fresh global absence query"
brain["peer_review"] = {"reviewer": "w439", "path": receipt, "kept_claims": sorted(kept), "assigned_referee": "w440", "assigned_referee_verdict": "pending", "quasi_isometry_and_new_lower_bound": "not covered by w439 receipt"}
(root / "BRAIN_STATE.json").write_text(json.dumps(brain, indent=2) + "\n", encoding="utf-8")
source = json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
source["independent_review"] = brain["peer_review"]
source["math_store_read"] = {"path": "~/math-brain-build/local/population/brain.sqlite3", "mode": "read-only URI", "scope": "named schema and six critical-percolation title matches only", "result": "Retrieved dated percolation definition and lattice open-problem cards; their dated status is not a current-openness certificate. No exact Codex P0043 ledger row recovered."}
(root / "SOURCE_STATUS.json").write_text(json.dumps(source, indent=2) + "\n", encoding="utf-8")
hook = json.loads((root / "hook_proposal.jsonl").read_text(encoding="utf-8"))
assert len(hook["text"]) <= 300
measurement = {"command": "python -X utf8 finalize_packet.py", "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
               "saved_claim_rows": len(claims), "proved_special_case_rows": sum(row["status"] == "proved special case" for row in claims),
               "unproved_route_rows": sum(row["status"] == "conjecture" for row in claims),
               "submitted_draft_entries": len(published["entries"]), "submitted_relations": len(published["relations"]),
               "published_matches_local": True, "hook_text_characters": len(hook["text"]),
               "own_finite_experiment_status": "NOT_RUN: fresh distress gate held", "live_brain_improvement": "NOT_MEASURED"}
(root / "measurements.json").write_text(json.dumps(measurement, indent=2) + "\n", encoding="utf-8")
print(json.dumps(measurement, indent=2))
