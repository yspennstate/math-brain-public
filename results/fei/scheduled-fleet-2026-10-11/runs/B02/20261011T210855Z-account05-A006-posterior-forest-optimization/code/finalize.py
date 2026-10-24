"""Persist protocol-shaped handoff and hash receipts, restricted to A006."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json

BASE=Path(__file__).resolve().parents[1]
AGENT=BASE.parents[1]
REPORTS=Path('~/mop_fei100/reports/fei-2026-10-11')
SUPP=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents')
CONTEXT=Path('~/brain_workers/FEI100_20261011/context')

def save(path,obj):
    path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

sources=[]
for path,scope in [
    (REPORTS/'EXECUTION_PROTOCOL.json','full execution protocol'),
    (REPORTS/'README.md','full overview'),
    (REPORTS/'CURRENT_STATUS.md','full current status'),
    (REPORTS/'CLAIM_REGISTRY.json','registry, no B02 pending candidate at supplied snapshot'),
    (REPORTS/'OBSTRUCTION_REGISTRY.json','obstructions and source navigation'),
    (REPORTS/'PACKET_STATUS.json','packet index, A006 initial open state'),
    (REPORTS/'STREAM_NEXT_ACTIONS.json','stream instructions, especially B02'),
    (REPORTS/'FEI_100_agent_research_plan.tex','Endpoint J and A006 acceptance/dispatch contract'),
    (REPORTS/'source_material/reductions/paper/forests.tex','full section and complete posterior proof; principal dependency'),
    (SUPP/'SEED_LEMMAS.md','full seed statements; Section 2 complete prior mixture proof'),
    (SUPP/'CAMPAIGN.md','campaign scope and units'),
    (SUPP/'CLAIMS.md','baseline claim ledger'),
    (SUPP/'COUNTEREXAMPLES.md','known failures and valid exclusions'),
    (SUPP/'NATIVE_MAPPING.md','B02 mapping'),
    (SUPP/'baseline/current-threshold-paper.tex','Sections 5.2 and 5.6 queue and witness probability'),
    (SUPP/'baseline/computations/verify_witness_forests.py','full code inspection; not executed or modified'),
    (SUPP/'sources/OVERLAPPING_PRODUCT_NOTE.md','full note, not a theorem premise'),
    (CONTEXT/'threshold_paper_38pp.txt','Section 5.6 Proposition 5.5 and addressing context'),
    (CONTEXT/'threshold_paper_29pp_earlier_version.txt','abstract and introductory scope'),
    (CONTEXT/'percolation_spectral_pivotal_entropy_30pp.txt','Section 2 Lemma 2.1 spatial refinement, not used as premise'),
    (CONTEXT/'percolation_spectral_pivotal_entropy_31pp_other_version.txt','abstract and introductory scope'),
    (Path('~/brain_workers/FEI100_20261011/BOARD.md'),'full initial board'),
]:
    data=path.read_bytes()
    sources.append({'path':str(path),'sha256':sha256(data).hexdigest(),'bytes':len(data),'inspection_scope':scope})
save(BASE/'out/SOURCES.json',sources)
proof_hash=next(s['sha256'] for s in sources if s['path'].endswith('forests.tex'))
seed_hash=next(s['sha256'] for s in sources if s['path'].endswith('SEED_LEMMAS.md'))
statement=('For every integer m>=1, f_m=2*1[x0=1]*1[at least one xi=1 for 1<=i<=m]-1 '
 'on the uniform (m+1)-cube, represented as the union of the m distinct clauses (x0 AND xi), '
 'with supports ordered (0,i), M_i=1, pi_i=1/4 and lambda_i=1/m, has exact finite posterior '
 'partition weights S_B({0})=1/4, S_B(T)=m^(-t)*(a/4)^t, and '
 'S_B({0} union T)=t!*a^(t-1)/(4*m^t)*(1+(1-t/m)*a), where t=|T|>=1 and a=2^(-6/5). '
 'Its complete conditioned all-partition residual is <=(43/10) I(f_m), and its exact '
 'conditioned all-partition run-cost expectation is <=(23/2) I(f_m). A normalized prior '
 'w_k=1/((k+1)(k+2)) on lambda_i^(k)=2^(-k)/m pays at most v additional bits, giving '
 'bounds (53/10) I and (25/2) I respectively. Every point-mass posterior choice in '
 'this representation has residual/I tending to infinity as m tends to infinity.')
hypotheses=['integer m>=1','uniform independent physical signs','specified fixed sunflower DNF and support orders',
 'distinct actual finite partition-forest runs only, including ordered child-label draws',
 'base-two entropy and costs, gamma=6/5, natural logarithms for rank F',
 'failed/infinite paths have zero output mass; reference is conditioned on nonempty initial roots']
claim_id='A006-SUNFLOWER-POSTERIOR-FOREST-PAYMENT'
dependencies=[{'source':'source_material/reductions/paper/forests.tex','locator':'thm:posteriorforest and eq:forestcost',
               'sha256':proof_hash,'status':'SOURCE_COMPLETE_BASELINE_READ'},
              {'source':'SEED_LEMMAS.md','locator':'Section 2 normalized prior over complete reference laws',
               'sha256':seed_hash,'status':'SOURCE_COMPLETE_BASELINE_READ'}]
claim={'claim_id':claim_id,'version':1,'exact_statement':statement,'hypotheses':hypotheses,
 'statement_sha256':sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 'contributors':['account05/A006'], 'proof_source':{'path':str(BASE/'REPORT.md'),'sections':'complete derivation, Sections 2-6'},
 'proof_dependencies':dependencies,'review_records':[], 'status':'ANALYTICALLY_PROVED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[], 'refutes':['uniform dimension-independent deterministic forest residual payment in the specified sunflower DNF'],
 'first_unproved_line':None, 'next_consumers':['A007','A008','A009','A010','A014','A086','A094','B20']}
save(BASE/'CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':BASE.name,'stream':'B02','packet_id':'A006',
 'gap_id':'G-J-COST','attempt_id':'A006-G-J-COST-001-sunflower','method':'exact all-partition posterior enumeration plus all-m binomial spectrum payment',
 'mathematical_delta':'Exact distinct-run optimum and absolute complete-cost influence bounds for an unbounded-read sunflower DNF; certified deterministic-residual divergence; universal gap remains open.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'RESTRICTED_COST_THEOREM_PROVED_PENDING_REVIEW; FULL_FEI_OPEN',
 'claim_versions_used':dependencies,'claims_created_or_changed':[{'claim_id':claim_id,'version':1}],
 'source_artifacts':['REPORT.md','CLAIMS.json','FROZEN_SPEC.json','code/check.py','out/CHECK.json','out/PILOT_V1.json','out/SOURCES.json','out/RECEIPTS.json'],
 'next_consumers':['A007','A008','A009','A010','A014','A086','A094','B20'],
 'next_action':'Independent A086/A094 reconstruction; then extend the forced-star enumeration to a shared r-variable conjunction with private singleton leaves, uniformly in r and m.',
 'stagnant_substantive_attempts':0,'blockers':['No universal representation/cost payment established.','Independent review and supervisor mirror upload not yet performed.'],
 'packet_ids':['A006']}
save(BASE/'PROGRESS.json',progress)
save(BASE/'PACKET_DELTA.json',progress)
AGENT.joinpath('STATUS.md').write_text('STATE: A006 complete local artifact: exact all-partition sunflower posterior optimum; residual <=43/10 I and paid-prior whole cost <=25/2 I; independent review pending; full FEI open.\nNEXT: A086/A094 review; extend forced-star coding to an r-variable shared conjunction, paying all priors and distinct-run entropy.\n',encoding='utf-8')
now=datetime.now(timezone.utc).isoformat()
with AGENT.joinpath('WORKLOG.md').open('a',encoding='utf-8') as file:
    file.write('\n'+now+': Completed all-m sunflower cost proof and deterministic witness obstruction. Pilot passed; full trace expansion passed 213,593 assertions in 1.861 seconds. Saved protocol files, source pins and receipts. No independent acceptance or remote upload claimed.\n')
with AGENT.joinpath('LEARNED.md').open('a',encoding='utf-8') as file:
    file.write('\nFor common-plus-private T, all partition forests are stars. Inside roots contribute t! actual runs; outside roots contribute (m-t)t! actual runs. The residual optimizer weights runs by 2^(-B), whereas the exact run-cost optimizer weights by actual conditional q; they generally differ. Complete residual <=43/10 I and exact all-partition run-cost <=23/2 I for all m>=1. A fixed normalized one-sided scale prior adds at most v<=I bits.\n')
protocol=json.loads((REPORTS/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
check_fields=set(protocol['required_per_run']['claim_fields'])
assert set(claim)==check_fields
required={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert set(progress)==required
assert json.loads((BASE/'PROGRESS.json').read_text())==json.loads((BASE/'PACKET_DELTA.json').read_text())
receipt=[]
for path in sorted(BASE.rglob('*')):
    if path.is_file() and path.name!='RECEIPTS.json':
        data=path.read_bytes()
        assert len(data)<20_000_000
        receipt.append({'path':str(path.relative_to(BASE)),'bytes':len(data),'sha256':sha256(data).hexdigest()})
save(BASE/'out/RECEIPTS.json',{'saved_at_utc':now,'scope':'local persistence only; receipt excludes itself',
 'artifacts':receipt,'protocol_fields':'PASS','remote_upload':'NOT_PERFORMED','independent_review':'PENDING'})
print(json.dumps({'status':'PASS','saved_files':len(receipt)+1,'claim_id':claim_id,'run':str(BASE)},indent=2))
