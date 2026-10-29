# Variance monotonicity points the wrong way for every consumer this campaign has, and the
# natural weakening of doubling (a density of good scales) is Kesten repackaged. Both should be
# taken off the target list. 2026-08-15 pass 4.
# STATUS: payoff audit + one derived consequence + the break that kills it. chi = 1/3 UNMOVED.

## 0. Why this note exists

Fire 93 (MONOTONICITY_PROBE_20260812.md) closed with monotonicity as "a genuinely separate,
plausibly softer target", and LOOP_STATE promoted it to the campaign's most concrete remaining
sub-problem. That verdict was about how hard monotonicity is to PROVE. Nobody asked what it would
BUY. Asking first is cheaper than proving, and the answer is: nothing any consumer in this
campaign wants.

## 1. The payoff audit. Three consumers, three failures.

Monotonicity is D_{n+1} >= D_n, hence D non-decreasing, hence R_n := D_{Mn}/D_n >= 1.

CONSUMER 1 - the (L1') premise / doubling. The engine needs beta = O(R_n), i.e. an UPPER bound
R_n <= A. Monotonicity delivers R_n >= 1, the opposite inequality. It is not a weak version of
doubling; it is doubling's mirror. Nothing about an upper bound follows.

CONSUMER 2 - the variance lower bound that rho = Q_n^2/D_n needs. Monotonicity gives
D_n >= D_{n_0} for n >= n_0, i.e. a CONSTANT floor. The unconditional Newman-Piza bound is already
D_n >= c log n, which is unboundedly stronger. Monotonicity is strictly weaker than what is
already on file.

CONSUMER 3 - stabilising the maintain-up window. The proposal was L(j+1) := L(j), licensed by
monotonicity. But the engine's output is U(j+1) = (M/2) U(j), so R(j+1) = U(j+1)/L(j+1) =
(M/2) R(j): the window ratio GROWS by M/2 per step and blows up in log n steps. Monotonicity does
not stabilise the window, it watches it diverge.

So of the campaign's three places where a regularity statement could be spent, monotonicity is
wrong-signed at one, dominated at another, and inert at the third.

[SCOPE OF THIS AUDIT, so the title is not read as more than it is. Three is the number of
consumers I could enumerate from the campaign's own reduction - (L1')/beta, rho's denominator, and
the maintain-up window. It is not a proof that no consumer exists. The other engine inputs ((L2')
kurtosis, (L3) block count, the localization tail, the occupation caps) are geometric statements
about geodesics, not regularity statements about the variance sequence, so a variance-monotonicity
hypothesis has no place to enter them - but that is a reading of the reduction, not a theorem.
Anyone who finds a fourth consumer overturns section 4's verdict, and that is the cheapest way to
attack this note.]

## 2. What monotonicity does give: doubling on a positive density of scales

This is the one non-trivial consequence I could find, and it is worth writing down before it is
killed in section 3, because it is the natural weakening anyone would reach for.

Take dyadic scales n_k = 2^k, k = 0..K, N = 2^K, and R_k := D_{n_{k+1}}/D_{n_k}. Then

    sum_{k<K} log_2 R_k  =  log_2 (D_N / D_1)                          (telescoping, exact)
                         <= log_2 (C N / d_1)  =  K + log_2(C/d_1)     (Kesten D_N <= C N)

and monotonicity gives log_2 R_k >= 0 for every k, so the summands are non-negative and Markov
applies:

    #{ k < K : R_k > 2^lambda }  <=  ( K + log_2(C/d_1) ) / lambda.

At lambda = 2: at least half of all dyadic scales satisfy Var(X_{2n}) <= 4 Var(X_n). So
constant-A doubling, which section 4bis of the continuity note identified as the wall itself,
holds unconditionally on a set of scales of density >= 1 - 1/lambda, GIVEN monotonicity.

ARITHMETIC CHECKED, including against instances built to break it. Swept K = 40 over five
sequences satisfying both hypotheses - n^{2/3}, n (Kesten-saturating), n/log n (BKS), and two
adversarial ones cramming all the growth into three scales and into a single scale. The
observation that would have shown Markov applied backwards is a measured bad-count EXCEEDING the
bound; none did. The Kesten-saturating row gives sum log_2 R_k = K exactly, so the average ratio
is exactly 2 and the density constant is not an artifact of slack.

## 3. The break: the density statement is Kesten repackaged, so it cannot improve on Kesten

The natural next move is to run the engine on the good scales. It does not work, and the reason is
visible in the derivation rather than in the geometry.

The telescoping identity is an EQUALITY: sum_k log_2 R_k = log_2(D_N/D_1). The only input that
turned it into a bound was D_N <= C N. So the density statement is a CONSEQUENCE of the global
linear bound, and a consequence cannot by itself prove anything stronger than what it came from -
using it to bound D_N is spending D_N <= C N to re-derive a bound on D_N.
[Stated precisely, because the absolute version would be too strong: this rules out the density
statement carrying the argument ON ITS OWN. It does not rule out some future argument that
combines the density with a genuinely new input, which would be a different claim standing on that
input. What it does say is that the density is not itself new information.]

Concretely: with S the good set, D_N/D_1 = prod_{k in S} R_k * prod_{k not in S} R_k. On S the
factors are at most 2^lambda; off S they are >= 1 and have NO upper bound - and bounding them is
exactly what was to be proved. One uncontrolled scale breaks the product, and the density
statement is silent about which scales are bad or how bad. The telescoping needs EVERY scale;
"most scales" buys nothing, because the product is not robust to a single unbounded factor.

The numeric sweep shows this directly: in every row, sum log_2 R_k equalled log_2(D_N/D_1) to the
digit. The budget IS the global bound. That equality is the whole obstruction in one line.

## 4. Verdict

DOWNGRADE monotonicity. It should come off the list of concrete targets, not because it is easy or
hard, but because no consumer in this campaign can spend it: wrong-signed for doubling, dominated
by Newman-Piza for the rho side, inert for the window. If someone proves it, the campaign's map
does not move.

DO NOT SPEND FIRES on "doubling at most scales" either. It is the natural weakening of the
wall-equivalent hypothesis and it is free given monotonicity, which is exactly why it is worthless
- it is derived from the linear bound and cannot beat it.

WHAT THIS LEAVES. After fire 3 closed the continuity route (base case = doubling = the wall) and
this fire removes monotonicity and the density weakening, the two "softer side problems" named on
08-12 are both accounted for - doubling is the wall (fire 89, re-confirmed fire 3), monotonicity
has no consumer (here).

[CORRECTED IN PLACE, fire 5 (same session). The paragraph originally continued: "the campaign's
honest remaining target is unchanged and singular: rho_n = Q_n^2/D_n = O(1), i.e. H1+H3, a
concentration envelope AT the fluctuation scale with a matching lower bound." THAT IS WRONG, and
it was wrong when written - CRUX 9.3 had already retired it. rho is the PRE-REDUCTION framing;
9.2's consequence reads verbatim "Under (L1)+(L2), CONSTANT-strength chaos delivers the halving.
No envelope, no fluctuation-scale concentration, no value of chi is used anywhere," and 9.3 calls
section 2's eps shortfall "an artifact of routing the fourth moment through a lossy envelope, not
an intrinsic demand of the engine." The correct ledger is 9.5's: (L1') is THE WALL, (L2') is a
scale-free shape condition, (L3) is worth one power of n. My error was summarising the campaign
instead of reading it - the third time in one session that reading the primary text rather than my
own summary produced the result. Nothing else in this note is affected: monotonicity's three failed
consumers and the density-is-Kesten break stand as written. See
L2PRIME_FIRST_MEASUREMENT_20260815.md.]

CAVEAT I am explicit about: sections 1 and 3 are audits of what the CAMPAIGN's engine can consume.
They are not claims that monotonicity is uninteresting as FPP mathematics - it is a natural
question, open even for the mean (arXiv 1202.2665), and fire 93's FKG obstruction stands. The claim
is only that proving it would not advance this program.

Related: MONOTONICITY_PROBE_20260812.md (the obstruction, which stands),
DOUBLING_IS_NOT_A_SIDE_DOOR_20260812.md (the sibling sub-problem, wall-equivalent),
CONTINUITY_BOOTSTRAP_20260815.md section 4bis (where doubling was re-identified as the base case).
