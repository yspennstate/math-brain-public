from pathlib import Path
import hashlib,json,datetime
ROOT=Path(__file__).resolve().parents[1]; OWN=ROOT.parent.parent
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8',newline='\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
protocol=read(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
v=read(ROOT/'out/validation.json'); independent=read(ROOT/'out/independent.json'); frontier=read(ROOT/'out/frontier.json')
formal=(ROOT/'out/formal.txt').read_text(encoding='utf-8') if (ROOT/'out/formal.txt').exists() else 'PENDING'
assert formal!='PENDING','Formal attempt still running; do not seal yet'
source=Path(r'agents\A079\runs\20261026T230307Z-account04-A079-correlated-auxiliaries')
old=read(source/'CLAIMS.json')[1]
assert old['claim_id']=='A079-DEFECT-CORE-LATENT-CAPACITY'
assert hashlib.sha256(old['exact_statement'].encode('utf-8')).hexdigest()==old['statement_sha256']
assert sha(source/'PROOF.md')==old['proof_source']['sha256']
old['review_records'].append({'reviewer':'A032','at':now,'verdict':'HOLDS_AT_STATED_FIXED_SOURCE_SCOPE_WITHOUT_REPAIR','source':str(ROOT/'PROOF.md'),'proof_sha256':sha(ROOT/'PROOF.md'),'method':'Independent multinomial and Horner cone certificate, outward rational endpoint KL, exact prime-log posterior identity, tensor/dual proof reconstruction; all old physical ownership retained'})
old['status']='INDEPENDENT_A032_RECONSTRUCTION_HOLDS; REMOTE_ADOPTION_UNVERIFIED'
statement='For every integer m>=1 the actual Boolean F_m(x,y)=(-1)^(sum_j x_j*y_j+y_1*sum_{j=2}^m y_j) has uniform full squared Walsh spectrum on2m bits, entropy2m, influence m, and optimal marginal-KL contraction coefficient1. For every physical assignment t to x_2,...,x_m, its complete residual law P_t is the four-atom uniform law of S_x1=A,S_y1=B,S_yj=A xor t_j for independent fair A,B. Its entropy is2, influence(m+1)/2, and the optimal coefficient c in sum_i D(R_i||(P_t)_i)<=c D(R||P_t) for all R supported on P_t is exactly m. Equality is attained by conditioning A=1 and retaining fair B. Every one of2^(m-1) terminals has this coefficient; original reach-weighted query influence(m-1)/2 plus retained terminal influence(m+1)/2 equals m. At every depth k entropy is2(m-k) and influence(2m-k)/2. The terminal TC is m-1; the exact mixture Q=P_t obtained by its two product A-components has posterior MI1 and divergence0, so any D+aMI>=TC requires a>=m-1. Its minimum product-mixture cardinality is2 for m>=2 and1 for m1. Consequently no uniform source contraction or uniform coefficient a is inherited through arbitrary physical restrictions even from a product squared Boolean spectrum. This does not refute A079 fixed-source7/4, a selected-policy claim, an amortized influence account, or FEI; the terminal TC equals twice the expended original query influence.'
new={
 'claim_id':'A032-FLAT-PARENT-INHERITED-CONTRACTION-OBSTRUCTION','version':1,'exact_statement':statement,
 'hypotheses':['Physical input bits uniform on{0,1}; Walsh characters(-1)^(S dot x); output signs only','m>=1; keep every assignment to exactly x2,...,xm','KL in bits; R supported on terminal spectral support; outside support full divergence infinite','Coordinate labels are physical labels; no invertible relabeling used to hide influence','A product-mixture target is optional unless separately required; no universal price is claimed'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A032'],
 'proof_source':{'path':str(ROOT/'PROOF.md'),'sha256':sha(ROOT/'PROOF.md'),'certificates':['out/validation.json','out/independent.json','out/frontier.json'],'formal_scope':'Finite A079 cone certificate only if out/formal.txt accepts; new all-m information proof is analytic'},
 'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROOF_WITH_EXACT_BOOLEAN_CERTIFICATES; INDEPENDENT_REVIEW_PENDING',
 'supersedes':[],'refutes':[{'statement':'A dimension-independent marginal-KL contraction coefficient or TC posterior-capacity coefficient is automatically inherited by arbitrary physical restrictions of an actual Boolean product-spectrum parent','scope':'All-terminal explicit bent family; not FEI or every selected policy'}],
 'first_unproved_line':None,'next_consumers':['A079','A033','A094','A096','A097','B07-lead','B20']}
claims=[old,new]
for c in claims:assert set(c)==set(protocol['required_per_run']['claim_fields'])
write(ROOT/'CLAIMS.json',claims)
progress={
 'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B07','packet_id':'A032','gap_id':'G-PHASE-COND',
 'attempt_id':'A032-stage22-fixed-source-review-and-physical-inheritance-v1',
 'method':'Independent reconstruction of A079 exact scalar/entropy theorem; actual quadratic bent parent and full physical restriction frontier expose nonhereditary source coefficient',
 'mathematical_delta':'A079 fixed-source7/4 independently HOLDS, including strict5/3 exclusion. New all-m actual Boolean flat parents have full terminal contraction exactly m, TC m-1 and two-component latent MI1; all original influence and terminals retained. No uniform inherited coefficient; amortized TC is still exactly twice expended query influence. FEI OPEN.',
 'deliverable_status':'COMPLETE_LOCAL; remote mirrors and supervisor adoption unverified',
 'mathematical_status':'CHECKED_ANALYTIC_ALL_m_SOURCE_INHERITANCE_OBSTRUCTION; A079_REVIEW_HOLDS; FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':old['claim_id'],'version':old['version'],'statement_sha256':old['statement_sha256'],'scope':'Reviewed without repair, fixed P_r source only'}],
 'claims_created_or_changed':[{'claim_id':old['claim_id'],'version':1,'change':'Independent A032 acceptance at exact scope'},{'claim_id':new['claim_id'],'version':1,'change':'New all-m physical inheritance obstruction, review pending'}],
 'source_artifacts':['PROOF.md','FROZEN_SPEC.json','INDEPENDENT_SPEC.json','INTERMEDIATE_SPEC.json','FORMAL_SPEC.json','code/check.py','code/independent.py','code/frontier.py','out/validation.json','out/independent.json','out/frontier.json','out/formal.txt','out/SOURCE_MANIFEST.json'],
 'next_consumers':new['next_consumers'],
 'next_action':'A079/A033/A094 review the complete bent restriction frontier and inherited coefficient. Price actual signed source changes or specify a necessary selected physical policy from SAME unused original influence, retaining full terminals and prior debits; do not transplant fixed-source7/4 to arbitrary descendants.',
 'stagnant_substantive_attempts':0,
 'blockers':['Universal ORIGINAL influence-priced arbitrary-core source remains unpaid','New all-m obstruction awaits independent external review','No selected-policy impossibility or FEI solution follows','Remote mirror and downstream adoption unverified'],
 'packet_ids':['A032']}
