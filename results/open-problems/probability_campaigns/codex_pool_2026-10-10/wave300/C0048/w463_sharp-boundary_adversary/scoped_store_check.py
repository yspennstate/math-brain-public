"""Read target records only; SQLite is explicitly opened read-only."""
from pathlib import Path
import json
import sqlite3

result = {"search_scope": "C0048 / exact Potts discontinuity title only", "export_records": []}
export = Path("~/math-brain-build/export/population/nodes.jsonl")
if export.exists():
    with export.open(encoding="utf-8-sig") as stream:
        for number, line in enumerate(stream, 1):
            if not any(term in line for term in ["potts_discontinuity_d3_q3", "Discontinuity of the Potts phase transition", '"C0048"']):
                continue
            item = json.loads(line)
            result["export_records"].append({"line": number, "record": item})
            if len(result["export_records"]) >= 4:
                break
store = Path("~/math-brain-build/local/population/brain.sqlite3")
result["sqlite_path"] = str(store)
result["sqlite_read_only"] = True
if store.exists():
    connection = sqlite3.connect(store.as_uri()+"?mode=ro", uri=True, timeout=5)
    tables = [name for (name,) in connection.execute("select name from sqlite_master where type='table' and name in ('nodes','cards','items','sources')")]
    result["candidate_tables"] = tables
    for table in tables:
        columns = [row[1] for row in connection.execute(f'pragma table_info("{table}")')]
        if "title" not in columns:
            result.setdefault("schema_only", {})[table] = columns
            continue
        chosen = [name for name in ["id", "node_id", "logical_name", "title", "statement", "kind", "status", "verification"] if name in columns]
        selections = ",".join('"'+name+'"' for name in chosen)
        cursor = connection.execute(f'select {selections} from "{table}" where title like ? limit 4', ("%Discontinuity of the Potts phase transition%",))
        result.setdefault("canonical_records", {})[table] = [dict(zip(chosen, row)) for row in cursor]
    connection.close()
else:
    result["sqlite_result"] = "named store path missing; no alternate private configuration read"
output = Path(__file__).with_name("STORE_SOURCE_REPORT.json")
output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
for key, value in result.items():
    if key == "export_records":
        for entry in value:
            item = entry["record"]
            print(json.dumps({"export_line": entry["line"], **{k: v for k, v in item.items() if k in ["id", "logical_name", "title", "statement", "kind", "status", "payload"]}}, ensure_ascii=False)[:4400])
    else:
        print(json.dumps({key: value}, ensure_ascii=False)[:4400])
