# The positive part of the block increment is capped by the gap to the best avoiding path -
# and that means fire 8 measured a functional the engine does not consume.
# 2026-08-15 pass 9. STATUS: elementary exact decomposition + a
# pre-registered prediction that would deflate my own fire-8 result. No compute used (throttle).
# chi = 1/3 UNMOVED.

## 1. The decomposition (elementary, exact, no hypotheses)

Fix a block L and split the paths from 0 to the endpoint by whether they use an edge of L:

    A  := min over paths THROUGH L of T_w        A' := the same min under w' (L resampled)
    C  := min over paths AVOIDING L of T_w

C is UNCHANGED by the resample - paths avoiding L touch no resampled edge - so the same C appears
in both fields. Hence

    X = min(A, C),      X^L = min(A', C).

On the touching event U_L the geodesic uses L, so X = A and A <= C. Therefore, on U_L,

    Delta_L = min(A', C) - A.

Two consequences, both immediate:

  (i)  UPPER CAP BY THE GAP.  Delta_L <= C - A =: G_L,  the gap between the best path avoiding L
       and the geodesic. So the POSITIVE part obeys  (Delta_L)^+ <= G_L  on U_L.
  (ii) UPPER CAP BY THE NO-REROUTE INCREMENT.  The original geodesic gamma lies in the through
       class, so A' <= T_{w'}(gamma) = A + Delta_0 where Delta_0 = sum_{e in gamma cap L}(w'_e-w_e).
       Hence Delta_L <= Delta_0, and (Delta_L)^+ <= (Delta_0)^+.

Together:

    0 <= (Delta_L)^+ <= min{ (Delta_0)^+ , G_L }        on U_L.                            (*)

Nothing here needs curvature, chaos, a variance bound, or planarity - only that resampling inside L
leaves the avoiding class alone. G_L is a purely geometric competition quantity: how much slack the
geodesic has over the best route that skips the block.

## 2. Why this matters, and it is uncomfortable for my own last fire

CRUX 6d.1 (D7), the one thing the referee kept out of sections 6-6c, is explicit: "The engine
consumes ONLY the positive part: step (4)'s kappa-term and steps (6)-(8) all use (.)^+, so Theorem
8.1 holds verbatim with A2 replaced by A2^+ := Sum E[((X^L - X)^+)^2] <= A2." And 9.1 already writes
A4 with the positive part.

So the functionals the engine actually consumes are built from (Delta_L)^+, not from Delta_L.

FIRE 8 MEASURED kappa4(Delta), NOT kappa4(Delta^+). Its result - that rerouting fattens the
conditional fourth moment, excess +0.056 at N=24 and +0.186 at N=40, both clear of zero - is a
statement about the two-sided increment. But rerouting acts ONLY DOWNWARD: by (ii), Delta <= Delta_0
pointwise, and rerouting is exactly the event where the inequality is strict. So everything
rerouting does to the distribution it does to the LEFT tail.

That is entirely consistent with what I measured and it undercuts the significance I gave it. A
heavier left tail raises kurtosis of the two-sided variable. It does not follow that the positive
part - which by (*) is squeezed between 0 and min(Delta_0^+, G_L), and which rerouting can only
SHRINK - gets heavier at all.

## 3. Pre-registered prediction, written before the measurement (compute is throttled tonight)

    PREDICTION. Repeating fire 8's paired-excess measurement on the POSITIVE PART, i.e.
        EXCESS^+ := kappa4((Delta)^+ | U) - kappa4((Delta_0)^+ | U),
    the excess will be at or below zero, and in any case will NOT show the growth seen on the
    two-sided statistic (+0.056 -> +0.186 as occupation goes 6.04 -> 10.09).

    [AMENDMENT, filed 2026-08-15 fire 10 BEFORE running the measurement and before seeing any
    positive-part number. The prediction as written above does not account for an ATOM AT ZERO, and
    the omission cuts against it. (Delta)^+ has mass at 0 whenever Delta <= 0, and for a variable
    with P(Y=0) = 1-q one has kappa4(Y) = kappa4(Y | Y>0)/q - the atom inflates kurtosis by 1/q.
    Rerouting pushes increments DOWN, so P(Delta>0) < P(Delta_0>0), i.e. q_Delta < q_0, and
    EXCESS^+ therefore gets a MECHANICAL positive push of roughly the ratio q_0/q_Delta with no
    tail-fattening whatever. A positive EXCESS^+ would therefore NOT by itself refute the reasoning
    in section 2.
    SO THE TEST IS SPLIT, and both halves are pre-registered here:
      (a) EXCESS^+ := kappa4((Delta)^+) - kappa4((Delta_0)^+)  - reported, but expected to be
          contaminated by the atom and NOT read as evidence on its own;
      (b) EXCESS^{+|+} := kappa4(Delta | Delta>0) - kappa4(Delta_0 | Delta_0>0), which removes the
          atom from both sides and isolates SHAPE. This is the statistic the prediction is really
          about: it should be at or below zero and should not grow.
    Also reported for the record: q_Delta and q_0 themselves, so the size of the mechanical effect
    is visible rather than inferred.]

    IF THE PREDICTION HOLDS: fire 8's effect is real but lives in a part of the increment the engine
    never looks at, and its practical significance for (L2') collapses. The honest main claim becomes
    "rerouting fattens the two-sided increment and leaves the engine's functional alone."

    IF THE PREDICTION FAILS - excess^+ positive and growing - then rerouting fattens the functional
    the engine DOES consume, and fire 8's result keeps its force and gains a mechanism. That would
    be the stronger outcome for the campaign and the worse one for (L2').

Either way the measurement is cheap once compute clears: the same runs, with (.)^+ applied before
the moments, plus G_L recorded so (*) can be checked as a control (the code already computes the
avoiding-class minimum implicitly - it is X^L when the resample makes the block unattractive).

## 3bis. RESULT (2026-08-15 fire 11): MY PREDICTION IS REFUTED - and the refutation has a
## confound of its own, found by breaking it, pointing the same way.

CONTROL FIRST, as pre-registered. The two-sided excess had to reproduce fire 8 or the run is not
to be interpreted: measured +0.0455 [+0.0049, +0.0869] at N=24 and +0.1398 [+0.0573, +0.2247] at
N=40, against fire 8's +0.0557 and +0.1855. Overlapping intervals, same sign, same growth. The run
reproduces.

    N   samples   occ   reroute  q_Delta  q_0    q_0/q_Delta   EXCESS      EXCESS_p    EXCESS_pp
    24   61227   6.04   0.384    0.5049  0.6439    1.2755      +0.0455     +1.8375     +0.3329
                                                               [.005,.087] [1.74,1.94] [.280,.380]
    40   24760  10.08   0.606    0.5065  0.7337    1.4487      +0.1398     +2.6946     +0.5603
                                                               [.057,.225] [2.48,2.91] [.459,.664]

THE AMENDMENT WAS RIGHT ABOUT THE ATOM. q_0/q_Delta is 1.28 and 1.45, and EXCESS_p is +1.84 and
+2.69 - an order of magnitude larger than anything else here, exactly the mechanical inflation the
amendment predicted. Without the split, that number would have been uninterpretable and I would
have had to explain it after the fact.

THE PREDICTION FAILS ON THE STATISTIC I NOMINATED. EXCESS_pp = +0.3329 [0.2801, 0.3804] and
+0.5603 [0.4591, 0.6643] - positive, clear of zero, GROWING, and LARGER than the two-sided effect.
I predicted at or below zero and not growing. That is the branch I called the worse outcome for
(L2'): rerouting fattens the functional the engine actually consumes, more than it fattens the
two-sided increment.

BUT I AM NOT BANKING THAT REFUTATION YET, because breaking it found a confound I did not anticipate
when I nominated the statistic, and it pushes the same direction as the effect. EXCESS_pp truncates
each variable at ITS OWN zero. Rerouting shifts Delta down, so zero sits further into Delta's upper
tail and truncates it HARDER - measured, q_Delta = 0.505 against q_0 = 0.644, so Delta keeps half
its mass where Delta_0 keeps two thirds. Truncating a distribution further right mechanically raises
kurtosis (a normal cut at its mean is the half-normal, kurtosis ~3.87; cut further right it tends
toward an exponential, kurtosis 9). And {Delta>0} is a strict SUBSET of {Delta_0>0}, so the pairing
I relied on is broken by the conditioning itself. So EXCESS_pp mixes SHIFT with SHAPE, and I cannot
tell from it how much of +0.33/+0.56 is either.

THE CLEAN TEST, pre-registered and running: compare at MATCHED SELECTION STRENGTH - keep the top q
fraction of each variable with the SAME q for both (q = q_Delta, the smaller), so neither is cut
harder. EXCESS_mf at or below zero means the refutation was the shift and my prediction survives on
shape; EXCESS_mf positive and growing means it is genuine shape in the engine's own functional and
the prediction is refuted for real. Raw pairs are being saved this time so further cuts need no
re-run.

HONEST STANDING RIGHT NOW: my fire-9 prediction is refuted on the statistic I chose, and the choice
was flawed. Both of those are true at once and I am not using the second to soften the first - the
prediction failed. Whether the underlying claim (rerouting leaves the engine's functional alone)
also fails is what EXCESS_mf decides.

## 3ter. MATCHED-FRACTION RESULT (fire 13): the prediction is refuted ROBUSTLY, my confound
## reasoning was BACKWARDS, and the fire-9 mechanism is wrong in a way that matters.

N=24, computed from the saved pairs while the N=40 collect was still running (61227 samples,
occ 6.04, reroute 0.384, q_Delta 0.5049, q_0 0.6439):

    EXCESS_pp (own-zero cut)              +0.3329  [+0.2799, +0.3824]   clear of 0
    EXCESS_mf (MATCHED fraction, q=.5049) +0.9003  [+0.8469, +0.9506]   clear of 0
    kept counts 30912 vs 30912 - equal by construction, so neither side is cut harder.

I EXPECTED REMOVING THE CONFOUND TO SHRINK THE EFFECT. It nearly TRIPLED it. So my confound
argument in 3bis had the direction WRONG, and the reason is specific: I reasoned "truncate further
right and kurtosis rises, normal -> half-normal 3.87 -> exponential 9". That is the unbounded case.
Delta_0 is a sum of ~6 iid (w'-w) each in [-1,1] - BOUNDED, observed range -3.918 to +4.213 - and
truncating a bounded variable further right leaves a shorter interval and drives it toward UNIFORM,
kurtosis 1.8. Measured directly, kurtosis against kept fraction q:

      q      k4(Delta_0)  k4(Delta)   excess
    0.90        3.4225     3.3925     -0.03
    0.75        3.1860     4.0678     +0.88
    0.6439      2.7538     3.8537     +1.10
    0.5049      2.1867     3.0872     +0.90
    0.35        1.6844     2.2000     +0.52
    0.20        1.3426     1.5708     +0.23
    0.10        1.1737     1.2809     +0.11

Monotone DOWN in q for both, exactly opposite to what I asserted. So EXCESS_pp was UNDERSTATING the
effect (it cut Delta_0 less hard, leaving its kurtosis higher), not inflating it.

WHAT THE CURVE SAYS, and it is more than a single number. The excess is positive at every matched
fraction from 0.10 to 0.75, peaks near q ~ 0.64 at +1.10, and only vanishes at q = 0.90 where almost
nothing is truncated (-0.03, i.e. zero). Read together with the two-sided excess (+0.046): keeping
everything, the effect is small and left-tail-driven; drop the bottom decile and it disappears;
truncate to the upper half or two-thirds and a LARGER effect appears that is not the left tail at
all. Those are two different phenomena and only the second lives in the engine's functional.

THE MECHANISM, AND IT INVERTS SECTION 2's REASONING. Section 2 argued the positive part is
"squeezed between 0 and min(Delta_0^+, G_L), and which rerouting can only SHRINK", concluding it
cannot get heavier. That inference is FALSE, and the decomposition of section 1 is what shows why:
(Delta)^+ = min(Delta_0, G)^+ with G RANDOM. Shrinking by a random amount is not taming - it is
MIXING. A variable capped at a randomly varying ceiling is a mixture over ceilings, and mixtures
have HIGHER kurtosis than their components at matched scale. So the gap cap I derived does not
protect (L2'); by making the cap random it is a candidate mechanism for BREAKING it. The structure
was right and the conclusion I drew from it was exactly backwards.

STANDING: my fire-9 prediction is refuted robustly - across truncation schemes, and by a larger
margin once my own directional error is removed. The rerouting effect reaches the functional the
engine consumes. This is the worse branch for (L2'), and (L2') failing takes CRUX 9.5's reduction
with it. NOT YET SETTLED: whether the excess GROWS with block size in the matched statistic - N=40
is still computing, and growth is what separates "a constant kurtosis penalty the engine can absorb
into kappa4" from "kappa4 unbounded", which is the thing (L2') actually forbids. One point cannot
say. HYPOTHESIS, not result: the random-ceiling mixture mechanism above.

## 3quater. READ THE LEVELS (fire 13, N=40 landed). THIS OVERTURNS THE LAST TWO SECTIONS'
## FRAMING, AND (L2') LOOKS FINE.

Everything above reports a DIFFERENCE of two kurtoses. Differences are only as stable as their
baseline, so I finally computed the LEVELS - which is what (L2') is actually about, since (L2')
asks whether a kurtosis is BOUNDED, not whether it exceeds something.

    N    occ    k4(Delta) two-sided   k4(Delta^+) with atom   k4(Delta_0^+)   A4/(A2^+)^2
    24   6.04         3.0564                 6.1143               4.2768         6.1143
    40  10.08         3.0854                 6.2345               3.5399         6.2345

(A4/(A2^+)^2 is the engine's own ratio and is the same statistic as k4(Delta^+) by definition.)

THE ENGINE'S FUNCTIONAL IS ESSENTIALLY FLAT: 6.1143 -> 6.2345, up 2 percent, while occupation rises
67 percent and the reroute fraction goes 0.384 -> 0.606. The two-sided kurtosis is flatter still,
3.0564 -> 3.0854. THE NULL, by contrast, FALLS hard: 4.2768 -> 3.5399.

So decompose the growth in the excess I have been reporting: EXCESS_p went +1.8375 -> +2.6946, a
change of +0.857. Of that, +0.120 is k4(Delta^+) rising and -0.737 is the null falling. EIGHTY-SIX
PERCENT OF THE "GROWTH" IS THE BASELINE MOVING. The same arithmetic applies to the matched-fraction
statistic, whose null is a truncation of that same falling Delta_0.

CONSEQUENCE, stated plainly against my own last two sections: (L2') asks for a CONSTANT kappa4. The
measurement says the engine's kappa4 is about 6.2 and moves 2 percent over the range measured. That
is CONSISTENT WITH BOUNDED - it is what (L2') holding looks like. The alarming picture in 3bis and
3ter - "positive, growing, larger than the two-sided effect, (L2') in trouble" - was an artifact of
reporting a difference against an unstable baseline. The rerouting effect on the LEVEL is real but
small (+0.12 in kurtosis units); the null's collapse is what produced the drama.

WHAT SURVIVES OF FIRE 9's PREDICTION. Its letter failed - there IS a positive excess in the engine's
functional at every cut, so "at or below zero" was wrong. Its substance was closer to right than the
last two sections allowed: rerouting does not meaningfully fatten the functional the engine
consumes. I refuted myself on the excess and then had to un-refute myself on the level.

WHAT SURVIVES OF 3ter's MECHANISM. The random-ceiling mixture argument explains why k4(Delta^+) sits
at ~6.2 rather than at the null's ~3.5-4.3 - an elevated LEVEL, which is a one-off cost the engine
absorbs into its constant kappa4. It does NOT predict growth, and no growth was found. So it is a
mechanism for the gap, not for a divergence.

THE LESSON, and it is the third instance tonight of one shape: a difference of two measured
quantities is not a measurement of either. The governor's "174/hour" was a differenced total; fire
8's excess growth was half the null falling; this is the same error at 86 percent. WHEN A BASELINE
CAN MOVE, REPORT THE LEVEL.

STILL NOT SETTLED: two sizes cannot establish boundedness any more than they can establish
divergence. k4 ~ 6.2 flat over one 67-percent step in occupation is evidence, not proof, and the
regime remains 10 orders of magnitude below l_0. What HAS changed is the direction of the worry:
nothing measured here threatens (L2').

## 3quinquies. FOUR-POINT LEVEL SWEEP (fire 15): IT SATURATES. (L2') is satisfied at these sizes.

Pre-registered before the run: k4(Delta^+) staying inside roughly 6.0-6.5 across occupation 4 -> 14
is real evidence for (L2') at these sizes; leaving the band upward by occ 14 puts (L2') back in
question; a low reading at occ 4 means the statistic is still settling.

    occ    N   samples  reroute   k4(D^+) = A4/(A2^+)^2    increment   k4(D) 2-sided   null
   3.95   16    76498    0.167    5.7339 [5.642, 5.838]        -           2.9590     5.0787
   6.04   24    61227    0.384    6.1143 [6.010, 6.223]     +0.3804        3.0564     4.2768
  10.08   40    24760    0.606    6.2345 [6.022, 6.439]     +0.1202        3.0854     3.5399
  14.05   56    14425    0.740    6.2290 [5.962, 6.509]     -0.0055        3.1219     3.0944

RISE, DECELERATE, FLAT. The increments are +0.38, +0.12, -0.01 across comparable multiplicative
steps in occupation (x1.53, x1.67, x1.39). The last step is flat to within a fifth of its own CI
width, and the sequence is inside the pre-registered band for occ 6-14. The occ-3.95 point sits at
5.73, just below the band and climbing into it - the "still settling at the low end" case that was
named in advance rather than after.

THE SHAPE ALSO RULES OUT LOG GROWTH, which was the honest worry three points ago: fit
k4 ~ a + b log(occ) to the first step and it predicts +0.46 for the second and +0.30 for the third.
Observed: +0.12 and -0.01. The deceleration is far faster than logarithmic.

A MECHANISM FOR THE SATURATION, offered as hypothesis not result: the reroute fraction runs
0.167 -> 0.384 -> 0.606 -> 0.740. Once nearly every resample reroutes, enlarging the block stops
changing the qualitative structure of (Delta)^+ = min(Delta_0, G)^+ - the random ceiling is active
almost always, so the mixture stops changing composition. Saturation of kappa4 tracking saturation
of the reroute fraction is what that predicts, and it is what the table shows.

AND THE CLEANEST ILLUSTRATION OF TONIGHT'S METHOD ERROR, now with four points. The EXCESS over the
null goes 5.7339-5.0787 = +0.655 at occ 4, to 6.2290-3.0944 = +3.135 at occ 14 - a 4.8x increase,
which read alone says "the effect is exploding". The QUANTITY goes 5.7339 -> 6.2290, up 9 percent
and flat over the last two points. The null fell 5.0787 -> 3.0944, and that fall is essentially the
entire "growth". Two fires were spent interpreting the first column.

STANDING ON (L2'). It asks for a CONSTANT kappa4. Across a 3.6x range of occupation and a reroute
fraction going 0.167 -> 0.740, the engine's own ratio A4/(A2^+)^2 saturates at about 6.23, and the
two-sided kurtosis (L2')'s literal statement is flatter still at 2.96 -> 3.12. THAT IS WHAT (L2')
HOLDING LOOKS LIKE, and it is now four points rather than two.

LIMITS, unchanged and stated so this is not read as a proof: occupation 4-14 edges against an
engine whose hypotheses first hold near l_0 ~ 1e18; square blocks rather than the engine's tall thin
W ~ sqrt(nQ); one weight law (U[1,2]); and the last point's CI is the widest of the four (14425
samples) so "flat" there is a point estimate inside noise, not a tight bound. Saturation over a
measured range is evidence for boundedness, never proof of it.

## 4. Break-it on section 1 before anyone builds on it

- IS C REALLY UNCHANGED? Yes by construction: the avoiding class is defined by using no edge of L,
  and only edges of L are resampled. The one thing to watch is the BLOCK BOUNDARY convention - an
  edge with one endpoint in L must be assigned to L or not, consistently, in both the resample and
  the class definition. If a boundary edge is resampled but counted as "avoiding", C moves and (i)
  fails. The campaign's blocks are edge-sets, so this is a convention to state, not a defect.
- IS X = A ON U_L? U_L is defined by the geodesic meeting L, so the minimising path is in the
  through class and X = A. If the geodesic is non-unique and the canonical selection picks a
  through-path while an avoiding path ties, then X = A = C and G_L = 0 - the cap is still valid,
  just vacuous. Ties do not break (*), they only make it uninformative.
- DOES (*) HELP ANYWHERE ELSE? It caps the positive part by a quantity with no occupation in it,
  which is the opposite failure mode from 6d(D1)'s B = Theta(n) - that bound is occupation-driven
  and provably tight. Whether E[G_L^2 | U_L] is any easier to control than the occupation route is
  NOT addressed here and should not be assumed; G_L small means the geodesic is nearly indifferent
  to the block, which is a statement about competition and is plausibly its own hard problem.
- NOVELTY [PASS RUN 2026-08-15 fire 12, and it goes AGAINST the decomposition being new]. Two
  literature searches. The closest live work is Dembin, Elboim and Peled, "On the influence of edges
  in first-passage percolation on Z^d" (arXiv 2307.01162, 2023): for compactly-supported weights with
  uniformly-positive density it asks which edges have probability at least eps of lying on the
  geodesic and bounds their number by O(eps^{-2d/(d-1)} (log|v|)^C) uniformly in v, answering a
  question of Benjamin-Kalai-Schramm (2003). That is precisely the edge-influence question, and
  bounding one edge's or one block's influence by the slack to the best ALTERNATIVE route is the
  natural instrument for it - so the min(A,C) decomposition is very likely folklore in that
  literature. Elboim also already appears in this campaign's own notes ("anchored methods e.g.
  Elboim penetrate one layer only"), so the lineage was adjacent all along.
  WHAT I CAN AND CANNOT SAY: I read search summaries, NOT the papers. No source stated the
  decomposition explicitly in what I saw. But it is elementary enough that failing to find it in a
  two-search sweep is weak evidence of novelty and strong evidence of nothing. VERDICT: treat as
  KNOWN IN KIND / folklore, not new. It remains useful HERE because the campaign did not have it and
  because of what it implies about which functional fire 8 measured - that implication is the
  contribution, not the identity. Anyone wanting to claim more must actually read DEP 2307.01162 and
  the BKS influence line.
  [superseded note kept for the record:] not found in this campaign (grepped problem/, CRUX, LOG for avoiding-path/competitor/gap
  language; the only hits are self-avoidance, a different notion, and 6d's off-U remark). NOT
  checked against the literature, where a comparison between the geodesic and the best avoiding path
  is a natural object and may well be standard. Do not call it new without that pass.

## 5. Disposition

NEW: the decomposition X = min(A,C), X^L = min(A',C) with C resample-invariant, and the resulting
two-sided cap (*) on the positive part; and the observation that fire 8 measured kappa4(Delta) while
the engine consumes kappa4 of the positive part, with the direction of rerouting (downward only)
predicting that the two results differ.

NOT CLAIMED: that (L2') holds or fails; that G_L is controllable; that fire 8's effect is or is not
in the engine's functional - that is the pre-registered measurement, not yet run. chi = 1/3 UNMOVED,
(L1') still the wall.

Related: L2PRIME_PAIRED_EXCESS_20260815.md (the fire-8 result this predicts against),
CRUX_iteration_arithmetic.md 6d.1 D7 (the positive-part correction this leans on) and 9.5.
