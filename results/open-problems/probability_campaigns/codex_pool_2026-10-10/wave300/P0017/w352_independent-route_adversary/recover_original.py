"""Follow the intake README's exact original campaign pointer."""
from pathlib import Path
import json
import sqlite3
import re

ROOT=Path(__file__).resolve().parent
base=Path('~/Downloads/Probability_1000_20h_20260906')
matched=[]
source_ids=set()
for name in ('problems.jsonl','attempts.jsonl'):
    path=base/name
    if not path.is_file():
        print('MISSING',str(path))
        continue
    with path.open(encoding='utf-8-sig') as stream:
        for number,line in enumerate(stream,1):
            if re.search(r'\bP0017\b',line):
                row=json.loads(line)
                result={'path':str(path),'line':number,'row':row}
                matched.append(result)
                if row.get('source_id'): source_ids.add(row['source_id'])
                print(json.dumps(result,ensure_ascii=False))
path=base/'sources.jsonl'
if path.is_file():
    with path.open(encoding='utf-8-sig') as stream:
        for number,line in enumerate(stream,1):
            row=json.loads(line)
            if row.get('source_id') in source_ids:
                result={'path':str(path),'line':number,'row':row}
                matched.append(result)
                print(json.dumps(result,ensure_ascii=False))
(ROOT/'ORIGINAL_SOURCE_REPORT.json').write_text(json.dumps(matched,indent=2,ensure_ascii=False),encoding='utf-8')
db=Path('~/.agents/coordination/agent_mesh.sqlite3')
if db.is_file():
    with sqlite3.connect(db.as_uri()+'?mode=ro',uri=True,timeout=3) as con:
        rows=con.execute('SELECT sender_agent,recipient,created_at,topic,body FROM messages WHERE recipient=? ORDER BY created_at DESC LIMIT 8',('w352',)).fetchall()
        print('MESH_READONLY',json.dumps(rows,ensure_ascii=False))
