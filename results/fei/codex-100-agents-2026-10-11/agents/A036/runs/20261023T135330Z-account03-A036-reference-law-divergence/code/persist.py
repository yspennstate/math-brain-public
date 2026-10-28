from pathlib import Path
import json,hashlib,time
R=Path(__file__).resolve().parents[1];A=R.parents[1];checks=0
def ck(x):
 global checks
 checks+=1;assert x,checks
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
p=json.loads(protocol.read_text(encoding='utf-8-sig'))['required_per_run']
progress=json.loads((R/'PROGRESS.json').read_text());fields=set(p['progress_fields']);fields.remove('packet_ids (one primary ID, for compatibility)');fields.add('packet_ids')
ck(set(progress)==fields);ck(progress['packet_ids']==['A036']);ck((R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes())
claims=json.loads((R/'CLAIMS.json').read_text())
for c in claims:
 ck(set(c)==set(p['claim_fields']));ck(hashlib.sha256(c['exact_statement'].encode()).hexdigest()==c['statement_sha256'])
 ck(c['contributors']);ck(c['first_unproved_line'])
source=Path(claims[0]['review_records'][-1]['source_run'])
original=next(c for c in json.loads((source/'CLAIMS.json').read_text(encoding='utf-8-sig')) if c['claim_id']==claims[0]['claim_id'])
for key in ['claim_id','version','exact_statement','hypotheses','statement_sha256','contributors','proof_dependencies','supersedes','refutes','first_unproved_line']:
 ck(claims[0][key]==original[key])
ck(claims[0]['review_records'][-1]['substantive_repair']==False)
ck(claims[1]['review_records']==[])
report=(R/'REPORT.md').read_text()
for h in p['report_fields']:ck('## '+h in report)
ck(report.strip().split('\n')[-1].startswith('Universal bridge:'))
status=(A/'STATUS.md').read_text().splitlines();ck(len(status)==2 and status[0].startswith('STATE: ') and status[1].startswith('NEXT: '))
for name in ['REVIEW_PILOT.json','REVIEW_CHECK.json','REPAIR_PILOT.json','REPAIR_CHECK.json','INDEPENDENT_AUDIT.json']:
 ck(json.loads((R/'out'/name).read_text())['status']=='PASS')
for name in ['FROZEN_SPEC.json','REPAIR_FROZEN_SPEC.json','AUDIT_FROZEN_SPEC.json']:
 spec=json.loads((R/'out'/name).read_text())
 for key in ['helper_version','actual_Boolean_family','parameter_domain','case_count','symmetry','arithmetic','memory_estimate_MB','maximum_runtime_seconds']:
  # Repair frozen spec uses family alias, normalized in finalized spec before this check.
  ck(key in spec or (key=='actual_Boolean_family' and 'family' in spec))
ck('673/256' in claims[1]['exact_statement']);ck('673/256' in report)
ck('T=L/Z=H(v/Z)-log2 Z' in (R/'PROOF.md').read_text(encoding='utf-8'))
proof=(R/'PROOF.md').read_text(encoding='utf-8');ck('>673/256' in proof);ck('FIRST UNSUPPORTED UNIVERSAL LINE' in report)
inventory=[]
for f in sorted(R.rglob('*')):
 if not f.is_file() or f.name=='PERSISTENCE.json' or '__pycache__' in f.parts:continue
 ck(f.stat().st_size<20*1024*1024)
 inventory.append({'path':str(f.relative_to(R)),'bytes':f.stat().st_size,'sha256':sha(f)})
out={'status':'PASS','assertions':checks,'files':len(inventory),'maximum_file_bytes':max(x['bytes'] for x in inventory),'claims':len(claims),'packet_delta_identical':True,'external_review_new_claim':'PENDING','mirror_verified':False,'artifacts':inventory}
(R/'out/PERSISTENCE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='artifacts'}))
