import hashlib
import json
from pathlib import Path

root = Path(r"~\brain_workers\w563")
bundle = json.loads((root / "draft_bundle_001.json").read_text(encoding="utf-8"))
assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w563"
keys = [entry["key"] for entry in bundle["entries"]]
assert len(keys) == len(set(keys)) == 2
for entry in bundle["entries"]:
    assert entry["source"]["license"].startswith("owner-own-work")
    assert entry["statement"] and entry["title"] and entry["logical_name"]
    assert bool(entry["proof_text"]) == (entry["kind"] in {"lemma", "theorem"})
for relation in bundle["relations"]:
    assert relation["from_key"] in keys
    assert relation["kind"] in {
        "depends_on", "defines", "proves", "refutes", "generalizes",
        "specializes", "analogous_to", "cites", "semantic_association"
    }
    assert relation.get("to_key") in keys or relation.get("to_existing_logical")
for name in ("CLAIMS.jsonl", "VERDICTS.jsonl"):
    rows = (root / name).read_text(encoding="utf-8").splitlines()
    for row in rows:
        json.loads(row)
    print(name, len(rows), "valid rows")
json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))

inbox = Path(r"~\math-brain-inbox\w563")
inbox.mkdir(parents=True, exist_ok=True)
destination = inbox / "bundle_001.json"
if destination.exists():
    assert destination.read_bytes() == (root / "draft_bundle_001.json").read_bytes(), "bundle filename collision"
else:
    part = inbox / "bundle_001.json.part"
    part.write_bytes((root / "draft_bundle_001.json").read_bytes())
    part.replace(destination)
digest = hashlib.sha256(destination.read_bytes()).hexdigest()
receipt = {
    "draft_path": str(destination),
    "sha256": digest,
    "entries": len(keys),
    "relations": len(bundle["relations"]),
    "submitted": True,
    "reviewed_by": "w563",
    "ingested": False,
    "retrievable": False,
    "integrator_receipt": None,
}
(root / "SUBMISSION.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt))
