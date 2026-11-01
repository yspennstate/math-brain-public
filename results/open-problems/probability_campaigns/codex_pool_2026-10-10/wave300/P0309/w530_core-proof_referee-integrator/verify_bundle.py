"""Validate this worker's staged draft without invoking the live integrator."""
import json
import sqlite3
from pathlib import Path

draft_path = Path(r"~\math-brain-inbox\w530\bundle_001.json")
draft = json.loads(draft_path.read_text(encoding="utf-8"))
assert draft["spec"] == "mathbrain-draft-v1"
assert draft["author_agent"] == "w530"
assert 0 < len(draft["entries"]) <= 200
keys = {entry["key"] for entry in draft["entries"]}
assert len(keys) == len(draft["entries"])
relation_kinds = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
for entry in draft["entries"]:
    assert entry["namespace"] == "probability.core"
    assert entry["kind"] in {"definition", "lemma", "theorem", "concept"}
    assert entry["statement"] and entry["title"] and entry["logical_name"]
    assert entry["proof_text"] if entry["kind"] in {"lemma", "theorem"} else entry["proof_text"] is None
    assert entry["source"]["license"].startswith("owner-own-work")
    assert entry["source"]["source_id"] and entry["source"]["url"]
for relation in draft["relations"]:
    assert relation["from_key"] in keys
    assert relation["kind"] in relation_kinds
    assert bool(relation.get("to_key")) != bool(relation.get("to_existing_logical"))
    if "to_key" in relation:
        assert relation["to_key"] in keys
    assert relation["rationale"]

store = r"~\math-brain-build\local\population\brain.sqlite3"
con = sqlite3.connect("file:" + store + "?mode=ro", uri=True)
try:
    row = con.execute(
        "SELECT metadata_json FROM nodes WHERE title=? LIMIT 1",
        ("Open problem: Positive-temperature crystalline Gibbs phases for three-dimensional Riesz gases",),
    ).fetchone()
    assert row, "P0309 parent not found in read-only local store"
    parent_logical = json.loads(row[0])["logical_id"]
    for relation in draft["relations"]:
        if "to_existing_logical" in relation:
            assert relation["to_existing_logical"] == parent_logical
finally:
    con.close()
print(f"VALID: {len(draft['entries'])} entries; {len(draft['relations'])} relations; parent={parent_logical}")
