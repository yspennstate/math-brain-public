# A016 stage 2: complete codes on tensor bent splices

## exact target, quantifiers, hypotheses and units

Follow B04 STREAM_NOTES.md v2, 2026-10-11 23:25 UTC: evaluate a-fold tensor bent splices with even core dimension m, compare an actual whole-set code and the one-root reference with selector entropy increment Delta and total influence I, and give certified cases m=2,4,6. All inputs are independent fair binary variables, outputs are +/-1, and costs and entropies are in bits. The all-parameter statements below hold for a>=1 and even m>=2; the queue limiting constant is stated for each FIXED a as m tends to infinity through even integers. Finite validation uses a=1,2. This is a lead-directed mechanism calibration and source-bound stopping-tree guard; it is not a universal FEI claim.

Result: the n=a(m+1) bit whole-set mask costs at most 3I, and the literal one-root reference costs less than 9I, uniformly in both parameters. Their cost/Delta ratios diverge exponentially with m even though their cost/I ratios remain bounded. The actual raw selector-first derivative charge has an additional tensor-spectator term and diverges relative to I when a grows at fixed m. Removing independent spectator factors repairs that particular overcharge.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-11 23:19 UTC, the complete B04 lead notes v2, and own STATUS.md before choosing this stage. Re-read EXECUTION_PROTOCOL.json (fei-execution-protocol/2, revision 2026-10-11-execution-v2). Read the lead's CLAIMS.json, especially B04-BENT-SPLICE-SHARP v1 and B04-NODE-BOUNDARY v1, and code/verify.py to identify the precise tensor family. The lead's advertised REPORT.md did not exist at the initial read: its claims' source locator cannot serve as a complete proof receipt at that time. Therefore the spectrum, influence, leading entropy asymptotic, code bound and tensor boundary calculation are reconstructed here without treating the missing report as an accepted premise.

Read A018's saved REPORT.md locators from its collision-law run for the normalization and bent-splice construction. The source queue definitions and the integral G come from A016 stage 1 REPORT.md sections 4-5, which reconstruct threshold_paper_38pp sections 5.2/5.6/5.7 and reductions/forests.tex. That stage remains pending independent review; the asymptotic argument is summarized again below, and no external acceptance is assumed. No new broad universal candidate was opened while the stream has outstanding review work. Source hashes and access failures are recorded in out/SOURCE_RECEIPTS.json.

## complete derivation or exact first unsupported line

### 1. Actual Boolean family, Fourier atoms, and corrected influence

On m binary data bits define g(y)=(-1)^(y_1 y_2+...+y_{m-1}y_m), and g'(y)=g(y)-2*1{y=0}. Since g(0)=1, both are Boolean. Let f_m(x,y)=g(y)-2x*1{y=0}. For a disjoint blocks put F_{a,m}=product_{j=1}^a f_m(x_j,y_j), with n=a(m+1) coordinates. This matches the lead's a-fold tensor family, not a splice sharing one data block among all selectors.

Set delta=2^{-m} and u=2^{-m/2}. Each bent coefficient equals e_T u, e_T in {+1,-1}. The product of two-bit Walsh tables proves this directly. The fraction of positive signs is w_+=(1+u)/2, since sum_T hat(g)(T)=g(0)=1. Using the fair binary selector character, the parent Fourier coefficients are

    hat(f_m)(selector absent,T)=e_T u-delta,
    hat(f_m)(selector present,T)=delta.

Thus their squared masses are delta(1-e_T u)^2 and delta^2. The data marginal for T is their sum. Parseval holds exactly. The empty mass is p_empty=(u-delta)^2, and the tensor empty mass is p_empty^a.

Every data coordinate of g has influence 1/2. At the origin and its m neighbors g has value +1, so all edges incident to the origin are originally nonpivotal. Flipping the origin turns both directed orientations of each such edge pivotal. Hence each data influence of g' is 1/2+2delta, not 1/2+delta. Averaging the two branches gives

    Inf_x(f_m)=delta,
    Inf_{y_i}(f_m)=1/2+delta,
    J:=I_data(f_m)=m/2+m delta,
    I_0:=I(f_m)=m/2+(m+1)delta.

Disjoint multiplication preserves each factor's physical influences, so I(F)=a I_0 and I_sel=a delta. This corrected the first pilot's anticipated formula; the failed assertion is retained in out/PILOT_FAILURE.json.

### 2. Exact entropy increment and its asymptotic scale

Write

    A(u)=-2 sum_{e=+/-1} w_e (1-eu)^2 log2(1-eu),
    B(u)=sum_{e=+/-1} w_e (1-2eu)^2 log2|1-2eu|,
    w_e=(1+eu)/2,

