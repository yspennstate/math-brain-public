"""Read-only structural validation for this worker's P0003 draft packet."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUNDLE = json.loads((ROOT / "bundle_001.json").read_text(encoding="utf-8"))
assert BUNDLE["spec"] == "mathbrain-draft-v1"
assert BUNDLE["author_agent"] == "w407"
assert len(BUNDLE["entries"]) <= 200
keys = {e["key"] for e in BUNDLE["entries"]}
assert len(keys) == len(BUNDLE["entries"])
allowed_kinds = {"definition", "lemma", "theorem", "concept"}
allowed_relations = {
    "depends_on", "defines", "proves", "refutes", "generalizes",
    "specializes", "analogous_to", "cites", "semantic_association",
}
for entry in BUNDLE["entries"]:
    assert entry["kind"] in allowed_kinds
    assert entry["statement"] and entry["namespace"] and entry["logical_name"]
    if entry["kind"] in {"lemma", "theorem"}:
        assert entry["proof_text"]
    else:
        assert entry["proof_text"] is None
    source = entry["source"]
    assert all(k in source for k in ("source_id", "url", "revision", "license", "excerpt"))
    if source["url"].startswith("C:/") and source["excerpt"]:
        assert source["excerpt"] in Path(source["url"]).read_text(encoding="utf-8")
for rel in BUNDLE["relations"]:
    assert rel["from_key"] in keys and rel["to_key"] in keys
    assert rel["kind"] in allowed_relations and rel["rationale"]
dependencies = {key: set() for key in keys}
for rel in BUNDLE["relations"]:
    if rel["kind"] == "depends_on":
        dependencies[rel["from_key"]].add(rel["to_key"])

def walk(key, path):
    assert key not in path, "cyclic depends_on relation"
    for next_key in dependencies[key]:
        walk(next_key, path | {key})

for key in keys:
    walk(key, set())
claims = [json.loads(s) for s in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8-sig").splitlines() if s.strip()]
for claim in claims:
    assert all(k in claim for k in ("statement", "assumptions", "source", "proof_or_counterexample", "independent_reviewer", "remaining_gap", "status"))
json.loads((ROOT / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
json.loads((ROOT / "RETRIEVAL_EVIDENCE.json").read_text(encoding="utf-8"))
print(f"PASS entries={len(keys)} relations={len(BUNDLE['relations'])} claims={len(claims)}")
