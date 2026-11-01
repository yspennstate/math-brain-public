"""Persist the stage, enforce protocol fields, and hash actual local artifacts."""
from pathlib import Path
import json, hashlib

RUN = Path(__file__).resolve().parents[1]
HOME = RUN.parents[1]
ROOT = HOME.parents[1]
PROTO = Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def read(p): return Path(p).read_text(encoding='utf-8')
def write(p, s): Path(p).write_text(s, encoding='utf-8')
def obj(p): return json.loads(read(p))
def dump(p, x): write(p, json.dumps(x, indent=2, ensure_ascii=False)+'\n')
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

protocol = obj(PROTO)
assert obj(RUN/'out/SECOND_QUERY.json')['status']=='PASS'
assert obj(RUN/'out/DIRECT.json')['status']=='PASS'
assert obj(RUN/'out/READBACK.json')['status']=='PASS'
assert obj(RUN/'out/FORMAL_ADMISSION.json')['status']=='NOT_ADMITTED'

claim_id = 'A061-ORIGINAL-MARGINAL-ENVELOPE-ALL-HISTORIES'
old_id = 'A061-PRODUCT-REFERENCE-LOCAL-PRICE-OBSTRUCTION@1'
statement = ('For every finite Boolean core g with a source-supporting inherited normalized spectral reference R, '
 'the lifted bent carrier preserves this reference under every fair adaptive ordinary physical restriction, '
 'including reference-only rows. With K=KL(p_g||R) and M=sum_j h2(Inf_j(g)), K+M plus accumulated actual outcome KL '
 'is a supermartingale up to stopping or one final carrier/product conversion, retaining the full terminal H+KL. '
 'The least pending booking B obeys B<=M. For the explicit GF(2^l) selector stress family, every l>=2, '
 'the total original selector-root pending reserve is at most Wcap=3 for l=2 or 39l/32 for l>=3, '
 'and Wcap<13Sbar/48, where Sbar is the one original mean child (4I-H) owner. '
 'With unrelated old expenditure at most Sbar/4 and an already booked nested pending reserve theta, '
 'top up only Wcap-theta, leaving more than 23Sbar/48 in the same owner. '
 'At l=2,3 the complete optional-stop depth-two policy minimum is respectively '
 '47/32-(3/8)log2(7) and 0; it is below Sbar/25 and its increase from depth one is below Sbar/50.')
hyp = [
 'Uniform physical Boolean inputs; entropy, total correlation and KL in bits; actual coherent restriction kernel, extended fairly on source-zero rows.',
 'Carrier F=(-1)^((u+v+L(y)+c)*v)g(y); initial P=p_g(T xor su*L)/4 and Q=R(T xor su*L)/4. R normalized and positive on source support.',
 'Policy chooses only still-unrevealed ordinary core coordinates adaptively, may stop, or query fresh v then convert once to product references. No intermediate reset, no earlier u query, and converted children are terminals.',
 'Quantitative owner comparison is only for h(a,b,x)=psi(a)(1-2*1[x=ab]) on GF(2^l), l>=2, and selector children carrier and carrier*h, using the original uniform product parent reference.',
 'The same original Sbar=2*(3l)+2-H(h)/2 is supplied, with unrelated old expenditure omega<=Sbar/4. Previously allocated theta must be a nested pending booking for the SAME inherited reference and policy class; other consumed debits remain in omega.',
 'Exact depth-two assertions apply only to l=2,3, all distinct first/second ordinary directions and adaptive outcomes, with optional earlier stops/carrier conversions.'
]
claim = dict(claim_id=claim_id,version=1,exact_statement=statement,hypotheses=hyp,
 statement_sha256=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest(),
 contributors=['A061/fleet03'],
 proof_source={'path':str(RUN/'PROOF.md'),'sha256':sha(RUN/'PROOF.md'),
 'validation':[str(RUN/'out'/x) for x in ['SECOND_QUERY.json','DIRECT.json','READBACK.json','FORMAL_ADMISSION.json']]},
 proof_dependencies=[{'claim':old_id,'scope':'Explicit field-family construction and original owner; reproduced critical l=2 source directly this stage; all-l edge count and owner comparison reconstructed in PROOF.md.',
 'acceptance':'A064 independently reports HOLDS for the full stage17 source in its 20261022T224340Z run; original A061 claim file remains unmodified.'}],
 review_records=[],status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=[],
 first_unproved_line=None,next_consumers=['A064','A065','A087','A094'])
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
dump(RUN/'CLAIMS.json',[claim])

