"""Validate and submit this worker's complete draft to the explicitly named inbox."""
import json
import os
from pathlib import Path

root = Path(__file__).resolve().parent
source = root / "bundle_001.json"
payload = json.loads(source.read_text(encoding="utf-8"))
assert payload["spec"] == "mathbrain-draft-v1"
assert payload["author_agent"] == "w515"
assert len(payload["entries"]) == 3
keys = {entry["key"] for entry in payload["entries"]}
assert len(keys) == len(payload["entries"])
for entry in payload["entries"]:
    assert entry["kind"] in {"definition", "lemma", "theorem", "concept"}
    assert all(field in entry for field in ("namespace", "logical_name", "title", "statement", "proof_text", "assumptions", "domain", "source"))
    assert entry["source"]["license"].startswith(("cc-by", "owner-own-work"))
    assert bool(entry["proof_text"]) == (entry["kind"] in {"lemma", "theorem"})
for relation in payload["relations"]:
    assert relation["from_key"] in keys
    assert ("to_key" in relation) != ("to_existing_logical" in relation)
    if "to_key" in relation:
        assert relation["to_key"] in keys
    assert relation["kind"] in {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}

target_dir = Path("~/math-brain-inbox/w515").resolve()
assert str(target_dir).lower() == "~\\math-brain-inbox\\w515"
target_dir.mkdir(parents=True, exist_ok=True)
part = target_dir / "bundle_001.json.part"
final = target_dir / "bundle_001.json"
assert not part.exists() and not final.exists(), "refuse overwrite"
part.write_bytes(source.read_bytes())
os.rename(part, final)
assert json.loads(final.read_text(encoding="utf-8"))["bundle_slug"] == payload["bundle_slug"]
print(f"submitted {final} with {len(payload['entries'])} entries and {len(payload['relations'])} relations")
