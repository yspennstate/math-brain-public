from pathlib import Path
import json,hashlib,datetime,copy

RUN=Path(__file__).resolve().parents[1];BASE=RUN.parents[1]
ROOT=BASE.parents[1]
OLD=BASE/'runs/20261023T105842Z-account03-A069-geometric-transfer'
REF=ROOT/'agents/A070/runs/20261023T112210Z-account03-A070-analytic-route-referee'
PROTO=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
protocol=read(PROTO);cert=read(RUN/'out/CERTIFICATE.json');pilot=read(RUN/'out/PILOT.json')
assert cert['status']=='PASS' and not cert['pilot'] and cert['full_core_trees']==1456
assert cert['elapsed_seconds']<55 and pilot['elapsed_seconds']<60
sourceclaims=read(REF/'CLAIMS.json')
prior=copy.deepcopy(next(c for c in sourceclaims if c['claim_id']=='A069-PREEXPOSURE-FROZEN-FLAG-PRIVATE-PAYMENT'))
original=next(c for c in read(OLD/'CLAIMS.json') if c['claim_id']==prior['claim_id'])
for k in ['exact_statement','hypotheses','statement_sha256']:assert prior[k]==original[k]
assert sha(Path(prior['proof_source']['path']))==prior['proof_source']['sha256']
receipt=next(r for r in prior['review_records'] if r['reviewer']=='account03/A070')
assert receipt['independent'] and not receipt['substantive_repair']
assert sha(Path(receipt['source_claim_file']))==receipt['source_file_sha256']
prior['status']='UNCHANGED_INDEPENDENT_A070_FULL_SCOPE_RECEIPT_CONSUMED_BY_A069_PENDING_B20'
consumers=['A070','A088','A094','A096','B14','B20']
statement=('For any finite uniform Boolean pair a,b and original probability reference R dominating its mean squared Fourier law P, retain only direct frequency marginals and query every physical core coordinate on every branch of a complete adaptive tree T. Put B=CE(P,R), J=(I(a)+I(b))/2, D_v=parent B minus average BOTH full child B, j_v=mean physical queried influence, and V_T=sum_v 2^(-depth(v)) (D_v-4j_v)_+. Then D_v>=0, sum weighted D_v=B, sum weighted j_v=J, and V_T=B-A_T with 0<=A_T=sum weighted min(D_v,4j_v)<=4J. Hence max(0,B-4J)<=V_T<=B and |V_T-V_U|<=4J for any two complete adaptive trees or independently seeded mixtures using the SAME original source. The coefficient4 is sharp: a=b=chi_x on x,z and R=(epsilon,1,15-2epsilon,epsilon)/16, epsilon=2^-k, give V_xz=4-log2(1+epsilon) and V_zx=log2(1+epsilon). For k>=2 the SAME5/8 allowance pays zx but fails xz. Positive full references cannot give an exact universal multiplicative V<=KJ including constant pairs. Support-dominating references with zero cells are hereditary and remove only this support obstruction. Every all-function selected-tree source bound V<=K I(f) on diagonal pairs implies FEI(K+4); conversely FEI(C) supplies R=P with every paired tree V<=(C+2)J, and V<=C I(f) on the diagonal. The min/max positive invoices have the stated exact finite Bellman recursion. These comparisons and equivalences supply NO universal influence-priced source or full FEI proof. Under the prior accepted frozen-product wrapper, actual projected core invoices inherit this comparison only within its explicit control/stopping hypotheses and after paying any additional4J from an original unused owner.')
hyp=['Finite uniform Boolean cubes; bits for entropy/CE and ordinary physical pivotal influence.',
 'R is a normalized nonnegative ORIGINAL law, positive wherever P=(P_a+P_b)/2 is positive; occupied-cell CE is finite and zero-mass terms are omitted.',
 'All physical restrictions use only direct marginals of this SAME R; every coordinate is queried on every path, including at constant outputs; both full children/terminals retained.',
 'Complete adaptive tree choices depend only on physical history. Randomizing seeds are initially independent of the core; use their original physical distribution.',
 'Expected-tree accounts only; no pathwise bank, renewed source, calibration, omitted irrelevant continuation or deposit of negative excess is claimed.',
 'The concrete original9-bit5/8 theorem remains fixed-relative-order. New sharpness example has a different explicitly supplied two-bit reference; it is not an FEI counterexample.',
 'Wrapper application separately assumes the accepted previous frozen product-reference/core-invoice identity at every allowed physical control history; this stage does not prove an arbitrary source affordable.']
