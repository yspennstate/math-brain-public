# A018 stage 2: independent review of sharp selector and boundary debt

Run 20261012T010436Z-account05-A018-shared-data-collision-law; B04/A018. Full FEI remains OPEN.

Verdicts: **HOLDS** for B04-SEL-LOG-SHARP@1, **HOLDS at the stated asymptotic scope** for B04-BENT-SPLICE-SHARP@1, and **HOLDS** for B04-NODE-BOUNDARY@1. These are independent reconstructions of the lead's existing claims, not three new theorem candidates. The usual zero-mass entropy convention is necessary at the two-bit bent endpoint. No source repair changes any theorem statement.

## Exact target, quantifiers, hypotheses and units

For arbitrary fresh uniform a-bit selectors x, independent uniform data y, and Boolean branches g_x(y) on one common cube, put F(x,y)=g_x(y), s=I_sel(F), and Delta=H(F)-average_x H(g_x). All H and h_2 use bits. With the normalized stage-1 row laws, Delta=M_W+B_W and B_W=H(S_W|S_data). The first target is the universal inequality

Delta <= min(a,(2/ln2)s)+a h_2(s/a) <= s log_2(e^3 a/s).

At a=0 both sides mean zero. At s=0 the right side is its continuous zero extension, avoiding an undefined 0 log 0 expression.

The second target is the even-m bent one-point splice, s=delta=2^{-m}, u=sqrt(delta):

Delta=delta(m+3/ln2)-(19/(6ln2))delta^2+O(delta^3),
[(2/ln2)delta+h_2(delta)]-Delta=(8/(3ln2))delta^2+O(delta^3).

Disjoint tensor powers scale Delta and selector influence additively. Sharpness means the gap is o(s) along these actual Boolean families; it does not assert an exact pointwise supremum for every pair (s,a).

The third target concerns every Boolean f on n>=1 uniform coordinates and every physical coordinate i. Write g=f|_{x_i=0}, h=f|_{x_i=1}, D=(g-h)/2, d=Inf_i(f). For this trinary derivative use the spectral energy

I(D)=sum_T |T| hat(D)(T)^2 = sum_{S contains i} (|S|-1) hat(f)(S)^2.

Then Delta_i H <= (3/ln2)d+2I(D). The derivative's I is an L2 Dirichlet energy, not the edge-disagreement influence of a trinary-valued function.

## Sources actually read, revisions and theorem locators

Stage start readback: BOARD.md dated 2026-10-12 01:00 UTC, B04/STREAM_NOTES.md v2 dated 2026-10-11 23:25 UTC, own STATUS.md and LEARNED.md. The lead explicitly assigns A018 an independent exact reconstruction of claims (1),(2),(4); the proposed quadratic common-spectrum continuation from stage 1 is superseded by this review direction. A019 has meanwhile proved and the lead has reconstructed rare translations, so that baseline is not restarted.

The governing protocol remains fei-execution-protocol/2, revision 2026-10-11-execution-v2, re-read this stage. Original claims are claude/B04/runs/20261011T224500Z-claude-B04-sharp-selector-debt/CLAIMS.json. Exact statement text and versions are preserved. Its announced statement hashes differ from direct UTF-8 hashes; each review record retains both values, and the local statement_sha256 uses the recomputed UTF-8 digest. Original proof_source fields point to a REPORT.md not present in that run's file listing; this review provides its own complete analytic proofs rather than assuming access to the missing report. The lead's code/verify2.py was read after writing this stage's separate checker; it uses floating entropy for its node census. No lead module or code is imported. The new checker supplies a rational replacement, without changing the mathematical claims.

Dependencies reconstructed in A018 stage 1: threshold_paper_38pp Proposition 8.6, equations (75)-(79), normalized Delta=M+B; elementary posterior M_W<=(2/ln2)I_W proof, independently reconstructed by the B04 lead this stage. The source-complete A018 stage-1 report and its accepted scope are retained without re-running its census. Elementary conditioning, binary entropy and an indicator-specific tensorization proof below supply the remaining argument. No external paper, pending A019 theorem, or floating search is assumed as a premise. Local source hashes are saved in out/SOURCE_RECEIPTS.json.

## Complete derivation or exact first unsupported line

### 1. Selector logarithmic envelope: HOLDS

Let Z_j indicate selector coordinate j in the parent spectral sample. By the entropy chain rule and conditioning,

B_W=H(S_W|S_data) <= H(S_W) <= sum_{j in W} h_2(P(Z_j=1)).

