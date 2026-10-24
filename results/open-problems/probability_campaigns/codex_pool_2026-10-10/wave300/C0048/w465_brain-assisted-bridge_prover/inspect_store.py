"""Targeted schema/card inspection. The live database is always opened mode=ro."""
import json
from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parent
DATABASE = Path("~/math-brain-build/local/population/brain.sqlite3")
with sqlite3.connect(DATABASE.as_uri() + "?mode=ro", uri=True, timeout=10) as connection:
    tables = connection.execute("SELECT name,sql FROM sqlite_master WHERE type='table'").fetchall()
    selected = [row for row in tables if any(word in row[0].lower() for word in ("node", "source", "card"))]
    result = {"database": str(DATABASE), "open_mode": "ro", "tables": []}
    for name, sql in selected:
        # Identifiers come only from sqlite_master; quote rather than interpolate raw identifiers.
        quoted = '"' + name.replace('"', '""') + '"'
        columns = connection.execute("PRAGMA table_info("+quoted+")").fetchall()
        result["tables"].append({"name": name, "sql": sql, "columns": columns})
    output = ROOT / "evidence"
    output.mkdir(exist_ok=True)
    (output / "store_schema.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
