# I8 from curvature: a diving-chain sketch (iter 73, author's hand)

REFEREE VERDICT (iter 80/81): REPAIRABLE - no fatal defect survived a full re-derivation; three
printed claims are wrong and are corrected in place below with [REF] tags. Report:
I8_sketch_REFEREE_iter74.md. The three: (1) the branching-2 recursion consumes a class membership
that fails - repaired by re-typing the far child as bulk (the referee's fix, with fixed-point
constant C_K = 1/(1 - K^{xi-1}) = 3.019 at K=5, xi=3/4, CONVERGES with the path architecture found
independently in the addendum's Part 3); (2) section 6.4's single-log claim is FALSE - the forced
deep quantile puts (log l)^{2/theta} into GEOM and the honest bound is
A_+(l) = O(sqrt(l) (log l)^{max(1, 2/theta)}); (3) the header's old prize line "a hypothesis the
program already carries as H2" is FALSE against MG2A's pointwise H2 - see the corrected prize
statement below. THE FEARED FATAL POINT (first-order tilt leak in GEOM) DOES NOT EXIST: the chain
telescopes exactly, and a slope lemma (report section 3b) shows H2-pointwise-UPPER at e_2 plus
convexity and evenness controls the tilted second difference, because the class fixed point keeps
base-tilt-over-increment <= C_K - 1 = 2.02 at every level. My "shrinking arc" reason (6.2) was
WRONG - corners can accumulate at e_2 (referee counterexample: piecewise-linear interpolation of
s^2) - but the conclusion holds for the ratio reason. CORRECTED PRIZE STATEMENT: the TRUE
hypothesis set is H2-pointwise-upper at e_2 (for GEOM) + arc-curvature AS ALREADY CONSUMED BY the
published wandering input (two-sided, on the arc the strayed chords realize) + concentration +
full-plane Alexander. No hypothesis NEW to the sketch's own named inputs; the arc lives inside
input (ii), not as an extra assumption.

STATUS: DERIVED SKETCH, REFEREED REPAIRABLE, corrections applied in place. Historical original
header preserved below for the record; read the verdict banner first.
[Original header:] If this survives, the salvaged note's one open input I8 (the one-wall Alexander
bound) REDUCES to curvature of the limit shape in an arc at e_2 - a hypothesis the program already
carries as H2 [REF: FALSE as stated - see banner point (3)] - plus published inputs. The corner
route would then need NO hypothesis beyond the program's own set [REF: corrected to "no hypothesis
new to the sketch's named inputs"]. That is a large enough prize that this sketch must be treated
with proportionate suspicion.

## 1. The device: dive into the bulk, where the wall does not exist

Target: A_+(l) := E T_+((0,0),(0,l)) - g l <= C sqrt(l) polylog(l), conditional inputs permitted
from {curvature at e_2 (H2-arc), published concentration, published full-plane Alexander}.

Fix K >= 5. Let d := the wandering scale at step-length l/K (under the conditional inputs,
d = (l/K)^xi with xi <= 3/4; the argument below only needs d chosen >= that wandering quantile).
Define the diving chain
    w_0 = (0,0), w_1 = (d, l/K), w_j = (d, j l/K) for j = 1..K-1, w_K = (0, l).
Pathwise, T_+((0,0),(0,l)) <= Sum_j T_+(w_j, w_{j+1}), and expectations add by linearity (the
segments share the configuration; no independence is used anywhere):
    a_l <= Sum_j E T_+(w_j, w_{j+1}).                                              (1.1)

## 2. Pricing the three kinds of segment

(BULK, j = 1..K-2): both endpoints at depth d, chord vertical of length l/K. On the event that the
free geodesic between them deviates less than d, it stays in H and T_+ = T. So
    E T_+(w_j, w_{j+1}) <= E T(w_j, w_{j+1}) + b (b/a)(l/K + 2d) P(deviation >= d),      (2.1)
where the second term uses the crude deterministic bound T_+ <= b(b/a)(l1-diameter) on the touching
event [occupation-lemma style]. With d at the wandering quantile and a stretched-exponential
wandering tail (the conditional input), the second term is o(1). The first term is the FULL-PLANE
mean, and published Alexander gives E T(w_j, w_{j+1}) <= g(l/K) + C sqrt(l/K) log(l/K).

