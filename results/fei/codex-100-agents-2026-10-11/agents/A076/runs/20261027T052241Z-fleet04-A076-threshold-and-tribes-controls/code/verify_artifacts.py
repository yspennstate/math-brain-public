"""Read-only protocol schema, hash and persisted-surface audit."""
from pathlib import Path
import json, hashlib
R=Path(__file__).resolve().parents[1]
P=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
def read(n):return (R/n).read_text(encoding='utf-8')
progress=json.loads(read('PROGRESS.json'));claims=json.loads(read('CLAIMS.json'))
fields=P['required_per_run']
expected={x.split(' (')[0] for x in fields['progress_fields']}
assert set(progress)==expected,(set(progress)^expected)
assert read('PROGRESS.json')==read('PACKET_DELTA.json')
for c in claims:
    assert set(c)==set(fields['claim_fields'])
    assert hashlib.sha256(c['exact_statement'].encode()).hexdigest()==c['statement_sha256']
v=json.loads(read('out/VALIDATION.json'))
assert v['status']=='PASS' and v['cases']==2832 and v['exact_assertions']==19918
assert v['script_sha256']==hashlib.sha256((R/'code/check_activation.py').read_bytes()).hexdigest()
assert len(v['bent_grouped_cases'])==7
assert len((R.parents[1]/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert read('REPORT.md').rstrip().split('\n')[-1].startswith('This stage moves C019/C024')
assert 'RUNTIME_UNVERIFIED' in read('REPORT.md')
for f in json.loads(read('out/MANIFEST.json')):
    p=R/f['path'];assert hashlib.sha256(p.read_bytes()).hexdigest()==f['sha256'],str(p)
out={'status':'PASS','protocol_fields':'exact','files':'persisted and hash checked','full_fei':'OPEN','independent_review':'PENDING'}
(R/'out/ARTIFACT_AUDIT.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
