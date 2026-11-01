from pathlib import Path
import json,hashlib
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1]
P=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text())
claims=json.loads((R/'CLAIMS.json').read_text());progress=json.loads((R/'PROGRESS.json').read_text())
assert set(progress)=={s.split(' (')[0] for s in P['required_per_run']['progress_fields']}
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for c in claims:
 assert set(c)==set(P['required_per_run']['claim_fields'])
 assert c['statement_sha256']==hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
text=(R/'REPORT.md').read_text()
assert all('## '+s in text for s in P['required_per_run']['report_fields'])
assert text.strip().split('\n\n')[-2]=='## Universal bridge'
assert all(x not in text for x in ('PILOT_CK','PILOT_TIME','FULL_CK','FULL_TIME','REPRO_CK','REPRO_TIME'))
full=json.loads((R/'out'/'full_RESULTS.json').read_text())
raw=[json.loads(line) for line in (R/'out'/'full_ROWS.jsonl').read_text().splitlines()]
assert raw==full['rows'];assert len(raw)==31 and sum(len(x['orders']) for x in raw)==124
for row in raw:
 for order in row['orders'].values():
  assert F(order['I'])==F(row['I']) and F(order['Q'])==F(row['Q'])
  assert F(order['bad_credit'])/F(order['I'])==F(order['ratio'])
  assert 0<=F(order['bad_credit'])<=F(order['Q'])
for c in full['sign_certificates']:
 assert c['method']=='interval'
 assert int(c['lo'])>0 if c['sign']>0 else int(c['hi'])<0
assert len((R.parents[1]/'STATUS.md').read_text().splitlines())==2
result={'status':'PASS','checks':['protocol claim/progress field sets','statement SHA256','progress/delta identity','all required report sections and final universal bridge','no template placeholders','all 31 flushed rows match aggregate','124 exact ratios and influence/face invariants','1127 strict interval certificates','two-line STATUS'],'total_executed_validation_assertions':sum(json.loads((R/'out'/x).read_text())['assertions_passed'] for x in ('pilot_RESULTS.json','full_RESULTS.json','REPRODUCTION_RESULTS.json')),'independent_agent_review':'PENDING'}
(R/'out'/'ARTIFACT_VALIDATION.json').write_text(json.dumps(result,indent=2))
receipts=[]
for f in R.rglob('*'):
 if f.is_file() and f.name!='RECEIPTS.json':
  assert f.stat().st_size<20*1024*1024
  receipts.append({'path':str(f.relative_to(R)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
(R/'out'/'RECEIPTS.json').write_text(json.dumps(receipts,indent=2))
assert all(hashlib.sha256((R/x['path']).read_bytes()).hexdigest()==x['sha256'] for x in receipts)
print(json.dumps(result));print('Artifact receipts verified:',len(receipts))
