"""Observe only the two submitted drafts' exact IDs in the read-only store."""
import datetime
import json
import sqlite3
from pathlib import Path

root=Path(__file__).resolve().parent
receipts=[json.loads((root/name).read_text(encoding='utf-8')) for name in
          ('submission_receipt.json','followup_submission_receipt.json')]
assert all(r['submitted'] for r in receipts)
bundles=[json.loads(Path(r['draft_path']).read_text(encoding='utf-8')) for r in receipts]
logical=[f"math:{e['namespace']}:{e['logical_name']}" for bundle in bundles for e in bundle['entries']]
assert len(logical)==len(set(logical))==12
db=Path(r'~\math-brain-build\local\population\brain.sqlite3').resolve(strict=True)
with sqlite3.connect(db.as_uri()+'?mode=ro',uri=True,timeout=5) as conn:
    conn.execute('PRAGMA query_only=ON')
    query="SELECT id,title,body,metadata_json FROM nodes WHERE json_extract(metadata_json,'$.logical_id') IN ("+','.join('?' for _ in logical)+') LIMIT 24'
    rows=conn.execute(query,logical).fetchall()
found={json.loads(m)['logical_id'] for _,_,_,m in rows}
observed={'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'method':"Strict read-only fetch by the two submitted drafts' exact logical IDs; ranked recall not run",
 'submitted':True,'reviewed':False,'ingested':bool(rows),'retrievable':bool(rows),
 'expected_entries':len(logical),'found_entries':len(found),'complete_ingestion_observed':set(logical)==found,
 'draft_paths':[r['draft_path'] for r in receipts],
 'retrieval_scope':'exact logical-ID fetch only','cards':[{'id':i,'title':t,'body':b,'metadata':json.loads(m)} for i,t,b,m in rows]}
(root/'brain_state_observation.json').write_text(json.dumps(observed,indent=2,ensure_ascii=False),encoding='utf-8')
source=json.loads((root/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
source['brain_states']={k:observed[k] for k in ('submitted','reviewed','ingested','retrievable')}
source['brain_state_observed_at']=observed['observed_at']
source['brain_state_observation_method']=observed['method']
source['draft_paths']=observed['draft_paths']
source['ingested_entry_count']=len(found)
(root/'SOURCE_STATUS.json').write_text(json.dumps(source,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in observed.items() if k!='cards'},indent=2))
