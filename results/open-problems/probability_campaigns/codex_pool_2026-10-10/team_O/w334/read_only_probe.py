"""Bounded source probes; never mutate a live file or database."""
from pathlib import Path
import json
import sqlite3
import sys

if sys.argv[1] == "schema":
    path = Path("~/math-brain-build/local/population/brain.sqlite3")
    db = sqlite3.connect(path.as_uri() + "?mode=ro", uri=True)
    db.execute("PRAGMA query_only=ON")
    for name, sql in db.execute("SELECT name,sql FROM sqlite_master WHERE type='table'"):
        if not name.startswith("sqlite_"):
            print(json.dumps({"table": name, "schema": sql}, ensure_ascii=False))
    db.close()
elif sys.argv[1] == "cards":
    path = Path("~/math-brain-build/local/population/brain.sqlite3")
    db = sqlite3.connect(path.as_uri() + "?mode=ro", uri=True)
    db.execute("PRAGMA query_only=ON")
    terms = ["P0193", "P0411", "C0113", "P0039", "P0245", "C0012", "C0072", "C0108", "C0155", "P0026"]
    found = []
    for term in terms:
        for row in db.execute("SELECT id,title,body,metadata_json FROM nodes WHERE title LIKE ? OR body LIKE ? LIMIT 4", ("%" + term + "%", "%" + term + "%")):
            item = dict(zip(["id", "title", "body", "metadata_json"], row))
            item["query"] = term
            found.append(item)
            print(json.dumps(item, ensure_ascii=False))
    Path(__file__).with_name("store_cards.json").write_text(json.dumps(found, ensure_ascii=False, indent=2), encoding="utf-8")
    db.close()
else:
    raise SystemExit("unknown probe")
