# Independent mathematical audit of the FEI campaign plan

11 October 2026. Reviewer: /root/fei_audit.

## Verdict and scope

The principal conditioned posterior-forest inequality, its constant, the physical restriction decomposition, and the existential good-coordinate equivalence are correct as written in the reviewed plan. The bit conversion of the phase-energy estimate is also correct. No reviewed formula supplies a proof of unrestricted FEI.

The most consequential defects in the initial plan are incomplete hypotheses and several tasks that would rediscover an already proved corollary or an already refuted payment. These should be corrected before treating the 100 packets as a mature deployment design. In particular, B09 needs the three explicit weighted-threshold obstructions already present in the recovered reductions manuscript; B07 needs the existing fixed-prefix no-go controls; and B05 must retire fixed-price local variance/moment repairs after the new natural run.

I independently reconstructed the analytic B05 counterexample and found no gap in its stated local no-go theorem. I did not inspect, rerun or independently implement its floating-point checker. The older Brain source controls below are distinguished from this new analytic audit: where only the recovered route map or addendum was read, their original proof remains the source to retrieve before importing it as an accepted dependency.

No shared final file or external repository was edited by this reviewer. Proposed TeX insertions are in [plan_audit_ready_to_integrate.tex](sandbox:/workspace/scratch/cd992ff12e5c/fei_audit_scratch/plan_audit_ready_to_integrate.tex). Input hashes are in [plan_mathematical_audit_input_hashes.json](sandbox:/workspace/scratch/cd992ff12e5c/fei_audit_scratch/plan_mathematical_audit_input_hashes.json).

The line references below refer to the initial plan source with SHA-256 e7cc3f21e59cf4c718e481c21caac18c042b0f716f0e15162a86e09d2e7fd692. The reviewed initial assignments JSON hash is 940483bc46fe5cdad8ec05d69983898fa9f4c873b8bc8358f3e20d37c6928ccf. The parent and another agent may subsequently revise these files.

## 1. Corrections ranked by mathematical importance

### 1.1 B09 is missing already proved weighted-threshold obstructions

Locations: lines 185–189, A041/A042/A044/A045, the mandatory suite, first action at line 691.

The recovered reductions paper's biased.tex does more than say that weighted sums lose a symmetric lattice argument. It proves:

1. Conditional physical total correlation is not bounded by a universal multiple of influence, even for increasing weighted thresholds.
2. The proposed variance normalization paid by pivotal logarithms fails with coefficient exactly one, even after adding any fixed O(I) term.
3. A coordinatewise conditional-total-correlation recursion cannot be paid by influence at even one coordinate universally: its explicit family makes every coordinate ratio grow with arity.

The first two controls use the event A_m = {mX_0 + sum X_j >= m}, with light bias q = m^(-2) and heavy bias q_0 = (m-1)q^m/[1+(m-1)q^m]. With alpha = P(A_m), Q the conditional physical input law, V = Var(f_m), and rho_i physical pivotal probabilities, the recovered theorem gives

    alpha TC(Q)/I = (ln m + 1)/8 + O((ln m)/m),
    [V ln(1/V) - sum I_i ln^+(4 rho_i/V)]/I
        = (ln m)/2 - ln 2 + O((ln m)/m).

The genuine corrected entropy in bits nevertheless has H^+/(I-V) -> 2. These are normalization failures, not generalized-FEI counterexamples.

For the third control, set the two-branch mixture parameter eta = 1/2, equivalently q_0 = q^m/(1+q^m), and let q tend to zero with m fixed. For every coordinate j,

    alpha sum_{k != j} I_Q(X_j;X_k) / I_j -> m ln 2 / 2.

Then let m increase. This is an existential no-go for conditional PHYSICAL total-correlation payment. It must not be confused with the still-open spectral erasure B_i target.

Required revision: A041 should start from all three controls and formulate one replacement inequality that survives them. Reproving the known failed symmetry/TC step is baseline reproduction, not a new research result. The larger-multiplier version of the pivotal-credit estimate is not refuted by the coefficient-one control.

### 1.2 A019 and first-action B12 repeat an existing corollary

Locations: line 318, line 693.

The public paper now already proves I_sel >= c a implies the closure constant max{2/c,C}. Merely replacing orthogonality with a quantitative neighboring-disagreement condition is therefore completed baseline work.

