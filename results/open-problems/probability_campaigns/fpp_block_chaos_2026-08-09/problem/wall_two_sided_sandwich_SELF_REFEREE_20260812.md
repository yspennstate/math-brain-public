# SELF-REFEREE of wall_two_sided_sandwich_note_20260812.md (Addendum, "THE ESCAPE").
# 2026-08-12. STATUS: adversarial self-referee that CONFIRMS a flaw in my
# own earlier note and PARTIALLY RETRACTS it. This is my own referee, not an independent one -
# an independent referee is still owed. chi = 1/3 UNMOVED (as always).

## What I set out to break
The Addendum's load-bearing claim ("THE ESCAPE", note lines 93-100): tracking the window ratio
R(j) := U(j)/L(j) up the scales BREAKS the circularity that stops a one-directional variance
induction, "because neither bound is proved about itself; each is proved from the OTHER at the
previous scale." The note then (lines 102-120) treats the upper leg's per-step contraction
factor rho_U as an R-INDEPENDENT CONSTANT ("the refereed halving delivers a constant-factor
contraction; whether its constant is small enough ... [is] open").

## The break (confirmed, grounded in the note's own identity)
The note's own line 88: the halving consumes (L1')'s beta = U(j+1)/L(j). Two facts the note did
not combine:

  1. FPP variance is INCREASING in scale, so U(j+1) >= Var(X_{n_j}) (the upper bound at the
     bigger scale is at least the true variance at the smaller). Hence
         beta = U(j+1)/L(j)  >=  Var(X_{n_j}) / L(j).
  2. The refereed halving (Thread A, CRUX 3b/9.8) REQUIRES beta = O(1) to contract. That is its
     premise, not its conclusion.

Combine: the halving can be applied only when Var(X_{n_j})/L(j) = O(1), i.e. only when the
LOWER bound L(j) is already within a constant of the true variance. But the only UNCONDITIONAL
lower bound is L(j) >= c log n (the note's own line 28, quoting LOG 409). With that,
         beta  >~  Var(X_n) / log n  ~  n^{2chi} / log n  >>  1,
so the halving's O(1) premise FAILS AT THE START - not merely at large R, at the first step from
the unconditional window. rho_U is therefore NOT the R-independent constant the note treats it
as: it is < 1 only in the regime R = O(1) (tight window), and it is >= 1 (non-contracting)
precisely in the loose-window regime the bootstrap is supposed to escape from.

So the two-sided carry does NOT break the circularity. It RELOCATES it: from the one-directional
"assume R = O(1)" into the R-dependence of rho_U. For the lower leg to make beta = O(1) it would
have to lift L(j) from c log n up to ~ n^{2chi} (to within a constant of U) - which IS the whole
problem (pin the variance from below). "Each leg proved from the other" is, at the loose-window
start, "each leg needs the other's conclusion first." That is the same circularity LOG 409
identified, wearing a window.

## Steelman attempts (each fails, and failing sharpens the finding)
- "beta only needs to be O(g), and g = 2^{2chi} ~ 1.587 = O(1)." No: the CERTIFIABLE bound on
  beta is U(j+1)/L(j), which is >= Var(X_n)/L(j), not ~ g. The TRUE ratio is g = O(1); you
  cannot CERTIFY it without a tight window, which is what you lack.
- "Maintain R <= K up the scales instead of contracting a huge R(0) down." This exposes an
  INTERNAL INCONSISTENCY in the note: SETUP/ESCAPE read as maintain-window-up (inductive
  hypothesis R <= K), while the CORRECTION paragraph (lines 108-120) reads as contract-a-
  polynomial-R(0)-down over log n steps. Different arguments, different requirements. Under
  maintain-up the base case is fine (R = O(1) at n_0 = O(1)) but the STEP is exactly the
  circular one (needs L(j) ~ U(j) to fire the halving); under contract-down, rho_U cannot
  contract at large R. Either reading, the escape fails - and the note owes which one it means.
- "The lower leg rho_L compensates." rho_L is UNPROVEN (Thread B), and its own premise
  (anticoncentration GIVEN an upper bound U(j)) plausibly also weakens as U(j) loosens, so it
  likely degrades in the SAME large-R regime rather than compensating. Leaning on it is leaning
  on the unproven thing in the regime it is weakest.

## Disposition
RETRACTED: the Addendum's claim that tracking R(j) BREAKS the circularity / that the obstruction
is "reclassified as one missing contraction rate rho_L." It is not one missing rate; the upper
rate rho_U is itself R-dependent and non-contracting at the loose-window start, so BOTH legs are
entangled with the window they are trying to tighten.

SURVIVES (unchanged, still useful): (a) the SANDWICH FRAMING - chi as a two-legged fixed point,
s_block pinned to the global std-dev scale from both sides; (b) the identification of the lower
leg's content as restricted-min anticoncentration (Thread B). These are reorganizations of where
the difficulty sits; they never claimed to move chi and they still don't.

NET: the note is now honestly bounded. Its structural reorganization stands; its one claim to
"escape / break the circularity" does not, and is withdrawn. A future attempt should NOT treat
the two-sided bootstrap as circularity-free; the genuine open target is unchanged and stark -
lift the variance LOWER bound from c log n toward n^{2chi} by a means that does not itself
presume a tight window. chi = 1/3 exactly where it was.

Related: wall_two_sided_sandwich_note_20260812.md (the note refereed here; its "THE ESCAPE" and
"CORRECTION" are the target), D_lowerbound_blocktime_attempt_20260812.md (Thread B, the lower
leg), CRUX_iteration_arithmetic.md 3b+9.8 (the refereed halving whose beta = O(1) premise is the
crux), memory fpp_wall_is_the_variance_ratio_three_routes (the "does not start" finding this
confirms rather than escapes).
