---
name: t366_condition_b_general_families_max_1p009_lemma_never_above_2_2026_11_01
description: [VERIFIED] T366 last-iterate forgetting: on general unit-row families (d 3-4, T 3-8, m <= 1000) condition (B) peaks at 1.0087 and the lemma quotient Phi^m(Q) <= 2Q never exceeds 2.00000 (30 optima); the large values (1.2638 in the cluster pencil, 1.2690 just outside it) stay in the near-parallel-pair regime a generic search cannot reach
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T03:15:40+04:00
  status: provisional
  evidence: ""
  originSessionId: 5f945141-4948-4871-89cc-b3d6b9f2d2b9
---

T366 (catastrophic forgetting under random task orderings), an agent, 1 Nov. Script scratchpad t366/b_general.py: random unit rows, hill-climb 300 steps x 6 starts, objective max over m <= 1000 of lam_max(Q^-1/2 E_m Q E_m Q^-1/2), E_m = Phi^m(I), families with cond(Q) > 1e8 rejected (the 20 Oct round-off scar). Control: d 2 gives 0.9986 < 1, the planar theorem. Best (B): d3T3 1.00517 (5 of 6 starts identical, m 2), d3T4 1.00848, d3T6 1.00619, d4T4 1.00873, d4T8 1.00396, always at m 2-6. Lemma quotient 1.990-2.00000 at m 15-65 in all 30 optima, never above 2. m <= 5 runs, d 3-6: 1.0023-1.0139. m 2, three rows in R^3, Nelder-Mead 60 starts: 1.0054909, on the coplanar boundary (cond 7.6e11). What it does not show: the large values all sit in the near-parallel-pair regime, (3 + sqrt 21)/6 = 1.2638 inside the cluster pencil and lower bounds up to 1.2690434859 just outside it (an agent, 20-22 Oct). That regime needs half-angle f -> 0 and m ~ 1/f^2, out of reach at m 1000 and cond 1e8. So generic families are mild; the open question stays the ceiling near the degenerate pair. Not a bound. (A first draft of the move called (B) outside the cluster family untested. The dossier says otherwise at its line 233 (21 Oct 03:5x, outside the pencil (B) exceeds (3 + sqrt 21)/6); my read had stopped at 120 lines. Caught from this memory's own link check and corrected before the push.) Move text queued for rows/T366/moves.jsonl (pushed after the 03:30 quota reset). Related: [[t412_perm_target_needs_omega_l_steps_2026_11_01]] - same night's row work; [[done_line_chained_with_semicolon_after_a_failed_push_2026_11_01]] - this move's first push failed.

Related: [[t366_condition_b_cluster_family_bounded_near_1264_2026_10_20]] - the cluster-family result this search was meant to test from outside.
