# Corrections to this ledger

Added 2026-09-08 by the session that commissioned it. Appended rather than edited into the rows, so
the original text stays as written. Counts below were recomputed from the files, not taken from the
build report.

## Verified independently

113 problem rows, 110 admitted, 110 attempts (every admitted row has one), 47 sources, 3 exclusions,
110 distinct dedup keys among the admitted rows. Zero overlap by (source_id, locator) against all
three earlier ledgers. Campaign total across the four ledgers: **777 distinct (source_id, locator)
pairs**. All of that matches the build report exactly.

## E0052 — the conjecture is MISSTATED, and the misstatement inverts an inequality

The row states the problem as:

> "Prove or disprove that P(sum_i X_i <= n + 1) >= 1 - 1/e."

The source says the opposite direction about the opposite event. Bandeira, *Ten Lectures and
Forty-Two Open Problems*, Section 4.8, Conjecture 4.33 (due to Feige), verbatim:

> "Given n independent random variables X_1, ..., X_n s.t., for all i, X_i >= 0 and E X_i = 1 we
> have Prob( sum_{i=1}^n X_i >= n + 1 ) <= 1 - e^{-1}"

So the conjecture is an UPPER bound on P(sum >= n+1), not a LOWER bound on P(sum <= n+1). These are
not complements: P(sum >= n+1) and P(sum <= n+1) overlap on the atom at exactly n+1, and that is
precisely where the extremal example puts its mass, so the swap is not harmless.

**How the error shows itself.** The row reports the extremal example as giving probability
1 - (n/(n+1))^n, decreasing to 1 - 1/e. That is correct for the SOURCE's event: with
X_i = n+1 w.p. 1/(n+1) and 0 otherwise, P(sum >= n+1) = P(K >= 1) = 1 - (n/(n+1))^n -> 1 - 1/e.
But under the row's own restatement the same law gives

    P(sum <= n+1) = P(K <= 1) = 2(n/(n+1))^n  ->  2/e = 0.7358,

computed here at n = 1, 2, 5, 10, 100, 1000, 10000 and converging cleanly to 2/e. Since
2/e = 0.7358 > 1 - 1/e = 0.6321, that law does NOT attain the row's stated bound and is not extremal
for it. Two downstream claims in the row therefore do not hold as written: that the bound "is
attained in the limit" by that example, and that "the conjecture cannot be improved to any constant
larger than 1 - 1/e".

**What survives.** The row's central observation does survive, once aimed at the correct statement:
this conjecture is genuinely stronger than the trivial bound. Markov gives
P(sum >= n+1) <= E[sum]/(n+1) = n/(n+1), which tends to 1, while the conjecture asserts <= 1 - 1/e.
So the row's application of the D-ledger lesson - test a conjectured inequality against the trivial
bound before believing it says anything - reaches the right conclusion by an argument aimed at the
wrong inequality. Its obstruction field (no common scale, so no single truncation; the reduction to
two-point laws blocked by non-compactness) is unaffected and reads sensibly.

**Fix**: restate E0052 as Feige's conjecture, P(sum_i X_i >= n+1) <= 1 - e^{-1}, and redo the
extremality remark against that event.

## E0064 — checked, the derivation holds

Rozikov's Problem 11 on strictly non-Volterra quadratic stochastic operators. The row's argument is
correct as far as it goes and I re-derived it: P_{ij,k} = 0 whenever k is in {i,j} forces
dV_k/dx_k = 2 sum_j P_{kj,k} x_j = 0 identically, so trace DV(x) = 0 everywhere; V is homogeneous of
degree 2, so Euler's identity gives DV(x*) x* = 2 V(x*) = 2 x* at a fixed point, i.e. the radial
eigenvalue is exactly 2; the remaining m-1 eigenvalues therefore sum to -2 and at least one has
modulus at least 2/(m-1). Since attractiveness needs every non-radial eigenvalue strictly inside the
unit disc, this obstruction bites only while 2/(m-1) >= 1, i.e. m <= 3, and says nothing for m >= 4.
The row's conclusion - that the source's non-attractiveness statement is unobstructed above
dimension 3 and may fail there - is what the computation supports, and its obstruction field
correctly notes that a bound is not a construction.

## Everything else is unaudited

Three of 110 admitted rows have been checked (E0052, E0064, and the E0044/E0028/E0043/E0049
exclusion reasoning read in passing). The other 107 have not. Note the ledger's exclusion discipline
looks right where I read it: E0044 was deliberately KEPT admitted because Lai-Lim refutes only
direction (a) of Bandeira's Open Problem 0.2 while the row concerns direction (b) - the same
distinction that caught the wrongly-dropped D0039, applied prospectively here.

## E0077 — settled (added 2026-09-08, later the same day)

The attempt row E0077-A001 reduced the conjecture to the sign of a deviation-matrix quadratic form
and called the non-reversible case open. It is not: the time-stationary void probability is
E[exp(-Lambda(0,t])], Jensen gives exp(-lambda* t) as a lower bound from stationarity alone, and
the source's Lemma 2.1 finishes. Attempt E0077-A002 carries the proof; the write-up is
Downloads/Probability_E0077_MMPP_scv_proved_2026-09-08.md. E0078 (the stochastic order) is not
settled by it.

## E0078 - refuted (added 2026-09-08, evening)

