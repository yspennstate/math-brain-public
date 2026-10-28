from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
assert A==Path(r'agents\A067')
PREV=A/'runs/20261023T060732Z-account03-A067-hypercontractive-refinement'
SRC=Path(r'agents\A088\runs\20261023T105519Z-account03-A088-booleanity-referee')
SRC0=SRC.parent/'20261023T070855Z-account03-A088-booleanity-referee'
def sha(b):return hashlib.sha256(b).hexdigest()
def write(name,v):
 p=R/name;assert p.resolve().is_relative_to(A.resolve());p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(v if isinstance(v,str) else json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol_path=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(protocol_path.read_text(encoding='utf-8-sig'))
sources=[]
paths=[Path(x['path']) for x in json.loads((PREV/'out/SOURCES.json').read_text())]
paths += [SRC/'PROOF.md',SRC/'CLAIMS.json',SRC0/'PROOF.md',SRC0/'CLAIMS.json',PREV/'PROOF.md',PREV/'CLAIMS.json',protocol_path]
for p in dict.fromkeys(paths):
 if p.is_file():
  b=p.read_bytes()
  try:b.decode('utf-8-sig');enc='utf-8-sig'
  except UnicodeDecodeError:enc='binary'
  sources.append({'path':str(p),'sha256':sha(b),'bytes':len(b),'encoding':enc})
write('out/SOURCES.json',sources)
sourceclaims=json.loads((SRC/'CLAIMS.json').read_text(encoding='utf-8-sig'))
selected=[x for x in sourceclaims if '71/96' in x['exact_statement']]
assert not selected,'Source schema changed: inspect actual registered theorem before adopting'
sourceproofsha=sha((SRC/'PROOF.md').read_bytes())
extracted=('For every m>=2 and every 0<=H<=T<=m, the canonical G_m edited branch queried by H complete zero-path pairs, then w, then T-H complete zero-path pairs, retaining every stopped sibling and original b_m, uses only original Q_c marginals and one original rate3. Its cumulative original-reach CE debit E_old,Q<7/48 and full terminal KL K_old<19/32, hence actual entropy debit E_old,H<71/96. With unchanged old D, r>4^-m/8 and original I_X=m+(2m+1)4^-m/2, the same diminished remaining account is r+I_X-E_old,H>m-71/96. This statement is extracted from A088 PROOF sections1--5; it has no matching registered record in that run CLAIMS.json at intake.')
sourceclaim={'claim_id':'A067-RECONSTRUCTION-A088-EARLY-W-ACCOUNT','version':1,'exact_statement':extracted,'hypotheses':['Canonical Boolean quadratic phase, marked origin and dummy w; m>=2','All0<=H<=T<=m histories exactly as primary A088 proof; both full children and every stopped terminal retained','Original fixed rate3, original Q_c marginals, signed full CE/H/KL and removed influence retained'],
 'statement_sha256':sha(extracted.encode()),'contributors':['A088: primary theorem and proof; A067: independent reconstruction without repair'],
 'proof_source':str(R/'DEPENDENCY_REVIEW.md'),'proof_dependencies':['A067-POSTCORE-BENT-FLAG-SAME-CHILD-BANK@1','A088 primary PROOF.md sha256:'+sourceproofsha],
 'review_records':[],'status':'SOURCE_PROOF_INDEPENDENTLY_RECONSTRUCTED_LOCAL_RECEIPT','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A088','A070','A094','B14','B20']}
