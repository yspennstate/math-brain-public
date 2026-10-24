from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path(__file__).resolve().parents[1]
def read(p):return p.read_text(encoding='utf-8-sig')
def write(p,s):p.write_text(s,encoding='utf-8',newline='\n')
ind=json.loads(read(R/'out/independent.json'))
assert ind['assertions']==29 and ind['strict_margin_lower_bound']=='15/4'
assert ind['I']=='3/2' and ind['r']=='5/16' and ind['L']=='11/4'
report=read(R/'REPORT.md')
extra=('Independent reconstruction: code/independent.py evaluates all eight triangle characters by direct finite sums, without FWHT. '
'For epsilon=2^-64 at a saturated singleton, exact outward logarithm intervals certify '
'D(P||q)-D(Rstar||q)-(9/2)I in [3.78227921,3.78227922], strictly greater than 15/4 bits. '
'All 29 additional assertions PASS in '+str(ind['elapsed_seconds'])+' seconds. '
'FROZEN_TRIANGLE.json records the single-case domain before this check; out/independent.json is its receipt. '
'This is a separate self-reconstruction, not independent peer acceptance.\n\n')
if 'Independent reconstruction: code/independent.py' not in report:
 report=report.replace('## proof dependencies and changed downstream conclusions',extra+'## proof dependencies and changed downstream conclusions')
 write(R/'REPORT.md',report)
claim=json.loads(read(R/'CLAIMS.json'))[0]
assert hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
progress=json.loads(read(R/'PROGRESS.json'))
assert progress==json.loads(read(R/'PACKET_DELTA.json'))
protocol=json.loads(read(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')))
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert all('## '+field in report for field in protocol['required_per_run']['report_fields'])
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
assert len(read(R.parents[1]/'STATUS.md').splitlines())==2
receipts=json.loads(read(R/'out/RECEIPTS.json'))
receipts['final_verified_at_utc']=datetime.now(timezone.utc).isoformat()
receipts['independent_triangle']={'assertions':29,'margin_lower_bound':'15/4','peer_acceptance':False}
old=R.parent/'20261014T054454Z-account05-A014-overlap-beyond-worst-case-read/code/check.py'
receipts['source_dependencies']=[{'path':str(old),'sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'bytes':old.stat().st_size}]
receipts['files']=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='RECEIPTS.json':
  raw=p.read_bytes();assert len(raw)<20*1024*1024
  receipts['files'].append({'path':str(p.relative_to(R)),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)})
write(R/'out/RECEIPTS.json',json.dumps(receipts,indent=2)+'\n')
for item in receipts['files']:
 assert hashlib.sha256((R/item['path']).read_bytes()).hexdigest()==item['sha256']
print(json.dumps({'artifact_validation':'PASS','files':len(receipts['files']),'main_exact_assertions':395826,'direct_triangle_assertions':29,'protocol_keys':'PASS','remote_persistence':'UNVERIFIED','full_fei':'OPEN'}))
