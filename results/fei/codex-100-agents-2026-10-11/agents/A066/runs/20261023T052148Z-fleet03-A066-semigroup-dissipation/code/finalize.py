from pathlib import Path
from datetime import datetime,timezone
import json,hashlib

run=Path(__file__).resolve().parents[1];agent=run.parents[1]
def write(p,s):p.write_text(s,encoding='utf-8',newline='\n')
def dump(p,s):write(p,json.dumps(s,indent=2,ensure_ascii=True)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
full=json.loads((run/'out/CHECK_FULL.json').read_text(encoding='utf-8'))
witness=json.loads((run/'out/WITNESS.json').read_text(encoding='utf-8'))
pilot=json.loads((run/'out/CHECK_PILOT.json').read_text(encoding='utf-8'))
spec=json.loads((run/'out/FROZEN_SPEC.json').read_text(encoding='utf-8'))
assert full['status']==pilot['status']==witness['status']=='PASS'
assert spec['helper_sha256']==sha(run/'code/check.py')
assert len(full['unpaid_rows'])==full['admitted_forests_unpaid']==6

proof=r'''# The next genuine seed query: an exact inherited-bank obstruction

Bits for H, CE, KL, JS; natural logs for b and the heat area K. This continues A066-NONFLAT-DATA-RELEASE-AND-SOURCE-PAYMENT v2. It refutes a proposed literal-reference continuation of that admission, not v2 itself, FEI, or existence of a different paid query/calibration policy.

## 1. The correct signed payment identity

For ANY Boolean sign g and a physical singleton i, write a_T=ghat(T), c_T=ghat(T+i). Let p be the full Fourier probability and p_+,p_- the actual full child probabilities. Fix a complete normalized reference Q of finite CE. KEEP both physical children, including dummies. Set

    pbar(T)=a_T^2+c_T^2=(p_+(T)+p_-(T))/2,
    Qbar(T)=Q(T)+Q(T+i).                                      (1)

Both children inherit the SAME literal full Qbar. Positive child mass implies positive Qbar, so CE stays finite even if Q has zeros off actual support. Define

    B=H(p)-H(pbar) >=0,
    J=H(pbar)-E_s H(p_s) >=0,
    D=sum_T pbar(T) KL(p(v|T)||Q(v|T)) >=0,
    C=CE(p,Q)-E_s CE(p_s,Qbar).

The entropy and CE chain rules give EXACTLY

    DeltaH=B+J,  C=B+D,  DeltaH-C=J-D.                       (2)

Indeed C=sum_(T,v) p(T,v)log2[Qbar(T)/Q(T,v)], with zero actual terms omitted. It is nonnegative. But CE decreasing does NOT imply it pays the true entropy decrement: J, not -J, is added to erasure. The failed draft used B-J; its first pilot rejected that identity on the genuine two-bit negative AND. Rejected draft and helper are preserved in out/DRAFT_v1_REJECTED.md, code/check_v1_failed.py and out/PILOT_v1_FAILURE.json. They are not proof dependencies. Formula(2) is reconstructed here independently of A014's CE-only monotonicity. No novelty is claimed for erasure/JS chain rules or for reference projection.

For a finite adaptive forest, with ORIGINAL reaches w_h, (2) telescopes to

    sum_h w_h Delta_h H + E_leaf CE - CE_root
       =E_leaf KL - KL_root =sum_h w_h(J_h-D_h).              (3)

Every entropy decrement is nonnegative since B,J>=0. Both full terminal CE/KL bills remain. Old debits cannot be undone. No negative later entropy bill is used to refund a previous spend. Nonnegative conditional KL D is an actual reference-code refund and cannot also be spent a second time elsewhere.

## 2. Exact v2-admitted source with no initial off-support mass

Take d=1, b(x)=(-1)^x, delta=1/2. Use precisely the v2 attachment, ordered as (j,z,x):

    F=(1,-1,-1,-1,-1,-1,-1,-1),
    F_0=(1,-1,-1,-1) on (z,x), F_1=(-1,-1,-1,-1).

Its spectra are

    p_F=(9/16,1/16,1/16,1/16,1/16,1/16,1/16,1/16),
    p_0=(1/4,1/4,1/4,1/4), p_1=(1,0,0,0).

Choose the ORIGINAL finite-cost complete references, before the first debit,

    Q_0=(1/10,2/5,1/10,2/5), Q_1=(1,0,0,0).                 (4)

These references have EXACTLY the actual spectral supports. In particular Q_1 does not carry unused mass on its physical dummy z or x. A cleanup of initial occupied ghosts cannot supply the missing margin in this example. Complete means a normalized law on the complete physical spectrum, positive wherever actual p is positive; strict positivity on zero-actual atoms is unnecessary and was not a v2 hypothesis.

Physical edge counts give Ibar=1/2, e=Inf_j(F)=1/4, I(F)=3/4, R=(d+1)e=1/2. Fix ORIGINAL quota A=4 Ibar=2 and old debit tau=Ibar/4=1/8. Do not renew them after j. The opening complete terminal cost is

    E CE(F_s,Q_s)=(1/2)log2 5.

The root entropy is H(F)=4-(9/8)log2 3, so Delta_j H=3-(9/8)log2 3 <=5/4=5e. Thus the ACTUAL v2 extra spend L=max(Delta_j H-5e,0) is zero. The same original source and residual are

    U=15/8-(1/2)log2 5 =7/8-(1/2)log2(5/4),
    S=U-R-L=3/8-(1/2)log2(5/4).                             (5)

The v2 admission is satisfied:

    U>=3R/2-e/4=11/16,

equivalent to log2(5/4)<=3/8, certified by 5^8<2^19 (390625<524288). L=0 is certified by 3^9>2^14. Also S>=0 follows from admission. Therefore this is an actually admitted physical state with both full references and an old prior debit, not a freely rescaled local capacity.

## 3. Query the actual seed x next, on BOTH physical j branches

The F_0 children are the z literal and the constant -1. Their full spectra are (0,1) and (1,0). The F_1 children remain constants. Literal projection of (4) gives

    Qbar_0=(1/5,4/5), Qbar_1=(1,0).

For F_0, B=1,J=1,D=0,C=1,DeltaH=2. Conditional D=0 because both Q_0 and p_0 have uniform conditional x occupancy at each residual z atom. For F_1 every one of these costs is zero. At ORIGINAL reach1/2 for each j child,

    E Delta_x H=1, E C=1/2, E(J-D)=1/2.

The inherited old reserve has r_0=d delta=1/2 and r_1=0; the seed query removes it, releasing E r=1/4=R-e. The query therefore needs an additional1/4 from the SAME already-reduced S. But

    S<1/4 <=> log2(5/4)>1/4 <=>5^4>2^9 (625>512).           (6)

Thus the exact v2 admission alone does NOT guarantee this next prescribed data payment under unchanged FULL-reference projection. This is not merely failure of a conservative booking. Even if ALL unused slack of the first j charge is recovered and S is spent down to zero, the mandatory whole ledger has

    Delta_j H+E Delta_x H+E terminal CE+tau -(A+4e)
      =[5+4log2 5-9log2 3]/8
      =(1/8)log2(20000/19683)>0.                             (7)

Here E terminal CE=(1/2)log2(5/2), and the final old reserve is zero. Formula(7) has the exact rational sign20000>19683. No decimal sign or interval precision is needed. It retains both old terminal bills, the ORIGINAL quota, the old debit, actual L and the dummy z. It is a counterexample to the stated CONTINUATION rule, not to Boolean FEI: H(F)<4I(F), and no claim about every possible next query is made.

## 4. Paid empty calibration repairs this particular witness

Let u_s=p_s(empty), q=Qbar(empty). Preserve the old conditional nonempty profile but set

    Qcal_s(empty)=u_s,
    Qcal_s(T nonempty)=(1-u_s)Qbar(T)/(1-q).

Zero-sector endpoints use the corresponding point mass. Finite CE ensures occupied sectors have positive reference mass. The EXACT release from calibration is

    V=E_s KL(Ber(u_s)||Ber(q)) >=0,
    Ccal=C+V,  DeltaH-Ccal=J-D-V.                            (8)

This is a supplied-reference categorical identity, not a free replacement of the conditional nonempty profile. It agrees with the distinction in A014 v6: its calibration transports FULL CE, while a true entropy bill still needs its signed JS comparison. The two principles must not be conflated.

In the witness each remaining physical cube has one bit z. Its nonempty sector has just one atom. Calibration therefore makes every terminal reference its actual point-mass spectrum, without changing any conditional nonempty profile. Terminal CE becomes zero, and the original rate-four ledger, including old tau, is paid. It releases E terminal CE=(1/2)log2(5/2)>0. The witness does NOT refute A014, actual-occupancy calibration, a carefully selected continuation, or arbitrary-source FEI. Its role is to prohibit claiming that literal CE monotonicity alone closes the true A066 debit.

## 5. Semigroup endpoints, boundary, and the residual charge

For every finite Boolean g, write p=ghat^2, q_t(S)=p(S)exp(-2t|S|),

    J_g(t)=sum_nonempty |S|q_t(S)ln(1/p(S)),
    K(g)=integral_0^infinity J_g(t)dt,
    b(g)=p(empty)ln(1/p(empty)).

The corrected heat identity is2K=ln2 H-b. The raw entropy derivative requires subtraction of2t sum|S|q_t. At small times J_g(t)<=J_g(0); at large times J_g(t)<=exp(-2t)J_g(0). Both endpoints are integrable for each finite g. A universal2K<=C I would imply FEI since b<=Var<=I. The pointwise no-integrable-envelope obstruction from earlier stages is unchanged; no function supremum is interchanged with time integration.

There is also a uniform absolute SINGLETON boundary payment, not inferred in v2. Let m=E g and phi(m)=-m^2 ln(m^2), phi(0)=0. Its continuously extended derivative is -2m(ln(m^2)+1). For |m|=exp(-r), r>=0, exp(-r)|2r-1|<=1: on r<=1/2 it is at most1, and on r>=1/2 its maximum is2exp(-3/2)<1. Hence |phi'|<=2. Writing child means m+a,m-a, Booleanity gives |a|=|E(g_+-g_-)|/2<=e_i=Pr(g_+!=g_-). Therefore

    |Delta_i b|<=2|a|<=2e_i (natural-log units).              (9)

Its sign may be either. Over any finite adaptive tree, sum reach*|Delta b|<=2 sum reach*e_i<=2I(g). This uses the physical Boolean mismatch bound, stronger than only a^2<=e_i. It pays the boundary, not the nonempty spectral information debt.

For the COMPLETE heat reference Psi(g,Q)=ln2 CE(g,Q)-b(g)=2K+ln2 KL(p||Q), (2) and (8) give

    2Delta K+E_s Psi(g_s,Qbar)-Psi(g,Q)=ln2*(J-D),
    2Delta K+E_s Psi(g_s,Qcal_s)-Psi(g,Q)=ln2*(J-D-V).         (10)

The signed boundary cancels EXACTLY when retained in the terminals. These expressions are not asserted nonpositive. The earlier false draft had the wrong sign on J in precisely this identity. A querywise physical bound on the remaining JS exists, but using it on top of an already assigned A would require a legitimate UNUSED influence/source owner, not a second use of the same quota.

## 6. Correct bank test and first unsupported line

At an actual next frontier, denote its expected old-reserve release by dr>=0. The signed net demand on the same remaining source is E(J-D-V)-dr after paid categorical calibration (set V=0 for literal references). Its positive part must be covered by the actual remaining S, with earlier tau/L permanently booked. This is an exact eligibility test, not a proof that S supplies it. If it passes, the source, full references, old bills and same remaining reserve telescope correctly. The three-bit witness proves that the previous admission is insufficient if V is left unpriced/omitted.

FIRST UNSUPPORTED UNIVERSAL LINE: choose and pay a genuine post-calibration conditional-NONEMPTY profile/data continuation so that the positive signed residual E(J-D-V)-dr fits in the SAME diminished original source after all old debits and both terminal CE/KL bills. Alternatively supply a universally cheap opening reference and stronger valid source invariant. Neither a new reference nor a fresh local K I is a permitted substitute. Conditional nonempty profile replacement adds its actual CE conversion separately; the simple categorical repair above does not pay arbitrary changes of that profile.

Rung: complete analytic author derivation and exact rational certificates; independent A070/A088/A094 review pending. No full Lean certificate, universal source payment or full FEI proof is claimed.
'''
write(run/'DERIVATION.md',proof)

statement=('Retain A066-NONFLAT-DATA-RELEASE-AND-SOURCE-PAYMENT v2 at its stated scope. Its admission U>=3R/2-e/4 does NOT by itself pay every prescribed subsequent seed query under LITERAL full-reference pushforward. An exact counterexample is d=1,b(x)=(-1)^x,F=(1,-1,-1,-1,-1,-1,-1,-1),Q0=(1/10,2/5,1/10,2/5),Q1=(1,0,0,0),ORIGINAL A=2,tau=1/8,e=1/4,R=1/2,L=0. Both references have exactly the actual supports. Querying x on BOTH actual j children has mean JS=1/2, conditional KL=0,old-reserve release1/4; it needs1/4 from S=3/8-(1/2)log2(5/4)<1/4 although opening admission holds. Even after using every opening slack, the complete terminal-inclusive ledger exceeds A+4e by log2(20000/19683)/8>0. Empty/nonempty calibration with the original conditional nonempty profile repairs this specific witness and is not refuted. For every Boolean singleton physical query and fixed finite-cost complete Q, literal pushforward has DeltaH-C=JS-Dconditional; after paid categorical calibration the residual is JS-Dconditional-Vcategorical. Signed heat-reference transport has exactly ln2 times that residual. Universally |Delta b_empty|<=2 Inf_i in natural-log units; both semigroup endpoints remain integrable per finite function. No universally cheap source, arbitrary-profile reset payment, selected-coordinate counterexample or FEI conclusion is asserted.')
prior={'claim_id':'A066-NONFLAT-DATA-RELEASE-AND-SOURCE-PAYMENT','version':2,'scope':'Retained opening profile/admission and same physical reserve, analytic author proof and exact checks; independent review pending.'}
claim={'claim_id':prior['claim_id'],'version':3,'exact_statement':statement,'hypotheses':['Finite uniform Boolean cube, same two-control attachment and actual first j query as v2','Explicit rational references with finite full CE; no zeros at occupied actual atoms','Original A,tau and actual L are fixed; both physical branches and full terminal CE/KL retained','Obstruction concerns prescribed seed query with literal full-reference projection; calibration/profile policies are distinct'],'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A066'],'proof_source':str(run/'DERIVATION.md'),'proof_dependencies':[prior],'review_records':[],'status':'ANALYTIC_AUTHOR_PROOF_EXACT_RATIONAL_COUNTEREXAMPLE_REVIEW_PENDING','supersedes':[{'claim_id':prior['claim_id'],'version':2,'scope':'Retains all v2 results, adds exact limitation of admission-only continuation and corrected signed reference/heat identities; no v2 theorem withdrawn.'}],'refutes':[{'claim_id':'A066-STAGE9-DRAFT-UNCHANGED-REFERENCE-ZERO-DEBIT-CONTINUATION','version':1,'scope':'Rejected unpublished draft had wrong entropy/JS sign. Explicit witness also refutes its admission-only extension even allowing unused first-query slack.'}],'first_unproved_line':'Pay a selected post-calibration genuine conditional-nonempty profile/data residual from SAME diminished original bank, retaining old tau/L and both full terminal CE/KL bills; cheap universal source remains unavailable.','next_consumers':['A070','A088','A094','A096','A097','A014']}
dump(run/'CLAIMS.json',[claim])

