from pathlib import Path
import difflib
import json

root = Path(__file__).resolve().parent
required = ["STATUS.md", "SOURCE_STATUS.json", "ATTEMPT.md", "CLAIMS.jsonl",
            "REPORT.md", "REVIEW_PACKET.md", "PEER_AUDIT.md", "MEASUREMENTS.json",
            "SUBMISSION_STATE.json", "DRAFT_VALIDATION.json", "RELATIONS_EVIDENCE.jsonl"]
assert all((root / p).is_file() for p in required)
claims = [json.loads(line) for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
assert len(claims) == 8 and len({c["claim_id"] for c in claims}) == 8
assert all(all(c.get(k) for k in ("statement", "assumptions", "source", "proof_or_counterexample", "independent_reviewer", "remaining_gap", "status")) for c in claims)
allowed_statuses = {"conjecture", "numerical evidence", "sketch", "proved special case", "independently checked proof"}
assert all(c["status"] in allowed_statuses for c in claims)
for p in ("SOURCE_STATUS.json", "MEASUREMENTS.json", "SUBMISSION_STATE.json", "DRAFT_VALIDATION.json"):
    json.loads((root / p).read_text(encoding="utf-8"))
local = (root / "bundle_001.json").read_text(encoding="utf-8")
inbox = Path("~/math-brain-inbox/w376/bundle_001.json")
assert inbox.read_text(encoding="utf-8") == local
hook_path = root / "hook_proposals" / "probability-w376.jsonl"
hook_text = hook_path.read_text(encoding="utf-8")
hooks = [json.loads(line) for line in hook_text.splitlines() if line.strip()]
assert len(hooks) == 1
hook = hooks[0]
assert set(hook) == {"id", "area", "event", "cue", "fire_when", "silent_when", "text", "evidence", "proposer"}
assert len(hook["text"]) <= 300 and hook["area"] == "math"
live = "primary_directive/hooks1000/proposals/probability-w376.jsonl"
diff = "".join(difflib.unified_diff([], hook_text.splitlines(keepends=True), fromfile="a/" + live, tofile="b/" + live))
(root / "patches" / "02_p0110_hook_proposal.diff").write_text(diff, encoding="utf-8")
receipt = {"required_files_present": len(required), "claim_rows": len(claims),
           "all_required_claim_fields_present": True, "submitted_bundle_matches_local": True,
           "local_hook_proposals": len(hooks), "hook_text_characters": len(hook["text"]),
           "hook_schema_fields_valid": True, "math_referee_review_pending": True,
           "formal_proof_receipt": None, "live_brain_store_writes": 0}
(root / "PACKET_VALIDATION.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))
