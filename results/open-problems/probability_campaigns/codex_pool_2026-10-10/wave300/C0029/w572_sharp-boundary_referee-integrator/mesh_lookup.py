"""Read-only lookup of named proof peers' active mesh teams."""
import sqlite3

path = "file:~/.agents/coordination/agent_mesh.sqlite3?mode=ro"
conn = sqlite3.connect(path, uri=True)
rows = conn.execute(
    "SELECT c.name, a.agent_id FROM campaigns c "
    "JOIN agents a ON a.campaign_id=c.campaign_id "
    "WHERE c.status=? AND a.agent_id IN (?,?,?,?,?)",
    ("active", "w570", "w571", "w572", "w575", "codex-01a12190"),
).fetchall()
for row in rows:
    print(*row)
