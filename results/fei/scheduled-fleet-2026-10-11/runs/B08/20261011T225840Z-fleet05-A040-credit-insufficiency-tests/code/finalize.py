from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1]; AGENT=ROOT.parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
run=ROOT.name
def save(name,obj): (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
statement='For G_a=addressing on a address bits tensor a three-bit point defect, TC, K_supp, K_shape and A036 support-restricted normalized T are strictly positive O(1), and each divided by H is Theta(1/a), with constants in REPORT.md. For even k>=4 quadratic bent point surgery, every physical-coordinate J_i is strictly positive, J_i/B_i~4*2^-k/ln(2), TC/H~8*2^-k/(k*ln(2)), normalized T/(sum B_i)~32*k*2^(-2k)>0, and B_i/Inf_i->2. For the B05 family with r=2k, min_i B_i/Inf_i->2 and J_best/h2(Inf_best)->1, while selector J/h2->2/3. Sparse tribes t=w, width w have (M-T/4)/I->2+log2(e) and (TC-T/4)/I->log2(e)-2.'
hyp=['Boolean signs on uniform physical cubes','base-two entropy and KL','A036 v1 support-restricted signed product-marginal reference; no unspecified zero completion','disjoint physical tensors where specified','even k>=4 for asymptotic bent and B05 controls','sparse tribes t=w, w->infinity']
claim={
 'claim_id':'A040-LIVE-CREDIT-INSUFFICIENCY-AND-BEST-COORDINATE-GUARD','version':1,
 'exact_statement':statement,'hypotheses':hyp,'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),
 'contributors':['A040'],'proof_source':str(ROOT/'REPORT.md'),'proof_dependencies':[],
 'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':['positive universal fixed fraction of erasure recovered by some physical-coordinate posterior KL J_i','positive universal fixed fraction of spectral entropy recovered by the specified global support-restricted credits alone'],
 'first_unproved_line':None,'next_consumers':['A036','A037','A038','A039','A064','A088','A094','B20']}
save('CLAIMS.json',[claim])
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':run,'stream':'B08','packet_id':'A040','gap_id':'G-R-MISMATCH','attempt_id':'A040-credit-insufficiency-1',
 'method':'self-contained signed Walsh/packet derivations, exact Fraction validation and rational log intervals',
 'mathematical_delta':'Positive global credits/H=Theta(1/a) on addressing times fixed defect; all-coordinate posterior J/B~4*2^-k/ln2 on bent point surgery; B05 best-coordinate and sparse-tribes calibration guards proved.',
 'deliverable_status':'COMPLETE_LOCAL_PENDING_REVIEW','mathematical_status':'SCOPED_CREDIT_TESTS_RESOLVED_FULL_FEI_OPEN',
 'claim_versions_used':[], 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
 'source_artifacts':['REPORT.md','out/FROZEN_SPEC.json','out/FROZEN_SPEC_BENT_REPAIR.json','code/check.py','code/bent_repair.py','out/verification.json','out/bent_repair.json','out/source_receipts.json','out/PILOT_CORRECTION.md'],
 'next_consumers':claim['next_consumers'],
 'next_action':'A037/A039 evaluate actual data-first stopping-tree erasure-minus-single-use-posterior on bent point surgery with terminal entropy retained; A088/A094 independently reconstruct this package.',
 'stagnant_substantive_attempts':0,
 'blockers':['Independent review and supervisor adoption/copy not yet observed; universal erasure and stopping-tree payments remain open'],
 'packet_ids':['A040']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
src=[]
base=Path(r'~\mop_fei100\reports\fei-2026-10-11')
paths=[base/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
supp=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
paths += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += [supp/'sources'/n for n in ['ERASURE_REDUCTION.md','BLOCK_RESTRICTION_IDENTITY_2026-09-18.md','GAMMA_ENDPOINT_LEDGER.md','ROUTE_MAP_CURATED.md']]
paths += list(Path(r'~\brain_workers\FEI100_20261011\context').glob('*.txt'))
paths += [Path(r'~\brain_workers\FEI100_20261011\BOARD.md'),Path(r'~\brain_workers\FEI100_20261011\claude\B08\STREAM_NOTES.md')]
paths += list(Path(r'~\brain_workers\FEI100_20261011\agents\A036').glob('runs/*/REPORT.md'))
paths += list((base/'runs'/'B05').glob('*/REPORT.md'))
for p in paths:
 b=p.read_bytes();src.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'use':'context/excerpts or tested-family/definition source; mathematical derivations self-contained'})
