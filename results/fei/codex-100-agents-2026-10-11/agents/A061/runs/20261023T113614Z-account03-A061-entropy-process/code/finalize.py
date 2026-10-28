"""Stage20: persist scoped theorem, exact checks and honest universal gap."""
from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]; HOME=R.parents[1]; ROOT=HOME.parents[1]
P=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def rd(p):return Path(p).read_text(encoding='utf-8')
def wr(p,s):Path(p).write_text(s,encoding='utf-8',newline='\n')
def obj(p):return json.loads(rd(p))
def dump(p,x):wr(p,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
protocol=obj(P)
full=obj(R/'out/FULL_SOURCE.json'); direct=obj(R/'out/DIRECT_REPLAY.json'); pilot=obj(R/'out/PILOT.json')
assert full['status']==direct['status']==pilot['status']=='PASS'
assert direct['independent_assertions']==157 and direct['source_rows']==2048
cid='A061-FIXED-PRODUCT-ONE-PREFIX-HALFBIT-OBSTRUCTION'
statement=('For every Boolean core f and normalized supporting reference R, the fresh bent extension F(U,V,Y)=(-1)^(UV)f(Y), '
 'Q=uniform_4 tensor R, preserves the complete signed inherited-reference/product-reset booking problem under every finite adaptive ordinary Y history followed by protected V. '
 'If R is the actual core product reference, Q is the actual original full product. There is an explicit Boolean family F_l on3l+5 bits, l>=2, '
 'with EVERY influence1/2 and original uniform product reference, for which ONE prescribed ordinary selector query before V has erasure E=0 and requires EXACT extra root reserve '
 'B_l=(l+1-log2(1-2^(-l-1)))/2 for optional inherited/product stops after V, including any subsequent inherited-reference physical continuation. '
 'Both sibling reset debits are positive; full terminal H is retained. B_l/Inf_U tends to infinity, and B_l divided by the two-query influence spend1 tends to infinity. '
 'The V-first mode instead has reserve0. At l2 the11-bit witness has H17/2, I11/2, K5/2 and B=3-(log2 7)/2>3/2. '
 'If the SAME original owner S=4I-H is supplied with booked K and unrelated old consumption omega<=S/4, then B_l<S/8 and S-omega-K-B_l>S/8. '
 'This refutes hereditary fixed-half-bit eligibility after one prescribed ordinary prefix, not A064 immediate-pivot eligibility or FEI.')
hyp=[
 'Finite uniform physical cube, predictable coordinate choices, fair physical outcomes; bits for entropy/KL. Supporting references normalized and transported by the actual coherent kernel with fair extension on EVERY source-zero row.',
 'Generic reduction permits only ordinary Y queries before protected V. Exact equality concerns corresponding finite declared policies and their signed pending reserve; reference-only rows are retained.',
 'Explicit family is PROOF.md section1: field bilinear h_l, inner affine carrier/selector, then a fresh independent bent pair U,V. Original reference is the genuine full source marginal product, not an arbitrary source-matching law.',
 'Declared expensive order queries inner selector s once, then outer V. Each terminal may keep inherited KL or reset to actual product; after reset arbitrary finite physical continuation must keep inherited references. No additional unpaid product reset is admitted.',
 'Sharp lower bound uses the admitted immediate post-reset stopping cut. It does not assert a lower bound for every prescribed later continuation, every order, or an existentially selected tree.',
 'Owner repair is conditional on supplied UNUSED original S=4I-H, full original K booked once and unrelated omega<=S/4. Nested pending theta is topped up by B-theta only; consumed debits remain in omega. No owner renewal or universal owner availability is claimed.'
]
claim=dict(claim_id=cid,version=1,exact_statement=statement,hypotheses=hyp,
 statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),contributors=['A061/account03'],
 proof_source={'path':str(R/'PROOF.md'),'sha256':sha(R/'PROOF.md'),'validation':[str(R/'out'/x) for x in ['FULL_SOURCE.json','DIRECT_REPLAY.json','PILOT.json']]},
 proof_dependencies=[{'claim':'A061-PRODUCT-REFERENCE-LOCAL-PRICE-OBSTRUCTION@1','scope':'Field fixture provenance; source spectrum/reference formulas reconstructed in PROOF.md section6 and exact actual-source replay.'}],
 review_records=[{'reviewer':'A061','verdict':'AUTHOR_PROOF_AND_TWO_REPRESENTATIONS_CHECKED_NOT_EXTERNAL_ACCEPTANCE','scope':'Integer FWHT/reference transport versus independently implemented direct characters, physical edges and normalized reference transport. Shared pinned scalar log arithmetic disclosed.'}],
 status='AUTHOR_PROVED_EXACTLY_CHECKED_PENDING_INDEPENDENT_REVIEW',supersedes=[],
 refutes=['UNREGISTERED-CANDIDATE: A064 immediate fixed-product half-bit reserve stays sufficient after one prescribed ordinary query before protected pivot',
 'UNREGISTERED-CANDIDATE: a dimension-independent multiple of just that two-query physical influence spend pays these product resets'],
 first_unproved_line=None,next_consumers=['A064','A065','A087','A094','B20'])
