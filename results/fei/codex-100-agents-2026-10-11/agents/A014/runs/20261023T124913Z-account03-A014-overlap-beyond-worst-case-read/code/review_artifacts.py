from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def read(p):return p.read_text(encoding='utf-8-sig')
def js(p):return json.loads(read(p))
def find(obj,key):
    if isinstance(obj,dict):
        if key in obj:return obj[key]
        values=obj.values()
    elif isinstance(obj,list):values=obj
    else:return None
    for val in values:
        found=find(val,key)
        if found is not None:return found
    return None
protocol=js(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
progress=js(R/'PROGRESS.json');assert set(progress)=={s.split(' (')[0] for s in find(protocol,'progress_fields')}
assert progress==js(R/'PACKET_DELTA.json') and progress['packet_ids']==['A014']
claim=js(R/'CLAIMS.json')[0];assert set(claim)==set(find(protocol,'claim_fields'))
assert claim['version']==8 and claim['review_records']==[]
assert hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
report=read(R/'REPORT.md')
for heading in find(protocol,'report_fields'):assert heading in report,heading
assert report.rstrip().split('\n\n')[-1].startswith('This stage moves C020')
assert 'all-relevant' in report and 'Full FEI remains OPEN.' in report
status=read(A/'STATUS.md').splitlines();assert len(status)==2 and status[0].startswith('STATE: ') and status[1].startswith('NEXT: ')
receipts=js(R/'out/RECEIPTS.json');paths=[row['path'] for row in receipts['files']];assert len(paths)==len(set(paths))
for row in receipts['files']:
    p=(R/row['path']).resolve();assert p.is_relative_to(R.resolve())
    assert p.stat().st_size==row['bytes']<20_000_000 and hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'],p
for row in receipts['rolling_files']:
    p=Path(row['path']);assert p.parent==A and hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256']
for name in ['check','independent','history','scalar']:
    out=js(R/f'out/{name}.json');assert out['assertions']>0 and out['elapsed_seconds']<300
assert len(js(R/'out/RUNNER_v3.json'))==4
assert js(R/'out/scalar.json')['log_cross_checks']==128
assert 'def binary_bounds' not in read(R/'code/check_v1.py') and 'def binary_bounds' in read(R/'code/check.py')
print(json.dumps({'schemas':'PASS','statement_hash':'PASS','receipt_hashes':'PASS','run_files':len(paths),'rolling_files':3,'report_readback':'PASS','peer_review':'PENDING','FEI':'OPEN'}))
