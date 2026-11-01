from pathlib import Path
import json, hashlib
from datetime import datetime, timezone

run=Path(__file__).resolve().parent.parent
agent=run.parent.parent
def write(name,value):
    (run/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
statement=('For every finite disjoint tensor product of Boolean one-point defects f_m=1-2*1_point, m>=2, including physical translations, global sign, character multiplication, fresh character coordinates and irrelevant coordinates, let P=fhat^2, Q be the product of its actual spectral coordinate marginals, B=sum_i h2(P(i in S)), K=D2(P||Q), b=sign(fhat)*sqrt(Q) on the common support and zero off it, v_U=(sum_S b_S b_{S xor U})^2, Z=sum_U v_U, T=H(v/Z)-log2 Z, I=sum_i P(i in S). Then K>=max(0,B-4I), K>=T/4-8I, and B<=T/4+8I. In particular the latter two separately proved inequalities imply H(P)<=16I, while the direct factor entropy bound gives H(P)<=4I. All entropy and divergence quantities are in bits.')
claim={
 'claim_id':'A036-POINT-DEFECT-TENSOR-NORMALIZED-PAYMENT-RECOVERY',
 'version':1,
 'exact_statement':statement,
 'hypotheses':['Genuine Boolean sign on uniform finite cube','Disjoint point-defect tensor factorization as stated','Actual product-marginal reference Q, same-sign amplitude b','Product-compatible actual phases; support terms retained','All logarithms base two'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),
 'contributors':['A036'],
 'proof_source':'REPORT.md, Sections 1-7; code/check.py; out/verification.json',
 'proof_dependencies':[],
 'review_records':[],
 'status':'ANALYTICALLY_PROVED_LOCALLY_EXACTLY_CHECKED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],
 'refutes':[],
 'first_unproved_line':None,
 'next_consumers':['A037','A038','A039','A040','A048','A066','A088','A094','B20']}
write('CLAIMS.json',[claim])
progress={
 'protocol_revision':'2026-10-11-execution-v2',
 'run_id':run.name,
 'stream':'B08',
 'packet_id':'A036',
 'gap_id':'G-A036-NORMALIZED-DIVERGENCE-RECOVERY',
 'attempt_id':'A036-reference-law-divergence-attempt-1',
 'method':'Explicit same-sign product-marginal reference; exact level collision formula; singleton recovery; rational entropy caps; disjoint tensor extension',
 'mathematical_delta':'Proved restricted normalized payment K>=T/4-8I and separate recovery B<=T/4+8I, plus K>=[B-4I]_+, on arity-unbounded disjoint point-defect tensors. Raw-L obstruction retained. Universal endpoint open.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT',
 'mathematical_status':'RESTRICTED_THEOREM_PROVED_UNREVIEWED; UNIVERSAL_TARGET_OPEN',
 'claim_versions_used':[],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
 'source_artifacts':['REPORT.md','REFERENCE_DIVERGENCE.tex','NORMALIZED_COLLISION_LEDGER.md','code/check.py','out/FROZEN_SPEC.json','out/verification.json','out/check_receipt.json','out/source_receipts.json','out/save_receipts.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'Prove or refute payment and recovery separately for a point surgery of a tensor of two point-defect factors, retaining changed marginals and actual signs. A088/A094 independently review this restricted package.',
 'stagnant_substantive_attempts':0,
 'blockers':['B08 STREAM_NOTES.md absent at stage reads; no mathematical dependency blocked','Independent review and supervisor mirrors not observed'],
 'packet_ids':['A036']}
write('PROGRESS.json',progress)
write('PACKET_DELTA.json',progress)
verified=json.loads((run/'out/verification.json').read_text())
write('out/check_receipt.json',{'command':'python -X utf8 code/check.py','working_directory':str(run),'exit_code':0,'observed_summary':{'cases':15,'all_assertions_passed':True,'runtime_seconds_diagnostic':verified['runtime_seconds_diagnostic']},'verification_sha256':sha(run/'out/verification.json'),'initial_failure':'out/INITIAL_CHECK_FAILURE.txt','external_independent_review':False})
roots=[Path(r'~\mop_fei100\reports\fei-2026-10-11'),Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents'),Path(r'~\brain_workers\FEI100_20261011\context')]
sources=[]
for root in roots:
    for p in root.glob('*'):
        if p.is_file() and p.suffix in ['.md','.json','.tex','.txt']:
            sources.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'read_scope':'See REPORT.md source paragraph; full-file hashing does not claim full substantive review'})
for p in (roots[1]/'sources').glob('*.md'):
    sources.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'read_scope':'Curated source catalogue; only cited route-map excerpts used for context'})
board=Path(r'~\brain_workers\FEI100_20261011\BOARD.md')
sources.append({'path':str(board),'sha256':sha(board),'bytes':board.stat().st_size,'read_scope':'Full board read at initial stage'})
write('out/source_receipts.json',sources)
(agent/'STATUS.md').write_text('STATE: A036 local stage complete: restricted normalized collision payment K>=T/4-8I and separate recovery B<=T/4+8I proved on point-defect tensors; exact checks passed; independent review pending; full FEI open.\nNEXT: A088/A094 reconstruct proof; test a point surgery of a two-factor point-defect tensor with changed marginals and actual signs.\n',encoding='utf-8')
now=datetime.now(timezone.utc).isoformat()
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+now+': Saved complete restricted payment/recovery proof and exact certificate. Fifteen dimensions m=2..16 passed, direct Walsh reconstruction m=2..7; runtime '+str(verified['runtime_seconds_diagnostic'])+' seconds. Initial large-rational text serialization failure repaired by outward rational grid rounding. Full FEI remains open; next point surgery leaves exact tensor factorization.\n')
expected_claim={'claim_id','version','exact_statement','hypotheses','statement_sha256','contributors','proof_source','proof_dependencies','review_records','status','supersedes','refutes','first_unproved_line','next_consumers'}
expected_progress={'protocol_revision','run_id','stream','packet_id','gap_id','attempt_id','method','mathematical_delta','deliverable_status','mathematical_status','claim_versions_used','claims_created_or_changed','source_artifacts','next_consumers','next_action','stagnant_substantive_attempts','blockers','packet_ids'}
assert set(claim)==expected_claim
assert set(progress)==expected_progress
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
receipt=[]
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='save_receipts.json':
        assert p.stat().st_size<20*1024*1024
        receipt.append({'path':str(p.relative_to(run)),'sha256':sha(p),'bytes':p.stat().st_size})
write('out/save_receipts.json',{'saved_at_utc':now,'run_directory':str(run),'protocol_field_sets_checked':True,'progress_delta_byte_identical':True,'all_run_files_under_20mb':True,'files':receipt,'mirror_status':'NOT_OBSERVED','independent_review_status':'PENDING'})
print(json.dumps({'saved_at_utc':now,'files':len(receipt)+1,'protocol_field_sets_checked':True,'progress_delta_byte_identical':True,'all_run_files_under_20mb':True}))
