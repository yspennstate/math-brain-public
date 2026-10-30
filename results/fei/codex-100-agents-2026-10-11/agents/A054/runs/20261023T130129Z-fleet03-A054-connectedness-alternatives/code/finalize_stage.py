from pathlib import Path
import json,hashlib,datetime,subprocess,sys
R=Path(__file__).resolve().parents[1];A=R.parents[1];FLEET=A.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,obj):(R/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
base=Path('math-open-problems/reports/fei-2026-10-11');P=read(base/'EXECUTION_PROTOCOL.json')
main=read(R/'out/EXACT_CHECK.json');ind=read(R/'out/INDEPENDENT_CHECK.json');pilot=read(R/'out/PILOT.json')
assert all(o['status']=='PASS' for o in [main,ind,pilot]);total=main['assertions']+ind['assertions']
prev=A/'runs/20261023T105740Z-fleet03-A054-connectedness-alternatives'
src52=FLEET/'agents/A052/runs/20261023T120425Z-fleet03-A052-critical-source-structure'
sources=[base/'EXECUTION_PROTOCOL.json',FLEET/'BOARD.md',FLEET/'claude/B11/STREAM_NOTES.md',src52/'REPORT.md',src52/'ALIGNMENT_PROOF.md',src52/'CLAIMS.json',prev/'FORCED_DIRECTION_PROOF.md',prev/'CLAIMS.json',FLEET/'agents/A051/runs/20261023T113401Z-fleet03-A051-near-extremizer-definition/REPORT.md',FLEET/'agents/A055/runs/20261023T112023Z-fleet03-A055-extremal-obstruction-referee/REPORT.md',FLEET/'agents/A053/runs/20261023T123501Z-fleet03-A053-near-tensor-perturbations/LINEAR_RADIUS_PROOF.md']
write('out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'provenance':'observed local read-only bytes; scope in REPORT, mutable board hash not an immutable commit'} for p in sources])
c52=read(src52/'CLAIMS.json')[0]
write('out/REVIEW_RECEIPT.json',{'source_claim_id':c52['claim_id'],'version':c52['version'],'statement_sha256':c52['statement_sha256'],'proof_sha256':sha(src52/'ALIGNMENT_PROOF.md'),'reviewer':'fleet03/A054','scope':'Sections1--4 and6 analytic fixed-K deficit normal form, signed full original-pair rows, influence change, complete bank; excludes source census/global four-bit maximizer certificate and other scopes','verdict':'SCOPED_HOLDS_WITHOUT_REPAIR','review':'REVIEW_A052.md'})
cid='A054-RESET-COMPONENT-CROSSING-INTERFACE';cons=['A051','A052','A053','A055','A090','A094','claude/B11','B20']
stmt=('For every uniform finite Boolean sign F and original proper coordinate pair A, let W be the outside translation space, c(v)=P[F(X)!=F(X+v)], b(q)=min_{v+W=q}c(v), mW the minimum c-cost basis of W and mQ the minimum b-cost basis of V/W. Then J_A(F)=mW+mQ is exactly minimum input-affine influence preserving the ORIGINAL query partition, and each minimum is its threshold-rank integral. For a source f, rematch one complete original cofactor by s*chi_v and call the resulting actual Boolean root F, retaining all four full signed Fourier rows. Set Delta=I(F)-I(f), R=I(F)-J_A(F)>=0. If f is initially joint input-affine/cubic-phase D_K maximal, or stationary under these composites, K>0, then H(F)-H(f)<=K(Delta-R). Thus Omega=H(f)-H(F)+K Delta pays the explicit KR interface. Let t be mean full affine/character minimum child influence, S* the complete optimized child reserve and L_F the full rematched entropy decrement. The exact ORIGINAL-source bank is D_K(f)+S*=L_F-K(J_A(F)-t)+Pi, Pi=Omega-KR. With old booked0<=u<=R it is L_F-K(J_A(F)+u-t)+(Pi+Ku). Pi>=0 under initial joint stationarity, and S*>=0 under genuine least dimension. A genuine3bit global D2-maximizer negative only at000, rematched on original branch1 by its outside character, has new support{0,5}, Hnew2,Inew3/2,J1,R1/2,S*=0; the new pair is exactly paid while the original positive deficit remains Pi. This refutes dropping Pi, not FEI or a sufficiently-high-K theorem. Prior version2 component-crossing payment remains valid for fresh labels of F transported through INPUT maps; old labels cannot be carried through a sign-changing phase. Universal pair selection/full FEI not asserted.')
claim=dict(claim_id=cid,version=3,exact_statement=stmt,hypotheses=['Finite uniform Boolean cube n>=3; entropy bits; ORIGINAL proper pair and its four complete actual children','J optimizes input maps preserving that partition only; output phases are the explicitly charged branch rematches','Rank-completed inequality requires joint input/degree<=3 output-phase initial normal form, not phase-only stationarity or descendant stationarity','Old debit0<=u<=R and all complete signed terminal reserves retained; genuine critical nonnegativity requires least essential dimension at the SAME K'],statement_sha256=hashlib.sha256(stmt.encode()).hexdigest(),contributors=['fleet03/A054'],proof_source={'path':str(R/'PAIR_RANK_INTERFACE.md'),'sha256':sha(R/'PAIR_RANK_INTERFACE.md'),'locator':'Sections1--5, equations1--6 and explicit genuine critical guard'},proof_dependencies=[{'claim_id':c52['claim_id'],'version':c52['version'],'acceptance':'SCOPED_INDEPENDENT_RECONSTRUCTION_HOLDS_WITHOUT_REPAIR','used_scope':'finite joint cubic-phase deficit normalization and actual signed pair/terminal identities; REVIEW_A052 excludes source census'},{'claim_id':cid,'version':2,'acceptance':'AUTHOR_PROOF_EXACT_VALIDATION_PASS_PENDING_INDEPENDENT_REVIEW','used_scope':'inherited-component local interface payment, input-only scope and old-debit bank'}],review_records=[],status='AUTHOR_PROOF_EXACT_VALIDATION_PASS_PENDING_INDEPENDENT_REVIEW',supersedes=[cid+'@2'],refutes=['Unregistered helper: an exactly paid rematched same-original-partition pair can exclude the original genuine critical source after omitting Pi; explicit3bit K2 global-max counterguard'],first_unproved_line=None,next_consumers=cons)
write('CLAIMS.json',[claim])
next_action='A052/A051 combine rank-completed ORIGINAL-pair alignment with exact nonnegative smaller-child reserves to force high-K payment INCLUDING Pi and every old debit; A090/A094 independently reconstruct quotient lifts, phase price and critical guard.'
prog=dict(protocol_revision=P['revision'],run_id=R.name,stream='B11',packet_id='A054',gap_id='B11-SIGNED-CRITICAL-QUERY-RESET-SELECT',attempt_id='A054-stage20-rank-completed-phase-interface',method='Independent source reconstruction; exact internal/quotient rank optimization; signed nonlinear phase interface; genuine critical counterguard; exact finite certificates.',mathematical_delta='Complete A052 signed pair alignment by the exact whole partition-preserving rank release R, giving entropy change<=K(Delta-R); retain phase price Pi in ORIGINAL bank. Genuine globally D2-critical counterguard has positive R and exactly paid new pair but positive original Pi.',deliverable_status='COMPLETE_LOCAL',mathematical_status='AUTHOR_PROOF_EXACT_VALIDATION_PASS_FULL_FEI_OPEN',claim_versions_used=[cid+'@2',c52['claim_id']+'@'+str(c52['version'])],claims_created_or_changed=[cid+'@3'],source_artifacts=['PAIR_RANK_INTERFACE.md','REVIEW_A052.md','out/FROZEN_SPEC.json','out/FROZEN_ADMISSION.json','out/EXACT_CHECK.json','out/INDEPENDENT_CHECK.json','out/EXAMPLES.json','out/SOURCE_RECEIPTS.json','out/REVIEW_RECEIPT.json'],next_consumers=cons,next_action=next_action,stagnant_substantive_attempts=0,blockers=['Universal sufficiently-high-K ORIGINAL-pair payment including Pi remains open.','Joint stationarity is an INITIAL finite source choice, not inherited by descendants.','A nonlinear phase changes sign support; original component labels cannot cross that operation for free.','New version independent review, registry adoption and remote supervisor copies unverified.','Shared checklist lock/timeout is administrative; brain personal-model/state/dream freshness degraded.'],packet_ids=['A054'])
write('PROGRESS.json',prog);write('PACKET_DELTA.json',prog)
# Required checklist infrastructure is separate from owned research outputs.
try:
 p=subprocess.run([sys.executable,'-X','utf8','task_checklist_hook.py','done','T-20261023-476',f'A054 stage20 saved: rank-completed pair alignment, genuine critical phase-price guard;{total} exact checks;full FEI/review open.'],capture_output=True,text=True,encoding='utf-8',timeout=8)
 admin={'exit_code':p.returncode,'output':(p.stdout+p.stderr)[-500:]}
except subprocess.TimeoutExpired:admin={'status':'TIMEOUT_8S','meaning':'closure unverified; shared lock not changed; no retry'}
write('out/CHECKLIST_END.json',admin)
report=f'''# exact target, quantifiers, hypotheses and units

A054/B11 stage20 strengthens signed ORIGINAL-pair interface payment toward
full FEI. Finite uniform Boolean signs, Fourier entropy bits, n>=3,
proper ORIGINAL pair A, outside translation space W. All four complete
children, mixed signed rows, phase costs and old debits remain. Full FEI
OPEN. Current owner deadline23October14:49UTC governs the old protocol clock.

# sources actually read, revisions and theorem locators

BOARD12:58UTC, unchanged lead STREAM_NOTESv2 and own stage19 STATUS read
at start. Actual protocol2026-10-11-execution-v2 fields refreshed; prior
full campaign/registry/plan/supplement/four-manuscript baseline reads
retained, not presented as new full audits. A05212:04 REPORT and whole
ALIGNMENT_PROOF read; REVIEW_A052 independently reconstructs analytic
Sections1--4 and6 without repair, excluding source census/global4bit
maximizer and other scopes. A05111:34 and A05511:20 REPORT-scoped occupation
and ALL-block debt objections consumed; A053 current linear-radius head
inspected without theorem adoption. Prior A054 marked-query proof and
claim remain dependencies. out/SOURCE_RECEIPTS pins observed local bytes,
not immutable commits. No outside novelty or recalled theorem premise.

Fresh wake warned personal-model99.5h, state-of-mind84.1h and dream34.8h
stale; the owner was told before affected notes were used. Brain self-care
degraded/unverified; personal-context/consolidation reliability remains
affected. Current instructions and actual proof sources govern.

# complete derivation or exact first unsupported line

PAIR_RANK_INTERFACE Sections1--5 proves the full derivation. Every input
basis preserving the original query partition consists of an outside
basis and lifted quotient basis. Their independent exact minima give
J=mW+mQ, each a finite threshold-rank integral; for a pair mQ is the
sum of the two cheapest of THREE quotient directions. This accounts for
all dependent directions and actual lifts, rather than adding swap gains.

After an explicit one-branch character rematch F, R=I(F)-J is the actual
entire partition-preserving input release. Initial JOINT cubic-phase/
input-affine stationarity forces H(F)-H(f)<=K(DeltaI-R), sharpening A052's
physical-phase inequality by KR. The compensated entropy/influence price
Omega pays KR. Pure phase stationarity alone does not justify this extra
input operation. Sign-support labels must restart after the phase; only
subsequent INPUT maps transport those fresh actual component labels.

The original bank retains Pi=Omega-KR: D0+S*=L_F-K(J-t)+Pi. With old
booked u it is L_F-K(J+u-t)+(Pi+Ku), exactly the same account. In a
genuine initial critical normal form S*>=0 and Pi>=0. Their nonnegativity
does not mean either term can be erased. Version2's local8gamma component
interface remains paid by4(R-u) under its stated fibre/flux hypotheses
for the NEW root; ORIGINAL-root transfer must still retain Pi+Ku.

Explicit genuine critical guard: n3 negative support{{000}}, K2, global
D2-maximal among ALL256 sources and least dimension by ALL22 smaller
sources. Its positive deficit is5/2-(9/8)log2(3), certificate2^20>3^9.
Original pair(0,1), rematch branch1 by outside character, gives support
{{0,5}}, Hnew2,Inew3/2,J1,R1/2. All complete child entropies and affine
minima are0, so S*=0 and the NEW original-partition pair is EXACTLY paid.
The ORIGINAL positive deficit remains Pi. This refutes only omitting the
phase price, even with genuine criticality; it is a LOW-rate guard and
does not refute a sufficiently-high-K selection theorem or FEI.

FIRST UNSUPPORTED UNIVERSAL LINE: for high absolute K combine completed
alignment, exact nonnegative smaller-child reserves and all mixed Boolean
rows to force a paid ORIGINAL pair INCLUDING Pi and old debits. A large
rank release or an apparently paid rematched row alone does not do this.

# executed validation with domain, arithmetic, commands and outputs

Frozen specifications precede searches. Main pilot: {pilot['assertions']}
checks on768 competitors, PASS in{pilot['seconds']:.6f}s, excluded from
final total. Full primary: {main['assertions']} checks,15552 signed
competitors,960 critical competitors,8475 positive-release competitors,
PASS in{main['seconds']:.6f}s. Domain ALL256 labelled3bit signs and17
fixed4bit signs (mask1 plus first16 prescribed LCG masks), every ORIGINAL
proper pair, every changed branch, every outside character and BOTH
signs. Every signed coefficient, physical influence change, exact internal
and quotient rank minimum, constructed reset, complete child orbit values
and full bank at u0 and fully spent R are checked. No exhaustive4bit
or new global4bit cubic-orbit claim. Three-bit D2 maxima are selected
against all256, and lower-dimensional FEI2/FEI3 checks are exact.

Independent replay imports no primary helper: direct character sums,
EVERY ordered partition-preserving input basis/lift map, explicit complete
child character/basis minima, integer-product entropy sign certificates.
{ind['assertions']} checks, {ind['examples']} representatives including
the explicit critical fixture, {ind['ordered_actual_maps']} actual maps,
PASS in{ind['seconds']:.6f}s. Independent admission covers all2563bit
sources plus22 smaller sources and the fixed4bit point deficit formula;
the latter's positive deficit has2^144>7^49. All mixed data and complete
terminals retained. This is an independent implementation by A054, not
independent-agent acceptance. Final NEW-stage total{total}; pilot and
all previous-stage counts excluded. No floating sign decision.

Commands: python -X utf8 code/check_pair_rank.py --pilot; same without
--pilot; python -X utf8 code/independent.py. Each job capped55s, expected
130--140MB peak (unmeasured), sequential, no >300MB job so no heavy-job
admission required. No dimension escalation, GPU, detached work or Lean
certificate. Resource warnings were not treated as live admission, and
no governor or existing work was restarted, killed or throttled.

# proof dependencies and changed downstream conclusions

This is version3 extending the existing A054 interface candidate, not a
third broad unreviewed candidate. A052 analytic finite-normal-form and
signed-pair identity scope independently HOLDS without repair. The new
rank-completed inequality, explicit whole-phase interface and exact
critical counterguard are author-proved with finite exact validation;
independent review remains pending. Prior component-interface payment
retains its stated hypotheses and input-only label transport. No registered
theorem refuted. The rank credit must be paired with its entropy price;
source canonicalization is initial and cannot renew descendant budgets.
Universal constant gain0; no all-dimensional pair supplier is proved.

# one next mathematical action and independent reviewer

{next_action} A051/A055 consume the genuine critical phase-price guard;
A053 retains actual complete-terminal payment; B11/B20 coordinate source-
bound adoption. No external messages sent.

# actual persistence receipts or precise save blocker

All four protocol files, proof, scoped review, frozen specs, code and
exact outputs saved only in A054's research tree. Finalizer checks exact
schema keys, statement hash, proof hash, byte-identical progress copies,
required report headings,20MB cap and two-line STATUS. Persistence receipt
hashes all run artifacts and rolling files; subsequent readback required.
Shared checklist working/old347 closure timed out8s; current476 closure
receipt is out/CHECKLIST_END, result {admin.get('status',admin.get('exit_code'))};
no shared lock changed. This administrative issue does not block the math.
Independent acceptance, shared registry adoption, supervisor repository
copies and brain ingestion unverified. No git, mail, brain-content writes,
other-agent research mutation, deletion or trading access. All stage
mathematical jobs finished; no existing work stopped; nothing left running.

## Universal bridge

C019 stopping-tree payment gains a stronger exact ORIGINAL-pair source
constraint: optimize internal and quotient ranks to price the entire
partition-preserving input reset, then charge its release against the
actual phase entropy/influence interface. The genuine critical K2 guard
shows that even a paid rematched pair with positive rank release retains
positive ORIGINAL deficit as Pi. Universal constant gain is zero. What
remains is high-K pair selection with Pi, exact nonnegative full child
reserves and all old debits paid together. NEXT targets that joint signed
rank/price inequality, the missing universal supplier, rather than another
weak admission class already known to preserve arbitrary-core hardness.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
status=f'STATE: A054 stage20 saved: exact ORIGINAL-pair internal/quotient rank completion; phase price retains genuine K2 critical counterguard; {total} exact checks PASS; FEI OPEN, review pending.\nNEXT: Force high-K ORIGINAL-pair payment including Pi, full nonnegative child reserves and old debits; A052 consume completed alignment; A090/A094 review.\n'
(A/'STATUS.md').write_text(status,encoding='utf-8')
entries={'WORKLOG.md':f'\n2026-10-23 {R.name}: consumed A052 cubic-phase alignment and independently reconstructed analytic Sections1--4,6 without repair. Exact partition-preserving influence minimum is internal-basis plus quotient-lift minimum. Initial joint phase/input criticality gives entropychange<=K(DeltaI-R); ORIGINAL bank retains Pi=Omega-KR, or Pi+Ku with old debit. Actual global D2-maximal3bit point source rematches to exactly paid pair with R1/2 but positive original Pi. {total} new final exact checks PASS; independent review/full FEI OPEN. No existing work stopped, nothing running.\n','LEARNED.md':f'\n2026-10-23 {R.name}: For ORIGINAL pair with outside space W, exact partition-preserving input minimum J=mW+mQ, quotient costs b(q)=min_lift w(v); both are threshold-rank integrals and pair quotient cost is two cheapest of three. Joint INITIAL cubic-phase/input D_K stationarity forces Hnew-H0<=K(DeltaI-R), R=Inew-J. Omega pays KR, but original bank is D0+S*=Lnew-K(J-t)+Pi with Pi=Omega-KR>=0, not a free refund. Old u retains Pi+Ku against J+u. Genuine3bit K2 global-max point defect rematches to U{{0,5}}, H2,Inew3/2,J1,R1/2,S0; new pair exactly paid while original Pi=D2>0. No child stationarity or old support-label transport through phases. Universal high-K supplier remains open.\n'}
for name,entry in entries.items():
 p=A/name
 if R.name not in p.read_text(encoding='utf-8'):
  with p.open('a',encoding='utf-8',newline='') as f:f.write(entry)
(R/'CHECKPOINT.md').write_text('STATE: COMPLETE_LOCAL; final proof, exact certificates, four protocol files and rolling records saved; FEI OPEN.\nNEXT: '+next_action+'\n',encoding='utf-8')
assert set(prog)==set('packet_ids' if k.startswith('packet_ids ') else k for k in P['required_per_run']['progress_fields'])
assert set(claim)==set(P['required_per_run']['claim_fields'])
assert all('# '+h in report for h in P['required_per_run']['report_fields'])
assert hashlib.sha256(claim['exact_statement'].encode()).hexdigest()==claim['statement_sha256']
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json']
assert all(p.stat().st_size<20*1024*1024 for p in files)
write('out/PERSISTENCE_RECEIPT.json',{'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in files+[A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']],'full_fei':'OPEN','independent_review':'PENDING','remote_copy':'UNVERIFIED'})
print(json.dumps({'status':'SAVED_SCHEMA_PASS','claim':cid+'@3','assertions':total,'files':len(files),'full_fei':'OPEN','checklist':admin.get('status',admin.get('exit_code'))}))
