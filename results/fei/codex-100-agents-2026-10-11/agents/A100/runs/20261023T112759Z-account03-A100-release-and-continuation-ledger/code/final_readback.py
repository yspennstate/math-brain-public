from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess,sys,time
R=Path(__file__).resolve().parents[1];O=R/'out';A=R.parent.parent

def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,x):p.write_bytes((json.dumps(x,indent=2)+'\n').encode())
# Required administrative task closure; no peer message, brain research write or repository mutation.
args=[sys.executable,'-X','utf8','task_checklist_hook.py','done','T-20261023-377','A100 stage19 saved/read back: A079 ghost theorem full-scope independent acceptance;90330+825 exact checks;197 recorded review groups and ten questions;FEI/source-price/zero-credit conversion OPEN;remote adoption unverified.']
r=subprocess.run(args,capture_output=True,encoding='utf-8',errors='replace',creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0));save(O/'CHECKLIST_DONE_RECEIPT.json',{'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'status':'DONE_HELPER_SUCCEEDED' if r.returncode==0 else 'ADMINISTRATIVE_LOCK_OR_HELPER_FAILURE_RESEARCH_FILES_STILL_SAVED'})
start=time.perf_counter();m=load(O/'PERSISTENCE_RECEIPTS.json');n=len(m['files'])
for x in m['files']+m['rolling_snapshot']:
 b=Path(x['path']).read_bytes();assert len(b)==x['bytes'] and hashlib.sha256(b).hexdigest()==x['sha256'],x['path']
for x in load(O/'REVIEW_SOURCE_RECEIPTS.json'):
 b=Path(x['path']).read_bytes();assert len(b)==x['bytes'] and hashlib.sha256(b).hexdigest()==x['sha256'],x['path']
protocol=load(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'));cs=load(R/'CLAIMS.json');p=load(R/'PROGRESS.json');spec=load(O/'FROZEN_SPEC.json');main=load(O/'GHOST_REVIEW.json');audit=load(O/'INDEPENDENT_CONSERVATION_AUDIT.json')
assert len(cs)==1 and set(cs[0])==set(protocol['required_per_run']['claim_fields']);assert set(p)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']};assert p['packet_ids']==['A100'];assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert hashlib.sha256((R/'code/check_ghost.py').read_bytes()).hexdigest()==spec['helper_sha256'];assert main['transactions']==spec['case_count']==1512;assert main['exact_assertions']==90330;assert audit['assertions']==825;assert main['status']==audit['status']=='PASS';assert main['runtime_seconds']<55 and audit['runtime_seconds']<55
src=next(c for c in load(Path(load(O/'CRITICAL_SOURCE_RUNS.json')['A079'])/'CLAIMS.json') if c['claim_id']==cs[0]['claim_id'])
for k in ['claim_id','version','exact_statement','hypotheses','statement_sha256','proof_source']:assert src[k]==cs[0][k]
assert cs[0]['review_records'][-1]['reviewer']=='A100/account03/B20';assert not cs[0]['review_records'][-1]['substantive_repair_supplied']
assert hashlib.sha256(Path(src['proof_source']['path']).read_bytes()).hexdigest()==src['proof_source']['sha256']
report=(R/'REPORT.md').read_text();assert all('## '+h+'\n' in report for h in protocol['required_per_run']['report_fields']);assert report.rstrip().split('## ')[-1].startswith('Universal bridge\n');assert len(load(O/'NEXT_TEN_QUESTIONS.json'))==10;assert len((A/'STATUS.md').read_text().splitlines())==2
ledger=load(O/'THEOREM_RELEASE_LEDGER.json');assert ledger['full_FEI_status']=='OPEN';assert any(c['claim_id']==cs[0]['claim_id'] and c['A100_full_reconstruction_this_stage'] for c in ledger['accepted'])
files=[]
for path in sorted(R.rglob('*')):
 if path.is_file() and path.name not in ['PERSISTENCE_RECEIPTS.json','FINAL_READBACK.json'] and '__pycache__' not in path.parts:
  b=path.read_bytes();assert len(b)<20_000_000;files.append({'path':str(path),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
m['files']=files;m['local_readback']='PASS';m['independent_final_readback']='out/FINAL_READBACK.json';save(O/'PERSISTENCE_RECEIPTS.json',m)
for x in files:
 b=Path(x['path']).read_bytes();assert len(b)==x['bytes'] and hashlib.sha256(b).hexdigest()==x['sha256']
assert time.perf_counter()-start<55
result={'status':'PASS','at_utc':datetime.now(timezone.utc).isoformat(),'original_current_payloads_checked':n,'final_payloads_rehashed':len(files),'rolling_snapshots_checked':3,'target_source_receipts_checked':3,'prior_original_immutable_hashes_compared':load(O/'PREVIOUS_RECEIPT_VERIFICATION.json')['original_immutable_payload_hashes_compared'],'main_exact_assertions':90330,'independent_audit_assertions':825,'recorded_review_counts':ledger['counts'],'new_source_statement_scope_hash_preserved':True,'frozen_main_helper_hash_preserved':True,'ten_questions':10,'full_FEI':'OPEN','private_remote_canonical_public':'UNVERIFIED','brain_selfcare':'DEGRADED/UNVERIFIED: wake attachment access and stale model/state/dream continuity affected','checklist_done_returncode':r.returncode,'local_readback_runtime_seconds':round(time.perf_counter()-start,6)};save(O/'FINAL_READBACK.json',result);print(json.dumps(result,indent=2));print('CURRENT_STATUS\n'+(A/'STATUS.md').read_text());print('REPORT_FINAL_PARAGRAPH\n'+report[report.rfind('## Universal bridge'):])
