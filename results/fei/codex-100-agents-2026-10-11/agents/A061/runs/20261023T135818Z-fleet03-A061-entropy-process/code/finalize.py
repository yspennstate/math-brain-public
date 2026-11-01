"""Persist stage21 proof/review without overstating universal completion."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];HOME=R.parents[1];ROOT=HOME.parents[1]
P=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def rd(p):return Path(p).read_text(encoding='utf-8')
def wr(p,s):Path(p).write_text(s,encoding='utf-8',newline='\n')
def obj(p):return json.loads(rd(p))
def dump(p,x):wr(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
protocol=obj(P);main=obj(R/'out/MAIN.json');pilot=obj(R/'out/PILOT.json')
assert main['status']==pilot['status']=='PASS'
assert main['counts']['pivot_states']==1524 and main['counts']['reset_children']==3048
assert main['negative_eligibility_witness'] is not None
primary=main['author_predicates']+main['independent_transport_predicates']
source=ROOT/'agents/A064/runs/20261023T130211Z-fleet03-A064-global-debt-potential'
sc=obj(source/'CLAIMS.json')[0]
assert sc['claim_id']=='A064-PREFIX-SECTOR-ELIGIBILITY-DEBT' and sc['version']==1
source_hash_ok=hashlib.sha256(sc['exact_statement'].encode('utf-8')).hexdigest()==sc['statement_sha256']
assert sha(source/'PROOF.md')==sc['proof_source']['sha256']
review={'claim':'A064-PREFIX-SECTOR-ELIGIBILITY-DEBT@1','source_proof_sha256':sha(source/'PROOF.md'),'source_statement_sha256':sc['statement_sha256'],'raw_statement_hash_matches':source_hash_ok,
 'reviewer':'A061/fleet03','verdict':'SCOPED_SECTOR_AND_CAPITAL_ARGUMENT_RECONSTRUCTION_HOLDS_NO_REPAIR',
 'scope':'Persistent full sector reference; exact pivot normalizer/child KL; optional positive-part bill and sharp half-bit eligibility guard; finite signed Snell drift; rare branch expectation; any-reference capital impossibility.',
 'independence_limit':'A061 authored one source dependency, the earlier fixed-product prefix obstruction. This is NOT a new independent full-chain acceptance of that A061 dependency. A087/A094 must supply full-chain review; no repair contributed to A064 source.',
 'validation':str(R/'out/MAIN.json'),'new_GU_result':'PROOF.md sections1--3 and2a are NEW A061 proof, independently unreviewed.'}
dump(R/'out/REVIEW.json',review)
cid='A061-GU-VALID-CLASS-ALL-PRODUCT-STOP-CAPITAL-OBSTRUCTION'
statement=('Let C be the restriction-closed class of all finite disjoint products of point signs f_m=1-2*1[x=0], bent pairs (-1)^(uv), characters and constants. '
 'Every f in C satisfies G(f)<=(19/8)I(f), with the stronger per-coordinate guard Delta_i U<=(19/8)Inf_i. '
 'On every finite fair adaptive physical restriction tree in C, V_t=(19/8)I(f_t)-U(f_t) is nonnegative, initially <=(19/8)I(f), and a supermartingale; '
 'its exact predictable drop is (19/8)Inf_(i_t)-Delta_(i_t)U. Terminal U remains paid by the SAME original influence budget, and V plus its accumulated drops is a martingale. '
 'Nevertheless, for m>=3, take N=2^(m-1) disjoint point_m factors g_m and F_m=(-1)^(uv)g_m in C. ANY supporting original reference and ANY account paying terminal KL and actual outcome KL that admits immediate v-query, actual-product reset of both children and stopping must have Account/I(F_m)>=(m^2-5m-2)/(m+1), unbounded. '
 'Full terminal H or U only strengthens that obstruction. These same sources have H(F_m)<=4I(F_m). Thus a valid hereditary GU bound and a paid nonnegative physical U-process do NOT imply cheap capital for ALL product stopping cuts, for any reference choice. Universal GU and FEI remain open.')
hyp=['Finite uniform physical cubes; entropy, U and divergences in bits. U=sum_S p(S)log2(pi(S)/p(S)), pi(S)=sum_(T containing S)p(T); zero-mass terms omitted.',
 'Factors have DISJOINT physical coordinates. Arbitrary factor count/dimension, adaptive physical query order and bounded stopping are admitted. All actual terminals remain in the explicitly defined class.',
 'Capital obstruction requires admission of immediate protected-v query and actual marginal-product replacement in BOTH children followed by stopping. It does not address a selected rule excluding that action.',
 'Reference normalized and supports actual spectrum; actual predictions/kernel and full terminal costs are retained. No factorization of an arbitrary supplied reference is assumed for the capital lower bound.',
 'Point GU all-m proof uses exact upper-set sum, convexity of A(t)+3log2(e)t^2 and elementary ln2>2/3. Finite certificate is validation only; no finite-to-infinite extrapolation.',
 'No universal original source supplier, nonproduct admissible terminal policy or arbitrary-core drift inequality is proved. No claim that GU itself implies this impossible auxiliary necessity condition.']
claim=dict(claim_id=cid,version=1,exact_statement=statement,hypotheses=hyp,statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),contributors=['A061/fleet03; A064 any-reference capital obstruction credited as source context'],
 proof_source={'path':str(R/'PROOF.md'),'sha256':sha(R/'PROOF.md'),'validation':[str(R/'out/MAIN.json'),str(R/'out/REVIEW.json')]},
 proof_dependencies=[],review_records=[{'reviewer':'A061','verdict':'AUTHOR_ANALYTIC_AND_EXACT_DIRECT_CHARACTER_CHECK_NOT_EXTERNAL_ACCEPTANCE','scope':'All-m convexity proof, every-coordinate physical drift and actual U/G sums; capital necessity reconstructed separately from A064.'}],
 status='AUTHOR_PROVED_EXACTLY_CHECKED_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=['UNREGISTERED-CANDIDATE: hereditary GU-valid cores necessarily admit O(I) capital for ALL actual-product stopping cuts under some original supporting reference'],first_unproved_line=None,next_consumers=['A064','A065','A087','A094','B20'])
assert set(claim)==set(protocol['required_per_run']['claim_fields']);dump(R/'CLAIMS.json',[claim])
progress=dict(protocol_revision=protocol['revision'],run_id=R.name,stream='B13',packet_id='A061',gap_id='G-R-MISMATCH',attempt_id='A061-stage21-GU-valid-capital-necessity-counter',
 method='Independent A064 sector/capital reconstruction; analytic upper-set GU certificate and explicitly priced physical supermartingale on the SAME capital-obstruction class; exact direct-source replay.',
 mathematical_delta='NEW GU19/8 and V=19I/8-U on hereditary point/bent/character products; all product-stop capital/I nevertheless unbounded for ANY initial reference. A064 sector/capital extension HOLDS at scoped review; own dependency not counted as independent full-chain review.',
 deliverable_status='COMPLETE_LOCAL_ARTIFACTS',mathematical_status='SCOPED_ALL_DIMENSIONAL_GU_PROCESS_AND_NECESSITY_OBSTRUCTION_PROVED; NEW_INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
 claim_versions_used=['A064-PREFIX-SECTOR-ELIGIBILITY-DEBT@1','A087-PRODUCT-HISTORY-SIGNED-COCYCLE-INSTALLATION@1','A061-FIXED-PRODUCT-ONE-PREFIX-HALFBIT-OBSTRUCTION@1'],claims_created_or_changed=[cid+'@1','A064-PREFIX-SECTOR-ELIGIBILITY-DEBT@1 scoped review record'],
 source_artifacts=[str(R/x) for x in ['OPEN_TARGET.md','PROOF.md','FROZEN_SPEC.json','REVISED_SPEC.json','out/MAIN.json','out/PILOT.json','out/REVIEW.json']],next_consumers=['A064','A065','A087','A094','B20'],
 next_action='Specify ONE narrower terminal/reference policy for arbitrary indecomposable Boolean cores and price its explicit nonnegative U correction from ORIGINAL influence, retaining old charges/full terminals. Do not demand cheap ALL-product-stop accounts even on GU-certified cores. A087/A094 independently review the new necessity counter and physical process.',
 stagnant_substantive_attempts=0,blockers=['Universal GU/FEI and arbitrary-core initial influence-priced source/drift remain OPEN. New scoped theorem independent review pending.',
 'Original4644-state audit failed its55second timing guard; drift-verifier double negation fixed. First corrected runpy invocation failed import path before mathematics. Revised1524-state direct CLI replay PASS; failures preserved, not counted as certificates.',
 'Both checklist working and completion registration failed: checklist lock held too long. Stage artifacts are complete; shared checklist closure remains blocked. No lock deletion or shared-control repair.',
 'No git/remote mutation under user write-only-A061 scope; supervisor archive/mirror/downstream-use receipts pending.',
 'Brain self-care degraded/unverified: owner100.4h/state85.0h/dream35.7h stale; affected personal context excluded from mathematical premises.'],packet_ids=['A061'])
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
dump(R/'out/ADVERSARIAL_REVIEW.json',{'status':'AUTHOR_CHECKED_NOT_EXTERNAL_ACCEPTANCE','strongest_failure_case':'Per-coordinate GU or terminal U might have been inferred from a summed bound outside a hereditary class; prove every coordinate separately via point symmetry and bent/character factors, then induct nonnegativity.',
 'checks':['Point vacuum term A(d) retained; m0/m1 endpoints separately handled.', 'Convexity A+3ct^2 proves all dimensions analytically; actual direct upper-set sums independently check m1..8.', 'Tensor closure uses literal disjoint physical coordinates and cylinders, not an invalid global reference factorization.', 'Capital counter is any-reference and an actually admitted cut; full H/U cannot lower its KL bill.', 'A064 review is no-repair and explicitly excludes author independence on its A061 dependency.', 'Corrected potential drift subtracts child potentials; original redundant predicate sign bug and timing failure disclosed.']})
dump(R/'out/ARCHIVE_RECEIPT.json',{'status':'SUPERVISOR_ARCHIVE_PENDING','git_executed':False,'remote_mutation':False,'scope':'User authorizes research writes only inside A061; supervisor copies completed runs. No remote save/mirror/native-ingestion claimed.'})
sourcepaths=[P,ROOT/'BOARD.md',ROOT/'claude/B13/STREAM_NOTES.md',source/'PROOF.md',source/'CLAIMS.json',
 ROOT/'agents/A065/runs/20261023T133350Z-fleet03-A065-stopping-rule-falsifier/PROOF.md',
 ROOT/'agents/A087/runs/20261023T121304Z-fleet03-A087-restriction-referee/PROOF.md',
 HOME/'runs/20261023T113614Z-fleet03-A061-entropy-process/PROOF.md',
 HOME/'runs/20261023T113614Z-fleet03-A061-entropy-process/code/arith.py',
 HOME/'runs/20261023T113614Z-fleet03-A061-entropy-process/code/independent_oracle.py']
dump(R/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p)} for p in sourcepaths])
dump(R/'out/CONTROL_READ_RECEIPT.json',{'private_order_url':'https://github.com/yspennstate/math-research-brain/blob/main/scheduled_tasks/work/shared/full-fei-only-2026-10-12/ORDER.md','focus_revision':'2026-10-14.1 / GU-LASER-20261014','focus_assignment':'B13 explicit nonnegative correction, physical rule, drift/terminal U and dimension-independent bound; new scoped certificate and false necessity bridge in PROOF.md','universal_H_from_U_reduction_used':False,'note':'No reliance on the unread original universal H/U reduction; GU validity here and the source-family H bound are proved directly.'})
report=f'''# A061 stage21: a GU-valid physical process does not fund every product reset

## exact target, quantifiers, hypotheses and units

The frozen target is the proposed necessity bridge that a restriction-closed Boolean class with uniform GU admits O(I) capital for ALL actual-product stopping cuts under some supporting original reference. It is FALSE. For the SAME class of all finite disjoint point-sign/bent/character products, this stage proves GU with ONE pair(a,b)=(19/8,0) and an explicitly priced nonnegative physical supermartingale, but any such account has unbounded capital/I. Every factor count, dimension, physical history and terminal U is retained. Units bits. This does not refute GU or FEI. Universal GU and full FEI remain OPEN.

## sources actually read, revisions and theorem locators

BOARD2026-10-23 13:59UTC; B13 lead v2; own STATUS/prior stage20 proof and helpers; protocol2026-10-11-execution-v2. A06420261023T130211Z PROOF sections1--5 and CLAIMS supplies A064-PREFIX-SECTOR-ELIGIBILITY-DEBT@1: exact all-prefix sector bill, rare debt growth and any-reference all-product-stop capital obstruction. A08720261023T121304Z PROOF independently accepts our stage20 obstruction and proves the all-physical product cocycle/one actual install at2A. A06520261023T133350Z PROOF reconstructs that extension, closing our former NEXT. These new results were consumed rather than repeated as new claims. Source byte pins are in out/SOURCE_RECEIPTS.json. The authenticated private ORDER and GU focus contract2026-10-14.1 were read: B13 must connect an explicit correction/rule to GU or a sufficient U process. Our new certificate tests an exact missing necessity bridge and includes that process. No unread universal H-from-U reduction is used; all GU and H claims here are derived directly. Current user campaign window overrides old fleet01 endpoints. No unrelated brain/film work was performed.

## complete derivation or exact first unsupported line

PROOF.md sections1--3 derive the actual point law with d=2^(1-m), p_empty=(1-d)^2 and nonempty p=d^2. Its COMPLETE upper-set functional is U_m=A(d)+md-md^2, A(d)=-2(1-d)^2log2(1-d). A physical query leaves one constant and one smaller point, giving G_m/I_m=1+(m-2)d+[A(d)-A(2d)/2]/d. The function A(t)+3log2(e)t^2 is convex on[0,1], so its midpoint inequality bounds the bracket by3log2(e)d^2. For m>=3 the resulting bound decreases with m; ln2>2/3 gives G/I<19/8. m2 has ratio2; m1/constants have G=U=0. No endpoint division or vacuum term is omitted.

Disjoint products have multiplicative p/pi, hence additive U,I,G. Bent pairs have(I,U,G)=(1,1,2), while their physical descendants are characters/constants. This proves hereditary GU19/8 for all finite such products. Symmetry within each point factor gives the stronger guard at EVERY physical coordinate. Thus ANY predictable relevant-coordinate rule has V_t=19I(f_t)/8-U(f_t)>=0, exact drop19Inf_(i_t)/8-Delta_(i_t)U>=0, and V plus accumulated drops is a martingale on the revealed-bit filtration. At EVERY bounded stopping cut U_root<=19E(sum spent Inf)/8+E U_terminal<=19I_root/8. The terminal U is paid from the SAME original influence account, not dropped or renewed.

Nevertheless take N=2^(m-1) point_m factors g_m and a fresh bent pair F_m. Point marginal entropy M>=md(m-1), while its full entropy H<=2d(2m+1); thus TC(g_m)>=m^2-5m-2 and I(F_m)=m+1. For ANY supporting initial reference, an admitted immediate v-query and actual-product resets in BOTH children forces terminal KL TC(g_m), plus nonnegative actual outcome KL. Capital/I therefore tends to infinity. Full terminal H=H(g_m) is retained and would strengthen the bill to M(g_m). These same F_m obey H<=4I and the hereditary GU certificate. Consequently a paid U process does NOT require the broad account demanded by that false bridge.

PROOF.md section4 independently reconstructs A064's persistent FULL sector form Q=w_b R_b/2, fair-zero predictions r, exact K_child=D_b+log(r_b/w_b), ZERO pivot erasure, optional reserve B=mean[log(w_b/r_b)-(D_b-TC_b)]_+, and bound B<=1/2+mean[TC_b-D_b]_+. The positive part is before averaging. Product eligibility need not persist under prefixes. Its finite signed Snell recursion gives K+G+accumulated O supermartingale at all admitted cuts, including the reset boundary. Its rare-branch invariant is an expectation, not pathwise conservation. Scoped verdict HOLDS, no repair. A061 authored one source dependency, so this is NOT an independent full-chain review of that older A061 claim; A087/A094 acceptance remains separate.

No unsupported line remains in the scoped new theorem. The first universal unpaid line is an ORIGINAL influence-priced correction for an explicit narrower terminal/reference policy on arbitrary indecomposable Boolean cores. Requiring cheap capital for ALL product stops cannot be that missing lemma, even if GU has already been certified on the cores.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded computation; after the original timing failure REVISED_SPEC.json froze a smaller corrected audit. `python -X utf8 code/check.py` now runs the bounded pilot then corrected main. Integer direct characters, independently counted physical edges, Fraction full references, prime-log forms and96-bit outward32-term atanh signs certify all comparisons. No floating search or extrapolation establishes the theorem.

- Pilot PASS: {pilot['counts']['pivot_states']} pivot states, {pilot['author_predicates']} author and {pilot['independent_transport_predicates']} direct-transport predicates; {pilot['seconds']:.3f}s. All normalized core pairs on0/1 bits and four full references.
- Corrected main PASS: {main['counts']['pairs']} core pairs, {main['counts']['reference_entries']} reference entries,1524 ordered-prefix pivot states,3048 actual reset children and {main['counts']['ordinary_queries']} ordinary queries; {main['seconds']:.3f}s. Includes four selected2-bit and four3-bit pairs, all orders/outcomes, deterministic product endpoints, unequal sector weights, correlated and different-product references. A negative eligibility witness is actually exercised and saved. Source full truth tables and references are checked against the independent sector representation at every prefix.
- Main primary predicates: {main['author_predicates']} author + {main['independent_transport_predicates']} independent direct-transport = {primary}. Another {main['auxiliary_scalar_predicates']} scalar-helper checks and the pilot are separate, excluded from that total. Exact actual U/G on point dimensions1..8 is checked directly against the analytic law and19/8 residual. All-m/all-factor/all-history coverage is the analytic proof, not this finite check.

The original4644-state audit reached its final55-second runtime assertion and FAILED that guard; no main PASS file was saved. A redundant drift predicate had double-negated child terms; corrected to subtract them. First corrected invocation via runpy failed import resolution before mathematics. Both issues are disclosed in REVISED_SPEC.json/out/DEVELOPMENT_LOG.json; the final direct CLI run above is the certificate. No failed run is counted as PASS or added to primary totals. The revised job was frozen at100MB and120seconds; pilot55seconds. No >300MB job, GPU, compiler, detached work, automatic dimension increase, other-agent write, or process shedding occurred. No formal certificate is claimed.

## proof dependencies and changed downstream conclusions

New {cid}@1 is self-contained author proof/exactly checked, pending external review. A064's original capital obstruction is credited; the new contribution is its coexistence with a concrete hereditary GU bound and a FULLY PAID physical U-process. This is not a claim to have improved arbitrary-core initial funding. A064's scoped new argument HOLDS under reconstruction with the contributor-conflict limitation above; details and source hashes are in out/REVIEW.json. A087/A065's all-product-history2A result is consumed as closure of our earlier NEXT, not restated as new work. No source tree or shared index was edited. A064/A065/A087/A094/B20 are named local consumers; this is a handoff, not a downstream-use receipt.

## one next mathematical action and independent reviewer

Specify ONE narrower physically selected terminal/reference class for an arbitrary indecomposable Boolean core, with an explicit nonnegative U correction whose ORIGINAL cost is O(I) and whose complete terminal U is paid. Use the GU-valid capital obstruction as a mandatory guard against reintroducing ALL product stops. A087/A094 should independently verify the convexity/GU proof, every-coordinate drift and any-reference capital counter together; A064 should consume the precise false-necessity boundary. Another point dimension, product-history depth or universal product-KL/I estimate cannot remove the arbitrary-core hypothesis.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json, complete proof/specs/code/outputs/review and rolling files are saved locally. code/finalize.py verifies exact protocol fields, raw UTF-8 statement/proof hashes, compatibility identity, report headings/last paragraph, two-line STATUS and actual byte readback in out/PERSISTENCE_RECEIPTS.json. No local save blocker. Research writes remain inside A061; git/remote mutation were prohibited by the user and supervisor copies completed runs. Archive/mirror, new external review, native ingestion and downstream use are pending and not claimed. Checklist working registration failed on its shared lock; no lock was removed. Brain self-care remains degraded/unverified: owner100.4h, state85.0h and dream35.7h stale; affected personal context was excluded from proof premises.

**Universal bridge:** C019 stopping-tree payment and C024 history transfer advance by separating a sufficient physical U-process from an unnecessarily strong reference-payment demand: a SAME-original-budget V=19I/8-U works on a hereditary GU19/8 class, but ALL product-reset capital/I is unbounded for every reference on that very class. A064's exact signed eligibility mechanism is reconstructed at scope. What remains is a narrowed, explicitly selected and influence-funded U terminal/reference policy for arbitrary cores. NEXT removes that arbitrary-core hypothesis without demanding the now-refuted broad account, rather than producing another isolated point-class estimate.
'''
wr(R/'REPORT.md',report)
wr(HOME/'STATUS.md',f'STATE: A061 stage21 complete: hereditary point/bent class GU19/8 and V=19I/8-U paid for ALL physical histories, yet ALL product-stop capital/I unbounded ANY reference; A064 scoped review HOLDS;{primary} main predicates PASS; new review pending; FEI OPEN.\nNEXT: A087/A094 review A061-GU-VALID-CLASS-ALL-PRODUCT-STOP-CAPITAL-OBSTRUCTION@1 in runs/20261023T135818Z-fleet03-A061-entropy-process; A064 consume false necessity bridge; construct narrower fully paid U terminal/reference policy for arbitrary indecomposable cores.\n')
entry=f'\n2026-10-23 stage21 (20261023T135818Z): consumed independent acceptance of stage20 and A087/A065 closure of all physical product histories/one actual tensor installation. A064 new sector/optional-debt/capital proof independently reconstructed at scope, own dependency conflict disclosed. NEW analytic GU19/8 for hereditary disjoint point/bent/character products; V=19I/8-U nonnegative physical supermartingale, exact drift and FULL terminal U paid from same original influence. SAME class has any-reference ALL-product-stop capital/I diverging by point tensor source, refuting proposed necessity bridge but not GU/FEI. Corrected1524-state audit+actual point m1..8 PASS,{primary} primary predicates; original55sec timing failure, redundant drift sign and runpy import failure preserved/disclosed. No heavy/formal/remote work. Local protocol/proof/rolling files saved; new external review and supervisor archive pending; universal narrower arbitrary-core U policy remains OPEN.\n'
if entry.strip() not in rd(HOME/'WORKLOG.md'):wr(HOME/'WORKLOG.md',rd(HOME/'WORKLOG.md')+entry)
lesson='''
Stage21 durable fact (2026-10-23): Point_m, d=2^(1-m), has COMPLETE U=A(d)+md-md^2, A=-2(1-d)^2log2(1-d). Every query leaves constant/point_(m-1). G/I=1+(m-2)d+[A(d)-A(2d)/2]/d. Convexity A+3log2(e)t^2 yields bracket<=3log2(e)d^2; m>=3 decreasing bound<19/8, m2ratio2,m1/constants0. Disjoint point/bent/character products and ALL physical descendants inherit same GU19/8 AND per-coordinate guard; V=19I/8-U>=0 is an influence-priced supermartingale for ANY physical rule, exact drop19Inf/8-DeltaU, full terminal U paid once. Nevertheless N=2^(m-1) point_m factors plus fresh bent pair has I=m+1, H<=4I and forces ANY account admitting immediate pivot+both product stops to pay>=m^2-5m-2, ANY supporting initial reference. Thus GU validity/paid U process DOES NOT imply cheap ALL-product-stop capital. Narrow selected terminal/reference policy is essential, not another initial-reference retuning. A064 sector formula reconstructed unchanged: B=mean[log(w/r)-(D-TC)]_+, full reference incl zeros, product eligibility nonhereditary. Source review has own-dependency independence limitation. Exact corrected1524-state audit plus direct point m1..8; all-dimension proof analytic. NEXT narrower arbitrary-core U policy, not deeper product prefixes.
'''
if lesson.strip() not in rd(HOME/'LEARNED.md'):wr(HOME/'LEARNED.md',rd(HOME/'LEARNED.md')+lesson)
assert len(rd(HOME/'STATUS.md').splitlines())==2
assert obj(R/'PROGRESS.json')==obj(R/'PACKET_DELTA.json')
assert sha(R/'PROOF.md')==claim['proof_source']['sha256']
assert hashlib.sha256(obj(R/'CLAIMS.json')[0]['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
for h in protocol['required_per_run']['report_fields']:assert '\n## '+h+'\n' in rd(R/'REPORT.md')
assert rd(R/'REPORT.md').rstrip().split('\n\n')[-1].startswith('**Universal bridge:**')
receipts=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and '__pycache__' not in p.parts and p.name!='PERSISTENCE_RECEIPTS.json':
  assert p.stat().st_size<20_000_000;receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
 p=HOME/name;receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
dump(R/'out/PERSISTENCE_RECEIPTS.json',{'status':'LOCAL_READBACK_PASS','files':receipts,'scope':'Local persistence only; not remote archive, independent review or downstream use.'})
for row in obj(R/'out/PERSISTENCE_RECEIPTS.json')['files']:assert sha(row['path'])==row['sha256']
print(json.dumps({'status':'PASS','primary_predicates':primary,'source_raw_statement_hash_matches':source_hash_ok,'receipt_files':len(receipts),'protocol':'PASS','statement_proof_hashes':'PASS','new_review':'PENDING','full_GU_FEI':'OPEN','remote':'NO_MUTATION'}))
