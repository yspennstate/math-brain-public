from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
receipt=[]
for p in sorted(ROOT.rglob('*')):
 if p.is_file() and p.name!='artifact_receipts.json':
  data=p.read_bytes();assert len(data)<20*1024*1024
  receipt.append(dict(path=str(p),bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
 p=AGENT/name;data=p.read_bytes();receipt.append(dict(path=str(p),bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
progress=json.loads((ROOT/'PROGRESS.json').read_text(encoding='utf-8'))
assert progress['packet_ids']==['A035']
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+h in report for h in protocol['required_per_run']['report_fields'])
assert '**Universal bridge:**' in report.splitlines()[-1]
(ROOT/'out'/'artifact_receipts.json').write_text(json.dumps(dict(local_only=True,independent_review='pending',external_mirror='not_verified',artifacts=receipt),indent=2),encoding='utf-8')
print('Local receipts:',len(receipt),'files; report headings, rolling status, size limits and primary packet checked.')
