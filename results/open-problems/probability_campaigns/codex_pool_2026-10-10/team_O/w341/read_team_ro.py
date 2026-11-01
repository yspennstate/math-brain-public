"""Equivalent pending-inbox peek without registration, delivery updates or ack."""
import json
from pathlib import Path
import sqlite3

ROOT=Path(__file__).resolve().parent
con=sqlite3.connect('file:~/.agents/coordination/agent_mesh.sqlite3?mode=ro',uri=True)
con.row_factory=sqlite3.Row
sql="""SELECT rowid AS delivery_seq,* FROM messages
WHERE recipient=? AND (delivered_at IS NULL OR (requires_ack=1 AND acked_at IS NULL))
AND lower(topic) NOT LIKE '%test%' AND lower(topic) NOT LIKE '%bank%'
ORDER BY rowid LIMIT 8"""
rows=[dict(r) for r in con.execute(sql,('w341',)).fetchall()]
con.close()
report={'agent':'w341','mode':'read-only; registration, delivery and acknowledgements unchanged','messages':rows}
(ROOT/'reports'/'team_readonly_peek.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('TEAM_READONLY_PENDING',len(rows),flush=True)
for r in rows:
    print(json.dumps({k:r.get(k) for k in ('message_id','sender_agent','topic','body')},ensure_ascii=False),flush=True)
