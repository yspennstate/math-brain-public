import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1];A=R.parents[1];ROOT=A.parents[1]
peer=ROOT/'agents/A067/runs/20261023T120754Z-fleet03-A067-hypercontractive-refinement'
old=A/'runs/20261023T105519Z-fleet03-A088-booleanity-referee'
def read(p):return p.read_text(encoding='utf-8')
def write(p,s):
 with p.open('w',encoding='utf-8',newline='\n') as f:f.write(s)
def js(p,x):write(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
check=json.loads(read(R/'out/CHECK.json'));pilot=json.loads(read(R/'out/PILOT.json'))
assert check['status']==pilot['status']=='PASS'
assert check['quadratic_cases']==1098
assert F(check['m2_min_reserve_lower'])>F(13,96)

# Stronger non-Boolean scope diagnostic, exact rational complex arithmetic.
values=[(F(1),F()),(F(3,5),F(4,5))]
coeff=[tuple((values[0][j]+s*values[1][j])/2 for j in (0,1)) for s in (1,-1)]
p=[x*x+y*y for x,y in coeff]
energy=sum((values[0][j]-values[1][j])**2 for j in (0,1))/4
assert all(x*x+y*y==1 for x,y in values) and p==[F(4,5),F(1,5)] and energy==F(1,5)
assert 5**5>2**11
js(R/'out/COMPLEX_SCOPE.json',{'status':'PASS','checks':4,'unimodular_values':['1','(3+4i)/5'],'squared_spectrum':[str(x) for x in p],'physical_energy':str(energy),'both_child_squared_norms':[1,1],'actual_rate3_debit':'log2(5)-11/5 > 0','exact_sign_certificate':'5^5=3125 > 2^11=2048','scope':'Generic 2-bit query bound survives; binary quadratic rank-zero free payment does not extend to arbitrary complex phases.'})

sourceclaims=json.loads(read(peer/'CLAIMS.json'))
review=next(c for c in sourceclaims if c['claim_id']=='A067-QUADRATIC-BELLMAN-ALL-CLEAN-REFINEMENTS')
observed=hashlib.sha256(review['exact_statement'].encode('utf-8')).hexdigest()
assert observed==review['statement_sha256']
review['review_records'].append({'reviewer':'fleet03/A088','verdict':'HOLDS_AT_STATED_QUADRATIC_AND_SUPPLIED_ANCESTOR_SCOPE','independent':True,'substantive_repair':False,'source':str(R/'PROOF.md'),'validation':str(R/'out/CHECK.json'),'method':'Own polar-matrix rank elimination and literal Walsh spectra for all quadratic phases n<=4; independent all-dimensional rank potential reconstruction. A088 authored the separate original source; this is not a second review of that source.'})
review['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_LOCAL_RECEIPT'
statement='For every m>=2, use the original canonical G_m account with fixed original rate3, old z debit D and original Q_b,Q_c. After H completed edited zero-path pairs then w,0<=H<=m, query any permutation of the remaining data coordinates on the surviving edited zero path, stopping at any prefix and retaining all one-children. Arbitrary finite adaptive physical continuations of every clean terminal, including original b_m and all old clean siblings, are paid from the same diminished original account with remaining reserve >13/96. The additional edited-path actual debit is <=(1-4^{-(m-H)})/(2*4^H); total clean continuation debit is <=sum_L reach_L*k_L/2<=m/2. For m>=3 and for m=2,H>=1 the bound is analytic; all71 m=2 ordered prefixes are certified by exact rational logarithm intervals. All references are original marginals, both full CE/KL terminals and all removed influence invoices remain. No constant bound on the new full KL is asserted: the original clean b_m sibling alone can contribute m/2. This is a canonical matching-quadratic one-defect continuation, not an arbitrary edited-core or full FEI theorem.'
new={'claim_id':'A088-ARBITRARY-ORDER-EDITED-ZERO-SPINE-SAME-SOURCE','version':1,'exact_statement':statement,'hypotheses':['Finite uniform Boolean canonical matching quadratic with one origin edit; m>=2','Original A067/A088 ancestor account, fixed rate3 chosen once; same diminished r+I_X-E, old D and all actual removed influence retained','Only edited zero path continued; every stopped one-child retained and clean continuations arbitrary finite adaptive physical trees','Original references only marginalized; every full terminal CE and KL retained; no reset or new supply'], 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['fleet03/A088; A067 credited for independently reconstructed sharp clean quadratic stopping lemma'],'proof_source':str(R/'PROOF.md'),'proof_dependencies':['A067-QUADRATIC-BELLMAN-ALL-CLEAN-REFINEMENTS@1','A067-RECONSTRUCTION-A088-EARLY-W-ACCOUNT@1','A067-POSTCORE-BENT-FLAG-SAME-CHILD-BANK@1'],'review_records':[],'status':'AUTHOR_PROVED_EXACTLY_CHECKED_INDEPENDENT_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A067','A070','A094','A066','A096','B18','B20']}
js(R/'CLAIMS.json',[review,new])
now=datetime.now(timezone.utc).isoformat()
sources=[peer/'PROOF.md',peer/'CLAIMS.json',old/'PROOF.md',old/'PROGRESS.json',A/'runs/20261023T070855Z-fleet03-A088-booleanity-referee/code/check.py',ROOT/'BOARD.md',ROOT/'claude/B18/STREAM_NOTES.md']
js(R/'out/SOURCES.json',{'read_at':now,'bindings':[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources],'note':'BOARD is live; hash is an intake binding rather than a claim of a frozen board. No peer files modified.'})
total=check['checks']+4
nextaction='A067/A070/A094 review arbitrary-order edited zero-spine extension. Replace matching quadratic by an overlapping edited quadratic while proving its ACTUAL original source allowance and physical influence price; keep same old D/J/reference and both full terminal bills. Clean rank/4 continuation already available; arbitrary-core supplier remains open.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B18','packet_id':'A088','gap_id':'C019-EXCLUSIVE-TERMINAL-CORE-SLACK-FOR-SHARED-REFERENCE','attempt_id':'A088-arbitrary-order-edited-zero-spine-v1','method':'Independent clean rank/Bellman audit; generic normalized-child entropy decomposition; exact edited influences and discounted first/second-member exchange argument; rational endpoint certificate and real/complex phase diagnostics','mathematical_delta':f'A067 quadratic clean-payment theorem independently HOLDS unchanged. NEW arbitrary edited coordinate orders and prefixes after early w, plus ALL adaptive clean refinements, funded SAME original rate3 with reserve >13/96. Full terminal KL may grow at least m/2 and is included. {total} exact main/scope predicates PASS; new extension review pending; full FEI OPEN.','deliverable_status':'COMPLETE_LOCAL_SOURCE_BOUND_HANDOFF','mathematical_status':'SCOPED_A067_REVIEW_ACCEPTED_NEW_CANONICAL_CONTINUATION_AUTHOR_PROVED_PENDING_REVIEW_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256'],'status':c['status']} for c in [sourceclaims[0],review]],'claims_created_or_changed':[{'claim_id':review['claim_id'],'version':1,'change':'independent HOLDS review without repair'},{'claim_id':new['claim_id'],'version':1,'change':'narrow same-source continuation proved; external review pending'}],'source_artifacts':[str(p) for p in sources[:5]]+[str(R/'PROOF.md'),str(R/'out/CHECK.json'),str(R/'out/COMPLEX_SCOPE.json')],'next_consumers':new['next_consumers'],'next_action':nextaction,'stagnant_substantive_attempts':0,'blockers':['Arbitrary edited-core original supplier and full FEI OPEN','New arbitrary-order source continuation awaits independent external review','Supervisor mirror/adoption unverified; no git authorized','Brain self-care degraded/unverified: stale owner-model, state-of-mind and dream sources not used'],'packet_ids':['A088']}
js(R/'PROGRESS.json',progress);js(R/'PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

Audit A067-QUADRATIC-BELLMAN-ALL-CLEAN-REFINEMENTS@1 unchanged, then extend the same original canonical account to every data-coordinate order on its edited zero path after early w, with every prefix and all adaptive clean continuations. Uniform Boolean signs, bits, fixed original rate3, original Q marginals and all signed full terminals. Quantifiers and proof are in PROOF.md; no arbitrary-core or full FEI claim.

# sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL revision2026-10-11-execution-v2; current BOARD, B18 STREAM_NOTES v2, own stage20 STATUS/PROGRESS and prior proof/helper chain; A067 run20261023T120754Z PROOF sections1--4 and CLAIMS. Source hashes are in out/SOURCES.json. The current BOARD clean-payment dependency supersedes the stale lead's already-closed baseline dispatch. Original campaign and paper context is inherited from earlier stages, not newly represented as reread here.

# complete derivation or exact first unsupported line

PROOF.md gives the complete scoped derivation. A067's rank/4 Bellman bound and all-clean same-source application HOLDS without repair. For the new edited zero path, entropy loss<=2 and exact influences price first pair members by1/2 and exposed partners by2. A discounted exchange proves original-reach debit<=(1-4^-(m-H))/(2*4^H) for EVERY order and prefix. Adding all clean forests costs at mostm/2. The all-m source payment has reserve>13/96; the only exceptional endpoint m=2,H=0 is closed by exact exhaustive certificate, not floating evidence. The first unsupported universal line is an actual original source/influence allowance for arbitrary edited cores.

Generic two-bit query entropy transport survives complex unit-modulus phases. Binary quadratic stopping payment does not: [1,(3+4i)/5] has debit log2(5)-11/5>0, with both child norms1. The real isospectral [0,0,0,-2] diagnostic instead fails child normalization. No Boolean counterexample to FEI is claimed.

# executed validation with domain, arithmetic, commands and outputs

Frozen SPEC.json precedes the searches. Commands: `python -X utf8 -B code/check.py pilot` and `python -X utf8 -B code/check.py main`, executed from this run via their full relative run paths. Pilot: {pilot['checks']} predicates PASS, {pilot['runtime_seconds']:.3f}s. Main: {check['checks']} predicates PASS, {check['runtime_seconds']:.3f}s; all {check['quadratic_cases']} quadratic phases n=1..4 modulo output sign only; {check['literal_frontiers']} literal original-reference frontiers, including all71 distinct m=2 ordered prefixes and three prespecified orders for m=3,4. Larger-m all-order coverage comes from the analytic proof, not sampled orders. Exact Fraction Walsh spectra and F2 elimination; logarithms use28-term atanh with proved rational tail and outward2^-90 bounds. Additional4 exact complex diagnostic predicates PASS. Memory estimate100MB; no heavy job or dimension escalation. out/CHECK.json and out/COMPLEX_SCOPE.json contain certificates. No test failures occurred; a preliminary inline source-read command had shell quoting failure and was replaced by ordinary reads.

# proof dependencies and changed downstream conclusions

CLAIMS.json carries A067's exact version/hash with a local independent HOLDS review, plus the new narrow canonical continuation pending review. A067 independently reviewed the supplied A088 ancestor source; A088 does not claim independent acceptance of its own original proof. Dependencies are acyclic. Old allowance71/96 is an incoming-cut bound; after the new continuations FULL KL need not stay<19/32. A clean Boolean sibling alone contributesm/2 KL, while actual debit ism/4. All old D and actual removed-influence J remain; neither an old J<1/2 bound nor I_X supply is renewed.

# one next mathematical action and independent reviewer

{nextaction}

# actual persistence receipts or precise save blocker

All four protocol files, PROOF.md, frozen spec, scripts and rational outputs are saved in this run; rolling STATUS/WORKLOG/LEARNED updated. out/PERSISTENCE_RECEIPTS.json records schema/readback/hash/size checks. Only A088 research paths were written. Supervisor copy/adoption remains unverified; no git, peer messages or brain writes were performed for these research outputs. Brain self-care remains degraded/unverified: owner-model99.2h, state-of-mind83.8h, latest dream34.5h stale at wake; none supplies mathematical premises. The checklist working update failed with a lock timeout; it does not affect the saved mathematical certificates.

# Universal bridge

This moves C019 stopping-tree payment and C024 history transfer beyond completed-pair schedules: EVERY edited data order and prefix after early w, and all adaptive clean descendants, are paid from the SAME original diminished account with>13/96 remaining. A067's clean supplier is independently accepted, and growing full terminal KL is explicitly paid. The surviving obstruction is an actual original supplier for noncanonical edited quadratic or arbitrary cores, rather than transport bookkeeping. Testing the overlapping edited quadratic source next changes the source geometry while reusing the accepted clean rank lemma, making it the shortest nearby route toward the universal gap rather than another isolated H/I class bound.
'''
write(R/'REPORT.md',report)
write(A/'STATUS.md',f'STATE: A088 stage21: A067 clean rank/payment independently HOLDS; ANY edited data order after early w + ALL clean forests SAME original rate3 leaves>13/96; {total} exact checks PASS; new review pending; FEI OPEN.\nNEXT: {nextaction}\n')
for filename,text in [('WORKLOG.md',f'{now} stage21: Read current board; consumed A067 all-clean dependency rather than duplicating it. Independently reconstructed rank/4 proof; exact all1098 n<=4 quadratics. New discounted exchange pays every edited order/prefix after early w; all71 m2 endpoints exact; arbitrary clean forests same account>13/96. Main/scope {total} PASS; pilot {pilot["checks"]} PASS separately. New source continuation pending A067/A070/A094 review; full FEI open.'),('LEARNED.md','Stage21 durable: For any Boolean query, entropy loss=conditional spectral-bit entropy+JS(two child spectra)<=2; this also holds complex-unimodular and by itself uses no binary phase. Matching origin-edited zero-spine influences are .5+2eta on first members and2eta on exposed partners. Discounted surrogate prices .5,2 are maximized by adjacent pairs, totaling<=2(1-4^-k) times incoming reach. This pays arbitrary post-w query orders with all clean Bellman forests from the same original source, reserve>13/96 (m2 exact endpoint). New full KL can grow>=m/2, so the old19/32 cap is not hereditary. Complex values[1,(3+4i)/5] have both child norms1 and positive rate3 debit log2(5)-11/5, proving discrete binary phase is essential to clean rank-zero free payment. Arbitrary edited-core supplier remains open.')]:
 p=A/filename;before=read(p) if p.exists() else ''
 marker='stage21:' if filename=='WORKLOG.md' else 'Stage21 durable:'
 if marker not in before:write(p,before.rstrip()+'\n\n'+text+'\n')

protocol=json.loads(read(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')))
required=protocol['required_per_run'];claims=json.loads(read(R/'CLAIMS.json'))
assert all(set(c)==set(required['claim_fields']) for c in claims)
expected=[s.split(' (')[0] for s in required['progress_fields']]
assert set(progress)==set(expected)
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert all('# '+s in report for s in required['report_fields'])
assert len(read(A/'STATUS.md').splitlines())==2
receipts=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
  assert p.stat().st_size<20_000_000
  if p.suffix in ['.json','.py','.md']:read(p)
  if p.suffix=='.json':json.loads(read(p))
  receipts.append({'relative_path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size})
js(R/'out/PERSISTENCE_RECEIPTS.json',{'status':'PASS','saved_at':now,'protocol_exact_fields':True,'packet_delta_byte_identical':True,'rolling_status_two_lines':True,'research_write_scope':str(A),'mirror_adoption':'UNVERIFIED_SUPERVISOR_OWNED','files':receipts})
print(json.dumps({'status':'PASS','main_and_scope_checks':total,'new_reserve_bound':'13/96','claims':len(claims),'files_verified':len(receipts),'full_fei':'OPEN'}))
