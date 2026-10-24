"""Record exact peer verdicts and observe ingestion without writing the store."""
from pathlib import Path
from datetime import datetime,timezone
import json
import sqlite3

root=Path(__file__).resolve().parent
peer=Path('~/brain_workers/w542/CLAIMS.jsonl')
receipts=[]
if peer.exists():
    with peer.open(encoding='utf-8') as source:
        for line_number,line in enumerate(source,1):
            if 'w541-S1.1-verdict' in line:
                row=json.loads(line)
                if row.get('id')=='w541-S1.1-verdict':
                    receipts.append({'observed_at':datetime.now(timezone.utc).isoformat(),'receipt_path':str(peer),'line':line_number,'reviewer_verdict':row})
(root/'REVIEW_RECEIPTS.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in receipts),encoding='utf-8')
assert len(receipts)==1 and receipts[0]['reviewer_verdict']['status']=='independently checked proof'
assert receipts[0]['reviewer_verdict']['independent_reviewer']=='w542'
claims_path=root/'CLAIMS.jsonl'
claims=[json.loads(line) for line in claims_path.read_text(encoding='utf-8').splitlines() if line]
for claim in claims:
    if claim['id']=='w541-S1.1':
        claim['status']='independently checked proof'
        claim['independent_reviewer']='w542; KEEP as proved Gaussian special case, no P0321 implication'
        claim['review_receipt']=str(peer)+':'+str(receipts[0]['line'])
        claim['reviewed_scope']='stipulated Gaussian special case only; not P0321'
claims_path.write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in claims),encoding='utf-8')

bundle=json.loads((root/'bundle_001.json').read_text(encoding='utf-8'))
logical=[f"math:{row['namespace']}:{row['logical_name']}" for row in bundle['entries']]
store=Path('~/math-brain-build/local/population/brain.sqlite3')
found=[]
with sqlite3.connect(store.as_uri()+'?mode=ro',uri=True,timeout=5) as db:
    placeholders=','.join('?' for _ in logical)
    rows=db.execute(f"SELECT id,title,metadata_json FROM nodes WHERE json_extract(metadata_json,'$.logical_id') IN ({placeholders})",logical).fetchall()
    for nodeid,title,metadata_json in rows:
        metadata=json.loads(metadata_json)
        found.append({'id':nodeid,'title':title,'logical_id':metadata['logical_id'],'truth_status':metadata.get('truth_status')})
state_path=root/'SUBMISSION_STATE.json'
state=json.loads(state_path.read_text(encoding='utf-8'))
state.update({'reviewed':False,'review_state':'partial: Gaussian special case independently checked by w542; L2 counterexample and fixed-distance reduction still await designated review','reviewed_entries':['gaussian-obstruction'],'review_receipt':'~/brain_workers/w541/REVIEW_RECEIPTS.jsonl','ingested':len({e['logical_id'] for e in found})==len(logical),'ingestion_check':{'observed_at':datetime.now(timezone.utc).isoformat(),'store':str(store),'read_mode':'ro','matched_nodes':found},'retrievable':'not tested through recall; ingestion observed separately','draft_label_note':'Published concept payload retains its as-prepared unreviewed labels; this receipt records the later-read partial review without editing the submitted artifact.'})
state_path.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
source_path=root/'SOURCE_STATUS.json'
status=json.loads(source_path.read_text(encoding='utf-8'))
status['independent_derivation']['review_status']='w542 KEEP: independently checked Gaussian special case only'
status['independent_derivation']['receipt']=str(peer)+':'+str(receipts[0]['line'])
status['paired_proof_audit']={'path':'AUDIT.md','scope':'L1-L3 conditional; M unproved','verdict':'KEEP conditional lemmas; qualify descriptive volume-only-error sentence'}
status['next']='w542 checks S1.2-S1.3; the next research input is microscopic anchored connected-cumulant/bond-insertion control M.'
source_path.write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'submitted':state['submitted'],'reviewed':state['reviewed'],'independently_checked_claim':'w541-S1.1','ingested':state['ingested'],'canonical_nodes_found':len(found),'retrievable':state['retrievable'],'store_mode':'ro'}))