A useful next packet must either prove that condition for a genuinely new family with unbounded arity/depth, or bound the exact collision ledger for an explicit structural family with I_sel/a tending to zero. A statement about unbounded selector arity alone does not establish novelty.

Add the bent-splice control explicitly: for a one-bit selector between actual Boolean branches, I_sel = 2^(-m) and the entropy-increment ratio is at least m-1. This rules out universal selector-only increment charges. It does not refute the full entropy-to-total-influence inequality or a suitable-coordinate choice.

### 1.3 Phase-energy hypotheses are incomplete

Locations: lines 175–183, A034/A079.

Restore the source's hypotheses: disjoint groups X,Y of uniform independent physical bits, genuine Boolean sign f, and integer d >= 1 bounding every full Fourier coefficient's X-degree. Define p_X(S) = sum_T hat f(S,T)^2 and I_Y as physical/spectral influence in the auxiliary group.

The source's statement in nats is H_nat(p_X) <= 2 I_Y + 2(d-1) ln 2, so the plan's conversion to bits is correct. The phrase “correlated auxiliary coordinates” should mean correlated auxiliary SPECTRAL coordinates, not correlated physical inputs.

The d >= 1 condition is substantive: d = 0 would make the displayed additive term negative and would fail, for example, for a constant Boolean function. The unpaid conditional term and the fixed-cyclic-marginal tensor embedding are correctly retained.

### 1.4 Retire fixed-prefix Booleanity work already refuted

Locations: A033, A031/A032/A035 and the mandatory suite.

The recovered Brain route map §3 already records an explicit real-valued, dyadic, normalized family satisfying every prescribed fixed order of signed square-convolution cancellation, and norm constraints under correspondingly shallow physical restrictions, while aggregate erasure/influence diverges.

The cyclic-label addendum separately records a fixed atom-cap-prefix no-go. These are distinct relaxed hierarchies and neither family is an actual Boolean FEI counterexample.

Revise A033 to name the exact hierarchy, import the relevant no-go family, and identify an additional consequence of full Booleanity absent from it. Increasing a fixed truncation order, adding dyadic coefficients, or merely adding a small square defect is already rejected for the corresponding archived scopes. This does not exclude a finite proof using some other full-Booleanity consequence.

### 1.5 B05's new result materially changes local-potential work

Locations: B05, B06, B08, B13; current status; first actions.

The new natural run refutes every universal all-coordinate fixed-price inequality L <= Kd + A V_post + B M_inf. It should be a named mandatory guard, not just a status entry.

The next useful packet is a complete control-first versus selector-first tree calculation for the actual sparse-activation family, retaining terminal entropy. That would explain a possible nonlocal source of payment. Searching for another fixed finite linear combination of the same local variance/moment terms has already been ruled out.

Do not promote this local failure to a failure of an existential stopping-tree criterion, a universal theorem quantified only over suitably chosen trees, or full FEI.

### 1.6 Universal closures are not partial results

Location: line 636 under “Major partial outcomes.”

A universal good-coordinate erasure theorem or a universal summable stopping tree with uniformly paid terminals would prove unrestricted FEI. Move these to the primary outcome. The partial-outcome list should contain restricted-class variants with explicit class hypotheses and constants.

### 1.7 Clarify function-dependent references and physical bias

Location: line 121. A reference may depend on the fixed f, even on its spectrum. This is mathematically legitimate and does not require charging a separate description of f or its entire codebook. The problem with choosing Q = P_f is simply that its cross-entropy equals H(f), leaving the original desired bound unpaid. A codebook chosen separately for the sampled Fourier set A is different: that choice must be included in the actual reference experiment/ledger.

Location: A024. Restricting a uniform physical cube leaves its unqueried coordinates uniform. In disjoint composition, restrictions may change inner-output means and therefore the outer gate's induced product law. The packet must distinguish those effects rather than suggest that a fair physical restriction itself creates arbitrary biased physical inputs.

Location: line 255. “Every counterexample packet must give a reproducible Boolean definition” is too broad for explicitly auxiliary-law targets. Require a Boolean realization for a purported Boolean counterexample; allow a fully specified non-Boolean auxiliary counterexample with its relaxed target and scope clearly marked.

## 2. Conditioned posterior forests: exact audit

The plan correctly reproduces the theorem in recovered reductions/paper/forests.tex.

