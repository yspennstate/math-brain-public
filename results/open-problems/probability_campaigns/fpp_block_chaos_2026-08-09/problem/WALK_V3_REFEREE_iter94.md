# Hostile referee report, iter 94: the I3 entropy walk (iter 86) and the I8 v3-in-place document (iter 82)

VERDICTS FIRST.
- WALK (I3_entropy_route_walk_iter86.md): REPAIRABLE. One real defect, in S8: the variational
  parameter is set to a = r, which shrinks the usable lambda-window to width ~ 1/sqrt(r) and
  collapses the Gaussian t-range to a CONSTANT interval - the claimed range t in (0, C2 sqrt(r))
  is NOT delivered by the walk's own constant chase. The repair is one line (a = constant, fed by
  the same Claim 4), restores the claimed range with explicit constants, and costs no exponent.
  A second, smaller gap: the consumer's union bound runs over ALL wall-pair distances r <= R, and
  the walk addresses only r ~ n^kappa; the small-r pairs need a one-line deterministic branch.
  Everything else survives attack, and the fidelity caveat (W4) is now CLOSED against a clean
  source: the BLM lemma form the walk consumes is verbatim correct.
- V3 DOCUMENT (I8_from_curvature_v2_iter82.md, v3-in-place): REPAIRABLE, with one MAJOR. The new
  class window [0, C_K d(K s')] is SOLID where the sketch referee's fixed-point form was
  PUNCTURED: it admits members with far-depth strictly between 0 and the wandering quantile,
  whose far child is priced by an (H-wand) instance the re-scoped hypothesis does not supply
  (and whose touching probability is plausibly order one). The class-sup recursion fails on that
  dead band as written. Repair: restore the puncture {0} u [sigma W_{s'/K}, C_K d(K s')] and give
  D = 0 members the two-anchored-children step; branching 2 against 1/sqrt(K) still contracts.
  No exponent cost. GEOM re-wiring, touching account, and the consequence chain pass; the
  patchwork carries four real tag-inconsistencies listed under V4, one of which is the tail
  constant c missing from the very definition of sigma that the banner claims fixed.

Conventions. READ = quoted from a named file/source. DERIVED = re-derived here from scratch.
Weights in [a,b]; where the survey's variational parameter collides with the weight floor a, the
weight floor is written a_w. Sources fetched this session: Damron-Hanson-Sosoe, "Subdiffusive
concentration in first-passage percolation" (arXiv:1401.0917), full text extracted to
scratchpad DHS_1401.0917_text.txt; Boucheron's Missillac 2014 slides (dornsife.usc.edu), extracted
to BOUCHERON_SLIDES_text.txt. The ADH survey extraction pages 46-51 were re-read and are LEGIBLE
at the relevant displays (the walk's "mostly ?" fidelity fear does not afflict pages 46-51).

--------------------------------------------------------------------------------------------------
## PART I. THE WALK

### W1. S3 tensorization over the subgraph-indexed product: PASSES (DERIVED)

Tensorization of entropy: for a product measure mu = tensor_i mu_i over ANY finite index set and
f >= 0, Ent_mu f <= Sum_i E[Ent_i f], with Ent_i = entropy in coordinate i, all other coordinates
held fixed. I re-derived it via the variational formula (Ent f = sup{E fg : E e^g <= 1}) plus the
standard chain/Han decomposition; nothing in the proof sees the index set's meaning. Three points
- The product here is tensor over edges of B* cap H. A product over a subgraph's edge set is a
  product measure like any other; the conditioning convention (edge i resampled, all other
  H-edges fixed) is the same convention DHS use over the full lattice (their Proposition 2.7,
  READ from the fetched text, applied with "Ent_{e_k}" in exactly this sense).
- T_+ is a measurable function of the B* cap H coordinates ALONE, deterministically: T_+ <= b r
  via the wall segment, while any H-path leaving the box of l1-radius 2(b/a_w) r about the pair
  has >= 2(b/a_w) r edges, hence time > b r. So the localized T_+ equals the global T_+ pointwise
  and the finite-product entropy is the right object. (This also makes the walk's finite sum
  cleaner than the survey's infinite enumeration; no convergence caveat needed.)
- Entropy of a function of a sub-collection with respect to the full product equals its entropy
  with respect to the sub-product (entropy depends only on the law). No leakage.

### W2. S5 optimizer combinatorics under non-uniqueness: PASSES (DERIVED)

Claim attacked: (T_+^{i,'} - T_+)^+ > 0 forces e_i in G_+ := intersection of ALL H-geodesics.
Re-derivation in H: suppose T'_i > T_+ and some H-geodesic gamma avoids e_i. All of gamma's edge
weights are unchanged by the resample, so T'_i <= T'(gamma) = T(gamma) = T_+, contradiction. The
inequality T'_i <= T'(gamma) uses ONLY that gamma is an H-path (the resampled H-passage time is an
inf over the same H-path set); the equality T(gamma) = T_+ uses ONLY that gamma is A minimizer in
the original weights. Uniqueness is never touched; the quantifier order ("some geodesic avoids
e_i") is exactly what intersection-membership negates. Checked against the clean DHS text (READ):
their Lemma 3.1 usage "(T_z^{(k)} - T_z)^+ <= t'_{e_k} 1{e_k in Geo(z,z+x)}" is the same one-
directional implication. Two H-specific checks:
- Existence of a minimizer: the localized problem is a minimum over the finitely many self-
  avoiding H-paths in B*; attained always. No selection needed for the implication; G_+ and #G_+
  are measurable in the finite setting (e in G_+ iff the e-avoiding H-passage time exceeds T_+).
  The corner note's fixed-measurable-selection convention (C1 section 0, READ) is compatible and
  idle here.
- Ambient graph: every object quantified over (gamma, T'_i, G_+) lives in B* cap H; no edge
  outside H is ever referenced. The walk's "H-SAFE VERBATIM" is accurate.
Also S6 (DERIVED): if T'_i > T_+ then e_i lies on every original geodesic gamma, so
T'_i <= T'(gamma) = T_+ - tau_{e_i} + tau'_{e_i} <= T_+ + tau'_{e_i} <= T_+ + b (weights >= 0,
<= b). And tau'_{e_i} is independent of (e^{lambda T_+}, 1{e_i in G_+}) - both are functions of
the original weights - which is what the decoupling step consumes. No defect.

### W3. S8 constant chase: DEFECT FOUND - the claimed t-range is not delivered (DERIVED)

The pieces that CHECK:
- E q(lambda tau') <= 2 lambda^2 b^2 for lambda <= 1/b: for x in [0,1], e^x - 1 <= (e-1) x, so
  q(x) = x(e^x - 1) <= (e-1) x^2 < 2 x^2; with x = lambda tau' <= lambda b <= 1 this gives
  q <= 2 lambda^2 tau'^2 <= 2 lambda^2 b^2. CORRECT as displayed.
- The window arithmetic: with a = r, a E q <= 2 lambda^2 b^2 r < c^2 < 1 exactly on
  lambda in (0, c/(b sqrt(2r))). CORRECT as displayed.
- The entropy form: Ent e^{lambda T_+} <= [aEq/(1-aEq)] log E exp(#G_+/a) E e^{lambda T_+} is the
  survey's display (READ, ADH p.49, legible), and with a = r, log E exp(#G_+/r) <= b/a_w from
  Claim 4. So Ent <= C0 r lambda^2 E e^{lambda T_+} with C0 = 2 b^3 / (a_w (1 - c^2)) - but ONLY
  on the shrinking window lambda in (0, c/(b sqrt(2r))).
The step that FAILS: "exactly the range that yields the Gaussian upper tail ... FOR t in
(0, C2 sqrt(r))". Herbst gives psi_c(lambda) <= C0 r lambda^2 on the same window. Chernoff:
P(T_+ - E T_+ >= t sqrt(r)) <= exp(C0 r lambda^2 - lambda t sqrt(r)); the optimizer
lambda* = t/(2 C0 sqrt(r)) is admissible iff t <= 2 C0 c/(sqrt(2) b) - a CONSTANT, independent
of r. So the walk as written proves the Gaussian bound only on a bounded t-interval, plus (at
lambda = window edge) exp(-c t/(sqrt2 b)) beyond it. At t = eps sqrt(r) the walk's own machinery
yields exp(-c' eps sqrt(r)), NOT the claimed exp(-C1 eps^2 r). The claim "the same t-range
restriction as the survey's Theorem 3.11" is false as derived: the survey's (3.13) has the
lambda-window (0, C) CONSTANT (READ, p.47, legible), which is precisely what a = r destroys.
THE REPAIR (DERIVED, explicit, zero exponent cost). Choose a = a0 constant (say a0 = 1). Claim 4
gives, deterministically, log E exp(#G_+/a0) <= (b/a_w) r / a0 - the walk's "nothing random"
point survives untouched; this replaces the survey's Lemma 3.13 (whose role is exactly a linear-
in-r log-moment at FIXED a; READ, p.50). Then a0 E q <= 2 a0 lambda^2 b^2 <= 1/2 for
lambda <= 1/(2b sqrt(a0)) - a CONSTANT window - and
    Ent e^{lambda T_+} <= [a0Eq/(1-a0Eq)] (b/a_w)(r/a0) E e^{lambda T_+}
                       <= 4 lambda^2 b^3 (r/a_w) E e^{lambda T_+},  lambda in (0, 1/(2b)).
Herbst + Chernoff: P(T_+ - E T_+ >= t sqrt(r)) <= exp(-a_w t^2 / (16 b^3)) for
t in (0, 4 b^2 sqrt(r)/a_w). This is the claimed statement with C1 = a_w/(16 b^3),
C2 = 4 b^2/a_w. The DHS appendix's own assembly (READ from the fetched text: parameter p chosen
as a constant "p = alpha_1 from (1.12)", window "lambda in [0, lambda'']" constant, conclusion
Ent <= C50 lambda^2 ||x||_1 E e^{lambda F_m} for lambda in [0, C51]) confirms the constant-
parameter architecture is the intended one. Verdict: S8 defective as printed; statement-level
repair; after repair S8-S9 are sound.

### W4. FIDELITY CHECK against a clean source: FETCH SUCCEEDED - the lemma form is VERBATIM RIGHT

Fetched and extracted (this session): DHS arXiv:1401.0917, Appendix A.1, quoting BLM [5, Theorem
6.15] as their Theorem A.1 (READ, clean text):
    "Let X be a random variable and let X' be an independent copy. Then for lambda in R,
     Ent e^{lambda X} <= E[ e^{lambda X} q(lambda (X' - X)_+) ]   where q(x) = x(e^x - 1)."
This is EXACTLY the form the walk's S4 consumes: increment direction (resampled minus original)^+,
q(x) = x(e^x - 1), all real lambda. The survey extraction's Lemma 3.12 display carries a t/lambda
notational mismatch ("Ent e^{tX} <= E[e^{tX} q(lambda (X'-X)+)]") - now resolved as garbling or a
survey typo; the DHS statement is the clean one and matches the walk. Two corroborations:
- (DERIVED) The BLM book form is sometimes quoted with tau(-lambda (Z - Z'_i)_+). I checked the
  two forms are the SAME inequality: on the event Z' > Z, exchangeability of (Z, Z') turns
  E[e^{lambda Z} tau(-lambda (Z-Z')_+)] into E[e^{lambda Z'} tau(-u)] with u = lambda(Z'-Z) > 0,
  and e^{lambda Z'} tau(-u) = e^{lambda Z} e^u u (1 - e^{-u}) = e^{lambda Z} q(u). So whichever
  way BLM print 6.15, the DHS/survey/walk form is an exact rewrite. No direction trap exists.
- The Boucheron slides (fetched) use psi(x) = x(e^x - 1) with the same monotone-on-R+ property
  the walk's S6 consumption needs (q nondecreasing on x >= 0: q' = e^x - 1 + x e^x >= 0).
The walk's SOURCE-FIDELITY caveat can be closed on both counts it named: the lemma form (above)
and the t-range structure of Theorem 3.11 (t in (0, C2 sqrt(||x||_1)); legible at p.47 of the
extraction and consistent with DHS Theorem A.2's constant lambda-window). What the clean sources
do NOT rescue is the walk's own a = r assembly (W3): DHS/survey both use a constant parameter.

### W5. Lower-tail non-consumption: CONFIRMED (READ against C1 section 3, then swept)

The corner note's cost formula (C1 iter60 section 3, READ) consumes exactly two tails:
P(T(p,q) < E T - z S(r)) - the FREE time's LOWER tail (input I2, published) - and
P(T_+(p,q) > E T_+ + z S_+(r)) - the CONFINED time's UPPER tail (input I3). The decomposition
T_+ - T = [T_+ - E T_+] + [E T - T] + MEANGAP makes the direction assignment structural, not
incidental. I swept the rest of the note for any other T_+ tail consumption: Claim 6 uses
Var(T_+) via Efron-Stein (a variance, not a tail); the Splitting Lemma (6.6.2) and P2 forms are
expectations only; section 9's negative results consume nothing downstream; the union bound in
section 3 re-uses the same two tails. P(T_+ < E T_+ - z) appears NOWHERE. The walk's claim that
the lower tail of T_+ is never consumed is TRUE, and its non-coverage costs nothing. PASSES.

### W6. Range coverage at every consumed scale: PREMISE PARTLY FALSE; ONE REAL GAP; CLOSED BY W3'S REPAIR

Two corrections to the attack's premise, then the finding.
- The v3 recursion does NOT consume I3 at the scales r_j = l/K^j. Sections 2-5 of the v3 document
  price segment MEANS (linearity of expectation across the chain) using (H-curv), (H-wand),
  (P-Alex) only; no passage-time concentration enters the A_+ proof at any scale, including
  r0 = l^c. The multi-scale random input there is (H-wand)'s touching tail (see V3 below). So
  there is no I3 range check to run against the recursion: nothing is consumed.
- The place I3 IS consumed at many scales is the CORNER note's union bound: pairs at ALL
  distances r <= R = 5(b/a_w) h, each needing the upper tail at deviation z S_+(r) = n^delta
  sqrt(r) at its OWN r (the monotone-in-r evaluation at R only weakens thresholds).
The gap: for r < n^{2 delta}/C2^2 the deviation n^delta exits the Gaussian range (0, C2 sqrt(r)),
and the walk's S9 checks only r ~ n^kappa. Closure (DERIVED): (i) for r < n^{2delta}/(b-a_w)^2
the deviation exceeds the deterministic ceiling T_+ - E T_+ <= (b - a_w) r, so the probability
is ZERO; (ii) with the W3-repaired constant C2 = 4 b^2/a_w one has C2 > b - a_w ALWAYS
(4b^2 > a_w(b - a_w)), so ranges (i) and the Gaussian range overlap and cover every r >= 1
jointly - no middle band remains, and the exponential branch is not even needed. The walk owes
one sentence stating branch (i) and widening S9 from "r ~ n^kappa" to "all r <= R". With the
unrepaired a = r version the coverage would instead need the exponential branch exp(-c n^delta)
(theta = 1 in the consumer's exp(-c z^theta)) - so even the broken walk feeds the consumer, but
only by an argument the walk never states. After the W3 repair plus the one sentence: COVERED at
every consumed scale.

### Walk: what survives, and the repair bill

S1, S2, S3, S5, S6, S7, S10 pass re-derivation (S7's "nothing random" point is right and is
exactly what makes the a = constant repair free). S4 is verbatim-verified against a clean source.
Defects: (D-W1) S8's a = r collapses the Gaussian t-range to a constant interval; repair a = a0
constant, explicit constants above; no exponent cost. (D-W2) S9 covers only the top scale of the
consumer's union bound; repair is the deterministic-zero branch sentence; no cost. With both,
I3's status claim ("PROVED for bounded weights via the entropy route, QV bridge bypassed")
becomes deliverable as stated. VERDICT: REPAIRABLE.

--------------------------------------------------------------------------------------------------
## PART II. THE V3 DOCUMENT

### V1. The class window: MAJOR DEFECT - the fix over-shot and soldered a dead band into the class

What was checked and PASSES (DERIVED):
- Height nesting is exact: child 0's height s'/K, for s' in [s/2, s], lands exactly in class
  P(s/K)'s [s/(2K), s/K]. No drift at all in the height coordinate.
- Child 0's far-depth containment: the recursing child's far-depth is d(s) (v3's constant-depth
  chain; NOT the sketch referee's on-chord chain, see below); the child's window upper edge is
  C_K d(K s'/K) = C_K d(s'), and d(s)/d(s') = (s/s')^xi <= 2^xi = 1.68 <= C_K = 3.019. Stable
  for every s' in [s/2, s], worst case s' = s/2. The root D = 0 is contained. So the SOLID
  window is step-stable in the direction v3 built it for.
- The fixed-point identity itself: C_K K^{xi-1} + 1 = C_K iff C_K = 1/(1 - K^{xi-1}); at K = 5,
  xi = 3/4: 5^{-1/4} = 0.6687, C_K = 3.0185, C_K - 1 = 2.019. Arithmetic as printed.
- Against the instructed source (iter74 section 1, READ): the fixed point there is for the
  ON-CHORD chain (child far-depth D/K + d'), where C_K is exact. v3's chain is the CONSTANT-
  DEPTH variant (iter74 attack B's "even that variant survives" case), where the recursing
  child's far-depth is d(s) with no D/K term, and ANY constant >= 2^xi works. C_K = 3.019 is
  therefore sufficient-but-vestigial in v3's architecture; with the slope lemma retired, nothing
  consumes its exact value. Not a defect; worth a sentence in v4.
What FAILS (DERIVED): the sketch referee's window was PUNCTURED - far-depth in
{0} u [sigma W_{r/K}, C_K sigma W_r] - and the puncture was load-bearing: it is what kept every
far child's near-wall endpoint at or above the wandering quantile, so that "bulk-typed, priced
with (H-wand) at its own scale" made sense. v3 replaced it with the SOLID window
[0, C_K d(K s')] ("admits the root (D = 0) as an ordinary member"), thereby admitting members
with far-depth D in the dead band (0, sigma W_{s'/K}). For such a member the far child
((d(s), (K-1)s'/K) -> (D, s')) has an endpoint at depth D below the quantile:
- Its touching account needs P(free geodesic exits H) <= l^{-A}. Exit requires wall-ward
  deviation >= the chord clearance, whose MINIMUM along the segment is ~ D. For D = O(1) a fixed
  finite pattern of weights near the far endpoint forces the free geodesic through x = -1 with
  probability bounded below (two support points of the weight law suffice), so P(touch) is order
  ONE, and the touching term is order s' - linear, not l^{-A} times crude.
- Independently of that estimate, the consumed instance is OUTSIDE the re-scoped (H-wand), which
  covers "endpoints at depths in [d(r)-range, d(K r)-range]" - depth D ~ 0 is not in that range.
  So the step consumes a hypothesis instance the ledger does not supply. This is the same class
  of error as the [V2REF] statement-MAJOR (priced pairs outside the stated hypothesis), recreated
  by the v3 repair itself.
- The D = 0 case is also mis-typed below the root: a D = 0 member's far child has its far end ON
  the wall - a reversed anchored pair, in class at scale s/K - so its step is
  f(s) <= 2 f(s/K) + (K-2) bulk + GEOM, branching TWO. Section 2's "Two spines total, branching
  one thereafter" and section 5's "No branching factor exists" are false for the class-sup
  recursion as soon as D = 0 is "an ordinary member" at every scale. (The visited tree - root
  plus two spines with far-depths d(scale) - never enters the dead band and never branches; the
  defect is in the sup the recursion is stated over, which is exactly where a recursion must be
  airtight.)
THE REPAIR (DERIVED, no exponent cost): far-depth window {0} u [sigma W_{s'/K}, C_K d(K s')].
Step stability re-checked: child 0's far-depth d(s) = sigma W_{s/K} >= sigma W_{s'/K^2} (the
child's own lower edge, since s >= s'/K trivially) and <= C_K d(s') (above); visited spine
members sit in the upper band; the root and any D = 0 member take the two-anchored-children
step, giving worst-case branching 2 with per-level forcing ratio 2/sqrt(K) = 0.894 < 1 at K = 5
- the geometric sum survives, constants only (this is iter74's own 2^J-is-safe remark, reused).
Alternatively: drop {0} below the top scale and treat the root separately, keeping branching 1;
either variant closes V1. VERDICT: real MAJOR, statement-level repair, no exponent moves.

### V2. GEOM re-wiring: PASSES; the delta-range check passes but is OWED IN TEXT (DERIVED)

- Telescoping: (d(s), s'/K) + (K-2)(0, s'/K) + (D - d(s), s'/K) = (D, s'). Exact; and the
  leftover K g((0, s'/K)) - g((D, s')) = g((0,s')) - g((D,s')) <= 0 by evenness+convexity of g
  in the depth coordinate, so dropping it is legitimate. GEOM <= the two first differences at
  the axis, as claimed.
- Chordal conversion constant: g((o, h)) - g((0, h)) = h [u(o/h) - u(0)] <= h c'_+ (o/h)^2
  = c'_+ o^2/h for o/h <= delta, with c'_+ = c_+ + g(e_2)/2 + o(1) exactly per iter74's (3a)
  conversion (READ). With h = s'/K this is the displayed C c_+ offset^2 K/s'. Verified.
- Offsets: d(s) <= 2^xi d(s') and |D - d(s)| <= max(D, d(s)) <= C_K d(K s') (window + 2^xi <=
  C_K + monotonicity of d). Verified as displayed.
- The display's K-power: with d(r) := sigma W_{r/K}, the tight bound is C_K^2 sigma^2 K
  (s')^{2xi-1}; v3 prints K^{1+2xi}, which is what one gets reading d(K s') = sigma (K s')^xi.
  At K = 5, xi = 3/4: K^{2.5} = 55.9 >= C_K^2 K = 45.6, so the printed display is a valid (slack)
  upper bound; the sqrt(s) (log l)^{2/theta} conclusion follows either way at xi <= 3/4. Note
  the mismatch of conventions, no action beyond a sentence.
- THE DELTA-RANGE (the attack's core): (H-curv) needs offset/height <= delta. Ratios:
  child-0 offset ratio K d(s)/s' <= 2^xi sigma K^{1-xi} (s')^{xi-1}; far-child offset ratio
  <= C_K sigma K (s')^{xi-1}. Both are maximized at the SMALLEST height, s' ~ r0 = l^c:
  max ratio ~ C_K (A log l / c)^{1/theta} K l^{-c(1-xi)} = polylog x l^{-c/4} -> 0. So the
  ratios are inside ANY fixed delta for l >= l_0(delta, c, theta, K, A), at every scale
  including the last. PASSES - but no sentence in the document discharges this side condition;
  the o(1) tilt claims cover the far child's chord tilt, not the first-difference ratios
  explicitly. One owed sentence, no cost.

### V3. Touching account with the tail constant restored: PASSES (DERIVED)

- Quantile: P(dev >= sigma W) <= C exp(-c sigma^theta) = l^{-A} requires
  sigma = (A log l / c)^{1/theta}; v3 section 3's restored form is right (the leading constant C
  costs an additive log C/c inside the bracket - absorbed by A = 2's slack; fine).
- Segment count: per level per spine, K-1 full-plane segments (K-2 bulk + 1 far); 2 spines;
  log_K(l/r0) <= log_K l levels; root contributes K-2. Total O(K log_K l). Crude <= b(s'/K +
  offsets) <= C b l at the top. Sum <= O(K log l) x C l x l^{-A} = O(K l^{1-A} log l): o(1) for
  A > 1, comfortable at A = 2. The reconciliation note (spine needs A > 1, A = 2 taken) checks.
- Propagation of c into GEOM: sigma^2 = (A log l/c)^{2/theta} multiplies GEOM's polylog constant
  only; no exponent. As claimed.
- Caveat carried from V1: the far-child touching bound holds at "its own scale and depths" ONLY
  for far-depths at or above the quantile - i.e., only on the punctured window. With V1's repair
  this section is sound as printed.

### V4. Patchwork consistency: FOUR REAL FINDINGS (READ, line-level)

1. TWO SIGMAS. Section 2 (untagged) still defines the dive depth via "sigma := (A log l)^{1/theta},
   A = 2" - WITHOUT the tail constant c - while section 3's [V3] tag restores
   sigma = (A log l / c)^{1/theta} and says it "enters sigma, hence d = sigma W". The definition
   actually consumed by d(r), the class window, and GEOM is section 2's. The very bug the banner
   lists as fixed ("the tail constant c was silently dropped in v2") is still live in the
   governing definition. One-token fix; constant-level.
2. STALE ATTACK LIST. Section 6 (untagged) instructs the next referee to attack "the slope-lemma
   constant chase (17 c_+ and the 2.02 + 2 slack)" - retired by [V3] in sections 3-4 - and "the
   (H-wand) honesty clause's claim that published wandering proofs are two-sided-arc-conditional"
   - REVERSED by the [V2REF] honesty clause (one-sided enclosing ball, favourable direction).
   Both bullets now point at text the document no longer stands on. Meta-text only, but it
   contradicts the tagged corrections and will misdirect the next pass.
3. VESTIGIAL FIXED-POINT/RATIO TEXT. Section 2's child K-1 bullet still carries "the class tilt
   fixed point evaluates to C_K ... with base-tilt-over-increment <= C_K - 1 = 2.02 at EVERY
   level" - the enabling fact of the RETIRED slope lemma, presented as load-bearing ("this
   re-typing is the load-bearing architectural fact" sentence survives around it). In the v3
   wiring nothing consumes t/eta <= 2.02. Should be struck or marked idle alongside section 4.
4. UNDEFINED t(s). The class line says "tilt <= t(s)" and t(s) is defined nowhere in the
   document (the sketch referee's class had tilt as a DERIVED consequence of the depth window).
   As it stands the class has an undefined parameter; either define t(s) := C_K d(K s)/(s/2)
   -type or delete the clause as redundant.
   Swept and CLEAN: no surviving consumption of the struck K^xi-clearance claims (both strike
   notes present, no other clearance language); no untagged text consumes the retired slope
   lemma's INEQUALITY itself; (P-conc)'s free-times-only scoping is consistent everywhere; the
   main claim max(1, 2/theta) polylog is consistent between sections 1 and 5.

### V5. Consequence chain with (H-I3): PASSES, one attribution nit (DERIVED + READ)

- (H-I3) now appears in the ledger with the correct content (upper-tail sqrt-scale for T_+, the
  corner note's I3), correct provenance (corner referee's "no obstruction identified"), correct
  candidate closure (the walk, ledger entry 22), and the right conditionality sentence ("until
  that walk survives review, every consequence below is ALSO conditional on I3"). Given Part I,
  that PENDING flag is doing real work and must stay until the walk's W3/W6 repairs land.
- Chain inequalities re-checked: P2 <= MEANGAP (Claim 5, P2 = MEANGAP - Part1, Part1 >= 0) and
  MEANGAP <= A_+ (A_+ = MEANGAP + A, A >= 0 by E T >= g). The threshold citation (alpha > 1/3;
  package-relative chi in (1/3, 1/2)) matches the C1 banner verbatim, with the pinning cited.
- Nit: the "Assume" block lumps all five inputs into the THEN clause, but the A_+ theorem itself
  consumes only (H-curv) + (H-wand) + (P-Alex); (P-conc) and (H-I3) are consumed by the
  "Consequently" sentence (the corner note's cost formula). Splitting the statement would make
  the conditionality exact per-conclusion. Wording only; the ledger is complete - every named
  input now appears, including I3's pending status. The banner's worst-defect fix is delivered.
- Pedantic flag, inherited: "I8 of the salvaged corner note holds" - I8's C1 display says
  C sqrt(l) log l while the delivered bound is sqrt(l) (log l)^{max(1,2/theta)}. The corner note
  absorbs any polylog (iter74 R2 already ruled this costless), but the sentence should say
  "I8 at sqrt-polylog scale", as the theorem display itself does.

### V3 document: repair bill

(D-V1) MAJOR: punctured window {0} u [sigma W_{s'/K}, C_K d(K s')]; D = 0 handled by the
two-anchored-children step (branching 2, ratio 2/sqrt(K) < 1) or root-only admission. No
exponent cost. (D-V2..V4, minor): the delta-range sentence; the section-2 sigma definition
(insert /c); strike/retag the stale section-6 bullets and the vestigial 2.02 text; define or
delete t(s); optional convention sentence for the K-power slack in GEOM. VERDICT: REPAIRABLE
(MAJOR REVISION at V1; all statement-level; main claim and exponents unmoved).

--------------------------------------------------------------------------------------------------
## Cross-document note

The walk's repaired range (0, 4 b^2 sqrt(r)/a_w) covers the corner consumer at every pair
distance jointly with the deterministic-zero branch (W6), so (H-I3)'s candidate closure remains
the entropy route after repair - the QV-bypass thesis is intact; nothing in this report reopens
Kesten's bridge. The v3 dead-band defect does not contaminate the walk (no dependence either
direction); the two documents fail independently and repair independently.

Receipts: DHS_1401.0917_text.txt (Theorem A.1 at char ~44800; Theorem A.2 assembly with constant
p and constant lambda-window at ~45200-46600), BOUCHERON_SLIDES_text.txt (psi(x) = x(e^x-1),
monotone on R+, p.45), adh_survey_text.txt pages 46-51 (Prop 3.10, Thm 3.11, Lemma 3.12, (3.13),
(3.14), Lemma 3.13 - all legible on re-read). All in this scratchpad.
