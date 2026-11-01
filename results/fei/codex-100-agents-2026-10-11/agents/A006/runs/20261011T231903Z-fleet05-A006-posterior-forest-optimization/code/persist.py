"""Protocol persistence for A006 stage 2; writes only within A006."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
BASE=Path(__file__).resolve().parents[1]
AGENT=BASE.parents[1]
TEAM=AGENT.parents[1]
REPORTS=Path('~/mop_fei100/reports/fei-2026-10-11')
SUPP=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents')
A008=TEAM/'agents/A008/runs/20261011T221357Z-fleet05-A008-gate-label-compression'
A094=TEAM/'agents/A094/runs/20261011T224936Z-fleet05-A094-proof-chain-challenger'
def put(path,obj):
    path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
now=datetime.now(timezone.utc).isoformat()
source_pairs=[(TEAM/'BOARD.md','full stage-start board, snapshot 2026-10-11 23:19 UTC'),
 (TEAM/'claude/B02/STREAM_NOTES.md','full v1 directions and target'),
 (TEAM/'claude/B03/STREAM_NOTES.md','full v2; projective-plane theorem already completed locally'),
 (TEAM/'agents/A009/STATUS.md','affine-plane obstruction and next target'),
 (TEAM/'agents/A014/STATUS.md','signed-L2 and PP progress'),
 (REPORTS/'EXECUTION_PROTOCOL.json','full protocol'),
 (REPORTS/'source_material/reductions/paper/forests.tex','full conditioned posterior generator and theorem'),
 (SUPP/'baseline/current-threshold-paper.tex','pivotal antichain/noise/rank proof chain and derivative rank expectation'),
 (A008/'REPORT.md','full original report'),(A008/'WHOLE_SET_CODEC.tex','full proof'),
 (A008/'CLAIMS.json','original statement/version/hash'),
 (A094/'AUDIT.md','full prior-stage reconstruction and single-order rank obstruction')]
sources=[]
for path,scope in source_pairs:
    data=path.read_bytes()
    sources.append({'path':str(path),'sha256':sha256(data).hexdigest(),'bytes':len(data),'scope':scope})
put(BASE/'out/SOURCES.json',sources)
forest_hash=next(s['sha256'] for s in sources if s['path'].endswith('forests.tex'))
rank_hash=next(s['sha256'] for s in sources if s['path'].endswith('current-threshold-paper.tex'))
review=json.loads((A008/'CLAIMS.json').read_text(encoding='utf-8'))[0]
original_digest=sha256(json.dumps({'statement':review['exact_statement'],'hypotheses':review['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert original_digest==review['statement_sha256']
review['review_records']=review['review_records']+[{'reviewer':'A006','verdict':'ACCEPT_AT_ORIGINAL_STATED_SCOPE_NO_REPAIR',
 'proof_source':str(BASE/'AUDIT_A008.md'),'validation':str(BASE/'out/A008_REVIEW_CHECK.json'),
 'method':'Independent four-state dictionary trace pushforward and complete analytic proof reconstruction; author checker not imported',
 'reviewer_contributed_repair':False,'timestamp_utc':now}]
review['status']='INDEPENDENTLY_RECONSTRUCTED_AT_STATED_SCOPE_LOCAL_ADOPTION_PENDING'
deps=[{'source':'source_material/reductions/paper/forests.tex','locator':'thm:posteriorforest and eq:forestcost',
       'sha256':forest_hash,'status':'SOURCE_COMPLETE_BASELINE_READ'},
      {'source':'baseline/current-threshold-paper.tex','locator':'lem:pivotal-antichain, lem:antichain-noise, lem:ranktail; derivative-law rank expectation',
       'sha256':rank_hash,'status':'SOURCE_COMPLETE_BASELINE_PROOF_CHAIN_READ'}]
statement=('For every odd integer n>=1, let k=(n+1)/2 and Maj_n be uniform majority. '
 'Its positive prime-implicant table consists of every k-subset conjunction, with one cover ordered '
 'by a common physical order, lambda_R=1/binom(n-1,k-1), pi_R=2^(-k), and gamma=6/5. '
 'The conditioned posterior residual optimized over distinct actual finite partition-forest runs '
 'is at most [49/5+(6/5)*log2(e)]*I(Maj_n), strictly less than (58/5)*I(Maj_n) '
 'and at most (58/5)*sqrt(n). An admissible certificate uses the uniform posterior over all '
 'single-root containing-clause runs when |A|<=k, and one actual two-clause partition run '
 'with alternating ownership and one attachment when |A|>k. The same table construction, '
 'for an arbitrary Boolean spectrum, gives residual <=(43/5)*I+(6/(5*ln2))*E G(A), '
 'where G(A)=sum_{j in A}ln(j/(|A intersect [j-1]|+1)); the majority rank bound is '
 'E G<= (1+ln2)*I. No universal rank payment or all-Boolean PI-J bound is asserted.')
hyp=['uniform cube and bits for entropy/cost; natural units for G',
 'all positive prime implicants of odd majority; globally fixed support table and fractional weights',
 'partition subsets disjoint; every used gate visited exactly once; chronological child labels define actual run identity',
 'failed/infinite runs omitted and reference conditioned on nonempty initial roots',
 'no output-dependent reference-table or scale selection']
new={'claim_id':'A006-MAJORITY-PRIME-IMPLICANT-POSTERIOR-PAYMENT','version':1,
 'exact_statement':statement,'hypotheses':hyp,
 'statement_sha256':sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 'contributors':['A006'],'proof_source':{'path':str(BASE/'REPORT.md'),'sections':'complete derivation, Sections 2-6'},
 'proof_dependencies':deps,'review_records':[],'status':'ANALYTICALLY_PROVED_CERTIFIED_SMALL_CASES_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,
 'next_consumers':['B02','A007','A008','A009','A010','A015','A086','A094','B20']}
put(BASE/'CLAIMS.json',[review,new])
next_action=('Derive determinant lower bounds for actual source-SCC-constrained forests at a fixed prime-support assignment, '
 'with canonical child ordering, to certify the generic rank-weighted posterior mass; consume affine-plane obstruction '
 'and already completed PP/signed-L2 work, without redoing their class calculations.')
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':BASE.name,'stream':'B02','packet_id':'A006',
 'gap_id':'G-J-COST','attempt_id':'A006-G-J-COST-002-majority-prime-posterior',
 'method':'independent dictionary trace review, containing-clause posterior, two-gate ownership, exact algebraic partition sums and rational log enclosures',
 'mathematical_delta':'A008 v1 independently accepted at scope without repair; all odd majorities PI-J residual <58/5 I proved; full partition optima n=1,3 certified, constructive upper bounds n=5,7 checked; universal C020 gap retained.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'A008_INDEPENDENT_ACCEPTANCE_LOCAL; MAJORITY_COST_PROVED_PENDING_REVIEW; FULL_FEI_OPEN',
 'claim_versions_used':deps+[{'claim_id':review['claim_id'],'version':review['version'],'statement_sha256':review['statement_sha256'],'use':'independent review only, not majority proof premise'}],
 'claims_created_or_changed':[{'claim_id':review['claim_id'],'version':review['version'],'change':'independent review record'},
                            {'claim_id':new['claim_id'],'version':1,'change':'new restricted prime-table cost theorem'}],
 'source_artifacts':['REPORT.md','AUDIT_A008.md','CLAIMS.json','FROZEN_SPEC.json','code/check.py','code/persist.py',
 'out/A008_REVIEW_CHECK.json','out/MAJORITY_EXACT.json','out/SYMMETRIC_SPECTRA.json','out/CHECK_SUMMARY.json','out/SOURCES.json','out/RECEIPTS.json'],
 'next_consumers':new['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Universal rank-weighted actual-forest mass expectation unpaid; a universal single-order rank bound is false.',
 'Majority theorem independent review and supervisor adoption/upload unperformed.'], 'packet_ids':['A006']}
put(BASE/'PROGRESS.json',progress); put(BASE/'PACKET_DELTA.json',progress)
AGENT.joinpath('STATUS.md').write_text('STATE: A006 stage 2 complete: A008 v1 independently accepted locally; odd-majority prime-implicant posterior R<58/5 I proved, exact optima n=1,3 certified; majority review pending; full FEI OPEN.\nNEXT: Certify source-SCC-constrained actual-forest sums via determinant bounds for arbitrary prime tables; consume A009/A014/B03 dependencies without repeating plane or known-class FEI calculations.\n',encoding='utf-8')
with AGENT.joinpath('WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+now+' stage 20261011T231903Z: Followed B02 lead direction rather than prior shared-core NEXT. Reconstructed A008 from 5,454 independent dictionary traces and analytic all-m proof, accepted at original scope with no repair. Proved all-odd-majority prime-table residual <58/5 I using containing-clause posterior for small sets and two-gate forests for large sets. Pilot passed 11,574 assertions in 38.930 seconds; exact n=1,3 optima and n=5,7 construction intervals saved. B03 v2 reports PP cost already complete; next is generic forest-count certification, not another plane computation.\n')
with AGENT.joinpath('LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage 2: A008 dictionary/output theorem independently reconstructed at original scope, no repair. For odd majority, prime clauses are all k=(n+1)/2 subsets and lambda=1/binom(n-1,k-1). One-root cohort has binom(n-s,k-s) distinct runs for s<=k and log[binom(n,k)/binom(n-s,k-s)]<=2s. For s>k, alternating ownership fits two different clauses; each owner predecessor denominator is at least half the global selected position. This proves the fixed-table residual <=(43/5)I+(6/(5 ln2))E G, hence <58/5 I for majority. A universal bound on E G/I is false (A094 XOR-of-conjunction stress); do not use this regular-function input as a universal shortcut.\n')
protocol=json.loads((REPORTS/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
for claim in (review,new):
    assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert set(progress)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert (BASE/'PROGRESS.json').read_bytes()==(BASE/'PACKET_DELTA.json').read_bytes()
report=(BASE/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:
    assert '## '+field in report
assert report.rstrip().split('## Universal bridge\n\n')[-1].count('\n')==0
artifacts=[]
for path in sorted(BASE.rglob('*')):
    if path.is_file() and path.name!='RECEIPTS.json':
        data=path.read_bytes(); assert len(data)<20_000_000
        artifacts.append({'path':str(path.relative_to(BASE)),'bytes':len(data),'sha256':sha256(data).hexdigest()})
put(BASE/'out/RECEIPTS.json',{'saved_at_utc':now,'scope':'local persistence only','artifacts':artifacts,
 'protocol_fields':'PASS','independent_review_A008':'ACCEPT_AT_STATED_SCOPE_NO_REPAIR',
 'independent_review_majority':'PENDING','remote_upload':'NOT_PERFORMED'})
print(json.dumps({'status':'PASS','saved_files':len(artifacts)+1,'run':str(BASE)},indent=2))
