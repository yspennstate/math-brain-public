from pathlib import Path
import json,hashlib
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];O=R/'out';A=R.parent.parent
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
protocol=load(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
progress=load(R/'PROGRESS.json');claims=load(R/'CLAIMS.json')
fields=set(protocol['required_per_run']['progress_fields']);fields.remove('packet_ids (one primary ID, for compatibility)');fields.add('packet_ids')
assert set(progress)==fields
assert all(set(c)==set(protocol['required_per_run']['claim_fields']) for c in claims)
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+h in report for h in protocol['required_per_run']['report_fields'])
assert report.rsplit('## ',1)[1].startswith('Universal bridge\n')
receipts=load(O/'REVIEW_SOURCE_RECEIPTS.json')['files']
for row in receipts:assert sha(Path(row['path']))==row['sha256']
source=next(c for c in load(Path(receipts[0]['path'])) if c['claim_id']==claims[0]['claim_id'])
for key in ['claim_id','version','exact_statement','hypotheses','statement_sha256','contributors','proof_dependencies']:
 assert claims[0][key]==source[key],key
assert hashlib.sha256(claims[0]['exact_statement'].encode('utf-8')).hexdigest()==claims[0]['statement_sha256']
spec=load(O/'FROZEN_SPEC.json');assert sha(R/'code/check_account.py')==spec['checker_sha256']
asp=load(O/'FROZEN_AUDIT_SPEC.json');assert sha(R/'code/audit_literal.py')==asp['code_sha256']
v=load(O/'ACCOUNT_REVIEW.json');au=load(O/'INDEPENDENT_AUDIT.json')
assert v['checks']==39961 and v['transactions']==1112 and au['checks']==73750
assert all(row['matches'] for row in load(O/'PREVIOUS_ORIGINAL_RECEIPT_VERIFIED.json')['files'])
ledger=load(O/'THEOREM_RELEASE_LEDGER.json');assert any(c['claim_id']==claims[0]['claim_id'] for c in ledger['accepted'])
assert not any(c['claim_id']=='A011-PADDING-FRESH-RESET-SAME-SOURCE-BANK' and str(c['version'])=='5' for c in ledger['accepted'])
assert len(load(O/'NEXT_TEN_QUESTIONS.json'))==10
status=(A/'STATUS.md').read_text(encoding='utf-8').splitlines();assert len(status)==2 and status[0].startswith('STATE:') and status[1].startswith('NEXT:')
index=['# A100 release index: full FEI OPEN','',f"Recorded statement/version review groups: {ledger['counts']}. These are local evidence classifications, not fresh blanket theorem proofs.",'','Fresh independently reconstructed result: A094-A011-V5-PHYSICAL-QUERY-KL-LEDGER-GAP@1. Analytic proof with exact certificates; no Lean certification.','', 'A011v5 terminal-functional inequality is unrefuted. Its identification with full physical root-plus-reset payment omits query KL contractions; full-policy payment remains conditional.','', 'Private remote mirrors, canonical adoption, downstream use and public release: UNVERIFIED. Local save receipts are in out/PERSISTENCE_RECEIPTS.json.','', 'The complete source/version/hypothesis/review records are in out/THEOREM_RELEASE_LEDGER.json. Failed routes: out/FAILED_ROUTE_ARCHIVE.json. Next ten exact questions: CONTINUATION.md.','', '| Recorded accepted statement | Version | Source receipts |','|---|---:|---:|']
index += [f"| {c['claim_id']} | {c['version']} | {len(c['sources'])} |" for c in sorted(ledger['accepted'],key=lambda x:(x['claim_id'],str(x['version'])))]
(R/'RELEASE_INDEX.md').write_text('\n'.join(index)+'\n',encoding='utf-8',newline='\n')
progress['deliverable_status']='COMPLETE_LOCAL_BYTE_READBACK_VERIFIED';save(R/'PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
save(O/'SCHEMA_VALIDATION.json',{'status':'PASS','report_fields_exact':True,'progress_fields_exact':True,'claim_fields_exact':True,'packet_delta_byte_identical':True,'target_statement_hypotheses_hash_unchanged':True,'frozen_checkers_unchanged':True,'A011v5_not_fully_accepted':True,'ten_questions':10,'primary_checks':v['checks'],'independent_literal_checks':au['checks'],'full_FEI':'OPEN'})
files=[]
for p in sorted(R.rglob('*')):
 if not p.is_file() or '__pycache__' in p.parts or p.name in ['PERSISTENCE_RECEIPTS.json','FINAL_READBACK.json']:continue
 assert p.stat().st_size<20_000_000,p
 files.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
rolling=[{'path':str(A/n),'bytes':(A/n).stat().st_size,'sha256':sha(A/n)} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]
save(O/'PERSISTENCE_RECEIPTS.json',{'saved_utc':datetime.now(timezone.utc).isoformat(),'files':files,'rolling_snapshot':rolling,'local_save':'BYTE_READBACK_PASS','remote_mirror':'UNVERIFIED','public_release':'UNVERIFIED','full_FEI':'OPEN'})
for row in load(O/'PERSISTENCE_RECEIPTS.json')['files']:assert sha(Path(row['path']))==row['sha256']
for row in rolling:assert sha(Path(row['path']))==row['sha256']
save(O/'FINAL_READBACK.json',{'status':'PASS','payloads_rehashed':len(files),'rolling_snapshots':len(rolling),'maximum_file_bytes':max(x['bytes'] for x in files),'formal_target':'UNVERIFIED','exact_schema_and_source_invariance':True,'remote_or_public_receipts':'NONE_OBSERVED','full_FEI':'OPEN'})
print(json.dumps(load(O/'FINAL_READBACK.json')))