sourceversion=sourceclaim['claim_id']+'@'+str(sourceclaim['version'])
review={'reviewer':'account03/A067','verdict':'HOLDS_AT_STATED_CANONICAL_EARLY_W_POST_W_FRONTIER_SCOPE','independent':True,'substantive_repair':False,'source':str(R/'DEPENDENCY_REVIEW.md'),'validation':str(R/'out/CHECK.json'),'method':'All-m independent source-bound reconstruction; own original truth-table restrictions, physical influences and complete original-reference frontier bills; no A088 code imported'}
sourceclaim['review_records'].append(review)
sourceclaim['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_LOCAL_RECEIPT'
write('out/DEPENDENCY_REVIEW.json',{'local_extracted_statement_id':sourceversion,'local_extracted_statement_sha256':sourceclaim['statement_sha256'],'source_path':str(SRC/'PROOF.md'),'source_proof_sha256':sourceproofsha,'registry_state':'Primary proof theorem absent from latest source CLAIMS.json; local receipt is not an adopted A088 registry record','source_claim_ids_actually_present':[x['claim_id']+'@'+str(x['version']) for x in sourceclaims],'review':review})
pilot=json.loads((R/'out/PILOT.json').read_text());main=json.loads((R/'out/CHECK.json').read_text());audit=json.loads((R/'out/INDEPENDENT_AUDIT.json').read_text())
assert all(x['status']=='PASS' for x in [pilot,main,audit])
statement=('For every Boolean quadratic phase g=(-1)^q on a finite uniform cube, with q of F2 degree<=2, let r be the rank of its alternating polar matrix. Every finite adaptive physical stopping tree has total expected complete actual entropy-drop-minus-3-influence debit at most r/4. For g equal to a product of k disjoint quadratic pairs, arbitrary disjoint characters, dummy coordinates and a global sign, the exact maximum over all such trees is k/2, attained by querying one member per pair then stopping. Every inherited reference supporting the incoming actual spectrum is marginalized only, with E_H=E_Q+weighted_terminal_KL-incoming_KL; zero off-support entries are allowed. For every m>=2 and every supplied A088 canonical early-w/post-w paid cut 0<=H<=T<=m, independently continuing ALL retained clean leaves, including original b_m, by arbitrary such trees adds actual debit F<=sum_L reach_L*k_L/2<=m/2. With all old D, removed influence J and both full CE/KL children retained, the SAME original fixed-rate3 account has remaining reserve r+I_X-E_old-F>m/2-71/96>=25/96. Neither inherited KL nor the original increment I_X is renewed. The active edited leaf remains at its supplied cut. No arbitrary edited-core supplier, higher-degree bound or full FEI is asserted.')
claim={'claim_id':'A067-QUADRATIC-BELLMAN-ALL-CLEAN-REFINEMENTS','version':1,'exact_statement':statement,
 'hypotheses':['Finite uniform Boolean signs; actual quadratic F2 phase and physical restrictions; history-dependent adaptive choices use only preceding outcomes','Rate3 fixed at original source; arbitrary finite stopping trees retain every outcome branch','Inherited Q supports actual P, may vanish off support, and is only marginalized; all terminal KL and signed banks retained','Global application uses exactly the supplied canonical A088 early-w/post-w account for m>=2; active edited branch remains unchanged'],
 'statement_sha256':sha(statement.encode()),'contributors':['account03/A067; A088 credited for the separately supplied ancestor account'],
 'proof_source':str(R/'PROOF.md'),'proof_dependencies':[sourceversion,'A067-POSTCORE-BENT-FLAG-SAME-CHILD-BANK@1'],
 'review_records':[],'status':'AUTHOR_PROVED_EXACTLY_CHECKED_INDEPENDENT_REVIEW_PENDING','supersedes':[],'refutes':[],
 'first_unproved_line':None,'next_consumers':['A088','A070','A094','A068','A066','A096','B14','B20']}
write('CLAIMS.json',[sourceclaim,claim])
nextaction='Supply and pay one edited-source restriction for a noncanonical quadratic interaction graph, using the rank/4 clean-leaf potential and SAME original reference/account; derive the changed phase moment or exhibit an exact failure before claiming extension. A088/A070/A094 review this clean-refinement closure; A068 compare overlapping-quadratic source scope.'
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B14','packet_id':'A067','gap_id':'G-R-MISMATCH-POSTCORE-UNUSED-CHILD-RESERVE','attempt_id':'A067-stage20-quadratic-Bellman-all-clean-refinements',
 'method':'Sharp adaptive stopping Bellman price from Boolean restriction structure; all-quadratic rank potential; independent reconstruction of supplied early-w/post-w source and full CE/KL transfer',
 'mathematical_delta':'ALL adaptive clean refinements of every supplied canonical paid frontier are funded from SAME diminished original rate3 account, remaining>m/2-71/96>=25/96. Exact clean maximum k/2; every quadratic phase has stopping debit<=rank/4. No logarithmic dimension factor and no arbitrary edited-core supplier. A088 ancestor allowance independently accepted without repair.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_ALL_DIMENSIONAL_PROOF_PENDING_INDEPENDENT_REVIEW_FULL_FEI_OPEN',
 'claim_versions_used':claim['proof_dependencies'],'claims_created_or_changed':[claim['claim_id']+'@1',sourceversion+' independent acceptance recorded'],
 'source_artifacts':['PROOF.md','DEPENDENCY_REVIEW.md','REPORT.md','FROZEN_SPEC.json','FROZEN_INDEPENDENT_AUDIT.json','FROZEN_QUADRATIC_EXTENSION.json','code/check.py','code/audit.py','code/finish.py','out/PILOT.json','out/CHECK.json','out/INDEPENDENT_AUDIT.json','out/DEPENDENCY_REVIEW.json','out/MATH_RECALL.txt','out/SOURCES.json','out/RECEIPTS.json'],
 'next_consumers':claim['next_consumers'],'next_action':nextaction,'stagnant_substantive_attempts':0,
 'blockers':['Independent review of new Bellman/refinement theorem pending; full FEI and arbitrary edited-core supplier open','Private supervisor adoption/mirrors unverified; no git performed','Prior disclosed outside-tree placeholder remains untouched pending explicit deletion approval; not a mathematical blocker','Brain self-care degraded: stale owner model, state of mind and latest dream excluded from mathematical evidence'],
 'packet_ids':['A067']}
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

