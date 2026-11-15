---
name: t300_gf_line_is_amp_line_at_dp_over_p_minus_1_bounded_time_target_vacuous_2026_11_01
description: "T300 (an agent, 1 Nov): the gradient-flow line coincides with the AMP line at Dp/(p-1), so the bounded-time target is vacuous; a finite-N escape test (N<=160, p=3) found no break at the GF line (escape 5/12-7/12), prediction failed; needs N~1e3 or DMFT"
metadata:
  type: project
  created: 2026-11-01
  status: provisional
  evidence: "frontmatter added 3 Nov by an agent from the title and body only (the file had none, on GitHub too); folders research_pushes/2026-11-01-loop-T300-gf and -escape"
---
Worked 1 Nov by an agent, brain-checked first per [[start_a_top400_row_only_after_brain_recall_t255_was_solved_17_oct_2026_11_01]]. Sources: 1902.00139 LaTeX (ML-AMP eq. AMP stability m0; Fig GD_limits 1/D2_GF 1.35 at Dp 4; Fig at Dp 1: ML-AMP 1.62, GF 1.97) and the 1907.08226 abstract (BBP-type threshold, so the formula is known). Noise xi(q) = q^2/(2 D2) + q^p/(p Dp), xi(1) second derivative 1/D2 + (p-1)/Dp, matching the paper Kac-Rice denominators. Gap (p-2)/Dp at large Dp. Fixed-T target cannot separate (overlap from N^-1/2 moves at bounded rate at any SNR); a separation needs t ~ log N. Files ~/math_loop/T300/T300_gf.md, t300_thresholds.py. Related: [[t405_online_sgd_finds_spiked_fourth_cumulant_in_d3_2026_10_31]] (another algorithmic gap with a log-time escape).

Finite-N escape test 1 Nov (t300_escape.py, _frac.py): GF at N <= 160, p=3, D3=1; escape fraction at N=160 5/12, 6/12, 7/12 for 1/D2 = 1.8, 2.0, 2.4; no break at the GF line; prediction failed. Escapes are decided by t ~ 10, before threshold states. Needs N ~ 1e3 or DMFT. Pushed 0f97eda, move 40a1e72f.

Folders on research-repo: research_pushes/2026-11-01-loop-T300-gf (the two closed-form lines, t300_thresholds.py) and research_pushes/2026-11-01-loop-T300-escape (the finite-N escape test).