progress = dict(protocol_revision=protocol['revision'],run_id=RUN.name,stream='B13',packet_id='A061',
 gap_id='G-R-MISMATCH',attempt_id='A061-stage18-original-marginal-envelope',
 method='Exact inherited-reference KL chain plus physical influence averaging and binary-entropy concavity; backward booking induction; independent full-source spectrum and rational interval certificates.',
 mathematical_delta='Closed ALL ordinary-data depths for the supplied field-carrier owner, Wcap<13Sbar/48 after one original allocation; exact full depth-two optimum <Sbar/25 and second top-up <Sbar/50 at l=2,3. Full FEI remains open.',
 deliverable_status='COMPLETE_LOCAL_ARTIFACTS',mathematical_status='CONDITIONAL_FAMILY_THEOREM_AUTHOR_PROVED; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
 claim_versions_used=[old_id],claims_created_or_changed=[claim_id+'@1'],
 source_artifacts=[str(RUN/x) for x in ['PROOF.md','FROZEN_SPEC.json','DIRECT_SPEC.json','READBACK_SPEC.json','out/SECOND_QUERY.json','out/DIRECT.json','out/READBACK.json']],
 next_consumers=['A064','A065','A087','A094'],
 next_action='Construct a signed pending-reserve supersolution for sparse non-carrier histories using the inherited K/E terms, with an explicit one-original-owner inequality; do not reopen the closed field ordinary-depth frontier. A064/A087 independently reconstruct this all-history theorem.',
 stagnant_substantive_attempts=0,
 blockers=['Universal availability of a fresh carrier and unused original influence-scale owner is unproved.',
 'M/I is unbounded for point-defect cores, so the generic M envelope cannot by itself give universal FEI.',
 'Formal compiler not admitted: memok exit1, physical free1.3GB; no formal certificate claimed.',
 'Independent review and supervisor mirror/downstream-use receipts are pending. Archive metadata reports master; requested main branch returned404, so no remote mutation or push was performed.',
 'Brain self-care degraded/unverified: stale owner-model/state-of-mind and failed context attachment; neither used as a mathematical premise.'],
 packet_ids=['A061'])
fields={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==fields
dump(RUN/'PROGRESS.json',progress)
dump(RUN/'PACKET_DELTA.json',progress)
dump(RUN/'out/ARCHIVE_RECEIPT.json',{
 'status':'BLOCKED_REQUESTED_BRANCH_ABSENT',
 'repository':'yspennstate/math-open-problems',
 'metadata_default_branch':'master',
 'requested_branch':'main',
 'readback':'GitHub GET branches/main:404 Branch not found',
 'remote_mutation':False,'commit':None,
 'handoff':'Supervisor archive copy remains pending; no branch created or repository state changed.'})

source_paths = [PROTO, ROOT/'BOARD.md',ROOT/'claude/B13/STREAM_NOTES.md',
 ROOT/'agents/A064/runs/20261022T224340Z-fleet03-A064-global-debt-potential/REPORT.md',
 ROOT/'agents/A064/runs/20261022T224340Z-fleet03-A064-global-debt-potential/PROOF.md',
 ROOT/'agents/A065/runs/20261022T234254Z-fleet03-A065-stopping-rule-falsifier/REPORT.md',
 ROOT/'agents/A065/runs/20261022T234254Z-fleet03-A065-stopping-rule-falsifier/PROOF.md',
 ROOT/'agents/A065/runs/20261022T234254Z-fleet03-A065-stopping-rule-falsifier/code/interpose.py',
 HOME/'runs/20261021T195713Z-fleet03-A061-entropy-process/PROOF.md']
dump(RUN/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p)} for p in source_paths])
dump(RUN/'out/ADVERSARIAL_REVIEW.json',{
 'status':'AUTHOR_CHECK_ONLY; independent review pending',
 'checks':[
 {'boundary':'Inf=0 or1','resolution':'h2 endpoint convention and physical-edge averaging need no positive-influence division.'},
 {'boundary':'Source-zero/reference-positive rows','resolution':'Fair1/2 retained; direct full-source transport checked atomwise, including nonzero reference-only masses.'},
 {'boundary':'Normalization/order','resolution':'Every reached history carries its actual normalized Bayes reference; only source statistics memoized, never references by function.'},
 {'boundary':'Entropy/KL accounting','resolution':'Full terminal H+TC retained. O_v=0; ordinary O paid by exact K chain; E>=0 is an actual erasure refund.'},
 {'boundary':'Owner reuse','resolution':'Only one initial M allocation. Pending theta nested, top-up cap minus theta; unrelated old expenditure stays spent.'},
 {'boundary':'Finite-to-infinite','resolution':'All-l field result from analytic edge counts and integer3^12>2^19, not extrapolation from l=2,3 enumeration.'},
 {'boundary':'Universal obstruction','resolution':'Point defect gives M/I>=n-1. Generic envelope is not a universal FEI payment.'},
 {'boundary':'Policy scope','resolution':'No u before carrier terminal, no intermediate product reset, no continuation after converted terminal.'}],
 'primary_exact_assertions':115373,
 'excluded_from_primary_total':'614 pilot and3594 auxiliary shared-scalar direct assertions, to avoid counting overlap as independent proof.'})