(ANCHOR, j = 0 and K-1): one endpoint on the wall, chord (d, l/K), TILTED by angle ~ dK/l. These
are one-wall quantities again, at scale l/K: recurse. The recursion must carry (i) the tilt window
and (ii) the depth of the far endpoint; write f(r) for the supremum of the anchored deficit over
tilts within the window and far-depths <= wandering scale. Then (1.1) reads
    f-version: a_l - g l <= 2 f(l/K) + (K-2)[C sqrt(l/K) log l] + GEOM + o(1),         (2.2)
where GEOM is the deterministic price of the chain's shape:
    GEOM := 2 g((d, l/K)) + (K-2) g((0, l/K)) - g((0, l))
          = 2 [ g((d, l/K)) - g((0, l/K)) ].                                          (2.3)

## 3. Where curvature enters, and the exponent arithmetic

Crude norm bound: g((d,r)) - g((0,r)) <= d g(e_1) - linear in d, and with d = wandering the GEOM
term is the wandering scale again: this is EXACTLY the Splitting Lemma's obstruction reappearing,
and without curvature the chain buys nothing. (Consistency check: the device does not evade 6.6.2
for free.)

CURVATURE at e_2 (H2-arc form): g((d, r)) - g((0, r)) <= C d^2 / r for d <= r. Then
    GEOM <= 2 C d^2 K / l.
At xi = 3/4 (the PUBLISHED curvature-conditional wandering exponent): d^2 = (l/K)^{3/2}, so
GEOM <= 2C l^{1/2} K^{-1/2} - SQRT SCALE. At xi = 2/3 (KPZ): GEOM ~ l^{1/3} - better than sqrt.
The wandering exponent may be anything <= 3/4: GEOM <= 2C l^{2 xi - 1} K^{1 - 2 xi} <= sqrt scale
whenever xi <= 3/4. So under curvature, the geometric price of diving is at most sqrt(l), for every
published-compatible wandering exponent.

Recursion: f(l) <= 2 f(l/K) + C sqrt(l) log l  (the sqrt log from the bulk segments dominates GEOM
at xi <= 3/4). Master arithmetic: homogeneous exponent log_K 2 < 1/2 for K >= 5 (log_5 2 = 0.431),
forcing exponent 1/2 dominates:
    f(l) = O( sqrt(l) log l ).                                                        (3.1)
Hence A_+(l) <= f(l) = O(sqrt(l) log l): I8 at the strength the salvaged note needs, CONDITIONAL on
the section-4 gaps closing.

## 4. THE GAPS, enumerated with the intent that a referee attack each

(G1) The anchored recursion's induction load. f(r) must be defined over a CLASS (tilt window,
far-endpoint depth), and the recursion at the next level splits an anchored pair into bulk + anchored
pieces of the same class. Whether the class is stable under one recursion step - tilts compound as
dK/l per level - needs explicit bookkeeping. Alexander's own machinery faced exactly this and
resolved it with a two-parameter mesh; the one-wall version has not been checked.

(G2) The curvature input is used at TILTED directions (the chord (d, l/K)), so H2 must hold in an
ARC at e_2, not at the single direction - the same arc-vs-point issue the C1 referee flagged in the
old route (correction 10 there). The arc needed here shrinks with l (width ~ K d/l -> 0), which is
the favourable direction, but the hypothesis must be stated as arc-curvature.

(G3) The wandering tail. (2.1) needs P(deviation >= d) times a CRUDE linear bound to be o(sqrt).
Published curvature-conditional wandering bounds (Newman-Piza style) control the MEDIAN scale;
the TAIL at the quantile d needs the concentration-plus-curvature argument quantified (standard
shape, but the constants and the arc dependence must be tracked).

(G4) The bulk segments consume full-plane Alexander at direction e_2 exactly; fine. But their
endpoints are at depth d, and "the wall does not exist" requires the free geodesic to stay in H,
i.e. deviation < d toward the wall specifically; one-sided deviation is what is needed and what
wandering bounds give - no gap expected, listed for completeness.

(G5) Dependence between levels of the recursion: none is used (all bounds are expectations and
pathwise inequalities), but the DEFINITION of f as a supremum over a class must be checked to be
finite at the base scale and the log factors summed honestly across the O(log_K l) levels: each
level contributes its own log, so the honest form of (3.1) may be sqrt(l) log^2 l or sqrt(l)
polylog. Harmless for the note's I8 (any polylog is absorbed by its n^{o(1)}), but the exponent of
the log should be stated correctly.

## 5. What this changes if it survives

