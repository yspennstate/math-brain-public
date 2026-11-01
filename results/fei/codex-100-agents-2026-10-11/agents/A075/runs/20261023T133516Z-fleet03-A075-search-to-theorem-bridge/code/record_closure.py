"""Preserve shared checklist failure without rerunning mathematical jobs."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parent.parent
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,o):p.write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
stamp=datetime.now(timezone.utc).isoformat()
failure={'task':'T-20261023-502','operation':'done','exit_code':1,'error':"RuntimeError('checklist lock held too long')",'mathematical_artifacts':'COMPLETE_AND_VERIFIED','coordination_closure':'BLOCKED_SHARED_LOCK','retry_or_shared_file_surgery':False,'recorded_at':stamp}
write(ROOT/'out/CHECKLIST_CLOSURE.json',failure)
p=ROOT/'REPORT.md';report=p.read_text(encoding='utf-8')
old='Supervisor copying/mirrors/downstream use remain unverified; no public proof claim is made.'
new=old+' The required checklist done helper for T-20261023-502 was invoked AFTER the artifacts and NEXT line were saved, but exited1 with RuntimeError(checklist lock held too long). Shared checklist closure is BLOCKED, not assumed done; out/CHECKLIST_CLOSURE.json preserves the failure. No shared-lock surgery or repeated calculation was attempted.'
assert old in report;report=report.replace(old,new);p.write_text(report,encoding='utf-8')
progress=read(ROOT/'PROGRESS.json');progress['blockers'].append('Required checklist closure T-20261023-502 blocked by shared lock; mathematical artifacts and NEXT are complete, shared completion not persisted.')
write(ROOT/'PROGRESS.json',progress);write(ROOT/'PACKET_DELTA.json',progress)
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{stamp}: Required checklist done T-20261023-502 failed exit1: checklist lock held too long. Artifact/STATUS/NEXT closure already verified; shared checklist closure not assumed. No job rerun or lock surgery.\n')
receipt=read(ROOT/'out/PERSISTENCE.json');receipt['saved_at']=stamp;receipt['checklist_closure']='BLOCKED_SHARED_LOCK';receipt['files']=[];receipt['rolling_files']=[]
for p in sorted(ROOT.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE.json':
  assert p.stat().st_size<20*1024*1024;receipt['files'].append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)})
for n in ['STATUS.md','WORKLOG.md','LEARNED.md']:receipt['rolling_files'].append({'path':n,'sha256':sha(AGENT/n)})
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
write(ROOT/'out/PERSISTENCE.json',receipt)
for p in receipt['files']:assert sha(ROOT/p['path'])==p['sha256']
print(json.dumps({'local_artifacts':'PASS','files':len(receipt['files']),'checklist_closure':'BLOCKED_SHARED_LOCK','own_jobs_remaining':'NONE','full_fei':'OPEN'}))
