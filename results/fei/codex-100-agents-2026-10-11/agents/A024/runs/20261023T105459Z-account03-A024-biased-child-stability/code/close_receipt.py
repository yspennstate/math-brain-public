"""Record a failed shared-checklist closure without touching that shared lock."""
from pathlib import Path
import json,hashlib,datetime
run=Path(__file__).resolve().parents[1];home=run.parents[1]
def read(p):return p.read_bytes().decode('utf-8')
def write(p,s):p.write_bytes(s.encode('utf-8'))
def js(p,v):write(p,json.dumps(v,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
note=('Checklist closure blocked by shared lock: T-20261023-183 and '
      'T-20261023-339 timed out; serial retry of current T-20261023-339 also '
      'timed out. No shared lock altered.')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
# Inspect the actual text and exact insertion anchor before any mutation.
report=read(run/'REPORT.md');anchor='\n\n**Universal bridge**:'
assert report.count(anchor)==1 and '\r' not in report
state=read(home/'STATUS.md').splitlines();assert len(state)==2
notes=json.loads(read(run/'out/EXECUTION_NOTES.json'))
progress=json.loads(read(run/'PROGRESS.json'))
assert progress==json.loads(read(run/'PACKET_DELTA.json'))
notes['checklist_closure']={'status':'BLOCKED_SHARED_LOCK','attempts':3,
 'current_task':'T-20261023-339','detail':note}
notes['local_receipt_recovery']='Inline mutation rejected before execution by verbatim-surgery acknowledgement gate; replaced by this file-based byte-preserving writer with checked anchor.'
if note not in progress['blockers']:progress['blockers'].append(note)
if 'Lifecycle receipt: '+note not in report:
 report=report.replace(anchor,'\n\nLifecycle receipt: '+note+
  ' The research package is complete and locally verified; checklist metadata may remain open.'+anchor)
if 'Checklist closure blocked by shared lock.' not in state[0]:
 state[0]+=' Checklist closure blocked by shared lock.'
worklog=read(home/'WORKLOG.md')
marker='Stage19 lifecycle: '+note
if marker not in worklog:
 worklog+='\n'+stamp+' | '+marker+' Research artifacts and mathematical NEXT unchanged; no process left running.\n'
js(run/'out/EXECUTION_NOTES.json',notes)
js(run/'PROGRESS.json',progress);js(run/'PACKET_DELTA.json',progress)
write(run/'REPORT.md',report);write(home/'STATUS.md','\n'.join(state)+'\n')
write(home/'WORKLOG.md',worklog)
receipt=json.loads(read(run/'out/FINAL_RECEIPT.json'))
receipt['time_utc']=stamp;receipt['checklist_closure']='BLOCKED_SHARED_LOCK'
files=sorted(p for p in run.rglob('*') if p.is_file() and p.name!='FINAL_RECEIPT.json')
receipt['files']=[{'path':str(p.relative_to(run)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]
receipt['rolling_files']=[{'path':str(home/n),'sha256':sha(home/n)} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]
js(run/'out/FINAL_RECEIPT.json',receipt)
# Read the persisted receipt again; verify actual artifact bytes, not pre-write data.
saved=json.loads(read(run/'out/FINAL_RECEIPT.json'))
assert all(sha(run/x['path'])==x['sha256'] for x in saved['files'])
assert all(sha(Path(x['path']))==x['sha256'] for x in saved['rolling_files'])
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert len(read(home/'STATUS.md').splitlines())==2
assert read(run/'REPORT.md').count(anchor)==1
print(json.dumps({'status':'PASS_LOCAL_READBACK','run_hashes':len(saved['files']),
 'rolling_hashes':len(saved['rolling_files']),'main_exact_assertions':saved['main_exact_assertions'],
 'checklist':'BLOCKED_SHARED_LOCK','left_running':[]}))
print(read(home/'STATUS.md'))