next_action='After paid empty calibration, expose one genuine seed query with a nontrivial conditional-NONEMPTY spectrum; price JS-D-V and any actual profile conversion from SAME remaining A/tau/L, both full terminals retained. A070/A088/A094 review the exact witness and sign; A014 compare calibrated CE scope.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':run.name,'stream':'B14','packet_id':'A066','gap_id':'C019-C024-INHERITED-DATA-AND-TERMINAL-PAYMENT','attempt_id':'A066-stage9-admission-only-continuation-exact-obstruction','method':'Consume A014 full-CE projection; independently derive true entropy/heat signed transport; try to break admission-only heredity with rational complete references; integer log-power certificate and bounded exhaustive seed histories.','mathematical_delta':'Exact three-bit admitted-root counterexample to literal-full-reference continuation, gap=log2(20000/19683)/8>0; old tau and both terminals retained, no initial off-support reference mass. Paid empty calibration repairs this witness; first unpaid residual is JS-D-V on conditional nonempty profiles. Universal absolute singleton empty-boundary bound2Inf in nats.','deliverable_status':'COMPLETE_LOCALLY_REVIEW_PENDING','mathematical_status':'NARROW_ROUTE_OBSTRUCTION_AND_SIGNED_LEDGER_PROVED_BY_AUTHOR_FULL_FEI_OPEN','claim_versions_used':[prior],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':3}],'source_artifacts':[str(run/'DERIVATION.md'),str(run/'out/WITNESS.json'),str(run/'out/CHECK_FULL.json'),str(run/'out/SOURCE_READS.json')],'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Independent review pending; no universal initial source bound','Post-calibration conditional-nonempty residual/profile conversion unpaid generally','Shared contract cache stale/unresolved: no irreversible/shared mutation undertaken','No remote mirror or supervisor-copy receipt; user forbids git and outside research writes'],'packet_ids':['A066']}
dump(run/'PROGRESS.json',progress);dump(run/'PACKET_DELTA.json',progress)

