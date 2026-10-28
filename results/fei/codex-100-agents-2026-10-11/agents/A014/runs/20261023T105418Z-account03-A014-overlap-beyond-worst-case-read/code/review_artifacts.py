from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def read(p):return p.read_text(encoding='utf-8-sig')
def js(p):return json.loads(read(p))
protocol=js(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
def find(obj,key):
    if isinstance(obj,dict):
        if key in obj:return obj[key]
        for v in obj.values():
            found=find(v,key)
            if found is not None:return found
    elif isinstance(obj,list):
        for v in obj:
            found=find(v,key)
            if found is not None:return found
    return None
progress=js(R/'PROGRESS.json');claims=js(R/'CLAIMS.json');report=read(R/'REPORT.md');proof=read(R/'DERIVATION.md')
expected={s.split(' (')[0] for s in find(protocol,'progress_fields')}
assert set(progress)==expected,(set(progress)-expected,expected-set(progress))
assert progress==js(R/'PACKET_DELTA.json') and progress['packet_ids']==['A014']
for claim in claims:
    assert set(claim)==set(find(protocol,'claim_fields'))
    assert hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
    assert claim['version']==7 and claim['review_records']==[]
for heading in find(protocol,'report_fields'):
    assert heading in report,heading
assert report.rstrip().split('\n\n')[-1].startswith('This stage moves C020')
assert '## Universal bridge' in report and 'Full FEI remains OPEN.' in proof
status=read(A/'STATUS.md').splitlines();assert len(status)==2 and status[0].startswith('STATE: ') and status[1].startswith('NEXT: ')
receipts=js(R/'out/RECEIPTS.json');paths=[r['path'] for r in receipts['files']]
assert len(paths)==len(set(paths))
for row in receipts['files']:
    p=(R/row['path']).resolve();assert p.is_relative_to(R.resolve())
    assert p.stat().st_size==row['bytes']<20_000_000
    assert hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'],p
for row in receipts['rolling_files']:
    p=Path(row['path']);assert p.parent==A and hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256']
for name in ['check','scalar','independent','obstruction']:
    out=js(R/f'out/{name}.json');assert out['assertions']>0 and out['elapsed_seconds']<(60 if name=='obstruction' else 300)
print(json.dumps({'schemas':'PASS','all_receipt_hashes':'PASS','run_files':len(paths),'rolling_files':len(receipts['rolling_files']),'report_readback':'PASS','statement_hash':'PASS','review':'PENDING','FEI':'OPEN'}))
