# (L2') measured for the first time: the conditional increment is Gaussian-shaped, kappa4 ~ 3,
# flat over the range measured. Plus a correction to my own fire-4 target map.
# 2026-08-15 pass 5. STATUS: first empirical look at (L2'), honestly
# bounded; and a retraction of a framing I published two fires ago. chi = 1/3 UNMOVED.

## 0. First, the correction. My fire-4 target map was wrong.

Fire 4 closed with "the campaign's honest remaining target is singular and unchanged:
rho_n = Q_n^2/D_n = O(1), i.e. H1+H3." That is the PRE-REDUCTION framing, and CRUX 9.3 had already
retired it. Quoting the campaign's own text rather than my summary of it:

  "the chaos strength is NOT where the difficulty lives - constant strength, the only strength a
   BSS-type construction yields, suffices once (L1)+(L2) hold. Section 2's eps <~ log^4 n/n^2 is
   therefore an artifact of routing the fourth moment through a lossy envelope, not an intrinsic
   demand of the engine"

and 9.2's consequence, verbatim: "Under (L1)+(L2), CONSTANT-strength chaos delivers the halving.
No envelope, no fluctuation-scale concentration, no value of chi is used anywhere."

So rho is not the remaining target; it is an artifact of the lossy route. THE CORRECT LEDGER is
9.5's, after the REF-W1/REF-W2 repairs:

  (L1')  E[Delta_L^2 | U_L] <= beta Var(X_n)                    THE WALL (9.3: "the wall persists
                                                                INSIDE (L1)")
  (L2')  E[Delta_L^4 | U_L] <= kappa4 (E[Delta_L^2 | U_L])^2    scale-free SHAPE condition
  (L3)   Sum_L P(U_L) <= C_occ M                                worth exactly one power of n

and then eps <= 1/(16 kappa4 beta^2 C_occ), a CONSTANT.

This correction does not disturb fires 1-4's mathematics. It CONFIRMS their convergence: fire 1's
R = D_Mn/D_n, fire 3's constant-A doubling, and (L1') are the same object, and 9.3 independently
calls it the wall. What it retires is my fire-2 sentence "the wall is rho alone" (already
superseded by fire 3) and my fire-4 sentence naming rho as the remaining target. Both struck.

WHAT THE CORRECTION OPENS: (L2') is the one condition in the reduction that is NOT the wall, that
9.5 prices as "a scale-free shape condition", and that nobody in this campaign has ever examined.
That is the gap this note walks into.

## 1. Why a laptop can say anything about (L2') when it cannot say anything about chi

The campaign's standing caveat is that its machine-checks "test bookkeeping, never the regime" -
the construction's own hypotheses first hold around l_0 ~ 1e18. That caveat is about EXPONENTS: no
laptop separates n^{2/3} from n.

(L2') is different in kind. It is scale-free - a fourth moment against the square of a second, with
no exponent in it. A small lattice cannot tell us the value of chi, but it can tell us whether a
dimensionless shape statistic is near a constant or drifting. That is the whole reason this
measurement is worth running and the reason its result is worth less than it looks: see section 3.

## 2. The measurement

Setup mirrors the campaign's earlier Dijkstra checks for comparability: iid U[1,2] weights on Z^2,
exact Dijkstra geodesics, X = T((0,0),(N,0)) in a box of half-height H = 1.5 N^{3/4}, blocks tiling
the strip, U_L = {the original field's geodesic meets L}, Delta_L = X^L - X after resampling every
weight in L. Zero boundary escapes in every run (geodesics never reached the box edge, so no
truncation bias). Seeds 20260815 / 20260816.

AXIS-BLOCK CONDITIONAL KURTOSIS kappa4 = E[Delta^4|U] / (E[Delta^2|U])^2, medians:

    N = 16, n = 4, 900 reps    kappa4 = 2.886
    N = 24, n = 6, 700 reps    kappa4 = 2.973
    N = 32, n = 8, 500 reps    kappa4 = 2.927

Flat, no drift, and sitting at 3 - the Gaussian value. Off-axis blocks at N=16 gave a median 2.663
with a max of 3.815, i.e. the same order, noisier, as expected from fewer conditional samples.

POWER DIAGNOSTIC, run because a kurtosis cap fails through a RARE large increment and a few hundred
samples has almost no power to see one. For each axis block: what share of sum(d^4) comes from the
single largest |d|? If m4 is one observation wearing a moment's clothes, kappa4 ~ 3 would mean only
"no heavy tail was sampled", which is a different claim.

    N=16, 2500 reps: n_cond 2301-2416 per block, top1 share 0.015-0.024, top5 0.061-0.086,
                     kappa4 2.847-3.059, bootstrap 5-95% within [2.72, 3.20]
    N=24, 1800 reps: n_cond 1794-1800 per block, top1 share 0.025-0.035, top5 0.087-0.107,
                     kappa4 2.919-3.038, bootstrap 5-95% within [2.75, 3.22]

So m4 is BULK-CARRIED, not one point, and every interval contains 3. The diagnostic also
self-flagged correctly: the one under-sampled block (n_cond = 179) shows top1 share 0.113 and a
visibly wider interval [2.67, 3.52], exactly the signature it was built to detect.

## 3. What this is worth, and it is much less than it looks

DOES NOT SHOW (L2'). Three limits, each of which alone would be enough to refuse the inference:
 - RANGE. N in {16, 24, 32} is a single doubling. The engine's own hypotheses first hold around
   l_0 ~ 1e18. Reporting kappa4 ~ 3 "for planar FPP" would extrapolate 16 orders of magnitude past
 - POWER, and this is the binding one. With ~2000 conditional samples the measurement can see a
   contamination of probability q >~ 1/2000 and is blind below it. (L2') fails through a rare heavy
   increment; a tail at q = 1e-6 is invisible here and would leave every number above unchanged.
   The result is CONSISTENT WITH (L2'), which is not evidence FOR it at the tail.
 - GEOMETRY. These blocks are 4x4 to 8x8, roughly square. The engine's blocks are n x W with
   W = sqrt(n Q) - a very different aspect ratio, and the conditional occupation structure that
   drives the shape is exactly what the aspect ratio controls.

A FOURTH LIMIT, FOUND BY RUNNING THE ARTIFACT TEST ON MY OWN NUMBER, AND IT IS THE ONE THAT
DEFLATES IT. kappa4 ~ 3 is a suspicious number, so I asked the strongest way it could be an
artifact: if the geodesic seldom reroutes, Delta is just sum_{e in gamma cap L}(w'_e - w_e), a sum
of a few iid centred uniforms, Gaussian by CLT with kurtosis 3 as pure arithmetic and no FPP
content whatever. Measured (seed 20260817, comparing each actual Delta against the no-reroute
prediction Delta_0 computed on the original geodesic's edges inside L):

    N=16, n=4:  |gamma cap L| = 3.94 mean,  reroute fraction 0.170,
                kappa4(Delta) 2.904, kappa4(Delta_0) 2.891, kappa4(Delta | rerouted) 3.018,
                rerouted share of E[Delta^2] 0.153
    N=24, n=6:  |gamma cap L| = 6.04 mean,  reroute fraction 0.388,
                kappa4(Delta) 3.000, kappa4(Delta_0) 2.924, kappa4(Delta | rerouted) 3.023,
                rerouted share of E[Delta^2] 0.355

The artifact hypothesis is PARTLY refuted and PARTLY confirmed, and the confirmed part is what
matters. Refuted: rerouting is not rare - it happens in 17 to 39 percent of resamples, rises
sharply with block size, and carries 15 to 36 percent of the conditional second moment, so this is
not a pure no-reroute CLT, and kappa4 stays ~3.02 even restricted to the rerouted (i.e. genuinely
FPP) subpopulation. Confirmed, and decisive: the geodesic spends only about 4 to 6 EDGES inside
these blocks. A fixed-length sum of L iid uniforms has kurtosis exactly 3 - (6/5)/L, namely 2.70 at
L = 4 and 2.80 at L = 6; mixing over a varying L pushes it back up toward 3. Every number I
measured sits within roughly 0.1-0.2 of that trivial arithmetic. So at this block size the
statistic cannot resolve FPP shape from "a handful of uniforms added up", and the agreement with 3
is close to guaranteed before any percolation enters.

WHAT THEREFORE SURVIVES, which is less than section 2 looked like and more than nothing:
 - The measurement does NOT refute (L2'), and the cheap refutations - drifting kurtosis, m4 carried
   by one observation, a visibly heavy conditional tail - did not occur. A refutation would have
   killed the 9.5 reduction outright, so the null has some value for the reduction's viability.
 - But kappa4 ~ 3 is NOT evidence for (L2') at these block sizes, because a trivial mechanism
   predicts nearly the same number. I am recording my own reading as deflated rather than leaving
   section 2 to be quoted.
 - The genuinely informative measured trend is the REROUTING one: fraction 0.170 -> 0.388 and
   second-moment share 0.153 -> 0.355 as the occupation goes 3.94 -> 6.04 edges. The FPP content of
   this statistic grows fast with block size, which says the experiment is least informative
   exactly where I ran it, and that a larger-block run is worth real compute rather than a laptop
   afternoon.

## 4. The Gaussian reading, and why it does NOT make (L2') easier

kappa4 ~ 3 invites the thought that Delta_L | U_L is asymptotically Gaussian - which would follow
from a CLT for the single-block resampling increment, and would reframe (L2') from a moment
inequality into a distributional-limit question that may already be studied.

That reframing is a trap and I am recording it as one rather than as a lead. Convergence in
distribution does NOT give convergence of fourth moments; it gives it only under uniform
integrability of Delta^4. And uniform integrability of the fourth power IS the tail control that
(L2') is asking for. So the CLT route does not dodge the difficulty, it renames it - the same
shape as 9.8's finding that (L1') is the variance ratio rather than a new local condition, and the
same shape as fire 3's finding that the continuity route's base case is the wall.

kappa4 ~ 3 is therefore a description of the bulk, and (L2') is a statement about the tail. The
measurement speaks to the first and is nearly silent on the second. Anyone who cites this note as
support for (L2') is citing the bulk for a tail claim.

## 5. Disposition

NEW HERE, in descending order of how much I would stand behind it:
 1. The correction of the target map. rho is an artifact of the lossy fourth-moment route; the
    ledger is (L1') wall / (L2') shape / (L3) one power of n. This rests on reading CRUX 9.2/9.3/9.5
    directly and needs no measurement.
 2. The rerouting trend: fraction 0.170 -> 0.388 and second-moment share 0.153 -> 0.355 as block
    occupation goes 3.94 -> 6.04 edges. Measured, and it could have come out flat.
 3. The recorded trap that the Gaussian reading relocates rather than removes the tail control
    (a CLT gives moment convergence only under uniform integrability of Delta^4, which IS the tail
    control (L2') asks for).
 4. The kappa4 ~ 3 reading itself - DEFLATED by my own artifact test and not to be cited as
    support for (L2').

A NOTE ON INDEPENDENCE, since three of my checks agreed. The power diagnostic and the first-pass
sweep share my framing and their agreement is one anchor measured twice, not corroboration. The
artifact test is the only one that came at the number from a different direction - it withheld the
leading hypothesis and asked what a trivial mechanism would predict - and it is the only one that
moved the verdict. That is the check that earned its keep.

NOT CLAIMED: that (L2') holds. Not at this range, not at this power, not at this aspect ratio, and
not at this block occupation. chi = 1/3 UNMOVED, and (L1') is still the wall - untouched by
anything here.

NEXT, if anyone picks this up, and the artifact test reorders the priorities: the first fix is
BIGGER BLOCKS, not more reps. At 4-6 geodesic edges per block the statistic is dominated by
low-dimensional CLT arithmetic; the rerouting trend says the FPP content is still climbing steeply
at n = 6, so the experiment only starts being about FPP somewhere above it. After that, the
engine's aspect ratio (W ~ sqrt(n Q), tall thin blocks rather than square) and then an order of
magnitude more conditional samples on ONE axis block, since the tail is where the claim lives and
the bulk is already well estimated. This wants a research box, not a laptop afternoon.

[CORRECTED fire 6, and the recommendation above is WRONG - do not follow it. Bigger blocks cannot
discriminate anything, for a reason visible in the deflation's own formula: the trivial null has
kurtosis 3 - (6/5)/L, which CONVERGES TO 3 as the occupation L grows. (L2') holding also predicts a
bounded kurtosis near 3. So null and alternative converge to the SAME prediction, and enlarging the
blocks makes them less distinguishable, not more. I recommended the one axis along which the
experiment gets weaker.

THE RIGHT STATISTIC IS PAIRED, and it was already sitting in this note's own data. On each resample
both Delta (rerouting allowed) and Delta_0 (no-reroute, summed on the original geodesic's edges in
L) are observed, on the SAME weights with the SAME occupation. Delta_0 is therefore an EXACT
empirical null carrying the real occupation distribution - which is what the fixed-L formula could
not do. The FPP content is exactly

    EXCESS(n) := kappa4(Delta) - kappa4(Delta_0),

bootstrapped by resampling PAIRS, so the occupation confound cancels instead of being modelled.
See L2PRIME_PAIRED_EXCESS_20260815.md for the measurement.]

Related: CRUX_iteration_arithmetic.md 9.2/9.3/9.5 (the reduction, the ledger, the conditional
repair), MONOTONICITY_HAS_NO_CONSUMER_20260815.md (fire 4, whose closing target statement this
note corrects), CONTINUITY_BOOTSTRAP_20260815.md (fires 1-3).
