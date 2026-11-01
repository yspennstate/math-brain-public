"""Read-only handoff consistency check; no proof or store-ingest claim."""
import json
from pathlib import Path

root = Path(__file__).parent
assert (root / "STATUS.md").read_text(encoding="utf-8").splitlines()[0] in {"STATE: WORKING", "STATE: NEEDS_REVIEW"}
assert "NEXT:" in (root / "STATUS.md").read_text(encoding="utf-8")
source = json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
assert source["current_openness"] == "CLAIMED_RESOLVED_PENDING_INDEPENDENT_PROOF_AUDIT"
claims = [json.loads(line) for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
assert len({c["id"] for c in claims}) == len(claims)
assert all({"statement", "assumptions", "source", "proof_or_counterexample", "independent_reviewer", "remaining_gap", "status"} <= c.keys() for c in claims)
audits = [c for c in claims if c.get("type") == "audit-verdict"]
assert len(audits) == 8 and sum(c["verdict"] == "KEEP" for c in audits) == 7 and sum(c["verdict"] == "FIX" for c in audits) == 1
bundle = (root / "drafts" / "bundle_001.json").read_bytes()
inbox = Path("~/math-brain-inbox/w449/bundle_001.json")
assert inbox.read_bytes() == bundle
state = json.loads((root / "SUBMISSION_STATE.json").read_text(encoding="utf-8"))
assert state["submitted"] and not state["reviewed"] and not state["ingested"] and not state["retrievable"]
hook_local = (root / "proposals" / "math-w449.jsonl").read_text(encoding="utf-8").strip()
hook_global = Path("~/primary_directive/hooks1000/proposals/math-w449.jsonl").read_text(encoding="utf-8")
assert hook_local in hook_global
assert json.loads(hook_local)["proposer"] == "w449"
print(f"handoff valid: {len(claims)} claim/status rows, {len(audits)} scoped KEEP verdicts, {len(bundle)} inbox bytes, 1 hook proposal")
