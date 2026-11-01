"""Inspect only math card schemas; never write a shared store."""
from pathlib import Path
import sqlite3

known = Path("~/math-brain-build/local/population/brain.sqlite3")
if known.is_file():
    con = sqlite3.connect(known.as_uri()+"?mode=ro",uri=True,timeout=5)
    con.execute("PRAGMA query_only=ON")
    for (table,) in con.execute("SELECT name FROM sqlite_master WHERE type='table' AND (name LIKE '%card%' OR name LIKE '%node%')"):
        escaped = '"'+table.replace('"','""')+'"'
        columns = [row[1] for row in con.execute("PRAGMA table_info("+escaped+")")]
        print("POPULATION_SCHEMA",table,columns)
    con.close()
canonical = Path("~/math-research-brain")
if canonical.is_dir():
    for path in sorted(canonical.iterdir()):
        if path.name.lower() in {"local","data","src","store","README.md".lower()} or path.suffix.lower() in {".sqlite3",".sqlite",".db"}:
            print("CANONICAL_PATH",path)