For a finite union representation with nonconstant gates, finite ordered covers and positive global fractional incidence weights, the queue is a fixed random generator. Invalid and infinite runs have no successful-output mass. Activating a specified nonempty root set has probability

    2^(-Lambda) product_{root l} lambda_l pi_l.

Root and child names together charge each visited gate once. A partition forest really is an actual finite once-per-gate run because its selected subsets partition A, each attachment uses a selected parent variable, and the chosen directed forest reaches every used gate. The source-SCC root intersections are disjoint as proved in the recovered manuscript.

The subset normalizer contributes |A| log_2(6e). Size choices contribute at most |A| log_2 3; child counts at most |A|(1+log_2 3); multiset choices at most 2|A|. Hence

    K_ref = 3 + 2 log_2 3 + log_2(6e)

is correct. Conditioning on at least one initial root divides successful run mass by Z, adding log_2 Z with the displayed negative sign to its negative log probability. No almost-sure-termination assumption is required.

Log-sum over a law on distinct actual runs gives the posterior subtraction -H(P_A). Counting multiple abstract descriptions of one random-generator outcome would be invalid; the plan correctly prohibits it. Splitting the spectrum into empty/nonempty mass gives h_2(v), with nonempty mass v = Var(f), so the displayed residual and final sufficient FEI constant 2 + K_ref + K are correct.

The residual is not bounded by naming its optimizer. For a fixed representation/weight choice, the finite variational minimization over witnesses can be evaluated as a log partition sum, but that identity supplies no influence bound. A010 must certify all continuous weights and all allowed representations in its stated bounded family before claiming failure of its infimum; failure of one representation is weaker.

For a fully self-contained task packet, explicitly import the source's gate nonconstancy, finite-cover, source-SCC, and actual-run conditions. The plan's reference to the full recovered definitions is adequate for exposition but agents should not silently weaken them.

## 3. Physical restrictions, block exposure and the selector interface

The exact one-coordinate identity and mixing bound are correct. With parent Fourier pair c_T,d_T, its contribution is

    (c_T^2+d_T^2) kappa(d_T^2/(c_T^2+d_T^2)).

The conditional binary-entropy part is B_i and the remaining nonnegative part is a physical branch Jensen–Shannon term, at most (2/ln 2) sum min(c_T^2,d_T^2). This is at most (2/ln 2) I_i. The scalar expansion at small influence is correctly given as u log_2(1/u) + 3u/ln 2 + O(u^2).

For the good-coordinate equivalence, the entropy chain rule implies sum_i H(S_i|S_{-i}) <= H(S). Under FEI, an influence-weighted averaging argument therefore gives some relevant i with B_i <= C I_i. Conversely, this existential property applied to every reached restricted Boolean function, combined with the exact influence telescope, gives FEI with constant K + 2/ln 2. The hereditary quantifier is essential; a property only at the initial function is insufficient.

For any block W, uniform physical exposure gives

    I(f) - E_y I(f|W=y) = sum_{i in W} I_i(f).

The exact entropy decrement is conditional block erasure plus a nonnegative mixing term paid by (2/ln 2) times that same lost influence. A rule choosing W must be measurable from the already revealed physical history; conditioning on an unseen “favorable” input event does not preserve fair branches. Choosing W to be all inputs is tautological.

The exact shared-data multiplexer formula is this same block identity:

    B_W = sum_T R_T H(nu_T),
    M_W = a - sum_T R_T H(r_T).

Here nu_T is a conditional selector-SPECTRAL law, while r_T is a conditional PHYSICAL branch-label law. Then Delta_W H = B_W + M_W and 0 <= M_W <= (2/ln 2) I_W. This interface should be a shared dependency for B04, B06 and B12, preventing the same conditional erasure debt from being advertised as independently paid in different routes.

The stronger existing mismatch/KL bound, fully defined in the companion snippets, identifies a sharper unpaid tree term:

    E sum_v mu_v [log_2(1/mu_v) - D_2(nu_v || q_v)].

Its remaining 3 mu_v/ln 2 term already fits queried influence. This is a useful concrete bridge between B05/B06/B08/B13, but its universal bound remains open.

## 4. Independent analytic verification of B05

Audited original: recovered_git/B05_20261011T193057Z_REPORT.md, SHA-256 4064e379c4ff509a909c8b8d2da07d92e8f15e89a906f0745f5e40b767504a66.

