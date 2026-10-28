from pathlib import Path
from fractions import Fraction
import json, hashlib, re, datetime

run=Path(__file__).resolve().parents[1]
root=run.parents[1]
proto=Path(r'math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def locate(x,k):
 if isinstance(x,dict):
  if k in x:return x[k]
  for v in x.values():
   z=locate(v,k)
   if z is not None:return z
 if isinstance(x,list):
  for v in x:
   z=locate(v,k)
   if z is not None:return z
schema=read(proto)
progress=read(run/'PROGRESS.json')
expected=[x.split(' (')[0] for x in locate(schema,'progress_fields')]
assert set(progress)==set(expected)
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert progress['packet_ids']==['A001']
claims=read(run/'CLAIMS.json')
assert len(claims)==4
for c in claims:
 assert set(c)==set(locate(schema,'claim_fields'))
 assert isinstance(c['exact_statement'],str)
 assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
report=(run/'REPORT.md').read_text(encoding='utf-8-sig')
assert re.findall(r'^# (.+)$',report,re.M)==locate(schema,'report_fields')
assert report.strip().split('\n\n')[-1].startswith('**Universal bridge:**')
assert 'Full FEI remains OPEN' in report and '144688' in report
status=(root/'STATUS.md').read_text(encoding='utf-8-sig').splitlines()
assert len(status)==2 and status[0].startswith('STATE: ') and status[1].startswith('NEXT: ')
assert 'degraded/unverified' in report
checks=[read(run/'out'/p) for p in ['CHECK.json','CONTROLLER_CHECK.json','SUPPLIER_CHECK.json','BLOCK_AUDIT.json']]
assert sum(c['exact_assertions'] for c in checks)==144688
assert all(c['status']=='PASS' and c['elapsed_seconds']<55 for c in checks)
assert len(checks[0]['rows'])==72
for row in checks[0]['rows']:
 assert Fraction(row['margin']['interval'][0])>Fraction(253105,10**6)
 if row['parameters']==['1','1']:
  assert Fraction(row['margin']['interval'][1])<Fraction(253106,10**6)
assert checks[1]['case_count']==768 and checks[2]['case_count']==6 and checks[3]['case_count']==768
for data in [checks[1],checks[3]]:
 for row in data['rows']:
  key='mean_signed_reset' if 'mean_signed_reset' in row else 'whole_liability_change'
  assert Fraction(row[key]['interval'][1])<=0
receipt=run/'out/PERSISTENCE_RECEIPT.json'
artifacts=[]
for p in sorted(run.rglob('*')):
 if not p.is_file() or p==receipt:continue
 assert p.stat().st_size<20*1024*1024
 artifacts.append({'path':str(p.relative_to(run)),'size':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
assert len(artifacts)>=20
result={'status':'PASS','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'schema_fields_exact':True,'progress_copies_identical':True,'statement_hashes_verified':4,'exact_assertions':144688,'independent_review':'A004 review of previous canonical statement consumed unchanged; three new claims pending','universal_FEI':'OPEN','kernel_certification':False,'artifacts':artifacts,'rolling_files':[{'path':str(root/p),'sha256':hashlib.sha256((root/p).read_bytes()).hexdigest()} for p in ['STATUS.md','WORKLOG.md','LEARNED.md']]}
receipt.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='')
assert read(receipt)['status']=='PASS'
print(json.dumps({'status':'PASS','hashed_artifacts':len(artifacts),'exact_assertions':144688,'claims':4,'full_FEI':'OPEN'}))
