"""Read only the FEI retrieval cards; no store writes or export."""
import sqlite3

path = "~/math-brain-build/local/population/brain.sqlite3"
db = sqlite3.connect("file:" + path + "?mode=ro", uri=True)
names = [r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table'")]
print("TABLES", names)
for name in names:
    if name in ("cards", "claims", "nodes"):
        print("SCHEMA", name, list(db.execute(f"PRAGMA table_info({name})")))
        for pattern in ("%Fourier entropy and the entropy-influence conjecture%", "%Open problem: Fourier entropy versus total influence%", "%A New Bound for the Fourier%"):
            try:
                rows = list(db.execute(f"SELECT * FROM {name} WHERE title LIKE ? LIMIT 3", (pattern,)))
            except sqlite3.OperationalError as exc:
                print("QUERY_ERROR", str(exc))
                break
            for row in rows:
                print("CARD", str(row)[:3500])