digest=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
new={'claim_id':'A069-SHARP-INHERITED-CORE-ORDER-COMPARISON','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':digest,
 'contributors':['account03/A069'],'proof_source':{'path':str(RUN/'DERIVATION.md'),'sha256':sha(RUN/'DERIVATION.md'),'locators':'Sections1-5'},
 'proof_dependencies':[{'claim_id':prior['claim_id'],'version':prior['version'],'statement_sha256':prior['statement_sha256'],'acceptance':'Unchanged independent A070 full-scope receipt consumed; not an A069 self-review','scope':'Only wrapper application identifying actual invoices; abstract core theorem is proved directly.'}],
 'review_records':[],'status':'AUTHOR_PROVED_WITH_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':['Unregistered extension: a paid fixed-order positive core invoice is numerically unchanged after arbitrary core reordering under the same full reference.','Unregistered extension: mandatory strictly positive full original references admit V<=KJ for all constant cores when every coordinate is exposed.'],
 'first_unproved_line':None,'next_consumers':consumers}
save(RUN/'CLAIMS.json',[prior,new])
nextaction='A070/A088/A094 reconstruct nonnegative full decrement, complete-tree telescopes and sharp two-bit owner falsifier. Then construct an ORIGINAL support-dominating source or Bellman supersolution paid by influence for arbitrary Boolean cores; exploit Boolean coefficient relations. Order comparison is now sharp and closed; do not repeat ordering/private-width/optional-reset experiments or claim the FEI-equivalent source interface solved.'
sources=[PROTO,ROOT/'BOARD.md',ROOT/'claude/B14/STREAM_NOTES.md',Path(r'~\AGENTS.md'),OLD/'DERIVATION.md',OLD/'CLAIMS.json',REF/'DERIVATION.md',REF/'CLAIMS.json',REF/'out/CHECK.json']
manifest=[]
for p in sources:
 assert p.exists(),p
 manifest.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size})
save(RUN/'out/SOURCE_MANIFEST.json',manifest)
p={'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B14','packet_id':'A069',
 'gap_id':'C024-C019-ORIGINAL-OWNER-CUMULATIVE-CORE-EXCESS','attempt_id':'A069-stage10-sharp-order-and-source-boundary',
 'method':'Exact physical frequency-erasure likelihood ratios; full-tree CE/influence telescopes; sharp actual Boolean two-bit counterfamily; support inheritance; exact finite adaptive-tree verification.',
 'mathematical_delta':'Sharp dimension-independent4J order overhead proved, unchanged old-bank reuse refuted by a two-bit dictator, and strict-positive constant-source obstruction separated from support-dominating source admission. Universal initial-source payment is proved FEI-equivalent up to explicit constants, and remains open. Previous full expanded A069 theorem has unchanged A070 independent acceptance.',
 'deliverable_status':'COMPLETE_LOCAL_PENDING_NEW_REVIEW_AND_SUPERVISOR_COPY',
 'mathematical_status':'SCOPED_AUTHOR_PROOF_AND_EXACT_CERTIFICATES;FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':prior['claim_id'],'version':prior['version'],'statement_sha256':prior['statement_sha256']}],
 'claims_created_or_changed':[{'claim_id':prior['claim_id'],'version':prior['version'],'change':'Consumed independent A070 acceptance without changing statement/hypotheses/hash'},{'claim_id':new['claim_id'],'version':1,'change':'Sharp order comparison/source boundary and actual Boolean unchanged-bank obstruction'}],
 'source_artifacts':['DERIVATION.md','FROZEN_CERTIFICATE_SPEC.json','FROZEN_CERTIFICATE_SPEC_V2.json','code/certificate.py','code/rational.py','code/finalize.py','out/PILOT.json','out/CERTIFICATE.json','out/SOURCE_MANIFEST.json'],
 'next_consumers':consumers,'next_action':nextaction,'stagnant_substantive_attempts':0,
 'blockers':['Universal original influence-priced source/Bellman payment remains OPEN; equivalence is not a payment.','New theorem independent review, shared registry adoption and supervisor remote/mirror copies unverified.','Brain self-care degraded: owner model99.5h, state of mind84.1h, latest dream34.8h stale; those remembered contexts unverified.'],
 'packet_ids':['A069']}
