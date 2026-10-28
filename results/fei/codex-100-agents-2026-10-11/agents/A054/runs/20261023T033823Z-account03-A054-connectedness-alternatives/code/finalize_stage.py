from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1];FLEET=A.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(name,obj):(R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
base=Path('math-open-problems/reports/fei-2026-10-11')
P=read(base/'EXECUTION_PROTOCOL.json');main=read(R/'out/EXACT_CHECK.json');ind=read(R/'out/INDEPENDENT_CHECK.json');rank=read(R/'out/RANK_CHECK.json');pilot=read(R/'out/PILOT.json');lean=read(R/'out/LEAN_ADMISSION.json')
assert all(x['status']=='PASS' for x in [main,ind,rank,pilot])
total=main['assertions']+ind['assertions']+rank['assertions']
src=[base/'EXECUTION_PROTOCOL.json',FLEET/'BOARD.md',FLEET/'claude/B11/STREAM_NOTES.md',A/'runs/20261022T223731Z-account03-A054-connectedness-alternatives/FIBER_ADMISSION_AUDIT.md',A/'runs/20261014T055856Z-account05-A054-connectedness-alternatives/OVERLAP_PAYMENT.md',A/'runs/20261014T025808Z-account05-A054-connectedness-alternatives/RAW_SIGN_TRANSFER.md',A/'runs/20261014T055856Z-account05-A054-connectedness-alternatives/code/mathcore.py']
for agent,run,files in [('A052','20261023T014825Z-account03-A052-critical-source-structure',['REPORT.md','RANK_PAIR_PROOF.md']),('A051','20261023T002518Z-account03-A051-near-extremizer-definition',['REPORT.md','RESET_BUDGET.md']),('A055','20261022T233657Z-account03-A055-extremal-obstruction-referee',['REPORT.md'])]:
 src += [A.parent/agent/'runs'/run/f for f in files]
write('out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'pin':'observed local bytes; shared sources are read-only, mutable hashes are observations'} for p in src])
stmt=('For every actual nonempty cube support U of mass p, let f=1-2*1_U and transport its original connected-component labels through an invertible affine INPUT map T, without output-character multiplication. Let gamma_A count directed internal edges across inherited labels in the reset chart. Then sum_l 4E_A(g_l composed with T)=I_A(f composed with T)+2gamma_A; W_singleton=Inf_i/2+gamma_i; and max_proper (W_A-gamma_A)/(|A|p)=max_i Inf_i/(2p) for n>=2. For a nonincreasing-influence input reset with release rho, its signed labelled release is rho_L=rho-2gamma_all. With old booked debit0<=u<=rho, unused R=rho-u, 2gamma_A<=R and W_A>=|A|p/2 imply L_A<=C I_A+4R<=C(I_A+R), C=4+2/ln2+4/(e ln2). All actual child entropies and signed terminal component excess remain. Minimizing labelled directional cost ell(v)=w(v)+2gamma(v) by a greedy independent basis guarantees rho_L>=0; rho_L>=u suffices to fund all crossing flux from unused release. At an input-influence-minimal root that optimizer has rho=gamma_all=0. Actual activated bent functions F_k=1-A_k-A_k*(-1)^(ab+cd), k>=2, with shear a<-a+c, have full affine span, minimum affine influence, rho=0 and gamma_all=2^-k/8>0, refuting free crossing funding by rho alone. Universal block/fragment selection and full FEI are not asserted.')
cid='A054-RESET-COMPONENT-CROSSING-INTERFACE'
claims=[dict(claim_id=cid,version=1,exact_statement=stmt,hypotheses=['Finite uniform Boolean cube; n>=2 for proper-block maximum; p>0 for conditional normalization; entropy in bits','Labels are the original actual components before reset, retained in every actual child','Reset is invertible affine INPUT change only, no character multiplication; its ordinary release is nonnegative where used as funding','The old debit u is retained, and only R=rho-u is available; require2gamma_A<=R and the stated W threshold','Critical exclusion at K>=C assumes least essential dimension among positive K-violations, so every reset/query child is eligible'],statement_sha256=hashlib.sha256(stmt.encode()).hexdigest(),contributors=['account03/A054'],proof_source={'path':str(R/'RESET_COMPONENT_INTERFACE.md'),'sha256':sha(R/'RESET_COMPONENT_INTERFACE.md'),'locator':'Sections1--5; equations1--11'},proof_dependencies=[{'claim_id':'A054-RAW-SIGN-BLOCK-TREE-TRANSFER','version':1,'acceptance':'AUTHOR_PROVED_SOURCE_COMPLETE_PENDING_INDEPENDENT_REVIEW','used_scope':'universal sign/raw transfer and row bound; independent of component geometry'}],review_records=[],status='AUTHOR_PROOF_EXACT_VALIDATION_PASS_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=['Unregistered helper2gamma_all<=rho for arbitrary influence-nonincreasing input resets; explicit activated bent witness'],first_unproved_line=None,next_consumers=['A051','A052','A053','A055','A090','A094','claude/B11','B20'])]
write('CLAIMS.json',claims)
next_action='At an actual child of a genuine high-K critical source, select a label-aware reset and next original query whose crossing flux and full signed bill fit SAME unused release after the previous debit; retain both terminal deficits and mixed T.'
prog=dict(protocol_revision=P['revision'],run_id=R.name,stream='B11',packet_id='A054',gap_id='G-R-SELECT',attempt_id='A054-stage18-inherited-label-reset-interface',method='Source-scoped rank review; exact crossing-edge interface; executable labelled minimum-basis repair; actual zero-release Boolean counterfamily; finite exact validation.',mathematical_delta='Inherited-label flux is a necessary additional interface under input resets; prove paid coefficient8gamma<=4R from SAME unused release and supply labelled rank optimizer; canonical roots have no such new funding.',deliverable_status='COMPLETE_LOCAL',mathematical_status='AUTHOR_PROOF_EXACT_VALIDATION_PASS_FULL_FEI_OPEN',claim_versions_used=['A054-RAW-SIGN-BLOCK-TREE-TRANSFER@1','A054-FIBER-ADMISSION-SINGLETON-AUDIT@1'],claims_created_or_changed=[cid+'@1'],source_artifacts=['RESET_COMPONENT_INTERFACE.md','REVIEW_A052.md','out/FROZEN_SPEC.json','out/FROZEN_RANK.json','out/EXACT_CHECK.json','out/INDEPENDENT_CHECK.json','out/RANK_CHECK.json','out/LEAN_ADMISSION.json','out/SOURCE_RECEIPTS.json'],next_consumers=['A051','A052','A053','A055','A090','A094','claude/B11','B20'],next_action=next_action,stagnant_substantive_attempts=0,blockers=['Universal selected original-pair/continuation payment is OPEN.','Input-influence-minimal roots force the labelled optimizer to have zero release/flux; useful reserve must arise after an actual query.','Output-character resets change sign support and are outside this transported-label theorem.','New theorem independent review pending; Lean compiler admission held; remote mirror/adoption unverified.'],packet_ids=['A054'])
write('PROGRESS.json',prog);write('PACKET_DELTA.json',prog)
report=f'''# exact target, quantifiers, hypotheses and units

A054/B11 stage18 repairs connected-component interface accounting when
actual physical queries are interleaved with input-affine resets. All
cubes finite and uniform, signs Boolean, Fourier entropy bits. Let p>0
be negative support mass and retain ORIGINAL actual component labels.
Input maps are invertible and preserve p; output-character centering is
excluded because it changes the sign support. All terminals and old
debits remain. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

BOARD snapshot2026-10-23 03:34UTC, unchanged B11 STREAM_NOTESv2 and own
STATUS read at stage start. Protocol2026-10-11-execution-v2 schema and
dispatch/compute rules retained from the prior complete read and reloaded
by the finalizer. New A051 RESET_BUDGET Sections1--3, A052 RANK_PAIR_PROOF
Sections1--5 and its REPORT, and A055 newest REPORT consumed. Prior
A054 fiber audit, raw/sign transfer, overlap theorem and helper revisited.
Earlier campaign and paper baseline reads are not a fresh paper audit.
out/SOURCE_RECEIPTS pins local bytes; changing shared-file hashes are
observations, not immutable commit claims. One two-wording read-only
math recall returned WEAK MATCH and no answering card; it is no premise.
The degraded wake's stale owner-model/state notes were reported; current
orders and research artifacts govern.

# complete derivation or exact first unsupported line

RESET_COMPONENT_INTERFACE.md supplies all proofs. Direct physical edge
counting gives labelled influence I^L=I+2gamma. Original labels become
noncomponent labels after a shear, and W_i=Inf_i/2+gamma_i. Conditional
entropy chains imply2W_A<=I_A+2gamma_A. The corrected all-block maximum
is still the singleton maximum; a reset cannot carry free component
credit. The exact raw terminal excess Delta=X_A+Z_A is retained.

The signed labelled release satisfies rho_L=rho-2gamma_all. An actual
full-span affine-minimal activated bent family has rho=0 and
gamma_all=2^-k/8, k>=2, despite total influence tending to0. On its
original c query, W_c=3q/8>=p/2=5q/16 but Inf_c=q/2<p=5q/8. The
uncorrected post-reset component inference fails. This refutes the
unregistered free-flux helper, not A052 rank funding or FEI.

With an old debit u, unused release R=rho-u, the explicit crossing
interface8gamma_A is paid at4R whenever2gamma_A<=R. Combined with the
actual raw/sign row bound and W_A>=rp/2 this proves
L_A<=C I_A+4R<=C(I_A+R), at the SAME C=4+2/ln2+4/(e ln2)<37/4.
The complete actual terminal identity is equation10. At K>=C and u=0
this excludes the stated least-dimensional critical class, using genuine
smaller-child nonviolation. It is not a restriction-closed FEI class.

An executable greedy rank optimizer with labelled directional cost
ell(v)=w(v)+2gamma(v) guarantees rho_L>=0 and supplies flux funding;
rho_L>=u is a sufficient test with an old debit. However an already
input-influence-minimal root forces rho=gamma=0. This limitation is
explicit, and the optimizer does not select a paid next query.

FIRST UNSUPPORTED LINE: choose an actual query/reset/next-query fragment
on a genuine high-K source whose full signed row bill and crossing flux
fit SAME unused descendant release after all prior debits. Conditions
on labelled decrease and W are sufficient hypotheses, not consequences
of criticality. Output-character resets need a new sign-partition ledger.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC and FROZEN_RANK precede their jobs. Final main pilot:
{pilot['assertions']} assertions. Main full: {main['assertions']} exact assertions,
{main['transforms']} transforms, {main['block_cases']} block cases, and
{main['paid_actual_terminal_cases']} full actual-terminal payment tests, PASS in
{main['seconds']:.6f}s. Domain: all276 labelled truth tables n1..3,
all elementary ordered shears (empty supports skipped for conditional
normalization), every proper query block, plus four fixed activated bent
fixtures k0,2,3,4. Three positive crossing/payment examples with actual
nonzero entropy drops are saved. The old-debit boundary guard demonstrates
that a release fully used by crossing cannot be offered again.

Independent direct-character/explicit-label/all-direction replay:
{ind['assertions']} assertions PASS in {ind['seconds']:.6f}s, on the four fixed
fixtures and every physical translation through8bits. It verifies the
complete Fourier-coefficient magnitude multiset, exact gamma, all parity
costs and the affine-minimum criterion without importing the main helper.
Rank checker: {rank['assertions']} assertions PASS in {rank['seconds']:.6f}s,
{rank['nonempty_roots']} nonempty roots, exhaustive unordered bases1/3/28 through3bits
versus greedy/rank-integral values, {rank['positive_release_roots']} positive-release roots,
and {rank['input_minimal_roots']} input-minimal roots with zero new release/flux.
Total final full checks {total}, excluding pilots and the initial v1
algebra-only pilot. This is this stage's targeted count, separate from
the preceding8776 checks; no count is cumulative.

Commands: python -X utf8 followed by this run's code/check_reset_flux.py
--pilot then full; code/independent_fixture.py; code/check_label_rank.py
--pilot then full; code/run_lean.py. The v2 main specification was frozen
before rerunning pilot/full to add complete actual entropy terminals.
Integer edge counts, Fraction and exact prime-log vectors certify
identities; outward112-bit rational atanh intervals with explicit tail
decide signs. The finite payment replay uses37/4 as a rigorous relaxation;
the exact C theorem uses the analytic source bound, not floating estimates.

Python estimates70--110MB and55s caps, no GPU, detached work or dimension
escalation. Fresh memok exited{lean['gate_exit']}; the separate stricter compiler
admission returned {lean['status']}. No compiler started. FluxBudget.lean
formalizes only the intended scaled scalar flux inequality and is not
certified. Rung: written proof plus exact validation; new independent
acceptance pending. No whole-Fourier Lean certificate is claimed.

# proof dependencies and changed downstream conclusions

The flux identity, corrected admission maximum, counterfamily, signed
release and labelled rank optimizer are derived locally. Payment uses
A054-RAW-SIGN-BLOCK-TREE-TRANSFER@1 and its raw-row upper bound, still
author-proved/pending independent review. REVIEW_A052 analytically
reconstructs only RANK_PAIR_PROOF Sections1--2, HOLDS without repair;
source paid-family Sections3--5 and census counts are not newly accepted.

This repairs a potential interface omitted when mixing A054 component
credit with B11 affine resets. A052's actual signed child bank remains
valid. Ordinary union release alone does not pay transported-label
flux. Label-aware cost supplies a precise alternative with one owner,
but output centering, original-pair selection and spent-descendant
continuation remain unpaid. No universal constant improves.

# one next mathematical action and independent reviewer

{next_action}
A051/A052/A053/A055 consume the new interface. A090 should reconstruct
edge normalization and finite rank minimization; A094 should challenge
support preservation, old debit, terminal component excess and canonical
root inertness. No outgoing messages or shared-index writes occurred.

# actual persistence receipts or precise save blocker

Four protocol files, full proof, scoped source review, frozen specs,
code and exact outputs saved in the requested A054 run. STATUS has two
lines; WORKLOG and LEARNED appended. out/RECEIPTS verifies exact schema
fields, statement/proof hashes, byte-identical progress copies and20MB
file caps. Independent review, supervisor GitHub copying, registry adoption
and brain ingestion remain unverified; no local save blocker. No git,
mail, brain write, other-agent mutation, or trading process was used.

# Universal bridge

C019 stopping-tree payment through B11 critical selection gains an exact
inherited-component crossing interface and an executable labelled rank
reset:8gamma_A is paid by4 times SAME unused release, with prior debit
and full actual terminals retained. The neutral bent counterfamily proves
why union-rank release alone cannot supply this payment. Universal gain
is zero: canonical roots have no new labelled funding and selected
descendant continuation remains open. NEXT joins actual child eligibility,
independent rank and this flux cost after a real query, because that is
the missing implication toward full FEI; another uncorrected connectedness
or affine class would only reuse the interface the counterfamily defeats.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text(f'STATE: A054 stage18 saved: inherited-label flux paid by SAME unused labelled-rank release; zero-rho affine-minimal bent guard; {total} exact checks PASS; FEI OPEN, review pending.\nNEXT: A051/A052/A053/A055 select actual child reset/next query with crossing flux and signed bill inside SAME remaining release after old debit; A090/A094 review.\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
for name,marker,line in [('WORKLOG.md','stage18: inherited-label reset interface',f'\n{stamp} stage18: inherited-label reset interface repaired. I^L=I+2gamma; zero-rho full-span affine-minimal bent roots expose free-credit failure. Labelled rank minimization funds8gamma at4 unused release, preserves old debit and complete terminals. {total} exact checks PASS. Canonical-root funding is zero; descendant selection and FEI OPEN.\n'),('LEARNED.md','Stage18 durable:', '\nStage18 durable: Under INPUT affine resets original component labels can cut new internal edges. I^L=I+2gamma, W_i=Inf_i/2+gamma_i, and corrected block admission still collapses to singleton influence. rho_L=rho-2gamma_all can be negative even when rho=0: activated -(-1)^(ab+cd), shear a<-a+c, gives gamma=q/8 and full affine minimum. Unused R=rho-u pays crossing8gamma<=4R if2gamma<=R; all child and spectral terminal excess retained. A minimum labelled-cost parity basis (cost w+2gamma) guarantees rho_L>=0; rho_L>=u funds the old-debit case. At input-minimal roots this optimizer has rho=gamma=0, so universal continuation still needs actual descendant release and selected signed query. No output-character transport is covered.\n')]:
 existing=(A/name).read_text(encoding='utf-8') if (A/name).exists() else ''
 if marker not in existing:
  with (A/name).open('a',encoding='utf-8') as f:f.write(line)
expected=set(P['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(prog)==expected
assert all(set(c)==set(P['required_per_run']['claim_fields']) for c in claims)
assert all('# '+h in report for h in P['required_per_run']['report_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
receipts=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='RECEIPTS.json':
  assert p.stat().st_size<20_000_000
  receipts.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
write('out/RECEIPTS.json',{'status':'PASS','protocol_fields':'EXACT','compatibility_copy':'BYTE_IDENTICAL','total_final_exact_checks':total,'files':receipts,'rolling':[{'path':str(A/name),'sha256':sha(A/name)} for name in ['STATUS.md','WORKLOG.md','LEARNED.md']],'review':'PENDING','remote_copy':'UNVERIFIED'})
print(json.dumps({'status':'COMPLETE_LOCAL','exact_assertions':total,'files':len(receipts),'lean':lean['status'],'protocol':'PASS'}))
