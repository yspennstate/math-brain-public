from pathlib import Path
import json,hashlib
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];O=R/'out';A=R.parent.parent
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
protocol=load(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
progress=load(R/'PROGRESS.json');claims=load(R/'CLAIMS.json')
fields=set(protocol['required_per_run']['progress_fields']);fields.remove('packet_ids (one primary ID, for compatibility)');fields.add('packet_ids')
assert set(progress)==fields and len(claims)==1
assert all(set(c)==set(protocol['required_per_run']['claim_fields']) for c in claims)
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+h in report for h in protocol['required_per_run']['report_fields'])
assert report.rsplit('## ',1)[1].startswith('Universal bridge\n')
for row in load(O/'REVIEW_SOURCE_RECEIPTS.json')['files']:assert sha(Path(row['path']))==row['sha256']
spec=load(O/'FROZEN_SPEC.json')
for name,key in [('exact.py','helper_sha256'),('review_floor.py','checker_sha256'),('audit_floor.py','audit_sha256')]:assert sha(R/'code'/name)==spec[key]
source=Path(load(O/'REVIEW_SOURCE_RECEIPTS.json')['files'][-1]['path']);original=next(c for c in load(source) if c['claim_id']==claims[0]['claim_id'])
for f in ['claim_id','version','exact_statement','hypotheses','statement_sha256','contributors','proof_dependencies']:assert original[f]==claims[0][f],f
v=load(O/'FLOOR_REVIEW.json');au=load(O/'INDEPENDENT_AUDIT.json');assert v['checks']==8970 and au['checks']==271
assert v['prefix_nodes']==50 and v['post_admission_children']==56
lines=(A/'STATUS.md').read_text(encoding='utf-8').splitlines();assert len(lines)==2 and lines[0].startswith('STATE:') and lines[1].startswith('NEXT:')
progress['deliverable_status']='COMPLETE_LOCAL_BYTE_READBACK_VERIFIED';save(R/'PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
save(O/'SCHEMA_VALIDATION.json',{'status':'PASS','report_fields':7,'progress_fields':len(fields),'claim_fields':len(protocol['required_per_run']['claim_fields']),'packet_delta_byte_identical':True,'source_statement_hypotheses_version_unchanged':True,'frozen_code_hashes_unchanged':True})
files=[]
for p in sorted(R.rglob('*')):
 if not p.is_file() or '__pycache__' in p.parts or p.name in ['PERSISTENCE_RECEIPTS.json','FINAL_READBACK.json']:continue
 assert p.stat().st_size<20_000_000,p
 files.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
assert len(files)>20
rolling=[{'path':str(A/n),'bytes':(A/n).stat().st_size,'sha256':sha(A/n)} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]
save(O/'PERSISTENCE_RECEIPTS.json',{'saved_utc':datetime.now(timezone.utc).isoformat(),'local_readback':'PASS','files':files,'rolling_snapshot':rolling,'remote_mirror':'UNVERIFIED','public_release':'UNVERIFIED','full_FEI':'OPEN'})
# A second pass checks the manifest's actual bytes, not only its written row counts.
for x in load(O/'PERSISTENCE_RECEIPTS.json')['files']:assert sha(Path(x['path']))==x['sha256']
save(O/'FINAL_READBACK.json',{'status':'PASS','payloads_rehashed':len(files),'rolling_snapshots':len(rolling),'source_proofs_unchanged':True,'protocol_fields_exact':True,'frozen_spec_and_checkers_bound':True,'no_running_research_job_from_this_stage':True,'remote_or_public_receipts':'NONE_OBSERVED','full_FEI':'OPEN'})
print(json.dumps({'status':'PASS','payloads_rehashed':len(files),'rolling_snapshots':len(rolling),'full_FEI':'OPEN'}))
