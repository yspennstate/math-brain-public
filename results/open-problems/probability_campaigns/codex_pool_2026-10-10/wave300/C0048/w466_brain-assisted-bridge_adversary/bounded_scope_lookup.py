"""Bounded targeted brain lookup; measures scope without invoking whole-store recall."""
from pathlib import Path
import json
import sqlite3
import subprocess
import time
import re

root=Path(__file__).resolve().parent
broad=json.loads((root/'brain_target_nodes.json').read_text(encoding='utf-8'))
started=time.perf_counter()
args=['rg','-i','-m','6','C0048',
      '~/math-brain-build/export/population/nodes.jsonl']
r=subprocess.run(args,capture_output=True,text=True,encoding='utf-8')
if r.returncode not in (0,1):
    raise RuntimeError(r.stderr)
raw_candidates=[json.loads(s) for s in r.stdout.splitlines() if s.strip()]
target=[]
rejected=[]
for candidate in raw_candidates:
    logical=json.loads(candidate['metadata_json']).get('logical_id','')
    if re.search(r':(?:open-problem|attempt)-c0048-',str(logical),re.I):
        target.append(candidate)
    else:
        rejected.append({'id':candidate['id'],'logical_id':logical,
                         'reason':'C0048 occurred in unrelated bytes such as a digest; not the candidate logical ID.'})
grep_seconds=time.perf_counter()-started
con=sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro',uri=True,timeout=3)
con.execute('PRAGMA query_only=ON')
started_sql=time.perf_counter()
con.set_progress_handler(lambda:int(time.perf_counter()-started_sql>8),10000)
live=[]
for node in target:
    row=con.execute('SELECT id,kind,title,body,metadata_json FROM nodes WHERE id=?',(node['id'],)).fetchone()
    if row:
        live.append(dict(zip(('id','kind','title','body','metadata_json'),row)))
sql_seconds=time.perf_counter()-started_sql
con.close()
(root/'brain_C0048_nodes.json').write_text(json.dumps(live,ensure_ascii=False,indent=2),encoding='utf-8')
result={'kind':'local targeted lookup diagnostic; not ranked production recall',
 'baseline':{'query':'broad title Potts OR mean-field OR C0048, first 12 file-order matches',
             'cards':len(broad),'spin_glass_cards':sum('spin glass' in n['title'].lower() for n in broad),
             'C0048_cards':sum('c0048' in json.dumps(n).lower() for n in broad)},
 'bounded_repair':{'query_argv':args,'grep_seconds':grep_seconds,
                   'raw_grep_candidates':len(raw_candidates),
                   'rejected_false_ID_matches':rejected,
                   'grep_cards':len(target),'live_id_fetch_seconds':sql_seconds,
                   'live_cards':len(live),
                   'spin_glass_cards':sum('spin glass' in n['title'].lower() for n in live)},
 'initial_failure':{'query':"SELECT id,kind,title,body,metadata_json FROM nodes WHERE title LIKE '%Potts%' OR body LIKE '%C0048%' OR title LIKE '%Biskup%' LIMIT 30",
                    'budget_seconds':8,'returned_cards':0,'observed_error':'sqlite3.OperationalError: interrupted',
                    'evidence':'inspect_store.py, first target lookup tool run'},
 'limitation':'Broad file-order grep deliberately has low specificity; this comparison is not a benchmark of brain ranking. The ID fetch establishes live presence, not source accuracy or theorem applicability. No global recall control was changed.'}
(root/'measurement_retrieval.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
for node in live:
    meta=json.loads(node['metadata_json'])
    print(json.dumps({'id':node['id'],'logical_id':meta.get('logical_id'),
          'title':node['title'],'body':node['body']},ensure_ascii=False))