Walsh Parseval gives P(Z_j=1)=Inf_j(F). Concavity of h_2 therefore gives B_W<=a h_2(s/a). This argument uses neither orthogonality of branches nor a disjoint-support mixture. Stage 1's posterior bound and the alphabet bound give M_W<=min(a,(2/ln2)s); add them.

For 0<t<=1, -(1-t)ln(1-t)<=t, hence h_2(t)<=t log_2(e/t). Thus

min(a,(2/ln2)s)+a h_2(s/a)
<= (2/ln2)s+s log_2(ea/s)
=s log_2(e^3 a/s).

At s=0 every queried influence is zero and F is independent of the selector, so Delta=B=M=0. The a=0 case is also exact. All units and constants agree with B04-SEL-LOG-SHARP@1.

### 2. Bent-splice formula and sharpness: HOLDS

Take b(y)=(-1)^(y_1y_2+...+y_{m-1}y_m) on even m>=2 data bits, and b'=b-2*1_{y=0}. The exact two-bit transform tensorizes: hat(b)(T)=e_T u, e_T in {+1,-1}, u=2^{-m/2}. Its signs have multiplicities

N_e=(2^m+e 2^{m/2})/2, equivalently N_e u^2=w_e=(1+eu)/2.

Parseval gives the uniform squared spectrum of b, H(b)=m. For the parent splice the two coefficients at data set T are e_T u-u^2 and u^2. For b' the coefficient is e_T u-2u^2. The selector differs only at the flipped data vertex, so s=u^2 exactly. Summing these signed coefficient histograms before squaring gives

Delta=m u^2-2 sum_e w_e(1-eu)^2 log_2(1-eu)
          +sum_e w_e(1-2eu)^2 log_2|1-2eu|.

At m=2, e=+1, the latter term is zero by z^2 log|z| -> 0 as z -> 0; do not evaluate log(0) numerically. This is the standard spectral-entropy zero convention. The parent coefficient calculation is independent of the lead's simplification and agrees with its stated A+B formula.

For an analytic remainder proof work in natural units. Define L(z)=(1-z)^2 ln(1-z). On |z|<1 its coefficients are

c_1=-1, c_2=3/2, c_k=-2/[k(k-1)(k-2)] for k>=3.

This follows by multiplying the absolutely convergent series ln(1-z)=-sum_{k>=1} z^k/k by 1-2z+z^2. The weighted sum sum_e ((1+eu)/2)L(lambda e u) contains only even powers. Its u^(2j) coefficient is c_(2j) lambda^(2j)+c_(2j-1) lambda^(2j-1). Combining lambda=1 with multiplier -2 and lambda=2 with multiplier +1 gives

Delta ln2 = m delta ln2+3delta-(19/6)delta^2-(61/30)delta^3+O(delta^4).

In particular the first two claimed terms hold. For a direct rigorous remainder through order delta^2, m>=4 implies delta<=1/16 and |2u|<=1/2. For j>=3 the absolute combined coefficient is at most 2*4^j (use |c_k|<=1 for k>=3). Consequently

|Delta ln2 -m delta ln2-3delta+(19/6)delta^2|
<=2 sum_{j>=3}(4delta)^j
<= (512/3)delta^3.

This proves an explicit uniform O(delta^3) error rather than a numerical series fit. Also

h_2(delta)ln2=delta ln(1/delta)+delta-delta^2/2+R,
|R|<=delta^3/[6(1-delta)].

Subtracting yields the claimed (8/3)delta^2 natural-unit sharpness gap, with a uniform O(delta^3) error. Its sign is strictly positive for all sufficiently large even m; the finite endpoint signs checked here are separately certified. Since the gap/delta tends to zero, for every epsilon>0 a large even m violates an envelope lowered everywhere by epsilon*s. Tensor products on disjoint (selector,data) blocks satisfy Delta_t=t Delta_1 and s_t=t delta; the a=t envelope is also t times the one-bit envelope. No pointwise optimality away from this sequence is claimed.

### 3. Derivative-boundary payment: HOLDS

The one-bit selector envelope gives

Delta_i H <= (2/ln2)d+h_2(d)
<= (3/ln2)d+d log_2(1/d).

Let A=supp(D)={y:g(y)!=h(y)}, so E[1_A]=d and D takes only 0,+1,-1. I(D)>=I(1_A): on an edge with just one active endpoint the derivative squared differences are identical; on an edge with two active endpoints the indicator has zero difference whereas D has nonnegative squared difference.

