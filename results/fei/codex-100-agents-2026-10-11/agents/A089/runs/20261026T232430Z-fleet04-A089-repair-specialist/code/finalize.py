from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def dump(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
formal=json.loads((R/'out/FORMAL.json').read_text(encoding='utf-8'))
assert formal['exit_code']==2 and 'no new compiler process' in formal['stdout']
p=R/'REPORT.md';s=p.read_text(encoding='utf-8');s=s.replace('Its rung and any admission blocker must be read from that receipt; it certifies at most the named integer regrouping, never the real allocation theorem or entropy proof.','The attempt returned exit2, SETUP_UNVERIFIED: the fresh admission check held for a hung window or less than5500MB available memory. No compiler process launched. Formal rung is INCOMPLETE, not a pass or a mathematical refutation; no Lean certification is claimed.')
p.write_text(s,encoding='utf-8',newline='\n')
p=R/'PROOF.md';s=p.read_text(encoding='utf-8');s+='\nFormal receipt: the guarded core attempt returned SETUP_UNVERIFIED (exit2), with no compiler process launched because compute admission held. No Lean-checked mathematical result is claimed. The analytic proof and exact finite certificates are the achieved rung.\n';p.write_text(s,encoding='utf-8',newline='\n')
for name in ['PROGRESS.json','PACKET_DELTA.json']:
 p=R/name;v=json.loads(p.read_text(encoding='utf-8'));v['blockers'].append('Lean core attempt INCOMPLETE: admission held, no compiler launched; no Lean certification.');dump(p,v)
protocol=json.loads(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
fields=protocol['required_per_run'];pf=[x.split(' (')[0] for x in fields['progress_fields']]
v=json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'));assert set(v)==set(pf)
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
claims=json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'))
for c in claims:assert set(c)==set(fields['claim_fields'])
assert claims[1]['statement_sha256']==hashlib.sha256(claims[1]['exact_statement'].encode('utf-8')).hexdigest()
src=json.loads((R/'out/A075_SOURCE_CLAIM.json').read_text(encoding='utf-8'))
for k in ['exact_statement','hypotheses','statement_sha256','version','claim_id']:assert claims[0][k]==src[k]
sources=json.loads((R/'out/SOURCE_RECEIPTS.json').read_text(encoding='utf-8'))
for row in sources:assert sha(Path(row['path']))==row['sha256']
status=(A/'STATUS.md').read_text(encoding='utf-8').splitlines();assert len(status)==2 and status[0].startswith('STATE: ') and status[1].startswith('NEXT: ')
report=(R/'REPORT.md').read_text(encoding='utf-8')
for f in fields['report_fields']:assert '## '+f in report
assert report.rstrip().splitlines()[-1].startswith('**Universal bridge:**')
assert json.loads((R/'out/VALIDATION.json').read_text(encoding='utf-8'))['total_checks']==38022
assert json.loads((R/'out/INDEPENDENT_WITNESS.json').read_text(encoding='utf-8'))['partial_assignments']==27
audit={'status':'PASS','protocol_fields':'exact','claim_versions':2,'main_predicates':38022,'runtime_guards_included':3072,'separate_witness_restrictions':27,'source_files_rechecked':len(sources),'formal_rung':'INCOMPLETE_ADMISSION_HELD_NO_COMPILER','full_FEI':'OPEN','external_review_repaired_proof':'PENDING','remote_persistence':'UNVERIFIED'}
dump(R/'out/FINAL_AUDIT.json',audit)
inventory=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE.json':
  assert p.stat().st_size<20_000_000
  if p.suffix in ['.md','.json','.py','.lean','.jsonl']:p.read_text(encoding='utf-8')
  inventory.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for name in ['STATUS.md','LEARNED.md','WORKLOG.md']:
 p=A/name;inventory.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
dump(R/'out/PERSISTENCE.json',{'scope':'local snapshot; manifest excludes itself to avoid circular hash; no remote receipt asserted','files':inventory})
print(json.dumps(audit))
