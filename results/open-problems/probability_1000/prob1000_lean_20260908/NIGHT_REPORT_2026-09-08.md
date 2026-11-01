# Open problems in probability: the night of 8 September 2026

One document for the morning. Everything below is on main in
`06_math_research/prob1000_lean_20260908` (scripts, Lean files, report copies) and in the intake
ledgers (`probability_1000_intake_D/E_20260908`, rows and CORRECTIONS.md); the write-ups are in
Downloads next to this file. Times are the machine's clock.

## Settled

**E0077, the folklore MMPP conjecture c^2 >= 1 (Asanjarani-Nazarathy Conjecture 4.1): PROVED.**
The time-stationary void probability of any Cox process is E[exp(-Lambda(0,t])], Jensen gives
exp(-lambda* t) as a lower bound from stationarity alone, integrate, and the source's own Palm
inversion lemma finishes. Equality iff Poisson, so an MMPP has c^2 = 1 iff all rates are equal,
which was their other unproved belief. The general Cox-process form they conjectured in a withdrawn
2018 note follows too. Lean: `E0077.lean`, six theorems, standard axioms only. Prior art: the source,
its withdrawn predecessor and two searches found no proof; the void-probability inequality itself may
be folklore elsewhere. Write-up `Probability_E0077_MMPP_scv_proved_2026-09-08.md`.

**E0078, the companion Conjecture 4.2 (T^pi >=_st T^alpha for every MMPP): REFUTED.** The order is
exactly "the hazard of the time-stationary interval never exceeds lambda*", which a Cox process with
a non-constant periodic intensity violates provably (a two-line monotonicity argument), and a 24-state
cyclic MMPP with a half-cycle block of rate 2/3 violates it by 8 percent (30-digit expm; 64 states
give 49 percent). Confirmed by simulating the point process itself: P(T^pi > 53) = 0.00538 against
P(T^alpha > 53) = 0.00794, a 29-sigma rejection, with c^2 = 2.56 on the same path. Robust to strictly
positive rates and backward jumps. The source's million random instances could not see it because
the mechanism needs a long nearly deterministic lap with small per-visit exposure. Write-up
`Probability_E0078_MMPP_stochastic_order_refuted_2026-09-08.md`.

**E0105 and E0104, the mobile Boolean survey's Open problems 3 and 2 (inertial case): SETTLED.** The
time to detect a ball before an enemy point is reached equals the ball's detection time on the event
that it comes first, so the whole problem is the joint law of two detection times; for straight-line
motion the detecting starting states are capsules, and the joint survival function is the Poisson
void probability of a union of two parallel capsules, explicit up to a one-dimensional lens integral.
Validated against a 60,000-configuration simulation of the particle system (P(S_K < S_a) 0.7670
against 0.7671 +- 0.0017). Write-up `Probability_E0105_inertial_Boolean_detection_before_a_point_2026-09-08.md`.

**D0016 and D0018, Khoshnevisan's Open Problems 1 and 3 on slices of the Brownian sheet: settled in
d = 3 and d = 5 by a Codex agent's proofs, audited here line by line.** At most two zeros per positive
slice in d = 3 and at most two disjoint double pairs per slice in d = 5, simultaneously in s. Both go
against the conjectures the source states ("I conjecture that the answer is no"). d = 2 and d = 4 are
the critical cases and stay open. Recorded in intake D CORRECTIONS.md with the packet path; the 2024
"Zeros of the Brownian Sheet" paper answers his Open Problem 4 only.

**E0060, Rozikov's Problem 3 (a transversal Volterra operator with a periodic itinerary): YES**, by
Zakharevich's three-state cyclic operator, whose itinerary is 1, 3, 2, 1, ... with geometrically
growing sojourns; the live question is dimension four, where a cyclic-type operator mixes three
routes (1,4,3,2,1,4,2,1 observed), consistent with Ganikhodjaev-Zanin 2012.

## Rediscovered or found in the literature

**E0046, Bandeira's Open Problem 1.2, complex half (alpha_C decreasing): proved here independently,
then found settled.** The route: the LUE half-integer moment partial sums obey
n^2 S_{n+1} = (2n^2 + 3/4) S_n - n^2 S_{n-1} (derived from the generating function
(1-t)^{-3/2} 2F1(-1/2,-1/2;1;t)), the ratio recursion rho_n = 2 + 3/(4n^2) - 1/rho_{n-1} then stays
below (1+1/n)^{3/2} by induction from (1+x)^{3/2} + (1-x)^{3/2} >= 2 + 3x^2/4. Lean `E0046.lean`
certifies the inequality and the induction. Prior art, searched only afterwards: O. Hutnik settled the
real half in August 2026 (arXiv:2608.12151) and the complex half in a 2026 companion preprint built on
Abreu's recurrence; Abreu's 2016 proof had been withdrawn. The ledger's status search had missed all
of it; the search phrase that finds it is "average singular value" "Gaussian random matrix". The
lesson is written down: search before proving, not after.

**E0061, Rozikov's Problem 4 (is the non-cyclic sign condition sufficient for the Volterra ergodic
theorem on S^2?): answered YES in Ganikhodjaev-Zanin, arXiv:1205.3841 (2012), Theorem 1**, which
states the iff and attributes it to their 2004 note; that note not yet read. Numerics agree.

## Attacked without a settlement

**E0018, Malrieu's Open question 3 (can the instability set in the switching rate be several
intervals?): no.** Reduced exactly to whether the exponent G(r) of a traceless planar pair can have two
humps above its two limits; 1,500 random pairs, about forty designed families and thirty optimizer
seeds over the four essential parameters found every curve unimodal, the only non-unimodal shape being
an endpoint dip that yields one unbounded interval. A side correction to Conjecture 4.3 (E0017): the
peak of G for the survey's own pair is at r = 0.230 with G = 0.1986, not r = 4.6; the value is right,
the location is roughly 1/r.

**E0045, the Mallat-Zeitouni basis conjecture:** a common-random-numbers search over rotations in
p = 3 found no basis beating the eigenbasis at d = 2 (an optimizer "gain" of 0.06 percent vanished on
fresh samples); the p = 4, 5 sweep was still running at the time of writing.

**P0245, Aldous-Fill Open Problem 6.30 (stationary cover time >= (n-1)H_{n-1}):** exact minimisation
over reversible chains on 3 and 4 states returns the complete graph's value exactly; on 5 states no
chain below it was found. Evidence for, no proof.

## Bookkeeping

Ledger rows appended for every item above (attempt ids ...-A002), statuses updated, corrections
recorded; brain memories filed for each settled or rediscovered result; eight pushes to main, each
scanned for secrets; the mesh carries a handoff to the Codex fleet agent with the open obligations.
Intake F (a further 100+ problems) is being built by a subagent; its first launch died on a network
error and was relaunched. Standing caveat on every "settled" line: prior art was checked by web search
only, the same evening, and the E0046 case shows what that is worth.