Close the actual next unpaid step named by A088: data queries inside retained clean exits after its canonical early-w/post-w history, with the SAME diminished original account, reference and every old invoice. The result closes EVERY finite adaptive clean refinement, including the original b_m sibling, for all m>=2 and all0<=H<=T<=m. All entropies, CE and KL are in bits; actual uniform Boolean signs and physical restrictions are essential. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

Current BOARD rows A067/A070/A088/A094/A096/A097 and B14 STREAM_NOTES v2 were consumed with own STATUS/WORKLOG/LEARNED and previous run. A088 {SRC/'PROOF.md'}, sections1--5 supplies the exact already-paid account and section6 explicitly names this unpaid continuation. Its preceding {SRC0/'PROOF.md'} supplies completed-pair pricing. The latest source CLAIMS.json contains only the earlier A067 result, not this new early-w theorem. We therefore pin the primary PROOF bytes by SHA256 {sourceproofsha} and extract a clearly LOCAL reconstruction receipt {sourceversion}; no A088 registry adoption is claimed. DEPENDENCY_REVIEW.md independently reconstructs its allowance without repair; this run does not import A088 code. EXECUTION_PROTOCOL revision {protocol['revision']} sets the exact fields. Campaign indices, supplement, earlier relevant runs and paper context were read-only refreshed and pinned in out/SOURCES.json. They supply context; no new paper theorem or internet claim is invoked. Read-only math recall is saved in out/MATH_RECALL.txt; no brain write was made.

# complete derivation or exact first unsupported line

PROOF.md gives the all-dimensional derivation. A clean phase of k disjoint quadratic pairs, characters and dummy coordinates has H=2k. An intact-pair query has entropy drop2 and influence1/2, so its rate3 debit is+1/2. Character and dummy queries have debits-3 and0. Along each adaptive path at most k pairs are first hit. Therefore EVERY finite adaptive stopping tree costs at most k/2, and querying one member per pair attains equality. The bound uses no independence or future-outcome selection.

The upper bound extends to EVERY quadratic Boolean phase: autocorrelation gives a uniform squared spectrum on2^r labels, H=r, where r is the alternating polar rank. Deleting a coordinate reduces r by0 or2. Nonzero-row influences are1/2; isolated coordinates are characters or dummies. Thus r/4 is a Bellman super-solution. It is an upper bound, not necessarily attained, for overlapping interactions. The independent audit retains strict examples to prevent overclaiming equality.