assert set(claim)==set(protocol['required_per_run']['claim_fields']);dump(R/'CLAIMS.json',[claim])
progress=dict(protocol_revision=protocol['revision'],run_id=R.name,stream='B13',packet_id='A061',gap_id='G-R-MISMATCH',
 attempt_id='A061-stage20-genuine-product-one-prefix-loss',method='Exact bent-carrier reduction of signed reset booking; all-dimensional actual Boolean field family; two exact source/reference implementations.',
 mathematical_delta='Fixed-product eligibility is NOT hereditary after even one ordinary query, with g=h and zero erasure. Exact reserve B_l grows unbounded versus half bit/two-query spend; same original nonlocal owner repair leaves>S/8. Generic bent extension preserves arbitrary core history-reset problem exactly.',
 deliverable_status='COMPLETE_LOCAL_ARTIFACTS',mathematical_status='SCOPED_ALL_DIMENSIONAL_OBSTRUCTION_AND_CONDITIONAL_REPAIR_PROVED; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
 claim_versions_used=['A061-PRODUCT-REFERENCE-LOCAL-PRICE-OBSTRUCTION@1','A064-SHARP-PRODUCT-ELIGIBLE-NONAFFINE-RESET@1','A087-PROTECTED-PIVOT-PHASE-LIABILITY@1'],
 claims_created_or_changed=[cid+'@1'],source_artifacts=[str(R/x) for x in ['PROOF.md','FROZEN_SPEC.json','COUNTER_SPEC.json','out/FULL_SOURCE.json','out/DIRECT_REPLAY.json','out/PILOT.json']],
 next_consumers=['A064','A065','A087','A094','B20'],
 next_action='Construct a hereditary nonlocal original-owner/reference policy across an ordinary query removing a reference-only cell; preserve signed K/E and consumed charges. A087/A094 independently review the new fixed-product counter/reduction; A064 consumes the exact boundary on its no-prefix theorem.',
 stagnant_substantive_attempts=0,blockers=[
 'Full FEI and universal influence-priced hereditary owner/reference supply remain OPEN; product K/I cannot be universally bounded.',
 'New scoped claim independent review pending; predecessor stage19 independently HOLDS by A087, not acceptance of this new claim.',
 'Planned large census cancelled after analytic counterfamily; fresh memok exit1 physical3.2GB/commit3.5GB free also bars >300MB work. Formal compiler not started; no Lean verdict.',
 'Archive main GET returned404 Branch not found; no git or remote mutation. Supervisor mirror/downstream-use receipts pending.',
 'Brain self-care degraded/unverified: stale owner/state/dream context and two attached-document integrity/lock failures; affected context not used as proof premises.'],packet_ids=['A061'])
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
dump(R/'out/FORMAL_ADMISSION.json',{'status':'NOT_STARTED_NO_FORMAL_VERDICT','fresh_memok_exit':1,'free_physical_GB':3.2,'free_commit_GB':3.5,'heavy_jobs_started':False,'note':'No compiler started. Tiny exact Python jobs stayed below300MB estimates. Stale governor snapshot was not treated as fresh admission.'})
dump(R/'out/ARCHIVE_RECEIPT.json',{'status':'REQUESTED_MAIN_BRANCH_ABSENT','repository':'yspennstate/math-open-problems','readback':'Fresh GitHub GET branches/main:404 Branch not found','git_executed':False,'remote_mutation':False,'commit':None,'next':'Supervisor archive/mirror; no branch created.'})
sources=[P,ROOT/'BOARD.md',ROOT/'claude/B13/STREAM_NOTES.md',
 ROOT/'agents/A064/runs/20261023T105821Z-account03-A064-global-debt-potential/PROOF.md',
 ROOT/'agents/A064/runs/20261023T105821Z-account03-A064-global-debt-potential/CLAIMS.json',
 ROOT/'agents/A065/runs/20261023T112150Z-account03-A065-stopping-rule-falsifier/PROOF.md',
 ROOT/'agents/A087/runs/20261023T061410Z-account03-A087-restriction-referee/PROOF.md',
 HOME/'runs/20261023T051706Z-account03-A061-entropy-process/PROOF.md',
 HOME/'runs/20261023T051706Z-account03-A061-entropy-process/code/direct.py']
