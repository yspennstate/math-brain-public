import sqlite3


DB = "file:~/math-brain-build/local/population/brain.sqlite3?mode=ro"
with sqlite3.connect(DB, uri=True) as con:
    tables = [row[0] for row in con.execute(
        "SELECT name FROM sqlite_master WHERE type=? AND name NOT LIKE ?",
        ("table", "sqlite_%"),
    )]
    print("tables", tables)
    for table in tables:
        if table in {"cards", "nodes", "claims"}:
            print("columns", table, [row[1] for row in con.execute(f"PRAGMA table_info({table})")])
    for namespace in ("probability.core", "probability.saw", "probability.selfavoiding"):
        pattern = f'%math:{namespace}:%'
        count = con.execute("SELECT COUNT(*) FROM nodes WHERE metadata_json LIKE ?", (pattern,)).fetchone()[0]
        examples = [row[0] for row in con.execute(
            "SELECT title FROM nodes WHERE metadata_json LIKE ? LIMIT 3", (pattern,)
        )]
        print("namespace", namespace, "nodes", count, "examples", examples)
