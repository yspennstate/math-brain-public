"""Validate the local referee packet and submitted draft state only."""
import json
from pathlib import Path

root = Path("~/brain_workers/w506")
claims = [json.loads(line) for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
assert len(claims) == len({row["id"] for row in claims})
needed = {"assumptions", "source", "proof_or_counterexample", "independent_reviewer", "remaining_gap", "status"}
for row in claims:
    assert "statement" in row or "claim" in row, row["id"]
    assert needed <= set(row), (row["id"], sorted(needed-set(row)))
assert all(row["verdict"] in {"KEEP", "FIX", "DROP"} for row in claims if row["kind"] == "audit_verdict")
source = json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
assert source["current_openness"] == "UNKNOWN" and source["novelty_claim"] is False
bundle = json.loads((root / "DRAFT_BUNDLE.json").read_text(encoding="utf-8"))
withdrawn = Path("~/math-brain-inbox/w506/bundle_001.withdrawn.part")
assert json.loads(withdrawn.read_text(encoding="utf-8")) == bundle
assert not Path("~/math-brain-inbox/w506/bundle_001.json").exists()
state = json.loads((root / "BUNDLE_STATE.json").read_text(encoding="utf-8"))
assert not state["submitted"] and state["previously_submitted"] and state["withdrawn"]
assert state["reviewed"] and state["review_verdict"].startswith("FIX")
assert not state["ingested"] and not state["retrievable"]
hooks = [json.loads(line) for line in (root / "HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
assert len(hooks) == 1 and len(hooks[0]["text"]) <= 300
print(f"claims={len(claims)} withdrawn_bundle_entries={len(bundle['entries'])} relations={len(bundle['relations'])} hooks={len(hooks)} statuses=honest")
