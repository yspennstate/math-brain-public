from pathlib import Path
import json
import sqlite3

root = Path(__file__).resolve().parent
cards = json.loads((root/'STORE_P0017_REPORT.json').read_text(encoding='utf-8'))
for card in cards:
    metadata = json.loads(card['metadata_json'])
    print(json.dumps({'id':card['id'],'title':card['title'],'body':card['body'],'metadata':metadata},ensure_ascii=False,indent=2))

db = 'file:~/.agents/coordination/agent_mesh.sqlite3?mode=ro'
con = sqlite3.connect(db,uri=True,timeout=2)
con.execute('PRAGMA query_only=ON')
rows = con.execute("SELECT a.agent_id,c.name,c.status FROM agents a LEFT JOIN campaigns c ON c.campaign_id=a.campaign_id WHERE a.agent_id IN (?,?,?,?)",('w351','w352','w353','w356')).fetchall()
print(json.dumps({'named_peer_teams':rows},ensure_ascii=False))
rows = con.execute("SELECT name,status FROM campaigns WHERE status='active' AND (name LIKE ? OR name LIKE ? OR name LIKE ?) LIMIT 8",('%P0017%','%W0300_O%','%PROBABILITY300%')).fetchall()
print(json.dumps({'relevant_active_teams':rows},ensure_ascii=False))
con.close()
