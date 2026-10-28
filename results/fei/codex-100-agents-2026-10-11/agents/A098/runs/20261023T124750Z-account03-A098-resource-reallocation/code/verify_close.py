from pathlib import Path
import json,hashlib,subprocess,sys
from datetime import datetime,timezone
RUN=Path(__file__).resolve().parents[1];OWN=RUN.parents[1];OUT=RUN/'out'
def read(p):return p.read_text(encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
m=json.loads(read(OUT/'MANIFEST.json'))
assert all(sha(RUN/x['path'])==x['sha256'] for x in m['files'])
assert all(sha(Path(x['path']))==x['sha256'] for x in m['rolling'])
report=read(RUN/'REPORT.md');assert report.rsplit('\n#',1)[-1].startswith('# Universal bridge')
assert 'Universal FEI constant improvement is0' in report
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
claims=json.loads(read(RUN/'CLAIMS.json'))
assert len(claims)==2
for c in claims:assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
status=read(OWN/'STATUS.md');assert len(status.splitlines())==2 and status.splitlines()[1].startswith('NEXT: ')
# Close the checklist and persist the same current NEXT in one operation.
(OWN/'STATUS.md').write_text(status,encoding='utf-8')
hook=Path(r'task_checklist_hook.py')
result=subprocess.run([sys.executable,'-X','utf8',str(hook),'done','T-20261023-464','A098 stage20 saved/readback verified: two scoped source reviews,620 exact checks,14 local handoffs;FEI remains open.'],capture_output=True,text=True,encoding='utf-8',creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
blocked=result.returncode!=0 or 'lock held too long' in result.stdout+result.stderr
receipt={'at':datetime.now(timezone.utc).isoformat(),'task':'T-20261023-464','returncode':result.returncode,'stdout':result.stdout,'stderr':result.stderr,'closure':'BLOCKED_SHARED_CHECKLIST' if blocked else 'COMMAND_SUCCEEDED','owner_seen':'NOT_MARKED'}
save(OUT/'CHECKLIST_CLOSE.json',receipt)
readback={'verdict':'PASS','original_manifest_hashes_checked':len(m['files']),'rolling_hashes_checked':len(m['rolling']),'claim_statement_hashes':True,'packet_delta_identical':True,'report_final_universal_bridge':True,'status_two_lines':True,'checklist_closure':receipt['closure'],'remote_adoption':'UNVERIFIED'}
save(OUT/'READBACK.json',readback)
files=[p for p in RUN.rglob('*') if p.is_file() and p.name!='MANIFEST.json']
assert all(p.stat().st_size<20_000_000 for p in files)
m['files']=[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]
m['final_readback_at']=datetime.now(timezone.utc).isoformat()
save(OUT/'MANIFEST.json',m)
print(json.dumps(readback))
print(status)
print(report[report.index('## Universal bridge'):])
