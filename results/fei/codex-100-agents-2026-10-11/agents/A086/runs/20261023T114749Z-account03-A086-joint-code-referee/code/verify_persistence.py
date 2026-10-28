from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
# Scope the queue receipt to this run; shared-stream adoption was not verified.
old='cap of two new source-complete pending candidates respected'
new='two new claims pending in this run; global stream queue/adoption reconciliation unverified'
for p in (R/'REPORT.md',R/'code/finalize.py'):
 text=p.read_text(encoding='utf-8')
 if old in text:p.write_text(text.replace(old,new),encoding='utf-8')
pr=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
claims=read(R/'CLAIMS.json');progress=read(R/'PROGRESS.json')
assert all(set(c)==set(pr['required_per_run']['claim_fields']) for c in claims)
assert set(progress)=={x.split(' (')[0] for x in pr['required_per_run']['progress_fields']}
assert progress==read(R/'PACKET_DELTA.json')
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+s in report for s in pr['required_per_run']['report_fields'])
assert report.rstrip().split('\n\n')[-1].startswith('C024 history transfer')
assert report.rstrip().endswith('Full FEI remains OPEN.')
status=(A/'STATUS.md').read_text(encoding='utf-8').splitlines();assert len(status)==2 and status[0].startswith('STATE:') and status[1].startswith('NEXT:')
for item in read(R/'out/SOURCE_RECEIPTS.json')['files']:assert sha(Path(item['path']))==item['sha256']
paths=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']+[A/x for x in ['STATUS.md','WORKLOG.md','LEARNED.md']]
assert all(p.stat().st_size<20_000_000 for p in paths)
records=[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in paths]
(R/'out/PERSISTENCE_RECEIPTS.json').write_text(json.dumps({'files':records,'mirror_verified':False,'reread_verified':True},indent=2)+'\n',encoding='utf-8')
assert all(sha(Path(x['path']))==x['sha256'] for x in records)
print(json.dumps({'status':'FINAL_ARTIFACTS_REREAD_VERIFIED','files':len(records),'assertions':read(R/'out/VALIDATION_TOTALS.json')['completed_assertions'],'full_fei':'OPEN','external_review_pending':2}))
