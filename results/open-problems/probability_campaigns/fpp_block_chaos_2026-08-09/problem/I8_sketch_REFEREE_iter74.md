# Referee report on I8_from_curvature_sketch_iter73.md (hostile pass, iter 74)

VERDICT: REPAIRABLE. No fatal defect found after a full re-derivation of every display,
including section 6. Three real defects, each with a constructive repair and a priced cost:
(R1) the recursion class as written is not closed under one step (the far child is not in it);
(R2) the wandering quantile in (2.1) is used at median scale where a deep quantile is required,
and the corrected quantile propagates a polylog^2 into GEOM, so (3.1) and (6.4) are wrong as
printed: the honest bound is sqrt(l) (log l)^{max(1, 2/theta)}, not sqrt(l) log l;
(R3) the header's prize claim ("a hypothesis the program already carries as H2") is false
against MG2A's exact H2, which is pointwise and explicitly not arc-uniform - though, in the
sketch's favour, I prove below that GEOM itself needs only the pointwise UPPER bound at e_2;
the arc load enters entirely through the published wandering input's own conditionality.
The feared fatal defect (first-order tilt term in GEOM, priority attack B) does NOT occur:
the chain telescopes exactly and homogeneity kills the linear term identically.

Conventions as in C1 iter60 section 0 (READ): H = {x >= 0}, wall x = 0, points (x,y) = (depth,
height), g the norm, chords written (depth-offset, height). Everything below marked DERIVED was
re-derived by me from scratch; READ means taken from the named file.

--------------------------------------------------------------------------------------------------
## 1. ATTACK A: one full recursion step, written out (DERIVED)

