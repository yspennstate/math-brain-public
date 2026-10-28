from pathlib import Path
from fractions import Fraction as F
import json,hashlib
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def rd(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=rd(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
claim=rd(R/'CLAIMS.json')[0];assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert claim['version']==5 and not claim['review_records']
assert hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
p=rd(R/'PROGRESS.json');assert set(p)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']};assert p['packet_ids']==['A011']
v=rd(R/'out/VALIDATION_SUMMARY.json');assert v['all_validation_assertions']==2576591
assert (v['main']['sequences'],v['main']['target_prefixes'],v['main']['frontiers'])==(54,162,2646)
assert 4*F(4081,4096)-F(125,46)-1==F(6311,23552)>0
assert 15*F(4081,4096)-320*F(151,8192)-F(37,8)==F(18111,4096)>0
receipts=rd(R/'out/ARTIFACT_RECEIPTS.json')
for row in receipts['files']:
 q=Path(row['path']);q=q if q.is_absolute() else R/q
 assert q.stat().st_size==row['bytes'] and sha(q)==row['sha256'],str(q)
report=R/'REPORT.md';text=report.read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:assert '## '+field in text
assert text.strip().split('\n\n')[-1].startswith('Universal bridge:')
assert 'does not bound the sum of positive resets alone' in text and 'Full FEI OPEN' in text
closure=rd(R/'out/CHECKLIST_CLOSURE.json');closed=closure['status']=='DONE'
closing='Checklist entry T-20261023-514 closed for this completed local stage.' if closed else 'Checklist entry T-20261023-514 closure remains blocked by the shared checklist service; the exact error is preserved in out/CHECKLIST_CLOSURE.json.'
report.write_text(text.rstrip()+' '+closing+' Full FEI and independent v5 review remain open.\n',encoding='utf-8',newline='')
status=A/'STATUS.md';lines=status.read_text(encoding='utf-8').splitlines();assert len(lines)==2
assert lines[0].startswith('STATE:') and lines[1].startswith('NEXT:')
if not closed:lines[1]+=' Retry shared checklist closure when its lock/service recovers.'
status.write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='')
if not closed:
 p['blockers'].append('Shared checklist closure failed; mathematical stage and local files complete. See CHECKLIST_CLOSURE.json.')
 (R/'PROGRESS.json').write_text(json.dumps(p,indent=2)+'\n',encoding='utf-8',newline='');(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:f.write('\nChecklist T-20261023-514 closure status:'+closure['status']+'; initial lock failure preserved. NEXT retained: independent v5 reconstruction and cancellation-aware source admission. Clarified that the exact cubic tail is for the normalized geometric majorant, not equality for arbitrary-width S_M. Final schema/hash audit passed.\n')
out={'status':'PASS','verified_prior_receipts':len(receipts['files']),'claim_version':5,'statement_sha256':claim['statement_sha256'],'protocol_fields_exact':True,'progress_delta_byte_identity':True,'validation_assertions':2576591,'external_review':'Pending, not created by author or this audit','remote_mirror':'Supervisor handoff unverified','left_running':'Nothing; all mathematical jobs completed','checklist':closure['status']}
dest=R/'out/FINAL_AUDIT.json';dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
rows=[]
for q in sorted(R.rglob('*')):
 if q.is_file() and q.name!='ARTIFACT_RECEIPTS.json':
  assert q.stat().st_size<20_000_000,str(q)
  rows.append({'path':str(q.relative_to(R)),'bytes':q.stat().st_size,'sha256':sha(q)})
for n in ['STATUS.md','WORKLOG.md','LEARNED.md']:
 q=A/n;rows.append({'path':str(q),'bytes':q.stat().st_size,'sha256':sha(q)})
receipts['files']=rows;(R/'out/ARTIFACT_RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps(out))
