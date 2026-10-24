"""Validate only w467's staged, local draft artifacts."""

import json
from pathlib import Path

root = Path(__file__).resolve().parent
bundle = json.loads((root / "bundle_001.json").read_text(encoding="utf-8"))
assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w467"
assert 0 < len(bundle["entries"]) <= 200
keys = {entry["key"] for entry in bundle["entries"]}
assert len(keys) == len(bundle["entries"])
logical_names = {(entry["namespace"], entry["logical_name"]) for entry in bundle["entries"]}
assert len(logical_names) == len(bundle["entries"])
allowed_kinds = {"definition", "lemma", "theorem", "concept"}
allowed_relations = {
    "depends_on", "defines", "proves", "refutes", "generalizes", "specializes",
    "analogous_to", "cites", "semantic_association",
}
for entry in bundle["entries"]:
    assert entry["kind"] in allowed_kinds
    for field in ("key", "namespace", "logical_name", "title", "statement", "assumptions", "domain", "source"):
        assert field in entry
    if entry["kind"] in {"lemma", "theorem"}:
        assert isinstance(entry["proof_text"], str) and entry["proof_text"].strip()
    else:
        assert entry["proof_text"] is None
    source = entry["source"]
    for field in ("source_id", "url", "revision", "license", "excerpt"):
        assert field in source
    assert source["license"].startswith(("arxiv-nonexclusive", "owner-own-work"))

dependencies = {key: [] for key in keys}
for relation in bundle["relations"]:
    assert relation["kind"] in allowed_relations
    assert relation["from_key"] in keys
    assert bool(relation.get("to_key")) != bool(relation.get("to_existing_logical"))
    if "to_key" in relation:
        assert relation["to_key"] in keys
        if relation["kind"] == "depends_on":
            dependencies[relation["from_key"]].append(relation["to_key"])
    else:
        assert relation["to_existing_logical"].startswith("math:")

visited = set()
active = set()

def visit(key):
    if key in active:
        raise AssertionError("cyclic depends_on relation")
    if key in visited:
        return
    active.add(key)
    for target in dependencies[key]:
        visit(target)
    active.remove(key)
    visited.add(key)

for key in keys:
    visit(key)

for name in ("CLAIMS.jsonl", "REVIEW_PACKET.jsonl", "HOOK_PROPOSALS.jsonl"):
    rows = [json.loads(line) for line in (root / name).read_text(encoding="utf-8").splitlines() if line.strip()]
    assert rows, name
    print(name, len(rows), "valid JSON rows")

json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
patch = (root / "patches" / "01_bundle_001.diff").read_text(encoding="utf-8")
target = "~/math-brain-inbox/w467/bundle_001.json"
assert patch.startswith(f"--- a/{target}\n+++ b/{target}\n")
added = "".join(
    line[1:] for line in patch.splitlines(keepends=True)
    if line.startswith("+") and not line.startswith("+++")
)
assert added == (root / "bundle_001.json").read_text(encoding="utf-8")
print("bundle:", len(bundle["entries"]), "entries,", len(bundle["relations"]), "relations; schema checks passed")
print("patch reproduces byte-identical staged bundle")
