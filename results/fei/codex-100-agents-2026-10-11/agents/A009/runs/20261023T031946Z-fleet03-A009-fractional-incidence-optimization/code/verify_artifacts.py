"""Read-only verification of finished local packet and persistence receipts."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
def read(p):return json.loads((R/p).read_text(encoding='utf-8'))
p=read('PROGRESS.json'); d=read('PACKET_DELTA.json')
expected={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(p)==expected and p==d and p['packet_ids']==['A009']
for c in read('CLAIMS.json'):
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    if c['claim_id'].startswith('A009-'):
        h=hashlib.sha256(json.dumps({'exact_statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
        assert h==c['statement_sha256']
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
report=(R/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:assert '# '+field in report
assert report.rstrip().split('\n\n')[-1].startswith('Universal bridge:')
receipts=read('out/RECEIPTS.json')['files']
for rec in receipts:
    target=R/rec['path']
    assert target.stat().st_size==rec['bytes']<20*1024*1024
    assert hashlib.sha256(target.read_bytes()).hexdigest()==rec['sha256']
actual={str(x.relative_to(R)) for x in R.rglob('*') if x.is_file() and x.name!='RECEIPTS.json'}
assert actual=={x['path'] for x in receipts}
f=read('out/full.json');assert f['status']=='PASS'
assert len(f['graphs'])==330 and len(f['fixtures'])==6 and len(f['obstruction'])==3
assert f['counts']['direct_exception_set']==336
print(json.dumps({'status':'VERIFIED','files':len(receipts),'full_checks':f['total_checks'],'schema':'EXACT','compatibility_copy':'IDENTICAL','hashes':'ALL_MATCH','rolling_status_lines':2}))
