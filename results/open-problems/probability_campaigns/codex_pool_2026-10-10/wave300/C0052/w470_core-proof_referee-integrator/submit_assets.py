"""Validate and stage this worker's authorized brain and hook drafts."""

import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
source = root / "bundle_001.json.part"
bundle = json.loads(source.read_text(encoding="utf-8"))
assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w470"
keys = {entry["key"] for entry in bundle["entries"]}
assert len(keys) == len(bundle["entries"])
for entry in bundle["entries"]:
    assert entry["namespace"] == "probability.statmech"
    assert entry["kind"] in {"definition", "concept"}
    assert entry["proof_text"] is None
    assert entry["source"]["license"].startswith("arxiv-nonexclusive")
for edge in bundle["relations"]:
    assert edge["from_key"] in keys
    assert edge.get("to_key") in keys or edge.get("to_existing_logical", "").startswith("math:probability.statmech:")
    assert edge["kind"] in {"defines", "semantic_association"}

destination = Path("~/math-brain-inbox/w470")
destination.mkdir(parents=True, exist_ok=True)
partial = destination / "bundle_001.json.part"
final = destination / "bundle_001.json"
assert not final.exists(), "Use a new bundle name to avoid overwriting an integrated draft"
data = source.read_bytes()
partial.write_bytes(data)
partial.replace(final)
assert final.read_bytes() == data

hook_path = Path("~/primary_directive/hooks1000/proposals/math-w470.jsonl")
hook = {
    "id": "math-w470-01",
    "area": "math",
    "event": "Stop",
    "cue": r"(?is)\b(C0052|three-dimensional Ising)\b.{0,200}\b(proved|solved|nontriviality follows)\b",
    "fire_when": "An agent reports C0052 solved after deriving a second-moment plan while the current-overlap variance estimate is still open.",
    "silent_when": "An agent reports only a conditional C0052 reduction and explicitly leaves the original-current overlap estimate open.",
    "text": "Before claiming 3D Ising nontriviality, check the source-normalized g(beta) and the hardest original-current overlap estimate. A second-moment route with its variance bound open is not a proof.",
    "evidence": "memory:perceptron_proof_open_gaps_fleet_2026_07_12; probability_1000_intake_claude_20260907/attempts.jsonl:42",
    "proposer": "w470",
}
assert len(hook["text"]) <= 300
existing = hook_path.read_text(encoding="utf-8") if hook_path.exists() else ""
if not any(json.loads(line).get("id") == hook["id"] for line in existing.splitlines() if line.strip()):
    with hook_path.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(hook, ensure_ascii=False) + "\n")

receipt = {
    "bundle_path": str(final),
    "bundle_sha256": hashlib.sha256(data).hexdigest(),
    "entries": len(bundle["entries"]),
    "relations": len(bundle["relations"]),
    "hook_path": str(hook_path),
    "hook_id": hook["id"],
    "state": "submitted_draft_not_ingested",
}
(root / "SUBMISSION.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps(receipt, indent=2))
