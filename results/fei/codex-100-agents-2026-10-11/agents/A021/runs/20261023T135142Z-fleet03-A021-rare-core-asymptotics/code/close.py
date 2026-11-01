from pathlib import Path
import hashlib,json,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def read(p):return Path(p).read_text(encoding='utf-8')
def write(p,s):Path(p).write_text(s,encoding='utf-8',newline='')
def load(p):return json.loads(read(p))
def dump(p,o):write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
manifest=load(R/'out/PERSISTENCE.json')
for name,row in manifest['files'].items():assert sha(R/name)==row['sha256'],name
receipt={'at':now,'entry':'T-20261023-520','working':'Earlier command exit0, observed this stage.','done_command_exit':1,'done_command_output':"checklist: error: RuntimeError('checklist lock held too long')",'status':'CLOSURE_BLOCKED_BY_SHARED_CHECKLIST_LOCK','research_artifacts':'COMPLETE_LOCAL_EXTERNAL_REVIEW_PENDING','other_tasks_touched':False}
dump(R/'out/CHECKLIST_RECEIPT.json',receipt)
report=read(R/'REPORT.md')
report=report.replace('Current computations have completed; no research job is left running.',
 'Current computations have completed; no research job is left running. Closing checklist entry T-20261023-520 was attempted but returned exit1: shared checklist lock held too long. The research deliverable is saved; checklist closure remains blocked by that shared lock. No lock was removed and no other task was changed.')
write(R/'REPORT.md',report)
pr=load(R/'PROGRESS.json');pr['blockers'].append('Checklist T-20261023-520 done attempt exit1: shared checklist lock held too long; local research artifacts complete. Retry closure after the shared lock clears, without modifying other tasks.')
dump(R/'PROGRESS.json',pr);write(R/'PACKET_DELTA.json',read(R/'PROGRESS.json'))
status=read(A/'STATUS.md').splitlines();status[1]+=' Checklist T-20261023-520 closure blocked by shared lock; retry after it clears.';write(A/'STATUS.md','\n'.join(status)+'\n')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now} | Final persistence audit: all prior manifest hashes verified. Checklist T-20261023-520 closure attempted, exit1 (shared checklist lock held too long); saved exact receipt, left lock/other tasks untouched, NEXT records retry. Research complete locally, no research jobs running, external review and supervisor publication pending.\n')
manifest['generated_at']=now;manifest['files']={str(p.relative_to(R)):{'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(R.rglob('*')) if p.is_file() and '__pycache__' not in str(p) and p.name not in ('PERSISTENCE.json','FINAL_VALIDATION.json')};manifest['rolling']={str(A/n):sha(A/n) for n in ('STATUS.md','WORKLOG.md','LEARNED.md')};dump(R/'out/PERSISTENCE.json',manifest)
assert (R/'PACKET_DELTA.json').read_bytes()==(R/'PROGRESS.json').read_bytes()
c=load(R/'CLAIMS.json')[0]
assert c['proof_source']['sha256']==sha(R/'PROOF.md')
assert c['proof_source']['additional_proof']['sha256']==sha(R/'BALANCED_COROLLARY.md')
assert c['statement_sha256']==hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()
assert len(read(A/'STATUS.md').splitlines())==2
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
v=load(R/'out/FINAL_VALIDATION.json');v.update(at=now,prior_manifest_hashes_verified=True,checklist_closure='BLOCKED_SHARED_LOCK_RECEIPT_SAVED');dump(R/'out/FINAL_VALIDATION.json',v)
print(json.dumps({'status':'PASS_LOCAL_ARTIFACT_AUDIT','files':len(manifest['files']),'checklist':'CLOSURE_BLOCKED_SHARED_LOCK','research_jobs_left_running':False,'external_review':'PENDING','full_fei':'OPEN'}))
print(read(A/'STATUS.md'))