At any supplied paid frontier E_old<71/96 and R_old=r+I_X-E_old>m-71/96. All retained clean leaves have weighted pair count at most m, EVEN INCLUDING original b_m. Their arbitrary simultaneous refinements add actual debit at most m/2. Hence the SAME remaining original reserve is greater than m/2-71/96>=25/96. This is an explicit new withdrawal bound. It does not reuse the original full increment after old costs.

Every query retains both full physical children and the inherited marginal Q. E_H(L)=E_Q(L)+weighted terminal KL-K_L; incoming KL is subtracted, not reset. Positive dummy CE debits with zero actual entropy cost are retained and independently checked. Legacy pricing uses J_old+J_clean; the old J_old<1/2 bound is NOT extended to new queries. Signed frontier identities are background accounting; the sharp stopping bound and its funded application are new.

The earlier stage19 remainder concerned ONE paired block; this stage uses A088's later early-w/post-w account and subtracts the new all-clean continuation cost. These are different histories, explaining the new25/96 lower margin. The first unsupported line is an edited-source supplier for noncanonical interaction phases, or comparable Bellman control beyond quadratic Boolean phases. The pure quadratic clean continuation is now closed. This is not a proof of full FEI.

# executed validation with domain, arithmetic, commands and outputs

Frozen specs preceded computation. Pilot: {pilot['checks']} exact checks, {pilot['runtime_seconds']:.6f}s, 13 clean representatives through n3 and all6 m2 supplied frontiers. Main: {main['checks']} exact checks, {main['runtime_seconds']:.6f}s; 50 clean representatives through n6, {main['unique_Bellman_truth_tables']} unique literal Bellman tables and {main['Bellman_query_edges']} query edges, all31 supplied m2,3,4 frontiers, and {main['clean_physical_query_checks']} complete inherited clean-query checks. Bellman recursion represents ALL adaptive stopping choices; the attaining trees retain every branch. The main also reconstructs full old/new reference, entropy, KL and J bills from original truth tables.

Separate direct-character/ANF audit: {audit['checks']} exact assertions, {audit['runtime_seconds']:.6f}s, all278 Boolean functions n0..3, all150 labelled quadratic phases and all44 matching-family members. It checks H=GF2 rank and optimum<=rank/4, with exact matching equality. This strengthens the first audit, which had178 checks on44 matching members; the changed count comes from adding all quadratic phases and GF2 rank certificates. No author helper, FFT or logarithm implementation is imported by this audit. All results PASS.

Commands from A067: `python -X utf8 -B runs/{R.name}/code/check.py pilot`, then the same with `full`; `python -X utf8 -B runs/{R.name}/code/audit.py`. Integer Walsh transforms, exact physical edge counts and Fraction arithmetic are used. Clean entropy and Bellman maxima are exact rationals; nonflat inherited logarithms use28-term atanh intervals with a proved rational tail. Decimal values are display only. The all-m bridge is analytic, not finite-data extrapolation. Estimated memory120MB main and25MB audit; runtimes are below frozen caps. No >300MB job, GPU, automatic dimension increase or detached process was used. No Lean certificate is claimed.

# proof dependencies and changed downstream conclusions

The supplied primary-proof allowance is independently reconstructed at its exact scope without repair; {sourceversion} and out/DEPENDENCY_REVIEW.json are LOCAL extracted-statement receipts, not adopted A088 claim versions. The missing early-w theorem in source CLAIMS.json is explicitly preserved as a registry/adoption limitation. Stage19's rate3 experiment is preserved rather than renamed. The NEW claim {claim['claim_id']}@1 awaits a different reviewer. The general quadratic potential is standalone, while the global canonical refinement application additionally needs the supplied ancestor account. A088/A070 no longer need to stop at the first retained-clean data query for this supplied source. Arbitrary edited-core admission, higher-degree phases and the universal FEI target remain open.

# one next mathematical action and independent reviewer

{nextaction}

# actual persistence receipts or precise save blocker

All run files and code/outputs are local under A067. code/finish.py checks the protocol field sets, statement hashes, PACKET_DELTA equality, two-line STATUS and per-file20MB cap; out/RECEIPTS.json pins the actual bytes. WORKLOG and LEARNED record this result and the precise next supplier gap. Source trees and other agents' outputs are unchanged. Private supervisor adoption and mirrors remain unverified. The prior disclosed outside-tree placeholder remains untouched pending cleanup approval. Brain self-care is degraded/unverified: the owner model, state of mind and latest dream are stale, and none is mathematical evidence. All launched stage commands will be allowed to complete; no work is intentionally left running at handoff.

