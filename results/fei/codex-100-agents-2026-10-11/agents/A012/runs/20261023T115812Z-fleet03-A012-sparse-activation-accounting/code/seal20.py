from pathlib import Path
from hashlib import sha256
import subprocess,sys,json,time
R=Path(__file__).resolve().parents[1]
checklist='~/<private-repo>/12_cognitive_architecture/task_checklist/checklist.py'
count=json.loads((R/'out/EXACT_RESULTS.json').read_text(encoding='utf-8'))['assertions_final_outputs_once']
cmd=[sys.executable,'-X','utf8',checklist,'done','T-20261023-410',f'A012 stage20 saved: paid partial-profile second query with FULL conversion, >1/128 bit;{count} checks; third-query flat-booking floor<-1/16;FEI open']
receipt={'task_id':'T-20261023-410','command':cmd,'working_update':'FAILED earlier: checklist lock held too long','remote_mirror':'UNOBSERVED'}
try:
 v=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=45,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
 receipt.update(returncode=v.returncode,stdout=v.stdout,stderr=v.stderr)
except subprocess.TimeoutExpired as e:
 receipt.update(returncode=None,stdout=str(e.stdout or ''),stderr='Completion timed out45s; only this own command child ended by subprocess timeout.')
def write(p,x):p.write_bytes((json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode('utf-8'))
write(R/'out/CHECKLIST_RECEIPT.json',receipt)
ok=receipt['returncode']==0
line=('Checklist T-20261023-410 completion exited0; working update had failed with shared lock.' if ok else 'Checklist T-20261023-410 completion remains operationally BLOCKED: '+receipt['stderr'].strip()+'; local mathematical artifacts are complete.')
report=R/'REPORT.md'
with report.open('r',encoding='utf-8',newline='') as f:s=f.read()
s=s.replace('Checklist working T-20261023-410 failed with a shared lock; the final attempt receipt will be saved separately.',line+' Exact command/output is in out/CHECKLIST_RECEIPT.json.')
with report.open('w',encoding='utf-8',newline='') as f:f.write(s)
p=json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))
p['blockers']=[x for x in p['blockers'] if not x.startswith('checklist T-20261023-410')]
if not ok:p['blockers'].append(line)
write(R/'PROGRESS.json',p);write(R/'PACKET_DELTA.json',p)
for name in ('WORKLOG.md','LEARNED.md'):
 with (R.parents[1]/name).open('a',encoding='utf-8',newline='') as f:f.write('\nStage20 final persistence: '+line+' Supervisor remote mirror remains unobserved.\n')
proto=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))['required_per_run']
c=json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'))
assert set(c[0])==set(proto['claim_fields'])
assert sha256(c[0]['exact_statement'].encode()).hexdigest()==c[0]['statement_sha256']
assert set(p)=={x.split(' (')[0] for x in proto['progress_fields']}
assert p==json.loads((R/'PACKET_DELTA.json').read_text(encoding='utf-8'))
assert len((R.parents[1]/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert s.rstrip().splitlines()[-1].startswith('This moves C024')
assert all(x.stat().st_size<20_000_000 for x in R.rglob('*') if x.is_file())
out={'status':'PASS','protocol_keys':True,'statement_sha256':c[0]['statement_sha256'],'assertions_final_outputs_once':count,'files':[{'path':str(x.relative_to(R)),'bytes':x.stat().st_size,'sha256':sha256(x.read_bytes()).hexdigest()} for x in sorted(R.rglob('*')) if x.is_file() and x.name!='FINAL_VALIDATION.json'],'independent_agent_v8_review':'PENDING','mirror':'UNOBSERVED','checklist_completion_ok':ok}
write(R/'out/FINAL_VALIDATION.json',out)
print(json.dumps({'status':'PASS','sealed_files':len(out['files']),'checklist_done':ok,'receipt':line}))