report=f'''# A066 stage9: admission does not automatically pay the next seed query

## exact target, quantifiers, hypotheses and units

Continue the SAME v2 source after the paid j query; test the next physical seed query, both complete child CE/KL bills, prior tau, actual L and reserve. H/CE/KL/JS are bits, heat K and empty boundary b are nats. Result: a three-bit genuine Boolean witness passes the opening admission but literal-full-reference continuation exceeds the ORIGINAL whole bank by **log2(20000/19683)/8>0**, even using every unused opening slack. Its incoming references have exactly the actual spectral supports. It refutes the proposed continuation, not v2, selected paid policies or FEI. Empty/nonempty calibration repairs this particular witness. Universal singleton |Delta b|<=2Inf in nats is proved separately.

## sources actually read, revisions and theorem locators

The required local protocol/registries, README/status/plan, supplemental campaign documents/sources, current BOARD(2026-10-23 05:15 UTC), B14 lead v2(2026-10-11 23:25 UTC), and rolling A066 state were read. out/SOURCE_READS.json records33 source access/hash receipts. The four supplied paper texts contain cp1252 soft-hyphen bytes: UTF8 decoding failed explicitly; they were then read using explicit cp1252, not silently relabelled as corrupt. No paper theorem is needed for the new derivation. Prior A066 v2 DERIVATION/CLAIMS and LEARNED were read. A014 v6 REPORT/CLAIMS distinguishes full-CE projection/calibration from true entropy payment; this source motivated the test, not an unreviewed theorem imported as a proof. A094 current status/board supplied coordination context. One two-wording read-only math recall returned existing restriction-deficit definitions/quantifier warnings; no recalled card is a proof dependency. No brain writes.

The canonical packet index still says A066 NOT_YET_ADOPTED and carries initial routing: that stale index is not a receipt of current review. The stream lead's old semigroup/class tests were already treated in earlier stages; this is the rolling NEXT, not a repetition of those tests. Broad-candidate cap respected by extending the SAME claim to v3, not opening a new universal candidate.

## complete derivation or exact first unsupported line

DERIVATION.md sections1-6 give the entire signed chain rule, rational witness, whole-bank calculation, categorical repair and heat translation. The critical identity is **DeltaH=B+JS**, whereas the literal reference releases **C=B+Dconditional**. Therefore the unpaid cost is JS-Dconditional. After retaining the actual empty calibration refund V, it becomes JS-Dconditional-V. A draft used the false B-JS sign; the first pilot failed, the rejected draft/helper and exact failure are preserved, and no result from that failed draft is asserted.

Witness: d1, b=(-1)^x; Q0=(1/10,2/5,1/10,2/5), Q1=empty point mass; original A2,tau1/8,e1/4,R1/2,L0. Admission is 5^8<2^19; positive next-query source shortfall follows from5^4>2^9. Allowing all first-query slack still leaves the whole-ledger excess because20000>19683. Initial unused ghost mass is absent. Empty/nonempty calibration yields terminal CE0 and repairs the witness without changing its one-atom conditional nonempty sector. This does not justify replacing a genuinely nonempty profile for free.

First unsupported universal line: choose and pay a post-calibration genuine conditional-NONEMPTY query/profile residual from the SAME diminished original account after tau/L and both full terminals. Initial cheap references remain unpaid. The generic bank test alone is not a theorem that the bank has money.

## executed validation with domain, arithmetic, commands and outputs

The frozen specification precedes each searched helper version. Pilot: all b(0)=1,d0..2,11 seeds,72 first seed-query cases,652 adaptive policy nodes,725 total nodes; {pilot['exact_assertions']} exact assertions PASS in{pilot['seconds']:.6f}s. Full: all b(0)=1,d0..3,139 seeds,1608 first seed-query cases,18764 adaptive policy nodes,20373 total nodes; **{full['exact_assertions']} exact assertions PASS in{full['seconds']:.6f}s**. Domain is smaller than stage8's163 seeds because this stage tests full histories rather than the root profile; no old count changed. Two original refs (actual,half-uniform), original rates4/8 and tau=Ibar/4 give556 source cases:550 admitted,6 rejected. Of1650 tested forests at admitted roots,1644 fit and6 leave an unpaid whole-ledger bill; all six case-level interval rows are in out/CHECK_FULL.json. They are classified as failures of payment, not treated as successful cases.

Arithmetic: independently coded direct-character Walsh sums, rational physical edges, complete-reference marginal identities,28-term range-reduced atanh logs with explicit positive tail bound, outward2^-60 exports. Checks retain signed empty boundary, nonempty heat area, full terminal costs, old reserve, JS and conditional KL. Main checker also rejects an unpriced zero-influence prescribed-reset control. Zero-margin identities use exact marginal equalities/interval overlap with the derived analytic chain rules; no floating tolerance proves a sign.

Independent witness: code/witness.py uses integer FWHT, direct edges and exact log-power comparisons with cleared rational exponents; **{witness['exact_assertions']} assertions PASS in{witness['seconds']:.6f}s**, no log approximations. It verifies admission, L0, no initial off-support mass, next physical query, strict whole-ledger excess and paid calibration repair. Its canonical sign certificate is20000/19683>1. Independent implementation is author-side reproduction, not independent-agent acceptance.

Commands: `python -X utf8 code/check.py pilot`, `python -X utf8 code/check.py full`, `python -X utf8 code/witness.py` from the run, or their absolute-path equivalents from A066. Corrected v2 full check passed once; output-only localization reran exactly the same frozen inputs to export the six already detected failures. A localization-only v3 syntax error executed no cases and is archived; v4 compiled and completed. Counts are NOT added across pilots or reruns. Helpers/spec hashes and old failed versions are retained. Memory estimate200MB, actual peak unmeasured; one job at a time, max runtime55s, largest truth table5 bits. No >300MB job, GPU, detached work or compiler was launched. Shared memory pressure was observed; the compute snapshot is saved. No work was stopped to free resources.

## proof dependencies and changed downstream conclusions

A066 opening v2 remains an explicit pending-review dependency at its named narrow scope. All new identities and the witness are derived from definitions. A014 v6 is a source/coordination comparison, not an imported proof dependency: its claimed CE monotonicity is not asserted to pay DeltaH. No previously accepted claim is refuted here. The only named refuted object is this stage's unpublished sign-wrong continuation draft. No broad new candidate was opened. Full FEI remains OPEN. Bound2Inf pays the absolute empty boundary but does not pay the conditional nonempty residual or construct a universal integrated heat envelope.

## one next mathematical action and independent reviewer

{next_action} These are requested consumers, not messages sent, reviews accepted or downstream adoption claimed. The fixed whole-quota test of a tiny cube is a route obstruction, not a new FEI class result.

## actual persistence receipts or precise save blocker

All four protocol files, derivation, frozen versions, exact helpers and outputs are saved inside the assigned A066 run. out/RECEIPTS.json verifies exact protocol fields, statement hash, identical progress/delta, sizes and hashes. STATUS has two lines; WORKLOG and LEARNED are current. No git/mail/shared-tree/other-agent/trading/brain mutation or deletion. Supervisor copying, GitHub/mirror persistence and independent review remain unverified. Stale/locked shared contract caches prevented no reversible local research and were not bypassed for an irreversible action. Brain self-care remains degraded/unverified: owner-model and state-of-mind notes are stale; they were not relied on for mathematics or current preferences.

## Universal bridge

C019 stopping-tree payment and C024 history transfer gain an exact LIMITATION of the previous source admission: even a genuine next seed query with no initial off-support mass can overspend the SAME original whole bank by log2(20000/19683)/8 under literal full-reference transport. Universal constant improvement is zero. Paid empty calibration repairs this narrow witness, and heat boundary cancellation leaves the precise signed nonempty residual JS-D-V. NEXT attacks that residual after calibration with old tau/L and full terminals retained, because merely extending CE-monotone histories would repeat a false entropy payment; paying an actually changed nonempty profile is the shortest identified route from this corrected obstruction to a universal bridge.
'''
write(run/'REPORT.md',report)

