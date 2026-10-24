import sqlite3

path = '~/.agents/coordination/agent_mesh.sqlite3'
conn = sqlite3.connect('file:' + path + '?mode=ro', uri=True)
rows = conn.execute(
    "SELECT campaign_id, name, status FROM campaigns WHERE status='active' "
    "AND (lower(name) LIKE '%prob%' OR lower(name) LIKE '%c0047%') "
    "ORDER BY rowid DESC LIMIT 20"
).fetchall()
for row in rows:
    print(*row, sep=' | ')
