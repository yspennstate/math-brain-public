"""Re-read final human-facing report and exact schemas; refresh local receipts."""
from pathlib import Path
import json,hashlib,datetime
root=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
protocol=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
report=(root/'REPORT.md').read_text(encoding='utf-8')
for heading in protocol['required_per_run']['report_fields']:assert '# '+heading+'\n' in report
assert report.rstrip().split('\n')[-1].startswith('Universal bridge:')
assert read(root/'PROGRESS.json')==read(root/'PACKET_DELTA.json')
assert set(read(root/'PROGRESS.json'))=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
for claim in read(root/'CLAIMS.json'):
    assert set(claim)==set(protocol['required_per_run']['claim_fields'])
    assert hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
ledger=read(root/'out'/'MIXED_LEDGER.json')
assert len(ledger)==286 and sum(x['terminal'] for x in ledger)==146
assert read(root/'out'/'validation.json')['assertions']==12792
assert len((root.parents[1]/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
receipt_path=root/'out'/'PERSISTENCE_RECEIPTS.json'
receipt=read(receipt_path);receipt['saved_at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();receipt['final_report_re_read']=True;receipt['files']=[]
for path in sorted(root.rglob('*')):
    if not path.is_file() or path==receipt_path or '__pycache__' in str(path):continue
    data=path.read_bytes();assert len(data)<20_000_000
    receipt['files'].append({'path':str(path.relative_to(root)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
receipt_path.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
for item in read(receipt_path)['files']:
    assert hashlib.sha256((root/item['path']).read_bytes()).hexdigest()==item['sha256']
print(json.dumps({'status':'FINAL_FILES_RE_READ_AND_VERIFIED','files':len(receipt['files']),'mixed_states':len(ledger),'assertions':12792,'report_complete':True,'research_jobs_running':0}))