Let delta = 2^(-k), p = 2^(-2k) = delta^2 and d = p delta = delta^3, with k even and at least four. The quadratic bent sign has all Walsh coefficients c_T of magnitude sqrt(delta), including c_empty = sqrt(delta). The two activated Boolean children differ at exactly one residual vertex of their 3k-cube. Consequently their Walsh difference is 2d at EVERY residual index, and e_T,U = d^2 at all 1/d packets. Summing gives the exact disagreement d.

For nonempty data T, the coefficient midpoint is p(c_T-delta), so

    q/e = delta^(-1) - 2 c_T/delta + 2
        = delta^(-1) (1 + O(sqrt(delta))).

The minimum obeys the reported lower bound 1/(4 delta). Empty-data/nonempty-control midpoint p(sqrt(delta)-1-delta), and all-empty midpoint 1+p(sqrt(delta)-1-delta), also give theta=e/q <= 4 delta. These checks use actual physical Boolean children, with no formal spectral-law substitution.

Nonempty-data packets have total mismatch mass (1-delta)d. Applying q h_2(e/q) >= e log_2(q/e) gives

    L >= (1-delta)d(k-2).

The expansion h_2(t) = t[log_2(1/t)+log_2 e+O(t)] yields the sharper nonempty contribution (1-delta)d[k+log_2 e+O(sqrt(delta))]. Empty-data/nonempty-control packets have total mismatch at most delta d and logarithm O(k), hence o(d) entropy. The all-empty packet contributes O(kd^2), also o(d). Thus L/d = k+log_2 e+o(1) is correct.

Since q is a normalized packet law and E_q theta=d,

    V_post = E_q theta^2 - d^2 <= (max theta)d <= 4 delta d.

Every neighbor of the changed residual vertex has common child value +1. Changing that vertex creates one pivotal undirected edge in each residual coordinate, so each child-influence difference is exactly 2d. There are 3k such coordinates; therefore M_inf = 12kd^2.

For finite nonnegative K,A,B,

    (L-Kd-A V_post-B M_inf)/d
       >= (1-delta)(k-2)-K-4A delta-12Bk d -> infinity.

This proves the no-go without the floating checker. The fixed collection of local moment refunds extension is valid when each refund is nonnegative and bounded above by a fixed multiple of theta near zero: every such expected refund is O(d), while L/d grows.

Here L is exactly B_y, the parent's spectral erasure at the chosen selector coordinate. The full system still has ordinary influence of order kp, whereas L is of order kp delta. The report's two child-influence formulas are correct. There is no contradiction with full FEI, and the argument supplies neither an all-coordinate bad family nor a failure of every adaptive stopping tree.

## 5. Source-based controls that should be attached to the relevant packets

The full mandatory suite need not be rerun after every change. Attach the specific control to the statement it attacks.

| Guard | Existing source | Exact consequence |
|---|---|---|
| BENT_SELECTOR | reductions/paper/restrictions.tex, Bent splice | Universal selector-only/all-coordinate entropy-increment payment fails. |
| B05_RARE_REFUNDS | New B05 original report | Fixed-price local variance/moment refunds fail; selected global trees survive. |
| WEIGHTED_TC | reductions/paper/biased.tex, weighted counterexample | Universal alpha TC <= K I fails within weighted thresholds. |
| WEIGHTED_PIVOTAL_CREDIT | Same theorem and following remark | Coefficient-one pivotal credit plus O(I) fails; larger multipliers are not refuted. |
| WEIGHTED_LOCAL_TC | Same file, local TC proposition | Even existential conditional-physical-TC coordinate payment fails; spectral B_i is a different target. |
| FIXED_CONV_PREFIX | recovered_git/brain_route_map.md §3 | Fixed-order signed-convolution relaxations do not suffice. Non-Boolean scope. |
| FIXED_CAP_PREFIX | recovered_git/brain_cyclic_label_obstruction.md, 10:06 clarification | Fixed atom-cap prefixes do not repair the signed-lifetime relaxation. Non-Boolean scope. |
| RAW_CONV_TENSOR | recovered_git/brain_route_map.md §4 | Keep T=H(v/Z)-log_2 Z. Raw L has a genuine Boolean tensor obstruction. |
| OVERLAP_PRODUCT | recovered_git/brain_route_map.md §8.2 | H(fg)<=H(f)+H(g) fails for shared variables; disjoint additivity survives. |

