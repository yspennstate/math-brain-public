from pathlib import Path
from fractions import Fraction as F
import hashlib,json,datetime
R=Path(__file__).resolve().parents[1]
def js(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
receipt=js(R/'out/PERSISTENCE_RECEIPTS.json')
assert all(sha(R/x['path'])==x['sha256'] for x in receipt['files'])
assert F(123,128)*4-F(13,4)==F(19,32)
assert F(123,128)*15-F(645,128)==F(75,8)
assert F(19,32)-F(1,4)==F(11,32)
assert F(75,8)-F(15,16)==F(135,16)
assert F(105,32)+100*F(9,512)==F(645,128)
claim=js(R/'CLAIMS.json')[0];report=(R/'REPORT.md').read_text(encoding='utf-8')
assert claim['version']==3 and not claim['review_records']
assert claim['statement_sha256']==hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()
assert '## Universal bridge'==report.strip().split('\n\n')[-2]
assert 'full FEI is OPEN' in report and 'Delta is not described as a KL-only physical reset.' in report
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((R.parents[1]/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
totals=js(R/'out/VALIDATION_TOTALS.json');assert totals['exact_assertions']==3040390
assert sum(x['positive_signed_resets'] for x in totals['primary'] if x['mode'] in ['0','1','2','3'])==785
assert totals['independent_replay']['frontiers']==28
out={'status':'PASS','preexisting_file_hashes_checked':len(receipt['files']),'symbolic_margin_identities':5,'exact_assertions_in_executed_jobs':3040390,'scope':'saved bytes, schemas, statement digest, full report scope and exact rational margin arithmetic; does not create an independent-agent proof review','jobs_left_running':0,'work_stopped':0,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(R/'out/FINAL_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
files=[p for p in sorted(R.rglob('*')) if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']
receipt['files']=[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]
(R/'out/PERSISTENCE_RECEIPTS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps(out))
