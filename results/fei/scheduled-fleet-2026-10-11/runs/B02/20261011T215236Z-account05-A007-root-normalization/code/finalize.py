from pathlib import Path
from datetime import datetime, timezone
import hashlib,json

run=Path(__file__).resolve().parents[1]; agent=run.parents[1]
def save(path,obj):
    path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
reports=Path('~/mop_fei100/reports/fei-2026-10-11')
protocol=json.loads((reports/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
statement=('For every nonconstant finite Boolean indicator B=OR_l b_l with rho_l=E b_l>0, '
 'every r>=1 and every fixed lambda_l>0 with sum lambda_l<=1, let p=2^-r, '
 'F=2 A_r B-1 on fresh core coordinates, g=2B-1, v=Var(F), '
 's=sum lambda_l rho_l, D=product(1+p lambda_l rho_l)-1 and delta=log2(D/(p s)). '
 'There exist distinct actual partition-forest laws with K=1 when the spectral set meets the core '
 'and 1<=K<=|T| otherwise. Their root block equals v log2(s)+v delta+r(E K-v) '
 '+E sum_roots log2(1/rho_l), with 0<=r(E K-v)<=p I(g)/2 and '
 'v delta<=(log2 e) 2rp E B. Thus normalized common-core rarity overhead is '
 'at most (log2 e) I(F), leaving base rarity and all remaining coding costs unpaid. '
 'For disjoint private conjunctions rho_l=2^-w_l and Q=product(1-rho_l), '
 'E K-v=4p^2 Q(sum rho_l-(1-Q)). All E are unconditioned spectral-weighted sums '
 'over nonempty sets; entropy units are bits. A fixed complete-reference scale prior '
 'lambda^(j)=2^-j lambda, w_j=1/((j+1)(j+2)) pays v for selecting j=0.')
claim=dict(claim_id='A007-SHARED-CORE-ROOT-CANCELLATION',version=1,exact_statement=statement,
 hypotheses=['uniform finite cube','fresh r>=1 conjunction core','B nonconstant','rho_l>0',
             'positive fixed incidence weights with sum<=1','actual conditioned partition forests','bits'],
 statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['A007'],
 proof_source={'path':'REPORT.md','sections':'Derivation 1-6','companion':'ROOT_NORMALIZATION.tex'},
 proof_dependencies=[{'source':'source_material/reductions/paper/forests.tex','locator':'thm:posteriorforest and eq:forestconditioning','status':'source-complete baseline'},
                     {'source':'SEED_LEMMAS.md','locator':'Section 2','status':'source-complete elementary mixture interface'}],
 review_records=[],status='AUTHOR_PROVED_EXACTLY_CHECKED_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=[],
 first_unproved_line=None,next_consumers=['A006','A014','A086','A094','B20'])
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
save(run/'CLAIMS.json',[claim])
progress=dict(protocol_revision=protocol['revision'],run_id=run.name,stream='B02',packet_id='A007',
 gap_id='G-J-COST/SHARED-CORE-ROOT-NORMALIZATION',attempt_id='A007-root-normalization-1',
 method='exact normalization plus constructive star forests and Boolean spectral suppression',
 mathematical_delta='Proved normalized common-core rarity overhead <= log2(e) I(F) for arbitrary activated data unions; exact heterogeneous-petal excess-root formula. Other costs remain unpaid.',
 deliverable_status='COMPLETE_LOCAL_ARTIFACT',mathematical_status='ROOT_COMPONENT_PROVED_REVIEW_PENDING_FULL_FEI_OPEN',
 claim_versions_used=['baseline forests.tex thm:posteriorforest (hash in out/SOURCES.json)','SEED_LEMMAS Section 2 (hash in out/SOURCES.json)'],
 claims_created_or_changed=[{'claim_id':claim['claim_id'],'version':1}],
 source_artifacts=['REPORT.md','ROOT_NORMALIZATION.tex','ROOT_FAMILY.md','FROZEN_SPEC.json','code/check.py','out/CHECK.json','out/SOURCES.json','out/RECEIPTS.json'],
 next_consumers=claim['next_consumers'],next_action='A086/A094 reconstruct root law, source-component validity and spectral expectation; A006 incorporate into shared-r-core complete posterior ledger.',
 stagnant_substantive_attempts=0,blockers=['B02 Claude stream notes absent','independent review pending','complete base coding-cost estimate remains open'],
 packet_ids=['A007'])
assert set(progress)==set(x.split(' (')[0] for x in protocol['required_per_run']['progress_fields'])
save(run/'PROGRESS.json',progress); save(run/'PACKET_DELTA.json',progress)

sources=[(reports/'EXECUTION_PROTOCOL.json','full read'),
 (reports/'FEI_100_agent_research_plan.tex','Endpoint J and A007 contract'),
 (reports/'source_material/reductions/paper/forests.tex','conditioned queue and thm:posteriorforest'),
 (Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents/SEED_LEMMAS.md'),'Section 2'),
 (Path('~/brain_workers/FEI100_20261011/agents/A006/runs/20261011T210855Z-account05-A006-posterior-forest-optimization/REPORT.md'),'full report; not a proof premise')]
context=Path('~/brain_workers/FEI100_20261011/context')
for p in context.glob('*.txt'):
    sources.append((p,'threshold current: joint coding and activation; others: introductions/scope'))
save(run/'out'/'SOURCES.json',[dict(path=str(p),sha256=sha(p),scope=scope) for p,scope in sources])
check=json.loads((run/'out'/'CHECK.json').read_text())
now=datetime.now(timezone.utc).isoformat()
(agent/'STATUS.md').write_text('STATE: A007 root component proved locally for arbitrary shared-core activations; 176,748 exact assertions passed; independent review pending; full FEI OPEN.\nNEXT: A086/A094 review root law and star forest; A006 combine with complete shared-r-core posterior cost; B02 pending-claim cap reached.\n',encoding='utf8')
with (agent/'WORKLOG.md').open('a',encoding='utf8') as f:
    f.write(f'\n{now} — Read protocol, board and A006 report; B02 lead notes absent. Derived log D normalization, one-core-root construction, p^2 suppression of multiple roots, and exact heterogeneous-petal excess. Checked {check["petal_cases"]} petal cases and {check["arbitrary_activation_cases"]} arbitrary-data cases, {check["assertions_passed"]} exact assertions in {check["elapsed_seconds"]:.3f}s. Saved complete root-component proof; full remaining coding cost open.\n')
(agent/'LEARNED.md').write_text('''# Durable A007 facts

- Conditioned root law: D=product(1+lambda_l pi_l)-1, Lambda+log2 Z=log2 D; q(R)=product_R(lambda_l pi_l)/D for nonempty R. For a=sum lambda pi, log2 D=log2 a+delta, 0<=delta<=a log2 e.
- Singleton-root posterior over eligible E cancels to log2[D/sum_E(lambda pi)]. This optimizes only the root block; later root-dependent draws remain.
- For F=2 A_r B-1 with pi_l=2^-r rho_l and sum lambda<=1, a Fourier set meeting the common core admits an actual one-root star. Core-empty sets permit K<=|T|. Their nonempty-data spectral mass has factor 4p^2.
- Hence r(E K-Var(F))<=p I(2B-1)/2 and the complete normalization plus common rarity scale is <=log2(e) I(F), in addition to unpaid base rarity. All expectations here are unconditioned spectral-weighted sums on nonempty sets.
- For heterogeneous disjoint conjunction petals, E K-v=4p^2 Q(sum rho_l-(1-Q)). Cancellation is not pointwise exact for multiple roots; suppression pays its expectation.
- Fixed rare k-root patterns retain (k-1)log2(1/t); neither a negative normalizer nor root entropy pays arbitrarily many copies for free.
- Arbitrary Boolean B is admitted, so this component lemma cannot establish full FEI without paying remaining base labels, ranks, congestion and rarity. Complete-reference priors must retain their own normalizers and pay selection costs.
''',encoding='utf8')
# Check exact protocol field names and persisted report coverage.
report=(run/'REPORT.md').read_text()
for field in protocol['required_per_run']['report_fields']: assert '## '+field in report,field
receipts=[]
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='RECEIPTS.json':
        receipts.append(dict(path=str(p.relative_to(run)),size_bytes=p.stat().st_size,sha256=sha(p)))
for p in (agent/'STATUS.md',agent/'WORKLOG.md',agent/'LEARNED.md'):
    receipts.append(dict(path=str(p),size_bytes=p.stat().st_size,sha256=sha(p)))
save(run/'out'/'RECEIPTS.json',dict(saved_at=now,scope='local persistence only; mirrors and review pending',files=receipts))
print(json.dumps(dict(files=len(receipts),claim_id=claim['claim_id'],schema_fields_checked=True,check=check['assertions_passed'])))
