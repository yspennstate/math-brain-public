"""Resolve cross-bundle targets by their logical-id field, never by digest text."""
import json
import sqlite3
from pathlib import Path

ROOT=Path(__file__).resolve().parent
IDS=['P0288','C0034','C0151','P0127','P0456','C0058','C0082','C0126','P0014','P0042']
con=sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro',uri=True)
result={}
for pid in IDS:
    pattern='%'+('p0288-' if pid=='P0288' else 'open-problem-'+pid.lower()+'-')+'%'
    rows=con.execute("SELECT id,title,body,metadata_json FROM nodes WHERE kind='claim' AND json_extract(metadata_json,'$.logical_id') LIKE ? ORDER BY created_at DESC LIMIT 2",(pattern,)).fetchall()
    selected=[]
    for nid,title,body,raw in rows:
        meta=json.loads(raw)
        selected.append({'node_id':nid,'logical_id':meta['logical_id'],'title':title,'body':body,'truth_status':meta.get('truth_status'),'source_id':meta.get('source_id')})
    result[pid]=selected
    print(pid,[(x['logical_id'],x['title']) for x in selected],flush=True)
bad=con.execute("SELECT id,title,metadata_json FROM nodes WHERE metadata_json LIKE ? ORDER BY created_at DESC LIMIT 3",('%c0151%',)).fetchall()
false=[{'node_id':nid,'title':title,'logical_id':json.loads(raw).get('logical_id')} for nid,title,raw in bad if 'c0151' not in str(json.loads(raw).get('logical_id','')).lower()]
con.close()
(ROOT/'reports'/'resolved_targets.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8')
(ROOT/'reports'/'metadata_substring_false_matches.json').write_text(json.dumps({'query':'metadata_json LIKE %c0151%','top_hits':len(bad),'incorrect_logical_targets':len(false),'false_hits':false,'correct_query':"json_extract(metadata_json,'$.logical_id') LIKE %open-problem-c0151-%"},indent=2),encoding='utf-8')
print('Unqualified metadata search:',len(false),'false logical targets out of',len(bad),flush=True)
