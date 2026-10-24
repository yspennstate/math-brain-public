import json
import sqlite3
from pathlib import Path

path = Path("~/brain_workers/w385/bundle_001.json")
bundle = json.loads(path.read_text(encoding="utf-8"))
conn = sqlite3.connect("file:~/math-brain-build/local/population/brain.sqlite3?mode=ro", uri=True)
keys = {e["key"] for e in bundle["entries"]}
assert len(keys) == len(bundle["entries"])
print("bundle", bundle["bundle_slug"], "entries", len(bundle["entries"]), "relations", len(bundle["relations"]))
namespace = "probability.first-passage-percolation"
existing_ns = sum(
    json.loads(meta).get("logical_id", "").startswith(f"math:{namespace}:")
    for (meta,) in conn.execute(
        "SELECT metadata_json FROM nodes WHERE metadata_json LIKE '%probability.first-passage-percolation%'"
    )
)
print("existing_namespace_nodes", existing_ns)
for e in bundle["entries"]:
    print("ENTRY", e["key"], e["kind"], e["namespace"], e["logical_name"], e["source"]["license"])
    print("STATEMENT", e["statement"])
    print("ASSUMPTIONS", e["assumptions"])
    print("SOURCE", e["source"]["source_id"], e["source"].get("url"))
    count = conn.execute("SELECT count(*) FROM nodes WHERE lower(title) LIKE ? OR lower(body) LIKE ?", (f'%{e["logical_name"].replace("-", " ").lower()}%', f'%{e["logical_name"].replace("-", " ").lower()}%')).fetchone()[0]
    print("phrase_matches", count)
for rel in bundle["relations"]:
    assert rel["from_key"] in keys
    assert rel.get("to_key", rel.get("to_existing_logical"))
    if "to_key" in rel:
        assert rel["to_key"] in keys
    print("REL", rel)
