from pathlib import Path
import json,hashlib,datetime
root=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
p=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
report=(root/'REPORT.md').read_text(encoding='utf-8')
for h in p['required_per_run']['report_fields']:assert '# '+h+'\n' in report
assert report.rstrip().split('\n')[-1].startswith('Universal bridge:')
progress=read(root/'PROGRESS.json');assert progress==read(root/'PACKET_DELTA.json')
assert set(progress)=={x.split(' (')[0] for x in p['required_per_run']['progress_fields']}
for c in read(root/'CLAIMS.json'):
    assert set(c)==set(p['required_per_run']['claim_fields'])
    assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
ledger=read(root/'out'/'MIXED_LEDGER.json');assert len(ledger)==194
assert sum(x['terminal'] for x in ledger)==100
assert read(root/'out'/'validation.json')['assertions']==28728
assert len((root.parents[1]/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
receipt={'saved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','schemas_exact':True,'claim_statement_hashes_rechecked':True,'packet_delta_equals_progress':True,'report_re_read':True,'rolling_status_two_lines':True,'mixed_states':194,'research_jobs_running':0,'independent_review':'V9_NEW_ANALYTIC_CLAUSES_PENDING','remote_adoption':'SUPERVISOR_OWNED_NOT_VERIFIED','files':[]}
for path in sorted(root.rglob('*')):
    if not path.is_file() or path.name=='PERSISTENCE_RECEIPTS.json' or '__pycache__' in str(path):continue
    data=path.read_bytes();assert len(data)<20_000_000
    receipt['files'].append({'path':str(path.relative_to(root)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
dest=root/'out'/'PERSISTENCE_RECEIPTS.json';dest.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
for item in read(dest)['files']:assert hashlib.sha256((root/item['path']).read_bytes()).hexdigest()==item['sha256']
print(json.dumps({'status':'FINAL_FILES_VERIFIED','files':len(receipt['files']),'assertions':28728,'mixed_states':194,'research_jobs_running':0}))