For RAW_CONV_TENSOR, the source uses a normalized reference amplitude b, v_U=(sum_S b_S b_{S xor U})^2, Z=sum_U v_U, L=sum_U v_U log_2(1/v_U), and T=L/Z. The missing -log_2 Z term is essential. Tensor-additivity of T is not a proof of its universal payment.

For B08's fixed positive occurrence reserve, the older route map also records a no-go for every fixed positive coefficient in the specified finite-center potential. A038 correctly asks agents to retrieve the exact current K_occ definition. It should also retrieve that exact rejected reserve before proposing a new fixed coefficient.

## 6. Measurable proof packets and dependency discipline

The 100 listed topics cover useful directions, but phrases such as “derive a nontrivial entropy-weighted inequality,” “find broad structured covers,” and “find the weakest useful hypothesis” do not yet specify a unique finite work product. Each live invocation should freeze one candidate statement, parameter regime, intended implication, and applicable falsifier before sustained work. The first output may legitimately be a precisely formulated candidate and its first unsupported line; repeated renaming of that line is not a new result.

Recommended immediate mathematical packets:

1. B02: compute the entire conditioned posterior residual on a new explicit selector/overlap family, with actual distinct runs and global weights. A variational identity alone is completed bookkeeping.
2. B05/B13: compare full control-first and selector-first trees for the new sparse-bent family, retaining all branch weights, terminal entropy and the single source of logarithmic credit.
3. B06: formulate one constrained, history-measurable block-selection rule, and prove or disprove its hereditary conditional-erasure criterion. The exact block identity itself is already recovered.
4. B07/B16: name an additional full-Booleanity consequence beyond both fixed-prefix no-go families and prove a restricted conditional-entropy consequence; tensor-padding admission remains mandatory.
5. B09: choose one precise replacement for the already failed normalization estimates, and first test all three weighted controls before a general proof.
6. B12: prove a new structural class satisfying the already known disagreement corollary, or a complete collision payment where that corollary degenerates; test bent splice first.
7. B08: retain the exact mismatch/KL rebate and normalized convolution definitions; ask whether a specified global credit pays a specified debt, rather than count positivity of a divergence as progress.

Acceptance must distinguish a new identity, a new restricted theorem, a known identity reproduced, a precise helper disproved, a FEI-equivalent endpoint restated, and an actually closed universal proof. The plan correctly requires complete dependency chains and two substantive independent audits for any claimed full solution.

## 7. Precise source pins

The recovered reductions files are included in the input hash ledger and should be distributed with their exact theorem labels and supporting checks.

The mismatch/KL source is math-open-problems commit fe94de760ee2b47545419a7447b492816bd16045, path proofnet24/P03-fei/runs/2026-09-20/2026-09-20T12-28-55+0300__fei-isospectral-splicing-symmetry-quotient.md, Theorems 3.1–5.1, blob 3421c0cbfd22031554befb962ec92cd0c8bb45b9.

The fixed-convolution-order source at the same commit is proofnet24/P03-fei/continuations/2026-09-20-booleanity-order/REPORT.md, Theorem 2.1 and later strengthened variants, blob 721f6c2216fbca989bbe1e9f48fe7cacdf9832a3.

The normalized convolution source at the same commit is research_pushes/2026-09-30-fei-normalized-convolution-0236z/REPORT.md, blob 43f02ba681df60762b28515540a8f851f95286ba. Its later output-enclosure correction is separately identified in the recovered route map; copying an old rounded “interval” is not a rigorous numerical certificate.

The phase-energy addendum points to math-open-problems commit 0c5ada5a0b8ef28902a444fd190644ebd75cb84f, its boolean-phase-padding-energy archive, reviewed REPORT SHA-256 29de09cee7fcc57e95e881ca1cb3b41176bba421f79405ca3062bee10734f3e6. Its conditional-completion scope guard is at commit 456cb7cd81afe54a7830f2255adbbdec96f971e7, CONDITIONAL_SCOPE_ROOT_REVIEW.md, blob 7ebadc2879039707d61328cbc37eaaf82d20e14b.

These are source locators for mathematical work, not an assertion of fresh external retrieval, native Brain ingestion, formal certification, or a solved conjecture.