Parent: anchored pair (p, q), p = (0,0) on the wall, q = (D, r), far-depth D, tilt t = D/r.
The sketch's section 1 constructs the chain only for the wall-to-wall vertical parent; for the
recursion to mean anything the tilted construction must be supplied. The natural one (waypoints
on the chord, displaced into the bulk by the dive depth d' at segment scale r/K):

    w_0 = p,  w_j = (D j/K + d', j r/K)  for j = 1..K-1,  w_K = q.

All w_j have x > 0 (inside H); T_+(p,q) <= sum T_+(w_j, w_{j+1}) pathwise; waypoints must be
rounded to lattice points, costing O(b) per waypoint, O(K log l) total, absorbed in polylog.
Children and their chords:

  j = 0 (ANCHOR):     chord (D/K + d', r/K); near end ON wall. In the anchored class at scale
                      r/K iff far-depth D/K + d' and tilt (D + K d')/r pass the windows.
  j = 1..K-2 (BULK):  chord (D/K, r/K), endpoints at depths >= d'. Bulk-priceable.
  j = K-1 (FAR):      chord (D/K - d', r/K), endpoints at depths D(K-1)/K + d' and D.
                      NEAR END NOT ON THE WALL. This child is NOT in the class {one endpoint on
                      the wall, ...} for any parameter values. THIS IS THE G1 DEFECT, made exact.

Consequences, in order.

(a) The display "f(l) <= 2 f(l/K) + ..." (section 3, line 56) is UNJUSTIFIED as written for any
level below the top. At the top level (D = 0) both end children are anchored (the far child is
the reversed anchored pair; e_2-translation invariance of T_+ and the y-reflection lattice
symmetry keep it in the class), so (2.2) itself is fine. At depth >= 1 the parent has exactly ONE
wall endpoint, hence ONE anchor child; the far child is off-wall at both ends and f does not
price it. As printed, the recursion consumes a class membership that fails.

(b) THE REPAIR, verified. Price the far child as BULK, not as anchored: both its endpoints are
at depth >= min(D, D(K-1)/K + d') >= (1 - 1/K) D, so the free-geodesic deviation event at scale
r/K with margin (1-1/K)D keeps it in H, and full-plane Alexander (uniform in direction) prices
its mean. This works iff D is at least of order d', which forces a LOWER window on far-depth.
Restated class (the missing bookkeeping):

    F(r) := sup over pairs (p wall, q at depth D), D in {0} U [sigma W_{r/K}, C_K sigma W_r],
            tilt automatically <= C_K sigma W_r / r,
    where W_s = s^xi, sigma = the quantile inflation of section 4 below, C_K := 1/(1 - K^{xi-1}).

Step stability, checked at K = 5, xi = 3/4 (C_K = 1/(1 - 5^{-1/4}) = 3.019):
  - Anchor child far-depth: D/K + sigma W_{r/K} <= C_K sigma W_r / K + sigma W_{r/K}
    = (C_K K^{xi-1} + 1) sigma W_{r/K} = C_K sigma W_{r/K}. EXACT FIXED POINT: the window
    reproduces itself with the same constant. (C_K K^{xi-1} + 1 = C_K is the defining identity.)
  - Anchor child far-depth lower end: D/K + sigma W_{r/K} >= sigma W_{r/K} = K^xi sigma W_{r/K^2}
    >= 3.34 sigma W_{r/K^2}: comfortably above the child's own lower window. Closed.
  - Far child min chord depth: >= (1-1/K) D >= 0.8 sigma W_{r/K} at the lower window end:
    the deviation quantile needed is 0.8 sigma, same tail class. Closed.
  - D = 0 (top) far child: on-wall by symmetry, in class. Closed.
No THIRD class parameter (near-depth) is needed - but only because the far child is re-typed as
bulk. If one insists on recursing it, the class does need near-depth as a third parameter and a
chain construction from an off-wall near end, which the sketch does not have. The bulk repair is
the correct move and is strictly simpler than the sketch's own picture.

(c) A structural consequence the author missed: with the repair, anchored pairs spawn ONE
anchored child each, so the tree has exactly 2 anchored spines at every level, not 2^j pairs.
The homogeneous coefficient is 1, not 2; log_K 2 < 1/2 and the whole 2^J early-stopping
arithmetic of (6.1) are then unnecessary (any stopping scale r0 <= sqrt(l) works: the stopped
contribution is 2 f(r0) <= 4 b r0). The sketch's arithmetic is an overcount that happens to be
safe; it is not wrong once (a) is repaired, just slack. G1 verdict: DEFECT REAL, REPAIR EXHIBITED,
NO EXPONENT COST.

--------------------------------------------------------------------------------------------------
## 2. ATTACK B: GEOM for tilted parents (DERIVED) - the feared fatal defect is ABSENT

With the on-chord construction of section 1, the chords sum vectorially to the parent chord
(the +d' and -d' displacements cancel between j = 0 and j = K-1). Write c_i = C/K + delta_i,
sum delta_i = 0, delta_0 = (d',0), delta_{K-1} = (-d',0), others 0. Then

    GEOM = sum g(c_i) - g(C) = g(C/K + (d',0)) + g(C/K - (d',0)) - 2 g(C/K)

by homogeneity (K g(C/K) = g(C)): GEOM is an EXACT SECOND DIFFERENCE of g at the tilted chord
direction C/K, increment (d',0). In chordal coordinates u(s) := g((s,1)) (convex, even by the
lattice reflection x -> -x):

    GEOM = (r/K) [ u(t + eta) + u(t - eta) - 2 u(t) ],   t = D/r,  eta = K d'/r.

There is NO first-order term for ANY norm g and ANY tilt: the derivative of g in the tilt
direction cancels identically because the decomposition telescopes. The priority-attack worry
(linear-in-d times tilt) would arise only for a chain whose chords do NOT sum to the parent
chord - e.g. the sketch's constant-depth waypoints of section 1 applied verbatim to a tilted
parent, which dump the whole offset D - d' into the last segment. Even that variant survives at
xi <= 3/4 (its GEOM ~ D^2 K / r = sqrt scale), but the on-chord chain is cleaner and is what the
write-up should fix as the construction. ATTACK B: the sketch survives, conditional on actually
writing the tilted construction, which iter 73 never does.

--------------------------------------------------------------------------------------------------
## 3. ATTACK C: what curvature hypothesis is ACTUALLY consumed (DERIVED, two findings)

(3a) Form equivalence at e_2. MG2A's H2 (READ, its lines 49-53) is in angular form:
c_- phi^2 <= h(phi) - h(0) - h'(0) phi <= c_+ phi^2, |phi| <= delta, h(phi) = g(unit at angle
phi), h'(0) = 0 forced by reflection symmetry at a lattice axis. Chordal conversion:
g((s,1)) = sqrt(1+s^2) h(phi(s)), phi(s) = arctan s, so u(s) - u(0) = h(phi) - h(0)
+ (s^2/2) g(e_2) + O(s^4). Hence the sketch's form g((d,r)) - g((0,r)) <= C d^2/r on d <= delta r
is equivalent at e_2 to H2-pointwise-upper with C = c_+ + g(e_2)/2 + o(1). No gap AT e_2. But the
task-level phrasing "uniformly over directions in the arc" applied to the FIRST difference
g((d,r)) - g((0,r)) is incoherent at tilted bases (the first difference there has a genuine
linear term even for u(s) = s^2); the object the argument needs at tilted bases is the CENTERED
SECOND difference of section 2, and any final statement of the hypothesis must say so.

(3b) Does pointwise-at-e_2 control the tilted second difference? In general NO: counterexample
u* := piecewise-linear interpolation of s^2 at nodes s_k = 2^{-k}, symmetrized. u* is convex,
even, and s^2 <= u*(s) <= 3 s^2 (chord of s^2 on [s, 2s] is bounded by 3s^2), so H2-pointwise
holds two-sidedly with (c_-, c_+) = (1,3); yet at a node the second difference with increment
eta << s_k is (3/2) s_k eta - FIRST order in eta - and corners accumulate at e_2, inside EVERY
shrinking arc. So (6.2)'s "the arc shrinks" is NOT the reason G2 closes: shrinkage alone buys
nothing against corners accumulating at the axis.

WHAT SAVES THE SKETCH is a ratio the author never states: in the recursion the base tilt and the
increment are COMPARABLE AT EVERY LEVEL. From the repaired class, t <= C_K sigma W_r/r and
eta = K sigma W_{r/K}/r = sigma K^{1-xi} r^{xi-1}, so t/eta <= C_K K^{xi-1} = C_K - 1 = 2.02
(K=5, xi=3/4; the fixed-point identity again). And for ANY convex even u with only the UPPER
pinning u(s) - u(0) <= c_+ s^2 on |s| <= delta: u'(s) <= [u(2s) - u(s)]/s <= 4 c_+ s (using
u(s) >= u(0)), hence

    u(t+eta) + u(t-eta) - 2u(t) = int_0^eta [u'(t+s) - u'(t-s)] ds <= eta [u'(t+eta) - u'(t-eta)]
                                <= 4 c_+ eta (t + 2 eta) <= 4 c_+ (t/eta + 2) eta^2 <= 17 c_+ eta^2.

(Check against u*: with eta ~ t/2 the window [t-eta, t+eta] has total slope variation ~ C t ~ C eta,
second difference <= C eta^2 - the counterexample indeed does not bite in this regime.) So GEOM_r
<= C c_+ sigma^2 K^{1-2xi} r^{2xi-1}, the sketch's scaling with sigma^2 attached, consuming ONLY
H2-pointwise-UPPER at e_2 plus convexity and evenness. This is BETTER than the sketch's own G2/6.2
story and is the correct closure of G2 for GEOM. The load-bearing new fact is the level-uniform
bound t/eta <= 2.02, which is exactly the class fixed point of section 1 - i.e. G1's repair and
G2's closure are the same lemma. ATTACK C verdict: the sketch's stated reason is wrong, the
conclusion is right, and the GEOM curvature consumption is genuinely pointwise.

(3c) BUT the arc does not disappear from the hypothesis ledger: it moves into input (ii). The
published curvature-conditional wandering bounds (Newman-Piza / Licea-Newman-Piza style, and any
stretched-exponential-tail refinement) condition on shape curvature ON AN ARC around the
direction, including the LOWER side (deviation from the tangent at least quadratic - that is what
makes transverse detours expensive), because the strayed chords realize an arc of directions of
width ~ the wandering slope. The recursion uses wandering at tilts up to ~ sigma W_r/r, within
that arc. So the sketch's TRUE hypothesis set is: H2-pointwise-upper at e_2 (for GEOM, this
report) + arc-curvature as consumed by the wandering citation (two-sided in the published
proofs) + concentration + full-plane Alexander.

--------------------------------------------------------------------------------------------------
## 4. ATTACK D: the quantile bug in (2.1) (DERIVED) - real, repairable, costs a polylog power

As printed: "d at the wandering quantile ... the second term is o(1)". If d is the median (or any
fixed quantile), P(deviation >= d) is a CONSTANT and the touching term is b(b/a)(l/K + 2d) times
a constant ~ l/K PER SEGMENT; (K-2) segments give Theta(l). Fatal at face value. The repair is
forced: with the stretched-exponential tail P(dev >= sigma W) <= C exp(-sigma^theta), take
sigma = (A log l)^{1/theta}, A >= 2, so every touching term across the whole tree (O(2^J K)
segments, each <= b(b/a) l) sums to O(l^{2} l^{-A}) = o(1). So d = sigma W_{r/K}, NOT the median.

Propagation, which the sketch's arithmetic silently omits: d enters GEOM SQUARED, so every GEOM
term carries sigma^2 = (A log l)^{2/theta}. Summed over the tree (weights 2^j, ratio
2 K^{-1/2}·K^{... } < 1 at xi = 3/4, K >= 5, or over the 2 spines after the repair - same order):

    GEOM total <= C sqrt(l) (log l)^{2/theta};  bulk Alexander total <= C sqrt(l) log l.

Honest conclusion: A_+(l) = O( sqrt(l) (log l)^{max(1, 2/theta)} ). For theta <= 1 (H1's stated
range) that is at least log^2. Therefore: (3.1) "O(sqrt(l) log l)" is NOT delivered by this
argument, and (6.4)'s "a SINGLE factor of log l suffices; G5 closes" is FALSE - (6.4) accounted
the bulk logs only and priced d at median scale inside GEOM while (2.1) needs the deep quantile;
the two displays are inconsistent as printed. The sketch's own G5 hedge ("may be sqrt(l) log^2 l
or polylog") was correct and should be reinstated. Cost: polylog exponent only; the note's I8
absorbs any polylog, so nothing downstream breaks. Also minor, no action needed: the crude
constant in (2.1) should be b(l/K + |depth difference|), the printed b(b/a)(l/K + 2d) is a
harmless overcount, and E[T_+ 1(touch)] <= crude P(touch), E[T 1(no touch)] <= E T are sound.

--------------------------------------------------------------------------------------------------
## 5. ATTACK E: early stopping (6.1)-(6.4), re-derived

(6.1) arithmetic CHECKS: log_5 2 = 0.4307; 2^J f(r0) <= C r0 (l/r0)^{0.431} = C l^{0.431} r0^{0.569}
<= C sqrt(l) iff r0 <= l^{0.0693/0.5693} = l^{0.1217}; c <= 0.12 valid. f(r0) <= 2b r0 for tilted
anchored pairs CHECKS: T_+ <= b(r0 + D) <= 2b r0 via the in-H staircase, g >= 0 subtracted.
With the section-1 repair the whole 2^J apparatus is unnecessary (2 spines, any c < 1/2), but as
written it is correct and merely slack.

(6.2) tilt compounding CHECKS with two corrections. Per-level increment: anchor-child tilt =
parent tilt + K d'/r, d' = sigma W_{r/K}, so increment = sigma K^{1-xi} r^{xi-1} (the sketch's
K r^{xi-1} up to the sigma and a K^{-xi}). Increments grow geometrically downward (ratio K^{1-xi}
= 1.495 per level), sum dominated by the smallest scale times C_K = 3.02: total tilt <=
3.02 sigma K^{1-xi} r0^{xi-1} ~ (log l)^{1/theta} l^{-c(1-xi)} -> 0. The EVERY-INTERMEDIATE-LEVEL
check the task demanded: accumulated tilt at scale r_j is <= C_K sigma K^{1-xi} r_j^{xi-1}, which
is exactly the class window at scale r_j (the fixed point of section 1) - so the window holds at
every level, not just in total. Correction 1: the sketch's display omits sigma (the same median/
quantile slip as attack D); harmless since sigma is polylog. Correction 2: "H2 need only hold in
a fixed small arc; the argument uses a vanishing sub-arc" is the wrong mechanism (section 3b);
what closes G2 is the t/eta ratio, not the shrinkage.

