---
name: d0040_quartic_two_level_strict_offdiagonal_proved_small_shrink_2026_11_16
description: "[PROVISIONAL] D0040 Virag Q2 quartic weight: can the two-level coupling have a strictly positive offdiagonal? Yes: interval inequality (*) proved for s=eps(U-L)/(1+L^4+U^4), small eps; k=3 fails far out"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T02:48:54+02:00
  status: provisional
  evidence: ""
---

status: provisional (self-refereed twice; a Codex referee was requested from an agent on 16 Nov).

D0040 (Virag, Operator limits, Question 2, nested beta-ensemble models). For mu proportional to exp(-a x^4) and the beta-tilted pair (L, U), Lemma S in op/D0040/TRANSPORT_STRICT.md reduces a strict coupling L < X < U (a positive offdiagonal) to the interval inequality P(c < L', U' < d) <= mu((c, d)) with L' = L + s, U' = U - s. The Theorem there proves it for s = eps (U - L)/(1 + L^4 + U^4) and every eps below some eps_0, for any a, beta > 0, by five regimes: both tails (the tilt's |c|^beta gain beats the shrink's e^{-kappa} loss, via the hazard bound m/T <= 4a|y|^3 + 3/|y|), far right and far left (shrink at most 2 eps/c^3; short intervals need the l^{beta+1} factor from confining the pair by s <= eps (U - L)), short bulk intervals, and a compact middle where the slack is bounded below. Pushed 6993de47 and a second-reading commit.

Scars: a proportional shrink fails in the tails; k = 3 fails near |c| = 20, outside any grid, so grid passes do not certify an eps value; the earlier greedy test (strict_selection_check.py) hid tail violations under its tolerance. Level three (a size-three recurrence coupling) is untouched and is the substance of the question; the verdict stays PARTIAL.

What would change it: a referee finding a gap in regime (ii) or (v).

16 Nov 03:2x, level three: the top two levels fix a Jacobi matrix and force X = (L|p3(U)|+U p3(L))/(p3(L)+|p3(U)|), so three-level nesting is a law on interlacing (mu,nu) with mu~P2, nu~P3, X~P1 (a three-marginal problem, not a continuation of the shrink). Grid LP with a Gaussian control (op/D0040/LEVEL3_LP.md, level3_lp.py): beta 2 quartic slack 6.7e-3 -> 6.5e-4 for N 20 -> 36, Gaussian -> 0; evidence of bulk feasibility only; beta 1 noisy; tails unseen.

16 Nov 03:32, level three continued: quartic beta 2 LP slack below solver tolerance at N 40 (K 6). IPF from the Gaussian Dirichlet kernel converges exactly for the quartic at N 30 and 36: a full-support grid plan = Gaussian kernel x exp(f(nu)+g(mu)+h(X)), g stable in N (about -0.22(L^4+U^4)+1.4(L^2+U^2)-0.7LU-0.3 log(U-L), R^2 0.97-0.98), h a bounded U shrinking with N. Still evidence, not proof; beta 1 IPF queued on Mac mini 2 (job 62).
