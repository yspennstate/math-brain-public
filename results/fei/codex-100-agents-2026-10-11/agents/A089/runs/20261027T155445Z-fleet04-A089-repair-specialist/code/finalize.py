from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def dump(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=json.loads(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
fields=protocol['required_per_run'];pf={s.split(' (')[0] for s in fields['progress_fields']}
progress=json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'));assert set(progress)==pf
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
claims=json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'))
for c in claims:assert set(c)==set(fields['claim_fields'])
assert claims[1]['statement_sha256']==hashlib.sha256(claims[1]['exact_statement'].encode('utf-8')).hexdigest()
source=json.loads((R/'out/SOURCE_CLAIM.json').read_text(encoding='utf-8'))
for k in ['claim_id','version','exact_statement','hypotheses','statement_sha256']:assert claims[0][k]==source[k]
assert sha(R/'code/check_v1.py')==json.loads((R/'out/MAIN_INCOMPLETE.json').read_text(encoding='utf-8'))['code_sha256']
v=json.loads((R/'out/VALIDATION.json').read_text(encoding='utf-8'));assert v['status']=='PASS' and v['summary_circuits']==712 and v['source_cases']==56 and v['total_predicates']==19494
assert json.loads((R/'out/INDEPENDENT_ORIGINAL_OWNER.json').read_text(encoding='utf-8'))['cases']==32
assert json.loads((R/'out/FORMAL.json').read_text(encoding='utf-8'))['no_Lean_certificate'] is True
report=(R/'REPORT.md').read_text(encoding='utf-8')
for f in fields['report_fields']:assert '## '+f in report
assert report.rstrip().splitlines()[-1].startswith('**Universal bridge:**')
assert 'INCOMPLETE' in report and 'coefficient ONE' in report
status=(A/'STATUS.md').read_text(encoding='utf-8').splitlines();assert len(status)==2 and status[0].startswith('STATE: ') and status[1].startswith('NEXT: ')
for row in json.loads((R/'out/SOURCE_RECEIPTS.json').read_text(encoding='utf-8')):
 if Path(row['path']).name not in ['BOARD.md']:assert sha(Path(row['path']))==row['sha256']
audit={'status':'PASS','exact_protocol_key_sets':True,'source_version_unchanged':True,'main_predicates':19494,'included_runtime_guards':712,'certified_summary_circuits':712,'source_cases':56,'independent_source_cases':32,'original9280_domain':'INCOMPLETE_NOT_COUNTED','formal':'ADMISSION_HELD_NO_COMPILER','new_source_external_review':'PENDING','full_FEI':'OPEN','remote_persistence':'UNVERIFIED'}
dump(R/'out/FINAL_AUDIT.json',audit)
inventory=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE.json':
  assert p.stat().st_size<20_000_000
  if p.suffix in ['.md','.json','.py','.lean','.jsonl']:p.read_text(encoding='utf-8')
  inventory.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
 p=A/name;inventory.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
dump(R/'out/PERSISTENCE.json',{'scope':'local files only; manifest excludes itself; supervisor remote copy unverified','files':inventory})
print(json.dumps(audit))
