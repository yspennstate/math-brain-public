"""A006 stage 3 metadata and local receipts; writes only within A006."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
BASE=Path(__file__).resolve().parents[1]
AGENT=BASE.parents[1]
TEAM=AGENT.parents[1]
REPORTS=Path('~/mop_fei100/reports/fei-2026-10-11')
A008=TEAM/'agents/A008/runs/20261012T005959Z-account05-A008-gate-label-compression'
A009=TEAM/'agents/A009/runs/20261012T031835Z-account05-A009-fractional-incidence-optimization'
def put(path,obj): path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
now=datetime.now(timezone.utc).isoformat()
source_pairs=[(TEAM/'BOARD.md','full stage-start read, snapshot 2026-10-13 21:34 UTC; later tail revisited'),
 (TEAM/'claude/B02/STREAM_NOTES.md','full v2, 2026-10-11 23:35 UTC'),
 (AGENT/'runs/20261011T231903Z-account05-A006-posterior-forest-optimization/PROGRESS.json','previous stage handoff'),
 (REPORTS/'EXECUTION_PROTOCOL.json','full revision 2026-10-11-execution-v2'),
 (REPORTS/'source_material/reductions/paper/forests.tex','full prior-stage baseline; generator and posterior proof revisited this stage'),
 (A008/'REPORT.md','full original report'),(A008/'READ_ONCE_DNF.tex','full source proof'),(A008/'CLAIMS.json','full unchanged claim statement and dependency chain'),
 (A009/'REPORT.md','full report and complete transfer T'),(A009/'FOREST_TRANSFER.tex','full source proof; read for next interface, not independently accepted')]
sources=[]
for path,scope in source_pairs:
    data=path.read_bytes(); sources.append({'path':str(path),'scope':scope,'bytes':len(data),'sha256':sha256(data).hexdigest()})
put(BASE/'out/SOURCES.json',sources)
forest_hash=next(s['sha256'] for s in sources if s['path'].endswith('forests.tex'))
review=next(c for c in json.loads((A008/'CLAIMS.json').read_text(encoding='utf-8')) if c['claim_id']=='B02-A008-UNEQUAL-READONCE-DNF-FOREST-PAYMENT')
def digest(statement,hyp):
    return sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert digest(review['exact_statement'],review['hypotheses'])==review['statement_sha256']
review['review_records'].append({'reviewer':'A006','verdict':'HOLDS_AT_ORIGINAL_STATED_SCOPE_NO_REPAIR',
 'proof_source':str(BASE/'REVIEW_A008.md'),'validation':str(BASE/'out/A008_REVIEW_CHECK.json'),
 'method':'Independent physical Boolean truth tables and integer FWHT; full all-width root/binomial/actual probability chain reconstructed analytically; author code not imported',
 'reviewer_supplied_substantive_repair':False,'timestamp_utc':now})
review['status']='INDEPENDENTLY_RECONSTRUCTED_AT_STATED_SCOPE_LOCAL_ADOPTION_PENDING'
statement=('For every fixed finite nonconstant gate table and ordered support covers satisfying the forests.tex interface, '
 'positive feasible lambda, nonempty covered set A and eligible assignment tau, let V be the used gates and c its number '
 'of source SCCs in the directed ownership-incidence graph, e=|V|-c, and b_tau=2^(-B_nonroot). '
 'Put w_uv(x)=sum_{j in A_u intersect R_v}x_(u,j) for u!=v and use incoming Laplacian L_vv=sum_u w_uv, L_vu=-w_uv. '
 'Let T_tau(x)=sum_{R selecting one root in each source SCC} product_{r in R}pi_r det L_(V\\R,V\\R)(x). '
 'For the monomial map M(product x^h)=product h!, the exact sum over distinct actual once-per-gate partition-forest queue runs with this assignment is '
 'sum_r 2^(-B(A;r))=b_tau M(T_tau). Different assignments are disjoint. With T_can=T_tau(1), '
 'D_(u,j)=number of eligible child gates at attachment group (u,j), a_D=(D+1)/2 for D>=1 and a_0=1, '
 'T_can<=M(T_tau)<=min(e!T_can,T_tau(a_D)). These determinant bounds are rational for rational pi, and can be summed '
 'with the separately algebraic b_tau to bound the full optimized residual cost -log2 sum_tau b_tau M(T_tau). '
 'T_tau factors into grounded non-source SCC determinants and rarity-weighted source-SCC cofactor sums, but its factorial-moment expectation need not factor across SCCs. '
 'The e! bound is sharp on positive-mass sunflower prime-table assignments. This computes the surrogate B mass, not exact queue probabilities, and asserts no universal O(I) or FEI bound.')
hyp=['finite original forests.tex table with nonempty relevant supports, ordered covers, and strictly positive feasible fractional lambda',
 'A nonempty and covered; tau assigns each selected coordinate to an eligible gate; each used gate visited exactly once with selected subsets partitioning A',
 'exactly one root in every source SCC of the ORIGINAL directed ownership graph; no other roots',
 'initial roots and attachment-coordinate occurrences ordered deterministically by the fixed original generator; child labels at repeated attachment slots distinguish actual events',
 'B is eq:forestcost, gamma=6/5, entropy and costs in bits, F in natural logs; failed and infinite runs contribute no output mass',
 'rational determinant assertion conditional on rational rarity pi; algebraic b_tau is kept separate; no free output-dependent reference selection']
deps=[{'source':str(REPORTS/'source_material/reductions/paper/forests.tex'),
 'sha256':forest_hash,'locators':['eq:forestpacking','eq:forestcost','thm:posteriorforest','actual queue definition and source-SCC partition forests'],
 'status':'SOURCE_COMPLETE_BASELINE_READ'}]
new={'claim_id':'A006-ACTUAL-FOREST-DETERMINANT-MOMENT-BOUNDS','version':1,
 'exact_statement':statement,'hypotheses':hyp,'statement_sha256':digest(statement,hyp),
 'contributors':['A006'],'proof_source':{'path':str(BASE/'FOREST_MOMENTS.md'),'certificate':str(BASE/'out/FOREST_CHECK_3.json'),
 'sharpness':str(BASE/'out/STAR_CERTIFICATES.json')},'proof_dependencies':deps,'review_records':[],
 'status':'ANALYTICALLY_PROVED_EXACT_COMBINATORIAL_CHECKED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':['factoring factorial-moment expectation into expectations of source-SCC determinant factors, even for actual Boolean prime tables'],
 'first_unproved_line':None,'next_consumers':['B02','A008','A009','A010','A014','B03','A086','A094','B20']}
put(BASE/'CLAIMS.json',[review,new])
next_action=('Replace the off-support B_max term in A009 full-cost transfer T by the assignment-sensitive determinant-mass upper cost, '
 'retaining signed normalization and full label/rank/subset costs; prove one influence-paid expected error bound at N*2^-w comparable to one, '
 'or exhibit its first actual Boolean counterexample. Do not factor SCC expectations or rerun affine-plane FEI.')
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':BASE.name,'stream':'B02','packet_id':'A006',
 'gap_id':'G-J-COST','attempt_id':'A006-G-J-COST-003-actual-forest-determinant-moments',
 'method':'independent whole A008 proof reconstruction; exact rooted incoming-Laplacian polynomial, actual chronological child-slot bijection, factorial moments and rational determinant bounds',
 'mathematical_delta':'A008 unequal read-once forest payment v1 independently accepted without repair; arbitrary-reference fixed-assignment actual B mass computed exactly and bounded by rational canonical/weighted determinants; SCC expectation shortcut refuted on actual prime sunflower; 50,576 exact assertions passed. Universal O(I) gap retained.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'A008_WHOLE_CLAIM_ACCEPTED_LOCALLY; DETERMINANT_INTERFACE_PROVED_PENDING_REVIEW; UNIVERSAL_PIJ_AND_FULL_FEI_OPEN',
 'claim_versions_used':deps+[{'claim_id':review['claim_id'],'version':review['version'],'statement_sha256':review['statement_sha256'],'use':'whole independent review only; not a determinant theorem premise'}],
 'claims_created_or_changed':[{'claim_id':review['claim_id'],'version':review['version'],'change':'independent whole-claim review record at unchanged statement hash'},
 {'claim_id':new['claim_id'],'version':1,'change':'arbitrary-reference exact mass and computable bounds, not a universal payment candidate'}],
 'source_artifacts':['REPORT.md','FOREST_MOMENTS.md','REVIEW_A008.md','CLAIMS.json','FROZEN_SPEC.json','code/check.py','code/persist.py',
 'out/PILOT_SUMMARY.json','out/CHECK_SUMMARY.json','out/FOREST_CHECK_2.json','out/FOREST_CHECK_3.json','out/A008_REVIEW_CHECK.json','out/STAR_CERTIFICATES.json','out/SOURCES.json','out/RECEIPTS.json'],
 'next_consumers':new['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Universal influence-paid expected joint label/rank/subset cost remains unproved; exact assignment sum and moment calculation are not generally polynomial.',
 'New determinant interface independent review, supervisor adoption and mirror verification unperformed.'], 'packet_ids':['A006']}
put(BASE/'PROGRESS.json',progress); put(BASE/'PACKET_DELTA.json',progress)
old_status=(AGENT/'STATUS.md').read_text(encoding='utf-8')
put(BASE/'out/START_STATUS.json',{'stage_start_status':old_status,'scope':'saved rolling status before this stage update'})
AGENT.joinpath('STATUS.md').write_text('STATE: A006 stage 3 complete: arbitrary-reference actual forest B mass equals determinant factorial moment; rational lower/upper bounds proved; A008 unequal-block whole claim independently accepted; 50,576 exact assertions PASS; new interface review pending, FEI OPEN.\nNEXT: Replace A009 full-transfer off-support B_max by determinant-mass cost at density N*2^-w comparable to one, retaining signed normalization and all joint costs; A008/A086/A094 review the actual-run moment interface.\n',encoding='utf-8')
with AGENT.joinpath('WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+now+' stage 20261013T214427Z: Read updated BOARD, B02 v2 and saved determinant NEXT. Independently reconstructed and accepted A008 unequal-readonce v1 whole statement, no repair. Derived incoming-Laplacian source-SCC forest polynomial; actual repeated-attachment child-label orders introduce factorial moments, not abstract duplicate witnesses. Proved canonical/rational-weight determinant bounds and SCC factorization; actual Boolean sunflower star refutes factoring SCC expectations and makes e! gap sharp. Pilot 281 assertions in 0.009341 s; full 50,295 assertions in 5.220846 s over 127 tables, 3,904 ownership cases, 5,264 traces, 29 block-review cases and seven stars. All outputs saved, full FEI OPEN. NEXT is the density-sensitive full error-cost ledger, not another calibration family.\n')
with AGENT.joinpath('LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage 3 durable interface: For fixed ownership tau, incoming Laplacian minors rooted at exactly one vertex per source SCC give attached-forest polynomial T(x), weighted by root pi. Exact actual-run B mass is b_tau*M(T), where M(x^h)=product h!. Only labels within repeated-coordinate slots can be permuted; initial-root order and order between attachment coordinates are fixed. An actual event uniquely recovers ownership, so sum assignments without duplicate descriptions. T(1)<=M(T)<=min(e!T(1),T(a_D)), with e=used gates-source SCCs and a_D=(D+1)/2 for child capacity D>=1. Rational pi gives rational determinant bounds; b_tau remains algebraic. SCC polynomial factorization is valid, separate SCC expectations are not: forced two-child star gives moment 2pi versus product pi. e! gap sharp on actual sunflower prime tables. This is surrogate B mass, not q(run), and no universal O(I) follows. A008 unequal-readonce v1 full constants and actual probabilities independently reconstructed at unchanged scope.\n')
protocol=json.loads((REPORTS/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
for c in (review,new): assert set(c)==set(protocol['required_per_run']['claim_fields'])
assert set(progress)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert (BASE/'PROGRESS.json').read_bytes()==(BASE/'PACKET_DELTA.json').read_bytes()
report=(BASE/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']: assert '## '+field in report
assert report.rstrip().split('## Universal bridge\n\n')[-1].count('\n')==0
assert len(AGENT.joinpath('STATUS.md').read_text(encoding='utf-8').splitlines())==2
artifacts=[]
for path in sorted(BASE.rglob('*')):
    if path.is_file() and path.name!='RECEIPTS.json':
        data=path.read_bytes(); assert len(data)<20_000_000
        artifacts.append({'path':str(path.relative_to(BASE)),'bytes':len(data),'sha256':sha256(data).hexdigest()})
rolling=[]
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
    data=(AGENT/name).read_bytes(); rolling.append({'path':str(AGENT/name),'bytes':len(data),'sha256':sha256(data).hexdigest()})
put(BASE/'out/RECEIPTS.json',{'saved_at_utc':now,'scope':'local persistence only','artifacts':artifacts,'rolling':rolling,
 'protocol_fields':'PASS','A008_whole_review':'ACCEPT_AT_UNCHANGED_SCOPE_NO_REPAIR','new_claim_independent_review':'PENDING',
 'supervisor_upload_and_mirror':'UNOBSERVED_NOT_PERFORMED'})
print(json.dumps({'status':'PASS','saved_files':len(artifacts)+1,'max_artifact_bytes':max(a['bytes'] for a in artifacts),'run':str(BASE)},indent=2))
