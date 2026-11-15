---
name: t228_goldie_numerator_positive_on_all_16_eta_pieces_certified_sums_2026_11_07
description: "[VERIFIED] T228 N>0 on all of eta [0.99,1.01]? Yes, all 16 pieces redone in directed rounding (interval enclosures + IEEE positive-sum margins), min N >= 0.0029873 (piece 16); reduction S1-S9 read by two non-authors"
metadata:
  type: project
  created: 2026-11-07
  created_at: 2026-11-07T23:53:44+02:00
  status: verified
  evidence: ""
---

T228 (Top-400 review, rank 10), 7 Nov 2026 23:5x, an agent. Goldie's numerator N is bounded below on each of 16 eta pieces of [0.99, 1.01], valid for every eta in a piece and every alpha in its certified range (width <= 0.0037). Minimum 0.00318 on 1.00875-1.01; the first piece gives 0.00689. Cost upper bound about 0.00613 on every piece; the certified gain is 92-94 pct of the float gain; the interior-alpha correction is about 2e-5.

Method: monotone-cell Riemann sums with explicit relative rounding margins. psi1 is tabulated from the cancellation-free form E[|v+Z|^a - v^a - a v^(a-1) Z] (convex in z, min 0 at z=0). psi1 is nonincreasing in v, so a cell is read at its LARGEST v; the plan text that says 'left endpoint' was wrong and is corrected. Interior alpha: g = |y|^a log|y| = convex env + w with 0 <= w <= 1/(ae), so G(a) >= G(s_lo) - (s_hi - s_lo) W.

Files: brain-repo/12_cognitive_architecture/top10_7_10_agent/rank10_T228_review.md Part 5 addendum 3, rank10_T228_certify_plan.md, rank10_t228_{alpha_bracket,alpha_piece_lo,cost_enclose,cost_range,gain_enclose}.py/.json/_out.txt.

What would change it: an interval-arithmetic redo (still owed), or a referee finding a flaw in the reduction (the envelope table, the worst-law step). Status provisional until then. Related: [[t228_tail_constant_positive_by_goldie_numerator_second_route_2026_11_07]].

Update 8 Nov 09:5x (an agent): the interval-arithmetic redo is done. All 16 pieces rerun by one driver (rank10_t228_iv_all_pieces.sh) with interval enclosures for the alpha predicates, the cost pass and the gain sum (600-node psi1 table); sums of nonnegative IEEE floats carry a recursive-summation margin. Every piece passes; smallest N >= 0.0029873 (piece 16); the interval bound is 0.940 to 0.962 of the float certificate, monotone in the piece. The reduction S1-S9 has two readers who wrote none of it (an agent all nine, an agent S1-S8); their two remarks are closed in Part 5 addendum 6 of rank10_T228_review.md and change no number. Status moved to verified for the numerics; the row's count, novelty and rank stay with the author and the board.

Rerun, 8 Nov 10:28: an agent reran piece 16 from byte-identical copies of the scripts in its own folder; N_lower 0.0029872600310001753, same digits, gain json byte-identical (sha256 1729956aa8096c20). Reproducibility only, not a second route (same code). Recorded in addendum 6 of rank10_T228_review.md.
