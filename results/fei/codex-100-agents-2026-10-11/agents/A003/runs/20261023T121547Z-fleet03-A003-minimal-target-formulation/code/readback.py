"""Final persistence/readback audit and source-bound prior-stage review receipt."""
import json,hashlib,datetime
from pathlib import Path
R=Path(__file__).resolve().parents[1]; A=R.parents[1]; ROOT=A.parents[1]
def read(p): return p.read_text(encoding='utf-8')
def save(p,x): p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
src=ROOT/'agents/A004/runs/20261023T070305Z-fleet03-A004-constant-and-unit-ledger/CLAIMS.json'
claims=json.loads(read(src)); prior=next(x for x in claims if x['claim_id']=='A003-REFERENCE-SINGLETON-DISCREPANCY-FUNDED-RESET')
oldsrc=A/'runs/20261023T062246Z-fleet03-A003-minimal-target-formulation/CLAIMS.json'
old=json.loads(read(oldsrc))[0]
assert prior['statement_sha256']==old['statement_sha256']
review=next(x for x in prior['review_records'] if x['reviewer']=='A004/fleet03')
assert review['verdict']=='HOLDS unchanged at supplied-source scope'
save(R/'out/PRIOR_STAGE19_REVIEW_RECEIPT.json',{'source':str(src),'source_sha256':sha(src),'claim_id':prior['claim_id'],'version':prior['version'],'statement_sha256':prior['statement_sha256'],'review':review,'scope':'Record existing independent A004 acceptance; A003 does not claim to independently accept its own theorem or audit every A004 result.'})
report=read(R/'REPORT.md')
marker='Additional source-bound receipt: A004 run20261023T070305Z CLAIMS.json independently accepts the unchanged stage19 A003 discrepancy theorem at its supplied-source scope (statement SHA256 92ff79e4608a696a33eb048444fa1d4cedbc88e538b7924e8a144f46b12a51a9). This is recorded in out/PRIOR_STAGE19_REVIEW_RECEIPT.json; the NEW stage20 theorem remains pending independent review.'
heading='## one next mathematical action and independent reviewer'
if marker not in report:
 report=report.replace(heading,marker+'\n\n'+heading)
 (R/'REPORT.md').write_text(report,encoding='utf-8')
status=read(A/'STATUS.md')
if 'stage19 accepted by A004;' not in status:
 status=status.replace('full FEI OPEN.','stage19 accepted by A004;full FEI OPEN.')
 (A/'STATUS.md').write_text(status,encoding='utf-8')
for filename in ['WORKLOG.md','LEARNED.md']:
 p=A/filename; text=read(p)
 line='\n2026-10-23 stage20 review receipt: A004 source CLAIMS independently accepts unchanged A003 stage19 discrepancy theorem, SHA92ff79e4608a696a33eb048444fa1d4cedbc88e538b7924e8a144f46b12a51a9; supplied-source scope only. Stage20 independent review remains pending.\n'
 if line not in text: p.write_text(text+line,encoding='utf-8')
# Reopen actual deliverables, validate stored data, and inspect every prior receipt.
assert read(A/'STATUS.md').splitlines()[0].startswith('STATE: ')
assert len(read(A/'STATUS.md').splitlines())==2
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
claim=json.loads(read(R/'CLAIMS.json'))[0]
assert hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
assert report.rstrip().splitlines()[-1].startswith('**Universal bridge:**')
assert 'K L I(g)-H(g)' in read(R/'DERIVATION.md') or 'K L J-H' in read(R/'DERIVATION.md')
assert 'First unsupported universal line:' in report
assert json.loads(read(R/'out/CHECK_FULL.json'))['assertions']==1828004
receipts=[]
for p in R.rglob('*'):
 if p.is_file() and p.name not in ['RECEIPTS.json','FINAL_READBACK.json']:
  assert p.stat().st_size<20_000_000
  receipts.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
save(R/'out/RECEIPTS.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'artifacts':receipts,'scope':'Final local readback only; no remote mirror verification'})
stored=json.loads(read(R/'out/RECEIPTS.json'))
for row in stored['artifacts']: assert sha(R/row['path'])==row['sha256']
save(R/'out/FINAL_READBACK.json',{'status':'PASS','verified_artifacts':len(receipts),'protocol_files_reopened':True,'statement_hash_verified':True,'progress_delta_identical':True,'status_two_lines':True,'prior_stage19_independent_acceptance':'A004 unchanged supplied-source scope','new_stage20_independent_review':'PENDING','full_FEI':'OPEN'})
print(json.dumps(json.loads(read(R/'out/FINAL_READBACK.json'))))
print(read(A/'STATUS.md'))
print(report.rstrip().splitlines()[-1])
