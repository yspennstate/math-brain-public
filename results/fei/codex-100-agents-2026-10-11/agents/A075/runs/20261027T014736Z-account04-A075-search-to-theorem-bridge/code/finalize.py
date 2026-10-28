from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]
A=R.parents[1]
W=A.parents[1]
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
main=load(R/'out/MAIN.json');pilot=load(R/'out/PILOT.json');boundary=load(R/'out/BOUNDARY.json');audit=load(R/'out/AUDIT.json')
signs=load(R/'out/SOURCE_SIGNS.json');assert signs['status']=='PASS'
formal=load(R/'out/FORMAL.json') if (R/'out/FORMAL.json').exists() else {'status':'NOT_COMPLETED','reason':'Compiler receipt absent; no Lean claim.'}
(R/'PROOF.md').write_text((R/'DERIVATION.md').read_text(encoding='utf-8'),encoding='utf-8',newline='')
source=W/'agents/A071/runs/20261023T135901Z-account03-A071-search-space-design'
src=load(source/'CLAIMS.json')
claims=src if isinstance(src,list) else src.get('claims',[])
source_claim=next(c for c in claims if c['claim_id']=='A071-PRIME-BALL-PROPER-PARTITION-OBSTRUCTION')
review={'reviewer':'A075','date':now,'verdict':'ACCEPT_UNCHANGED','independence':'Own direct physical matrix groups and character sums, plus complete analytic reconstruction','source_statement_sha256':source_claim['statement_sha256'],'source_claims_sha256':digest(source/'CLAIMS.json'),'source_proof_sha256':digest(source/'PROOF.md'),'scope':'All n>=3, all proper disjoint Boolean partitions, every K>=0; zero discount; H/I limit4; explicit H<5I; not FEI resolution','artifact':'REVIEW.md'}
save(R/'out/INDEPENDENT_REVIEW.json',review)
(R/'REVIEW.md').write_text('A071-PRIME-BALL-PROPER-PARTITION-OBSTRUCTION@1 is independently accepted unchanged.\n\nThe residual row criterion is an iff: summaries have only two outputs, and any two row types supply a summary. For every nontrivial proper block of a radius-one ball, inside weights 0,1,2 give three distinct rows since the outside is nonempty. Every relevant singleton core is a bit or its complement and its deficit hull is zero for K>=0. Hence the initial bank is exactly H+kappa I.\n\nThe spectrum is mu=1-2(n+1)/2^n and nonempty coefficient -2(n+1-2|S|)/2^n. Edge count gives I=2n(n-1)/2^n. With delta=1-mu^2, the nonempty entropy lies between (2n-2-2log2(n+1))delta and (2n-2)delta; eta(mu^2)<=delta/ln2. Since delta/I=2(n+1)(1-(n+1)/2^n)/(n(n-1)), squeezing gives H/I->4. The source all-n H<5I bound follows from (4n-1)(n+1)/(n(n-1))<=5 for n>=8 and its five rational small-n upper bounds. No asymptotic inequality is applied outside its stated range. Own matrix/character/edge code checks dimensions3..6, with both signs also covered by the main domain. This accepts the source statement only; the new arbitrary-core perturbation theorem is separately attributed and awaits external review.\n',encoding='utf-8',newline='')
statement='For every finite Boolean f:{0,1}^n->{-1,+1} and every integer m>=3, G_m(x,z)=f(x)*b_(n+m)(x,z), with b_N=-1 exactly on the radius-one Hamming ball, has at least three residual rows for every coordinate block B with 2<=|B|<=n+m-1. Thus G_m admits no proper nonsingleton single-Boolean-output block compression. With f fixed and m->infinity, H(G_m)->H(f) and I(G_m)->I(f); ratios converge when f is nonconstant. For every fixed finite C>=0, FEI(C) for all such block-prime functions is equivalent to full FEI(C), without changing C.'
new={'claim_id':'A075-ARBITRARY-CORE-BOOLEAN-PRIME-PERTURBATION','version':1,'exact_statement':statement,'hypotheses':['Uniform finite physical cube; squared normalized real Walsh coefficients; entropy in bits.','m>=3; original f arbitrary, including constants and dummies.','Block compression uses one Boolean output per disjoint coordinate block; all outside inputs retained.','Ratio statement only when I(f)>0; C fixed across all dimensions.'],'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A075'],'proof_source':'PROOF.md sections1-5; code/verify.py; code/audit.py','proof_dependencies':[],'review_records':[],'status':'ANALYTIC_PROOF_EXACT_FINITE_VALIDATION_EXTERNAL_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':'Full FEI still requires a dimension-independent entropy/influence payment on arbitrary block-prime functions; the reduction supplies none.','next_consumers':['A071','A072','A074','A080','A084','A089','A092','B15','B20']}
reviewed=dict(source_claim);reviewed['review_records']=list(reviewed.get('review_records',[]))+[review];reviewed['status']='INDEPENDENTLY_ACCEPTED_LOCAL_A075';reviewed['next_consumers']=['A071','A080','A092','B20']
save(R/'CLAIMS.json',{'claims':[new,reviewed]})
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B15','packet_id':'A075','gap_id':'G-INITIAL-SIGNED-BANK-PRICE','attempt_id':'stage21-universal-prime-perturbation','method':'Consume A071 obstruction; arbitrary-core Boolean perturbation with explicit residual rows and dimension-sensitive entropy continuity; exact Walsh/edge/matrix checks.','mathematical_delta':'Full FEI reduces to Boolean block-prime functions with unchanged constant, through explicit radius-one perturbation of any padded core. Initial proper-partition bank obstruction now retains arbitrary starting H/I rather than just limit4. A071 source independently accepted unchanged.','deliverable_status':'COMPLETE_LOCAL_VERIFIED_EXTERNAL_REVIEW_PENDING','mathematical_status':'ANALYTIC_REDUCTION_PROOF; FULL_FEI_OPEN; FORMAL_STATUS_IN_OUT_FORMAL_JSON','claim_versions_used':['A071-PRIME-BALL-PROPER-PARTITION-OBSTRUCTION@1 (reviewed; inspiration)','A075-WHOLE-ROW-SIGNED-COMPOSITION-DRIFT@1 (bank consequence only)'],'claims_created_or_changed':[new['claim_id']+'@1',source_claim['claim_id']+'@1 independent acceptance, unchanged'],'source_artifacts':['PROOF.md','REVIEW.md','out/FROZEN_SPEC.json','out/PILOT.json','out/MAIN.json','out/BOUNDARY.json','out/AUDIT.json','out/FORMAL.json','out/SOURCE_PINS.json'],'next_consumers':new['next_consumers'],'next_action':'A071/A080/A074 independently review the three-block case split and growing-alphabet continuity; then test a paid physical-history or multi-output initialization on G_m for arbitrary original f, preserving the same unused influence owners.','stagnant_substantive_attempts':0,'blockers':['Initial bank O(I) funding remains open; no full FEI proof or Boolean unbounded-ratio family.','External review and supervisor mirror/adoption not yet verified.'],'packet_ids':['A075']}
save(R/'PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
boundary_fail=[{k:r[k] for k in ['n','mask','m','min_rows']} for r in boundary['results'] if not r['prime'] and r['proper_blocks']]
save(R/'out/BOUNDARY_FAILURES.json',boundary_fail)
report=f'''# exact target, quantifiers, hypotheses and units

For every actual Boolean f on n uniform bits, construct block-prime G_m=f(x)b_(n+m)(x,z) for every m>=3, retaining H and I in the limit m->infinity. A block-prime function has at least three residual truth-matrix rows for every proper block of at least two bits; thus no such block admits a one-Boolean-output summary. FEI(C) on this class is equivalent to full FEI(C) with the same constant. Entropy is in bits. Constants and dummies are allowed in f; ratio convergence requires nonconstant f. Full FEI OPEN.

# sources actually read, revisions and theorem locators

Read current machine AGENTS, full execution protocol v2, report README/CURRENT_STATUS and registry/packet/stream files, campaign plan and supplement files, B15 v2 notes, current BOARD, own latest proof and rolling files, A071 stage21 PROOF/PROGRESS and A084 resumed stage21 PROOF/PROGRESS. Exact source paths and hashes are in SOURCE_PINS and INDEPENDENT_REVIEW. Required paper text intake required cp1252 decoding after UTF-8 rejected byte0xad; no false source-corruption claim is made. Paper composition/percolation locators are background, not proof premises. A084 already improves reserve3 to9/4; this run does not duplicate or independently accept that scalar theorem. Latest board records A072/A074 independent acceptance of our previous drift theorem. A071 source is reviewed unchanged here. The B15 initial sparse-family assignment is already closed; dispatch consumes its new initial-bank obstruction.

The session wake completed with OWNER ALERT REQUIRED NOW: personal-model/state/dream notes stale. Alert delivered before using affected notes; mathematics uses current task sources. Compute snapshot status ok: available RAM7253MB, disk14.4GB. No work is killed/throttled. Research writes remain inside A075; no git, mail, shared-index/brain writes, trading access or remote compute. Contract cache stale/unmatched; no irreversible action attempted. The read-only math recall found neighboring FEI/decomposition cards, no direct proof of this perturbation construction; none is used as a premise. No web or priority/clock changes.

# complete derivation or exact first unsupported line

PROOF sections1-2 give three explicit row witnesses in each of the exhaustive cases: a block contains at least two padding bits, exactly one, or none. Arbitrary original f signs cannot merge these patterns. Three padding bits suffice uniformly; no optimal-padding assertion is made. The difference set has exactly N+1 points. Physical edge comparison gives |I(G)-I(f)|<=2N(N+1)/2^N. Parseval and Cauchy-Schwarz give TV of squared spectra <=2sqrt((N+1)/2^N); a maximal-coupling conditional-entropy argument pays the growing alphabet by h2(epsilon)+N epsilon. Both errors vanish. Passing a hypothetical dimension-independent block-prime FEI inequality to this limit proves full FEI with the SAME constant. Constant f is handled without dividing by influence.

On every proper disjoint Boolean partition of G_m all cores are singleton bits/complements. Consequently the supplied-bank price is exactly H(G_m)+kappa I(G_m), and for nonconstant original f its ratio tends to H(f)/I(f)+kappa. Unlike a fixed H/I->4 family, this obstruction retains arbitrary original ratios. It does not make a divergent family without an original divergent family. The first unsupported line is the ORIGINAL O(I) initial source on these arbitrary indecomposable cores, or an invariant using paid histories/overlap/multiple outputs. No universal payment is inferred from decomposition failure.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC precedes search and pins helper hash. Pilot: {pilot['circuits']} actual circuits, {pilot['checks']} predicates, {pilot['elapsed_seconds']:.3f}s. Main: all {main['circuits']} Boolean functions on n=0..3 with m=3, {main['proper_block_checks']} proper-block tests and {main['checks']} exact predicates, {main['elapsed_seconds']:.3f}s. Both signs, constants and dummies included; no symmetry quotient. Direct characters and integer FWHT agree, Parseval, physical edges, exact squared-coefficient perturbation norm, TV bound and literal original-core restriction all pass. Every physical row is retained. Results save after each original dimension.

Boundary archive: {boundary['circuits']} cases n<=2, m=0..2, {boundary['checks']} predicates and {boundary['proper_block_checks']} block matrices. Some cases fail primeness; outputs preserve the case identifiers and minimum row counts. No statement for m<3 is inferred from passes or failures. Independently frozen audit: {audit['checks']} predicates, {audit['elapsed_seconds']:.3f}s, separate matrix grouping/direct Walsh/edge formulas on radius-one balls in dimensions3..6, all sign-pattern triples, frozen helper digest, and a real radius-zero negative control (two rows, hence compressible). These finite checks validate proof fidelity; PROOF supplies the all-dimensional bridge.

Commands: python -X utf8 code/verify.py pilot; main; boundary; code/audit.py; code/finalize.py. Integer/Fraction arithmetic; no floating logarithmic sign decisions, no LP, no GPU, no dimension escalation, memory estimates50-80MB, each measured check below60s. Formal receipt: {formal.get('status','see out/FORMAL.json')}. An earlier premature Lean invocation failed because the requested file did not yet exist; this is preserved as a setup failure, not mathematical evidence. The source is now saved, and the actual attempted compiler receipt is separate. No compilation-only proof claim is made.

# proof dependencies and changed downstream conclusions

The new A075-ARBITRARY-CORE-BOOLEAN-PRIME-PERTURBATION@1 is a self-contained analytic reduction, author-checked with exact finite controls, external review pending. A071-PRIME-BALL-PROPER-PARTITION-OBSTRUCTION@1 is independently accepted unchanged: full row argument, spectrum, influence, entropy squeeze H/I->4 and H<5I reconstructed in REVIEW. This consumes a pending source before introducing a new broad candidate. The arbitrary-core extension is attributed separately. The bank corollary uses the previous A075 supplied-envelope definition only; it is not needed for the FEI equivalence proof. No pending A084 scalar result or FEI assertion is used.

Downstream: proper Boolean partition search cannot remove arbitrary starting FEI difficulty by discarding decomposable cases; the indecomposable class is dense in H,I through explicit Boolean examples. A universal initial-bank payment must survive this construction, or explicitly use a different state/payment mechanism. No outside funds, influence reuse or new FEI constant follows.

# one next mathematical action and independent reviewer

A071/A080/A074 independently reconstruct the row patterns and the dimension-sensitive entropy continuity. Then price a useful paid restriction-history or multi-output initialization on G_m for arbitrary seed f with actual original owners. This directly tests a universal mechanism rather than another fixed-ratio example. A092 audits the reduction scope.

# actual persistence receipts or precise save blocker

Four protocol files, complete proof, source review, frozen search/audit specs, exact outputs, Lean source/receipt, helper code and rolling files are saved locally. PROGRESS and PACKET_DELTA are byte-identical. PERSISTENCE validates exact schema fields, statement hashes, source pins and file sizes; all files below20MB. Remote copy/mirror/downstream adoption remain unverified and belong to the supervisor. No own background worker is launched. The mandatory session wake is separate from research persistence; no shared checklist/mesh mutation is attempted under the explicit write-only-A075 rule.

# Universal bridge

C019 stopping-tree payment and C024 history transfer now have an explicit arbitrary-core initialization obstruction: every Boolean seed is approximated in BOTH Fourier entropy and physical influence by block-prime actual functions whose every proper Boolean-partition bank is exactly H+kappa I. The FEI target restricted to these indecomposable cores is equivalent with unchanged constant, upgrading the earlier ball limit4 to arbitrary seed ratios. What remains is an O(I) ORIGINAL source or a genuinely paid history/multiple-output mechanism on these cores. NEXT tests that mechanism on arbitrary f through G_m; it is shorter than another isolated class result because any proof on this reduced class would imply full FEI directly.
'''
report=report.replace('# proof dependencies and changed downstream conclusions','Independent source sign certificates also recheck BOTH H(b16)>3I and H(b32)>(7/2)I with a separately frozen 40-term positive-atanh expansion and explicit geometric remainder, using exact Fractions (out/SOURCE_SIGNS.json). Source statement hashes use their own canonical statement-plus-hypotheses JSON convention; the new claim uses raw UTF-8 statement hashing. Both conventions are explicitly checked and preserved, with receipts in out/HASH_CONVENTION_*.json.\n\n# proof dependencies and changed downstream conclusions')
(R/'REPORT.md').write_text(report,encoding='utf-8',newline='')
with (R/'REVIEW.md').open('a',encoding='utf-8',newline='') as out:
 out.write('\nBoth additional source finite signs H(b16)>3I and H(b32)>7I/2 are independently rechecked by exact outward logarithm intervals with the proved positive-atanh tail in code/source_signs.py and out/SOURCE_SIGNS.json. The source canonical statement-plus-hypotheses hash is retained unchanged; it is not a raw statement-string hash.\n')
(A/'STATUS.md').write_text('STATE: A075 stage21 saved: arbitrary Boolean cores approximate block-prime G_m in H and I; full FEI equivalent on that class with SAME constant;278 circuits/14782 blocks exact; A071 accepted;FEI OPEN.\nNEXT: A071/A080/A074 review row/continuity reduction; price paid-history or multi-output ORIGINAL bank on G_m for arbitrary seed, retaining all original owners.\n',encoding='utf-8',newline='')
lesson='\n'+now+' stage21: For every actual f, G_m=f(x)b_(n+m)(x,z), m>=3, has >=3 residual rows for EVERY proper block of >=2 coordinates. Three exhaustive cases by padding count prove it without hypotheses on f. Disagreement delta=(N+1)/2^N yields |I(G)-I(f)|<=2Ndelta, spectral TV<=2sqrt(delta), |H(G)-H(f)|<=h2(2sqrt(delta))+2Nsqrt(delta) eventually. Thus FEI(C) on block-prime functions iff full FEI(C), SAME constant. On all proper Boolean partitions their supplied bank is H+kappa I, retaining arbitrary original H/I in the limit. Not an FEI proof or divergent family. One-point perturbation alone fails (two-row block); radius-one is essential to this construction. A071 ball obstruction independently HOLDS.\n'
for name,text in [('WORKLOG.md',lesson+'Exact main278 circuits/14782 blocks/31510 predicates, boundary66 cases, independent audit246; pending external review.\n'),('LEARNED.md',lesson)]:
 if 'stage21: For every actual f' not in (A/name).read_text(encoding='utf-8'):
  with (A/name).open('a',encoding='utf-8',newline='') as out:out.write(text)
# Protocol schema and persistence audit, independent of prose completion.
protocol=load(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
fields=protocol['required_per_run']
expected={k.split(' (')[0] for k in fields['progress_fields']}
assert set(progress)==expected
for c in [new,reviewed]:
 assert set(c)==set(fields['claim_fields']),(set(c),set(fields['claim_fields']))
 hashes={'raw_statement_utf8':hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()}
 for key in ['statement','exact_statement']:
  payload={key:c['exact_statement'],'hypotheses':c['hypotheses']}
  hashes['canonical_json_'+key]=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')).hexdigest()
 assert c['statement_sha256'] in hashes.values(),(c['claim_id'],hashes)
 save(R/'out'/('HASH_CONVENTION_'+c['claim_id']+'.json'),{'claim_id':c['claim_id'],'stored':c['statement_sha256'],'matched_conventions':[k for k,v in hashes.items() if v==c['statement_sha256']]})
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for h in fields['report_fields']:assert '# '+h in report
files=[]
for p in R.rglob('*'):
 if p.is_file() and p.name!='PERSISTENCE.json':
  assert p.stat().st_size<20_000_000
  files.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':digest(p)})
save(R/'out/PERSISTENCE.json',{'status':'PASS','at':now,'protocol_schemas':'exact fields','claim_statement_hashes':'PASS','progress_compatibility':'byte identical','files':files,'remote_mirror':'UNVERIFIED','formal':formal})
print(json.dumps({'persistence':'PASS','files':len(files),'new_claim':new['claim_id'],'formal':formal.get('status'),'full_fei':'OPEN'}))