(6.4) FALSE as printed - see attack D. The geometric sum over levels is right (ratio 2/sqrt(K));
the single-log conclusion is not, because GEOM carries sigma^2.

--------------------------------------------------------------------------------------------------
## 6. ATTACK F: consistency with the Splitting Lemma (C1 6.6.2, READ)

The Splitting Lemma splits the H-geodesic at its RANDOM crossing of the midline and pays
b E[x*] - the depth of a wall-pair geodesic at the split height - at every dyadic scale; its (-)
clause says THAT route cannot see below wandering. The diving chain splits at DETERMINISTIC
waypoints and never splits at a return to the wall: the anchored ends are recursed, not split,
and the bulk/far segments are priced by full-plane Alexander on the no-touching event. No step
of the sketch re-uses wall-splitting. The two results are compatible, and the sketch's section 3
consistency check is correct and honest: without curvature GEOM ~ d g(e_1) = the wandering price,
i.e. the chain pays the deterministic ANALOGUE of E[x*] unless curvature converts linear depth
cost to quadratic. Directionally: the lemma is an inequality D_{2l} >= 2 D_l - 2b E[x*_l]
(re-derived, correct as stated in 6.6.2); combined with A_+ ~ sqrt it would only IMPLY a sqrt
lower bound on E[x*] if 2 D_l - D_{2l} >= c sqrt(l), which an upper bound on D_l does not force.
No contradiction in either direction. ATTACK F: PASSES.

