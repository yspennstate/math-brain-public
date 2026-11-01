"""Read-only, target-specific metadata check; no export or store mutation."""
import json
import sqlite3

con = sqlite3.connect("file:~/math-brain-build/local/population/brain.sqlite3?mode=ro", uri=True, timeout=2)
print(json.dumps({"tables": con.execute("SELECT name FROM sqlite_master WHERE type=?", ("table",)).fetchall()}))
rows = con.execute("SELECT id,kind,title,substr(body,1,1800) FROM nodes WHERE lower(title) LIKE ? OR lower(title) LIKE ? OR lower(title) LIKE ? LIMIT 12",
                   ("%p0162%", "%fourier entropy%", "%entropy-influence%")).fetchall()
print(json.dumps({"target_rows": rows}, ensure_ascii=False))
con.close()
