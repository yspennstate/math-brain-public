"""Inspect only the named math store, in SQLite read-only mode, with bounded output."""
import json
import pathlib
import sqlite3

root=pathlib.Path(__file__).resolve().parent
path=pathlib.Path("~/math-brain-build/local/population/brain.sqlite3")
connection=sqlite3.connect(path.as_uri()+"?mode=ro",uri=True,timeout=5)
connection.execute("PRAGMA query_only=ON")
tables=connection.execute("SELECT name,sql FROM sqlite_master WHERE type='table' AND (name IN ('cards','nodes','edges','entries','sources') OR name LIKE '%fts') LIMIT 20").fetchall()
out={"path":str(path),"mode":"read-only","tables":[{"name":name,"sql":sql} for name,sql in tables]}
(root/"store_schema.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out))
