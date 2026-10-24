"""Validate and submit this worker's immutable draft, without ingesting it."""
import json
from pathlib import Path

src = Path("~/brain_workers/w506/DRAFT_BUNDLE.json")
outdir = Path("~/math-brain-inbox/w506")
target = outdir / "bundle_001.json"
part = outdir / "bundle_001.part"
data = src.read_bytes()
obj = json.loads(data)
assert obj["spec"] == "mathbrain-draft-v1"
assert obj["author_agent"] == "w506"
assert 0 < len(obj["entries"]) <= 200
keys = {entry["key"] for entry in obj["entries"]}
assert len(keys) == len(obj["entries"])
required = {"key", "namespace", "logical_name", "kind", "title", "statement",
            "proof_text", "assumptions", "domain", "source"}
for entry in obj["entries"]:
    assert required <= set(entry)
    assert entry["kind"] in {"definition", "concept", "lemma", "theorem"}
    assert entry["proof_text"] if entry["kind"] in {"lemma", "theorem"} else entry["proof_text"] is None
    assert entry["source"]["license"].startswith("owner-own-work")
for relation in obj["relations"]:
    assert relation["from_key"] in keys and relation["to_key"] in keys
    assert relation["kind"] in {"depends_on", "defines", "proves", "refutes", "generalizes",
                                "specializes", "analogous_to", "cites", "semantic_association"}
assert not target.exists() and not part.exists(), "Refusing to overwrite a submitted bundle"
outdir.mkdir(parents=True, exist_ok=True)
part.write_bytes(data)
part.replace(target)
assert target.read_bytes() == data
print(f"submitted={target} bytes={len(data)} entries={len(obj['entries'])} relations={len(obj['relations'])}")