report = '''# A061 stage18: one original marginal reserve pays all ordinary carrier histories

## exact target, quantifiers, hypotheses and units

Prove a paid entropy/KL process along the fair adaptive restriction tree with its actual inherited reference and ONE original owner. PROOF.md §§1–3 proves the all-history theorem for every finite core and supporting carrier reference; the quantitative owner comparison applies to the explicit field selector for every l>=2. Units are bits. Policies reveal ordinary core coordinates adaptively, stop, or reveal fresh v and convert once at a terminal. No intermediate reset or post-conversion continuation is admitted. The fair filtration, exact one-step KL increments, source-zero fair extension and terminal full H+TC are explicit. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Execution protocol revision2026-10-11-execution-v2; BOARD dated2026-10-23 00:21UTC; B13 lead v2; own STATUS, LEARNED and stage17 field-family proof. A064 20261022T224340Z REPORT/PROOF supplied the reference lift, terminal carrier transfer and the reported independent acceptance of stage17. A065 20261022T234254Z REPORT/PROOF and interpose.py supplied the ordinary-history invariant, exact booking recursion, first-data-query frontier and tensor-reference obstruction. Their key invariant and recursion are reconstructed in PROOF.md §§1–2 rather than accepted on title alone. Baseline campaign/paper intake is inherited; no new outside paper theorem is asserted. Current read-source content hashes are in out/SOURCE_RECEIPTS.json. The current user deadline overrides the older protocol clock.

## complete derivation or exact first unsupported line

At history rho, K=KL(p||R), M=sum h2(Inf_j), and V=K+M. Physical-edge averaging and binary-entropy concavity give M-parent minus mean child M>=0. The actual normalized reference chain gives K-parent minus mean child K=E+O with E>=0. Thus V-parent minus mean child V>=O; V plus accumulated O is a supermartingale on the bounded fair-history filtration. At conversion V>=TC and the full terminal H is retained. The exact pending recursion B=max([TC-K]_+,max_i(mean Bchild-E)) therefore satisfies B<=M at every adaptive history. No descendant receives a renewed M allocation.

For the field source, the constant branch needs zero reserve and the other needs at most M_h, so W*<=M_h/2, with M_h=2l h2(2/q-2/q^2)+l h2(2/q). Direct field-edge counts hold in every basis. With the ORIGINAL Sbar=6l+2-H_h/2, choose Wcap=3 at l=2 or39l/32 at l>=3. The exact integer inequality3^12>2^19 proves Wcap<13Sbar/48. With unrelated omega<=Sbar/4, top up a nested previous pending theta only by Wcap-theta, leaving >23Sbar/48 in the SAME owner. This closes all ordinary-data depths of this fixture, beyond A065's second-query next target.

The sharper complete depth-two minima are W2=47/32-(3/8)log2(7) at l=2 and0 at l=3. Both W2<Sbar/25, additional W2-W1<Sbar/50, and remaining owner after the unrelated old quarter >71Sbar/100. These finite values preserve, rather than replace, the earlier immediate-carrier and first-query numbers. The all-history cap is a conservative bound for a larger policy class.

There is no unsupported line inside the stated conditional theorem. The first unpaid UNIVERSAL line is an influence-scale bound for the complete signed pending reserve in sparse non-carrier histories, with a genuinely unused original owner. Indeed f_n=1-2*1[x=0] has M/I>=n-1. A uniform comparison M<=C I is false, although this says nothing against FEI itself. See PROOF.md §4 and out/ADVERSARIAL_REVIEW.json.

## executed validation with domain, arithmetic, commands and outputs

Frozen specifications precede each computation: FROZEN_SPEC.json, DIRECT_SPEC.json and READBACK_SPEC.json. All commands use python -X utf8; relative commands below run from this stage directory. No dimension escalation, GPU, detached job, or >300MB computation was started.

- `python -X utf8 code/check.py pilot`: PASS,614 assertions,3 query candidates/7 histories,0.159s. Pilot cases are excluded from the primary total.
- `python -X utf8 code/check.py`: out/SECOND_QUERY.json PASS,114154 assertions,219 query candidates/440 reached histories,9.755s. Fixed l=2,3; all first/second distinct directions, physical outcomes, earlier stops and carrier choices. Dynamic programming represents726 full adaptive depth-two policies plus earlier stops. Integer FWHT, independently counted physical edges, rational references and exact prime-log expressions; outward32-term atanh log bounds with proved tail and96-bit rounding.
- `python -X utf8 code/direct.py`: out/DIRECT.json PASS,1205 direct assertions,0.437s. Independently constructed GF4 and direct character sums for the actual9-bit source, two ordinary queries, full lifted reference transport, and8 final carrier children. Additional3594 shared scalar assertions are excluded from the primary total.
- `python -X utf8 code/readback.py`: out/READBACK.json PASS,14 assertions,0.011s, exact saved-enclosure comparison and integer powers; W2<Sbar/25, second top-up<Sbar/50, spare>71Sbar/100.

Primary total115373 exact assertions. Analytic proof, not finite search, supplies all l and all ordinary-history depths. Fresh memok returned exit1: physical free1.3GB (required4.0), commit free19.7GB. The proposed512MB scalar Lean check was NOT_ADMITTED and no compiler started; out/FORMAL_ADMISSION.json records scope and reason. No formal theorem/axiom certificate is claimed. Brain self-care wake was degraded/unverified (stale owner model86.9h and state of mind71.5h, failed attachment/renderer); affected personal/context notes were not mathematical premises.

## proof dependencies and changed downstream conclusions

CLAIMS.json contains one new scoped claim A061-ORIGINAL-MARGINAL-ENVELOPE-ALL-HISTORIES@1, author proved pending independent review. Its field construction is A061-PRODUCT-REFERENCE-LOCAL-PRICE-OBSTRUCTION@1; A064 reports independent HOLDS for that source. General transport/booking facts are reconstructed here with no circular dependency on the new claim. A064's one-carrier and A065's first-query prices stay valid; no reimbursement or automatic tensor-reference law is asserted. The source-bound local handoff names A064/A065/A087/A094; this is not a downstream-use receipt. Full FEI and universal fresh-owner availability remain open.

## one next mathematical action and independent reviewer

Construct a source-dependent signed supersolution to B_rho=max([TC-K]_+,max_i(mean Bchild-E)) in sparse non-carrier histories with one original influence-scale owner, exploiting K/E refunds instead of the divergent M envelope. A064/A087 should independently reconstruct PROOF.md §§1–3 and the carrier/reference scope before adoption. The closed field ordinary-depth problem does not need another dimension survey.

## actual persistence receipts or precise save blocker

Required REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json are saved locally, together with proof, frozen specs, reproducible code and exact outputs; STATUS.md, WORKLOG.md and LEARNED.md are current. out/PERSISTENCE_RECEIPTS.json records SHA256 of actual run artifacts (excluding itself and bytecode) and rolling files; code/finalize.py checks protocol fieldsets, the claim statement hash, copy identity and file sizes, then rereads every receipt. No local save blocker. The requested archive-to-main check found repository default master and GET branches/main returned404; out/ARCHIVE_RECEIPT.json records this blocker. No branch was created or remote state changed. Supervisor copy, mirror verification, independent acceptance and actual downstream mathematical use are not claimed.

**Universal bridge:** C019 stopping-tree payment and C024 history transfer advance from a one-query frontier to ALL ordinary-data histories of the explicit all-l carrier fixture, using one original reserve <13Sbar/48 and retaining >23Sbar/48 after the old quarter. The exact two-query frontier needs <Sbar/25, with second top-up<Sbar/50. The universal unpaid line is a signed sparse-history reserve fitting an actually unused influence-scale owner when no fresh carrier is supplied. The next signed supersolution targets that obstruction directly; repeating closed field-class checks cannot supply full FEI.
'''
write(RUN/'REPORT.md',report)

