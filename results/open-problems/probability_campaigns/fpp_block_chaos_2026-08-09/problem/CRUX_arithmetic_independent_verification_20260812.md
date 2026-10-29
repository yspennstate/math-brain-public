# Independent arithmetic verification of CRUX Section 2 + 3b, and reconciliation of my iter65
# two-sided-wall self-referee against the file's Section 7. 2026-08-12.
# STATUS: VERIFICATION pass (re-derivation + internal-consistency check), NOT a domain referee.
# It confirms the ALGEBRA and LOGICAL STRUCTURE; it does NOT vouch for the analytic inputs
# (the C1/C2 chaos estimates, H1a, the Q^2 <~ n/log n bound, Newman-Piza's constant). chi = 1/3
# unmoved. No new claim of progress - this is checking existing work with my own eyes.

## What I re-derived, and the verdict (SOUND)

1. SECTION 2 HALVING (lines 5-9). From Var(X_{M^k n0}) <= (M/2)^k Var(X_{n0}) with k =
   log(N/n0)/log M: (M/2)^k = exp(k (log M - log 2)) = (N/n0)^{(log M - log 2)/log M} =
   (N/n0)^{1 - log2/logM}. So Var(X_N) <= Var(X_{n0}) (N/n0)^{1 - eps}, eps = log2/logM > 0.
   CORRECT.

2. THE rho REQUIREMENT (lines 14-16). eps <= D^2/(16 C2 V4), V4 ~ Q^4, so eps <=
   (D/Q^2)^2/(16 C2) = 1/(16 C2 rho^2) with rho = Q^2/D. CORRECT (the (Q^2/D)^2 = rho^2
   substitution is exact).

3. SECTION 3b SCALING (lines 50-55, 64-69). Q_s ~ s^alpha, true Var ~ s^{2 chi} =>
   rho_s = Q^2/Var = s^{2 alpha}/s^{2 chi} = s^{2(alpha - chi)}; then eps <~ rho^{-2} =
   s^{-4(alpha-chi)}. Constant-strength chaos (eps = const) survives iff -4(alpha-chi) >= 0
   i.e. alpha <= chi; H1a forces alpha >= chi; so alpha = chi exactly, admissible set (0, chi].
   CORRECT, and the file's scope correction (NOT the bare point 1/3; disjointness conditional
   on chi <= sqrt(2)-1 = 0.4142, stated with the hypothesis attached) is the right reading.

4. CORNER CRITERION (line 74-75). (3 alpha - 1)(alpha - 1) < 0: for alpha in (0,1) the second
   factor is negative, so the product is negative iff 3 alpha - 1 > 0, i.e. alpha > 1/3.
   CORRECT as an inequality; the file already notes the operative published-input number is the
   corrected 0.414, not this 1/3, so the disjointness bites only under chi <= 0.414.

No arithmetic or logical error found in these load-bearing steps. This is a CONFIRMATION
outcome, not an error-find.

## Reconciling my iter65 two-sided-wall self-referee against Section 7 (the honest part)

Section 7 of the CRUX file (lines 442-472) already isolates the SAME core obstruction my iter65
work reached: "rho has Var(X_n) in the DENOMINATOR ... unconditionally known is only Var >=
c log n (Newman-Piza)." So the fact that rho = O(1) needs a variance LOWER bound nobody has is
NOT my discovery - it is the campaign's already-named central wall (Section 2 line 25: "the
program lives or dies on closing rho_n").

Two things follow, both worth stating plainly:

(a) NO CONFLICT with the iter-68 resolution. Section 3b's header (lines 43-49) says "the iter-66
    challenge (Section 7) is REFUTED." But what iter-68 refuted is the NARROW challenge that 3b
    circularly IMPORTS the KPZ target (alpha=1/3): the answer is that the halving relates TRUE
    variances at two scales and n^{1-eps} is the telescoped OUTPUT, so alpha is nature's, not the
    theorem's. That refutation does NOT touch the rho-denominator obstruction, which remains the
    acknowledged wall. My iter65 note is about the wall's ITERABILITY (can a two-sided bootstrap
    supply the missing lower bound), not about importing the target - so it sits with the standing
    wall, not against the iter-68 refutation.

(b) MY iter65 CONTRIBUTION IS MODEST, AND I should not have framed it as more. Its genuine
    addition is narrow: it closes ONE proposed escape - the two-sided window-ratio bootstrap - by
    showing the upper leg's contraction rate rho_U is itself a tight-window (rho=O(1)) condition,
    so the bootstrap relocates rather than removes the circularity. That is a real but small
    increment on top of Section 7's already-stated denominator obstruction; the core insight was
    the file's, not mine. (Consistent with iter65's own retraction, which withdrew the stronger
    "escape" claim.)

## Honest scope / what this does NOT do
- Does NOT verify the analytic inputs: the C1/C2 chaos constants and their BSS-construction
  provenance, the H1a concentration hypothesis, the Q^2 <~ n/log n envelope upper bound, or the
  exact Newman-Piza c log n constant. Those are the domain referee's job and are flagged pending
  in the file itself.
- Does NOT move chi. It certifies that the ARITHMETIC from the stated inputs to the stated
  conclusions is correct, and that the file's careful hedging (conditional disjointness,
  alpha=chi not 1/3) is warranted. The wall stands exactly where the campaign already put it.

Related: CRUX_iteration_arithmetic.md Sections 2, 3b, 7; wall_two_sided_sandwich_note_20260812.md
+ its SELF_REFEREE (my iter65, reconciled here); memory fpp_wall_is_the_variance_ratio_three_routes.
