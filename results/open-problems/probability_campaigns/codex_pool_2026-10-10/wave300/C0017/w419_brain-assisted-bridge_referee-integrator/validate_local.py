"""Validate local draft format and evidence files before handoff."""
import json
from pathlib import Path

here = Path(__file__).resolve().parent
bundle = json.loads((here / "bundle_002.json").read_text(encoding="utf-8"))
assert bundle["spec"] == "mathbrain-draft-v1" and bundle["author_agent"] == "w419"
keys = [entry["key"] for entry in bundle["entries"]]
assert len(keys) == len(set(keys)) and len(keys) <= 200
for entry in bundle["entries"]:
    assert entry["kind"] in {"definition", "lemma", "theorem", "concept"}
    assert entry["statement"] and entry["source"]["license"].startswith(("arxiv-nonexclusive", "owner-own-work"))
    assert bool(entry["proof_text"]) == (entry["kind"] in {"lemma", "theorem"})
for edge in bundle["relations"]:
    assert edge["from_key"] in keys and edge["to_key"] in keys
    assert edge["kind"] in {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
assert json.loads((here / "SOURCE_STATUS.json").read_text(encoding="utf-8"))["current_openness"] == "UNKNOWN"
claims = [json.loads(line) for line in (here / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
assert all("statement" in claim and "remaining_gap" in claim and "status" in claim for claim in claims)
print(json.dumps({"bundle_entries": len(keys), "bundle_relations": len(bundle["relations"]), "claim_rows": len(claims), "source_status": "UNKNOWN"}))
