# Attempt (dead-end recorded): the variance LOWER bound D via block-time decomposition
# and the occupation cap. 2026-08-12, a separate session (disjoint lane; by hand).
# STATUS: attempt, NOT a result. Dies at a precise circularity, recorded 8.3-style so the
# next agent does not re-walk it. Nothing here moves chi = 1/3 or any refereed claim.

## Why this attempt suggests itself

8.4 splits the wall: the LOCAL moment caps (the (L1')/(L2') side, now shrunk to the near
band) and the variance lower bound D, "the half that Newman-Piza's log n leaves furthest
from the truth." The refereed occupation lemma is an UPPER cap on per-block time, and 8.3
records that trading probabilistic for deterministic input on the A4 side LOSES powers.
The untried direction: use the deterministic LOWER floor on level-time - every lattice
path from level to level must cross W rows, so T_level(gamma) >= a W for EVERY path,
uniformly - as a variance CHANNEL on the D side, where the occupation lemma's geometry
(levels of height W = n^{3/4} polylog, M blocks per level, near-band confinement under
(H-curv)) has not been exploited for a lower bound.

## The construction

Reveal the environment level by level: F_k = sigma(weights in levels 1..k), k = 1..n/W.
Doob decomposition: Var(X_n) = Sum_k E[Delta_k^2], Delta_k = E[X|F_k] - E[X|F_{k-1}].
Hope: the deterministic floor T_level >= aW forces each level's revelation to move the
conditional mean by ~ (time spent) x (level-average weight surprise), giving
Delta_k ~ aW x sigma/sqrt(#edges per level) per level, and summing n/W levels beats log n.

## Where it dies (the precise circularity)

The conditional-mean response to a level's weights is NOT (time floor) x (average shift).
Writing the first-order response of the min: revealing level k moves E[X | ...] by the
expected centered weight-sum ALONG THE OPTIMIZING PATH, and the optimizer re-chooses
within the level. A level-average shift delta moves every candidate path by delta x (that
path's level-time). The part of delta that moves ALL paths equally is delta x aW ONLY IF
every path had equal level-time; the transmitted variance is carried by the COMMON floor,
and the common floor is deterministic - a deterministic summand contributes ZERO variance.
What transmits is the VARIATION of level-time across the near-optimal ensemble:
    E[Delta_k^2] >~ sigma_level^2 x Var_paths(T_level restricted to the competitive set),
and Var_paths(T_level) at fluctuation scale IS (a face of) the quantity the wall is
trying to lower-bound - path-time variation across the competitive ensemble is the
fluctuation. The channel is self-referential: variance in, variance out. This is the same
circularity Newman-Piza escape only by paying corridor probabilities (their dyadic
corridor argument), which is exactly where their log n comes from; and it is the
lower-bound mirror of Chatterjee's chaos-variance equivalence - the transmission
coefficient of any environment-average channel is the path-ensemble's own sensitivity.

Two rescue ideas, both checked and dead:
- CONFINEMENT does not help: under (H-curv) the band still contains ~M^{3/4} blocks per
  level (the refereed near-band count), so within-band re-optimization keeps the dodge
  freedom that dampens the common response; confinement shrinks WHERE the ensemble lives,
  not its time-variation.
- The occupation UPPER cap is the wrong-signed object twice over: it bounds individual
  block-times above (no lower-bound content beyond the trivial aW floor already used),
  and 8.3(a) already showed deterministic caps cost powers when substituted for
  fluctuation-scale content.

## What survives

Only a reframing, stated without any claim of progress: any improvement of D through an
environment-revelation martingale requires a lower bound on the LEVEL-TIME VARIATION of
the competitive path ensemble at fluctuation scale - an object strictly between the
transversal wandering exponent (which measures displacement, not time) and the variance
itself. If some independent input ever lower-bounds competitive-ensemble time-variation
(e.g. from wandering-exponent machinery of the xi-side), this channel converts it to a D
lower bound with the level geometry above. Recorded as a conditional converter, nothing
more. The columnar/brochette literature (2605.23718) computes exponents by BREAKING
homogeneity with a defect column - its conditioning trick manufactures exactly the
time-variation that homogeneous Z^2 refuses to give for free; that contrast is the
cleanest statement of why this attempt had to die.

## Literature look on the converter's input (same day, one bounded pass)

Checked whether the xi-side (wandering) literature supplies the converter's input. It
does not: Licea-Newman-Piza give xi(d) >= 1/2 and xi(2) >= 3/5, and arXiv 2511.06166
(Nov 2025) mildly strengthens LNP-type NON-RANDOM fluctuation lower bounds - all of these
are DISPLACEMENT bounds. No known object lower-bounds competitive-ensemble level-TIME
same reason the main attempt died: the competitive ensemble is competitive precisely
because its members' times agree to within the fluctuation scale - displacement spreads
the ensemble in SPACE while the time coordinate is equalized by selection. THE MISSING
LEMMA, named for any future attempt: a quantitative statement that spatially separated
near-optimal paths cannot have their level-times equalized too well - i.e., a
lower bound on within-ensemble time dispersion in terms of ensemble diameter. That is a
rigidity assertion about the environment (two far-apart corridors rarely both run this
fast), which smells like the BKS/chaos side rather than the wandering side - and on the
chaos side it is again the variance, closing the loop. Recorded so the next agent starts
at the missing lemma, not at the martingale.

## The third face, and the obstruction unified (same day, one more by-hand pass)

Probed the missing lemma's chaos-side face directly: corridor-pair anticoncentration.
Take two disjoint corridors C1, C2 in the near band at separation >= l. Their
corridor-restricted optimal times S(C1), S(C2) are functions of DISJOINT weight sets,
hence independent; if the competitive ensemble (tolerance delta = fluctuation scale)
contains paths essentially living in each, then |S(C1) - S(C2)| <= 2 delta - a collision
event for independent variables, so
    P(both corridors competitive) <= Q(S(C1) - S(C2), 2 delta) <= min_i Q(S(Ci), 2 delta),
where Q is the Levy concentration function. If S(Ci) obeyed a sum-like anticoncentration
(Kolmogorov-Rogozin for a FIXED path: Q <= C delta / (sigma sqrt(n))), two-corridor
competitiveness would be rare and ensemble time-dispersion would follow - the missing
lemma would fall out of independence alone.

IT DIES because S(Ci) is not a sum: it is the MINIMUM over the corridor's exponentially
many paths, and a minimum's concentration function is not inherited from its summands -
strong concentration of the min is precisely the phenomenon under study. Rogozin applies
to each fixed path; the min destroys it. Lower-bounding Q^{-1}-dispersion of a
corridor-restricted min IS a localized variance lower bound: the missing lemma REDUCES TO
localized-D. (And paths that WEAVE between corridors break the disjoint-support
independence before this even starts - confining to corridors pays the Newman-Piza
probability again.)

UNIFICATION, the note's actual yield: the three natural lower-bound routes die at ONE
obstruction viewed from three sides -
  (1) martingale transmission needs ensemble level-time variation (= the fluctuation);
  (3) corridor-pair anticoncentration needs anticoncentration of a restricted MIN
      (= localized D).
Every door is the same door: ANTICONCENTRATION OF RESTRICTED MINIMA. This is the
lower-bound mirror of 9.8's upper-bound statement that (L1') is the variance ratio - the
wall seen from below is "restricted minima do not concentrate too fast", and localizing
the restriction does not weaken it. A future attempt on D should therefore attack
restricted-min anticoncentration DIRECTLY (e.g., can one lower-bound the concentration
function of a W x W block-crossing time? even THAT local object is the same problem at
scale W - which is, finally, the renormalization structure the exponent chi expresses).
Nothing proved; the geometry of why every naive route fails is now written down once.

## The door is not empty: Elboim's small-ball bound (pointer added same day)

arXiv 2406.10971 (Elboim, Jun 2024; answering Ahlberg-de la Riva) proves precisely the
UNRESTRICTED form of the object this note ends on: for planar FPP with weights
absolutely continuous on (0, infinity),
    max_a P(T(x,y) in [a, a+1]) <= C / sqrt(log |x-y|)
- an anticoncentration bound for the full point-to-point passage time (unit-width
scale; consistent with recovering the Newman-Piza variance scale). So restricted-min
anticoncentration is a LIVE technique area, not a bare wall. THE SHARPENED QUESTION for
any future attempt (replacing this note's generic "attack directly"): does Elboim's
argument run for CORRIDOR-RESTRICTED or W-box-crossing times? The abstract states
point-to-point only. If the method localizes, its output feeds this note's converter
through the level geometry. HONEST SCALING CAVEAT, unresolved: even a localized
C/sqrt(log W) per corridor enters the pair-collision arithmetic at a sqrt(log) gain
only; whether the aggregated corridor-pair sum then improves on Var >= c log n at all
REQUIRES THE ARITHMETIC TO BE RUN and is not claimed here. Weight-regularity also
matters: the bound needs absolutely continuous weights, one assumption stronger than
the campaign's bounded-weights baseline.

## Localization verdict from reading the actual proof (2406.10971 pp.1-4, same day)

Elboim's mechanism, read from the paper (not the abstract): a CONTINUOUS Mermin-Wagner
perturbation tau_r(e) = r/(2^k sqrt(log n)) on dyadic ANNULI Lambda_k, k in
[log2 sqrt(n), log2 n], ANCHORED AT THE ENDPOINT; total L2 cost ||tau_r||^2 <= C
(constant across the ~log n scales, so Lemma 2.1's e^{||tau||^2/2} stays bounded);
Lemma 3.1 gives every length-2^k path inside Lambda_k a gain >= delta_0 r/(2 sqrt(log n))
whp (at least half its edges sit in B_delta0, Binomial), and a geodesic from the endpoint
crosses EVERY annulus, so the total drift per unit r is ~ sqrt(log n) - the continuous
sweep pushes T through any unit interval in r-measure ~ 1/sqrt(log n) (Lemma 3.3
integrates over r). The union bound over paths (|P_k| <= C 4^k 3^{2^k}) is free.

SPLIT VERDICT for the converter:
- ANCHORED (point-to-point) restricted times LOCALIZE ESSENTIALLY VERBATIM: for a
  corridor of length l with pinned endpoints, run the same annuli at scales
  [sqrt(l), l] around an endpoint - confinement only SHRINKS the path family (union
  bound improves), the annuli fit in a width-l corridor, and Q(S_corridor, 1) <=
  C/sqrt(log l) follows with the same absolute-continuity hypothesis.
- FREE-ENDPOINT crossing times (level-boundary corridor times, the object THIS note's
  converter consumes) DO NOT obviously localize: with the min taken over all entry/exit
  points on the faces, a crossing path can hug a face and DODGE the small central
  annuli; only the O(1) outermost scales are unavoidable, and O(1) scales lose the
  sqrt(log) accumulation entirely. Pinning entry/exit to recover anchoring costs a
  union over ~W^2 boundary pairs, and small-ball probabilities ADD under unions -
  unaffordable as stated.
RESIDUAL GAP, precisely: either (i) a free-endpoint variant of the annulus argument
(e.g. annuli anchored at the argmin entry point, chosen measurably - the perturbation
must then be adapted, which breaks Lemma 2.1's product structure as stated), or (ii) a
version of the converter that consumes ANCHORED corridor times only (re-derive the
level decomposition with pinned waypoints - pinning costs the waypoint union again, now
OUTSIDE the small-ball, where it may be affordable at fluctuation-scale tolerance:
NOT checked, half-page of arithmetic, genuinely open). This is the note's narrowest
surviving question and the only one with a plausible yes.

## The half-page, run (same day). Verdict: NO as posed - and the obstruction is
## self-similar. THE NOTE CLOSES.

Setup: level height W, disjoint corridors C1, C2 crossing a level, tolerance delta ~ 1.
Condition on the environment OUTSIDE the corridors. Given the outside, a corridor's
competitiveness is the event that
    F_i := min over waypoint pairs (a, b) on C_i's faces of
           [ outside-prefix(a) + S_{C_i}(a -> b) + outside-suffix(b) ]
is within 2 delta of the other corridor's F_j - and F_1, F_2 are conditionally
independent (disjoint corridor supports; the outside is frozen). Two ways to use
Elboim's anchored bound Q(S_{C_i}(a->b), 1) <= C / sqrt(log W):

(i) UNION OUTSIDE THE SMALL-BALL: for FIXED waypoints the collision probability is
<= C/sqrt(log W); the union over ~W^2 pairs per corridor (W^4 for the pair event)
costs W^4 against a sqrt(log W) gain - fatal by any margin.

(ii) COLLAPSE THE WAYPOINTS INTO THE MIN: the honest event compares F_1 with F_2, and
F_i is a MINIMUM of W^2 (dependent) anchored completions. A minimum does not inherit
its summands' concentration function - bounding Q(F_i, delta) is again restricted-min
anticoncentration, ONE LAYER UP, and Elboim's anchoring cannot reach it because the
anchor IS the argument being minimized over.

CONCLUSION, and the attempt's final sentence: the anticoncentration wall is
SELF-SIMILAR - it reproduces at every layer where a free endpoint (equivalently, a
minimum over attachment points) appears, and endpoint-anchored methods penetrate
exactly one layer (the layer where geometry pins the point for free: the global
endpoints, which is Elboim's theorem and no further). A D-side improvement through this
family requires an anticoncentration mechanism stable under taking minima over
polynomially many attachments - which is a different kind of statement from any in the
current toolkit (it is, again, what the exponent's renormalization structure asserts).
Every route this note opened is now closed with its failure named. Status: attempt
complete, dead ends recorded, no claims. chi = 1/3 exactly where Newman-Piza left it.
