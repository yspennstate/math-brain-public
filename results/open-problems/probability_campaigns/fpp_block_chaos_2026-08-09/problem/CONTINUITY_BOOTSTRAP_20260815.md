# [FALSIFIER RUN 2026-08-15, same session, against section 5's instruction. VERDICT: the
# section-3 conclusion SURVIVES and is now stated more strongly; the REASON I gave for it was
# wrong and is struck. Read section 3bis, which replaces section 3's justification.
# Summary of the run: section 5 told a referee to attack at "can the chaos requirement be
# re-derived with D_{Mn} in the denominator instead of Q_n^4". CRUX 6.3 does re-derive it
# (eps <= D/(16 C B^2), B a per-block increment sup-bound), and CRUX 6d(D6) sharpens it further
# (eps <= D/(4 B^2)). So my premise that the fourth-moment input is irreducibly an ENVELOPE
# quantity is FALSE - 6.1 gives A4 <= B^2 A2, so it factors as occupation-squared times the
# SECOND moment. That sentence in section 5 is struck. But the conclusion does not depend on it:
# in all four accountings the campaign has derived, eps_max is MONOTONE INCREASING in D_n, which
# is what section 3 actually needs. See 3bis for the general reason. chi = 1/3 UNMOVED.]
#
# The two D_n-lower-bound dependencies have DIFFERENT shapes: one is bootstrap-shaped and a
# continuity argument removes it, the other is anti-bootstrap-shaped and no continuity
# argument can. This splits an obstruction the campaign has been treating as single.
# 2026-08-15. STATUS: structural finding + method proposal. One lemma
# proved, one negative structural claim derived, one hypothesis (a base case) NOT supplied.
# chi = 1/3 UNMOVED. Nothing here is a solution. Independent referee owed.

## 0. Provenance, including the correction that produced the result

This note began as a proposal to answer the 08-12 self-referee with a continuity (open-closed)
bootstrap. Running the falsifier on my own proposal - "is the campaign's n^2/log^4 n shortfall
really attributable to the quantity I claim to bootstrap?" - showed it is NOT, and the
correction is the actual content here. The first draft claimed to dissolve "the" wall; it
dissolves one of two, and there is a structural reason it cannot touch the other. That reason
is the finding.

## 1. Two quantities the campaign has been calling one obstruction

Notation as in the CRUX. D_n := Var(T(0,n e_1)); M the engine's scale step; Q_n the
concentration envelope.

  RATIO      R_n := D_{Mn} / D_n            (CRUX 9.8: (L1') holds at the axis blocks with
                                             beta = O(R_n); this is the engine's (L1') input)
  MISMATCH   rho_n := Q_n^2 / D_n           (CRUX 2: the required chaos strength is
                                             eps_n <= 1/(16 C_2 rho_n^2))

CRUX 9.8 closes by saying the program's three routes are "three independent routes into the
same obstruction", the shared ingredient being that both denominators are D_n and the only
unconditional lower bound is Newman-Piza's c log n. That shared ingredient is real. But R and
rho are not the same quantity and they do not behave the same way under the engine, and it is
the behaviour, not the ingredient, that decides whether a bootstrap exists.

Both blow up to ~ n/log^2 n on today's inputs, which is why they have looked interchangeable:
R_n <~ Mn/log^2 n by substituting the free bounds (9.8), and rho_n <~ (n/log n)/(c log n) =
n/log^2 n (section 2). The n^2/log^4 n shortfall in section 2 is rho_n^2 - it is the MISMATCH
squared, not the ratio.

