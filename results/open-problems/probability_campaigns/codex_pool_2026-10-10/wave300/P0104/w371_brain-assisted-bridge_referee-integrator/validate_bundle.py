"""Small local draft check; it does not touch the live math store."""
import json
from pathlib import Path

root = Path(__file__).parent
bundle = json.loads((root / "bundle_001.json").read_text(encoding="utf-8"))
assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w371"
entries = bundle["entries"]
assert len(entries) == 3
keys = {e["key"] for e in entries}
assert len(keys) == len(entries)
for entry in entries:
    assert entry["kind"] in {"concept", "definition", "lemma", "theorem"}
    assert entry["statement"] and entry["assumptions"]
    assert bool(entry["proof_text"]) == (entry["kind"] in {"lemma", "theorem"})
    assert entry["source"]["license"].startswith(("arxiv-nonexclusive", "owner-own-work"))
for rel in bundle["relations"]:
    assert rel["from_key"] in keys
    assert (rel.get("to_key") in keys) != bool(rel.get("to_existing_logical"))
    assert rel["kind"] in {"depends_on", "semantic_association"}
assert "F(0)<p_c" in entries[0]["statement"]
assert "oriented" in entries[0]["statement"]
assert "Z^2" in entries[0]["statement"]

# Exact equality case for the sharp two-quantile lemma: p=q=1/4,
# atoms 0,1,2 with masses 1/4,1/2,1/4.
mean = (0 * 0.25) + (1 * 0.5) + (2 * 0.25)
variance = (0 - mean) ** 2 * 0.25 + (1 - mean) ** 2 * 0.5 + (2 - mean) ** 2 * 0.25
bound = (0.25 * 0.25 / (0.25 + 0.25)) * (2 - 0) ** 2
assert variance == bound == 0.5

result = {
    "command": "python -X utf8 validate_bundle.py",
    "entries": len(entries),
    "relations": len(bundle["relations"]),
    "structural_check": "PASS",
    "exact_equality_check": "PASS; variance=bound=0.5",
    "integration": "NOT RUN; live store unchanged",
}
(root / "BUNDLE_VALIDATION.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
