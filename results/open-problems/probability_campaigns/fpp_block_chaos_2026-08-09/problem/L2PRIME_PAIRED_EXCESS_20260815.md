# The paired excess: the right statistic for (L2'), and what it measures.
# Corrects fire 5's own "bigger blocks" recommendation, which pointed the wrong way.
# 2026-08-15 pass 6. STATUS: design correction + measurement with
# pre-registered read. chi = 1/3 UNMOVED.

## 1. Fire 5's next-step recommendation was wrong, and the reason is in its own formula

Fire 5 deflated its kappa4 ~ 3 reading by noting that a sum of L iid centred uniforms already has
kurtosis 3 - (6/5)/L (2.70 at L = 4, 2.80 at L = 6), so at 4-6 geodesic edges per block the
statistic cannot separate FPP shape from arithmetic. It then recommended BIGGER BLOCKS.

That recommendation is self-defeating. 3 - (6/5)/L CONVERGES TO 3 as L grows. (L2') holding also
predicts a bounded kurtosis near 3. Null and alternative therefore converge to the same number, and
enlarging the blocks makes them LESS distinguishable, not more. I recommended the one axis along
which the experiment gets weaker, and I recommended it in the same paragraph that contained the
formula showing why.

## 2. The right statistic was already in fire 5's data

On every resample two quantities are observed on the SAME weights, with the SAME geodesic and the
SAME occupation:

    Delta    = X^L - X, the actual increment, rerouting allowed
    Delta_0  = sum_{e in gamma cap L} (w'_e - w_e), the no-reroute increment on the ORIGINAL
               geodesic's edges inside L

Delta_0 is an EXACT empirical null. It carries the real occupation distribution, so the mixing
correction that made the fixed-L formula inapplicable is already inside it - no modelling needed.
Everything that distinguishes FPP from arithmetic is the rerouting, and rerouting is exactly the
difference between the two. So the FPP content of the shape is

    EXCESS(n) := kappa4(Delta) - kappa4(Delta_0),

bootstrapped by resampling PAIRS (i, i) rather than the two samples separately, so the occupation
confound cancels rather than being estimated.

PRE-REGISTERED READ, written before the run: EXCESS growing in n with bootstrap CIs clear of 0 is a
measured FPP shape effect. EXCESS flat, or CIs covering 0 at high power, says the kappa4 route is
arithmetic end to end and (L2') needs a different observable.

## 3. Measurement

Setup as in fire 5 (iid U[1,2] on Z^2, exact Dijkstra, axis blocks only, boundary escapes
discarded). Sizing was scaled from a MEASURED dress rehearsal, 11.2 ms per rep at N = 24, not from
an estimate. Seeds 20260818 / 20260819.

FIRST PASS (2.5% / 97.5% bootstrap, 1200 resamples):

    N    n   samples   occ   reroute  k4(Delta) k4(Delta_0)   EXCESS      95% CI
    16   4    11531   3.95    0.170     3.003     3.009      -0.0060  [-0.0877, 0.0699]
    24   6     8978   6.05    0.373     3.051     2.946      +0.1058  [ 0.0068, 0.2067]
    32   8     5791   8.03    0.512     3.098     3.011      +0.0872  [-0.0680, 0.2430]
    40  10     3705  10.09    0.601     3.005     2.868      +0.1371  [-0.0393, 0.3151]

READ, and it is deliberately conservative. Three of four CIs cover zero. The one that excludes it
(N = 24) does so marginally, and against four tests a single 95% exclusion is what chance produces
about 19 percent of the time - so it is not evidence on its own. The point estimates are weakly
positive for N >= 24 (+0.09 to +0.14) and show no trend that survives the error bars, even while
the reroute fraction climbs from 0.170 to 0.601. Sample counts fall with size, which is why the
intervals widen exactly where the effect should be largest: the first pass is underpowered by
construction.

HIGH-POWER PASS (2000-resample paired bootstrap; reps sized from the measured first-pass
half-width, not guessed):

    N    n   samples   occ   reroute  k4(Delta) k4(Delta_0)   EXCESS         95% CI      halfwidth
    24   6   106134   6.04    0.383     3.048     2.992      +0.0557  [0.0263, 0.0843]    0.029
    40  10    45345  10.09    0.605     3.106     2.920      +0.1855  [0.1290, 0.2403]    0.056

THE PRE-REGISTERED CRITERION IS MET. Both intervals are clear of zero, and the excess more than
TRIPLES from N = 24 to N = 40 while occupation goes 6.04 -> 10.09 and the reroute fraction 0.383 ->
0.605. So there IS a measured FPP shape effect in the conditional fourth moment: rerouting fattens
it relative to a null built from the same weights and the same occupation. The first pass's null
result was underpowering, not absence - the point estimates were already +0.09 to +0.14 there and
the intervals simply could not resolve them.

THE DECOMPOSITION, which I checked before believing the trend and which weakens it. The excess grows
for TWO reasons in roughly equal measure: kappa4(Delta) rises 3.048 -> 3.106 (+0.058), and
kappa4(Delta_0) FALLS 2.992 -> 2.920 (-0.072). The null moving is not what a clean "FPP content
grows" story predicts, and it runs against the fixed-L formula, which would send the null UP toward
3 as occupation grows (2.80 at L = 6, 2.88 at L = 10). The likely reason is occupation VARIABILITY
differing between the two sizes - mixing sums of different lengths raises kurtosis, and the mix
changes with geometry - but I did not measure that, so it is a hypothesis. Read the excess as real
and its GROWTH as half-explained.

WHY THE EFFECT IS NOT AN ARTIFACT OF THE PAIRING, since Delta and Delta_0 are strongly dependent by
construction: the bootstrap resamples PAIRS, so the dependence is inside each resample rather than
across them. And the mechanism is the right one rather than a bookkeeping accident - X^L is a
minimum, so Delta <= Delta_0 pointwise, and as rerouting becomes common Delta becomes a min over
more competing paths and acquires a heavier LEFT tail. That is the FPP content, not a defect.

## 4. What this says about (L2') either way

Note first what is already interesting in the numbers regardless of significance: the reroute
fraction reaches 0.601 at N = 40 - the geodesic changes in a majority of resamples - and the
conditional fourth moment still sits within about a tenth of its no-reroute null. Whatever
rerouting does to the increment, it is not visibly fattening the fourth moment at these sizes. That
is mildly consistent with (L2') and it is the direction a refutation would NOT look like.

But the honest limits from fire 5 all still bind and one is worse here: the block occupation is
4-10 edges against an engine whose hypotheses start around l_0 ~ 1e18; the blocks are square rather
than the engine's tall thin W ~ sqrt(nQ); and a fourth-moment excess is a small difference of two
noisy fourth moments, which is the statistic least able to see a rare tail. None of this bounds
anything asymptotic.

## 5. Disposition

NEW HERE: the observation that fire 5's own deflation formula rules out its own recommendation
(null and alternative both converge to 3, so bigger blocks discriminate less); and the paired-excess
design, which removes the occupation confound by construction rather than by modelling it.

[QUALIFIED SAME NIGHT, fire 9 - read before quoting the claim below. The engine consumes ONLY the
POSITIVE part of the increment (CRUX 6d.1 D7: Theorem 8.1 holds verbatim with A2 replaced by
A2^+ = Sum E[((X^L - X)^+)^2]; 9.1 writes A4 the same way). What is measured below is
kappa4(Delta), the TWO-SIDED increment. And rerouting acts only DOWNWARD - Delta <= Delta_0
pointwise, with strict inequality exactly on the rerouting event - so everything rerouting does to
the distribution it does to the LEFT tail, which is not the tail the engine reads. Fire 9 also
proves an exact cap on the positive part, (Delta)^+ <= min{(Delta_0)^+, G} with G the gap to the
best path AVOIDING the block, so rerouting can only SHRINK the positive part. The prediction, filed
before the measurement: the same excess computed on (.)^+ will be at or below zero and will not show
this growth. If it holds, the effect below is real and lives where the engine never looks. See
POSITIVE_PART_IS_GAP_CAPPED_20260815.md.]

CLAIMED, on the pre-registered criterion and only that far: there IS a measured FPP shape effect in
the conditional fourth moment. Rerouting fattens kappa4 relative to a same-weights same-occupation
null, by +0.056 [0.026, 0.084] at N = 24 and +0.186 [0.129, 0.240] at N = 40. This is the first
positive measurement anyone in this campaign has taken on (L2'), and it exists only because the
statistic was re-designed - the same data read the un-paired way said nothing.

WHAT IT DOES NOT SAY, and the gap is the whole question. (L2') asks whether kappa4 stays BOUNDED.
kappa4(Delta) itself is 3.048 and 3.106 - still near Gaussian, still bounded, moving by six
hundredths over the range measured. What grows is the EXCESS over the null, and it grows partly
because the null falls. Two points cannot establish a rate, and extrapolating one would be the
fattens the conditional fourth moment, and whether it fattens WITHOUT BOUND - which is what would
break (L2') - is untouched, but is now a question with a measurable handle on it rather than an
untested hypothesis.

THE OBVIOUS NEXT MEASUREMENT, and it is cheap now that the design is right: three or four more
occupation points with matched sample counts, and a separate read of the occupation VARIANCE at
each size, to settle whether the null's fall is a mixing artifact. If the excess keeps climbing
after the null is controlled for, that is the first real evidence against (L2') - and (L2') failing
would take the 9.5 reduction with it.

chi = 1/3 UNMOVED. (L1') is still the wall and nothing here touches it.

Related: L2PRIME_FIRST_MEASUREMENT_20260815.md (fire 5, whose recommendation this corrects in
place), CRUX_iteration_arithmetic.md 9.5 (the reduction that makes (L2') a target at all).
