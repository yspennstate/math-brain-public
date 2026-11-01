"""Read-only schema discovery, restricted to the relevant store tables."""
from pathlib import Path
import json
import sqlite3

base = Path(__file__).resolve().parent
path = Path("~/math-brain-build/local/population/brain.sqlite3")
connection = sqlite3.connect("file:" + path.as_posix() + "?mode=ro", uri=True, timeout=5)
connection.execute("PRAGMA query_only=ON")
tables = [r[0] for r in connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('nodes','claims','sources','edges','cards')")]
result = {"store": str(path), "mode": "ro", "tables": {}}
for table in tables:
    result["tables"][table] = [dict(zip(("cid","name","type","notnull","default","pk"), row)) for row in connection.execute('PRAGMA table_info("'+table+'")')]
connection.close()
(base / "store_schema_receipt.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result, indent=2))