save('out/source_receipts.json',src)
checks=json.loads((ROOT/'out/verification.json').read_text())['checks']+json.loads((ROOT/'out/bent_repair.json').read_text())['checks']
(AGENT/'STATUS.md').write_text('STATE: A040 local packet complete: positive-credit asymptotic no-gos and B05 best-coordinate/tribes guards proved; '+str(checks)+' exact checks passed; review pending; full FEI OPEN.\nNEXT: A088/A094 reconstruct; A037/A039 pay data-first tree erasure minus single-use posterior on bent point surgery with terminal entropy retained.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+now+' — '+run+': read protocol, board/B08 source targets; proved support-exact addressing and all-coordinate bent positive-credit insufficiency, B05 best-coordinate opposite outcome, sparse-tribes normalized calibration. Initial slow Fraction pilot terminated and revised with dyadic interval arguments; enforced-timeout reruns passed '+str(checks)+' checks. Independent review, adoption and copying pending.\n')
(AGENT/'LEARNED.md').write_text('A040 durable facts ('+now+')\n\nAddressing has Q(A)=(1-2^-a)^(2^a-1), Q(.|A)=P. Support-restricted b=sqrt(Q(A))*fhat gives R=delta_0, Z=Q(A)^2, T=-2 log2 Q(A); conditioned b instead gives T=0. Tensor a fixed three-bit defect to make support and shape KL both strictly positive constants while H grows as 2a. This is entropy-fraction insufficiency, not failure of influence payment.\n\nQuadratic bent one-point surgery on even k>=4: d_i=1/2+2^-k*2; every coordinate has J_i/B_i~4*2^-k/ln2>0 and B_i/d_i->2. Exact pair formula and all-coordinate symmetry are in REPORT.md. TC/H~8*2^-k/(k ln2). The same full-support family has strictly positive normalized T~32*k^2*2^(-2k), T/(sum B_i)~32*k*2^(-2k). A positive KL need not pay a positive fraction of erasure, even at the best coordinate.\n\nB05 activated bent surgery r=2k: selector J/h2->2/3 and B/d~k; data/control B/d->2 and best-coordinate J/h2->1. Bad selector results cannot establish a best-coordinate obstruction. Sparse tribes t=w: (M-T/4)/I->2+log2 e and (TC-T/4)/I->log2 e-2.\n\nExact log series should first enclose huge rational arguments by outward dyadic brackets. Near one at extremely tiny scales, use u-u^2/2<=ln(1+u)<=u on the exact rational u, and check relative interval widths before exporting illustrative midpoints. Arbitrary denominator growth and a trial 256-bit grid exceeded pilot caps; the final local bound reduced runtime to 6.16 seconds. Output floating ratios are illustrative, not certified serialized intervals.\n',encoding='utf-8')
protocol=json.loads((base/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))['required_per_run']
assert set(progress)=={x.split(' (')[0] for x in protocol['progress_fields']}
assert set(claim)==set(protocol['claim_fields'])
assert json.loads((ROOT/'PROGRESS.json').read_text())==json.loads((ROOT/'PACKET_DELTA.json').read_text())
receipts=[]
for p in sorted(ROOT.rglob('*')):
 if p.is_file() and p.name!='save_receipts.json':
  b=p.read_bytes();assert len(b)<20*1024*1024;receipts.append({'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
save('out/save_receipts.json',{'saved_at':now,'files':receipts,'mirror_verified':False,'independent_review_observed':False,'checks':checks})
print(json.dumps({'checks':checks,'schema_checks':'PASS','files_hashed':len(receipts),'status_file':str(AGENT/'STATUS.md')}))
