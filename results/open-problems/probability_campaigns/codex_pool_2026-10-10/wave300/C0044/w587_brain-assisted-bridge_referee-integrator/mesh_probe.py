"""Read-only lookup of the existing team channel for the named C0044 peers."""

import sqlite3

uri = "file:~/.agents/coordination/agent_mesh.sqlite3?mode=ro"
db = sqlite3.connect(uri, uri=True, timeout=3)
for name, sql in db.execute("SELECT name, sql FROM sqlite_master WHERE type='table'"):
    if any(token in name.lower() for token in ("team", "member", "participant")):
        print(name, sql)
        try:
            for row in db.execute(f"SELECT * FROM {name} LIMIT 8"):
                if any(str(peer) in str(row) for peer in ("w585", "w586", "w587", "w590", "codex-01a12190")):
                    print("MATCH", row)
        except sqlite3.Error as exc:
            print("QUERY_ERROR", str(exc))
