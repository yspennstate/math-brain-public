"""Local, read-only structural validation for the P0003 draft bundle."""
import json
from pathlib import Path
import sys

root = Path(__file__).resolve().parent
name = sys.argv[1] if len(sys.argv) > 1 else "bundle_001.json"
bundle = json.loads((root / name).read_text(encoding="utf-8"))
assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w404"
assert len(bundle["entries"]) <= 200
keys = [entry["key"] for entry in bundle["entries"]]
assert len(keys) == len(set(keys))
allowed_kinds = {"definition", "lemma", "theorem", "concept"}
allowed_relations = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
for entry in bundle["entries"]:
    assert entry["kind"] in allowed_kinds
    assert entry["statement"] and entry["source"]["source_id"]
    assert entry["source"]["url"] and entry["source"]["revision"]
    assert entry["source"]["license"].startswith(("owner-own-work", "arxiv-nonexclusive"))
    assert bool(entry["proof_text"]) == (entry["kind"] in {"lemma", "theorem"})
for relation in bundle["relations"]:
    assert relation["kind"] in allowed_relations
    assert relation["from_key"] in keys
    assert (relation.get("to_key") in keys) != bool(relation.get("to_existing_logical"))
    assert relation.get("to_key") != relation["from_key"]
    assert relation["rationale"]
for number, line in enumerate((root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines(), 1):
    try:
        json.loads(line)
    except json.JSONDecodeError as error:
        raise AssertionError(f"CLAIMS.jsonl line {number}: {error}") from error
json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
print(json.dumps({"bundle_entries": len(keys), "relations": len(bundle["relations"]), "claim_rows": number, "json_valid": True, "structure_valid": True}))
