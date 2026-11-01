from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];OWN=R.parents[1]
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,v):p.write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8',newline='')
msg='Shared checklist working and done updates BOTH failed: RuntimeError(checklist lock held too long). T-20261023-429 remains administratively OPEN; local research artifacts are COMPLETE_LOCAL. Supervisor must reconcile closure; no shared lock was altered.'
save(R/'out/CHECKLIST_BLOCKER.json',{'task_id':'T-20261023-429','working_update':'FAILED_SHARED_LOCK','done_update':'FAILED_SHARED_LOCK','exact_error':"RuntimeError('checklist lock held too long')",'local_artifacts':'COMPLETE_LOCAL_SCHEMA_HASH_READBACK_PASS','administrative_task_state':'NOT_CLOSED','next_owner':'supervisor/shared-checklist owner','action':'Reconcile closure when shared lock clears; do not rerun completed research'})
p=read(R/'PROGRESS.json');p['blockers']=[x for x in p['blockers'] if 'checklist' not in x.lower()]+[msg]
save(R/'PROGRESS.json',p);save(R/'PACKET_DELTA.json',p)
for name in ['REPORT.md','code/finalize.py']:
 f=R/name;t=f.read_text(encoding='utf-8');old='supervisor copying/mirror verification is pending.';assert old in t;t=t.replace(old,'supervisor copying/mirror verification is pending. '+msg);f.write_text(t,encoding='utf-8',newline='')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:f.write('\n'+datetime.datetime.now(datetime.timezone.utc).isoformat()+' '+msg+'\n')
lines=(OWN/'STATUS.md').read_text(encoding='utf-8').splitlines();assert len(lines)==2
lines[1]+=' Supervisor reconcile T-20261023-429 closure: shared lock blocked both updates.'
(OWN/'STATUS.md').write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
paths=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE.json'];assert all(p.stat().st_size<20_000_000 for p in paths)
receipt=read(R/'out/PERSISTENCE.json');receipt['artifacts']=[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in paths];receipt['rolling']=[{'path':str(OWN/n),'sha256':sha(OWN/n)} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']];receipt['checklist']='T-20261023-429 NOT_CLOSED_SHARED_LOCK'
save(R/'out/PERSISTENCE.json',receipt)
for item in read(R/'out/PERSISTENCE.json')['artifacts']:assert sha(R/item['path'])==item['sha256']
assert read(R/'PROGRESS.json')==read(R/'PACKET_DELTA.json')
print(json.dumps({'local_artifacts':'COMPLETE_LOCAL_READBACK_PASS','checklist':'NOT_CLOSED_SHARED_LOCK','files':len(paths),'research_jobs_remaining':0,'full_FEI':'OPEN'}))