save(RUN/'PROGRESS.json',p);(RUN/'PACKET_DELTA.json').write_bytes((RUN/'PROGRESS.json').read_bytes())
report=f'''# A069 stage10: sharp core order comparison and original-source boundary

## exact target, quantifiers, hypotheses and units

For ANY finite Boolean pair on a uniform core cube, and ANY supplied original normalized reference dominating its mean squared spectrum, compare the cumulative positive rate4 core invoice over ALL complete adaptive physical query trees. Every coordinate, both children, irrelevant continuations and full terminal references remain. Units are bits and physical pivotal influence; all bank statements are expected-tree accounts. No source reset, renewed owner or universal source admission is assumed.

## sources actually read, revisions and theorem locators

Read current BOARD (B14/B20 and cross-stream live statuses), B14 STREAM_NOTES v2, own STATUS and prior stage9 sources, machine-wide AGENTS, and full protocol2026-10-11-execution-v2. Current campaign endpoint and own-folder restrictions override old protocol dates/shared-write defaults. Previously read campaign/paper baselines are not new mathematical premises. New A070/run20261023T112210Z DERIVATION Sections1-6 and complete CLAIMS were read. Its full expanded review independently accepts A069 stage9 unchanged, including frozen-root donor capacity>1519/2048 and SAME5/8 remainder>1/24. The receipt is source/hash checked and consumed, not an author self-review. A070's additional real guard is reconstructed numerically exactly here; no new independent full-scope acceptance of its overlapping claim is asserted. Source hashes and locators are in out/SOURCE_MANIFEST.json. No spatial percolation estimate is assumed universal.

## complete derivation or exact first unsupported line

DERIVATION Sections1-5 give the complete proof. Every inherited core decrement D is a nonnegative weighted log likelihood ratio. Both complete physical children cancel Fourier cross terms. Full core exposure gives sum weighted D=B and sum weighted queried influence=J. Therefore V_T=B-sum weighted min(D,4j), and max(0,B-4J)<=V_T<=B. Any two complete adaptive trees differ by at most4J, also for independently seeded mixtures. The previous stage's accepted identity transfers this comparison to its actual paired wrapper within the explicitly retained control/stopping hypotheses. It does not replenish the old owner.

The constant4 is sharp: the actual two-bit Boolean dictator pair with R=(epsilon,1,15-2epsilon,epsilon)/16 has invoices4-log2(1+epsilon) and log2(1+epsilon) in opposite orders. Their gap tends to4J. For k>=2, epsilon=2^-k, SAME5/8 pays one order and fails the other. The expensive continuation occurs at a constant output; omitting it would erase the inherited reference cost. This falsifies an unchanged-order invoice extension, not the earlier fixed-order nine-bit result and not FEI.

Strictly positive full references have positive B even for constant pairs with J=0, so a universal exact multiplicative source claim with that hypothesis is false. Permitting a root support-dominating reference, whose support guarantee is proved hereditary, removes this accounting obstruction. It does not supply the universal source price. On diagonal pairs, V<=KI implies H<=B=V+A<=(K+4)I. Conditional on FEI(C), R=P gives V<=CI on diagonal pairs and <=(C+2)J for paired cores, using JS<=TV<=2J. The exact min/max Bellman recursion and these explicit constants expose the remaining universal strength. They are not presented as a proof of the open side.

First unsupported line: construct an ORIGINAL influence-paid support-dominating source or selected complete-tree Bellman supersolution for arbitrary indecomposable Boolean cores, with old debits and all full costs retained. New order overhead is closed and sharp; universal initial-source payment and full FEI remain OPEN.

## executed validation with domain, arithmetic, commands and outputs

Frozen spec V1 precedes execution; V2 freezes the same-domain supported-source extension after the pilot and before the full check. Pilot PASS:8 full trees, {pilot['checks']} exact assertions, {pilot['elapsed_seconds']:.6f}s. Final PASS:{cert['full_core_trees']} full adaptive trees, {cert['checks']} assertions, {cert['elapsed_seconds']:.6f}s. Domain:all256 ordered two-bit Boolean pairs with nonflat R=(1,2,4,9)/16 AND with R equal to their actual mean spectrum; all36 ordered pairs of six explicit three-bit functions with nonflat R=(1,2,4,8,16,32,64,129)/256, every12 complete adaptive trees; seven sharpness k values1,2,3,4,8,16,32. No symmetry quotient or automatic dimension increase. The finite check is separate from the all-dimensional and all-k proofs.

Actual Fourier spectra are computed by integer Walsh, both physical child tables and reference marginals reconstructed, and complete CE differences compared with independently formed likelihood ratios. Exact prime-log cancellation verifies every telescope; positive parts use rigorous Fraction log intervals with a proved24-term atanh tail after reduction to[1,2). Every pair of tested complete tree invoices obeys the4J comparison. Explicit sharpness invoices agree symbolically with the two formulas. Zero reference cells are allowed only off actual support, and their full physical continuations are checked. The separate normalized-real fixture has child norms37/25,13/25 and core energy8/25 versus pivotal probability1/2, agreeing with A070; that algebraic example is not a Boolean FEI counterexample.

Commands from A069:

    python -B -X utf8 runs/{RUN.name}/code/certificate.py --pilot
    python -B -X utf8 runs/{RUN.name}/code/certificate.py
    python -B -X utf8 runs/{RUN.name}/code/finalize.py

Budget96MB, pilot/full cap55s, observed times above. No heavy search, GPU, new worker, detached job or formal compiler attempt. No resource gate above300MB was needed. Shell/source startup was slow; arithmetic remained small. No other agent's work was stopped. No floating sign decision or unexecuted validation is claimed.

## proof dependencies and changed downstream conclusions

The abstract core theorem is proved directly. Only its wrapper corollary consumes A069-PREEXPOSURE-FROZEN-FLAG-PRIVATE-PAYMENT@1, hash477ca502c81fa4117c6a21dd645ae3146e5e6e298dc78b72948c5421113ed0a4, now independently accepted unchanged by A070. Copied statement/hypotheses/hash are intact. New order theorem is author-proved with exact checks, pending independent review. Its sharp counterexample prohibits copying a fixed-order numerical owner invoice into a reordered continuation. An additional4J must be funded if only the general comparison is available. The old fixed-relative-order9-bit5/8 result remains valid. No registry adoption or remote review is inferred from local receipts.

## one next mathematical action and independent reviewer

{nextaction}

## actual persistence receipts or precise save blocker

Four exact-schema protocol files, complete derivation, frozen specifications, scripts and exact outputs are saved in this requested A069 run. Rolling STATUS has two lines; WORKLOG and LEARNED are updated. out/RECEIPTS.json hashes every other run artifact and rolling file, checks local readback and size limits. No local save blocker; external review/adoption and supervisor remote copies remain unverified. No Git, shared-index/brain research write, messaging, other-agent mutation or trading access occurred. Brain self-care is degraded/unverified: stale owner-model99.5h, state-of-mind84.1h and latest dream34.8h affect remembered owner context; the owner was explicitly alerted and current instructions/local evidence govern.

## Universal bridge

This stage moves C024/C019 by closing the adaptive core-order comparison with SHARP overhead4J, while an actual two-bit Boolean family disproves unchanged original-bank reuse after reordering. Support inheritance separates a necessary finite-CE encoding condition from the false strict-positive constant-source demand. What remains is the ORIGINAL influence-priced universal source or complete-tree supersolution; the explicit FEI equivalence proves that this remainder cannot be passed off as a solved transfer. NEXT must exploit Boolean coefficient relations to pay that original source from actual unused influence capacity, retaining old/full bills. It is the shortest remaining route because further core ordering or private-width examples cannot reduce the now-sharp order term or pay the initial universal source.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
status='STATE: A069 stage10: prior expanded theorem independently HOLDS(A070); sharp4J core-order comparison/support heredity; two-bit SAME-bank reorder obstruction; '+str(cert['checks'])+' exact checks PASS; FEI OPEN, new review pending.\nNEXT: A070/A088/A094 review sharp order/source boundary; build ORIGINAL influence-paid support-dominating arbitrary-core source or Bellman supersolution, all old debits/full terminals; ordering/private-width loops closed.\n'
(BASE/'STATUS.md').write_text(status,encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
for name,text in [('WORKLOG.md',f'\n{stamp} stage10: consumed A070 full expanded unchanged acceptance; proved sharp4J complete-core order bound and exact two-bit unchanged-owner falsifier; support inheritance/constant strict-positivity guard and FEI-hard source boundary. Pilot8 trees PASS; final1456 trees/{cert["checks"]} assertions PASS in{cert["elapsed_seconds"]:.6f}s. Full FEI open, new review pending; no jobs left by this finalizer.\n'),('LEARNED.md','\nStage10 durable: with ONE inherited support-dominating reference and full physical core exposure, each DeltaCE>=0, total DeltaCE=B and queried influence=J. Positive invoice V=B-A with0<=A<=4J, so every adaptive order differs by<=4J, sharply. Two-bit chi_x with R=(epsilon,1,15-2epsilon,epsilon)/16 has invoices4-log2(1+epsilon) versuslog2(1+epsilon); SAME5/8 can pay only one. Full constant-output continuations cannot be erased. Strict-positive full R makes a constant core invoice positive at J0; hereditary support-dominating R fixes support only. Universal source/selected-tree payment implies FEI(K+4); conditional FEI(C) gives diagonal all-tree boundC and pairedC+2 via R=P. These equivalences do not pay the open original source.\n')]:
 with (BASE/name).open('a',encoding='utf-8') as f:f.write(text)
cf=set(protocol['required_per_run']['claim_fields']);pf={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert all(set(c)==cf for c in read(RUN/'CLAIMS.json'))
assert set(read(RUN/'PROGRESS.json'))==pf
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len((BASE/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert all('## '+h in report for h in protocol['required_per_run']['report_fields'])
receipt=[]
for f in sorted(RUN.rglob('*')):
 if f.is_file() and f.name!='RECEIPTS.json':
  assert f.stat().st_size<20*1024*1024
  receipt.append({'path':str(f.relative_to(RUN)),'sha256':sha(f),'bytes':f.stat().st_size})
rolling=[{'path':str(BASE/n),'sha256':sha(BASE/n)} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]
save(RUN/'out/RECEIPTS.json',{'status':'PASS_LOCAL_READBACK','artifacts':receipt,'rolling':rolling,'remote_mirror':'UNVERIFIED','independent_review_new':'PENDING'})
for row in receipt:assert sha(RUN/row['path'])==row['sha256']
for row in rolling:assert sha(Path(row['path']))==row['sha256']
print(json.dumps({'status':'PASS_LOCAL_READBACK','artifacts':len(receipt),'checks':cert['checks'],'new_statement_sha256':digest,'prior_independent_review':'A070_FULL_SCOPE_UNCHANGED','full_FEI':'OPEN'}))
