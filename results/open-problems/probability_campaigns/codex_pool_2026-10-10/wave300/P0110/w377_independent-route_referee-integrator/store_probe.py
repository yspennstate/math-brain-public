"""Read-only, bounded P0110 checks against the local math-brain store."""

import json
import sqlite3


uri = "file:~/math-brain-build/local/population/brain.sqlite3?mode=ro"
conn = sqlite3.connect(uri, uri=True, timeout=5)
conn.execute("PRAGMA query_only=ON")
tables = [row[0] for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name LIMIT 40")]
print("tables", tables)
for table in tables:
    if any(token in table.lower() for token in ("claim", "card", "node", "entry")):
        cols = [row[1] for row in conn.execute(f'PRAGMA table_info("{table}")')]
        print("candidate", table, cols[:20])
rows = list(conn.execute("SELECT id, kind, title, substr(body,1,500) FROM nodes WHERE title LIKE ? LIMIT 8", ("%iid FPP law with proved KPZ%",)))
print("P0110 title matches", rows)
for node_id, kind, title, body in rows:
    if title.startswith("Open problem:"):
        metadata = conn.execute("SELECT metadata_json FROM nodes WHERE id=?", (node_id,)).fetchone()[0]
        print("P0110 target metadata", json.loads(metadata) if metadata else {})