with 0*log(0)=0. Substitution in the displayed Fourier masses gives

    H(f_m)=m+m delta+A(u),
    [H(g)+H(g')]/2=m-B(u),
    Delta_0=m delta+A(u)+B(u),  Delta(F)=a Delta_0.

The last identity follows from tensor entropy additivity and independent uniform selector branches. These identities supply exact finite expressions; the checker independently starts from the actual Boolean truth tables.

For fixed c, (1-ce u)^2 ln(1-ce u)=-ce u+(3/2)c^2 u^2+O(u^3). Averaging with w_e gives (-c+(3/2)c^2)u^2+O(u^4); symmetry removes odd powers. Therefore A=-delta/ln2+O(delta^2), B=4delta/ln2+O(delta^2), and

    Delta_0=delta[m+3/ln2+O(delta)],
    H(f_m)=m+O(m delta),  I_0=m/2+O(m delta).

Only this leading asymptotic is used; this stage does not re-open the lead's already computed second-order sharpness coefficient.

### 3. Whole-set mask: a complete decoder and uniform influence payment

Fix (a,m), the block order and the coordinate labels before drawing the Fourier set. The decoder reads n bits and outputs exactly the indicated subset. This is a full fixed-length binary code for every Fourier set, including the empty set; it needs neither a gate name per selected coordinate nor a spectral-model selection. Its exact cost is C_mask=n. Since I_0>=m/2 and m>=2,

    C_mask/I=(m+1)/I_0 <= 2(m+1)/m <=3.

For each fixed a,

    C_mask/I ->2,
    C_mask/Delta = (m+1)/Delta_0 ~ 2^m.

This reference works because the data spectrum is dense and total data influence is linear in the dimension. It would return n/I on an arbitrary Boolean seed and is not a universal reference bound.

### 4. Actual one-root generator, with every normalizer and the empty atom paid

Use one support R=[n], ordered by blocks (selector then m data coordinates), gamma=6/5, and theta_s(r)=min(1,(s/r)^gamma). After conditioning the root experiment on a nonempty root set, the sole root is deterministic: its root odds and rarity cancel exactly. Select a size s>=1 with probability 1/[s(s+1)], an s-subset with probability W_s(S)/Z_{n,s}, where

    W_s(S)=product_{r in S} theta_s(r),
    Z_{n,s}=e_s(theta_s(1),...,theta_s(n)),

then choose no children with probability 1/2. The selected successful single-visit run has probability

    q(S)=W_s(S)/[2s(s+1)Z_{n,s}].

These single-visit probabilities form a subprobability on nonempty sets. Larger collections of successful repeated visits may improve the output reference; they are not used or claimed optimized. The sole support is a coding parameter table, not a claim that F is one regular gate or one DNF conjunction. Direct subprobability/Gibbs coding is sufficient here.

Let p=p_empty^a and v=1-p. Give the empty set mass p and each nonempty set reference mass v q(S). This fixed reference depends only on the known parameters. Its complete expected negative logarithm is

    C_queue=h2(v)+sum_{S nonempty} P_F(S)
                    [1+log2(s(s+1))+log2 Z_{n,s}-sum_{r in S}log2 theta_s(r)].

There is no uncharged empty flag, root normalization, codebook choice or posterior label entropy. A posterior restricted to these single-root single-visit runs is a point mass given S. The empty mixture probability is paid by h2(v), rather than discarded.

Since theta<=1, Z_{n,s}<=binom(n,s)<=2^n. Every rank r<=n, so -sum log2 theta_s(r)<=gamma s log2(n/s). Using s(s+1)<=3^s and sup_{t in [0,n]} t log2(n/t)=n/(e ln2), and I=E|S|>=am/2>=1, gives

    C_queue <= [2+log2 3+3(1+gamma/(e ln2))] I <9 I.

Here h2(v)<=1<=I, Pr(S nonempty)<=I, n<=3I, and dropping v in the positive n-cost terms can only enlarge the bound. The strict numerical sign is exact: e>8/3, ln2>2/3, and log2 3<8/5 imply the bracket is less than 69/8<9. The first two inequalities follow from the exponential series and the first positive term of ln2=2 atanh(1/3), and the last follows from 3^5<2^8. No floating-point constant is a proof step.

### 5. Queue asymptotic and code/Delta ratio

Use the same constant as the addressing subset-generator analysis:

    w(t)=1 (0<=t<=1/2), w(t)=(2t)^(-gamma) (1/2<t<=1),
    integral_0^1 z w(t)/(1+z w(t)) dt=1/2,
    G=integral_0^1 log2(1+z w(t))dt-(1/2)log2 z
                                         -(1/2)integral_0^1 log2 w(t)dt.

The equation has one positive solution z. As in stage 1, coefficient tilting by independent Bernoulli odds z_n theta_s(r), with mean s, expresses log Z as sum log(1+z_n theta)-s log z_n plus log Pr(K=s). Chebyshev and bounded adjacent atom ratios on a central O(sqrt n) window show the last term is o(n), without invoking an unproved local limit theorem. Riemann sums yield the displayed integral whenever s/n tends to 1/2. The normalization logarithm has rate integral log(1+zw)-(1/2)log z.

For completeness, the spectral law of f_m is within total variation u+delta of the law with selector always absent and the m data bits fair and independent: summing the absolute differences of the absent-selector masses and the selector mass gives at most 2u+2delta. For fixed a the tensor total variation is at most a(u+delta). The largest nonempty queue cost is O(n log n), so replacing the true law by this ideal law changes the normalized expectation by o(1). In the ideal law a selector ranks are absent and all other rank indicators are fair; since a is fixed, omitting those ranks changes Riemann sums and the expected selected log-weight rate by o(1). Binomial concentration gives s/n->1/2, the size logarithm is o(n), and the empty mixture cost is at most one bit. Consequently

    C_queue/(am) ->G,
    C_queue/I ->2G,
    C_queue/Delta ~G 2^m.

The elementary uniform-subset/Gibbs lower bound and Z<=binom(n,s) upper bound give

    1<=G<=1+(gamma/2)(1-1/(2ln2)),
    2<=2G<=2+gamma(1-1/(2ln2)) < 2.3344.

The decimal is a display only. Unlike addressing, this single-support reference pays no a-bit address name or root rarity. Copying addressing's 2+2G limit would add a nonexistent address charge. Limits in growing a and fixed m are not inferred from this fixed-a asymptotic; the uniform <9I estimate covers that regime directly.

### 6. Tensor guard on the lead's derivative boundary charge

The raw derivative influence is not spectator-invariant. For one factor, D_x f_m=(g-g')/2=1{y=0}, so 2I(D)=m delta. In a tensor product with an independent spectator h,

    I(D*h)=I(D)+||D||_2^2 I(h)=I(D)+delta I(h),

although Delta_x H and B_x are unchanged by h. This is immediate from the product Fourier law, and is checked from actual physical derivatives below.

Consider the actual tree revealing selectors in block order and stopping after all a selectors. At the jth selector (j=0,...,a-1), the earlier factors are independently restricted branches of average data influence J, and the later factors still have influence I_0. Thus the expected total raw boundary charge is exactly

    T_raw=sum_visited E[2I(D_v)]
         =a m delta + delta a(a-1)(2J+delta),
    T_raw/I(F)=delta[m+(a-1)(2J+delta)]/I_0.

For every fixed even m this tends to infinity linearly with a. This is not a double-counting-free resource merely because each selector is queried once: every node's derivative also bills the same independent data spectators.

This overcharge survives the exact-B bad-node filter. For a single factor let q_T=(e_T u-delta)^2+delta^2. Then q_T>=delta/2. Its selector-present atom is delta^2, so

    q_T h2(delta^2/q_T)>=delta^2 log2(q_T/delta^2)
                               >=delta^2(m-1).

Summing all 2^m rows proves B_x>=delta(m-1). Both B_x and Inf_x=delta are invariant under the remaining independent factors and under fixing earlier selectors. Therefore, for any finite threshold K, choosing an even m with m-1>K makes EVERY selector node of this selector-first tree satisfy B_x>K Inf_x. Counting only those nodes does not remove the quadratic-in-a raw charge.

The narrow repair is to remove independent tensor spectators before pricing the boundary. The factorwise charge is T_factored=a m delta, with T_factored/I=m delta/I_0<=2delta<=1/2. More generally, if f=g(x_A)h(x_Ac) and i belongs to A, then Delta_i H(f)=Delta_i H(g), Inf_i(f)=Inf_i(g), and B_i(f)=B_i(g). Hence a valid node inequality for g can be lifted using I(D_i g), retaining the spectator's terminal entropy, instead of I(D_i f). This transfer uses no additional influence payment. It is an algebraic correction for exact disjoint factors; no analogous rule for overlapping or approximately independent cores is established here.

This refutes only a universal raw-charge bound for this specified selector-first stopping rule, including its bad-node filter. It does not refute the lead's existence of a better adaptive stopping tree, good data-coordinate choices, factor removal, C019, or FEI. It explains why a successful tree must make its boundary charge or selection tensor-aware.

### 7. Certified finite ratios

| a | m | mask/Delta | mask/I (exact) | queue/Delta | queue/I |
|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2.46524581 | 12/7 | 4.13777771 | 2.87733303 |
| 2 | 2 | 2.46524581 | 12/7 | 3.71226989 | 2.58144287 |
| 1 | 4 | 9.96262292 | 80/37 | 14.64893047 | 3.17921931 |
| 2 | 4 | 9.96262292 | 80/37 | 13.54670788 | 2.94000681 |
| 1 | 6 | 43.68187404 | 448/199 | 60.45329499 | 3.11561404 |
| 2 | 6 | 43.68187404 | 448/199 | 56.53051890 | 2.91344382 |

The table displays rounded centers of rational intervals, not standalone floating-point certificates. Exact interval endpoints, H, Delta, total/selector/data influence, empty mass, raw and factored boundary charges are in out/CHECK.json. In particular C_mask/I is exactly 12/7, 80/37, 448/199 for m=2,4,6, independently of a. The finite cases match the divergent code/Delta and bounded code/I diagnosis; the asymptotic proof, not those six cases, establishes the limits.

## executed validation with domain, arithmetic, commands and outputs

Saved FROZEN_SPEC.json before computation. Executed:

    python -X utf8 runs/20261011T232501Z-account05-A016-addressing-benchmark/code/check_bent_codes.py

Final run: 19226 assertions, zero failures, 1.921725 seconds of measured script runtime. Six full Boolean truth tables at (a,m) in {1,2} x {2,4,6}, n<=14, are transformed by an independent integer FWHT. Every Fourier squared coefficient is checked against the exact tensor product of the base formula. Physical edge counts independently verify every selector and data influence. Actual derivatives at every selector-first node, including all earlier selector assignments, are independently transformed and certify T_raw exactly. Base conditional erasure satisfies the displayed delta(m-1) lower bound.

Queue normalizers are NOT evaluated as ordinary floating point: theta=(s/r)^(6/5) is enclosed by dyadic rational fifth-root bounds, each endpoint checked by integer fifth powers. Elementary symmetric sums are enclosed by monotone exact rational recurrence. Every logarithm uses a 36-term rational atanh series with explicit geometric tail, then outward rounding to a common denominator 2^100. All final cost/Delta and cost/I intervals use positive rational denominator bounds. Early pilots stopped on the influence expectation error and on Python's huge-rational string-rendering limit; corrections and provenance are in out/PILOT_FAILURE.json. The frozen memory estimate was 40 MB; peak resident memory was not measured. This bounded job required no >300 MB memory gate, no GPU and no automatic dimension escalation. Exact results were checkpointed after each case in out/PARTIAL.json.

## proof dependencies and changed downstream conclusions

No unreviewed broad FEI statement is a premise. The bent constructor and node-charge target are sourced to the B04 lead; the claimed family identities and code estimates are independently derived here. G's representation follows the stage-1 coefficient argument, restated above, and remains pending independent review. This supplies the requested C020 control at all parameters and isolates a source-bound C019 obstruction in the lead's own tensor sharpness family. A018/A020 can compare exact bad-node B costs with the raw/factored derivative bills; B06 should not interpret a raw second-moment-type charge as a nonreused resource. No shared registry was edited and no novelty claim is made for tensor additivity or spectator invariance themselves.

## one next mathematical action and independent reviewer

A090/A091: independently reconstruct the point-flip edge factor two, fifth-root normalizer enclosure, and actual selector-first spectator charge. B04 lead/A019/A027: before another isolated family test, formulate a tensor-invariant bad-node boundary payment by removing exact independent factors and retaining their terminal entropy; then test a nonfactorable overlapping-core splice on that same fixed stopping rule. The first unsupported line is the existence of a universal adaptive stopping tree whose factor-aware bad-node boundary charges are O(I) without reusing influence or discarding terminal entropy. The selected tensor family proves no such universal existence statement.

## actual persistence receipts or precise save blocker

Saved the four required protocol files, the frozen specification, checker, checkpoint, final certified outputs, failed-pilot provenance and source/persistence receipts within this stage's A016 run folder. STATUS.md, WORKLOG.md and LEARNED.md are current. out/PERSISTENCE.json verifies schema keys, PACKET_DELTA identity and artifact SHA256 hashes. Supervisor copy, independent acceptance and mirror verification remain pending. No git, other agent directory write, brain mutation, deletion or external communication occurred.

### Universal bridge

This stage moves C020 by closing the lead's maximal selector-loss tensor bent-splice control: a complete mask costs <=3I and the literal single-root reference costs <9I for all a,m, while cost/Delta grows like 2^m. It also sharpens the lead's C019 adaptive-boundary target: the specified selector-first raw charge, even restricted to exact-B bad nodes, is a m delta+delta a(a-1)(2J+delta), so a dimension-independent raw budget fails under independent tensor spectators although a factorwise budget is <=I/2. What remains is a universal tensor-invariant adaptive boundary payment with complete terminal entropy and no repeated influence. NEXT is to repair that exact structural obstruction and test the resulting rule on a nonfactorable core; this directly addresses the missing universal mechanism rather than enlarging a solved class or another finite census.
