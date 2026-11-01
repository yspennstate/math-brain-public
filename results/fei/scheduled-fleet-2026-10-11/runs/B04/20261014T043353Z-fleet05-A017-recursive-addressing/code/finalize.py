"""Persist and audit A017 stage5; writes confined to this agent."""
from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1];old=R.parent/'20261014T014813Z-fleet05-A017-recursive-addressing'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
proto=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
P=json.loads(proto.read_text(encoding='utf-8-sig'))
claim=json.loads((old/'CLAIMS.json').read_text(encoding='utf8'))[0]
prior={k:claim[k] for k in ['claim_id','version','statement_sha256']}
claim['version']=3
claim['exact_statement']+=' Further extension: For every quadratic q, linear M and E of at most seven vertices in one M-fiber, the adaptive physical policy of PROOF.md sections2-3 queries a >=3/16 polar row at five-control seven-edit nodes when available, otherwise stops at the exactly proved rank-two radical-coset-minus-one collapse. It has zero localized K4 bad-boundary bill, retains all phase terminals and exactly one weighted data influence, and proves H(F)<=(4+2/ln2)(I(F)-1). For E of at most eight vertices in one M-fiber, the same policy uses the even pivotal-edge parity certificate at five-control eight-edit nodes; its bad bill remains zero and complete terminal payment proves H(F)<=7(I(F)-1). The collapse is an equality in original physical coordinates to a signed character times a one-point defect, with character supported on zero polar rows. The previously named fixed-order seven-edit obstruction is preserved.'
claim['hypotheses'].append('New universal seven/eight-edit conclusions use the adaptive policy and paid algebraic stopping terminals; they do not claim every polar pivot is good or cover arbitrary nine-edit nodes.')
claim['statement_sha256']=hashlib.sha256(json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
claim['proof_source']={'new_proof':'PROOF.md','new_proof_sha256':sha(R/'PROOF.md'),'inherited_proof':'INHERITED_PROOF.md','inherited_sha256':sha(R/'INHERITED_PROOF.md'),'inherited_JS_proof':'DERIVATION.md','JS_sha256':sha(R/'DERIVATION.md'),'certificates':['out/collapse_certificate.json','out/CRITICAL_CERTIFICATE.json','out/TERNARY_CERTIFICATE.json','out/tree8_validation.json','out/SEVEN_EDIT_FIXTURE.json']}
claim['proof_dependencies']=[dict(prior,scope='Exact signed ledgers, generic critical certificates, sparse/dense terminal payment, complete JS proof; original source proofs reproduced.',acceptance='Author-proved; full-chain independent review pending.')]
claim['review_records']=[];claim['supersedes']=[{'claim_id':prior['claim_id'],'version':2}];claim['first_unproved_line']=None
save(R/'CLAIMS.json',[claim])
progress=json.loads((old/'PROGRESS.json').read_text(encoding='utf8'))
progress.update(run_id=R.name,attempt_id='A017-stage5-physical-coset-collapse',method='Resume saved derivation; exact all-weak rank-two collapse, parity certificate, retained-terminal adaptive tree.',mathematical_delta='Universal seven-edit zero K4 bill and H<=(4+2/ln2)(I-1); eight-edit zero bill and H<=7(I-1); exact13120 physical collapse cases and442 integration roots. Full FEI open.',claim_versions_used=[prior],claims_created_or_changed=[{k:claim[k] for k in ['claim_id','version','statement_sha256']}],source_artifacts=['PROOF.md','INHERITED_PROOF.md','DERIVATION.md','NEXT_DERIVATION.md','out/collapse_certificate.json','out/tree8_validation.json','out/CRITICAL_CERTIFICATE.json','out/TERNARY_CERTIFICATE.json','out/SEVEN_EDIT_FIXTURE.json','out/SOURCE_RECEIPTS.json'],next_action='A091/A090 full-chain review; reconstruct signed nine-edit rank-two mask deflation, then resolve rank-four five-control good-pivot or single-terminal-reserve policy.',blockers=['No universal rank-four nine-edit policy or point-count-independent terminal representation proved.','Full-chain independent review and supervisor/mirror adoption pending.'])
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
sources=[proto,Path('~/brain_workers/FEI100_20261011/BOARD.md'),Path('~/brain_workers/FEI100_20261011/claude/B04/STREAM_NOTES.md'),old/'NEXT_DERIVATION.md',old/'PROOF.md',old/'DERIVATION.md',old/'CLAIMS.json',old/'code/validate6.py',R.parent/'20261011T234546Z-fleet05-A017-recursive-addressing/code/check.py',Path('~/brain_workers/FEI100_20261011/agents/A019/runs/20261014T025011Z-fleet05-A019-orthogonality-extensions/REPORT.md')]
save(R/'out/SOURCE_RECEIPTS.json',{'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sources':[{'path':str(p),'sha256':sha(p)} for p in sources],'scope':'local source hashes; no remote or review receipt'})
if not (R/'out/INCOMING_STATUS.md').exists():(R/'out/INCOMING_STATUS.md').write_bytes((A/'STATUS.md').read_bytes())
(A/'STATUS.md').write_text('STATE: A017 stage5 locally complete: <=7 edits H<=(4+2/ln2)(I-1), <=8 H<=7(I-1), zero adaptive K4 bill; rank-two collapse13120 exact cases; full FEI OPEN, review pending.\nNEXT: A091/A090 review v3; validate signed nine-edit rank-two deflation then rank-four five-control pivot/reserve, preserving full terminal costs and fixed-order3/8 obstruction.\n',encoding='utf8')
tag='2026-10-14 stage5 (run '+R.name+')'
entry='\n'+tag+': Closed saved all-weak rank-two coset-minus-one collapse in original coordinates; parity extends adaptive zero K4 bill through eight edits. Seven rate4+2/ln2, eight rate7, with full retained terminals/data influence1. Collapse13120cases/118080assertions; tree442roots/2284queries/2726leaves/6721terminalsets/67960assertions; critical128/2187 and seven3/8 obstruction rerun. New v3 supersedes v2; independent review pending. NEXT signed internal-edge correction and nine-edit rank-four policy.\n'
for name in ['WORKLOG.md','LEARNED.md']:
 p=A/name
 if tag not in p.read_text(encoding='utf8'):
  with p.open('a',encoding='utf8') as f:f.write(entry)
req=P['required_per_run'];assert set(claim)==set(req['claim_fields'])
assert set(progress)=={k.split(' (')[0] for k in req['progress_fields']}
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert all('## '+h in (R/'REPORT.md').read_text(encoding='utf8') for h in req['report_fields'])
assert (A/'STATUS.md').read_text(encoding='utf8').count('\n')==2
assert sha(R/'INHERITED_PROOF.md')==sha(old/'PROOF.md') and sha(R/'DERIVATION.md')==sha(old/'DERIVATION.md')
for p in R.rglob('*.json'):json.loads(p.read_text(encoding='utf-8-sig'))
for helper in ['collapse','tree8','critical','ternary','seven']:
 spec=json.loads((R/'out'/(helper+'_FROZEN_SPEC.json')).read_text(encoding='utf-8-sig'))
 assert spec['helper_sha256']==sha(R/'code'/(helper+'.py'))
assert json.loads((R/'out/collapse_certificate.json').read_text())['cases']==13120
assert json.loads((R/'out/tree8_validation.json').read_text())['roots']==442
files=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']
assert all(p.stat().st_size<20*1024*1024 for p in files)
save(R/'out/PERSISTENCE_RECEIPTS.json',{'status':'PASS','recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'claim_statement_sha256':claim['statement_sha256'],'files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(files)],'rolling_files':[{'path':str(A/name),'sha256':sha(A/name)} for name in ['STATUS.md','WORKLOG.md','LEARNED.md']],'review':'pending','remote_mirror':'not verified','protocol_schema':'PASS'})
print(json.dumps({'status':'PASS','artifacts':len(files)+1,'claim_version':3,'statement_sha256':claim['statement_sha256'],'schema':'PASS','compatibility':'IDENTICAL','all_under20MB':True}))
