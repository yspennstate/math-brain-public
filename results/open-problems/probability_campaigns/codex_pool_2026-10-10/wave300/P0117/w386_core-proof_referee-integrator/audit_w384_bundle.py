import json
import sqlite3
from pathlib import Path

bundle = json.loads(Path("~/brain_workers/w384/bundle_001.json").read_text(encoding="utf-8"))
conn = sqlite3.connect("file:~/math-brain-build/local/population/brain.sqlite3?mode=ro", uri=True)
names = {e["logical_name"] for e in bundle["entries"]}
assert len(names) == len(bundle["entries"])
keys = {e["key"] for e in bundle["entries"]}
assert len(keys) == len(bundle["entries"])
existing = []
for meta, title in conn.execute("SELECT metadata_json,title FROM nodes WHERE metadata_json LIKE '%probability.fpp%'"):
    logical = json.loads(meta).get("logical_id", "")
    if logical.startswith("math:probability.fpp:"):
        existing.append((logical, title))
print("existing_probability_fpp_nodes", len(existing), "examples", existing[:3])
for e in bundle["entries"]:
    print("entry", e["key"], e["kind"], e["namespace"], e["logical_name"], e["source"]["license"])
    duplicate = [x for x in existing if x[0] == f'math:{e["namespace"]}:{e["logical_name"]}']
    if duplicate:
        print("exact_duplicate", duplicate)
for rel in bundle["relations"]:
    assert rel["from_key"] in keys
    assert rel.get("to_key", rel.get("to_existing_logical"))
    if "to_key" in rel:
        assert rel["to_key"] in keys
print("entries", len(bundle["entries"]), "relations", len(bundle["relations"]))
