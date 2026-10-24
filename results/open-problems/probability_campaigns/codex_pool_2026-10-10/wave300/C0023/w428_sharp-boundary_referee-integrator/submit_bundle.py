"""Validate the local C0023 draft and place it atomically in the authorized inbox."""
import json
import os
from pathlib import Path

work = Path(r"~\brain_workers\w428")
source = work / "bundle_001.json"
bundle = json.loads(source.read_text(encoding="utf-8"))
assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w428"
entries = bundle["entries"]
relations = bundle["relations"]
assert 0 < len(entries) <= 200
keys = {entry["key"] for entry in entries}
assert len(keys) == len(entries)
assert sum(bool(entry.get("supersedes_existing")) for entry in entries) == 3
for entry in entries:
    assert entry["kind"] == "concept" and entry["proof_text"] is None
    assert entry["statement"] and entry["namespace"] == "probability.percolation"
    assert entry["source"]["license"].startswith("owner-own-work")
    assert entry["source"]["source_id"].startswith("owner-own-work:")
allowed = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
for relation in relations:
    assert relation["from_key"] in keys and relation["to_key"] in keys
    assert relation["kind"] in allowed and relation["rationale"]

destination = Path(r"~\math-brain-inbox\w428")
destination.mkdir(parents=True, exist_ok=True)
part = destination / "bundle_001.json.part"
final = destination / "bundle_001.json"
part.write_bytes(source.read_bytes())
os.replace(part, final)
assert json.loads(final.read_text(encoding="utf-8")) == bundle
print(f"submitted entries={len(entries)} revisions=3 relations={len(relations)} path={final}")