timestamp=datetime.now(timezone.utc).isoformat()
status=f'STATE: A066 stage9 saved: exact admitted three-bit next-DATA literal-reference failure, gap log2(20000/19683)/8; calibration repairs witness; {full["exact_assertions"]}+{witness["exact_assertions"]} exact checks PASS; review pending; FEI OPEN.\nNEXT: Pay post-calibration JS-D-V for a genuine conditional-NONEMPTY data/profile change from SAME diminished A,tau,L; both full terminals retained; A070/A088/A094 review, A014 compare CE scope.\n'
write(agent/'STATUS.md',status)
entry=f'\n{timestamp} {run.name}: stage9 v3. Pilot rejected draft sign DeltaH=B-JS; correct B+JS leaves JS-D. Exact no-off-support three-bit witness passes v2 admission, but next seed query overspends whole original account by log2(20000/19683)/8>0, even with opening slack. Same conditional nonempty profile plus empty calibration repairs it. Corrected full {full["exact_assertions"]} assertions,6 classified unpaid cuts; independent integer log-power witness {witness["exact_assertions"]} assertions. Review/full FEI open; no compiler/heavy job. NEXT: post-calibration nonempty residual from SAME diminished source.\n'
learn=f'\n{timestamp} {run.name}: For literal full-reference projection, DeltaH=B+JS, C=B+Dconditional, so TRUE residual=JS-D, not -JS-D. Paid actual-empty calibration subtracts Vcategorical. The admitted d1 seed b=(-1)^x with Q0=(1/10,2/5,1/10,2/5),Q1=empty,A2,tau1/8,R1/2,L0 fails the next BOTH-branch seed query: whole excess=log2(20000/19683)/8>0. Opening refs have exactly actual supports; no initial occupied-ghost cleanup explains it. Calibrating the one-bit terminals repairs this witness without changing nonempty profile. Do not promote CE monotonicity to true entropy payment. Universal |Delta b_empty|<=2Inf_i nats follows from phi(m)=-m^2 ln m^2 being2-Lipschitz and Boolean |mean-difference|/2<=physical mismatch. Heat-reference residual retains exactly ln2*(JS-D-V); boundary payment does not close nonempty information debt.\n'
for name,s in [('WORKLOG.md',entry),('LEARNED.md',learn)]:
    p=agent/name;old=p.read_text(encoding='utf-8') if p.exists() else ''
    if run.name not in old:write(p,old+s)
