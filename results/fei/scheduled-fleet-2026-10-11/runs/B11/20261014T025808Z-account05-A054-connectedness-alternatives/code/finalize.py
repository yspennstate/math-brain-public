from pathlib import Path
from fractions import Fraction as F
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def outward(v):
 a,b=map(F,v);s=10**6;lo=a.numerator*s//a.denominator;hi=-((-b.numerator*s)//b.denominator)
 return [f'{lo//s}.{lo%s:06d}',f'{hi//s}.{hi%s:06d}']
check=json.loads((ROOT/'out/EXACT_CHECK.json').read_text());pilot=json.loads((ROOT/'out/PILOT.json').read_text())
assert check['status']==pilot['status']=='PASS'
assert check['block_cases']==1978 and check['tree_cases']==548
display=outward(check['projection_price_interval']);save(ROOT/'out/PRICE_DISPLAY.json',dict(C_projection=display,rigorous_upper='37/4',universal_block_transfer_coefficient='4/(e ln2)'))
statement=('For every indicator g on a finite uniform cube, f=1-2g and every nonempty physical queried block A, let Lambda_A(g)=F(g)-E_xF(g_x) be the raw bit Fourier-entropy drop and L_A(f)=H(f)-E_xH(f_x). '
'Then L_A(f)<=4Lambda_A(g)+(4/(e ln2))I_A(f), including zero-energy blocks. The exact empty-coefficient correction is T(p)=-(1-2p)^2 ln((1-2p)^2)+4p^2 ln(p^2)-8ln2 p(1-p), with T(p)-E T(p_x)<=(8/e)Ent(p_x)<=16E_A(g)/e. '
'For every finite adaptive physical restriction tree the same transfer holds for total entropy decrements and erased influence, retaining actual leaf entropies and the inherited indicator orientation. '
'If g has actual connected components with pairwise disjoint projections on a proper r-coordinate block A, masses p_k and projection measures mu_k satisfying sum p_k log2(1/mu_k)>=r E g/2, then L_A(f)<=C_proj I_A(f), C_proj=4+2/ln2+4/(e ln2)<37/4<10. '
'Thus every physical-descendant ratio-critical sign in this geometric class has H/I<=C_proj at every positive support density, and every least-essential-dimension K-violator is excluded from it at K>=C_proj with the complete child reserve retained. Universal proper-block admission is not asserted.')
hyp=['Finite uniform physical cubes; Boolean indicators g and actual signs f=1-2g; raw indicator entropy F and sign entropy H in bits; I_A(f)=4E_A(g)',
'Universal block/tree transfer uses actual fair physical restrictions and the same inherited indicator orientation at every leaf; no density or component hypothesis',
'Projection critical consequence requires a proper nonempty block, actual connected-component projections pairwise disjoint, and weighted projection information at least r E g/2',
'Critical ratio conclusion requires all proper physical descendant ratios at most the root ratio and nonzero influence; threshold exclusion requires least essential dimension among all Boolean fixed-K violators',
'No arbitrary virtual component or row phase is treated as a physical descendant; every child/terminal deficit is retained']
claim=dict(claim_id='A054-RAW-SIGN-BLOCK-TREE-TRANSFER',version=1,exact_statement=statement,hypotheses=hyp,
statement_sha256=hashlib.sha256(json.dumps(dict(statement=statement,hypotheses=hyp),sort_keys=True,separators=(',',':')).encode()).hexdigest(),contributors=['account05/A054'],
proof_source=dict(path=str(ROOT/'RAW_SIGN_TRANSFER.md'),sha256=sha(ROOT/'RAW_SIGN_TRANSFER.md'),locator='sections1--5 and (5T)'),proof_dependencies=[],review_records=[],
status='AUTHOR_PROVED_EXACT_VALIDATION_PASS_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=[],first_unproved_line=None,next_consumers=['A052','A055','A051','claude/B11','A028','A064','A090','A094','B20'])
save(ROOT/'CLAIMS.json',[claim])
report=f'''# exact target, quantifiers, hypotheses and units

A054/B11, stage {ROOT.name}. Prove an influence-paid transfer from raw
indicator block/tree entropy payment to actual Boolean sign payment,
then remove the support-density hypothesis from the prior critical
projection class. All cubes are finite and uniform, g is an indicator,
f=1-2g, bit entropy H/F is distinguished from the explicitly natural
scalar correction T and Ent. I_A(f)=4E_A(g). The universal transfer
requires no geometric or criticality hypothesis; the projection
consequence states both separately. Ratios require nonzero influence.

# sources actually read, revisions and theorem locators

Read BOARD.md snapshot2026-10-14 02:53UTC, complete B11 STREAM_NOTESv2
(still2026-10-11 23:3xZ) and own STATUS/LEARNED at start. The lead's
original Brain45 task was completed last stage and is not repeated.
New A051/A052/A055 REPORTs identify signed pair/phase/child reserves as
the live selection route. Read A052 SIGNED_PAIR_PROOF sections1--4 and
CLAIMS, the actual A055 PROOF and A051 TWO_BIT_RESERVE dependency proofs.
REVIEW_SIGNED_PAIR.md independently reconstructs that full scoped chain
without repair, with ACCEPT_AT_STATED_ANALYTIC_SCOPE verdict; source
census assertion counts are not adopted. Review priority is met before
this narrow new transfer application. No source-bound review changes
another agent's files or the shared registry.

The complete execution protocol revision2026-10-11-execution-v2 was
read in the earlier stages and its unchanged header/schema refreshed
here. Earlier campaign and paper reads remain background, not claimed
as refreshed. Prior A054 PROJECTION_PAYMENT and exact arithmetic helper
are reused at their written scope; the new mathematical proof includes
its own needed analytic and projection arguments. No external paper,
internet search, brain write or literature-priority claim is needed.
Exact consulted source paths and local SHA256s are in SOURCE_MANIFEST.

# complete derivation or exact first unsupported line

RAW_SIGN_TRANSFER.md sections1--5 is the full proof; COMPONENT_EXCESS.tex
is the concise interface. Exact Fourier accounting shows that natural
sign entropy equals four times natural raw entropy plus
T(p)=-(1-2p)^2ln((1-2p)^2)+4p^2ln(p^2)-8ln2 p(1-p).
The block correction is exactly T(p)-average T(p_x), retaining every
actual child mass. Its second derivative simplifies to
16ln(2p/abs(1-2p)). The bound pT''>=-8/e proves convexity of
T+(8/e)p ln p; Jensen controls the correction by (8/e)Ent_x(p_x).
Logarithmic Sobolev on sqrt(p_x), followed by the L2 reverse triangle
inequality for actual indicator children, pays Ent_x(p_x)<=2E_A(g).
No lower density bound, non-Boolean surrogate or assumed criticality
enters this derivation.

Consequently L_A(f)<=4Lambda_A(g)+(4/(e ln2))I_A(f) for every physical
block. The same-leaf-partition finite-tree telescope retains actual
leaf H and F and charges only erased influence. It transfers a raw
tree rate K to a sign tree rate K+4/(e ln2), without a repeated root
bank. Zero queried influence makes the correction exactly zero.

The prior component projection credits imply E_A>=rp/4 and
Lambda_A<=(4+2/ln2)E_A whenever a proper component-isolating block has
Q_A=sum_k p_k log2(1/mu_k)>=rp/2. Therefore its actual sign decrement
is paid at C_proj=4+2/ln2+4/(e ln2), certified in
({display[0]}, {display[1]}) and analytically below37/4<10.
Physical sign ratio criticality now gives H/I<=C_proj at EVERY positive
support density, including rare non-Cartesian support. This removes
the preceding p>=p0 hypothesis, though the older moderately balanced
bound remains sharper within its narrower scope. A minimal fixed-K
violator obeys D_K+S_A<= (C_proj-K)I_A, with complete actual-child
reserve S_A>=0. K>=C_proj excludes the stated projection class.

First unsupported universal line: every prospective minimal high-K
violator admits such a proper affordable projection block, or a
different terminal-inclusive paid selection on connected support or
overlapping component projections. Rarity is no longer the missing
assumption for this class. Full FEI remains OPEN; the transfer theorem
does not assert global raw payment or universal proper-block admission.

# executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json was saved before pilot/full executions. The
arithmetic-only mathcore.py was copied from the previous stage by
stopping before its search loop; all writes from the new helper stay
inside this run. Commands from A054:

    python -X utf8 runs\\{ROOT.name}\\code\\check_transfer.py --pilot
    python -X utf8 runs\\{ROOT.name}\\code\\check_transfer.py

Pilot PASS: {pilot['tables']} indicators through n=2, {pilot['block_cases']}
block cases, {pilot['tree_cases']} terminal-inclusive physical trees,
{pilot['assertions']} assertions, {pilot['seconds']:.6f} helper seconds.
Full PASS: {check['tables']} indicators through n=3 and all1844 nonempty
small-table blocks, Brain45 all126 proper blocks, Brain44 its natural
data separator, plus seven rare retained-controller profiles: exactly
{check['block_cases']} block cases, {check['tree_cases']} physical tree
cases, {check['assertions']} assertions, {check['seconds']:.6f} helper
seconds. No symmetry quotient. The seven rare supports have frozen
dimensions5..11 and widths0..6, component projections of size3 on16
selector points, non-Cartesian fibers, and total mass2^(-width-2).
They validate the new transfer and density-free geometric price;
their criticality is NOT asserted. No high-threshold violating root
has been computed. Historical raw pruning refutations remain the
previous stage's exact mandatory controls, unchanged and unrevived.

Integer direct Walsh/FWHT and physical edge counts give exact spectra
and influence. Fraction and canonical prime-log vectors verify the
empty-coefficient correction and both block/tree telescopes. A32-term
range-reduced atanh series with explicit65th-order tail bounds supplies
outward112-bit logarithm intervals. A rational exponential partial sum
through20! and its geometric tail bound encloses e; finite inequalities
use the proved upper relaxation8/e_lower, never a floating exponential
sign. Final six-place price endpoints are outward rational roundings.
Leaf entropy and removed influence are checked separately; complete
and depth-one trees use the same inherited indicator orientation.

Frozen estimate130MB is below300MB; actual peak RAM was not measured.
Pilot cap55sec and full cap180sec were respected, one substantive job
at a time. No >300MB allocation required memok, no GPU, background
helper or automatic dimension increase. Dimensions5..11 were explicit
before execution, not inferred from the pilot. Tool/shell latency is
separate from helper runtime. Results are in PILOT.json, EXACT_CHECK.json
and RARE_PROFILE.json, saved upon completion.

# proof dependencies and changed downstream conclusions

The new bundled theorem is self-contained: Fourier empty-coefficient
accounting, elementary calculus/Jensen, the supplied two-point cube
log-Sobolev proof, reverse triangle inequality, elementary projection
uncertainty/edge isoperimetry, and actual-child deficit averaging.
A052's signed-pair chain is independently accepted at its scope as
a live related dependency, but is not assumed as a premise for this
transfer. Its actual A051/A055 dependency proofs are read and reviewed.
Old numerical bounds are not silently replaced or a full-FEI claim
adopted. The prior p>=p0 admission condition is superseded only for
the new larger paid constant; geometric proper-block admission remains.

A052/A055 receive a density-free actual-sign projection exclusion and
the exact empty-sector scalar correction. A028/A064 receive a same-tree
raw-to-sign transfer with leaf entropy and one erased-influence budget.
B11 lead need not repeat Brain45 phi. Independent A090/A094 review,
registry adoption and external mirrors are pending, not implied by saves.

# one next mathematical action and independent reviewer

Next: apply the curvature-paid transfer to a terminal-inclusive raw
component ledger at a proper block with overlapping projections, asking
whether actual critical child reserves pay the remaining projection
debt or labelled child cross term. Connected support must remain an
explicit boundary case. A090 should reconstruct the scalar curvature
and square-root-mean energy normalization; A094 should reconstruct the
same-leaf telescope and geometric criticality line. Do not expand the
completed finite census without a new signed selection hypothesis.

# actual persistence receipts or precise save blocker

The four protocol files, RAW_SIGN_TRANSFER.md, COMPONENT_EXCESS.tex,
REVIEW_SIGNED_PAIR.md, code, frozen specification and exact outputs are
saved only inside A054. Rolling STATUS, WORKLOG and LEARNED are updated.
out/RECEIPTS.json checks byte lengths/SHA256s, exact protocol fields,
byte-identical PROGRESS/PACKET_DELTA and the20MB file limit. Shared
source/index trees, another agent's files, brain stores, git and trading
directories were untouched; no outbound message was sent. Supervisor
copies, shared adoption and independent acceptance remain unverified.

# Universal bridge

This stage advances C019 stopping-tree payment and B11 critical block
selection by a universal raw-indicator-to-sign correction price of
4/(e ln2) times erased influence on the same leaf partition. It removes
the positive-density assumption from the component-projection critical
class at C_proj<37/4 while retaining all child reserves, with
{check['assertions']} exact checks. What remains is universal proper
geometric admission or signed payment of projection overlap and labelled
terminal cross terms; rarity no longer blocks this transfer. NEXT attacks
that remaining physical-child selection line because a uniform paid
choice would contradict every minimal FEI witness, whereas another rare
class census or another root-only embedding would not close the bridge.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=ROOT.name,stream='B11',packet_id='A054',gap_id='FEI-B11-A054-INITIAL',attempt_id='A054-raw-sign-curvature-3',
method='Exact empty-coefficient correction curvature; square-root mass-tilt log-Sobolev payment; same-leaf tree telescope; density-free component projection criticality',
mathematical_delta='Universal L_sign<=4Lambda_raw+4/(e ln2)I_A and same-tree transfer proved; projection critical price C_proj<37/4 now holds at every positive support density. Universal block admission remains open.',deliverable_status='COMPLETE_SAVED_LOCAL',
mathematical_status='UNIVERSAL_TRANSFER_AND_SCOPED_CRITICAL_PAYMENT_PROVED_FULL_FEI_OPEN',claim_versions_used=[],claims_created_or_changed=[dict(claim_id=claim['claim_id'],version=1)],source_artifacts=['REPORT.md','RAW_SIGN_TRANSFER.md','COMPONENT_EXCESS.tex','REVIEW_SIGNED_PAIR.md','out/EXACT_CHECK.json','out/RARE_PROFILE.json'],next_consumers=claim['next_consumers'],
next_action='Price projection overlap or labelled terminal cross term on an actual critical source using the curvature-paid raw-to-sign transfer and one child reserve; A090/A094 independent reconstruction.',stagnant_substantive_attempts=0,blockers=['Universal proper projection-block selection and connected/overlapping support payment remain open','Independent A054 review, shared registry adoption and remote mirrors pending'],packet_ids=['A054'])
save(ROOT/'PROGRESS.json',progress);save(ROOT/'PACKET_DELTA.json',progress)
review=dict(claim_id='A052-SIGNED-PAIR-ORIENTATION-REFUND',version=1,reviewer='account05/A054',verdict='ACCEPT_AT_STATED_ANALYTIC_SCOPE',source='REVIEW_SIGNED_PAIR.md',method='Independent complete analytic reconstruction including original A051/A055 dependencies, no repair or adopted finite census',registry_adoption='PENDING')
save(ROOT/'out/REVIEW_RECORDS.json',[review])
sources=[Path('~/brain_workers/FEI100_20261011/BOARD.md'),Path('~/brain_workers/FEI100_20261011/claude/B11/STREAM_NOTES.md'),Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')]
workers=AGENT.parent
source_dirs=[workers/'A051/runs/20261014T012634Z-account05-A051-near-extremizer-definition',workers/'A052/runs/20261014T015635Z-account05-A052-critical-source-structure',workers/'A055/runs/20261014T004129Z-account05-A055-extremal-obstruction-referee']
for d in source_dirs:
 sources.append(d/'REPORT.md')
 for name in ['SIGNED_PAIR_PROOF.md','TWO_BIT_RESERVE.md','PROOF.md','CLAIMS.json']:
  if (d/name).exists():sources.append(d/name)
sources+=[AGENT/'runs/20261013T235828Z-account05-A054-connectedness-alternatives'/x for x in ['PROJECTION_PAYMENT.md','out/MANDATORY_CONTROLS.json','code/projection_and_phi.py']]
save(ROOT/'out/SOURCE_MANIFEST.json',[dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size) for p in sources])
(AGENT/'STATUS.md').write_text(f'STATE: A054 universal raw-sign block/tree transfer proved; critical projection price C<37/4 is density-free; {check["assertions"]:,} exact checks PASS; signed-pair chain reviewed; full FEI OPEN.\nNEXT: A090/A094 review; A052/A055 pay projection overlap or labelled terminal cross terms with the new raw-sign correction and one actual child reserve.\n',encoding='utf-8')
marker=f'2026-10-14 / {ROOT.name}'
work=f'\n{marker}: Read BOARD02:53UTC and unchanged leadv2; independently reconstructed A052 signed-pair chain and its original dependencies without repair. Proved empty-sector curvature T\'\'=16ln(2p/|1-2p|), correction <=(8/e)Ent(p_x)<=16E_A/e, universal block/tree transfer and density-free projection exclusion C_proj<37/4. Pilot{pilot["assertions"]} checks/{pilot["seconds"]:.6f}s; full{check["assertions"]} checks/{check["seconds"]:.6f}s,1978 blocks and548 trees, fixed rare widths0..6. No new critical violating root claimed. Universal proper-block admission remains open. Required artifacts schema-checked and saved.\n'
learn=f'\n{marker}: Exact natural sign/raw correction T(p)=h((1-2p)^2)-4h(p^2)-8ln2 p(1-p), with T\'\'=16ln(2p/|1-2p|). T+(8/e)p ln p is convex, so its actual child Jensen gap is <=(8/e)Ent(p_x). Cube log-Sobolev on sqrt(p_x), using the L2 reverse triangle inequality for actual indicator children, gives Ent(p_x)<=2E_A(g). Therefore L_sign<=4Lambda_raw+4/(e ln2)I_A, universally and terminal-inclusively on the same restriction tree. The paid projection class now has physical critical sign ratio <=4+2/ln2+4/(e ln2)<37/4 at every positive support density. Proper projection-block admission and overlapping/connected support remain unproved.\n'
for name,text in [('WORKLOG.md',work),('LEARNED.md',learn)]:
 p=AGENT/name
 if marker not in p.read_text(encoding='utf-8'):
  with p.open('a',encoding='utf-8') as f:f.write(text)
protocol=json.loads(sources[2].read_text());ckeys=set(protocol['required_per_run']['claim_fields']);pkeys=set(protocol['required_per_run']['progress_fields']);pkeys.remove('packet_ids (one primary ID, for compatibility)');pkeys.add('packet_ids')
assert set(claim)==ckeys and set(progress)==pkeys
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
receipts=[]
for p in sorted(ROOT.rglob('*')):
 if p.is_file() and p.name!='RECEIPTS.json':
  assert p.stat().st_size<20_000_000;receipts.append(dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=sha(p)))
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
 p=AGENT/name;receipts.append(dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)))
save(ROOT/'out/RECEIPTS.json',receipts)
print(json.dumps(dict(status='SAVED_AND_SCHEMA_CHECKED',receipts=len(receipts),assertions=check['assertions'],price_display=display,full_fei='OPEN'),indent=2))
