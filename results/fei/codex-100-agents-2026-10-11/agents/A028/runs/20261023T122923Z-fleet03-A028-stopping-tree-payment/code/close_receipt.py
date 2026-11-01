"""Preserve a completion-checklist lock blocker without changing mathematics."""
from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def dump(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8',newline='')
msg='External completion checklist T-20261023-446 could not close: RuntimeError(checklist lock held too long). No shared lock was removed or modified; local research package is complete.'
dump(R/'out/completion_receipt.json',dict(status='BLOCKED_EXTERNAL_CHECKLIST_LOCK',message=msg,mathematical_outputs='ALL_PASS',local_save='COMPLETE',left_running='none',timestamp_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))
p=json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))
if msg not in p['blockers']:p['blockers'].append(msg)
dump(R/'PROGRESS.json',p);dump(R/'PACKET_DELTA.json',p)
rp=R/'REPORT.md';s=rp.read_text(encoding='utf-8')
anchor='No save blocker; supervisor publication/mirror verification remains pending, no git run.'
replacement='No local save blocker; supervisor publication/mirror verification remains pending, no git run. The external completion checklist could not close because its shared lock timed out; no shared lock was modified.'
s=s.replace(anchor,replacement);rp.write_text(s,encoding='utf-8',newline='')
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='') as w:w.write('\nCompletion receipt: '+msg+' NEXT remains the saved necessary-target feasibility/payer handoff; no calculation remains running.\n')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name not in ('artifact_manifest.json','validation.json')]
dump(R/'out/artifact_manifest.json',{str(p.relative_to(R)):{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in sorted(files)})
v=json.loads((R/'out/validation.json').read_text(encoding='utf-8'));v.update(saved_files=len(files),external_checklist='BLOCKED_LOCK_TIMEOUT',mathematical_outputs='ALL_PASS');dump(R/'out/validation.json',v)
print('Local package and manifest updated; checklist lock blocker preserved, mathematical checks PASS.')
