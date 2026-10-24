"""Extract only P0162 rows and the explicitly cited sources; never print a corpus."""
import json
import sqlite3
from pathlib import Path

base = Path(__file__).resolve().parent
research = Path("~/<private-repo>/06_math_research")
intake = research / "probability_1000_intake_claude_20260907"
matches = []
for filename in ["problems.jsonl", "attempts.jsonl"]:
    path = intake / filename
    for line_number, line in enumerate(path.open(encoding="utf-8-sig"), 1):
        if "p0162" not in line.lower():
            continue
        row = json.loads(line)
        matches.append({"file": str(path), "line": line_number, "record": row})
for filename in ["brain_bundle_C006p01.json", "brain_bundle_C006a04.json"]:
    path = intake / filename
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    for row in payload.get("entries", []):
        if "p0162" in str(row.get("logical_name", "")).lower():
            matches.append({"file": str(path), "record": row})

source_ids = set()
def source_walk(value):
    if isinstance(value, dict):
        for k, v in value.items():
            if k == "source_id" and isinstance(v, str):
                source_ids.add(v)
            source_walk(v)
    elif isinstance(value, list):
        for v in value:
            source_walk(v)
for row in matches:
    source_walk(row["record"])
source_rows = []
path = intake / "sources.jsonl"
for line_number, line in enumerate(path.open(encoding="utf-8-sig"), 1):
    if not any(source_id in line for source_id in source_ids):
        continue
    row = json.loads(line)
    if row.get("source_id") in source_ids:
        source_rows.append({"file": str(path), "line": line_number, "record": row})

result = {"target": "P0162", "records": matches, "cited_sources": source_rows,
          "attempts_H_I": "Targeted P0162 text search yielded no matching record; not a proof that all owner work was checked."}
(base / "SOURCE_RECORDS.json").write_text(json.dumps(result, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
for row in matches:
    record = row["record"]
    print(json.dumps({"file": Path(row["file"]).name,
          "line": row.get("line"),
          "record": {k:v for k,v in record.items() if k in ["problem_id","id","source_id","title","statement","method","result","obstruction","source","source_status","status","logical_name","codex_problem_id","original_id"]}}, ensure_ascii=False))
for row in source_rows:
    print(json.dumps({"cited_source": row["record"]}, ensure_ascii=False))

store = Path("~/math-brain-build/local/population/brain.sqlite3")
conn = sqlite3.connect(f"file:{store.as_posix()}?mode=ro", uri=True, timeout=4)
try:
    tables = [r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")]
    schema = {name:[r[1] for r in conn.execute('PRAGMA table_info("'+name.replace('"','""')+'")')]
              for name in tables if name in ["claims", "nodes", "artifacts", "entries", "sources", "relations", "cards"]}
    (base / "STORE_SCHEMA_TARGET.json").write_text(json.dumps({"tables": tables, "selected_columns":schema}, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"store_schema":schema, "tables":tables}, ensure_ascii=False))
finally:
    conn.close()
