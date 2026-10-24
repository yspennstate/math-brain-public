import sqlite3

with sqlite3.connect('file:~/.agents/coordination/agent_mesh.sqlite3?mode=ro', uri=True) as con:
    print(con.execute("SELECT campaign_id,name FROM campaigns WHERE status='active' AND (name LIKE '%prob%' OR name LIKE '%P0117%') LIMIT 20").fetchall())
