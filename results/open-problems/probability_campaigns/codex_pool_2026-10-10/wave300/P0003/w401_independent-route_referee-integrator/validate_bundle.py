"""Read-only handoff validation for the w401 P0003 draft."""

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LOCAL = ROOT / "drafts" / "bundle_001.json"
SUBMITTED = Path("~/math-brain-inbox/w401/bundle_001.json")
PROPOSAL = Path("~/primary_directive/hooks1000/proposals/math-w401.jsonl")

bundle = json.loads(LOCAL.read_text(encoding="utf-8"))
assert bundle == json.loads(SUBMITTED.read_text(encoding="utf-8"))
assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w401"
assert 0 < len(bundle["entries"]) <= 200
keys = {entry["key"] for entry in bundle["entries"]}
assert len(keys) == len(bundle["entries"])
for entry in bundle["entries"]:
    assert entry["kind"] in {"concept", "definition", "lemma", "theorem"}
    assert entry["statement"] and entry["logical_name"] and entry["namespace"]
    if entry["kind"] in {"concept", "definition"}:
        assert entry["proof_text"] is None
    else:
        assert entry["proof_text"]
    source = entry["source"]
    assert all(field in source for field in ("source_id", "url", "revision", "license", "excerpt"))
    assert source["license"].startswith(("arxiv-nonexclusive", "owner-own-work"))
for relation in bundle["relations"]:
    assert relation["from_key"] in keys
    assert relation["kind"] == "semantic_association"
    assert ("to_key" in relation) != ("to_existing_logical" in relation)
    if "to_key" in relation:
        assert relation["to_key"] in keys
    assert relation["rationale"]

claims = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines()]
reviews = [json.loads(line) for line in (ROOT / "REVIEWS.jsonl").read_text(encoding="utf-8").splitlines()]
assert all(row["verdict"] in {"KEEP", "FIX", "DROP"} for row in reviews)
proposal = [json.loads(line) for line in PROPOSAL.read_text(encoding="utf-8").splitlines()]
assert all(re.compile(row["cue"]) and row["fire_when"] and row["silent_when"] for row in proposal)
tracker = json.loads((ROOT / "BUNDLE_TRACKER.json").read_text(encoding="utf-8"))
assert tracker["submitted"] and tracker["reviewed"]
assert not tracker["ingested"] and not tracker["retrievable"]

print(json.dumps({
    "claims": len(claims),
    "reviews": len(reviews),
    "bundle_entries": len(bundle["entries"]),
    "bundle_relations": len(bundle["relations"]),
    "hook_proposals": len(proposal),
    "submitted_copy_equal": True,
    "states": {key: tracker[key] for key in ("submitted", "reviewed", "ingested", "retrievable")},
}, sort_keys=True))
