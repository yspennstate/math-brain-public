"""Structural validation only; this does not certify mathematical truth or ingest a bundle."""

import json
from pathlib import Path

root = Path(__file__).parent
source = json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
assert source["problem_id"] == "C0120"

for name, expected in (("CLAIMS.jsonl", 2), ("REVIEW_ROWS.jsonl", 6)):
    rows = [json.loads(line) for line in (root / name).read_text(encoding="utf-8").splitlines() if line.strip()]
    assert len(rows) == expected, (name, len(rows))

bundle = json.loads((root / "bundle_001.json").read_text(encoding="utf-8"))
assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w500"
entries = bundle["entries"]
assert 0 < len(entries) <= 200
keys = [entry["key"] for entry in entries]
assert len(keys) == len(set(keys))

required = {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"}
for entry in entries:
    assert required <= entry.keys(), entry.get("key")
    assert entry["kind"] in {"definition", "lemma", "theorem", "concept"}
    if entry["kind"] in {"lemma", "theorem"}:
        assert isinstance(entry["proof_text"], str) and entry["proof_text"].strip()
    else:
        assert entry["proof_text"] is None
    assert {"source_id", "url", "revision", "license", "excerpt"} <= entry["source"].keys()
    assert entry["source"]["license"].startswith("owner-own-work")

allowed = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
for relation in bundle["relations"]:
    assert relation["from_key"] in keys and relation["to_key"] in keys
    assert relation["kind"] in allowed
    assert relation["from_key"] != relation["to_key"]

dependency = {key: [] for key in keys}
for relation in bundle["relations"]:
    if relation["kind"] == "depends_on":
        dependency[relation["from_key"]].append(relation["to_key"])

def visit(node, active, done):
    if node in active:
        raise AssertionError("depends_on cycle")
    if node in done:
        return
    active.add(node)
    for target in dependency[node]:
        visit(target, active, done)
    active.remove(node)
    done.add(node)

done = set()
for key in keys:
    visit(key, set(), done)

print(f"validated: {len(entries)} draft entries, {len(bundle['relations'])} relations, 6 review rows, 2 claim rows")
