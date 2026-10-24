from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
BASE=Path(__file__).resolve().parents[1]; AGENT=BASE.parents[1]; TEAM=AGENT.parents[1]
REPORTS=Path('~/mop_fei100/reports/fei-2026-10-11')
A008=TEAM/'agents/A008/runs/20261013T222820Z-account05-A008-gate-label-compression'
A009=TEAM/'agents/A009/runs/20261013T235139Z-account05-A009-fractional-incidence-optimization'
A010=TEAM/'agents/A010/runs/20261014T001430Z-account05-A010-universal-residual-falsifier'
A014=TEAM/'agents/A014/runs/20261013T235200Z-account05-A014-overlap-beyond-worst-case-read'
def put(path,obj): path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(statement,hyp): return sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
sources=[]
pairs=[(TEAM/'BOARD.md','full initial board and middle reread; hash is final-save bytes of mutable board'),
 (TEAM/'claude/B02/STREAM_NOTES.md','full v2, 2026-10-11 23:35 UTC'),
 (REPORTS/'EXECUTION_PROTOCOL.json','full revision 2026-10-11-execution-v2'),
 (REPORTS/'source_material/reductions/paper/forests.tex','original queue/support/subset/root-conditioning definition revisited; complete prior baseline read retained'),
 (A008/'REPORT.md','full stage3 report'),(A008/'COMPLETE_MASS.md','full degree operator/probability representation/proof and false auxiliary singleton sentence'),
 (A008/'CLAIMS.json','full source claims and unchanged formal statement hash'),
 (A009/'REPORT.md','full stage3 report; matching coverage defect and complete cost interface'),
 (A009/'MATCHING_CERTIFICATE.md','full actual matching proof and all-graph mass formula; not wholesale independent review'),
 (A010/'REPORT.md','full stage3 report; independent/non-independent sector boundary'),
 (TEAM/'agents/A010/STATUS.md','latest directions'),(A014/'REPORT.md','full stage3 report; conditioned remainder substitution false')]
for path,scope in pairs:
    data=path.read_bytes(); sources.append({'path':str(path),'scope':scope,'sha256':sha256(data).hexdigest(),'bytes':len(data)})
put(BASE/'out/SOURCES.json',sources)
forest_hash=next(s['sha256'] for s in sources if s['path'].endswith('forests.tex'))
review=next(c for c in json.loads((A008/'CLAIMS.json').read_text(encoding='utf-8')) if c['claim_id']=='A008-COMPLETE-QUEUE-DEGREE-WEIGHTED-DETERMINANT-MASS')
assert digest(review['exact_statement'],review['hypotheses'])==review['statement_sha256']
review['review_records'].append({'reviewer':'A006','verdict':'FORMAL_STATEMENT_HOLDS_AT_UNCHANGED_SCOPE_WITH_AUXILIARY_SOURCE_ERROR',
 'proof_source':str(BASE/'REVIEW_A008.md'),'validation':str(BASE/'out/A008_OPERATOR_REVIEW.json'),
 'method':'Independent full root/count/multiset/child-slot probability reconstruction and integer moment proof; no author code imported',
 'reviewer_supplied_substantive_repair_to_formal_claim':False,
 'auxiliary_error':{'source':str(A008/'COMPLETE_MASS.md'),'locator':'Exact sharp separation, sentence In (1), each t_u=1/2 (uniform singleton choice)',
 'verdict':'ERROR','counterexample':'width-two gate with both endpoint orders has size-one subset draw t=1/4 exactly; any cover gives t<1/2',
 'formal_claim_affected':False,'dependent_evaluations':'Any complete q evaluation substituting t=1/2 must be recomputed; A009 uses correct 1/4 and is unaffected'},
 'timestamp_utc':now})
review['status']='FORMAL_CLAIM_INDEPENDENTLY_ACCEPTED_LOCALLY_AUXILIARY_SOURCE_ERROR_RECORDED_ADOPTION_PENDING'
statement=('For every finite nonempty simple graph G on its covered coordinates, f_G the positive edge-conjunction union, '
 'both fixed endpoint orders per width-two prime gate, pi_e=1/4 and any globally fixed strictly positive feasible lambda_e, '
 'put D=product_e(1+lambda_e/4)-1 and r_u=sum_{v neighbor u}lambda_uv. For every covered nonempty A and every inclusion-maximal matching M in G[A], '
 'let U=A\\V(M). For each choice of a neighbor nu(u) for all u in U, use matching edge gates owning their endpoint pairs, '
 'singleton gates {u,nu(u)} owning u as a child at nu(u) if matched or an isolated root otherwise. Let b count outside-A choices and '
 'h_v,h_w count child attachments at endpoints of matching edge e={v,w}, c_e=h_v+h_w. These form distinct actual source-SCC partition queue events. '
 'Their exact complete conditioned output mass Q_M(A) equals D^-1 product_{e in M}(lambda_e/24) times '
 'sum_nu[product_{u in U}(lambda_{u,nu(u)}/8)*4^(-b)*product_{e={v,w} in M} h_v!h_w!/((c_e+1)^2*(c_e+2))]. '
 'Different M and neighbor/chronological choices are disjoint actual events. Q_MS=sum_maximal_M Q_M is positive for every covered nonempty A '
 'and is an output subprobability <=Q_part<=Q_*. Each Q_M is at least D^-1*48^(-(|M|+|U|))*product_{e in M}lambda_e*product_{u in U}r_u. '
 'Normalized posterior q(r)/Q_MS retains final-output witness entropy. Exact rational log intervals certify C_MS=sum_nonempty P_f(A)log2(1/Q_MS(A))<5I(f_G) '
 'for all 63 nonempty labelled graph tables on four variables at each of lambda_e=1/maximum_degree and lambda_uv=1/(degree(u)+degree(v)). '
 'The mass and lower bound cover every finite graph and feasible weight vector, but no dimension-independent influence payment is claimed.')