write(run/'CHECKPOINT.md','STATE: Stage9 v3 complete locally; exact source-admission continuation obstruction and calibration repair saved; full FEI OPEN.\nNEXT: '+next_action+'\n')

protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
required=protocol['required_per_run']
assert set(claim)==set(required['claim_fields'])
pf={x.split(' (')[0] for x in required['progress_fields']}
assert set(progress)==pf
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert claim['statement_sha256']==hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()
assert all('## '+h in report for h in required['report_fields'])
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
assert len(status.splitlines())==2
receipts=[]
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='RECEIPTS.json':
        assert p.stat().st_size<20*1024*1024
        receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in [agent/'STATUS.md',agent/'WORKLOG.md',agent/'LEARNED.md']:
    receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
for row in receipts:
    p=Path(row['path']);assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes']
dump(run/'out/RECEIPTS.json',{'status':'PASS','timestamp':timestamp,'schema':'protocol exact-field-set PASS','statement_sha256':claim['statement_sha256'],'full_fei':'OPEN','independent_review':'PENDING','remote_copy':'UNVERIFIED','files':receipts})
print(json.dumps({'status':'PASS','assertions_full':full['exact_assertions'],'assertions_independent_witness':witness['exact_assertions'],'unpaid_cuts_localized':len(full['unpaid_rows']),'files_hashed':len(receipts),'version':3,'full_fei':'OPEN'}))
