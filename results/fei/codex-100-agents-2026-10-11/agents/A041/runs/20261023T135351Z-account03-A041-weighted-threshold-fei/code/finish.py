"""Check saved bytes; record mandated checklist lifecycle outcomes without touching locks."""
from pathlib import Path
import hashlib,json,subprocess,sys
R=Path(__file__).resolve().parents[1]; O=R/'out'; A=R.parents[1]
def read(p):return Path(p).read_text(encoding='utf-8')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,x):Path(p).write_bytes((json.dumps(x,indent=2)+'\n').encode('utf-8'))
old=json.loads(read(O/'ARTIFACT_SHA256.json'))
assert all(sha(R/x['path'])==x['sha256'] for x in old)
claims=json.loads(read(R/'CLAIMS.json'));new=claims[-1]
assert hashlib.sha256(new['exact_statement'].encode('utf-8')).hexdigest()==new['statement_sha256']
assert sha(R/'PROOF.md')==new['proof_source']['sha256']
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len(read(A/'STATUS.md').splitlines())==2
report=read(R/'REPORT.md');assert report.splitlines()[-1].startswith('Universal bridge:')
srcs=json.loads(read(O/'SOURCE_RECEIPTS.json'))
immutable=[x for x in srcs if '/runs/' in x['path'].replace('\\','/')]
assert all(sha(x['path'])==x['sha256'] for x in immutable)
validation={'status':'PASS','old_manifest_files_verified':len(old),'claims':len(claims),'new_statement_sha256':new['statement_sha256'],'new_proof_sha256':sha(R/'PROOF.md'),'main_exact_assertions':json.loads(read(O/'CHECKS.json'))['assertions'],'protocol_copy_identical':True,'status_two_lines':True,'full_FEI':'OPEN','review':'A045 full scoped theorem independently accepted; new A041 theorem awaits independent review','publication':'Supervisor copy and downstream use unobserved'}
dump(O/'FINAL_VALIDATION.json',validation)
hook='task_checklist_hook.py'
receipts=[]
for task,result in [('T-20261023-523','A041 stage saved: sharp joint singleton envelope and exact carry tradeoff; A045 full scoped review HOLDS;41372 checks PASS;prime Jhi/FEI open.'),('T-20261023-387','Prior A041 stage completed and saved: adaptive complete-reference bounds and exact certificates; full FEI remained open; subsequent stages preserved.')]:
 p=subprocess.run([sys.executable,'-X','utf8',hook,'done',task,result],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,encoding='utf-8',check=False)
 receipts.append({'task_id':task,'action':'done','returncode':p.returncode,'output':p.stdout[-5000:]})
 dump(O/'TASK_CHECKLIST.json',receipts)
success=[x['task_id'] for x in receipts if x['returncode']==0]
failed=[x['task_id'] for x in receipts if x['returncode']!=0]
extra=' Checklist completion receipts: succeeded='+str(success)+'; failed='+str(failed)+'; see out/TASK_CHECKLIST.json. Shared locks were never modified.'
report=report.replace('completion attempts are recorded separately.','completion attempts are recorded separately.'+extra)
report=report.replace('The first pilot was repeated after replacing two hand-rational exclusion checks with direct physical spectrum checks; the mathematical domain was unchanged.','The pilot was repeated after replacing two hand-rational exclusions with direct physical spectrum checks; the mathematical domain was unchanged. Main additionally verifies direct full-reference KL against the independently composed terminal law.')
(R/'REPORT.md').write_bytes(report.encode('utf-8'))
progress=json.loads(read(R/'PROGRESS.json'))
progress['blockers'].append('Checklist completion receipt: succeeded='+str(success)+'; failed='+str(failed)+'. Mathematical artifact completion is independent of checklist/mirror status.')
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert all(p.stat().st_size<20_000_000 for p in R.rglob('*') if p.is_file())
manifest=[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(R.rglob('*')) if p.is_file() and p.name!='ARTIFACT_SHA256.json']
dump(O/'ARTIFACT_SHA256.json',manifest)
assert all(sha(R/x['path'])==x['sha256'] for x in manifest)
print(json.dumps({'status':'ARTIFACTS_VERIFIED','files':len(manifest),'main_assertions':validation['main_exact_assertions'],'checklist_done':success,'checklist_blocked':failed,'new_independent_review':'pending','running_research_jobs':0}))
