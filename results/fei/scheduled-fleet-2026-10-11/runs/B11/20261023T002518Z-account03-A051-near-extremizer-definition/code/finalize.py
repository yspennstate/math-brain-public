from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1];TEAM=A.parents[1]
P=Path('~/mop_fei100/reports/fei-2026-10-11');RUN=R.name
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,x):
    (R/p).write_text(x if isinstance(x,str) else json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def append(p,s):
    old=p.read_text(encoding='utf-8') if p.exists() else ''
    if RUN not in old:p.write_text(old+'\n'+s,encoding='utf-8')
protocol=read(P/'EXECUTION_PROTOCOL.json');c=read(R/'out/CHECK.json');rv=read(R/'out/REVIEW_A005_CHECK.json');pilot=read(R/'out/PILOT.json');lean=read(R/'out/LEAN.json')
assert c['status']==rv['status']=='PASS'
assert c['helper_sha256']==sha(R/'code/check_reset.py')==read(R/'out/FROZEN_SPEC.json')['helper_sha256']
assert sha(R/'code/review_character.py')==read(R/'out/FROZEN_REVIEW.json')['helper_sha256']
assert c['physical_blocks']==1844 and c['complete_adaptive_policies']==3110
total=c['assertions']+rv['assertions']
sources=[P/'EXECUTION_PROTOCOL.json',TEAM/'BOARD.md',TEAM/'claude/B11/STREAM_NOTES.md',TEAM/'claude/B11/runs/20261011T230100Z-claude-B11-block-descent-recentring/CLAIMS.json']
ps=[('A051','20261021T193146Z-account03-A051-near-extremizer-definition','AFFINE_SELECTION.md'),('A052','20261021T222218Z-account03-A052-critical-source-structure','PATH_CODE_PROOF.md'),('A055','20261022T233657Z-account03-A055-extremal-obstruction-referee','PROOF.md'),('A005','20261022T231421Z-account03-A005-noncircular-endpoint-referee','DERIVATION.md'),('A002','20261021T210845Z-account03-A002-hardness-preserving-transformations','ADMISSION_PROOF.md')]
for agent,run,proof in ps:
    for fn in ['REPORT.md','CLAIMS.json',proof]:
        p=TEAM/'agents'/agent/'runs'/run/fn
        if p.exists():sources.append(p)
save('out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'kind':'local mutable-source observation; report records inspected scope'} for p in sources])
statement=('Let a(g) be the finite minimum influence over invertible affine spectral maps of a finite uniform Boolean sign g. If f is affine-influence minimal, its full child release rho_i=E[I(f_i)-a(f_i)] obeys 0<=rho_i<=sum_{j!=i}min(p_i,p_j), with sharp coefficient1. If I(f)<=a(f)+delta, the upper bound becomes sum_{j!=i}min(p_j,p_i+delta); epsilon-near finite D_K maxima have delta<=epsilon/K for K>0. For any nonempty physical A define rho_A=E[I(child)-a(child)], S_Astar=E[K a(child)-H(child)], D=H-KI, and L_A=H-EH(child). Then S_A=S_Astar+K rho_A and D+S_Astar=L_A-K(I_A+rho_A). For k in1..n, M=binom(n,k), t=binom(n-1,k-1), T_k=tH-sum_{|A|=k}H(S_A|S_Ac)>=0: T_k+(M-t)D+sum S_Astar+K sum rho_A=sum J_A<=2tI/ln2. On a least-essential-dimensional positive K-violation all S_Astar>=0, giving K sum rho_A+(M-t)D<=2tI/ln2. For every finite adaptive restriction tree followed by branch-dependent entropy-preserving nonincreasing-influence affine resets, sum w(query_I+reset_release)=I(root)-E I(leaves) and sum w L=H(root)-E H(leaves), so each reset is spent once and complete terminal deficits are retained. No uniformly paid pair/tree is selected.')
claim={'claim_id':'A051-FULL-AFFINE-CHILD-RELEASE-BUDGET','version':1,'exact_statement':statement,'hypotheses':['Finite uniform Boolean signs, normalized real Walsh coefficients, entropy bits','Finite affine orbit contains identity; all child entropies and original branch reaches retained','Local bound requires affine influence minimality, or explicitly I-a<=delta for its tolerance form','Critical budget requires nonviolation of EVERY smaller-dimensional Boolean function, not only unoptimized physical children; K>0','Tree resets have nonincreasing influence in each actual current chart; no global common chart assumed'],'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A051'],'proof_source':str(R/'RESET_BUDGET.md'),'proof_dependencies':['A051-AFFINE-MINIMUM-BASIS-CRITICAL-REDUCTION@1','CLAUDE-B11-R1@1 (only J_A<=2I_A/ln2 is needed)','Elementary physical restriction, conditional entropy chain and finite tree telescopes'],'review_records':[],'status':'AUTHOR_PROOF_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A052','A055','A005','A090','A094']}
save('CLAIMS.json',[claim])
save('out/REVIEW_RECORDS.json',[{'claim_id':'A005-CONDITIONAL-CHARACTER-BANK-VACUITY','version':1,'source_statement_sha256':'6931a97d55b81ba8a0cc8b02940a9457625f1118621973abf86ab9902ec593d2','reviewer':'A051','scope':'DERIVATION Sections1--3 only: conditional release, SAME-bank identity, critical high-K character vacuity','verdict':'HOLDS_SCOPED','reconstruction':'REVIEW_A005.md','exact_check':'out/REVIEW_A005_CHECK.json','repair_contributed':False,'exclusions':'Section5 rare activation, N11 root, and source finite census not adopted'}])
next_action='A052/A055 derive a lower bound on one ORIGINAL proper-pair affine child release that pays L_A-K I_A, using signed Boolean rows, SAME unused S_Astar, mixed T and both complete terminals; A005/A090/A094 review budgets and reset ownership.'
progress={'protocol_revision':protocol['revision'],'run_id':RUN,'stream':'B11','packet_id':'A051','gap_id':'G-R-SELECT','attempt_id':'A051-stage8-full-affine-release-budget','method':'Directional physical four-cycle bound, parity-basis rank counting, all-block entropy budget and adaptive affine-reset energy telescope','mathematical_delta':'Sharp singleton full-affine release bound with epsilon/K tolerance; all-k critical release budgets; exact same-owner adaptive reset telescope and point2 price4-to2 example; independent scoped acceptance of A005 Sections1--3. No universal constant improvement.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'NARROW_BUDGET_PROOF_AND_EXACT_CERTIFICATE_PENDING_REVIEW; PAID_PAIR_SELECTION_AND_FEI_OPEN','claim_versions_used':['A051-AFFINE-MINIMUM-BASIS-CRITICAL-REDUCTION@1','CLAUDE-B11-R1@1','A005-CONDITIONAL-CHARACTER-BANK-VACUITY@1 Sections1--3 scoped acceptance; not whole-bundle acceptance'],'claims_created_or_changed':[claim['claim_id']+'@1'],'source_artifacts':['RESET_BUDGET.md','REVIEW_A005.md','out/CHECK.json','out/REVIEW_A005_CHECK.json','out/LEAN.json','out/SOURCE_RECEIPTS.json'],'next_consumers':['A052','A055','A005','A090','A094'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['No lower release bound or uniformly paid physical pair has been obtained','Independent review of new theorem and supervisor remote/mirror adoption remain pending'],'packet_ids':['A051']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
lean_status=lean.get('status',lean.get('result',{}).get('status','UNVERIFIED'))
report=f'''# exact target, quantifiers, hypotheses and units

A051/B11 stage8, {RUN}. Uniform finite Boolean signs; Fourier entropy in
bits; fixed K>0 for the critical and epsilon/K statements. The target is
to quantify FULL affine optimization of actual physical children without
renewing their original influence account. Prove the local perturbation,
near-extremal and all-block budgets before assuming such resets pay a
selected pair. Full FEI remains OPEN. The owner deadline23October2026
14:49UTC governs over the older protocol endpoint.

# sources actually read, revisions and theorem locators

BOARD23October00:21UTC, unchanged B11 STREAM_NOTESv2, own STATUS and prior
AFFINE_SELECTION consumed. Protocol2026-10-11-execution-v2 read fully.
New substantive sources: A052 PATH_CODE_PROOF Sections1--5 and REPORT;
A055 PROOF Sections1--7 and REPORT; A005 DERIVATION Sections1--5 and REPORT;
A002 latest REPORT. B11 lead CLAUDE-B11-R1@1 statement/dependencies and
current A005 claim bundle inspected. Earlier campaign and four manuscript
baseline reads are not presented as fresh audits or new premises. One
two-wording read-only math recall supplied background only. Paths/current
source hashes are saved in out/SOURCE_RECEIPTS.json; mutable source hashes
are observations, not immutable revisions. Wake reported degraded personal
context: owner-model/state notes86.9/71.5hours old; current instructions
and research files govern. No external novelty or literature claim is used.

The lead's old read-once composition target was closed in earlier A051
stages. New physical-child objections take dispatch priority. A052's
independent acceptance of the preceding A051 affine reduction is consumed
at its stated scope; this is not a new self-acceptance.

# complete derivation or exact first unsupported line

RESET_BUDGET Sections1--5 contain the full proof. Physical four-cycle
counting bounds every child directional influence change by the queried
p_i. The affine parity-basis criterion and threshold rank counting give
rho_i<=sum_(j!=i)min(p_i,p_j), sharp at point2. For I-a<=delta the bound
is sum min(p_j,p_i+delta), so epsilon-near finite D_K maxima have explicit
epsilon/K error. Dummy parity disproves the exact bound without parent
affine minimality. No unspecified optimizer or near-extremizer is used.

Actual optimized child banks satisfy S_A=S_Astar+K rho_A and
D+S_Astar=L_A-K(I_A+rho_A), retaining full original terminal entropies.
Smaller-dimensional nonviolation makes S_Astar nonnegative at a genuine
minimal witness. Conditional entropy chain counting plus the established
channel log-Sobolev bound gives, for t=binom(n-1,k-1), M=binom(n,k),
K sum_{{|A|=k}}rho_A+(M-t)D<=2tI/ln2. The proof retains the exact
nonnegative entropy remainder and every optimized terminal reserve.

Adaptive branch-dependent affine resets have an exact single-owner
telescope: sum reach*(queried influence+reset release)=Iroot-EIleaf.
Entropy telescopes with the original complete children because each
reset preserves it. Previously booked release is not replenished at a
later chart. Point2 exhibits actual payment: its prescribed singleton
price falls from4 to2 when its literal child is centered to a constant,
using the SAME root influence1. No general selected-pair rule follows.

FIRST UNSUPPORTED LINE: obtain a LOWER bound on one actual proper pair's
release sufficient for its signed bill L_A-K I_A, from the SAME unused
S_Astar bank, including mixed T and both full terminals. Current results
are upper budgets and conservation identities. A052/A055 hard wrappers
fail child eligibility and cannot be substituted for a critical source.

# executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC.json and FROZEN_REVIEW.json precede jobs. Commands
from A051: python -X utf8 runs/{RUN}/code/check_reset.py --pilot, then
without --pilot; code/review_character.py; code/run_lean.py. Main v1
passed; v2 adds the explicit near-affine tolerance, with spec refreshed,
pilot and full rerun before adoption. Only final v2 full totals are counted.

Final pilot:22 tables,{pilot['assertions']} assertions PASS in
{pilot['runtime_seconds']:.6f}s. Final full:278 tables n0..3,1844 physical
blocks,6280 directional fibers,all168 n3 independent parity bases,
64 actual finite-critical block budgets and3110 complete adaptive
policies; {c['assertions']} exact assertions PASS in
{c['runtime_seconds']:.6f}s. Affine-minimal roots total56. Tolerance is
tested at each root's exact affine-orbit influence gap, not represented
as a full global near-D census. The point2 payment, physical-only failure,
dummy-parity missing-hypothesis failure and deliberate double booking
are distinct positive/negative controls.

Arithmetic: integer Walsh, independent physical translations and full
finite basis enumeration, Fraction, exact prime-log entropy vectors and
32-term rational atanh tails for signs. Zero marginal, zero rank, constants,
ties, k=n, and all original reaches are covered. No floating proof decision.
Separate A005 replay uses direct characters/physical edges on278 roots
and1608 children: {rv['assertions']} exact assertions PASS in
{rv['runtime_seconds']:.6f}s. Total final full assertions {total}, excluding
the pilot and earlier v1 pass; this is the new stage's targeted domain,
separate from the prior697326 affine-transform checks.

Python jobs estimate40--90MB, peak unmeasured,55s caps, no dimension
escalation/GPU/detached work. Start compute snapshot:status ok, about2GB
available RAM, CPU97.4percent, disk22.4GB; no existing work changed.
Fresh memok and compiler admission evidence is in out/LEAN_ADMISSION.json
and out/LEAN.json. Lean outcome: {lean_status}. Bank.lean formalizes only
the scalar conservation identity; no whole-Fourier-theorem formal
certification is claimed. Rung: author-checked proof/exact finite
certificate, new theorem pending independent review.

# proof dependencies and changed downstream conclusions

The parity-basis argument uses the independently reviewed
A051-AFFINE-MINIMUM-BASIS-CRITICAL-REDUCTION@1. Channel inequality uses
CLAUDE-B11-R1@1 (finite-cube Gross log-Sobolev); the displayed weaker
J_A<=2I_A/ln2 suffices. Other steps are derived from physical restrictions,
entropy chains and finite telescopes. REVIEW_A005 independently accepts
A005-CONDITIONAL-CHARACTER-BANK-VACUITY@1 DERIVATION Sections1--3 without
repair; source activation/N11 examples and source census remain outside
this acceptance. No source theorem is refuted or broad full-FEI candidate
opened. Full-affine release is now a quantified constrained resource
rather than an assumed new bank. No universal constant improves.

# one next mathematical action and independent reviewer

{next_action}
The next bound must be a lower funding/selection statement; another
qualitative affine or weak-root admission is already FEI-hard by the
consumed A052/A055/A002 results. Handoffs are source-bound local records;
no messages sent to peers or others.

# actual persistence receipts or precise save blocker

All four protocol files, proof, independent scoped review, frozen specs,
code and exact outputs saved under A051 only. Exact schema field sets,
byte-identical PROGRESS/PACKET_DELTA, required report headings, statement
hash,20MB limit and two-line STATUS checked. WORKLOG/LEARNED appended.
out/PERSISTENCE_RECEIPT.json hashes artifacts and rolling files. Git was
not run under the worker's standing ownership rules. Supervisor copying,
registry adoption, brain ingestion, remote mirrors and independent
acceptance of this new theorem remain unverified. No local save blocker.

## Universal bridge

C019 stopping-tree payment through B11 finite critical selection: this
stage quantifies full affine child release, its epsilon/K stability and
all-k critical budget, and proves an adaptive same-owner telescope;
point2's prescribed query is paid at2 instead of4 without increasing
root influence. The universal constant gains zero. What remains is the
lower funding bound selecting an actual original pair with mixed T and
complete terminal debt inside SAME unused S_Astar. NEXT targets precisely
that missing direction; another upper budget or isolated structural class
cannot pay the universal signed pair bill.
'''
save('REPORT.md',report)
(A/'STATUS.md').write_text(f'STATE: A051 stage8 saved: full-affine child release bound with epsilon/K tolerance, all-k critical budgets and same-owner adaptive reset telescope;{total} exact checks PASS; A005 Sections1--3 scoped HOLDS; FEI OPEN.\nNEXT: '+next_action+'\n',encoding='utf-8')
append(A/'WORKLOG.md',f'2026-10-23 {RUN}: Consumed A052 path/A055 weak-I arbitrary-core obstructions. Proved directional full-affine release bound, near-finite-extremality tolerance, all-block critical budget and adaptive conservation. Final v2 {c["assertions"]} checks, separate A005 {rv["assertions"]} checks PASS;3110 complete policies. Lean {lean_status}; full FEI/pair lower funding open.\n')
append(A/'LEARNED.md',f'''2026-10-23 {RUN}
- At an affine-influence-minimal parent, full child release rho_i<=sum_(j!=i)min(p_i,p_j), with constant1 sharp at point2. Directional child probability differs from its root by at most p_i; threshold-rank counting transfers this to every child parity basis. Dummy queried coordinate on padded parity disproves the bound without affine minimality.
- Near version: if I-a<=delta, rho_i<=sum min(p_j,p_i+delta); finite epsilon-near D_K maxima have delta<=epsilon/K, K>0. No unquantified stationarity or K0 division.
- Exact all-block bank: T_k+(M-t)D+sum S_Astar+K sum rho_A=sum J_A<=2tI/ln2. At a genuine minimal K-violator all optimized child reserves nonnegative. Thus full affine release has a bounded total budget, not a fresh second influence account. T_k=tH-sum H(S_A|S_Ac)>=0 by a fixed chain order.
- Any finite adaptive restriction/reset tree spends sum reach*(actual queried influence+booked release)=Iroot-EIleaf, with each branch in its actual changed chart. Complete entropy and signed leaf deficits remain. Reusing an old reset fails conservation; point2 singleton price4-to2 is a real SAME-I example. This does not select a universal paid pair.
- A005 Sections1--3 independently HOLD without repair; high-K character release is zero at K>=2+3/ln2. Source rare activation/N11 and large census are outside this acceptance. New full-affine theorem needs independent review; first unpaid line is a LOWER bound funding one original signed pair with mixed T and both terminals.
''')
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for h in protocol['required_per_run']['report_fields']:assert '# '+h in report
for p in R.rglob('*'):
    if p.is_file():assert p.stat().st_size<20_000_000
save('out/HANDOFF_CHECK.json',{'status':'PASS','protocol_exact_fields':True,'statement_sha256':claim['statement_sha256'],'byte_identical_compatibility':True,'required_headings':True,'status_two_lines':True,'all_below20MB':True,'full_fei':'OPEN','new_theorem_independent_review':'PENDING'})
save('out/PERSISTENCE_RECEIPT.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'artifacts':[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(R.rglob('*')) if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json' and '__pycache__' not in p.parts],'rolling_files':[{'path':str(A/n),'sha256':sha(A/n)} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']],'remote_copy':'UNVERIFIED'})
print(json.dumps({'status':'PASS','run':RUN,'final_full_assertions':total,'policies':c['complete_adaptive_policies'],'lean_status':lean_status,'claim_sha256':claim['statement_sha256']}))
