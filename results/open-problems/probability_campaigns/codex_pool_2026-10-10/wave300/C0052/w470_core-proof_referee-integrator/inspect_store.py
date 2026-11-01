"""Read-only, narrowly scoped C0052 duplicate probe."""

import sqlite3
import json

path = "~/math-brain-build/local/population/brain.sqlite3"
db = sqlite3.connect("file:" + path + "?mode=ro", uri=True)
tables = [row[0] for row in db.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
print("tables", tables[:40])
for table in tables:
    if any(word in table.lower() for word in ("claim", "card", "node")):
        print(table, [row[1] for row in db.execute(f"PRAGMA table_info({table})")])
for probe in ("non-triviality", "renormalized coupling", "sourced current", "ursell"):
    rows = db.execute(
        "SELECT id,title,substr(body,1,120),metadata_json FROM nodes "
        "WHERE lower(title) LIKE ? OR lower(body) LIKE ? LIMIT 12",
        ("%" + probe + "%", "%" + probe + "%"),
    ).fetchall()
    print("probe", probe, "count_sample", len(rows))
    for node_id, title, body, meta in rows:
        print("node", node_id, title, body.replace("\n", " "), meta[:180])
for node_id in (
    "claim_db355f188daf0592950298d6e3b23e5f2b7e6eb0f3a21694083ad47fdadd0048",
    "claim_93dc043f691fa62549866c90e84e26aa836d69164fd798c69ba9c0dc431b1fc0",
):
    row = db.execute("SELECT title,body,metadata_json FROM nodes WHERE id=?", (node_id,)).fetchone()
    if row:
        print("detail", node_id, row[0], row[1], {k: json.loads(row[2]).get(k) for k in ("logical_id", "truth_status", "trust_class", "source_id", "retired")})