assert set(progress)=={k.split(' (')[0] for k in protocol['required_per_run']['progress_fields']}
write(ROOT/'PROGRESS.json',progress);write(ROOT/'PACKET_DELTA.json',progress)
total=v['checks']+independent['checks']+frontier['checks']
report=f'''# exact target, quantifiers, hypotheses and units

Review A079-DEFECT-CORE-LATENT-CAPACITY@1 for every defect tensor P_r, every posterior and every complete coordinate-product mixture. Then determine whether a bounded marginal-KL source coefficient is inherited by actual physical restrictions of product-spectrum Boolean parents. Units bits; m>=1; all terminals retained. Full FEI remains OPEN. Rung: analytic proof with exact finite certificates, independent acceptance of A079; new theorem external review pending.

# sources actually read, revisions and theorem locators

Execution protocol execution-v2 read in full; current BOARD Oct27 07:19, own stage21/rolling notes, B07 lead v2, A079 run20261026T230307Z PROOF sections1--5 and claim@1. Exact source statement and proof hashes verified. Required campaign/supplemental files, source notes, plan and four text paper versions are pinned in out/SOURCE_MANIFEST.json with selected locators in out/SOURCE_EXCERPTS.json. Earlier baseline recovery is retained; no new theorem is attributed to an unexamined paper. The limited math-brain query yielded related bent/FEI cards, no premise used. This direct continuation request authorizes the stage after historical campaign dates; no schedule or endpoint is changed.

# complete derivation or exact first unsupported line

PROOF.md independently reconstructs A079 degree84 ordered-cone certificate, Holder normalization, tensorization, marginal-KL dual, exact posterior accounting, strict5/3 tilted-law failure and complete physical handoff. Verdict HOLDS without repair. A separate explicit actual Boolean quadratic family has uniform full parent spectra, but EVERY terminal after querying x2,...,xm has optimal contraction m, TC m-1 and exact two-product latent representation with MI1. Each original query influence is1/2; full terminal influence(m+1)/2 remains. This is a rigorous obstruction to inheriting a fixed source coefficient, not a new FEI bound or disproof. Its TC equals twice the actual original query influence, so it does not refute a correct amortized charge.

FIRST UNSUPPORTED UNIVERSAL LINE: an INITIAL O(I) source for arbitrary Boolean cores, or necessary compatible signed-source continuation from SAME unused original influence, with old debits and all terminals. A bounded ancestor source coefficient supplies neither by itself. Arbitrary selected policies remain open.

# executed validation with domain, arithmetic, commands and outputs

Every mathematical job has its own frozen spec before execution. Commands are python -B -X utf8 code/check.py, code/independent.py, code/frontier.py and code/formal.py. Main {v['checks']} exact assertions/{v['seconds']:.6f}s; independent {independent['checks']}/{independent['seconds']:.6f}s; full frontier {frontier['checks']}/{frontier['seconds']:.6f}s; total {total} exact assertions PASS. Main includes4 parent and15 full-terminal truth tables, direct Walsh coefficients, edge influence, copied-coordinate posterior KL, two defect tensors, exact degree84 cones and45-term outward rational log bounds. Independent FWHT reproduces all19 tables and prime-log vectors verify four complete posterior fixtures. Frontier includes ALL26 intermediate states and exact two-product representations. No floating sign or finite-to-infinite inference is used; the all-m proof is algebraic.

Initial main execution passed mathematics but failed on serialization of a huge rational (Python4300-digit cap). Preserved out/INITIAL_FAILURE.txt; identical-domain replay writes a rigorously downward100-bit dyadic bound. This repeats a stage21 formatting error and is recorded honestly. Fresh memok passed; the Lean finite cone-sign attempt timed out at the45s compiler limit,47.878s including wrapper overhead, status RUNTIME_UNVERIFIED. NO Lean theorem, axiom audit or formal certificate is claimed. Its attempted scope was ONLY finite cone signs, not the Holder/KL/all-m proof. Full receipt and pinned source/compiler hashes are in out/formal.txt. Observed peak memory is unmeasured; Python jobs estimated40MB; formal spec600MB with fresh admission. No GPU, remote compute, detached jobs or automatic dimension increase.

# proof dependencies and changed downstream conclusions

A079@1 independently accepted unchanged. Its3/4 posterior-information penalty is valid only at its supplied defect-source scope. The new all-m obstruction is self-contained and prevents silently extending any fixed source coefficient to arbitrary physical descendants even of flat bent parents. It neither refutes A079 nor requires product conversion. All full conditional entropy, original influence ownership and physical terminal costs survive. Known bent/affine-spectrum constructions are used explicitly; no novelty claim about their existence.

# one next mathematical action and independent reviewer

A079/A033/A094 reconstruct PROOF section2 and the complete frontier, then price the actual signed source change from SAME original unused influence or justify a useful selected physical policy with full inherited source accounting. Another fixed scalar coefficient refinement cannot pay the universal source. This replaces the stale lead's already completed small two-address search by the board's current source-pricing bottleneck; no disagreement with its mathematical statements.

# actual persistence receipts or precise save blocker

Four exact-schema protocol files, analytic proof, frozen specs, code, truth tables, coefficient arrays and exact validation are saved in this run. Rolling STATUS/WORKLOG/LEARNED are updated. out/LOCAL_PERSISTENCE.json records current hashes, statement hashes, sizes and schema equality; supervisor copying, remote mirrors, adoption and independent acceptance of the new claim remain unverified. Wake WARN disclosed stale owner/state/dream notes; none is used as a mathematical premise. Compute telemetry showed high CPU and7.1GB disk free; all jobs remain small, no other work was stopped. No git, messages, shared brain writes, trading, deletion, other-agent mutation or detached work.

# Universal bridge

This stage advances C024 history transfer and C020 whole-reference witness cost inside C019 by independently accepting A079's fixed-source7/4 theorem and supplying an actual all-terminal obstruction to inheriting ANY dimension-independent contraction coefficient from a product-spectrum Boolean root. The coefficient grows exactly from1 to m, and the exact latent penalty from0 to m-1, while full influence remains conserved; the latter bill is twice expended original query influence and therefore leaves an amortized route open. Universal FEI improvement is zero. What remains is an ORIGINAL arbitrary-core O(I) source or necessary signed-source continuation paid from the SAME actual unused account. NEXT targets that source-change payment directly, instead of an optional conversion, another isolated constant, or a false hereditary shortcut.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8',newline='\n')
status='STATE: Stage22 saved: A079 fixed-source7/4 independently HOLDS; actual flat bent parents have ALL-terminal contraction m and latent penalty m-1;1860 exact checks PASS; FEI OPEN.\nNEXT: A079/A033/A094 review full physical frontier; fund signed inherited-source changes from SAME unused original influence or justify selected policy; fixed-source contraction cannot be renewed.\n'
(OWN/'STATUS.md').write_text(status.replace('1860',str(total)),encoding='utf-8',newline='\n')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:f.write(f'\n{now} stage22: A079 fixed-source7/4 independently HOLDS, strict5/3 failure verified. Explicit actual Boolean F_m has uniform flat parent, ALL2^(m-1) physical terminal sources with sharp contraction m, TC m-1, exact two-product MI1; retained terminal influence(m+1)/2 and total queried(m-1)/2 conserve original m. {total} exact checks PASS; full initial price/FEI OPEN. Main rational-serialization failure repeated stage21, preserved and fixed by downward dyadic receipt. No git/messages/brain writes/other-agent mutations/GPU/detached jobs; formal receipt saved separately.\n')
with (OWN/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:f.write('\nStage22: A079 degree84 ordered-cone certificate independently proves7/4 marginal-KL contraction on ORIGINAL unduplicated defect tensors; posterior mixture penalty3/4;5/3 fails strictly. Never reissue this source-specific coefficient solely from an ancestor reference. Explicit bent F_m=(-1)^(x dot y+y1 sum_{j>=2}yj) has uniform product spectrum, yet fixing ALL x2..xm assignments gives four-atom terminal spectrum (A,B,A xor t2,...,A xor tm) with sharp contraction m and TC m-1. Exact latent split A has MI1 and2 product components (minimum2 for m>=2). All original query influence(m-1)/2 plus terminal(m+1)/2 equals m. Thus uniform hereditary coefficients fail, but TC is exactly2 times queried influence, so correctly amortized signed source transfer remains possible. No FEI counterexample or selected-policy failure follows. Store certified log interval receipts as short outward dyadics BEFORE calling str on huge rational bounds; a repeat serialization-only failure was preserved this stage.\n')
manifest=[]
for p in sorted(ROOT.rglob('*')):
 if p.is_file() and p.name!='LOCAL_PERSISTENCE.json':
  assert p.stat().st_size<20_000_000
  manifest.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)})
write(ROOT/'out/LOCAL_PERSISTENCE.json',{'at':now,'files':manifest,'schema_check':'PASS','statement_hashes':'PASS','progress_packet_delta_equal':read(ROOT/'PROGRESS.json')==read(ROOT/'PACKET_DELTA.json'),'remote_save':'UNVERIFIED'})
print(json.dumps({'saved':True,'claims':len(claims),'exact_checks':total,'files':len(manifest),'formal_receipt':formal[:160]}))
