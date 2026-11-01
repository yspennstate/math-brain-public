"""Static validation of this worker's draft; does not ingest or write a store."""

import json
import re
from pathlib import Path

path = Path("~/math-brain-inbox/w464/bundle_001.json.part")
bundle = json.loads(path.read_text(encoding="utf-8"))
assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w464"
assert 0 < len(bundle["entries"]) <= 200
keys = {entry["key"] for entry in bundle["entries"]}
assert len(keys) == len(bundle["entries"])
for entry in bundle["entries"]:
    assert {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"} <= set(entry)
    assert entry["kind"] in {"definition", "lemma", "theorem", "concept"}
    assert bool(entry["proof_text"]) == (entry["kind"] in {"lemma", "theorem"})
    assert re.fullmatch(r"[a-z]+(?:\.[a-z]+)*", entry["namespace"])
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", entry["logical_name"])
    assert entry["source"]["license"].startswith(("owner-own-work", "arxiv-nonexclusive"))
    assert entry["statement"] and entry["title"]
for relation in bundle["relations"]:
    assert relation["from_key"] in keys
    assert (relation.get("to_key") in keys) != bool(relation.get("to_existing_logical"))
    assert relation["kind"] in {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
    assert relation["rationale"]
print(json.dumps({"status": "PASS", "entries": len(bundle["entries"]), "relations": len(bundle["relations"]), "live_store_mutations": 0}))
