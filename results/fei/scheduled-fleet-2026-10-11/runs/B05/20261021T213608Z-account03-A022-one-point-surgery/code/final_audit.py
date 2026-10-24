"""Final artifact reconciliation; does not rerun mathematical searches."""
from pathlib import Path
import json, hashlib, datetime
root=Path(__file__).resolve().parents[1]; agent=root.parents[1]
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def save(p,o): p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=read(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
c=read(root/'CLAIMS.json'); p=read(root/'PROGRESS.json')
for name in ['ENDPOINT_SPEC.json','code/check_endpoints.py','out/endpoint_checks.json','out/source_excerpts.txt','code/final_audit.py']:
    if name not in p['source_artifacts']: p['source_artifacts'].append(name)
c[0]['proof_source']['validation']=['out/pilot.json','out/exact_checks.json','out/bank_checks.json','out/endpoint_checks.json','out/lean_check.txt']
for item in c:
    assert set(item)==set(protocol['required_per_run']['claim_fields'])
    assert item['statement_sha256']==hashlib.sha256(item['exact_statement'].encode('utf-8')).hexdigest()
assert set(p)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
save(root/'CLAIMS.json',c); save(root/'PROGRESS.json',p); save(root/'PACKET_DELTA.json',p)
assert (root/'PROGRESS.json').read_bytes()==(root/'PACKET_DELTA.json').read_bytes()
results=[read(root/'out'/n) for n in ['pilot.json','exact_checks.json','bank_checks.json','endpoint_checks.json']]
assert all(r['status']=='PASS' for r in results)
total=sum(r.get('exact_assertions',r.get('checks',r.get('assertions',0))) for r in results)
assert total==141899
report=(root/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']: assert field.lower() in report.lower()
assert report.rfind('Universal bridge')>report.rfind('Actual persistence')
leanraw=(root/'out/lean_check.txt').read_bytes()
lean=leanraw.decode('utf-16' if leanraw.startswith((b'\xff\xfe',b'\xfe\xff')) else 'utf-8')
assert 'RUNTIME_UNVERIFIED' in lean
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+datetime.datetime.now(datetime.timezone.utc).isoformat()+' final validation: 141899 exact assertions total PASS, including24 full-support/zero-seed-reference endpoint cases and362 bank checks. Lean attempt RUNTIME_UNVERIFIED123.5s (exceeded follow-up60s target), no formal certification or retry. Protocol field sets and statement hashes checked. Independent review/mirror unverified.\n')
receipt={'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'schema_fields':'PASS',
 'statement_hashes':'PASS','progress_delta_identical':True,'exact_assertions':total,
 'mathematical_rung':'analytic proof; exact author verification; independent review pending',
 'formal_check':'RUNTIME_UNVERIFIED after123.5s; no Lean certification',
 'external_mirror':'NOT_VERIFIED','independent_review':'PENDING','files':[]}
for file in sorted(root.rglob('*')):
    if file.is_file() and file.name!='persistence.json':
        assert file.stat().st_size<20*1024*1024
        receipt['files'].append({'path':str(file.relative_to(root)),'bytes':file.stat().st_size,
                                'sha256':hashlib.sha256(file.read_bytes()).hexdigest()})
save(root/'out/persistence.json',receipt)
print(json.dumps({k:v for k,v in receipt.items() if k!='files'}))