dump(R/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p)} for p in sources])
dump(R/'out/ADVERSARIAL_REVIEW.json',{'status':'AUTHOR_RECONSTRUCTION_NOT_EXTERNAL_ACCEPTANCE',
 'strongest_failure_case':'A bad prescribed prefix could be mistaken for failure of every tree or FEI; the V-first control has reserve0 and H/I<=18/11.',
 'checks':['Actual original product and every influence independently reconstructed; no arbitrary Q=p substitution.',
 'All reference-only mass retained with fair zero rows. Fresh outer bent tensor has FULL spectral support; no invalid general tensorization through a spectral-zero factor.',
 'Signed E credit retained and equals0; both sibling reset debits positive; complete terminal H+KL and old pipeline retained.',
 'B is allocated once. Same actual outer owner differs by2 from the predecessor inner owner. Old consumed charges are never relabelled as pending.',
 'Independent direct-character implementation checks full2048-row source and actual references. Shared prime-log arithmetic disclosed.',
 'All-l result analytic, not extrapolated from l2. A064 immediate theorem and A065 global mixture theorem are not refuted.']})
report=f'''# A061 stage20: one ordinary query destroys fixed-product half-bit eligibility

## exact target, quantifiers, hypotheses and units

Resolve A064's next boundary: does its immediate-pivot half-bit payment survive ONE ordinary query at the actual original product reference? It does not. PROOF.md proves an all-dimensional Boolean counterfamily with identical protected-pivot cores g=h and exact extra reserve B_l=(l+1-log2(1-2^(-l-1)))/2. A generic fresh bent carrier preserves the entire core reference/reset booking problem under every finite adaptive ordinary history. Physical outcomes are fair; entropy/KL units bits. References use the actual coherent kernel and fair extension on EVERY source-zero row. Full FEI is OPEN; this is a bad prescribed-prefix payment obstruction, not an FEI disproof or failure of every query rule.

## sources actually read, revisions and theorem locators

BOARD dated2026-10-23 11:35UTC, B13 lead v2, own STATUS/rolling facts, prior stage19 proof and exact helper, and execution protocol2026-10-11-execution-v2. A064 20261023T105821Z PROOF/CLAIMS gives A064-SHARP-PRODUCT-ELIGIBLE-NONAFFINE-RESET@1: immediate original-product half bit is sharp, and explicitly leaves an ordinary prefix unpaid. A065 20261023T112150Z PROOF advances full inherited-reference outcome allowance for tensor modules and names a query that can remove a reference-only cell. A087 20261023T061410Z PROOF independently accepts our stage19 affine-pivot theorem and proves protected-pivot phase liability; raw marginal liability remains unbounded/I. These new results were consumed, not rederived as new claims. Source hashes: out/SOURCE_RECEIPTS.json. Campaign/paper baseline remains inherited; no new external-paper theorem is used. Current owner campaign deadline supersedes the older protocol clock.

## complete derivation or exact first unsupported line

For ANY Boolean f and normalized supporting R, F=(-1)^(UV)f with Q=uniform4 tensor R has K_F=K_f,H_F=H_f+2. Every ordinary core restriction preserves this tensor and all actual K/E/O increments, including reference-only rows. At protected V, the prediction is fair and E_V=O_V=0. Both children have core K, H and product TC. Therefore the signed optional-reset recursion B=max(0,terminal requirement,max_i(mean B_child-E_i)) is exactly the core recursion at every finite declared policy class. This proves a universal reduction, not only a finite witness.

Use the GF(2^l) bilinear core h_l(a,b,x)=psi(a)(1-2*1[x=ab]), m=3l, H_l=H(h_l). The inner affine carrier/selector f_l chooses C_1 or C_h with one physical bit s; then add the fresh bent pair. All3l+5 physical influences are1/2, hence the GENUINE original product Q is uniform. The exact original quantities are H=6+H_l/2, I=(m+5)/2, K_0=m-1-H_l/2 and S_outer=4I-H=2m+4-H_l/2.

Query s once before outer V. Actual reference predictions are1/(2q),r=1-1/(2q), E_s=0 and O_s=(l-1-log2 r)/2. Actual normalized inherited KLs are K_G=2l-1 and K_H=m-H_l+log2 r. Query V next: its E and O are0 and both children retain those actual KLs. Product KLs are TC_G=m,TC_H=m-H_l, giving TWO positive reset debits J_G=l+1 and J_H=-log2 r. Thus EXACT extra original-root booking B_l=mean J=1+O_s. Necessity comes from resetting all four children and stopping: mean TC_terminal+mean accumulated O=K_0+B_l. Sufficiency follows by allocating these very signed debits once; current K pays any later inherited-reference physical continuation. No further unpaid reset is allowed. Mean full terminal H=2+H_l/2 is retained, so the entropy decrement is4. PROOF.md supplies the complete derivation, actual reference-only masses and filtration increments.

B_l/Inf_U=l+1-log2 r tends to infinity. The two actual queried influences s,V spend1 in total, so no fixed multiple of JUST that spend pays this policy. Already l2 gives an11-bit actual Boolean source with H17/2,I11/2,K5/2 and B=3-(log2 7)/2, whose excess over1/2 is>1. The exact V-FIRST negative control instead needs B=0; an existential rule can avoid the expensive order. These functions have H/I<=18/11, so they do not disprove FEI.

The same ORIGINAL nonlocal owner repairs this family, conditionally on unused owner availability. Retain full pipeline K_0 and old unrelated omega<=S_outer/4. If theta was a nested pending reserve, top up by B_l-theta only; consumed costs remain spent. K_0<S_outer/2, r>=7/8 and (8/7)^4<2 imply B_l<S_outer/8; hence S_outer-omega-K_0-B_l>S_outer/8. S_outer is the new actual outer source owner, equal to predecessor inner owner+2; no balance is renewed after s. There is no unsupported line in the scoped theorem. The first universal unpaid line is a hereditary reference/owner selection and transfer policy that can fund history-dependent reserves while retaining all actual K/E and old charges. Universal product K/I pricing is false elsewhere and is not assumed.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded the bounded census pilot. COUNTER_SPEC.json froze the changed targeted mechanism before the actual11-bit certificate. No automatic dimension escalation, detached work, GPU, heavy job or other-agent mutation occurred. Integer/Fraction spectra, physical edges, exact normalized references and prime-log forms with96-bit outward32-term atanh bounds certify all signs. Runtimes below are job-reported, not billing/capacity claims.

- `python -X utf8 code/check.py pilot`: out/PILOT.json PASS,13680 exact assertions,64 normalized two-core-bit pairs,192 pivot states and64 ordinary data queries; {pilot['seconds']:.3f}s. No half-bit failures in that finite domain. Initial syntax error was repaired and the pilot rerun; out/DEVELOPMENT_LOG.json preserves it.
- `python -X utf8 code/full.py`: out/FULL_SOURCE.json PASS,14208 exact assertions,{full['seconds']:.3f}s. Full2048-row actual source, integer FWHT, every physical influence, original product, all four actual pivot/reset children and eight post-query children. Checks full terminal H/KL, actual signed chain, V-first reserve0, positive two-sibling reset debits and same-owner surplus.
- `python -X utf8 code/replay.py`: out/DIRECT_REPLAY.json PASS,157 independent-implementation assertions,{direct['seconds']:.3f}s. Direct character sums over4194304 character terms, separate physical-edge/source construction and coherent reference transport; same pinned scalar interval arithmetic. Another8136 auxiliary scalar checks are reported separately. This is author reproduction, not external independent acceptance.

Primary targeted total14365=14208+157. Pilot13680 and auxiliary8136 are excluded to avoid inflating the primary count. The all-l proof is analytic and includes the entropy/support calculation for h_l; no finite-to-infinite extrapolation is made. The planned n2,3 broad pair census was CANCELLED after the analytic counterfamily, not executed. Fresh memok exit1 (physical3.2GB,commit3.5GB free) independently prohibited >300MB work; formal compiler NOT_STARTED and no Lean verdict claimed. Exact jobs were estimated100MB/65MB. The governor snapshot was stale and not treated as fresh admission or restarted.

Brain self-care remains degraded/unverified: owner model98.0h, state-of-mind82.6h and dream33.3h stale, plus integrity/lock failures for two attached BC23 context documents. Personal/context recall remains affected; none of those failed/stale notes is a mathematical premise here.

## proof dependencies and changed downstream conclusions

New {cid}@1 is author proved, exactly checked and pending independent review. Field fixture provenance is A061-PRODUCT-REFERENCE-LOCAL-PRICE-OBSTRUCTION@1, with all needed field facts reconstructed here. The A064/A065/A087 new results are consumed interfaces/context; this counter/reduction is self-contained. A087's independent acceptance of our stage19 theorem is recorded as predecessor review only. A064's no-prefix theorem is NOT refuted. The false extension is hereditary half-bit eligibility after one prescribed ordinary query, even with g=h. Affine phase liability alone cannot fix this inherited-reference funding loss. No predecessor source was edited. Named local consumers A064/A065/A087/A094/B20 are handoff targets, not claimed downstream-use receipts. Raw UTF-8 statement hash and proof-source hash are saved in CLAIMS.json.

## one next mathematical action and independent reviewer

Construct a hereditary nonlocal ORIGINAL-owner/reference transfer across one ordinary query that removes a reference-only cell, preserving actual signed K/E, full terminal H+KL and consumed charges. Use this one-prefix family as a compulsory failure guard; adding another affine depth or small pair census cannot repair its unbounded local price. A087/A094 should independently reconstruct the generic bent reduction, exact minimal booking and conditional SAME-owner repair. A064 can consume the precise boundary on its immediate theorem; A065 can use the reference-only-cell continuation frontier.

## actual persistence receipts or precise save blocker

All four protocol files, PROOF.md, frozen specs, code and exact outputs are locally saved; STATUS is two lines and WORKLOG/LEARNED updated. out/PERSISTENCE_RECEIPTS.json hashes actual bytes/sizes and code/finalize.py rereads them, protocol fieldsets, statement/proof hashes and identical compatibility copies. No local save blocker. Fresh archive GET branches/main returned404 Branch not found; no git, branch creation or remote mutation. Supervisor archive/mirror, external acceptance and downstream mathematical use remain pending.

**Universal bridge:** C019 stopping-tree payment and C024 history transfer advance by an exact universal bent-carrier reduction and an all-dimensional diagnosis of the first ordinary-prefix failure: B_l=(l+1-log2 r)/2 is unbounded relative to the old half bit and the two queried influences even at the genuine original product root. The SAME nonlocal original owner pays this family with>S_outer/8 remaining after full pipeline and old quarter. What remains is a hereditary influence-funded reference/owner transfer, especially when an ordinary query removes reference-only mass. NEXT attacks that exact universal funding step rather than another isolated affine-class bound.
'''
wr(R/'REPORT.md',report)
wr(HOME/'STATUS.md','STATE: A061 stage20 complete: one ordinary prefix at GENUINE product root defeats half-bit even g=h; exact B_l unbounded/local spend, SAME owner leaves>S_outer/8;14365 targeted checks PASS; review pending; FEI OPEN.\nNEXT: A087/A094 review A061-FIXED-PRODUCT-ONE-PREFIX-HALFBIT-OBSTRUCTION@1 in runs/20261023T113614Z-account03-A061-entropy-process; A064/A065 consume; construct hereditary nonlocal owner/reference transfer when an ordinary query removes reference-only mass.\n')
entry='\n2026-10-23 stage20 (20261023T113614Z): consumed A064 sharp immediate half-bit/A065 global reference/A087 phase liability and acceptance of stage19. Fresh bent extension preserves arbitrary core signed reset booking at every adaptive ordinary history. Exact all-l Boolean field family, actual original product, g=h: ONE selector query before outer pivot needs B_l=(l+1-log r)/2, E=0, both positive debits; local half-bit/two-query price fails unboundedly. V-first needs0, H/I<=18/11: FEI not refuted. SAME conditional original S_outer with full K/old quarter pays B<S/8 and leaves>S/8.14208 FWHT+157 independent direct assertions PASS;13680 pilot/8136 auxiliary excluded. Broad census cancelled, syntax error preserved/repaired, memok1 bars heavy/formal work. Local proof/protocol files saved; new independent review and archive/mirror pending; main404/no remote mutation.\n'
if entry.strip() not in rd(HOME/'WORKLOG.md'):wr(HOME/'WORKLOG.md',rd(HOME/'WORKLOG.md')+entry)
lesson='''
Stage20 durable fact (2026-10-23): F=(-1)^(UV)f with fresh uniform bent spectrum preserves ALL core actual reference/reset booking histories exactly: Q=uniform4 tensor R, ordinary core kernels including fair zero rows commute, K/E/O unchanged; protected V fair with E=O=0, child H=Hcore and TC=TCcore. Genuine product eligibility therefore survives the embedding but does NOT become hereditary. Outer-wrapped field selector on3l+5 bits has every Inf1/2 and genuine uniform product. One ordinary s before outer V gives rH=1-2^(-l-1), KG=2l-1,KH=3l-H_l+log rH, reset debits l+1 and-log rH, exact B=(l+1-log rH)/2. E_s=0, BOTH sibling debits positive. B unbounded/half-bit and queried influence spend1, even g=h. V-first has B0, H/I<=18/11; this is neither FEI nor every-rule failure. Same actual outer owner S=6l+4-H_l/2 (different from predecessor inner owner by+2), full K and old omega<=S/4 retained, has B<S/8 and spare>S/8 conditional on unused owner supply. l2:11 bits,H17/2,I11/2,K5/2,B=3-.5log7, B-.5>1.14365 targeted exact assertions in two implementations; all-l proof analytic. NEXT hereditary nonlocal reference/owner transfer through a query removing reference-only cells, not deeper affine prefix enumeration or universal product-K/I pricing.
'''
if lesson.strip() not in rd(HOME/'LEARNED.md'):wr(HOME/'LEARNED.md',rd(HOME/'LEARNED.md')+lesson)
assert obj(R/'PROGRESS.json')==obj(R/'PACKET_DELTA.json')
assert len(rd(HOME/'STATUS.md').splitlines())==2
assert sha(R/'PROOF.md')==claim['proof_source']['sha256']
assert hashlib.sha256(obj(R/'CLAIMS.json')[0]['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
for h in protocol['required_per_run']['report_fields']:assert '\n## '+h+'\n' in rd(R/'REPORT.md')
assert rd(R/'REPORT.md').rstrip().split('\n\n')[-1].startswith('**Universal bridge:**')
receipts=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and '__pycache__' not in p.parts and p.name!='PERSISTENCE_RECEIPTS.json':
  assert p.stat().st_size<20_000_000
  receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
for n in ['STATUS.md','WORKLOG.md','LEARNED.md']:
 p=HOME/n;receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
dump(R/'out/PERSISTENCE_RECEIPTS.json',{'status':'LOCAL_SAVED_HASH_READBACK_PASS','files':receipts,'scope':'Local receipt only; no mirror, external review or downstream use claimed.'})
for row in obj(R/'out/PERSISTENCE_RECEIPTS.json')['files']:assert sha(row['path'])==row['sha256']
print(json.dumps({'status':'PASS','receipt_files':len(receipts),'protocol_fieldsets':'PASS','statement_and_proof_hashes':'PASS','primary_exact_checks':14365,'full_fei':'OPEN','independent_review':'PENDING','formal':'NOT_STARTED','remote':'NO_MUTATION'}))