The salvaged note's conditional structure "corner closes iff alpha > 1/3, conditional on I8"
becomes "conditional on H2-arc + published inputs" - i.e. the corner route needs NOTHING beyond
the program's own hypothesis set. Combined with the refereed alpha = chi pinning, the assembly
picture "package assembles when chi > 1/3" would rest on H1-H4 + CH alone. The wall (CRUX section
2) remains the wall; nothing here touches it. And the Splitting Lemma's obstruction is CONFIRMED
rather than contradicted by this sketch: without curvature the chain pays wandering (section 3's
consistency check); curvature is precisely what converts the diving price from linear-in-depth to
quadratic-over-length.

Referee instructions when capacity allows: attack G1 first (it is where Alexander's machinery is
genuinely nontrivial), then G2's arc bookkeeping, then the log accounting in G5.

## 6. PARTIAL CLOSURE OF G1/G2 BY EARLY STOPPING (iter 74, author's hand; arithmetic below,
## still part of the SKETCH - the referee should attack this section on equal terms)

(6.1) STOP THE RECURSION EARLY. Do not run the recursion to scale O(1). Stop at
    r0 := l^c  for a small fixed c > 0,
and at the stopping scale use the crude deterministic bound f(r0) <= b (b/a) C r0 (any anchored
pair's confined time is at most b times a staircase, minus g times length - linear in r0 with a
harmless constant). The stopped recursion contributes
    2^J f(r0)  with  J = log_K(l / r0),  2^J = (l/r0)^{log_K 2}.
With log_K 2 <= 0.431 (K >= 5): contribution <= C r0 (l/r0)^{0.431} = C l^{0.431} r0^{0.569}.
This is <= C sqrt(l) iff r0 <= l^{(0.5 - 0.431)/0.569} = l^{0.121}. So ANY c <= 0.12 works: the
base of the induction is bounded by inspection, and G1's "finite at the base scale" clause closes.

(6.2) TILT COMPOUNDING DIES UNDER THE SAME REFINEMENT. [REF iter 81: the CONCLUSION stands
but THIS REASON IS WRONG - shrinking arcs buy nothing, since corners can accumulate at e_2
(referee counterexample, report 3b). What closes G2 is the level-uniform ratio t/eta <= C_K - 1
= 2.02 plus the slope lemma consuming H2-pointwise-upper + convexity + evenness. Same lemma as
G1's repair.] At level j (scale r_j = l/K^j), the chain
adds tilt at most K d_j / r_j = K r_j^{xi - 1} to the anchored sub-pairs. The increments GROW as
scales shrink (xi - 1 < 0), so the total is dominated by the smallest running scale:
    total tilt <= C K r_min^{xi - 1} <= C K (l^c)^{-(1 - xi)} = C K l^{-c(1-xi)} -> 0.
At xi = 3/4, c = 0.12: total tilt ~ l^{-0.03} = o(1). So the arc of directions the curvature
hypothesis must cover SHRINKS with l after all - the worry in G2 was an artifact of imagining the
recursion running to scale one. H2 need only hold in a fixed small arc at e_2; the argument uses a
vanishing sub-arc of it.

(6.3) WHAT REMAINS OF G1 AFTER (6.1)-(6.2). The class {anchored pairs at scale r, tilt <= t(r),
far-depth <= D(r)} must be checked stable under ONE recursion step with the explicit parameters
above - the compounding arithmetic is now done, the base is bounded, and what is left is writing
the step: that the two anchored children of an anchored parent lie in the class at the next scale.
That is bookkeeping with no new idea, and it is exactly what the referee should verify or break.

(6.4) LOG ACCOUNTING (G5): [REF iter 81 - THE SINGLE-LOG CLAIM BELOW IS FALSE as printed. It
priced d at median scale inside GEOM while (2.1) needs the deep quantile sigma = (A log l)^{1/theta},
A >= 2; d enters GEOM squared, so every GEOM term carries (log l)^{2/theta}. Honest bound:
f(l) = O( sqrt(l) (log l)^{max(1, 2/theta)} ) - for theta <= 1 that is at least log^2. The
original G5 hedge ("may be log^2 or polylog") was right and is reinstated. Downstream unharmed:
the note's I8 absorbs any polylog.] Original text: the forcing term at level j is C sqrt(r_j)
log(r_j) summed with weight 2^j; log(r_j) <= log l uniformly, the weighted sum of sqrt(r_j) is
geometric with ratio 2/sqrt(K) < 1, so a SINGLE factor of log l suffices: f(l) = O(sqrt(l) log l),
not log^2. G5 closes. [REF: struck per the correction above.]