--------------------------------------------------------------------------------------------------
## 7. ATTACK G: the prize claim of section 5 against the inputs' actual status

(iii) Full-plane Alexander: PUBLISHED, unconditional for bounded weights, uniform in direction
(Alexander 1997); consumed here at chords of every tilt in the shrinking window - fine. READ
against C1's own usage; not re-verified against the paper (bounded weights satisfy his moment
condition; citation-level check owed at write-up, as the file already notes).

(ii) "Published curvature-conditional wandering bounds with stretched-exponential tails":
OVERCLAIMED as stated. The published NP/LNP results are exponent statements (xi <= 3/4 under
curvature); the sigma-quantile stretched-exponential TAIL form the argument consumes at every
level (attack D makes it load-bearing, not decorative) is standard-derivable from concentration
plus curvature but must be quoted from a specific source or proved in an appendix - the sketch's
own G3 concedes exactly this; it remains open in iter 73 + section 6. And the curvature those
proofs condition on is ARC curvature including the lower side (section 3c).

(i) vs the program's H2: MG2A's exact H2 is H2-POINTWISE at the reference direction, two-sided
quadratic pinning of h(phi) at phi = 0 only, with the explicit sentence "Arc-uniform curvature is
not required by anything located", and the C1 update (ii)(c) warns arc hypotheses are plausibly
STRONGER than H2-pointwise. Therefore the header claim "REDUCES to curvature ... a hypothesis the
program already carries as H2" is FALSE as written. The correct accounting after this report:
GEOM needs only H2-pointwise-UPPER at e_2 (section 3b - a genuine improvement over the sketch's
own statement of its needs), but the wandering import needs arc curvature as its OWN condition,
so the corner route conditional on this sketch reads: H2-pointwise + [arc-curvature-conditional
wandering tails, published-modulo-G3] + Alexander. That is more than "the program's own set" by
exactly the arc condition inside input (ii). The prize is real but smaller than advertised.