Conjecture 4.2 of the same source fails: a 24-state cyclic MMPP with a half-cycle block of rate
2/3 has P(T^pi > 19.75) = 0.01425 < P(T^alpha > 19.75) = 0.01543, and the periodic-intensity Cox
process violates the order provably. Attempt row E0078-A002; write-up in
Downloads/Probability_E0078_MMPP_stochastic_order_refuted_2026-09-08.md. The row's earlier status
note (the order not implied by the E0077 proof) is superseded by the refutation.

## E0061 - already answered in the literature, it seems (added 2026-09-08, evening)

Ganikhodjaev and Zanin, arXiv:1205.3841 (2012, in Russian), Theorem 1: the Volterra operator on
S^2 is non-ergodic if and only if a, b, c are nonzero and of one sign - the iff that Problem 4 asks
for, attributed by them to their 2004 note (Russian Math. Surveys 59:3, 571-572), whose title claims
only the necessary condition. The 2009 source posed the problem after that note, so the attribution
needs checking against the note itself before the row is closed; long-orbit numerics agree with YES
in every non-cyclic sign pattern (e0061.py). Attempt E0061-A002.

## E0046 - already settled in 2026, missed by the intake search (added 2026-09-08, evening)

The row kept Bandeira Open Problem 1.2 open on a 2026-09-08 search. Both halves were settled this
year: O. Hutnik, arXiv:2608.12151 (12 August 2026) proves the real increase quantitatively and cites his
companion preprint (2026) for the complex strict decrease, built on L. D. Abreu, Complex Anal. Oper.
Theory 20 (2026) 159; Abreu's 2016 claim (arXiv:1606.00494) was withdrawn in 2023. I proved the complex
half independently tonight (row E0046-A002, Lean E0046.lean) and found the literature afterwards - the
search should have come first. Searching the exact phrase "average singular value" with "Gaussian
random matrix" finds all three papers on the first page; the intake searched for "monotonicity of
singular values" and "moments of the Marchenko-Pastur law", which do not.

## Prior-art searches run 2026-09-08 evening on the night's settled items

After the E0046 lesson (proved, then found settled), the other results were searched the same
evening. E0077 (MMPP c^2 >= 1): the source, its withdrawn 2018 predecessor, and no later proof found
in two searches; the void-probability inequality for Cox processes may exist under another name.
E0078 (the order T^pi >=_st T^alpha): no later counterexample or proof found. E0105/E0104 (inertial
Boolean detection before an enemy point): only the source and a Berkeley talk abstract by the same
author ("Explicit formulas and open questions for detection times for the mobile Boolean model");
nothing later on the enemy-point law. P0245 (Aldous-Fill 6.30): no resolution found; the complete
graph value (n-1)H_{n-1} and Feige's (1-o(1)) n log n bound are the standard references. D0016/D0018:
the 2024 paper "Zeros of the Brownian Sheet" (arXiv:2405.20019) answers Khoshnevisan's Open Problem 4
(projections), not Open Problems 1 or 3. None of this certifies novelty; it records that the first
page of results holds no prior resolution, which is more than the E0046 row had.

## E0061 - the sufficiency was NOT in the 2004 note; proved here (added 2026-09-08, late evening)

Read the Ganikhodzhaev-Zanin 2004 note in full (Mathnet English text): its only theorem is the
necessary condition (cyclic case fails). The 2012 paper's Theorem 1 asserts the iff and cites the note
for it, which the note does not support. The sufficiency has an elementary proof (row E0061-A003,
memo Downloads/Probability_E0061_Volterra_ergodic_theorem_sufficiency_2026-09-08.md): a zero
coefficient makes two coordinates monotone; mixed nonzero signs make the tournament transitive, the
top species' coordinate increases and its convergent product forces the other two to zero. Every
non-cyclic trajectory converges, so Problem 4 is answered YES. Status of the row: proved (the earlier
"resolved in literature pending verification" is withdrawn).

## E0077 prior art and E0078 statement correction (2026-09-08 22:5x UTC)

The previous no-later-proof-found search for E0077 was wrong. Qi-Ming He, *Bounds on the mean and squared coefficient of variation of phase-type distributions*, J. Appl. Prob. 58(4), 880-889 (2021), DOI https://doi.org/10.1017/jpr.2021.18, Theorem 3.2 and section 4.1 prove the exact finite irreducible MMPP SCV bound, including nonreversible Q and equality iff the arrival rates are constant. The newly appended E0077 row is **resolved_in_literature and not admitted**. Earlier rows and A002 remain historical rederivations and must not count as newly solved open problems. The earlier general Cox extension additionally needs an almost-sure nonempty-process assumption.

E0078's original title/statement also incorrectly mentioned an exponential. The conjecture actually compares the time-stationary wait T^pi with the event-stationary wait T^alpha. A002 refutes the correct comparison. A003 records a separate exact-rational, strictly-positive-rate 12-state witness at t=19/2, with survival gap below -1/300000. No novelty or smallest-state assertion is made. He 2021 section 4.3 repeats the same order question.

Author-hosted source bytes, scope evidence and exact certificate are retained under audits/evidence/2026/09/08/overnight-mmpp-exact. Current state must be obtained by the latest row per problem_id, consistent with intake_tools.py, rather than by counting all historical JSONL lines.
