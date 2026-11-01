"""Check artifact integrity and only the exact target cards in the live read-only store."""
from pathlib import Path
import datetime as dt
import hashlib
import json
import sqlite3
import time

ROOT=Path(__file__).resolve().parent
required=['STATUS.md','SOURCE_STATUS.json','ATTEMPT.md','REDUCTION.md','CLAIMS.jsonl',
          'PAIRED_AUDIT.md','REVIEW_PACKET.md','REPORT.md','measurement.json','compute_gate.json',
          'bundle_001.json','DRAFT_SUBMISSION.json','HOOK_PROPOSALS.jsonl']
assert all((ROOT/name).is_file() for name in required)
claims=[json.loads(line) for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
assert len(claims)==4
assert len({r['claim_id'] for r in claims})==4
claim_fields={'exact_statement','assumptions','source','proof_or_counterexample','independent_reviewer','remaining_gap','status'}
assert all(claim_fields <= row.keys() for row in claims)
assert all(row['status']=='proved special case' for row in claims)
assert all(row.get('brain_state')=='draft' for row in claims)

bundle=json.loads((ROOT/'bundle_001.json').read_text(encoding='utf-8'))
inbox=Path('~/math-brain-inbox/w409/bundle_001.json')
assert inbox.read_bytes()==(ROOT/'bundle_001.json').read_bytes()
assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w409'
assert len(bundle['entries'])==3
keys={row['key'] for row in bundle['entries']}
fields={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
for row in bundle['entries']:
    assert fields <= row.keys()
    assert row['kind']=='concept' and row['proof_text'] is None
    assert row['statement'].startswith('UNREVIEWED DRAFT')
    assert row['source']['license'].startswith('owner-own-work')
for rel in bundle['relations']:
    assert rel['from_key'] in keys and rel['to_key'] in keys
    assert rel['kind']=='semantic_association'
receipt=json.loads((ROOT/'measurement.json').read_text(encoding='utf-8'))
assert receipt['exact_assertions_passed']==198 and receipt['cells_checked']==85
assert not receipt['formal_proof']
hook=json.loads((ROOT/'HOOK_PROPOSALS.jsonl').read_text(encoding='utf-8').strip())
assert len(hook['text'])<=300 and hook['fire_when'] and hook['silent_when']

# The snapshot hash identifies the reviewed proof bytes; it is not a bundle digest or proof receipt.
peer=Path('~/brain_workers/w408/ATTEMPT.md')
peer_bytes=peer.read_bytes()
snapshot=ROOT/'w408_ATTEMPT.snapshot.md'
snapshot.write_bytes(peer_bytes)
audit_source={'source_path':str(peer),'snapshot_path':str(snapshot),
              'source_sha256':hashlib.sha256(peer_bytes).hexdigest(),
              'frozen_at_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
              'reviewed_sections':['L1','L2','L3','stopped Cardy input'],
              'hash_is_not_a_mathematical_proof':True}
(ROOT/'AUDIT_SOURCE.json').write_text(json.dumps(audit_source,indent=2),encoding='utf-8')

dbpath=Path('~/math-brain-build/local/population/brain.sqlite3')
store_result={'path':str(dbpath),'mode':'read-only','new_draft_retrieval_checked':False}
try:
    db=sqlite3.connect(dbpath.as_uri()+'?mode=ro',uri=True,timeout=3)
    deadline=time.monotonic()+5
    db.set_progress_handler(lambda: int(time.monotonic()>deadline),10000)
    ids=['claim_07a861a72ebeb008dc23e9db32147327c062427adee7a530bab01f0de67bd002',
         'claim_91f295e6d2a67634c0b90a5ee4130c1feed72dc0fe16086a679021c90c8917cb']
    rows=[]
    for nodeid in ids:
        row=db.execute('SELECT id,title,metadata_json FROM nodes WHERE id=?',(nodeid,)).fetchone()
        if row:
            meta=json.loads(row[2])
            rows.append({'id':row[0],'title':row[1],'logical_id':meta.get('logical_id'),
                         'claim_kind':meta.get('claim_kind'),'truth_status':meta.get('truth_status')})
    store_result['exact_existing_target_cards']=rows
    db.close()
except (sqlite3.Error,OSError) as exc:
    store_result['read_status']=type(exc).__name__+': '+str(exc)
(ROOT/'STORE_READ_CHECK.json').write_text(json.dumps(store_result,indent=2),encoding='utf-8')

source_status=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
source_status['live_store_readonly_check']='STORE_READ_CHECK.json; exact known node IDs only'
source_status['owner_solved_register_check']='Targeted C0017/conformal-percolation lookup in the named solved register returned no match; no global solved-work inference.'
(ROOT/'SOURCE_STATUS.json').write_text(json.dumps(source_status,indent=2),encoding='utf-8')
result={'artifact_validation':'PASS','claims':len(claims),'draft_concepts':len(bundle['entries']),
        'draft_relations':len(bundle['relations']),'hook_proposals':1,
        'exact_arithmetic_assertions':receipt['exact_assertions_passed'],
        'independent_referee_clearance':'pending','target_proof':'not established',
        'store_readonly_check':store_result}
(ROOT/'VALIDATION.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