--------------------------------------------------------------------------------------------------
## 8. Summary of required revisions (all repairable; no exponent damage)

R1 (G1, fatal as written, repaired here): state the tilted chain construction (section 1);
   replace the class with {far-depth in {0} U [sigma W_{r/K}, C_K sigma W_r]}, C_K = 1/(1-K^{xi-1});
   re-type the far child as bulk; recursion becomes f <= f(l/K) + (K-1) bulk + GEOM below the top.
R2 (attack D): d = (A log l)^{1/theta} W_{r/K}; conclusion becomes A_+ = O(sqrt(l)
   (log l)^{max(1,2/theta)}); withdraw (6.4)'s single-log claim; keep G5's original hedge.
R3 (attack C/G): restate the curvature input as (a) H2-pointwise-upper at e_2 for GEOM, via the
   slope lemma and the t/eta <= C_K - 1 fixed-point bound, and (b) the arc condition carried by
   the wandering citation; delete "already carries as H2" from the header; replace 6.2's
   shrinking-arc mechanism with the ratio mechanism.
Minor: lattice rounding of waypoints (O(K log l) total); (2.1)'s crude constant; both-orientation
   closure of the class under e_2-translation and y-reflection.

What I could not verify and did not assume: the exact published form of the wandering tail
(input (ii)) - left as the sketch's G3, now flagged as load-bearing at every level rather than
only in the bulk estimate.
