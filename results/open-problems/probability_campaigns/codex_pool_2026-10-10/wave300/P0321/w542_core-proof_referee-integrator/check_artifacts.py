"""Cheap syntax and relationship checks for the staged P0321 handoff."""

import json
from pathlib import Path


root = Path(__file__).resolve().parent
claims = [json.loads(line) for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines()]
source = json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
bundle = json.loads((root / "brain_bundle_001.json").read_text(encoding="utf-8"))
hook = [json.loads(line) for line in (root / "HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8").splitlines()]
state = json.loads((root / "BUNDLE_STATE.json").read_text(encoding="utf-8"))

assert source["current_openness"] == "UNKNOWN"
assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w542"
keys = {entry["key"] for entry in bundle["entries"]}
assert len(keys) == len(bundle["entries"])
for entry in bundle["entries"]:
    assert entry["namespace"] == "probability.core"
    assert entry["source"]["license"].startswith("owner-own-work")
    assert bool(entry["proof_text"]) == (entry["kind"] == "lemma")
for relation in bundle["relations"]:
    assert relation["from_key"] in keys
    if "to_key" in relation:
        assert relation["to_key"] in keys
    else:
        assert relation["to_existing_logical"].startswith("math:")
assert all(row["id"] for row in claims)
assert len({row["id"] for row in claims}) == len(claims)
assert all(row["proposer"] == "w542" for row in hook)
assert not state["submitted"] and not state["ingested"] and not state["retrievable"]
print(f"valid: {len(claims)} claim rows; {len(bundle['entries'])} entries; {len(bundle['relations'])} relations; {len(hook)} hook")