status = ('STATE: A061 stage18 complete: all ordinary carrier histories paid by ONE original reserve<13Sbar/48; exact depth-two total<Sbar/25, extra second top-up<Sbar/50; independent review pending; FEI OPEN.\n'
 'NEXT: Stage18 saved at runs/20261023T002802Z-fleet03-A061-entropy-process; claim A061-ORIGINAL-MARGINAL-ENVELOPE-ALL-HISTORIES@1; no remote commit (main absent). A064/A087 review; then signed sparse non-carrier booking using K/E and one original influence owner.\n')
write(HOME/'STATUS.md',status)
entry = ('\n2026-10-23 stage18 (20261023T002802Z): consumed A064 carrier transfer and A065 ordinary-history invariant/first-query objection; proved one original M=sum h2(Inf) envelope pays ALL permitted adaptive ordinary carrier histories. Field-family Wcap<13Sbar/48 leaves>23Sbar/48 after old quarter, retaining old pending theta by top-up only. Exact second-query DP l=2,3: W2=47/32-(3/8)log2(7),0; total<Sbar/25, incremental<Sbar/50. Main114154 + independent actual-full-source1205 + readback14 =115373 primary exact assertions; auxiliary/pilot excluded. Fresh memok exit1 (physical1.3GB), compiler not started. Analytic all-l proof saved; independent review/full FEI open; stale brain self-care context not used as premise.\n')
if entry.strip() not in read(HOME/'WORKLOG.md'): write(HOME/'WORKLOG.md',read(HOME/'WORKLOG.md')+entry)
archive_entry='\n2026-10-23 stage18 archive check: GitHub metadata reports yspennstate/math-open-problems default master; requested main branch GET returned404. No remote mutation, no git, no branch creation, no push claimed. Local artifacts and supervisor archive handoff retained.\n'
if archive_entry.strip() not in read(HOME/'WORKLOG.md'): write(HOME/'WORKLOG.md',read(HOME/'WORKLOG.md')+archive_entry)
learned = '''
Stage18 durable fact (2026-10-23): With source-supporting normalized inherited reference R and a fresh bent carrier, ordinary physical restriction preserves its full lift, including fair reference-only rows. K+M, M=sum h2(Inf), has drift E+O+M-parent-mean Mchild>=O, hence pays any bounded adaptive ordinary-history cut followed by at most one terminal carrier/product conversion. Full H+TC remains; no intermediate reset or earlier carrier-u query is included. The least pending B=max([TC-K]_+,max_i(mean Bchild-E)) is <=M by backward induction. ONE original M bank suffices; no per-node renewal. For the all-l field fixture, Wcap=3(l2) or39l/32(l>=3) is <13Sbar/48; after unrelated old quarter, spare>23Sbar/48. Old nested pending theta counts once, top-up only cap-theta. Complete depth-two minima at l2,l3 are47/32-(3/8)log2(7),0, both<Sbar/25 and incremental second top-up<Sbar/50. Analytic proof plus115373 primary exact checks; independent review pending, no Lean certificate. Point defect f_n=1-2*1[x=0] has M/I>=n-1: generic marginal reserve does NOT solve universal FEI. Next frontier is signed K/E payment in sparse non-carrier histories, not greater field restriction depth.
'''
if learned.strip() not in read(HOME/'LEARNED.md'): write(HOME/'LEARNED.md',read(HOME/'LEARNED.md')+learned)