The sharp support-isoperimetric factor follows from the same elementary product-entropy tensorization used in stage 1, applied to the indicator itself. On each one-bit fiber with one active endpoint,

Ent_i(1_A)=(ln2)/2=2 ln2 E_i[(D_i 1_A)^2],

and on constant fibers both sides are zero. Tensorize and sum to obtain

d ln(1/d)=Ent(1_A)<=2 ln2 I(1_A)<=2 ln2 I(D).

Therefore d log_2(1/d)<=2I(D), giving exactly

Delta_i H <= (3/ln2)d+2I(D).

This reconstructs the edge-isoperimetry step directly, with no outside Harper theorem dependency. Walsh expansion of f=(g+h)/2+(-1)^{x_i}(g-h)/2 shows hat(D)(T)=hat(f)(T union {i}) and proves the claimed spectral expression for I(D). At d=0, D=0 and Delta_i=0. At d=1, the support logarithm vanishes; all steps remain valid.

For the bent splice D is one signed point indicator on m bits, so I(D)=m delta/2. Its node bound is delta(m+3/ln2). Section 2 gives Delta/node-bound ->1, verifying first-order sharpness. The bound's derivative term cannot be discarded even though it is small in total mass.

### 4. What the review does not prove: first unsupported line

The lead's open statement remains unproved: there exists a terminal-certified adaptive physical stopping tree for every Boolean f in which

sum_{v: exact B_v>K d_v} pi_v * 2 I(D_v) <= K' I(f)

for fixed dimension-independent K,K', without spending a descendant/terminal influence reserve twice. All three accepted claims are local; they do not supply this selection and cumulative payment theorem. Replacing exact B_v by h_2(d_v) is invalid for the proposed localization: odd-function roots, including majority, can have exact B_v=0 even when the binary upper bound is positive. A fixed query order can charge the second spectral moment, which is not an absolute multiple of the first moment. This remains an honest C019 gap, rather than a consequence of the newly reviewed node lemma.

The board's A016 tensor-spectator overcharge and A017 point-surgery tests are relevant safeguards. Next work should remove exact spectators before boundary pricing and retain the actual terminal entropy; merely paying every node's full I(D_v) would repeat the known excess.

## Executed validation with domain, arithmetic, commands and outputs

Frozen spec: out/FROZEN_SPEC.json, persisted before computation, helper A018-independent-lead-review-v2. Separate implementation in code/check_lead.py uses standard-library integer arithmetic, Fraction logarithm enclosures and exact rational Taylor coefficients; it imports no lead checker.

Pilot command: `python -X utf8 runs\20261012T010436Z-account05-A018-shared-data-collision-law\code\check_lead.py --pilot`.

Result out/PILOT.json: PASS, 6,463 assertions, 1,082 block cases, 804 singleton nodes, all tables n<=3, observed runtime 0.169 seconds. All parent transforms are checked against independent direct character sums. The selector envelope is checked in both separate forms, Delta<=a+a h_2 and Delta<=(2/ln2)s+a h_2, so the min is certified without selecting a rounded branch. The cruder logarithmic envelope is certified as well. Zero-influence and empty-selector cases are included.

Full census command: `python -X utf8 runs\20261012T010436Z-account05-A018-shared-data-collision-law\code\check_lead.py`.

Its census completed and persisted out/CENSUS.json before a later bent precision check stopped. The completed census contains all 65,536 four-bit truth tables and all four coordinates, 262,144 singleton nodes, including 1,024 zero-influence nodes. Each parent Walsh transform is independently checked by direct sums. Physical child mismatch and physical trinary derivative edge energy independently verify the spectral quantities. For every nonzero node, the certified upper interval for

Delta_i / [(3/ln2)d+2I(D)]

is strictly below 81/100. The largest observed upper endpoint is the rational

4962238801213655492118400 / 6140668028959891248078249.

Its saved interval witness is truth mask 7, coordinate 0, d=1/8, I(D)=3/16, and

Delta ln2 = (768ln2-200ln5-72ln3)/256.

The certificate proves the uniform rational cap, not an exact symbolic maximum classification. The census's assertion count is 851,970 by the explicit loop count (65,536 direct-transform checks, three checks per 262,144 nodes, two final assertions); its original output was saved before timing/counter finalization, so no measured full-job runtime is invented.

All entropy expressions are exact rational or integer linear combinations of ln(prime). Enclosures use a 36-term atanh series with geometric tail, reduction to [1,2), and outward rounding to rational grid 2^-80. Signed coefficients select the appropriate interval endpoint; no floating subtraction is used for a sign.

