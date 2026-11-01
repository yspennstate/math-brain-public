import sqlite3

conn = sqlite3.connect(
    "file:~/.agents/coordination/agent_mesh.sqlite3?mode=ro", uri=True
)
print(
    conn.execute(
        "SELECT a.agent_id,c.name,c.status FROM agents a "
        "LEFT JOIN campaigns c ON a.campaign_id=c.campaign_id "
        "WHERE a.agent_id IN (?,?,?)",
        ("w435", "w436", "w437"),
    ).fetchall()
)
