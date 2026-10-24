"""Read-only structural gate for this draft; does not ingest the math store."""
import json
from pathlib import Path

p = Path(__file__).parent / "drafts" / "bundle_001.json"
bundle = json.loads(p.read_text(encoding="utf-8"))
assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w449"
assert 0 < len(bundle["entries"]) <= 200
entries = {entry["key"]: entry for entry in bundle["entries"]}
assert len(entries) == len(bundle["entries"])

required = {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"}
for e in entries.values():
    assert required <= e.keys()
    assert e["kind"] in {"definition", "lemma", "theorem", "concept"}
    assert e["proof_text"] if e["kind"] in {"lemma", "theorem"} else e["proof_text"] is None
    assert e["source"]["license"].startswith("owner-own-work")
    assert e["statement"].strip()

allowed_relations = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
for relation in bundle["relations"]:
    assert relation["from_key"] in entries
    assert relation["to_key"] in entries
    assert relation["kind"] in allowed_relations
    assert "Supporting ends:" in relation["rationale"]

print(f"valid: {len(entries)} entries, {len(bundle['relations'])} relations, 0 proves-target relations")
