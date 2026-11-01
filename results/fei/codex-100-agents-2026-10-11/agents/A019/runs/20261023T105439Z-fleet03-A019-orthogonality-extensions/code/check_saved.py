from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def read(p):
 with p.open('r',encoding='utf-8-sig',newline='') as f:return f.read()
def write(p,s):
 with p.open('w',encoding='utf-8',newline='') as f:f.write(s)
p=A/'LEARNED.md';s=read(p)
s=s.replace('NEXT must use actual original event influence, not renew source.','NEXT must audit whether any original influence is unallocated after B (which already contains J/2) and all terminal obligations; no additional query credit is certified.')
write(p,s)
p=A/'WORKLOG.md';s=read(p)
s=s.replace('NEXT: actual unused event-influence allocation.','NEXT: audit influence ownership first; B already contains J/2, and no additional unused credit is certified.')
write(p,s)
receipt=R/'out/PERSISTENCE_RECEIPTS.json';d=json.loads(read(receipt))
for item in d['files']:
 p=R/item['path'];assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'],str(p)
for p in R.rglob('*.json'):json.loads(read(p))
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
state=read(A/'STATUS.md');assert len(state.splitlines())==2
report=read(R/'REPORT.md').replace('\r\n','\n');assert report.rstrip().split('\n\n')[-1].startswith('This stage moves C024')
assert '33/128' in report and '16384' in report and '31689' in report
assert 'no additional unallocated credit is certified' in report
# Include this final readback script itself; all earlier receipts were checked first.
files=[p for p in R.rglob('*') if p.is_file() and p!=receipt]
assert all(p.stat().st_size<20_000_000 for p in files)
d['files']=[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(files)]
d['final_readback']='PASS; complete file hashes checked before manifest refresh; own rolling NEXT corrected in place to require influence ownership audit'
write(receipt,json.dumps(d,indent=2)+'\n')
print(state)
print(report[:1000])
print(report[report.rindex('## Universal bridge'):])
print(json.dumps({'status':'PASS','nonpilot_assertions':d['nonpilot_assertions'],'local_files':len(files),'new_independent_reviews':'PENDING','remote_mirror':'UNVERIFIED','full_fei':'OPEN','running_jobs':0}))