# Universal bridge

C019 stopping-tree payment, with C024 full inherited-reference transfer, now covers ALL adaptive clean refinements after every supplied canonical early-w/post-w frontier, at the SAME original rate3 and with remaining reserve>25/96. The new all-quadratic rank/4 potential removes any logarithmic dimension or degree payment in this clean regime, while explicitly retaining positive source invoices and full terminal KL. What remains is the original-source/phase supplier for an EDITED noncanonical Boolean core and a higher-degree analogue of the Bellman potential. Moving to overlapping quadratic interactions with this clean continuation already discharged directly tests that universal supplier, rather than producing another isolated class H/I estimate.
'''
write('REPORT.md',report)
status='STATE: Stage20: ALL adaptive clean refinements PAID from SAME original rate3, remainder>25/96; quadratic stopping<=rank/4; matching exact k/2;9708 main checks PASS; new review pending; FEI OPEN.\nNEXT: Noncanonical edited quadratic source/profile with SAME old D/J/reference/reserve; clean rank/4 payment now available; A088/A070/A094 review, A068 compare.\n'
(A/'STATUS.md').write_text(status,encoding='utf-8')
entry=f'''\n## 2026-10-23 stage20, account03 (run {R.name})
Read new BOARD/A088 stage20; did not repeat its all-pair/early-w work. Independently reconstructed supplied account E_old<71/96 without repair. NEW: all finite adaptive clean restrictions cost exactly k/2 at most (matching phases attain); intact query+1/2, character-3,dummy0. General quadratic Boolean phase upper bound rank/4 follows from flat spectrum H=polar rank and coordinate rank drop0/2. ALL clean descendants including original b_m add<=m/2, leaving SAME original reserve>m/2-71/96>=25/96 after old costs. Full incoming/terminal KL carried, no clipping/reset; positive dummy CE guard retained. Main{main['checks']} plus separate{audit['checks']} exact checks PASS; all278 n<=3 functions filtered to150 quadratic phases,44 matching members; main31 inherited frontiers and50 clean representatives. New theorem awaits independent review; full FEI OPEN. NEXT is noncanonical EDITED source supplier, not another clean query or transport identity. Personal brain wake degraded (three stale sources) excluded from mathematics. Prior outside-tree placeholder remains untouched pending approval.
'''
for name in ['WORKLOG.md','LEARNED.md']:
 with (A/name).open('a',encoding='utf-8') as f:f.write(entry)
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert all(set(c)==set(protocol['required_per_run']['claim_fields']) for c in [sourceclaim,claim])
assert all('# '+x in report for x in protocol['required_per_run']['report_fields'])
assert json.loads((R/'PROGRESS.json').read_text())==json.loads((R/'PACKET_DELTA.json').read_text())
assert len((A/'STATUS.md').read_text().splitlines())==2
receipts=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='RECEIPTS.json':
  b=p.read_bytes();assert len(b)<20_000_000;receipts.append({'path':str(p.relative_to(R)),'sha256':sha(b),'bytes':len(b)})
write('out/RECEIPTS.json',{'status':'PASS','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'schema_checks':'exact field sets, hashes, compatibility, sizes, two-line STATUS PASS','artifacts':receipts,'new_claim_sha256':claim['statement_sha256'],'independent_review':'NEW CLAIM PENDING; supplied ancestor locally accepted','mirror_status':'UNVERIFIED_SUPERVISOR_OWNED','brain_selfcare':'DEGRADED_UNVERIFIED_PERSONAL_CONTEXT_EXCLUDED'})
print(json.dumps({'status':'PASS','sources_read':len(sources),'receipt_count':len(receipts),'claim':claim['claim_id']+'@1','new_statement_sha256':claim['statement_sha256'],'source_reviewed':sourceversion,'main_checks':main['checks'],'independent_checks':audit['checks']}))