## 2. The engine's self-reference in R is bootstrap-shaped

  (HALVE)  Under package H and (L1') at parameter beta, the refereed engine gives
           D_{Mn} <= (1/2) M D_n, i.e. R_n <= M/2.
  (9.8)    Unconditionally, beta = O(R_n) at the blocks carrying the sums.

Hypothesis and conclusion are statements about the SAME quantity at the SAME scale, and the
conclusion is strictly stronger than the hypothesis needs to be: for any K > M/2,

           R_n <= K   ==>   R_n <= M/2 < K.                                    (*)

That is not circular. It is the exact input to an open-closed argument, and the campaign's two
closed routes (carry a window up the scales; contract a window down the scales) both failed
because they tried to turn (*) into a step-to-step induction in the SCALE variable, where the
self-referee's certification break bites and where only ~log n steps are available to erase a
polynomially large window.

METHOD. Let {nu_t}_{t in [0,1]} be a family of edge-weight laws with nu_1 = nu the target.
Fix K > M/2 and assume:
  (C1) CONTINUITY: for each fixed n, t |-> D_n(t) is continuous on [0,1] and D_n(t) > 0.
  (C2) UNIFORM ENGINE: for every t, the implication (*) holds for nu_t.
  (C3) BASE CASE: R_n(0) <= K for every n.

THEOREM. (C1)+(C2)+(C3) imply R_n(1) <= M/2 for all n, hence telescoping along n = M^k,
Var T(0,n e_1) <= C n^{1 - log_M 2}.

Proof. Fix N; put S_N := {t : R_n(t) <= K for all n <= N}. Nonempty by (C3); closed because
each R_n is continuous (C1) and S_N is a finite intersection of preimages of a closed set;
open because for t in S_N, (C2) gives R_n(t) <= M/2 < K for the finitely many n <= N, and
(C1) supplies a neighbourhood on which R_n <= K still holds. [0,1] is connected, so S_N =
[0,1]; then (C2) at t = 1 gives R_n(1) <= M/2 for n <= N. N was arbitrary and the conclusion
carries no N. []

TWO REMARKS THAT ARE THE POINT.
(a) NOTHING IS CERTIFIED. The bootstrap hypothesis is about the TRUE ratio, never about a
    proved pair (U, L). The self-referee's break - any certifiable beta is U(j+1)/L(j) >=
    Var(X_n)/(c log n) - does not apply, because no step of this argument exhibits a lower
    bound on D_n. The lower bound is supplied by the connectedness of [0,1].
(b) NO STEP BUDGET. The openness modulus may depend on N and degenerate as N grows, at no
    cost, because the conclusion extracted at each fixed N is N-free. Every earlier route died
    on a quantitative step budget (~log n doublings against a polynomially large window); this
    argument has none.
(b') The base point may depend on N: it suffices that for each N there is t_N with R_n(t_N) <=
    K for n <= N, since [t_N, 1] is connected. So (C3) may be met by a REGULARISED model
    approaching the target as the scale window grows.

(C1) IS CHEAP - proved. Let nu_t be supported in [a,b], 0 < a <= b < infinity, given by
quantile coupling w_e(t) = F_t^{-1}(U_e) on common uniforms, with
eta(h) := sup_{|t-t'|<=h} sup_u |F_t^{-1}(u) - F_{t'}^{-1}(u)| -> 0. The straight lattice path
gives X_n(t) <= b n and every path has >= n edges so X_n(t) >= a n; hence any geodesic has at
most (b/a) n edges. Comparing X_n(t) with a geodesic for w(t') and symmetrising,
||X_n(t) - X_n(t')||_infinity <= (b/a) n eta(h) on the coupling space, and both variables are
bounded by b n, so |D_n(t) - D_n(t')| <= (4 b^2/a) n^2 eta(h) -> 0. Positivity holds whenever
nu_t is non-degenerate. The n^2 is harmless by remark (b). []

## 3. The engine's dependence on rho is ANTI-bootstrap-shaped - and this is the finding

Ask the same question of the mismatch. Can an open-closed argument run on the condition
rho_n(t) <= K?

It cannot, and not for a technical reason. The bootstrap needs the engine to return the SAME
quantity, strictly improved. What the engine returns is D_{Mn} <= (1/2) M D_n and, telescoped,
D_n <= C n^{1-eps}: an UPPER bound on D_n. But rho_n = Q_n^2/D_n has D_n in the DENOMINATOR, so
an upper bound on D_n makes every bound on rho_n WORSE, not better. The implication runs

           rho_n <= K   ==>   (engine fires)   ==>   D_n smaller   ==>   rho_n LARGER.

The engine's conclusion degrades its own hypothesis. There is no K for which "rho <= K implies
rho <= K' < K" is delivered, so the openness step - the only step of the bootstrap that carries
mathematical content - has nothing to stand on. This is not "the base case is missing"; it is
that the argument shape does not exist for rho at all.

WHY THIS SPLITS THE OBSTRUCTION. Both R and rho need a variance LOWER bound on today's inputs.
That is what made 9.8 call them the same wall. But:
  - R's requirement is SOFT. It is a self-reference the engine closes on its own, and a
    standard method converts it into a base-case problem without ever proving a lower bound.
  - rho's requirement is HARD. rho_n = O(1) says the concentration envelope sits at the
    fluctuation scale, i.e. D_n >~ Q_n^2. Since D_n <= Q_n^2 always, rho_n = O(1) IS a genuine
    two-sided pinning of D_n - it is H1+H3, "chi exists", and the engine cannot produce it
    because the engine only ever bounds D_n from above.
So the correct map is not three routes into one obstruction. It is: ONE removable circularity
((L1'), the ratio) and ONE irreducible lower bound (rho, the mismatch), which happen to share
an ingredient under today's free bounds and are therefore easy to conflate. The campaign should
stop counting (L1') as evidence for the wall's strength; it is the soft one.

CONSEQUENCE FOR THE SANDWICH FRAMING (iter 51). That note said the wall is a two-legged fixed
point, upper leg = 3b/(L1'), lower leg = Thread B (restricted-min anticoncentration). This note
says which leg a continuity argument can carry: the UPPER leg's own certification, and only
that. The lower leg is rho's, and section 3 shows why no bootstrap reaches it. The sandwich is
not two legs of the same kind.

## 3bis. The real reason, found by running section 5's own falsifier (2026-08-15)

Section 3 argued from the particular shape rho_n = Q_n^2/D_n. That was too narrow, and the
falsifier I named found the narrowness immediately. The campaign has FOUR accountings of the
chaos requirement, not one:

  CRUX 2            eps <= D^2 / (16 C_2 V4),  V4 ~ Q^4        i.e. eps <= 1/(16 C_2 rho^2)
  CRUX 6.1 + 2      V4 <= B^2 A2 <= C M B^2 D                  i.e. eps <= D/(16 C_2 B^2)
  CRUX 6.3          eps <= D / (16 C B^2)
  CRUX 6d (D6)      eps <= D / (4 B^2)                         (the sharpest; the sqrt route is dominated)

where B is a per-block increment sup-bound, deterministic and uniform over blocks. My section-5
premise - that the fourth-moment input is irreducibly an envelope quantity - is false: (6.1) is
pointwise algebra and factors A4 as (occupation sup)^2 times the SECOND moment. Struck.

WHAT SURVIVES, AND WHY IT IS STRONGER. Every one of the four is MONOTONE INCREASING IN D_n. That
is not a coincidence of accounting, and the general reason is one line. Every version of the
halving has the form

      Var(X_{Mn})  <=  kappa A2  +  E(eps, D),

and the conclusion Var(X_{Mn}) <= (1/2) M D_n is extracted by demanding that the chaos-driven
error be beaten by the variance being halved, E(eps, D) <= c M D. Note E may itself carry D -
in 6.3 it does, E = B M sqrt(C D eps) - so "solve for eps and D lands on top" is NOT free and
needs its hypothesis stated:

  PROPOSITION. Let E(eps, D) be strictly increasing and continuous in eps, and suppose it grows
  in D strictly slower than linearly: E(eps, lambda D) <= lambda^theta E(eps, D) for all
  lambda >= 1, with theta < 1 uniform. Then the eps_max solving E(eps, D) = c M D is strictly
  increasing in D.
  Proof. Fix D and lambda > 1. E(eps_max(D), lambda D) <= lambda^theta E(eps_max(D), D) =
  lambda^theta c M D < lambda c M D, so eps_max(D) is strictly admissible at lambda D; since E
  is continuous and strictly increasing in eps, eps_max(lambda D) > eps_max(D). []

  The engine's own conclusion is an UPPER bound on D. So under theta < 1 the engine's output
  tightens its own chaos hypothesis, and no open-closed or bootstrap argument can run on the
  chaos condition.

THE HYPOTHESIS theta < 1 IS LOAD-BEARING, AND SPELLING IT OUT WEAKENS THE CLAIM I FIRST WROTE.
theta is set by how the fourth-moment quantity V4 scales with D:
  - V4 charged at an ENVELOPE scale that does not move when D moves (today's situation: Q comes
    from Kesten/Talagrand concentration and is not tied to any variance lower bound). Then E
    carries no D, theta = 0, and eps_max ~ D^2/V4 is STRICTLY INCREASING in D. Anti-bootstrap.
  - V4 tracking D^2 (the ideal case - BSS have Var = Theta(Q^2), so V4 ~ Q^4 ~ D^2). Then
    theta = 1, the demand is D-FREE, eps_max is a constant. NEUTRAL, not anti-bootstrap.
So the correct statement is the weaker and safer one:

  eps_max is NON-DECREASING in D in every accounting the campaign has derived. Shrinking D never
  LOOSENS the chaos requirement. A bootstrap on the chaos condition is therefore never
  favourable - strictly self-defeating in today's regime, neutral at best in the ideal one.

That is what section 3 needs and all it may claim. "Strictly self-defeating in every case" was
too strong and is withdrawn here.

A SEPARATE CORRECTION, so the B-route is not left looking like the chaos requirement. It is not.
6d(D2) is explicit that BSS control A4 through their tail hypothesis (M2), not through a uniform
pointwise sup-bound; the B-route of 6.1-6.3 is a valid but LOSSY alternative accounting (6b.2:
tight only for an adversarial resampling), and 6d(D1) shows it can never beat eps <~ D/n^2. So
eps_max = D/(4 B^2) is the requirement OF THAT ROUTE, not of the engine. What the B-route does
establish, and what is worth carrying, is a floor that no variance lower bound can lift: 6d(D1)
forces B = Theta(n), and even the best conceivable B ~ W = n^{2/3} (6d D3) leaves
B^2/D >= n^{4/3}/n^{2/3} = n^{2/3} at IDEAL D ~ n^{2/3}, i.e. eps <= n^{-2/3}. My formula
reproduces D3's "still short of a constant by n^{2/3}" from scratch rather than copying it, which
is the cross-check I ran before believing any of this. Read that as: granting H1+H3 in full does
not rescue the pointwise-B accounting - which is a fact about that accounting, and NOT evidence
against the conditional theorem P-b, whose route through (M2) is untouched by it.

Read plainly: chaos has to beat the variance, and a smaller variance is a harder target. An
argument that assumes the chaos condition in order to shrink the variance has assumed something
its own conclusion makes harder to satisfy. That is the anti-bootstrap shape, and it is a
property of what the condition MEANS rather than of how V4 happens to be bounded. Section 3's
conclusion therefore stands on this, not on rho's particular form.

CROSS-CHECK against the campaign's own arithmetic, which the proposition must reproduce. At the
ideal exponents (D ~ n^{2/3}, B ~ Q ~ n^{1/3}) 6d gives eps_max = Theta(1) - matching CRUX 2's
"their Theorem 2.1 gives rho = Theta(1), so a constant-order chaos estimate suffices". At today's
unconditional inputs (D >= c log n, B = Theta(n)) it gives eps_max >~ log n/n^2 - matching 6.4's
concession that the honest number is log n/n^2, worse by log^3 n than section 2's log^4 n/n^2.
Both endpoints reproduce, so the proposition is consistent with the numbers already on file.

A DEBT THIS RUN CLEARS, recorded because it nearly cost more. Sections 6, 6b, 6c were four fires
of work, withdrawn as a contribution by their referee (6d) while their ALGEBRA was confirmed. I
reached them only by following the falsifier I had written down; had I trusted my own summary of
section 2 I would have published a reason that 6d had already struck ("SECTION 2 MADE NO ERROR").
Two specific corrections I inherit rather than rediscover: B = Theta(n) is FORCED on Z^2 (6d D1's
explicit witness - weights a inside the block and b outside, straight-path geodesic, resampling to
all-b moves the passage time by exactly (b-a)n, so (6.2) is TIGHT), and even the best conceivable
occupation bound B ~ W = n^{2/3} leaves eps <= n^{-2/3}, short of a constant by n^{2/3} (6d D3).
So the numerator side of eps_max is closed too: B cannot be improved past W, and W is not enough.

## 4. What is missing, said plainly

GAP 1 - THE BASE CASE (C3), for the R-bootstrap. Not supplied. Families ruled out, recorded so
they are not re-walked:
  - Small noise w = 1 + delta xi, base at delta = 0. FAILS: D_n(0) = 0, so R_n(0) = 0/0 and
    (C1)'s positivity dies; the rescaled delta -> 0 limit is first passage over the monotone
    paths of the unperturbed problem, itself conjecturally KPZ and unsolved.
  - Large spread / heavy tails. No regime with a controlled RATIO; heavy right tails are
    avoided by the minimum and mass near the essential infimum drives the model toward
    critical percolation.
  - Interpolate to the rotationally invariant model of BSS 2604.01214. FAILS: not a
    one-parameter family of lattice weight laws, and H does not vary continuously along any
    path I can write.
  - Interpolate to solvable LPP. FAILS: different model class; no path inside FPP reaches it.
  - Bernoulli weights through p_c. FAILS: changes the fluctuation behaviour, supplies no bound
    on D_{Mn}/D_n.
  STRONGEST CASE THAT GAP 1 IS ONLY THE PROBLEM MOVED: the base case is "for all n at one t",
  the target is "for all n at t = 1". Honest answer: the gain is one free choice of model
  inside a connected family, plus remark (b')'s drifting base point. Whether that is enough
  freedom I do not know, and this note does not claim it is.

GAP 2 - rho, i.e. H1+H3. Untouched, and section 3 says structurally untouchable by this method.
This is the binding constraint and it is exactly where the campaign already had it. The
practical value of section 2 is therefore NOT that it brings the theorem closer; it is that it
removes (L1') from the list of things a future attempt must solve, so the search narrows to
one target instead of three.

## 4bis. The base case identified (2026-08-15, fire 3). It is constant-A doubling, which this
## campaign already showed is wall-equivalent - so the route's whole content is TRANSPORT.
## That is a smaller claim than section 2 hoped for, and a sharper one than section 4 left it.

(C3) asks for R_n(t_0) = D_{Mn}(t_0)/D_n(t_0) <= K, for all n, at one parameter value. With M = 2
that is verbatim the statement

    Var(X_{2n}) <= A Var(X_n)   with a CONSTANT A,

i.e. constant-A variance doubling for the base model. Fire 89's note
(DOUBLING_IS_NOT_A_SIDE_DOOR_20260812.md) already established what that costs: doubling is not a
side door, it is wall-equivalent. Its argument, restated in the present notation: given doubling
with constant A and the maintain-up hypothesis R(j) <= K, the pre-halving bound U_raw(j+1) <=
A U(j) certifies beta = U_raw(j+1)/L(j) <= A K = O(1), the refereed halving fires, and the
induction the campaign proved "does not start" starts. So doubling at a model already delivers the
halving AT THAT MODEL, with no continuity argument anywhere.

[CLARIFICATION to fire 89's argument, which strengthens it and is exactly the distinction this
note is about. Routing through U and L is unnecessary. 9.8 says beta = O(D_{Mn}/D_n) - the TRUE
ratio - and constant-A doubling IS a bound on that true ratio. So doubling gives beta <= CA = O(1)
at every scale directly, with no window, no certified pair, and no induction to start. Fire 89
reached the right conclusion through a certified window it did not need; the cleaner statement is
that doubling and the (L1') premise are the same object seen twice.]

CONSEQUENCE, stated against my own section 2. The continuity route does not weaken the base case
into something softer than the wall. Its entire marginal content is TRANSPORT: it converts "the
wall is solved at some model in the family" into "the wall is solved at the target". Where the wall
is solved nowhere in the family, it adds nothing. Section 4's hope - that "one free choice of
model" might be enough freedom - is answered: the free choice buys transport, not difficulty.

WHAT TRANSPORT IS NEVERTHELESS WORTH, and this is the fire's positive result. The family can be

  QUANTILE INTERPOLATION. For non-degenerate laws nu_0, nu_1 on [a,b] with 0 < a <= b < infinity,
  put F_t^{-1} := (1-t) F_0^{-1} + t F_1^{-1}. Each F_t^{-1} is non-decreasing, so it is the
  quantile function of a law on [a,b]; non-degeneracy is preserved (if a convex combination of two
  non-decreasing functions were constant, F_1^{-1} would have to be affine-DEcreasing in F_0^{-1},
  impossible for two non-decreasing non-constant functions); and section 4's continuity modulus is
  immediate and linear,
      eta(h) = sup_{|t-t'|<=h} sup_u |F_t^{-1}(u) - F_{t'}^{-1}(u)| <= h (b - a).
  So (C1) holds along ANY such segment, with no hypothesis beyond bounded non-degenerate weights.

  FALSIFIER RUN on the non-degeneracy step, because positivity of D_n(t) is what (C1) needs and a
  collapse at an interior t would make the family unusable. Swept t on a 401-point grid for four
  adversarial legal pairs (uniform vs two-atom; steep u^8 vs nearly flat; step vs micro-step of
  size 1e-9; convex vs concave), plus an ILLEGAL decreasing mate as a POSITIVE CONTROL so a clean
  sweep would mean something. Result: every legal pair stayed strictly positive with no interior
  dip below its own endpoints, and the illegal control collapsed to exactly 0.000e+00 at t = 1/2.
  The detector can print the fatal outcome and did not print it for a legal pair. (My first pass
  compared against a fixed 1e-12 floor and flagged two pairs whose ENDPOINTS I had built to be
  nearly degenerate - a bug in my verdict logic, not a finding; the comparison has to be against
  the endpoint variances, since the claim is about interior collapse.)

  [NOVELTY DEBT PAID, 2026-08-15 fire 4, and it DOWNGRADES the principle below. Literature pass
  run as owed. Verdict: NEW IN THIS SPECIFIC FORM, NOT NEW IN KIND - the same verdict iter 177
  returned on P-a, and for the same reason. Two findings, both against me:
   (i) Chatterjee, "The universal relation between scaling exponents in first-passage percolation"
       (Annals of Math 177 (2013); arXiv 1105.4566) proves chi = 2 xi - 1 and states the relation
       is universal - independent of dimension AND of the law of the weights under moment
       assumptions. Distribution-independence of FPP exponents is therefore an established theme,
       not an observation this note introduces.
   (ii) Worse for the principle's practical value: Damron-Hanson-Sosoe (PTRF; arXiv 1306.1197)
       prove sublinear variance for GENERAL distributions directly - absolutely continuous,
       discrete, singular continuous and mixtures, under only 2 + log moments - by replacing BKS's
       randomised starting point with a geometric average. So the field obtains distributional
       weaker than the bounded [a,b] support my continuity lemma needs. My framework is NARROWER
  WHAT THIS LEAVES OF IT: the conditional implication below is still correctly derived, and the
  not make it vacuous. But it must never be presented as a new idea about universality, and the
  honest one-line summary is: if the n^{1-eps} bound is ever proved for one bounded law, the
  field's existing machinery would very likely give it for all laws anyway, without this.]

  nu_0 on [a,b], and the engine's implication (*) holds uniformly along the segment from nu_0 to
  nu_1, then Var_{nu_1} T(0, n e_1) = O(n^{1 - log 2 / log M}).
  Since the segment exists between any two such laws, the conclusion is ALL-OR-NOTHING on that
  class: a proof of doubling for a single convenient bounded non-degenerate weight law would give
  sublinear variance for EVERY bounded non-degenerate weight law.

  SCOPE the statement needs and section 2 did not carry: the engine's own hypotheses first hold
  above a threshold l_0 (the campaign records l_0 ~ 1e18 at c = 0.5, ~1e80 at small c). So the
  open-closed set must be S_N = {t : R_n(t) <= K for all l_0 <= n <= N}, the base case is required
  only for n >= l_0, and the telescoped constant depends on l_0. Nothing else changes.

only model known to have the two-sided grip that doubling expresses is the rotationally invariant
continuum model of BSS 2604.01214, whose Theorem 2.1 has rho = Theta(1) - envelope AT the
fluctuation scale. That model is not a member of any quantile-interpolation family of iid bounded
weight laws on Z^2, so the segment that would transport it does not exist. And (C2) is worse here
than anywhere else in this note: the package includes pointwise curvature of the limit shape, which
varies with the weight law and is unknown for essentially every lattice law, so "uniformly along
the segment" is asking for it everywhere at once.

NET FOR THE ROUTE: section 2's method is correct and its certification argument stands, but its
base case is the wall wearing a different model's clothes. What survives as a usable statement is
proof would have to start (any one law) rather than how to start it. chi = 1/3 UNMOVED.

## 5. Disposition

NEW: the split of R from rho by bootstrap shape; the observation that (*) is bootstrap-shaped
rather than circular; the proof that (C1) is free for bounded weights; the derivation that no
open-closed argument can run on rho because the engine's output degrades rho's hypothesis; and
the consequent correction to 9.8's "three independent routes into the same obstruction".

NOT CLAIMED: any progress on chi. Section 2's theorem is conditional on (C1)-(C3), of which
(C1) is proved, the implication inside (C2) is refereed material, and (C3) is absent. Gap 2 is
untouched. chi = 1/3 is exactly where it was.

FALSIFIER FOR A REFEREE TO RUN FIRST: if the engine's chaos requirement can be re-derived in a
form whose denominator is D_{Mn} rather than Q_n^2 - i.e. if rho can be replaced by a ratio of
variances at two scales - then section 3's anti-monotonicity claim collapses and rho becomes
bootstrap-shaped too. I checked CRUX 2's derivation (eps_n <= D_n^2/(16 C_2 V4_n), V4_n ~ Q_n^4)
and the fourth-moment input is an ENVELOPE quantity, not a variance at another scale, so I
believe the claim holds; but that is the single place it would break, and it should be attacked
there and nowhere else.

Related: CRUX_iteration_arithmetic.md 2 (rho and the n^2/log^4 n shortfall) and 9.8 (the ratio
identity, and the "same obstruction" sentence this note corrects);
wall_two_sided_sandwich_SELF_REFEREE_20260812.md (the certification break that remark (a)
answers); wall_two_sided_sandwich_note_20260812.md (the two-leg framing section 3 refines);
D_lowerbound_blocktime_attempt_20260812.md (Thread B = the lower leg = rho's side).
