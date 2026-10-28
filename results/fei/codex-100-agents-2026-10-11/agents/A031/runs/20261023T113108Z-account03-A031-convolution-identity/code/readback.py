"""Independent persistence audit and scoped peer-review registration."""
from pathlib import Path
import json, hashlib
from datetime import datetime, timezone
R=Path(__file__).resolve().parent.parent
A=R.parent.parent
root=A.parent.parent
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def dump(p,o): p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(b): return hashlib.sha256(b).hexdigest()
protocol=load(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))['required_per_run']
claims=load(R/'CLAIMS.json')
peer_run=root/'agents/A035/runs/20261023T110610Z-account03-A035-signed-cancellation-countersearch'
srcclaims=load(peer_run/'CLAIMS.json')
peer=next(c for c in srcclaims if c['claim_id']=='A035-ALL-QUERY-TERMINAL-KL-ENVELOPE')
peer['review_records'].append({'reviewer':'A031','status':'ACCEPT_AT_STATED_SUPPLIED_SOURCE_SCOPE','source_statement_sha256':peer['statement_sha256'],'source_proof_sha256':sha((peer_run/'DERIVATION.md').read_bytes()),'artifact':'out/REVIEW_A035.json','scope':'Endpoint identity/original-source subtraction reconstructed and finite policies checked independently. Strengthened source originally A031; no claim of independent full-chain review. No universal initial-source conclusion.'})
peer['status']='SCOPED_ENDPOINT_TRANSFER_REVIEW_HOLDS_SOURCE_DEPENDENCY_RETAINED'
if not any(c['claim_id']==peer['claim_id'] for c in claims): claims.insert(0,peer)
dump(R/'CLAIMS.json',claims)
ack={'claim_id':srcclaims[0]['claim_id'],'source_review_records':srcclaims[0]['review_records'],'meaning':'A035 review of our stage19 source acknowledged; no new marker cycle claimed.'}
dump(R/'out/PREVIOUS_REVIEW_ACKNOWLEDGED.json',ack)
pr=load(R/'PROGRESS.json')
entry={'claim_id':peer['claim_id'],'version':peer['version'],'change':'A031 scoped review registered'}
if entry not in pr['claims_created_or_changed']: pr['claims_created_or_changed'].append(entry)
for p in ('out/PREVIOUS_REVIEW_ACKNOWLEDGED.json','out/REVIEW_A035.json'):
 if p not in pr['source_artifacts']: pr['source_artifacts'].append(p)
dump(R/'PROGRESS.json',pr); dump(R/'PACKET_DELTA.json',pr)
checks=[]
expected={x.split(' (')[0] for x in protocol['progress_fields']}
assert set(pr)==expected;checks.append('exact progress fieldset')
assert load(R/'PACKET_DELTA.json')==pr and pr['packet_ids']==['A031'];checks.append('packet compatibility copy')
for c in claims:
 assert set(c)==set(protocol['claim_fields'])
 assert sha(c['exact_statement'].encode('utf-8'))==c['statement_sha256']
checks.append('all claim exact fieldsets and statement hashes')
report=(R/'REPORT.md').read_text(encoding='utf-8')
for heading in protocol['report_fields']: assert '## '+heading in report
assert report.rstrip().split('\n\n')[-1].startswith('**Universal bridge:**')
checks.append('all report fields and final Universal bridge paragraph')
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
checks.append('rolling status exactly two lines')
changed=[]
for rec in load(R/'out/SOURCE_RECEIPTS.json'):
 if Path(rec['path'])==A/'LEARNED.md': continue # read before intentional append; preserved historical hash
 current=sha(Path(rec['path']).read_bytes())
 if current!=rec['sha256']: changed.append({'path':rec['path'],'recorded_sha256':rec['sha256'],'current_sha256':current})
dump(R/'out/LIVE_SOURCE_CHANGES.json',changed)
print(json.dumps({'changed_sources':changed}))
assert all(Path(rec['path']).name=='BOARD.md' for rec in changed), 'Changed mathematical dependency requires review; see LIVE_SOURCE_CHANGES.json'
checks.append('mathematical source hashes preserved; pre-append LEARNED historical and live BOARD changes explicitly recorded')
newclaim=next(c for c in claims if c['claim_id'].startswith('A031-SHARP'))
assert 'ghost' in newclaim['exact_statement']
for name in ['CHECK.json','REPRODUCE.json','GHOST_CHECK.json','GHOST_REPRODUCE.json']:
 result=load(R/'out'/name)
 assert result['checks']>0
checks.append('four exact-check receipts parsed with positive counts')
for p in R.rglob('*'):
 if p.is_file(): assert p.stat().st_size<20_000_000
checks.append('all run files below 20 MB')
manifest=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name not in ('MANIFEST.json','READBACK.json') and '__pycache__' not in p.parts:
  manifest.append({'path':p.relative_to(R).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())})
dump(R/'out/MANIFEST.json',{'created_utc':datetime.now(timezone.utc).isoformat(),'artifacts':manifest})
for rec in load(R/'out/MANIFEST.json')['artifacts']:
 assert sha((R/rec['path']).read_bytes())==rec['sha256']
checks.append('regenerated manifest re-read and all artifact hashes match')
dump(R/'out/READBACK.json',{'status':'PASS','checks':checks,'new_claim_external_peer_review':'PENDING','full_FEI':'OPEN','supervisor_copy':'PENDING','jobs':'All exact mathematical jobs completed; no detached job launched.'})
print(json.dumps({'status':'PASS','readback_checks':len(checks),'claims':len(claims),'artifacts':len(manifest),'full_FEI':'OPEN','external_peer_review':'PENDING'}))
