"""Read-only, narrowly targeted card lookup for C0017 draft links."""
import sqlite3

path = "~/math-brain-build/local/population/brain.sqlite3"
conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
needle = "open-problem-c0017-conformal-invariance-of-critical-bond-percolation-on-the-square-lattic"
for (table,) in conn.execute("SELECT name FROM sqlite_master WHERE type='table'"):
    cols = [row[1] for row in conn.execute(f'PRAGMA table_info("{table}")')]
    if "card" in table or "node" in table or "entry" in table:
        print("SCHEMA", table, cols[:20])
    if "logical_id" in cols:
        fields = [name for name in ("logical_id", "title", "statement") if name in cols]
        query = f'SELECT {", ".join(fields)} FROM "{table}" WHERE logical_id = ? LIMIT 1'
        row = conn.execute(query, ("math:probability.percolation:" + needle,)).fetchone()
        if row:
            print(table, dict(zip(fields, [str(v)[:650] for v in row])))
for pattern in ("%Conformal invariance of critical bond percolation%", "%parafermionic%spin%", "%Cardy%martingale%"):
    hits = conn.execute("SELECT title, substr(body,1,450), metadata_json FROM nodes WHERE title LIKE ? LIMIT 10", (pattern,)).fetchall()
    print("QUERY", pattern, "HITS", len(hits))
    for title, body, raw_meta in hits:
        meta = __import__("json").loads(raw_meta)
        print("CARD", title, "LOGICAL", meta.get("logical_id"), "BODY", body)
for title, body in conn.execute("SELECT title, body FROM nodes WHERE title = ? LIMIT 1", ("Attempt on Conformal invariance of critical bond percolation on the square lattice",)):
    print("LIVE_ATTEMPT_BAD_SPIN", body.count("spin sigma = 2/3"))
    print("LIVE_ATTEMPT_CONTEXT", body[max(0, body.find("spin sigma")-65):body.find("spin sigma")+120])
conn.close()
