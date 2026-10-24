"""Read-only targeted schema/title probe; no store mutation."""
import sqlite3

uri = "file:~/math-brain-build/local/population/brain.sqlite3?mode=ro"
con = sqlite3.connect(uri, uri=True, timeout=15)
tables = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")]
print("TABLES", tables)
for row in con.execute("SELECT id,kind,title FROM nodes WHERE lower(title) LIKE '%smirnov%' OR lower(title) LIKE '%parafermion%' OR lower(title) LIKE '%critical bond percolation on the square%' LIMIT 40"):
    print("MATCH", row)
con.close()
