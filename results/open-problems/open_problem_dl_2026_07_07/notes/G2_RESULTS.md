# G2 results: Lemma R + Claim P (the new final boss of the log front)
# Status: REFEREED. Claim P subsequently REFUTED (see CLAIMP_REFUTED.md). Verdicts:
# - LEMMA R: FIXABLE GAP — the pointwise hypothesis max_i |w(x_i)| <= B is FALSE
#   (referee's numerical refutation: max |g_lo| = 6.41 > B = 4 in a VALID net — the
#   peeled pieces a and g_hi can be pointwise large with cancellation keeping f bounded).
#   The L2 replacement ||w||_2 <= C B sqrt(n) is TRUE (adversarial ratio <= 0.36; <= 0.03
#   at d >= n) but UNPROVEN in-notes; correct fix: apply to g = f - a with ||f||_2 <=
#   B sqrt n + the affine bound ||a||_2 <= C(1+L*) sqrt n (needs ||v|| <= C L* FIRST —
#   stratified regime). MOOT for the route itself since Claim P is refuted, but the L2
#   form is the correct statement for any future use.
# - VBL: CORRECT (proof sound; vacuous at d >= n as self-diagnosed; the slope input in
#   the vacuousness computation legitimately cites stratified isolation — self-consistent
#   in the separated regime, non-circular).

## Lemma R (value bound -> rank-m projection; COMPLETE, one line)
After peeling g_hi (Claim 3, eps n/64, deterministic) and splitting the affine a, the
mesoscopic multiplier object is E_y sup <y, w> with w = (sum_c Q_c(<u_c, x_i>))_i, a
vector in col(R), R = the n x nu matrix of ReLU unit evaluations, nu <= m (band unit
budget), and max_i |w(x_i)| <= B := 2 + 2L* (value bound; g_hi corrections absorbed).
Then, for every y:   <y, w> <= B sqrt(n) ||P_R y||.
Proof: w in col(R); Cauchy-Schwarz; ||w||_2 <= B sqrt n. USES ONLY value bound + rank.
Trivial cap ||P_R y|| <= sqrt(min(nu, n)) ~ sqrt m is FATAL if attained at sqrt(mn)...
i.e. the content is that the capture is sqrt(m), not sqrt(n)-per-direction.

## Claim P (projection capture — THE remaining crux of the log front)
whp over x: E_y sup over ALL rank-<=m ReLU feature spans (any poles u in S^{d-1}, any
thresholds |t| <= t*) of ||P_R y|| <= C_0 sqrt(m), FLAT in n and d, LOG-FREE.
- m = 1 case = the dictionary bound (P4/Lemma D) — PROVED.
- E_y ||P_R y||^2 = rank <= m for FIXED R — the sup-before-E_y is the fight (same shape
  as the withdrawn visible-sector Theorem 3, but over ReLU spans, and with numerics
  decisively flat: adversarial matching-pursuit capture ~ 2 sqrt m at d = n and 4n,
  n = 300..2400; trivial cap sqrt(mn) = 110..310).
- COHERENCE REVERSAL: Claim P is hardest for SEPARATED directions (full rank), trivial
  for coherent (rank collapse) — opposite of G1; the coherent-stack core does not block
  this route.
- LOG-DISCIPLINE: a sqrt(log n) in Claim P re-enters the final rate as 1/polylog in the
  constant — the clean conjecture needs it log-free (the same discipline as sec:sharplog).
- Candidate proofs: (i) generic chaining over the joint feature ellipsoid using the
  Frobenius identity sum sigma_j(X)^2 = n (P4's device lifted to rank m); (ii) iterated/
  greedy dictionary argument (matching pursuit residuals); (iii) Maurey/empirical-
  process control of nu <= m columns.

## Content-zone closure (COMPLETE arithmetic, given Claim P)
W_g <= C_0 B sqrt(n m) = C_0 (2 + 2 c_0 eps sqrt T)(n/sqrt T). In the content zone
(T >= 2/(c_0 eps)^2; below it the sqrt-2 trivial floor closes the conjecture),
2/sqrt T <= sqrt 2 c_0 eps, so W_g <= C_0 (sqrt 2 + 2) c_0 eps n <= eps n/16 for
c_0 <= 1/(16 C_0 (sqrt 2 + 2)). Affine sector eps n/16 (needs ||v|| <= C L* — supplied
by inactive-region probes in the stratified setting: whp a random x has all
|<u_c, x>| < tau_0, where grad f = v). Plus contraction to remove the clip (P5 order:
peel first, then contract). => G2, hence (M), hence (per ASSEMBLY_MAP) the log-free PL
law at ALL widths m <= n/2 for d >= eps^{-2} log^C n — MODULO CLAIM P (+ the in-flight
stratified-isolation delivery for the v-probe and the general-activation transfer).

## VBL (variance-budget lemma — PROVED, correct, but vacuous at d >= n)
Statement: pairwise Gegenbauer coherence matrix R with ||R||_op = kappa < 1 and
sup_S |sum_c Q_c| <= B implies sum_c Var(Q_c) <= B^2/(1 - kappa). Proof via the addition
theorem + Cauchy-Schwarz per mode + the w^T R w bound. At d >= n separations give
kappa <= sqrt(m'/d) <= 1/2 => sum Var <= 2B^2.
VACUOUS at d >= n: rigidity P1 forces V_c <~ L*^2/d, so sum_c V_c <~ c_0^2 eps^2 << B^2
(numerics: ratio 3e-4) — the diagonal never binds; the adversary's energy is in the
CROSS-covariances. Lesson: variance is the wrong invariant; rank/projection is right.
VBL may still serve at moderate d (d <~ n c_0^2 eps^2) where variances are Theta(1).

## Numerics (seed 20260708, 5 scripts in agent scratchpad, < 2 min each)
VBL: holds under separation (ratio .04-.15 flat m' = 4..256), blows under coherence;
vacuousness at d >= n confirmed (3e-4). Joint width with value bound: ~ m^0.71, capped
vs uncoupled ~ m'. Projection capture: random dirs 0.96-1.01 sqrt m; adversarial ~ 2
sqrt m FLAT in d (n..4n) and n (300..2400). Per-cluster width sqrt n (P4-consistent).
