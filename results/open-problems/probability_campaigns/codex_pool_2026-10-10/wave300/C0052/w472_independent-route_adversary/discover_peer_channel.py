import json
from pathlib import Path
import sqlite3

root=Path(__file__).resolve().parent
path=Path('~/.agents/coordination/agent_mesh.sqlite3')
conn=sqlite3.connect('file:'+path.as_posix()+'?mode=ro',uri=True,timeout=2)
conn.execute('PRAGMA query_only=ON')
agents=conn.execute('SELECT agent_id,campaign_id FROM agents WHERE agent_id IN (?,?,?)',('w471','w472','w473')).fetchall()
columns=[row[1] for row in conn.execute('PRAGMA table_info(campaigns)')]
team_column='name' if 'name' in columns else 'title' if 'title' in columns else None
receipt={'agents':agents,'campaign_columns':columns,'confirmed_team':None}
if team_column:
    rows=conn.execute('SELECT campaign_id,'+team_column+' FROM campaigns WHERE '+team_column+' LIKE ? OR '+team_column+' LIKE ? LIMIT 12',('%prob%','%primary%')).fetchall()
    receipt['candidate_channels']=rows
    for identity,name in rows:
        if 'probability300' in name.lower() or 'primary-directive' in name.lower():
            receipt['confirmed_team']=name
            break
conn.close()
(root/'PEER_CHANNEL_RECEIPT.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt))
