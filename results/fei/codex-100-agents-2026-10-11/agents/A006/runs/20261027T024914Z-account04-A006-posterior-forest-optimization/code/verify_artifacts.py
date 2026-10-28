from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def rd(p):return json.loads(p.read_text(encoding='utf-8'))
protocol=rd(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))['required_per_run']
claims=rd(R/'CLAIMS.json');progress=rd(R/'PROGRESS.json')
expected={k.split(' ')[0] for k in protocol['claim_fields']}
assert all(set(c)==expected for c in claims)
expected={k.split(' ')[0] for k in protocol['progress_fields']}
assert set(progress)==expected
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert progress['packet_ids']==['A006']
for c in claims:
 assert c['first_unproved_line'] is None
c=claims[-1]
raw=json.dumps({'exact_statement':c['exact_statement'],'hypotheses':c['hypotheses']},ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')
assert hashlib.sha256(raw).hexdigest()==c['statement_sha256']
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
report=(R/'REPORT.md').read_text(encoding='utf-8')
for heading in protocol['report_fields']:assert '## '+heading in report
assert report.rsplit('## ',1)[-1].startswith('Universal bridge\n')
forest=rd(R/'out/CHECK.json');review=rd(R/'out/REVIEW.json')
assert forest['status']==review['status']=='PASS'
assert forest['assertions']==295 and review['assertions']==11673
assert forest['new_all_weight_and_mixture_gap']=='0'
assert forest['controls']['drop_incidence_caps_residual']=='-327'
assert forest['actual_distinct_runs']==15
assert (R/'out/LEAN.json').exists()
items=[]
for p in sorted(R.rglob('*')):
 if not p.is_file() or '__pycache__' in p.parts or p.name in ['PERSISTENCE.json','.final']:continue
 raw=p.read_bytes();assert len(raw)<20*1024*1024
 raw.decode('utf-8')
 items.append({'path':str(p.relative_to(R)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
rolling=[]
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
 p=A/name;raw=p.read_bytes();rolling.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
receipt={'status':'PASS','artifacts':items,'rolling':rolling,'exact_nonpilot_assertions':11968,'schemas':'protocol report_fields, claim_fields, progress_fields exact','statement_hash_algorithm':'new A006 claim: sha256 UTF8 compact sorted JSON of exact_statement and hypotheses; reviewed source metadata unchanged','new_review_status':'pending','mirror_status':'unverified','formal_status':'RUNTIME_UNVERIFIED; no target/axiom acceptance','checks':['all SHA readback','UTF8','sizes below20MB','required fields exact','delta byte equality','canonical new statement hash','report Universal bridge last','two-line status','exact output counts']}
(R/'out/PERSISTENCE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='\n')
for row in items:assert hashlib.sha256((R/row['path']).read_bytes()).hexdigest()==row['sha256']
(R/'.final').write_text('COMPLETE_LOCAL_READBACK_VERIFIED; FULL_FEI_OPEN; NEW_REVIEW_PENDING\n',encoding='utf-8',newline='\n')
print(json.dumps({'status':'PASS','files':len(items),'exact_nonpilot_assertions':11968,'new_claim_review':'pending','FEI':'OPEN'}))
