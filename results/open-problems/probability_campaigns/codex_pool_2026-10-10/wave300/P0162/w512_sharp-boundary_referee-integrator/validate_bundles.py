"""Read-only structural validation of the P0162 draft bundle handoff."""

import json
from pathlib import Path


paths = [
    Path("~/math-brain-inbox/w510/bundle_001.json"),
    Path("~/math-brain-inbox/w511/bundle_002.json"),
    Path("~/brain_workers/w512/DRAFT_BUNDLE.json"),
]
allowed_kinds = {"definition", "lemma", "theorem", "concept"}
allowed_relations = {
    "depends_on", "defines", "proves", "refutes", "generalizes",
    "specializes", "analogous_to", "cites", "semantic_association",
}
bundles = [json.loads(path.read_text(encoding="utf-8")) for path in paths]
global_names = {
    f"math:{entry['namespace']}:{entry['logical_name']}"
    for bundle in bundles for entry in bundle["entries"]
}
for path, bundle in zip(paths, bundles):
    assert bundle["spec"] == "mathbrain-draft-v1"
    assert len(bundle["entries"]) <= 200
    local_keys = {entry["key"] for entry in bundle["entries"]}
    assert len(local_keys) == len(bundle["entries"])
    for entry in bundle["entries"]:
        assert entry["kind"] in allowed_kinds
        for field in ("key", "namespace", "logical_name", "title", "statement",
                      "proof_text", "assumptions", "domain", "source"):
            assert field in entry, (path, field)
        if entry["kind"] in {"lemma", "theorem"}:
            assert entry["proof_text"], (path, entry["key"])
        else:
            assert entry["proof_text"] is None, (path, entry["key"])
        assert entry["source"]["license"].startswith("owner-own-work")
    for rel in bundle["relations"]:
        assert rel["from_key"] in local_keys
        assert rel["kind"] in allowed_relations
        assert rel.get("rationale")
        if "to_key" in rel:
            assert rel["to_key"] in local_keys
        else:
            assert rel["to_existing_logical"] in global_names
    print(f"{path.parent.name}: {len(bundle['entries'])} entries, "
          f"{len(bundle['relations'])} relations, local endpoints valid")