# Validate fieldsets and persisted identities before issuing actual receipts.
assert obj(RUN/'PROGRESS.json')==obj(RUN/'PACKET_DELTA.json')
assert len(read(HOME/'STATUS.md').splitlines())==2
for heading in protocol['required_per_run']['report_fields']:
 assert '\n## '+heading+'\n' in read(RUN/'REPORT.md')
assert read(RUN/'REPORT.md').rstrip().split('\n\n')[-1].startswith('**Universal bridge:**')
persist=[]
for p in sorted(RUN.rglob('*')):
 if p.is_file() and '__pycache__' not in p.parts and p.name!='PERSISTENCE_RECEIPTS.json':
  assert p.stat().st_size<20_000_000
  persist.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
 p=HOME/name
 persist.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
dump(RUN/'out/PERSISTENCE_RECEIPTS.json',{'status':'LOCAL_SAVED','files':persist,
 'scope':'Actual local file hashes, not supervisor/mirror/downstream-use receipts.'})
for receipt in obj(RUN/'out/PERSISTENCE_RECEIPTS.json')['files']:
 assert sha(receipt['path'])==receipt['sha256']
assert claim['proof_source']['sha256']==sha(RUN/'PROOF.md')
print(json.dumps({'status':'PASS','local_files_verified':len(persist),'primary_exact_assertions':115373,
 'protocol_fieldsets':'PASS','claim':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
 'full_fei':'OPEN','formal':'NOT_ADMITTED','running_jobs':0}))
