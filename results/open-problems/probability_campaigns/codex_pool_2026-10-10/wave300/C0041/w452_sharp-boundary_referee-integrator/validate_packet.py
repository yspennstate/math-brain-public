"""Static checks for the staged C0041 draft; never opens a live store."""

import json
from pathlib import Path


root = Path(__file__).parent
bundle = json.loads((root / "bundle_001.json").read_text(encoding="utf-8"))
source = json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
claims = [json.loads(line) for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line]
hooks = [json.loads(line) for line in (root / "hook_proposal.jsonl").read_text(encoding="utf-8").splitlines() if line]

assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w452"
assert source["candidate_id"] == "C0041"
assert len(bundle["entries"]) <= 200
keys = {entry["key"] for entry in bundle["entries"]}
assert len(keys) == len(bundle["entries"])
for entry in bundle["entries"]:
    assert entry["kind"] in {"definition", "lemma", "theorem", "concept"}
    assert entry["source"]["license"].startswith(("owner-own-work", "apache-2.0"))
    assert bool(entry["proof_text"]) == (entry["kind"] in {"lemma", "theorem"})
    assert all(entry[field] for field in ("key", "namespace", "logical_name", "title", "statement", "domain"))
for relation in bundle["relations"]:
    assert relation["from_key"] in keys and relation["to_key"] in keys
    assert relation["kind"] in {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
    assert relation["rationale"]
for claim in claims:
    assert claim["status"] in {"conjecture", "numerical evidence", "sketch", "proved special case", "independently checked proof"}
    assert all(field in claim for field in ("statement", "assumptions", "source", "proof_or_counterexample", "independent_reviewer", "remaining_gap", "status"))
for hook in hooks:
    assert len(hook["text"]) <= 300
    assert all(hook[field] for field in ("fire_when", "silent_when", "evidence"))
print(f"PASS: {len(bundle['entries'])} draft cards, {len(bundle['relations'])} relations, {len(claims)} claim rows, {len(hooks)} hook proposal")
