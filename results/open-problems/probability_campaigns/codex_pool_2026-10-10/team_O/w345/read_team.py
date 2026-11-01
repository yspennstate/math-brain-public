"""Read pending w345 messages via a read-only SQLite connection; no ack or sends."""
import json
from pathlib import Path
import sqlite3

ROOT=Path(__file__).resolve().parent
database='file:~/.agents/coordination/agent_mesh.sqlite3?mode=ro'
try:
    con=sqlite3.connect(database,uri=True,timeout=5)
    con.row_factory=sqlite3.Row
    tables=[r['name'] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('messages','inbox')")]
    out={'mode':'read-only-no-ack','agent':'w345','tables':tables}
    if 'messages' in tables:
        cols=[r['name'] for r in con.execute('PRAGMA table_info(messages)')]
        out['columns']=cols
        recipient=next((c for c in ('to_agent','recipient','recipient_agent','agent_to') if c in cols),None)
        if recipient:
            rows=con.execute(f'SELECT * FROM messages WHERE "{recipient}" IN (?,?) ORDER BY rowid DESC LIMIT 8',('w345','codex:w345')).fetchall()
            out['messages']=[dict(row) for row in rows]
    con.close()
except (sqlite3.Error,OSError) as exc:
    out={'mode':'read-only-no-ack','agent':'w345','error':str(exc)}
(ROOT/'team_read.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