Precision-only follow-up: the full run's later strict bent-gap test was not established on that grid. A separate `--bent-only` diagnostic saved out/LOW_PRECISION_FAILURE.json. The planned family and case counts were unchanged; out/PRECISION_AMENDMENT.json records refinement to 2^-96. Command:

`python -X utf8 runs\20261012T010436Z-account05-A018-shared-data-collision-law\code\check_lead.py --bent-only --bits96`.

Result out/BENT.json: PASS, 57 assertions, observed runtime 0.188 seconds. It certifies 20 even-m histogram cases m=2,4,...,40, separately reconstructs actual parent transforms at m=2,4,6,8, proves equality of the histogram and closed forms using exact prime-log expressions, checks tensor fixtures (m,t)=(2,2),(2,3),(4,2), and checks exact Taylor coefficients through delta^6. Refinement stopped as soon as all required signs were rigorous. The failed low-precision enclosure is preserved; it is not a counterexample or a theorem failure.

Jobs ran sequentially, no GPU, no randomization, no automatic dimension escalation. Estimated memory was 100 MB; no job was expected to exceed 300 MB, so memok was not triggered. Process peak memory was not measured. Full-job deadline was frozen at 300 seconds; pilot at 60 seconds. No claim of continuous campaign execution or capacity is made.

## Proof dependencies and changed downstream conclusions

The original lead versions and statement text are preserved in CLAIMS.json with independent A018 review records appended; their announced hashes and corrected UTF-8 hashes are both pinned. The stage-1 A018 posterior proof was accepted by the lead at its stated scope; Section 1 completes the entropy envelope through finite Shannon inequalities. Sections 2 and 3 reconstruct the all-dimensional sharpness and boundary proofs independently. Neither numerical census extrapolation nor an unaccepted class result is used in the analytic argument.

Downstream: A019/A020 can consume B04-SEL-LOG-SHARP@1 and B04-NODE-BOUNDARY@1 as independently reconstructed tools. B05/B06/C019 can consume their local constants and the exact derivative energy, while retaining the bad-node localization and terminal reserve as hypotheses. The lower-envelope obstruction is independently accepted only in its actual Boolean asymptotic scope. B20 may adopt these source-bound review records; this agent does not edit the shared registry. Second-moment closure and the lead's positive-energy corollary were not separate review targets here.

## One next mathematical action and independent reviewer

Next: reconstruct the spectator-free bad-node boundary bill on a splice whose mismatch uses the same data coordinates as its terminal core. Test whether a two-level physical stopping choice can transport that bill to distinct downstream deficit reserves while keeping terminal H explicit. Start with A016's spectator guard and A017's incompatible two-flip phase-gradient case; use exact B_v to decide which nodes owe boundary cost. This tests the universal bottleneck directly instead of opening another low-energy class.

A090/A091 should challenge this reconstruction, especially the trinary energy normalization and the asymptotic remainder. The B04 lead may adopt the three review verdicts. No external message or shared file was written; these local files are the authorized source-bound handoff.

## Actual persistence receipts or precise save blocker

The four required protocol files are REPORT.md, CLAIMS.json, PROGRESS.json and equal-content PACKET_DELTA.json. code/ and out/ contain the independent helper, frozen spec, pilot/census/bent certificates, precision-failure receipt, amendment, source hashes and persistence readbacks. STATUS.md remains two lines; WORKLOG.md is appended; LEARNED.md retains stage-1 facts plus the durable review conclusions. out/PERSISTENCE_RECEIPTS.json checks exact protocol field names (normalizing the annotated packet_ids name), JSON parse, packet-delta equality, statement hashes and file limits. Supervisor copy, mirror verification and adoption are not claimed. The original lead REPORT.md is absent; this complete independent proof resolves the review's source need locally, without mutating that run.

## Universal bridge

This stage moves C019 by independently validating the sharp local selector envelope and its physical derivative-boundary substitute, replacing floating node evidence with a 262,144-node rational certificate and proving the constants analytically. It also verifies why no uniformly smaller selector-only first-order price can remove the rare logarithm. The remaining universal obligation is to select a terminal-certified adaptive tree and pay the exact bad-node sum of 2I(D_v) once, after removing irrelevant tensor spectators; no universal cumulative constant is proved. The next shared-coordinate, two-level reserve test is the shortest route because it probes that precise missing transport step, while another orthogonal or disjoint-activation class would leave it untouched.