hyp=['uniform independent physical signs; positive conjunction for every edge of a finite nonempty simple graph; variables outside covered coordinates omitted',
 'gate table, both full endpoint orders, pi=1/4 and strictly positive fractional lambda fixed once from f before sampling A',
 'each selected subset owns either a matched pair or an unmatched singleton, subsets partition A and every used gate visited once',
 'matchings inclusion-maximal; chronological permutations only within repeated attachment slots, not initial roots or different coordinates',
 'complete original conditioned queue law, including absent-root normalization, size/subset/count/multiset probabilities and all label draws; failed/infinite runs omitted',
 'ideal output cross-entropy in bits, no uncharged prefix-rounding/selector costs; n=4 cost theorem is finite only, not extrapolated']
deps=[{'source':str(REPORTS/'source_material/reductions/paper/forests.tex'),'sha256':forest_hash,
 'locators':['original queue and subset definitions','eq:forestconditioning','source-SCC partition runs','thm:posteriorforest'],
 'status':'SOURCE_COMPLETE_BASELINE_READ'},
 {'claim_id':review['claim_id'],'version':review['version'],'statement_sha256':review['statement_sha256'],
 'status':'FORMAL_STATEMENT_INDEPENDENTLY_RECONSTRUCTED_UNCHANGED_WITH_NONESSENTIAL_AUX_SOURCE_ERROR',
 'use':'complete-mass interface; star formula also derived directly from original queue'}]
new={'claim_id':'A006-MAXIMAL-MATCHING-STAR-COMPLETE-MASS','version':1,'exact_statement':statement,'hypotheses':hyp,
 'statement_sha256':digest(statement,hyp),'contributors':['A006'],
 'proof_source':{'path':str(BASE/'STAR_COMPLETION.md'),'trace_certificate':str(BASE/'out/CHECK_4.json'),'cost_certificate':str(BASE/'out/COST_4.json')},
 'proof_dependencies':deps,'review_records':[],'status':'ANALYTIC_ARBITRARY_GRAPH_MASS_PROVED_EXACT_FINITE_COST_CERTIFIED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,
 'next_consumers':['B02','A008','A009','A010','A014','A015','B03','A086','A094','B20']}
put(BASE/'CLAIMS.json',[review,new])
next_action=('Pay the non-independent graph spectral expectation of matched-root label and unmatched row-mass costs with one fixed feasible vector, '
 'combining A010 local incidence cancellation and exact maximal-matching star factorial credit; prove one normalized full-cost inequality or its exact actual-Boolean obstruction. '
 'Higher-width transfer requires an explicit substitute for unmatched independence. A008/A009/A086/A094 review.')
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':BASE.name,'stream':'B02','packet_id':'A006','gap_id':'G-J-COST',
 'attempt_id':'A006-G-J-COST-004-maximal-matching-star-completion',
 'method':'independent complete-probability operator review; maximal matching leaves independent unmatched vertices; exact disjoint rooted-star queue events; rational mass/lower bound and logarithm intervals',
 'mathematical_delta':'Arbitrary graph matching-sector coverage defect closed by complete actual maximal-matching star mass; all 104 old n=4 positive-spectrum zero masses rescued; finite C_MS<5I at two fixed vectors certified. A008 formal complete-mass v1 independently HOLDS, nonessential source t=1/2 error isolated. 35,943 passing assertions; universal influence payment OPEN.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT',
 'mathematical_status':'ARBITRARY_GRAPH_COVERAGE_AND_MASS_PROVED_PENDING_REVIEW; A008_FORMAL_STATEMENT_ACCEPTED_WITH_AUX_SOURCE_ERROR; UNIVERSAL_PIJ_AND_FEI_OPEN',
 'claim_versions_used':deps,
 'claims_created_or_changed':[{'claim_id':review['claim_id'],'version':review['version'],'change':'unchanged formal statement independent review with scoped auxiliary source error'},
 {'claim_id':new['claim_id'],'version':1,'change':'new arbitrary-graph actual complete output mass and computable lower bound; finite cost certificate, not universal payment'}],
 'source_artifacts':['REPORT.md','STAR_COMPLETION.md','REVIEW_A008.md','CLAIMS.json','FROZEN_SPEC.json','COST_SPEC.json',
 'code/check.py','code/cost.py','code/persist.py','out/CHECK_3.json','out/CHECK_4.json','out/A008_OPERATOR_REVIEW.json',
 'out/COST_3.json','out/COST_4.json','out/SOURCES.json','out/RECEIPTS.json'],
 'next_consumers':new['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Dimension-independent expected matched-root label and unmatched row-mass payment unproved; maximal-matching star decomposition not extended to wider prime tables.',
 'New mass interface independent review, supervisor adoption/mirror copying unperformed; auxiliary t evaluation correction awaits source owner.'],
 'packet_ids':['A006']}
