"""Check the saved handoff files are parseable and internally consistent."""
import json
from pathlib import Path

root = Path(r"~\brain_workers\w530")
status = (root / "STATUS.md").read_text(encoding="utf-8")
assert status.startswith("STATE: WORKING\n") or status.startswith("STATE: NEEDS_REVIEW\n")
assert "NEXT: " in status
source = json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
bundle_state = json.loads((root / "BUNDLE_STATE.json").read_text(encoding="utf-8"))
claims = [json.loads(line) for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
assert source["target"] == "P0309"
assert source["source_statement_verified"] and not source["mathematically_complete_statement"]
assert source["current_openness"] == "UNKNOWN"
assert bundle_state["submitted"] and not bundle_state["ingested"] and not bundle_state["retrievable"]
assert all(c["status"] and c["remaining_gap"] and c["independent_reviewer"] for c in claims)
assert (root / "ATTEMPT.md").exists() and (root / "REVIEW.md").exists() and (root / "REPORT.md").exists()
print(f"VALID packet: {len(claims)} claims; source scoped; draft submitted, not ingested")