put(BASE/'PROGRESS.json',progress);put(BASE/'PACKET_DELTA.json',progress)
put(BASE/'out/START_STATUS.json',{'prior_status':(AGENT/'STATUS.md').read_text(encoding='utf-8'),'scope':'rolling status read before this stage update'})
AGENT.joinpath('STATUS.md').write_text('STATE: A006 stage 4 complete: arbitrary graph maximal-matching star queue mass positive on every covered set; all 104 n4 missing matching sectors rescued; full C_MS<5I certified at two vectors; A008 formal mass HOLDS with auxiliary t=1/2 error isolated; 35,943 checks PASS; new claim review pending, FEI OPEN.\nNEXT: Pay non-independent graph expected matched-root label/unmatched row-mass costs via A010 incidence cancellation and exact star factorial posterior; A008/A009/A086/A094 review mass and scoped t correction; wider-prime decomposition remains open.\n',encoding='utf-8')
with AGENT.joinpath('WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+now+' stage 20261014T011124Z: Consumed updated BOARD/B02 and A008/A009/A010/A014 sources. Independently reconstructed A008 complete formal mass v1; found auxiliary star t=1/2 source sentence false, with exact t=1/4 two-order counterexample, formal claim unaffected. Derived arbitrary-graph maximal-matching completion: unmatched vertices independent, attached to matching gates or external singleton roots; exact full child/multiset/chronological mass and 48-based lower bound. All 104 positive-spectrum zero-matching sectors at n4 rescued. Pilot/full exact traces 1577/32744 assertions in .043153/.641297s; separate rational costs 96/1526 assertions in 3.190150/1.054275s, C_MS<5I for all 63 graphs at two fixed vectors. Full FEI OPEN; next is expectation payment, not coverage or another known-class calibration.\n')
with AGENT.joinpath('LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage 4: For any graph prime table with both endpoint orders, t(singleton)=1/4 and t(pair)=1/6. Every inclusion-maximal matching M in G[A] leaves independent unmatched U, so choosing a neighbor for each u creates only matching-root stars and external singleton roots. Complete mass Q_M is D^-1 product_M(lambda/24) times sum_choices product_U(lambda/8)*4^-external*product_M[h_v!h_w!/((c+1)^2(c+2))]. Ownership recovers M and neighbors, so all events are distinct. Q_MS=sum_M Q_M>0 on every covered A; lower Q_M>=D^-1 48^(-(|M|+|U|)) product_M lambda product_U row_mass. This closes matching coverage but not universal expected label/row cost. All104 n4 matching failures rescued; rational intervals certify C_MS<5I for both fixed vectors, finite only. A008 complete formal mass v1 holds, but its auxiliary each t_u=1/2 uniform singleton sentence is false: actual singleton subset includes probability of choosing among two coordinates; one-order t is theta/[2*(1+2^-gamma)], not1/2. Ns star coefficient and formal identity do not depend on that error.\n')
protocol=json.loads((REPORTS/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
for c in [review,new]: assert set(c)==set(protocol['required_per_run']['claim_fields'])
assert set(progress)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert (BASE/'PROGRESS.json').read_bytes()==(BASE/'PACKET_DELTA.json').read_bytes()
report=(BASE/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']: assert '## '+field in report
assert report.rstrip().split('## Universal bridge\n\n')[-1].count('\n')==0
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
artifacts=[]
for p in sorted(BASE.rglob('*')):
    if p.is_file() and p.name!='RECEIPTS.json':
        data=p.read_bytes();assert len(data)<20_000_000
        artifacts.append({'path':str(p.relative_to(BASE)),'bytes':len(data),'sha256':sha256(data).hexdigest()})
rolling=[]
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
    data=(AGENT/name).read_bytes();rolling.append({'path':str(AGENT/name),'bytes':len(data),'sha256':sha256(data).hexdigest()})
put(BASE/'out/RECEIPTS.json',{'saved_at_utc':now,'scope':'local persistence only','artifacts':artifacts,'rolling':rolling,
 'protocol_fields':'PASS','A008_review':'FORMAL_CLAIM_HOLDS_AT_UNCHANGED_SCOPE_WITH_NONESSENTIAL_SOURCE_ERROR',
 'new_mass_independent_review':'PENDING','supervisor_upload_mirror':'UNOBSERVED_NOT_PERFORMED'})
print(json.dumps({'status':'PASS','saved_files':len(artifacts)+1,'max_artifact_bytes':max(a['bytes'] for a in artifacts),'run':str(BASE)}))
